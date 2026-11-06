# Adversarial verification and statement recheck — November 6, 2026

Reviewer: Codex agent `audit_reference_exercises`.
Baseline: `1d2632c22bb9a00b07f5780074b24854d99c3dbf`.

This fresh pass inspected the actual implementations of
`scripts/check_advanced_math.py`, `scripts/check_differentiation_expansion.py`,
`scripts/check_integration_expansion.py`, and `tests/test_content.py`.
It also extracted and reread all 72 current problem statements through
`scripts/build_content.py:problem_sections`, checking types, dependencies,
domains, physical units where specified, and hypotheses needed to make the
requests well posed. Earlier audit notes were not used as an approval shortcut.
Full analytical rederivation of the 72 solutions is recorded by the separate
chapter reviewers; this note does not relabel the numerical suites as proofs.

## Findings corrected in the verification code

### 1. Infinite reference values could silently pass all three proximity helpers

Each baseline `near` helper compared

```python
abs(actual - expected) <= tolerance * max(1, abs(expected))
```

For finite `actual=1.0` and `expected=math.inf`, both sides become infinity,
so the comparison succeeds. This was reproduced by compiling the actual helper
definitions from baseline `1d2632c`, not a copied approximation of their logic.
All three helpers silently accepted that probe. In addition, the integration
suite's `between` helper accepted an infinite result in an infinite interval.
Infinite tolerances, reversed interval bounds with sufficient slack, or infinite
slack could also defeat the intended finite-error interpretation. NaN operands
already failed the ordinary comparison; the repair makes their rejection
explicit and tests it alongside the infinity cases.

The maintained helpers now reject nonfinite real/complex magnitudes and
nonfinite or negative tolerances before comparison. The interval helper also
requires finite values and endpoints, ordered bounds, and finite nonnegative
slack. Valid zero tolerance and exact finite complex comparisons remain valid.
The reported mathematical check counts do not change.

The current mathematical inputs and expected values were all finite before
the repair. This is a verification defect that could conceal a future broken
calculation, not evidence that an existing book result was infinite or wrong.

### 2. Reciprocal hint references were checked for only the last chapter

In `test_printed_problems_are_followed_by_their_own_solutions`, generation and
assertion of the hint labels occurred after the manuscript loop. The local
`groups` variable therefore referred only to the final I2 chapter. Statement/
solution pairing was checked for all chapters, but reciprocal hint labels and
their problem-page references were not.

Those existing assertions now run inside the loop and cover every chapter.
No generated hint defect was found; this closes a gap in the claimed coverage.

### Regression and check results

One focused regression unit test compiles the actual `near` and `between`
function definitions from their source ASTs, avoiding a second execution of
the mathematical suites during the unit-test run. It checks ordinary finite
successes and failures, real and complex NaN/infinity in either comparison
position, infinite/negative tolerances, infinite/reversed bounds, and invalid
slack. The existing chapter hint assertions cover the corrected loop placement.

