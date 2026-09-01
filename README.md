# SALA Tech Knowledge Tree

A public, faculty-contributed, faculty-verified map of design-technology tutorials for architecture and landscape architecture students. Current scope: Grasshopper (8 chapters, 35 sections).

**Live site:** enable GitHub Pages on this repository (Settings → Pages → Deploy from a branch → main, root) and the tree is served at the repository's Pages URL.

## What is in here

- `index.html` — the entire site, one file, with the current content baked in. PLAN and ELEV views of the knowledge tree, per-tutorial pages, and course paths.
- `content-gh.json` — the source of truth: every tutorial, its chapter and order, prerequisites, resources, and status.
- `GRASSHOPPER-CURRICULUM.md` — the knowledge spine the tree is built from, with sections still lacking a dedicated resource marked as gaps.
- `content-template.xlsx` / `.csv` — for contributing tutorials in bulk from a spreadsheet.
- `scripts/validate.py` — content validator (unique ids, no prerequisite cycles, valid chapters). Runs automatically on every pull request.
- `CONTRIBUTING.md`, `CONTENT-GUIDE.md`, `DESIGN-BRIEF.md` — governance, authoring guide, and design rationale.

## Contributing a tutorial

The public contribution page is not enabled yet. For now, send materials to the coordinator or fill in the spreadsheet template; entries land in `content-gh.json` through a pull request, reviewed by a tutorial-team member other than the contributor. Sections marked as planned on the tree are open slots looking for a contributor.

## Editing content

`content-gh.json` is baked into `index.html` at the marker `let DATA = /*__CONTENT__*/`. After editing the JSON, replace the baked blob with the new compact JSON (any collaborator can do this with the one-line Python in `CONTENT-GUIDE.md`), or open the site and use Load JSON to preview changes before committing.
