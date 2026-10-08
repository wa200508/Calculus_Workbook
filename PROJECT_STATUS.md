# Project status

Updated October 7, 2026.

## Established decisions

- Explicit review text with complete worked solutions and one-step-at-a-time tutoring.
- Notation standard 0.2: literature-informed Leibniz operators, round operands, full arguments, and explicit types/dependencies.
- Root Markdown manuscript generates the site and LaTeX book.
- Educational content: CC BY-SA 4.0. Software: MIT. Correctness is not guaranteed.
- Static VitePress site, local search, build-time MathJax, and practice pages.
- GitHub Pages hosting after the intended public repository is supplied.

## Current content

Notation standard, literature review, proposed curriculum, and two complete pilots:
D2-001 (chain rule) and I2-001 (definite substitution). The full curriculum is planned;
the site does not imply all chapters are already written.

## Next steps

1. Connect the provided public repository and enable Pages via GitHub Actions.
2. Observe the first hosted site and PDF builds and review their output.
3. Develop D1 and D2 as representative chapters with practice variants and solutions.
4. Review the PDF layout and provide a public milestone PDF download.

See docs/DEVELOPMENT.md and CONTRIBUTING.md for the workflow and editorial rules.

## Local validation

Six content tests pass. Production builds pass for both `/` and a repository
subpath. Internal links, assets, anchors, and 292 rendered math expressions on
12 pages pass the built-site checks. Browser review confirmed equation rendering,
search, hint/solution disclosure, and dark blue algebra blocks. Local PDF
compilation remains blocked by the editor compiler's unavailable TeX bundle;
the GitHub PDF workflow awaits its first hosted run.
