# SALA Tech Knowledge Tree: Design Brief

A public tutorial platform for UBC SALA (architecture + landscape architecture students). Faculty contribute tutorials into one shared pool; a faculty tutorial team verifies everything; each course instructor defines their own path through the pool. Precedent: GSAPP Skill Trails, modernized.

Name: **SALA Tech Knowledge Tree**. In the wordmark, "Tech Knowledge" always reads as one unit (never split so that "Tech" pairs with "Tree").

## Core model

- **Tutorials** are the atomic unit. One shared pool; every tutorial belongs to exactly one branch (category) and one level.
- **Branches** (7): Foundations, Computational, AI Methods, Building Performance, Fabrication, Site + Data, Representation.
- **Levels** (3): beginner, intermediate, advanced. Beginner sits nearest the trunk; advanced at branch tips.
- **Prerequisites** link tutorials into a DAG (no cycles). They can cross branches.
- **Facets**: every tutorial is classifiable along multiple dimensions at once (branch, level, software, topic tags, course, format, contributor). No single hierarchy is privileged; views are projections of the database.
- **Courses** are instructor-owned ordered paths through the pool. The same tutorial can serve many courses.
- **Verification status** per tutorial: draft, in_review, verified. Only the tutorial team sets verified; unverified content is visually distinct everywhere.
- No "trails" concept. Removed.

## Views

**1. Tree (default landing view): a composable data tree.** The pool is a database; the tree is a query. A Grasshopper-data-tree-style radial diagram: root {0} at the center, ring arcs for groups with path chips ({0;1}, {0;1;2}), tutorials as leaves on the outer ring, data stored at the leaves. The user composes the path structure from facets: branch, level, software, topic (tags), course, format, contributor (e.g. PATH = {branch; level} or {software} or {course}); the tree reorganizes live. A tutorial with multiple values (two softwares, two courses) appears on multiple branches; hovering highlights all its instances. Prerequisite links draw as dashed arcs bundled through the center (the cloud-graph layer); hovering a leaf traces its full prerequisite chain. Checked-in leaves bloom; unverified leaves render dashed. Click opens the tutorial's page.

**2. Flowchart (alternative view).** The same data as a horizontal structured diagram for wayfinding: root → branch nodes → level columns (beginner / intermediate / advanced), prerequisite edges drawn between tutorials (cross-branch prerequisites visually distinct). Hovering a tutorial highlights its full prerequisite path back to the root. Layout is computed from the data (category + level + prerequisites); no manual coordinates.

**3. Index.** Filterable browse of the whole pool: filter by branch, level, software, verification status; global search across titles, summaries, software. Cards show branch color, title, level, duration, contributor, status badge, and personal check-in state.

**4. Courses.** One card per course: course code, name, instructor, term, link to the course site, short description, personal progress (n of m checked in, progress bar), then the tutorials as a single flat ordered sequence (numbered 1 to n, no module subdivision). Each stop shows check-in state and links to the tutorial page.

## Tutorial pages

Every tutorial has its own dedicated page with a unique, shareable URL (e.g. `#/tutorial/<id>` or `/tutorial/<id>`), reachable from all four views. A page shows: branch + status badge, title, summary, metadata (level, duration, format, software, contributor, last-reviewed date), ordered steps (each a video or text link out to hosted content), resources (downloadable files, external links), prerequisites (linked, both directions: "before this" and "leads to"), courses that include it, a verification statement, and the check-in button. Browser back/forward and direct linking must work.

## Check-in (student progress)

Students mark tutorials complete from the tutorial page; completion date recorded. Stored per browser (localStorage), no accounts, no server. Progress surfaces everywhere: blooming leaves on the tree, check marks in the flowchart and index, per-course progress bars, and a global counter in the header that links to the tree.

## Content system + governance (keep as is)

- The entire site renders from one `content.json`. No database.
- Faculty author in a shared spreadsheet (tutorials sheet + courses sheet); a coordinator converts CSV exports into content.json (site import button or `scripts/csv_to_json.py`).
- Lifecycle: contributor submits as draft → tutorial team reviews (accuracy, software version, licensing, accessibility, links, fit) → verified with reviewer + date → annual re-check.
- GitHub repo with PR-approval-as-verification, CI schema validator (`scripts/validate.py`), CODEOWNERS, branch protection. Already built; the redesign only needs to render from the same content.json.

## Architecture: one file per tutorial

Each tutorial is a standalone HTML page in `tutorials/<id>.html`. The file embeds one structured metadata block; the body is free-form HTML (embedded videos, images, interactive demos, anything).

```html
<script type="application/json" id="tutorial-meta">
  { ...exact tutorial schema below... }
</script>
<!-- free-form page body follows -->
```

`content.json` becomes a build artifact, never hand-edited: `scripts/build.py` scans all tutorial files, extracts and validates the meta blocks, and emits content.json for the Tree interface to render. The Tree, flowchart, index, and courses read only the compiled metadata; clicking through goes to the tutorial's own file (which is also its shareable URL, for free, on any static host).

Why this shape: it is AI-manageable by design. An agent editing one tutorial touches one bounded file; agents can generate or update tutorials in parallel with zero merge conflicts; a repo-level CLAUDE.md states the file contract (valid meta block + body) and CI enforces it, so generated content that breaks the contract cannot merge. One PR = one file = one review.

Shared `tutorial.css` plus a page template keep pages visually coherent; some per-author variation in the body is acceptable as long as the meta block validates.

## Data schema (per tutorial / per course)

```json
{
  "id": "gh-hello-grasshopper",
  "title": "...", "category": "computational", "level": "beginner",
  "software": ["Rhino", "Grasshopper"], "tags": ["parametric design"],
  "format": "video + files", "duration": "4 hr",
  "summary": "1-2 sentences",
  "steps": [{ "type": "video|text", "title": "...", "url": "..." }],
  "resources": [{ "label": "...", "url": "..." }],
  "contributor": { "name": "...", "role": "..." },
  "prerequisites": ["other-id"],
  "status": "draft|in_review|verified", "verifiedBy": "...", "updated": "YYYY-MM"
}
```

```json
{
  "id": "des212", "code": "DES 212", "name": "Design Media II",
  "instructor": "Xun Liu", "term": "2025W2", "url": "https://...",
  "description": "...",
  "tutorialIds": ["ordered", "flat", "list"]
}
```

## Constraints

- All interface text, content, and code in English.
- Public site, no login. Works as a static build (GitHub Pages / Netlify).
- Responsive down to mobile; keyboard accessible; reduced motion respected.
- Visual direction is open for the redesign, with two fixed points: the growing tree is the landing identity, and verification status must stay legible at a glance.

## Real content available

`content-des212.json` contains the first real population: 9 tutorials from DES 212 (2025W2) across 4 branches with real video links, files, and prerequisites, plus the DES 212 course path. Use it as the working dataset while designing.
