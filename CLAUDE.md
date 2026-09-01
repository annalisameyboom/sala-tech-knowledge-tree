# SALA Tech Knowledge Tree — instructions for Claude Code

## What this project is

A single-file public website mapping Grasshopper tutorials for SALA (UBC School of Architecture and Landscape Architecture) students. `index.html` is the entire site with content baked in; `content-gh.json` is the content source of truth. No build system, no dependencies, no backend.

## Task: publish to GitHub and enable Pages

The owner wants this pushed to GitHub (the `genenv` organization, same as genenv.github.io/des212-2026) and served via GitHub Pages.

1. Initialize git in this directory and make an initial commit (use the owner's local git identity; do not invent one):
   ```bash
   git init -b main
   git add -A
   git commit -m "SALA Tech Knowledge Tree: Grasshopper curriculum site"
   ```
2. Create the repository and push. Confirm the repository name with the owner first (suggested: `knowledge-tree`):
   ```bash
   gh repo create genenv/knowledge-tree --public --source=. --push
   ```
   If `gh` is not authenticated, run `gh auth login` and let the owner complete the browser step. Do not ask for or paste tokens directly.
3. Enable GitHub Pages from the main branch root:
   ```bash
   gh api -X POST repos/genenv/knowledge-tree/pages -f 'source[branch]=main' -f 'source[path]=/'
   ```
   If Pages already exists, use PUT on the same endpoint.
4. Verify, then report the URL to the owner:
   - `https://genenv.github.io/knowledge-tree/` returns the site (allow a minute for the first build)
   - The Tree view renders 35 nodes; clicking a node opens its tutorial page; PLAN/ELEV toggle works
   - The GitHub Actions run for `Validate content` is green

## Repository facts you need before changing anything

- `index.html` contains the content BAKED at the marker `let DATA = /*__CONTENT__*/...`. Editing `content-gh.json` alone does not change the site. To rebake after a content edit:
  ```bash
  python3 - <<'EOF'
  import json, re
  data = json.load(open('content-gh.json'))
  compact = json.dumps(data, separators=(',',':'), ensure_ascii=False)
  html = open('index.html').read()
  html = re.sub(r'let DATA = .*', lambda m: 'let DATA = /*__CONTENT__*/'+compact+'/*__END__*/;', html, count=1)
  open('index.html','w').write(html)
  EOF
  ```
- Always run `python3 scripts/validate.py content-gh.json` before committing content changes; it must PASS.
- Tutorial ids follow `gh-<chapter>-<order>` (e.g. `gh-4-2`). Every tutorial needs `chapter` and `order` integers; prerequisites must not form cycles.
- The site UI must stay English-only. No path notation like `{0;1}` in labels. No caption, legend, or statistics text on the Tree view. No verification or contributor credit lines in the visible UI.
- The Contribute page is intentionally absent from the UI for now; do not re-add it unless the owner asks.
- The six `status: "draft"` entries are intentional placeholders for missing curriculum sections; do not delete them.

## Scope discipline

Do exactly the publish task unless the owner asks for more. Do not refactor `index.html`, do not split it into multiple files, do not add frameworks or a build step.
