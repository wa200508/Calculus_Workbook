# Project status

Updated October 17, 2026. Stage: alpha development; no stable release.

## Current manuscript

Notation conventions and an introductory calculus methods reference precede
four mixed problem sets with 28 fully worked problems. The main chapters begin
with problems rather than lessons on a selected technique. Appendices contain
supporting tricks, 24 simpler reference exercises, and the notation literature
review. All 40 previous problem IDs are preserved; 12 new problems bring the total
to 52. Every problem has three hints, a complete solution, and a check. A separate
four-page quick reference condenses notation, calculus tools, and their conditions.

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
Main-branch checkpoints build both the site and PDFs; alpha version tags publish
fixed PDF prereleases. Edition 0.4.0-alpha.5 provides a 131-page book and a separate
four-page quick reference, both downloadable from the release. Every printed
problem is immediately followed by its complete worked solution; hints retain
reciprocal page references.

Chapter 1 now has deliberate boundaries between complete notation concepts.
Tables are unbroken, left aligned, and proportioned to their contents. Wrapped
list items remain single paragraphs. In the methods chapter, formulas stay with
their explanations and conditions. The quick reference uses two columns and
9-point body text, with full operator notation, visible dependencies, domain
conditions, and purple supporting identities.

Fifteen content tests and 141 independent numerical spot checks pass. Production
checks cover 74 HTML pages, internal links, assets, anchors, and 5,950 rendered
math expressions. Numerical spot checks do not replace analytical arguments.
Site run 39042667325 and tagged PDF run 39042668752 completed successfully.

The actual release PDFs were downloaded and checked: the reference is exactly
four pages; printable text bounds and notation-group checks pass. All notation
and methods pages were inspected locally, together with all four reference
pages. Production renders confirmed intact tables and reference-sheet layout.
The PDF workflow now enforces reference length and printable margins on every
build. The online reference has direct PDF access from navigation and practice.

Layout, reference-sheet implementation, and release preparation were pushed as
separate checkpoints (3196ed0, 335c7f0, d707baa). Publication remains alpha.
The 32 candidates in docs/PROBLEM_BACKLOG.md await the next content expansion.
See docs/QUICK_REFERENCE_DESIGN.md for the layout rationale and source map,
and docs/REVIEW_NOTES.md for the previous mathematical review.

See docs/DEVELOPMENT.md and CONTRIBUTING.md for the development workflow.
