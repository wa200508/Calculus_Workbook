# Project status

Updated October 12, 2026. Stage: alpha development; no stable release.

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
a fixed PDF prerelease. Edition 0.4.0-alpha.1 is published as a 111-page PDF, including eight pages of
introductory methods reference. The new reference and problem pages were rendered
for visual inspection; PDF text bounds show no horizontal margin overflow.

Twelve content tests and 141 independent numerical checks pass. Production checks
cover 72 HTML pages, internal links, assets, anchors, and 5,428 rendered math
expressions. The live mixed-set index and a new problem's hint and complete-solution
disclosures were verified in the browser. Site run 38324715403 and tagged PDF run
38324714616 completed successfully.

The restructuring, reading-page update, and mathematical validation were pushed
as separate checkpoints (d17bbf5, 80837b1, and 24e9f08), followed by the alpha tag.

See docs/DEVELOPMENT.md and CONTRIBUTING.md for the development workflow.
