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
a fixed PDF prerelease. Edition 0.4.0-alpha.1 is being validated for publication.
The previous fixed PDF, 0.3.0-alpha.3, has 90 pages. Current numerical, site, and
PDF results will be recorded after the new edition is built and inspected.

See docs/DEVELOPMENT.md and CONTRIBUTING.md for the development workflow.
