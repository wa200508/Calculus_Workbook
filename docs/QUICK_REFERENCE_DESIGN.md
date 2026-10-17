# Print layout and quick reference

The notation chapter is divided at conceptual boundaries: declarations,
delimiters, object typography and dependencies, ordinary derivatives, partial
and path derivatives, vector outputs, matrix/tensor inputs, integrals,
substitution, related symbols, and step labels. Tables are left aligned and
unbroken. Column widths include intercolumn spacing, with extra width for full
function declarations. Wrapped Markdown list items remain single paragraphs.
The methods reference keeps each operative entry and its conditions together;
the elementary table and inverse-function formulas form separate complete blocks.

## Four-page companion

CHEAT_SHEET.md is the content source. The generator creates the online reading
page and standalone calculus_quick_reference.tex. Its own preamble uses US Letter,
two columns, 9-point body text, 11-point leading, and explicit page boundaries.
Each column is unbroken, so formulas cannot drift into the next column or page.
The fourth page's supporting identities and expansions are purple.

1. Notation, objects, dependencies, evaluation, constants, elementary derivatives
   and primitives, hyperbolic functions, and inverse-function branches.
2. Derivative rules, compositions, inverse and implicit functions, variable powers,
   phase, path dependence, constraints, endpoint limits, and error notation.
3. Fundamental theorem, variable limits, substitution, parts, rational forms,
   symmetry, parameter differentiation, improper integrals, principal values,
   interchange theorems, oscillation, and representations.
4. Gradients, Jacobians, Hessians, measures and orientations, integral theorems,
   matrix and tensor operations, coordinate identities, and Taylor estimates.

The sheet condenses both introductory chapters. Full function arguments,
Leibniz operators, types, and local domain qualifications remain visible.
The compact entries complement the fuller hypotheses and explanations in the
methods reference; they do not replace them.

## Layout references

Two existing reference layouts informed the grouping and compact columns:

- [Paul Dawkins, Calculus Cheat Sheet](https://tutorial.math.lamar.edu/pdf/Calculus_Cheat_Sheet_All.pdf).
- [Robert G. Brown, One-Sheet Math Review (Duke)](https://webhome.phy.duke.edu/~rgb/Class/one-sheet-math-review/one-sheet-math-review.pdf).

The workbook sheet has original prose and typesetting, follows this book's
notation, and does not reproduce either document. Mathematical sources remain
listed in METHODS_REFERENCE.md and NOTATION_REVIEW.md.

## Verification

The PDF workflow compiles both documents using pdfLaTeX. The local review also
uses Tectonic. scripts/check_pdf_layout.py requires exactly four reference pages,
checks printable text bounds, and checks that the most vulnerable notation
concepts and tables stay on one page. This supplements visual inspection of all
introductory and reference-sheet pages; text bounds alone cannot detect every
layout defect. Future edits that lengthen a group require a new layout review.
