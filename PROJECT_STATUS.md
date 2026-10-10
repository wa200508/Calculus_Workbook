# Project status

Updated October 7, 2026. Stage: alpha development; no stable release.

## Established decisions

- Explicit review text with complete worked solutions and one-step-at-a-time tutoring.
- Notation standard 0.2: literature-informed Leibniz operators, round operands, full arguments, and explicit types/dependencies.
- Root Markdown manuscript generates the site and LaTeX book.
- Educational content: CC BY-SA 4.0. Software: MIT. Correctness is not guaranteed.
- Static VitePress site, local search, build-time MathJax, and practice pages.
- SSH remote: `git@github.com:wa200508/Calculus_Workbook.git`; incremental pushes on `main`.

## Current content

Notation standard, literature review, proposed curriculum, D1 scalar differentiation
with six complete problems, and two pilots: D2-001 (chain rule) and I2-001
(definite substitution). The purple supporting-tools appendix covers Euler identities,
Taylor expansions with error bounds, binomial expansion, completing the square,
rationalization, and logarithm identities. Substitution remains a core calculus method.
The full curriculum is planned;
the site does not imply all chapters are already written.

## Next steps

1. Enable GitHub Pages using GitHub Actions in the repository settings.
2. Observe the first hosted site and PDF builds and review their output.
3. Extend the scalar foundation and develop D2 product, quotient, and chain-rule practice.
4. Review the PDF layout and provide a public milestone PDF download.

See docs/DEVELOPMENT.md and CONTRIBUTING.md for the workflow and editorial rules.

## Validation

Nine content tests pass. The expanded production site builds and passes
internal-link, asset, anchor, and math-rendering checks.
The first GitHub site build and PDF build succeeded. Pages deployment returned
404 because Pages is not yet enabled; the user has been asked to enable GitHub
Actions as its source. The available browser is signed out of GitHub.
