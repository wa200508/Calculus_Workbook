# Project status

Updated October 13, 2026. Stage: alpha development; no stable release.

## Current manuscript

Notation conventions and an introductory calculus methods reference precede
four mixed problem sets with 28 fully worked problems. The main chapters begin
with problems rather than lessons on a selected technique. Appendices contain
supporting tricks, 24 simpler reference exercises, and the notation literature
review. All 40 previous problem IDs are preserved; 12 new problems bring the total
to 52. Every problem has three hints, a complete solution, and a check.

## Established decisions

- Graduate workbook with complete worked calculations; prior calculus study is assumed.
- Explicit Leibniz operators with round operands, full arguments, object types, and dependencies.
- Difficulty arises from reasoning and calculation, with direct problem setups.
- CHOICE blocks are neutral, DOMAIN blocks amber, algebra blue, and supporting tricks purple.
- Root Markdown manuscripts generate VitePress pages and the complete LaTeX book.
- Educational content: CC BY-SA 4.0. Software: MIT. Correctness is not guaranteed.
- SSH remote: `git@github.com:wa200508/Calculus_Workbook.git`; incremental pushes on `main`.

## Publication and verification

The full reading edition is published through GitHub Actions at
https://wa200508.github.io/Calculus_Workbook/generated/book.html.
Main-branch checkpoints build both the site and PDF; alpha version tags publish
a fixed PDF prerelease. Edition 0.4.0-alpha.4 is published as a 130-page PDF.
Every printed problem is immediately followed by its complete worked solution;
hints are collected in an appendix with reciprocal page references. Continuation
headers identify the problem. The introduction and reference prose now describe
the workbook's purpose and conventions in connected, reader-facing prose.

Thirteen content tests and 141 independent numerical spot checks pass. Production
checks cover 73 HTML pages, internal links, assets, anchors, and 5,578 rendered
math expressions. These spot checks do not replace analytical domain and
convergence arguments. The live introduction was verified in the browser.
Site run 38489328625 and tagged PDF run 38489330514 completed successfully.

The released PDF was downloaded and inspected: all 52 hint references resolve,
no unresolved references remain, and text bounds show no horizontal margin
overflow. Visual inspection covered the introduction, statement/solution pairing,
continuation headers, hints, and revised long calculations. The final edition
also removes orphaned hint-reference lines and displays the RF response check
on its own line.

Editorial changes, print restructuring, mathematical clarifications, and layout
repairs were pushed incrementally (335b038, 698ef68, b88cf38, 702e7f1, c4f1466).
The 32 proposals in docs/PROBLEM_BACKLOG.md are candidates for the next expansion,
not yet published as solved exercises. Review scope and findings are documented
in docs/REVIEW_NOTES.md.

See docs/DEVELOPMENT.md and CONTRIBUTING.md for the development workflow.
