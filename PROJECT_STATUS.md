# Project status

Updated November 6, 2026. Stage: alpha development; no stable or beta release.
The working manuscript contains changes after the fixed 0.4.0-alpha.7 edition.

## Current manuscript

The book has **72 fully worked problems: 48 main mixed problems and 24 reference
exercises**. Twenty substantial additions cover matrix exponentials and inverse
responses, constrained matrix gradients, tensor contractions and rotations,
nonlinear extensions, geometric accumulation, oscillatory limits, and singular
kernels. All original problem IDs and complete solutions are retained.

Each problem has three hints, a complete calculation, method-choice reasoning,
domain analysis, and a check. Printed statements continue directly into their
solutions, with hints in a separate page-referenced appendix. The website allows
individual hints and solutions to be opened separately. The main book has
185 pages. The shared quick reference remains four pages both inside the book
and as a standalone document.

## Mathematical review and corrections

The November 5 review analytically rederived all 52 original problems and
reviewed the notation chapter, methods reference, quick reference, and supporting
identities. Existing final answers were verified. Corrections address Tonelli's
scope at an infinite endpoint, missing sufficient hypotheses for reference
formulas, and the distinction between angular seams and Jacobian degeneracies.
The oscillatory-tail proof is now explicit, and the panel observation parameter's
units are declared.

Every new problem has an author derivation and an independent second analytical
agent review. Integration review corrected a spectral-gap notation issue so
that the perturbation bound uses the eigenvalue gap of the actual base matrix.
Two misleading prose phrases were also corrected. The evidence distinguishes
analytical arguments, numerical spot checks, selected visual inspection, and
external reader feedback. No human peer review or reader trial is claimed.

[The beta review ledger](docs/BETA_REVIEW.md) links evidence for all 72 problems
and the references. [The backlog](docs/PROBLEM_BACKLOG.md) maps the 20 promoted
proposals to stable IDs; twelve proposals remain unimplemented.

## November 6 fresh recheck

All 72 problems received another complete analytical pass, with main chapters
assigned to different reviewers. Statements were independently recalculated,
then every hint, solution step, result, and domain claim was compared. No new
mathematical error was found. Fresh edge-case calculations supplement these
arguments; [the recheck report](docs/RECHECK_2026-11-06.md) links per-problem evidence.

Two actual verification defects were corrected: comparison helpers could accept
an infinite expected value, and reciprocal printed hint links were checked only
for the last chapter. Helpers now require finite inputs and valid tolerances;
hint-link checks cover every chapter. A focused regression raises the unit/content
total to 17; the maintained mathematical checks remain 492. The mathematical
manuscript and both generated LaTeX documents are unchanged by this pass.

## Validation

- All 17 content/structure and verification tests pass, including the 72-problem inventory,
  stable IDs, matching statements/hints/solutions, and printed reading order.
- All 492 maintained independent numerical checks pass: 141 original checks,
  245 differentiation-expansion checks, and 106 integration-expansion checks.
  Finite differences and quadratures supplement the analytical proofs.
- Generation produces 14 reading pages and 72 individual practice pages, plus
  downloads and both tracked LaTeX sources. The expanded mathematical site build
  allows a 4 GiB Node heap so the single-page edition can compile reliably.
- The production site checks pass for 94 HTML pages, internal links/assets,
  anchors, and 8,858 rendered mathematical expressions. The build used the
  repository's actual GitHub Pages base path.
- Both PDFs compile. Automated checks pass for the 185-page book, printable
  margins, notation groups, and exactly four standalone and four embedded
  reference pages. No overfull-box warning is present in the final TeX logs.
- Selected revised reference pages and eight new solution pages were inspected
  visually, including matrix, tensor, Bessel, and interior-source formulas.
  This is not a whole-book reader or pagination trial.

## Publication

The complete current reading edition is published from main through GitHub
Actions at https://wa200508.github.io/Calculus_Workbook/generated/book.html.
Main-branch PDF builds supply the current book and companion as workflow
artifacts. The last tagged PDFs remain alpha.7; download labels distinguish
that fixed edition from the current manuscript and source downloads. No new
release has been tagged by this work.

The original correction checkpoint is `606a472`; both of its GitHub workflows
passed. The expansion and its verification are committed as subsequent tested
checkpoints on main. The final handoff records the pushed revision and workflow
results. Source Markdown is authoritative; the TeX documents and site are
generated from it.

## Next milestone: beta.1

The 48-problem main collection exceeds the approximate 40-problem planning
target, with matrix/tensor and geometric/singular coverage added. Analytical
agent evidence is complete for the included problems and references. Remaining
beta work is a full editorial/pagination and usability pass, representative
external reader trials, grayscale and mobile/keyboard checks, and consistent
beta release/tag metadata. The larger count and passing automated checks do not
declare the book ready for beta.

[The beta plan](docs/BETA_PLAN.md) preserves those release criteria. The next
concrete task is the complete reader/pagination review and representative reader
trials, rather than further content expansion solely to reach a count.

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
