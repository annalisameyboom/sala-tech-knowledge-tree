# Contributing to the SALA Tech Knowledge Tree

This document is the operating system for the platform: who does what, how a tutorial gets from an idea to a Verified badge, and the conventions that keep the collection consistent. It is written to be adopted as-is by a team; adjust names and cadences to fit.

## 1. Roles

| Role | Who | Responsibility |
|---|---|---|
| **Contributor** | Any SALA faculty, sessional, or staff member | Creates the tutorial and submits it using the template |
| **Tutorial Team** | 2 or 3 faculty members (suggested: rotating annually) | Reviews submissions, verifies content, owns the tree structure (branches, levels, trails) |
| **Coordinator** | One member of the Tutorial Team, or a student assistant | Front door for non-GitHub submissions; converts form/email submissions into entries; runs the annual re-check |

One rule above all: **contributors write, the Tutorial Team verifies.** No one verifies their own tutorial.

## 2. How to contribute (for contributors)

You need to produce two things: your actual content (videos, text, files) hosted somewhere stable, and one JSON entry describing it.

1. **Host your content first.** Videos go on unlisted YouTube/Vimeo or UBC media hosting; files and datasets go on the shared drive or a repository. The platform stores links, never the media itself.
2. **Copy `tutorial-template.json`** and fill in every field. Field guide:
   - `id`: lowercase, hyphenated, starts with a branch hint, unique. Example: `bp-daylight-basics`, `gh-data-trees`. Never change an id after publication.
   - `category`: one of the branch ids. If your topic fits no branch, propose a new one to the Tutorial Team; do not invent one silently.
   - `level`: where it sits on the branch. Beginner = no prior knowledge beyond the branch entry point. Advanced = assumes the intermediate material.
   - `summary`: one or two sentences, written as "what students can do afterward", not a table of contents.
   - `steps`: the ordered parts of your tutorial, each with a link. Keep steps at 5 to 20 minutes each.
   - `prerequisites`: ids of existing tutorials students should finish first. Check the tree before writing this; it draws the connections.
   - `status`: always submit as `"draft"`. The Tutorial Team moves it forward.
3. **Submit** through either door:
   - **GitHub door**: append your entry to the `tutorials` array in `content.json` and open a pull request.
   - **Form door**: use the submission form on the site (or email the template to the Coordinator), who opens the PR for you.
4. **Respond to review feedback.** Small fixes are usually resolved in one round.

Time budget honesty: a good tutorial takes 3 to 6 hours to prepare beyond the recording itself. Budget for it; do not submit raw lecture captures.

## 3. How to review (for the Tutorial Team)

Pick up submissions within **two weeks**. Move the entry to `"in_review"` when you start. Approve only if all of the following pass:

- [ ] **Accuracy**: instructions work as written, on the software version students actually have
- [ ] **Version currency**: software version is named; nothing depends on deprecated features
- [ ] **Scope + level**: content matches the declared `level`; prerequisites are correct and sufficient
- [ ] **Licensing**: all shared files, datasets, fonts, and images are cleared for public distribution
- [ ] **Accessibility**: videos captioned, PDFs machine-readable, no essential information carried by color alone
- [ ] **Links**: every url resolves and is on stable hosting (no personal Dropbox links)
- [ ] **Fit**: no duplicate of an existing tutorial; if it overlaps, merge or link instead

On approval: set `status: "verified"`, fill `verifiedBy` and `updated` (year-month), merge. The PR approval itself is the verification record; the Git history is the audit trail.

If it does not pass, leave concrete feedback on the PR and keep the entry at `in_review`.

## 4. Status lifecycle

```
draft ──submit──▶ in_review ──approve──▶ verified
  ▲                  │  ▲                    │
  └────rework────────┘  └───annual check ────┘
                            (out of date)
```

- **draft**: contributor is preparing it. Not deployed publicly in production.
- **in_review**: with the Tutorial Team. Renders as a dashed box on the tree.
- **verified**: live, badged, with reviewer and date shown.
- **Annual re-check** (start of Term 1): the Coordinator walks every verified entry. Anything broken or version-stale drops to `in_review` and its contributor is notified. This single ritual is what keeps the platform from rotting.

## 5. Conventions

- **Titles**: Noun phrase, series numbered with Roman numerals: "Grasshopper I: Visual Programming Basics".
- **Branches own structure, contributors own content.** Adding or renaming branches, changing levels, and curating trails are Tutorial Team decisions, made at most once per term so the tree stays stable for students.
- **Courses** are owned by their instructors. Any instructor can define a course path through the shared pool, including other people's verified tutorials, without Tutorial Team approval; add a row to the courses sheet or a `courses` entry in content.json. The tutorials themselves still go through verification as usual, and the validator flags draft tutorials inside course paths.
- **English** for all platform content and metadata.
- **One entry per skill.** If your tutorial covers two separable skills, split it and connect them with `prerequisites`.

## 6. Repository shape (production)

```
repo/
├── index.html              the site (renders from content.json)
├── content.json            all entries: the single source of truth
├── tutorial-template.json  what contributors copy for a single entry
├── content-template.xlsx   faculty-facing spreadsheet (tutorials + courses sheets)
├── content-template.csv    tutorials sheet as CSV
├── courses-template.csv    courses sheet as CSV
├── sample-content.json     demo data for testing the interface
├── scripts/validate.py     schema + workflow validator (CI runs it on every PR)
├── scripts/csv_to_json.py  merges spreadsheet exports into content.json
├── CONTRIBUTING.md         this document
└── CONTENT-GUIDE.md        schema reference + deployment notes
```

Suggested GitHub settings: protect the main branch; require one Tutorial Team approval to merge; enable the PR template with the checklist from section 3. Merging deploys the site (GitHub Pages or Netlify). With that, the entire validation system runs on infrastructure that costs nothing and that the school already knows how to maintain.
