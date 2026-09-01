# SALA Tech Knowledge Tree: Content Guide

How to populate, review, and eventually deploy the tutorial platform. The mockup (`index.html`) renders everything from a single data file, `content.json`. Populating the platform means editing that file.

## 1. The data model

Four top-level blocks:

| Block | What it holds |
|---|---|
| `site` | Name, subtitle, school, and the validation statement shown to students |
| `categories` | The branches of the tree (Foundations, Computational, AI Methods, Building Performance, Fabrication, Site + Data, Representation). Each has an `id`, display `name`, `color`, and a short `blurb`. Add or rename freely; the tree redraws itself. |
| `tutorials` | One entry per tutorial. This is where almost all content lives. |
| `courses` | Instructor-owned paths through the shared pool. Each course has `id`, `code`, `name`, `instructor`, `term`, `url`, `description`, and a `path`: an ordered list of sections (`label` + `tutorialIds`), typically modules or weeks. The same tutorial can appear in many courses. |

### A tutorial entry

```json
{
  "id": "site-gis",
  "title": "QGIS for Site Analysis",
  "category": "site-data",
  "software": ["QGIS"],
  "level": "beginner",
  "format": "video series",
  "duration": "2 hr",
  "summary": "One or two sentences on what students can do afterward.",
  "steps": [
    { "title": "Projections and coordinate systems", "type": "video", "url": "https://..." }
  ],
  "resources": [
    { "label": "QGIS starter project", "url": "https://..." }
  ],
  "contributor": { "name": "R. Deol", "role": "Sessional, Landscape Architecture" },
  "prerequisites": ["rhino-1"],
  "status": "verified",
  "verifiedBy": "Faculty tutorial team",
  "updated": "2026-05",
  "map": { "x": 700, "y": 620 }
}
```

Field notes:

- `id`: lowercase, hyphenated, unique. Used by `prerequisites` and `trails`, so never rename an id without updating references.
- `steps.type`: `video` or `text`. `url` points at the hosted content (YouTube/Vimeo unlisted links, a PDF on the shared drive, a page on genenv or a repo). The mockup leaves urls empty; production links them out or embeds them.
- `prerequisites`: ids of tutorials students should finish first. Same-branch prerequisites draw as solid tree links, cross-branch ones as dashed links, and both feed the "Before this" and "Leads to" chips. Hovering a skill on the tree highlights its full prerequisite path back to the root.
- `status`: `draft`, `in_review`, or `verified`. Anything not `verified` renders as a dashed box on the tree and carries a warning in its detail panel. In production you would simply not deploy drafts publicly.
- Tree position is fully automatic: category decides the branch (row band), `level` decides the column (beginner, intermediate, advanced), and prerequisites draw the connections. There are no coordinates to maintain.
- `updated`: year-month of the last faculty check. Surface this honestly; it is what keeps the platform from quietly rotting the way most tutorial collections do.

## 2. Populating content in the mockup

The shipped `content.json` is a minimal template: seven empty branches and one example entry (`example-entry`) showing the format. Contributors copy `tutorial-template.json` for new entries; the team process is defined in `CONTRIBUTING.md`. To preview a fully populated interface, load `sample-content.json` with the Load button.

Three ways, all working today:

1. Edit `content.json` directly and reopen `index.html` after re-injecting (see below), or
2. Open the site, go to **Contribute**, use **Load content.json** to render any edited file instantly, and **Download current content.json** to save the result, or
3. Use the **Submission form**: entries are added as drafts in the pipeline; download the JSON to keep them.

The HTML file carries an embedded copy of the content so it works as a single file with no server. To bake an updated `content.json` back into `index.html`, replace the JSON between the `/*__CONTENT__*/` and `/*__END__*/` markers in the script block, or run:

```bash
python3 - <<'EOF'
import json, re
data = json.dumps(json.load(open('content.json')), separators=(',', ':'))
html = open('index.html').read()
html = re.sub(r'/\*__CONTENT__\*/.*?/\*__END__\*/', data, html, count=1, flags=re.S)
open('index.html', 'w').write(html)
EOF
```

(For quick testing you can skip baking entirely and just use the Load button.)

## 3. The validation workflow

The interface encodes a three-stage pipeline that matches how a faculty team actually works:

1. **Submit** (contributor). Any faculty, sessional, or staff member records or writes the tutorial and submits it. Entry enters as `draft`.
2. **Faculty review** (tutorial team). Move to `in_review` when the team picks it up. Suggested review checklist: technical accuracy, current software version, licensing of shared files and datasets, captions on videos, and whether prerequisites are set correctly.
3. **Publish** (tutorial team). Set `status: "verified"`, fill `verifiedBy` and `updated`. Annual re-check: anything older than a year drops back to `in_review` until refreshed.

## 4. Recommended production path

When you move past the mockup, the cleanest architecture for a faculty-maintained public platform is a static site with content in a Git repository:

- **Content as files in GitHub.** Either keep the single `content.json`, or split into one markdown file per tutorial with YAML frontmatter (better for many contributors; no merge conflicts on one giant file).
- **Pull requests as the validation step.** Faculty submit tutorials as PRs; the tutorial team's PR approval literally is the verification. The Git history becomes the audit trail of who verified what and when. This maps one-to-one onto the pipeline above and costs nothing to run.
- **Static build and free hosting.** Astro, Eleventy, or plain Vite reading the content files; deploy on GitHub Pages or Netlify on merge. No database, no server maintenance, no login system to babysit. This is also why the GSAPP predecessor aged badly: it was a Meteor app with a MongoDB backend that needed ongoing care.
- **Video hosting stays external.** Unlisted YouTube/Vimeo or a UBC media service; the platform only stores links. Keeps the repo light and the videos replaceable.
- **A Google Form or the site form as the low-friction front door** for contributors who will not touch GitHub; a student assistant or team member turns submissions into PRs.

## 5. What the mockup demonstrates

- **Tree**: the whole collection as one legible hierarchy. Read left to right: root, branch (category), then skills in level columns from beginner to advanced. Solid links are branch structure, dashed links are cross-branch prerequisites, dashed boxes are unverified. Hover any skill to trace its path.
- **Index**: filterable browse by category, level, software, status, plus global search.
- **Trails**: faculty-curated sequences with verification counts.
- **Contribute**: the workflow explanation, live review pipeline sorted by status, working submission form, and JSON load/download: the content system itself.
- **Detail panel**: steps, resources, prerequisites both directions, trail membership, and an explicit verification statement with the review date.
