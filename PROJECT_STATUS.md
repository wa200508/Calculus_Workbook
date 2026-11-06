# Project status

Updated November 6, 2026. Stage: alpha development; no stable or beta release.
The working manuscript contains changes after the fixed 0.4.0-alpha.7 edition.

## Current manuscript

The book has **92 fully worked problems: 68 main mixed problems and 24 reference
exercises**. At the user's request, a second twenty-problem batch completes the
remaining twelve original backlog proposals and adds eight original subjects.
All 72 earlier statements, hint ladders, and complete solutions were compared
against `d272310` and preserved exactly.

The new topics include phase zeros and lifted angles, cubic folds and smooth
approximations, matrix square roots, nonlinear inverse maps, tensor transport,
Rayleigh quotients, Gaussian matrix moments, elliptic measures and ring kernels,
principal values, weighted panels, and Fresnel asymptotics. Every addition has
three hints, complete intermediate calculations, domain analysis, and checks.
The book now has **244 pages**. The shared quick reference remains four pages
both inside the book and as a standalone document.

## Mathematical review

The November 5 baseline audit covered all 52 original problems and the notation,
methods, quick-reference, and supporting-tool references. Corrections addressed
Tonelli's scope at an infinite endpoint, sufficient hypotheses, coordinate
seams, and the explicit oscillatory-tail proof. The first twenty additions
received author derivations and independent analytical review.

The November 6 fresh recheck covered all 72 then-existing problems at baseline
`1d2632c`; it found no further mathematical error. It corrected two verification
bugs: infinite-value false passes and reciprocal hint tests limited to the last
chapter. [The recheck report](docs/RECHECK_2026-11-06.md) preserves that scope.

The second twenty additions follow baseline `d272310`. Each has an author
derivation and an independent reviewer who calculated expected results before
reading the solutions. Additional readers checked the most delicate principal-
value, Fresnel, and numerical-verification arguments. One new dilogarithm
hypothesis was corrected: its finite value at one does not imply a finite
endpoint derivative. Elliptic functions consistently use the parameter convention
across the new problems. A wide ellipse-speed formula was moved into display
math after the printable-margin check detected overflow.

[The second-expansion report](docs/EXPANSION_2_2026-11-06.md) and
[the review ledger](docs/BETA_REVIEW.md) link evidence for every included ID.
The all-problem recheck remains explicitly a 72-problem baseline review; the
new twenty have separate expansion evidence. No external human review is claimed.

## Validation

- All **17 unit/content and verification tests** pass. They cover the exact
  92-problem inventory, stable IDs, three hints per problem, complete solution
  blocks, printed reading order, reciprocal hint references for every chapter,
  and nonfinite-value regressions for all five numerical scripts.
- All **1,445 maintained numerical checks** pass: 141 original checks, 245 and
  106 first-expansion checks, and 756 and 197 second-expansion checks.
  Numerical agreement supplements the analytical arguments.
- Generation produces 14 reading pages and 92 individual practice pages, plus
  downloads and tracked LaTeX. Production checks pass for **114 HTML pages**,
  internal links/assets, anchors, and **12,278 rendered math expressions** at
  the actual GitHub Pages base path.
- The larger single-page build allows a 6 GiB Node heap. Local production
  compilation completed successfully; this is a ceiling, not a reservation.
- Both PDFs compile. Printable margins and notation groups pass at 244 book
  pages, with exactly four standalone and four embedded reference pages. Final
  TeX logs contain no overfull-box warning. Selected twelve new solution pages
  were visually inspected; a complete reader/pagination trial remains pending.
- Both tracked TeX documents were regenerated from the manuscript and checked
  for freshness before commit.

## Publication

The complete current reading edition is published from main through GitHub
Actions at https://wa200508.github.io/Calculus_Workbook/generated/book.html.
Main-branch PDF builds supply the current book and companion as workflow
artifacts. The last tagged PDFs remain alpha.7, with 52 problems; download
labels distinguish that fixed edition from the current 92-problem manuscript
and current source downloads. No new release is tagged by this expansion.

Tested checkpoints are pushed incrementally on main. The final handoff records
the pushed revision and publication status. Root Markdown remains authoritative;
both TeX documents and the reading site are generated from it.

## Next milestone: beta.1

The 68-problem main collection exceeds the original approximate 40-problem
scope target. All forty recorded development proposals are represented in the
manuscript; [the proposal record](docs/PROBLEM_BACKLOG.md) maps them to IDs.
Included problems and references have analytical agent evidence. Remaining beta
work is a full editorial/pagination and usability pass, representative external
reader trials, grayscale and mobile/keyboard checks, and consistent beta
release/tag metadata. Passing automated checks and a larger count do not
declare beta readiness. Further content work can follow the user's priorities.

[The beta plan](docs/BETA_PLAN.md) preserves those release criteria.

## Established decisions

- Graduate workbook with complete calculations; prior calculus study is assumed.
- Explicit Leibniz operators with round operands, full arguments, object types,
  dependencies, and quantities held fixed.
- Difficulty arises from method selection, reasoning, and calculation.
- CHOICE blocks are neutral, DOMAIN blocks amber, algebra blue, and supporting
  tricks purple; text labels retain meaning without color.
- The quick reference is independently readable and shares its body between
  the standalone and embedded four-page editions.
- Educational content: CC BY-SA 4.0. Software: MIT.
- Incremental tested commits and pushes on main; publication remains alpha.

See [development](docs/DEVELOPMENT.md) and [contributing](CONTRIBUTING.md).
