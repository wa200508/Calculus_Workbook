# Project status

Updated October 9, 2026. Stage: alpha development; no stable release.

October 9 publishing update: a complete single-page HTML edition is generated
at `site/.vitepress/dist/generated/book.html`. The latest fixed PDF edition is
published through GitHub Releases
and saved locally as `build/calculus_workbook.pdf`. Alpha version tags build and
publish a compiled PDF through GitHub Releases. GitHub Pages is enabled with
GitHub Actions and the complete book is live at
https://wa200508.github.io/Calculus_Workbook/generated/book.html.

## Established decisions

- Explicit review text with complete worked solutions and one-step-at-a-time tutoring.
- Notation standard 0.2: literature-informed Leibniz operators, round operands, full arguments, and explicit types/dependencies.
- Root Markdown manuscript generates the site and LaTeX book.
- Educational content: CC BY-SA 4.0. Software: MIT. Correctness is not guaranteed.
- Static VitePress site, local search, build-time MathJax, and practice pages.
- SSH remote: `git@github.com:wa200508/Calculus_Workbook.git`; incremental pushes on `main`.

October 9 editorial update: the notation chapter is a descriptive account of
the book's conventions. Reader commands and chatbot/editorial guidance were
removed from that chapter; internal guidance is in `docs/NOTATION_AUTHORING.md`.

## Current content

Notation standard, 40 fully worked problems in six subject chapters, purple
supporting-tools appendix, and notation literature review. The editorial outline
is kept in the repository for development and is excluded from reading pages,
downloads, and the compiled PDF. Alpha edition 0.3.0-alpha.1 adds 16 graduate-review
problems in D3 and I3, with primary references and explicit domain arguments.

## Next steps

1. Add more mixed-method practice and integration by parts.
2. Continue developing the manuscript and publish further alpha PDF editions at reviewed milestones.

See docs/DEVELOPMENT.md and CONTRIBUTING.md for the workflow and editorial rules.

## Validation

Ten content tests pass. The numerical check script compares advanced formulas
against independent finite differences, quadrature, and tangent orthogonality.
Publication and visual verification for the expanded edition are in progress.
