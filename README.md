# Calculus: A Worked Review

An open, graduate-oriented review book with explicit notation, method selection, domain analysis,
and explicit intermediate calculations. Prior study of calculus is assumed.

**Alpha development — no stable release:** notation conventions, a comprehensive calculus methods reference,
28 problems in four mixed sets, 24 optional reference exercises, and a purple appendix of supporting tools. Material is
provided as-is; mathematical correctness is not guaranteed. See [the accuracy notice](DISCLAIMER.md).

## Read and preview locally

[Read the complete current book online](https://wa200508.github.io/Calculus_Workbook/generated/book.html)
on GitHub Pages. [Download the alpha PDF](https://github.com/wa200508/Calculus_Workbook/releases/tag/v0.4.0-alpha.5)
for a fixed, compiled edition. Each printed problem is followed immediately by
its worked solution, with hints and page references in a separate appendix.

Requirements: Node.js 22+, Python 3.10+, and pnpm 10.11.0.

```sh
pnpm install --frozen-lockfile
pnpm dev
```

Open the printed local URL. The site includes rendered math, local search, reading
routes, individual hints, complete solutions, dark mode, and source downloads.
After a manuscript edit, run `pnpm content` to refresh the generated pages.
The single-page edition is at `/generated/book.html`; its compiled HTML file is
`site/.vitepress/dist/generated/book.html` after `pnpm build`. Serve the built
site with `pnpm preview` so its styles and math assets load correctly.

The PDF workflow builds every manuscript checkpoint. Pushing an alpha version
tag such as `v0.4.0-alpha.5` also publishes the PDF as a GitHub prerelease.

```sh
pnpm check     # tests, production build, and internal-link/math checks
python3 scripts/check_advanced_math.py  # independent numeric spot checks
pnpm preview   # serve the production output
```

## Manuscript

- [Introduction](INTRODUCTION.md)
- [Notation standard](NOTATION_STANDARD.md)
- [Four-page quick reference](CHEAT_SHEET.md)
- [Introductory calculus methods reference](METHODS_REFERENCE.md)
- [Nonlinear scalar and parameter problems](DIFFERENTIATION_MIXED.md)
- [Fields and geometric constraints](DIFFERENTIATION_FIELDS.md)
- [Parameter integrals and geometric accumulation](INTEGRATION_MIXED.md)
- [Oscillatory and singular integrals](INTEGRATION_DOMAINS.md)
- [Tricks and identities appendix](TRICKS_APPENDIX.md)
- Optional reference exercises: [scalar derivatives](DIFFERENTIATION_SCALARS.md),
  [compositions](DIFFERENTIATION_RULES.md), [antiderivatives](INTEGRATION_SCALARS.md),
  and [coordinate changes](INTEGRATION_SUBSTITUTION.md)
- [Literature review](NOTATION_REVIEW.md)

These Markdown files are authoritative. The build generates site pages, downloads,
and the [standalone LaTeX book](calculus_workbook.tex). Regenerate that file instead
of editing it independently. [book-preamble.tex](scripts/book-preamble.tex) controls
its layout.

## Publishing and contribution

GitHub Actions checks pushes and pull requests. Successful `main` builds publish
to GitHub Pages after its source is set to GitHub Actions. Pull requests provide a
site artifact for review. A separate workflow produces the book and four-page reference PDFs, checks their
printable margins and reference-sheet length, and attaches both to alpha releases. The
repository name determines the Pages base path automatically.

The SSH remote is `git@github.com:wa200508/Calculus_Workbook.git`. Work is pushed
incrementally on `main`; no stable release has been tagged. See [development and publishing](docs/DEVELOPMENT.md),
[contributing](CONTRIBUTING.md), and [project status](PROJECT_STATUS.md).

## Licenses

Original educational content: **CC BY-SA 4.0**, allowing sharing and adaptation,
including commercial use, with attribution and ShareAlike under its terms.
Website code, scripts, configuration, and tests: **MIT**.

Read [content licensing](LICENSE-CONTENT.md), [MIT](LICENSE), the full
[CC BY-SA 4.0 text](LICENSES/CC-BY-SA-4.0.txt), and
[third-party notices](THIRD_PARTY_NOTICES.md). Both licenses include warranty
disclaimers. Linked literature retains its own rights.
