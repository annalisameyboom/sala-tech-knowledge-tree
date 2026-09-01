#!/usr/bin/env python3
"""Merge a spreadsheet export into content.json.

Usage:
  python3 scripts/csv_to_json.py sheet.csv content.json [--courses courses.csv]

Reads a CSV downloaded from the shared Google Sheet (made from
content-template.xlsx), converts each row to a tutorial entry, and merges
into content.json: rows are matched by id, new ids are added, existing ids
are updated. Rows whose id is empty or starts with '#' are skipped.
Writes content.json in place and prints a summary. Run scripts/validate.py
afterwards (CI runs it on the PR regardless).
"""
import csv
import datetime
import json
import sys

FIELDS = ["id", "title", "category", "level", "software", "format", "duration",
          "summary", "steps", "resources", "prerequisites", "contributor_name",
          "contributor_role", "status", "verified_by", "updated"]


def lines(cell):
    return [x.strip() for x in str(cell or "").split("\n") if x.strip()]


def commas(cell):
    return [x.strip() for x in str(cell or "").split(",") if x.strip()]


def row_to_tutorial(row):
    g = lambda k: str(row.get(k, "") or "").strip()
    steps = []
    for line in lines(g("steps")):
        parts = [p.strip() for p in line.split("|")]
        steps.append({"type": parts[0] if parts else "video",
                      "title": parts[1] if len(parts) > 1 else (parts[0] if parts else ""),
                      "url": parts[2] if len(parts) > 2 else ""})
    resources = []
    for line in lines(g("resources")):
        parts = [p.strip() for p in line.split("|")]
        resources.append({"label": parts[0] if parts else "",
                          "url": parts[1] if len(parts) > 1 else ""})
    return {
        "id": g("id"),
        "title": g("title"),
        "category": g("category"),
        "software": commas(g("software")),
        "level": g("level") or "beginner",
        "format": g("format") or "video series",
        "duration": g("duration") or "tbd",
        "summary": g("summary"),
        "steps": steps,
        "resources": resources,
        "contributor": {"name": g("contributor_name"), "role": g("contributor_role")},
        "prerequisites": commas(g("prerequisites")),
        "tags": commas(g("tags")),
        "chapter": int(g("chapter")) if g("chapter").isdigit() else None,
        "order": int(g("order")) if g("order").isdigit() else None,
        "status": g("status") or "draft",
        "verifiedBy": g("verified_by"),
        "updated": g("updated") or datetime.date.today().strftime("%Y-%m"),
    }


def row_to_course(row):
    g = lambda k: str(row.get(k, "") or "").strip()
    path = []
    for line in lines(g("path")):
        parts = line.split("|")
        path.append({"label": parts[0].strip() if parts else "",
                     "tutorialIds": commas(parts[1] if len(parts) > 1 else "")})
    return {"id": g("id"), "code": g("code"), "name": g("name"),
            "instructor": g("instructor"), "term": g("term"), "url": g("url"),
            "description": g("description"), "path": path}


def merge_courses(data, courses_csv):
    added, updated = 0, 0
    data.setdefault("courses", [])
    with open(courses_csv, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            row = {(k or "").strip().lower(): v for k, v in row.items()}
            cid = str(row.get("id", "") or "").strip()
            if not cid or cid.startswith("#"):
                continue
            entry = row_to_course(row)
            idx = next((i for i, c in enumerate(data["courses"]) if c["id"] == cid), None)
            if idx is None:
                data["courses"].append(entry)
                added += 1
            else:
                data["courses"][idx] = entry
                updated += 1
    return added, updated


def main():
    args = [a for a in sys.argv[1:] if a != "--courses"]
    courses_csv = None
    if "--courses" in sys.argv:
        i = sys.argv.index("--courses")
        if i + 1 < len(sys.argv):
            courses_csv = sys.argv[i + 1]
            args = [a for a in sys.argv[1:] if a not in ("--courses", courses_csv)]
    if len(args) != 2:
        print(__doc__)
        sys.exit(2)
    csv_path, json_path = args[0], args[1]

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    added, updated, skipped = 0, 0, 0
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            row = {(k or "").strip().lower(): v for k, v in row.items()}
            tid = str(row.get("id", "") or "").strip()
            if not tid or tid.startswith("#"):
                skipped += 1
                continue
            entry = row_to_tutorial(row)
            idx = next((i for i, t in enumerate(data["tutorials"]) if t["id"] == tid), None)
            if idx is None:
                data["tutorials"].append(entry)
                added += 1
            else:
                data["tutorials"][idx] = entry
                updated += 1

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"merged {csv_path} into {json_path}: {added} added, {updated} updated, {skipped} skipped")
    if courses_csv:
        ca, cu = merge_courses(data, courses_csv)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"merged {courses_csv}: {ca} courses added, {cu} updated")
    print("next: python3 scripts/validate.py " + json_path)


if __name__ == "__main__":
    main()
