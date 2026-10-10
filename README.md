# Calculus: A Worked Review

An open review book with explicit notation, visible algebra, complete worked
solutions, and help one step at a time.

**Alpha development — no stable release:** notation standard, 24 worked problems across four calculus chapters,
and a purple appendix of supporting tools. Full chapters are still being written. Material is
provided as-is; mathematical correctness is not guaranteed. See [the accuracy notice](DISCLAIMER.md).

## Read and preview locally

[Read the complete current book online](https://wa200508.github.io/Calculus_Workbook/generated/book.html)
on GitHub Pages. [Download the alpha PDF](https://github.com/wa200508/Calculus_Workbook/releases/tag/v0.2.0-alpha.4)
for a fixed, compiled edition of all material written so far.

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
tag such as `v0.2.0-alpha.4` also publishes the PDF as a GitHub prerelease.

```sh
pnpm check     # tests, production build, and internal-link/math checks
pnpm preview   # serve the production output
```

## Manuscript

- [Notation standard](NOTATION_STANDARD.md)
- [Scalar differentiation chapter](DIFFERENTIATION_SCALARS.md)
- [Products, quotients, and compositions](DIFFERENTIATION_RULES.md)
- [Scalar antiderivatives and definite integrals](INTEGRATION_SCALARS.md)
- [Substitution](INTEGRATION_SUBSTITUTION.md)
- [Tricks and identities appendix](TRICKS_APPENDIX.md)
- [Literature review](NOTATION_REVIEW.md)

These Markdown files are authoritative. The build generates site pages, downloads,
and the [standalone LaTeX book](calculus_workbook.tex). Regenerate that file instead
of editing it independently. [book-preamble.tex](scripts/book-preamble.tex) controls
its layout.

## Publishing and contribution

GitHub Actions checks pushes and pull requests. Successful `main` builds publish
to GitHub Pages after its source is set to GitHub Actions. Pull requests provide a
site artifact for review. A separate workflow produces a PDF artifact. The
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
