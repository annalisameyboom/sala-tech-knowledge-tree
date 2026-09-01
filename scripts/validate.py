#!/usr/bin/env python3
"""Validate content.json for the SALA Tech Knowledge Tree.

Run locally:  python3 scripts/validate.py content.json
CI runs this on every pull request; a merge is blocked until it passes.

Checks:
  structure   required top-level keys and field types
  ids         format (lowercase-hyphenated) and uniqueness
  references  categories, levels, statuses, prerequisites, trail members
  cycles      prerequisite graph must be acyclic
  courses     course paths reference real tutorials; drafts flagged
  workflow    verified entries need verifiedBy + updated; drafts cannot be on trails
  hygiene     warnings for empty urls on verified entries, long summaries
Exit code 0 = pass (warnings allowed), 1 = errors found.
"""
import json
import re
import sys

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED_TOP = ["site", "categories", "levels", "statuses", "tutorials"]
REQUIRED_TUT = ["id", "title", "category", "level", "summary", "contributor", "status"]

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def validate(data):
    for key in REQUIRED_TOP:
        if key not in data:
            err(f"missing top-level key: {key}")
    if errors:
        return

    cat_ids = [c.get("id") for c in data["categories"]]
    if len(cat_ids) != len(set(cat_ids)):
        err("duplicate category ids")
    levels = data["levels"]
    statuses = set(data["statuses"].keys())

    tut_ids = []
    for t in data["tutorials"]:
        tid = t.get("id", "<missing id>")
        for f in REQUIRED_TUT:
            if not t.get(f):
                err(f"{tid}: missing required field '{f}'")
        if not ID_RE.match(str(t.get("id", ""))):
            err(f"{tid}: id must be lowercase-hyphenated (a-z, 0-9, -)")
        if tid in tut_ids:
            err(f"{tid}: duplicate id")
        tut_ids.append(tid)
        if t.get("category") not in cat_ids:
            err(f"{tid}: unknown category '{t.get('category')}'")
        if t.get("level") not in levels:
            err(f"{tid}: unknown level '{t.get('level')}' (allowed: {', '.join(levels)})")
        if t.get("status") not in statuses:
            err(f"{tid}: unknown status '{t.get('status')}'")
        if t.get("status") == "verified":
            if not t.get("verifiedBy"):
                err(f"{tid}: verified but verifiedBy is empty")
            if not t.get("updated"):
                err(f"{tid}: verified but updated is empty")
            for i, s in enumerate(t.get("steps", [])):
                if not s.get("url"):
                    warn(f"{tid}: verified but step {i + 1} ('{s.get('title', '')}') has no url")
        if len(t.get("summary", "")) > 400:
            warn(f"{tid}: summary is over 400 characters; keep it to 1-2 sentences")
        for s in t.get("steps", []):
            if s.get("type") not in ("video", "text"):
                err(f"{tid}: step type must be 'video' or 'text', got '{s.get('type')}'")

    id_set = set(tut_ids)
    prereq = {}
    for t in data["tutorials"]:
        tid = t["id"]
        prereq[tid] = t.get("prerequisites", [])
        for p in prereq[tid]:
            if p not in id_set:
                err(f"{tid}: prerequisite '{p}' does not exist")
            if p == tid:
                err(f"{tid}: lists itself as a prerequisite")

    # cycle detection (DFS, three-color)
    WHITE, GREY, BLACK = 0, 1, 2
    color = {tid: WHITE for tid in id_set}

    def dfs(node, path):
        color[node] = GREY
        for p in prereq.get(node, []):
            if p not in id_set:
                continue
            if color[p] == GREY:
                err("prerequisite cycle: " + " -> ".join(path + [p]))
                continue
            if color[p] == WHITE:
                dfs(p, path + [p])
        color[node] = BLACK

    for tid in id_set:
        if color[tid] == WHITE:
            dfs(tid, [tid])

    by_id = {t["id"]: t for t in data["tutorials"]}
    trail_ids = []  # legacy: validated only if present
    for tr in data.get("trails", []):
        trid = tr.get("id", "<trail>")
        if trid in trail_ids:
            err(f"trail {trid}: duplicate id")
        trail_ids.append(trid)
        members = tr.get("tutorialIds", [])
        if len(members) < 2:
            warn(f"trail {trid}: fewer than 2 stops")
        for m in members:
            if m not in id_set:
                err(f"trail {trid}: references unknown tutorial '{m}'")
            elif by_id[m].get("status") == "draft":
                err(f"trail {trid}: contains draft tutorial '{m}' (publish trails with verified stops only)")
            elif by_id[m].get("status") != "verified":
                warn(f"trail {trid}: stop '{m}' is not verified yet")


def validate_courses(data, id_set, by_id):
    course_ids = []
    for c in data.get("courses", []):
        cid = c.get("id", "<course>")
        if cid in course_ids:
            err(f"course {cid}: duplicate id")
        course_ids.append(cid)
        if not c.get("name"):
            err(f"course {cid}: missing name")
        members = c.get("tutorialIds", [])
        if not members:
            warn(f"course {cid}: has no tutorials yet")
        for m in members:
            if m not in id_set:
                err(f"course {cid}: references unknown tutorial '{m}'")
            elif by_id[m].get("status") == "draft":
                warn(f"course {cid}: includes draft tutorial '{m}'")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "content.json"
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"FAIL: {path} not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"FAIL: {path} is not valid JSON: {e}")
        sys.exit(1)

    validate(data)
    if not errors:
        id_set = {t["id"] for t in data["tutorials"]}
        by_id = {t["id"]: t for t in data["tutorials"]}
        validate_courses(data, id_set, by_id)

    n = len(data.get("tutorials", []))
    print(f"checked {path}: {n} tutorials, {len(data.get('categories', []))} branches, {len(data.get('courses', []))} courses")
    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}")
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        sys.exit(1)
    print(f"PASS: 0 errors, {len(warnings)} warning(s)")


if __name__ == "__main__":
    main()