The following commands passed after the repairs:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/check_advanced_math.py
python3 scripts/check_differentiation_expansion.py
python3 scripts/check_integration_expansion.py
```

The results are **17 unit/content tests** and **492 mathematical spot checks**:
141 original mixed-problem checks, 245 differentiation-expansion checks, and
106 integration-expansion checks. No mathematical spot check was added or
removed by this verification repair.

## Independence and practical limits of the numerical suites

The scripts generally compare different representations rather than simply
evaluate the same closed expression on both sides. Important examples are:

| Area | Actual independently evaluated object | Compared result |
|---|---|---|
| Original derivatives | Central differences of the originally defined scalar, complex, or graph function | Analytic derivative expressions |
| Original parameter integrals | Direct original kernels, with coordinate changes to regularize endpoints where needed | Logarithmic, inverse-trigonometric, or special-function expressions |
| D4-008 | Newton solution of the original implicit constraint | Implicit first and second derivatives |
| D4-009 | Golden-section optimization retaining both endpoints | Piecewise maximizing value and its derivatives |
| D4-010 | Full matrix exponential series, without using the special square identity | Regime formulas and parameter derivatives |
| D4-011 and D3-008 | Pivoted elimination of the original matrices | Constrained-gradient and rank-one formulas |
| D3-009 | Explicit four-index sum over all 81 slots | Expanded energy and finite differences |
| D3-010 and D3-011 | Direct matrix rotation or vector normalization | Component derivatives and norm invariants |
| I4-007 | Circular-segment sections along a different coordinate direction | Oblique-cap formula and derivatives |
| I4-009 | Entrywise resolvent quadrature under a finite-interval transformation | Inverse and ordered noncommuting perturbation derivative |
| I4-011 | Direct complex angular/radial quadrature | Independently evaluated Bessel series and moment remainder |
| I3-010 and I3-011 | Original-coordinate finite integral or exponential-coordinate logarithmic integral | Explicit improper tail intervals and independent series bounds |
| I3-014 | Cartesian inner integration followed by a squared-distance split | Source-edge expression from three different panel maps |

Supplementary consistency checks are also present and should be described as
such. For example, hyperboloid tangent orthogonality does not determine the
normal's orientation: either sign is orthogonal. Trace/determinant invariants,
evenness, signs, and evaluated values likewise do not independently establish
complete derivative or convergence formulas. The final I4-006 boundary-slope
check differences its closed form; positive-distance Cartesian quadratures
supply a separate comparison, while the endpoint argument still requires proof.

Specific limitations retained explicitly rather than inflated into coverage:

- The mathematical scripts hardcode the reference formulas. They do not parse
  mathematical expressions out of the manuscript. An isolated typo in Markdown
  can therefore leave every numerical check passing; analytical source review
  remains necessary.
- The maintained mathematical suites primarily cover the 48 mixed problems.
  The 24 elementary reference exercises have structural coverage and separate
  analytical review; the 492 count is not 492 checks uniformly distributed over
  all 72 problems.
- The D3-009 numerical example intentionally uses a different anisotropic
  tensor/strain path from the manuscript's worked example. It checks the
  general contraction and off-diagonal multiplicity, but cannot certify the
  manuscript example's particular coefficients. Those require direct review.
- The I3-002 loop computes a nonsmall value at `(k,L)=(2,1)` without asserting
  it, because only the small-parameter cases enter the remainder comparison.
  That evaluation is not counted and must not be represented as a passing
  special-function check outside the small-parameter regime.
- Smooth phase-chart samples do not test phase jumps. Samples away from a
  source, zero eigenvalue, or endpoint do not prove regularity or interchanges
  there. Existing tests appropriately avoid numerically treating an undefined
  ordinary integral as a principal value without the stated prescription.
- All finite quadratures and finite differences have ordinary floating-point
  and discretization tolerances. The explicit improper tail bounds are real
  analytical bounds, but the full numerical calculation is not certified
  interval arithmetic. Loose slack at a very small remainder can confirm broad
  agreement without resolving its sharp leading coefficient.

No incorrect finite tolerance or asserted remainder stronger than its proved
bound was found for the current sample inputs. The exact squared bound in
D4-007 is justified by the exponent lying in `[-1,1]`; the positive/negative
remainder checks in I4-006, I4-011, I3-011, and I3-012 have the correct signs.
The Gaussian, damping, squared-sinc, and logarithmic-moment cutoff comparisons
respect their omitted tails. The noncommuting matrix samples really do have
nonzero commutators.

## All 72 statement checks

The parser inventory was independently checked against these eight ranges:

| IDs reread | Count | Statement hypotheses and traps inspected |
|---|---:|---|
| D4-001–D4-011 | 11 | Positive logarithmic power bases; finite real input domains; selected height branch; fixed delay parameters; reversed integral endpoints; local implicit branch; bounded maximizer; full matrix exponential; open positive-definite parameter domain and symmetric versus independent entry variations. |
| D3-001–D3-012 | 12 | Cutoff domain; excluded source and fixed wavenumber; principal phase zeros/cuts; graph versus full surface; parameter seam; anisotropic positive/indefinite domains; complex right-hand side; rank-one zero vector and excluded pole; tensor basis, index ranges and symmetries; active rotation convention; nonzero normalization; radial versus spatial differentiability, including zero wavenumber. |
| I4-001–I4-011 | 11 | Positive exponential parameters; logarithmic parameter endpoint; damping and signed frequency exceptions; finite endpoint weight; outward flux and source exclusion; dimensionless panel distance; nonunit plane normal; coincident positive poles; SPD resolvent path and noncommuting derivative; oriented moving Gaussian; signed/zero transverse wavenumber and area units. |
| I3-001–I3-014 | 14 | Folded substitutions; signed and zero wavenumbers; improper versus absolute convergence; sinc convention and removable phase matching; prescribed principal value; positive observation distance; nonnegative singular panels; volume Jacobian; finite/unbounded surface; cusp at zero; logarithmic moment remainder; almost-everywhere boundary-layer limit; curve orientation and excluded axis; strict interior source and separate panel maps. |
| D1-001–D1-006 | 6 | Fixed coefficients, positive root input, fixed parameters, preserved canceled exclusion, nonzero difference-quotient increment, and rational denominator exclusion. |
| D2-001–D2-007 | 7 | Scalar composition inputs, radians, excluded quotient input, strictly positive exponential/logarithmic/root arguments where required, and evaluation after differentiation. |
| I1-001–I1-006 | 6 | Arbitrary constants and connected components, endpoint order, exponential coefficient, trigonometric sign, and signed versus absolute area. |
| I2-001–I2-005 | 5 | Complete transformed bounds and derivative factors, zero inner derivative without inverse division, positive logarithm input, and reversed endpoint orientation. |

No additional statement-level type contradiction, physical-unit mismatch, or
missing hypothesis needed to pose these problems was found. In particular:

- D3-001 has propagation constant in inverse length and group velocity in
  length/time; D4-005's negative phase derivative has time units.
- I4-007 transforms the plane normal with the semiaxes and explicitly retains
  its nonunit length in the section relation.
- I4-009 specifies a continuously differentiable SPD matrix path rather than
  mere pointwise invertibility.
- I4-010 explicitly keeps negative orientation; I4-011's exponent is
  dimensionless and its transform has area units.
- I3-010 has inverse-length output and admits signed and zero wavenumbers;
  I3-012 explicitly requests the almost-everywhere limit; I3-014 requires
  strict source inequalities rather than silently allowing edge sources.

No manuscript source was changed during this verification task. The two
corrected findings concern the reliability and scope of verification code;
they are distinct from mathematical corrections to book statements or solutions.
