# Beta review ledger

Started October 18, 2026; updated November 6, 2026. See [BETA_PLAN.md](BETA_PLAN.md) for the review criteria.

Reviewed expansion revision: `ca49cd07c95d0b8ef1ee031971db47e5abbac8b6`.
[Integrated findings and verification](REVIEW_2026-11-05.md) records the original
correction checkpoint, added coverage, checks, and remaining reader-review gates.

**Pending** means no complete beta audit has yet been recorded. Existing
solutions, CHECK steps, targeted editorial reviews, and numerical spot checks
are not being relabelled as a full analytical audit. Add new problems to this
ledger when they enter the manuscript.

The original 52 problems have received the analytical agent reviews linked below.
All 20 additions have author derivations and an independent second analytical
agent review. The reference-formula audit is recorded separately. These reviews do not establish
independent human review, reader feedback, or completion of every beta release gate.

For each completed review, link an evidence note recording the reviewed revision,
reviewer/agent, derivation/domain checks, independent verification, findings and
fixes, and any remaining limitations. A correction can require re-review.

[The fresh November 6 recheck](RECHECK_2026-11-06.md) covers all 72 problems
again at baseline `1d2632c`, using different chapter reviewers and supplementary
adversarial calculations. The last column links per-problem evidence.

## Problem audit

