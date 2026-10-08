# Develop, review, and publish

Use Node.js 22+, Python 3.10+, and pnpm 10.11.0. Run `pnpm install --frozen-lockfile`
then `pnpm dev` and open the printed local URL. Theme edits refresh immediately.
After editing a root manuscript file, run `pnpm content` in another terminal;
the server picks up the generated pages.

Run `pnpm check` for tests, the production build, and internal link, asset, anchor,
and MathJax rendering-error checks. Use `pnpm preview` to serve that production
output. Inspect changed equations visually too; checks do not certify the book's
mathematical correctness.

## One manuscript, two presentations

Root Markdown manuscript files are authoritative. `scripts/build_content.py`
generates reference pages, practice pages with closed hints and solutions, offline
Markdown, and `calculus_workbook.tex`. The generated `.tex` remains tracked for
opening in a LaTeX editor. Keep content edits in Markdown and regenerate before
committing. `scripts/book-preamble.tex` controls the typeset layout.

The website shell lives in `site/`; styling and navigation are in
`site/.vitepress/`. Generated pages, dependency folders, and build products are
ignored by Git. Avoid committing credentials or local runtime folders.

## GitHub connection

The local repository uses `main`. No remote is configured yet. Once the intended
empty public repository URL is supplied, add it as `origin` and push the initial
history. Inspect and reconcile any existing remote history before pushing; do not
force-push over existing work.

Set GitHub **Settings → Pages → Build and deployment → Source: GitHub Actions**.
The `site.yml` workflow builds and deploys through GitHub's Pages artifact/actions,
without a personal access token or hosting secret. The repository name determines
the base path, including account-root Pages repositories. Use `SITE_BASE=/path/`
for another deployment path.

Successful pushes to `main` build, check, and deploy. Pull requests build and check
without production deployment. Every successful build provides a `reading-site`
artifact. To review one, extract it and serve it with `python3 -m http.server 8080`.
If built for `/repository-name/`, put the extracted files inside a directory named
`repository-name`, serve its parent, and open that path in the browser.

The separate `pdf.yml` workflow regenerates the manuscript, installs the TeX
compiler, builds the PDF, and provides a `calculus-workbook-pdf` artifact. Public
PDF downloads will be added after a successful workflow run and layout review.

## Routine work

1. Change the manuscript or website source.
2. Regenerate and review the local site.
3. Run `pnpm check`; inspect the diff, including regenerated LaTeX.
4. Commit a meaningful checkpoint and push it.
5. Review CI and the published site or pull-request artifact.

Keep the lockfile committed and update dependencies deliberately. Track
corrections by problem ID. Include the working folder in an independent backup:
Git saves committed work; the remote saves pushed history.

Codex may require escalation to write `.git` even when manuscript files are
writable. This is a sandbox metadata restriction, not a special Git setup.

Before a milestone release, review mathematics, assumptions, accessibility,
asset licenses, and PDF layout. Continue to label the current book a developing
edition until those reviews are complete.