| ID | Title | Beta audit | Evidence / unresolved findings | Fresh recheck, Nov 6 |
|---|---|---|---|---|
| D4-001 | A variable power near an excluded input | Analytical agent review complete | [Evidence](audit-d4.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D4-002 | An angle defined by a hyperbolic function | Analytical agent review complete | [Evidence](audit-d4.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D4-003 | A logarithmic ratio of radicals | Analytical agent review complete | [Evidence](audit-d4.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D4-004 | A coupled quadric and a constrained path | Analytical agent review complete | [Evidence](audit-d4.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D4-005 | A complex response with a delay parameter | Analytical agent review complete | [Evidence](audit-d4.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D4-006 | An integral with two moving endpoints | Analytical agent review complete | [Evidence](audit-d4.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D4-007 | A finite value with an oscillating slope | Author and independent analytical agent reviews complete | [Derivation](expansion-d4.md); [second review](expansion-differentiation-review.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D4-008 | A coupled exponential constraint | Author and independent analytical agent reviews complete | [Derivation](expansion-d4.md); [second review](expansion-differentiation-review.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D4-009 | A response selected by a bounded maximum | Author and independent analytical agent reviews complete | [Derivation](expansion-d4.md); [second review](expansion-differentiation-review.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D4-010 | A matrix exponential across a change of regime | Author and independent analytical agent reviews complete | [Derivation](expansion-d4.md); [second review](expansion-differentiation-review.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D4-011 | A scalar response on symmetric positive matrices | Author and independent analytical agent reviews complete | [Derivation](expansion-d4.md); [second review](expansion-differentiation-review.md) | [Rechecked](recheck-2026-11-06-d4.md) |
| D3-001 | Waveguide sensitivity at cutoff | Analytical agent review complete | [Evidence](audit-d3.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-002 | Spatial gradient of a complex Green kernel | Analytical agent review complete | [Evidence](audit-d3.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-003 | RF phase and the branch cut | Analytical agent review complete | [Evidence](audit-d3.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-004 | Ellipsoid height and surface normal | Analytical agent review complete | [Evidence](audit-d3.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-005 | A one-sheet hyperboloid | Analytical agent review complete | [Evidence](audit-d3.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-006 | A matrix-defined anisotropic scalar field | Analytical agent review complete | [Evidence](audit-d3.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-007 | A coupled field response | Analytical agent review complete | [Evidence](audit-d3.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-008 | A quadratic response near loss of invertibility | Author and independent analytical agent reviews complete | [Derivation](expansion-d3.md); [second review](expansion-differentiation-review.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-009 | Energy carried by coupled tensor components | Author and independent analytical agent reviews complete | [Derivation](expansion-d3.md); [second review](expansion-differentiation-review.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-010 | An anisotropic energy with turning principal directions | Author and independent analytical agent reviews complete | [Derivation](expansion-d3.md); [second review](expansion-differentiation-review.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-011 | A direction traced by three competing components | Author and independent analytical agent reviews complete | [Derivation](expansion-d3.md); [second review](expansion-differentiation-review.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| D3-012 | A finite value left after a point-source subtraction | Author and independent analytical agent reviews complete | [Derivation](expansion-d3.md); [second review](expansion-differentiation-review.md) | [Rechecked](recheck-2026-11-06-d3.md) |
| I4-001 | A difference of exponential kernels | Analytical agent review complete | [Evidence](audit-i4.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I4-002 | A logarithmic kernel on a finite interval | Analytical agent review complete | [Evidence](audit-i4.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I4-003 | A damped difference of oscillatory kernels | Analytical agent review complete | [Evidence](audit-i4.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I4-004 | A weighted logarithm with limiting parameter values | Analytical agent review complete | [Evidence](audit-i4.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I4-005 | Flux through a translated ellipsoid | Analytical agent review complete | [Evidence](audit-i4.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I4-006 | A panel kernel at positive observation distance | Analytical agent review complete | [Evidence](audit-i4.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I4-007 | An oblique ellipsoidal cap | Author and independent analytical agent reviews complete | [Derivation](expansion-i4.md); [second review](expansion-integration-review.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I4-008 | Two nearby poles off the real axis | Author and independent analytical agent reviews complete | [Derivation](expansion-i4.md); [second review](expansion-integration-review.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I4-009 | An accumulated matrix response | Author and independent analytical agent reviews complete | [Derivation](expansion-i4.md); [second review](expansion-integration-review.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I4-010 | A Gaussian with a moving truncation | Author and independent analytical agent reviews complete | [Derivation](expansion-i4.md); [second review](expansion-integration-review.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I4-011 | A circular aperture transform | Author and independent analytical agent reviews complete | [Derivation](expansion-i4.md); [second review](expansion-integration-review.md) | [Rechecked](recheck-2026-11-06-i4.md) |
| I3-001 | Sine over a half-period | Analytical agent review complete | [Evidence](audit-i3.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-002 | An oscillatory ratio on a finite interval | Analytical agent review complete | [Evidence](audit-i3.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-003 | Damping a conditionally convergent oscillatory integral | Analytical agent review complete | [Evidence](audit-i3.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-004 | A finite aperture integral at phase matching | Analytical agent review complete | [Evidence](audit-i3.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-005 | A reciprocal kernel with an interior pole | Analytical agent review complete | [Evidence](audit-i3.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-006 | Near a line source: differentiation under an integral | Analytical agent review complete | [Evidence](audit-i3.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-007 | A weakly singular CEM panel integral | Analytical agent review complete | [Evidence](audit-i3.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-008 | An ellipsoidal weighted volume | Analytical agent review complete | [Evidence](audit-i3.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-009 | Finite and infinite surface area of a hyperboloid | Analytical agent review complete | [Evidence](audit-i3.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-010 | A squared aperture kernel | Author and independent analytical agent reviews complete | [Derivation](expansion-i3.md); [second review](expansion-integration-review.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-011 | A logarithmic moment at an endpoint | Author and independent analytical agent reviews complete | [Derivation](expansion-i3.md); [second review](expansion-integration-review.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-012 | A shrinking layer and its parameter derivative | Author and independent analytical agent reviews complete | [Derivation](expansion-i3.md); [second review](expansion-integration-review.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-013 | Two closed paths around an excluded axis | Author and independent analytical agent reviews complete | [Derivation](expansion-i3.md); [second review](expansion-integration-review.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| I3-014 | A source inside a triangular panel | Author and independent analytical agent reviews complete | [Derivation](expansion-i3.md); [second review](expansion-integration-review.md) | [Rechecked](recheck-2026-11-06-i3.md) |
| D1-001 | Polynomial differentiation by linearity | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D1-002 | Radicals and negative powers | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D1-003 | Differentiation with fixed parameters | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D1-004 | Cancellation and a removable singularity | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D1-005 | Difference-quotient derivation | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D1-006 | Algebraic reduction before differentiation | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D2-001 | Differentiate a composition | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D2-002 | A polynomial times a sine | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D2-003 | A quotient with an excluded input | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D2-004 | An exponential of a quadratic | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D2-005 | Logarithmic composition | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D2-006 | Square-root composition | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| D2-007 | Nested trigonometric composition | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-d1-d2.md) |
| I1-001 | Polynomial antiderivatives by linearity | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |
| I1-002 | The reciprocal rule and two separate intervals | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |
| I1-003 | Evaluate at both endpoints | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |
| I1-004 | Reverse an exponential chain rule | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |
| I1-005 | Integrate a trigonometric sum | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |
| I1-006 | Signed accumulation versus area | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |
| I2-001 | Evaluate a definite integral | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |
| I2-002 | A derivative match needing a fixed multiplier | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |
| I2-003 | A cubic inside an exponential | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |
| I2-004 | A trigonometric input inside a reciprocal | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |
| I2-005 | Transforming reversed endpoints | Analytical agent review complete | [Evidence](audit-reference-exercises.md) | [Rechecked](recheck-2026-11-06-i1-i2.md) |


## Reference and reader reviews

| Area | Status | Evidence / unresolved findings |
|---|---|---|
| Notation conventions | Analytical agent review complete | [Evidence](audit-references.md); final rendering and usability are separate checks. |
| Calculus methods reference | Analytical agent review complete | [Evidence](audit-references.md); final rendering and usability are separate checks. |
| Four-page quick reference, standalone and embedded | Analytical agent review complete | [Evidence](audit-references.md); final rendering and usability are separate checks. |
| Supporting tricks and identities | Analytical agent review complete | [Evidence](audit-references.md); final rendering and usability are separate checks. |
| Complete-book editorial and pagination pass | Partial | Automated margins, notation groups, and four-page reference checks pass at 185 pages. Eight selected new solution pages and revised reference pages inspected; a complete reader/pagination trial remains pending. |
| Website mobile and keyboard usability | Pending beta review | Record actual devices, pages, and interactions tested. |
| Grayscale printing and reference-sheet use | Pending beta review | Record actual pages and results. |
| Representative external reader trials | Pending | No trial outcomes have been recorded. |
