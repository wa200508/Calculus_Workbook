# Editorial and mathematical review — October 13, 2026

## Scope

This pass revises the introduction, notation discussion, methods reference,
supporting-tools appendix, solution headings, and selected compressed arguments.
It changes the printed reading order for all 52 problems. The existing problem
statements and intended answers are retained. The development backlog is excluded
from the published book because its proposed problems do not yet have reviewed
solutions.

## Mathematical findings and repairs

- The supporting-tools appendix called the base of the natural logarithm the
  “Euler constant,” an ambiguous name. It now identifies it as the base of the
  natural logarithm.
- Big-O and little-o notation occurred in the harder solutions without a local
  definition in the notation chapter. Their meanings and the limits of
  differentiating a remainder estimate are now stated.
- D4-001 now shows the derivatives of both the variable base and variable exponent
  before combining them. Its extension is continuous at zero but has no finite
  derivative there; the difference-quotient argument remains essential.
- D4-005 now retains all response arguments in the logarithmic-derivative check.
- D4-006 now distinguishes the compact rectangle of integration coordinates and
  parameter values from the continuous functions bounded on that rectangle.
- I4-002 now justifies the series after division by the integration coordinate,
  not only the logarithm series before division. It also gives the monotone-
  convergence argument connecting the endpoint integral and series limit. The
  logarithm and arctangent expansions cited in the solutions have been added to
  the supporting reference.
- I4-004 now displays an integrable bound independent of the parameter near its
  endpoint. This supports the limit of the integral while leaving the divergent
  parameter derivative as a separate issue.
- I4-006 now includes the second coordinate transformation and all intermediate
  algebra leading to the arctangent primitive. Its endpoint slope still follows
  from the explicit remainder bound, not formal differentiation of big-O notation.

## Verification

Thirteen content tests pass, including a check that every printed statement is
followed by the matching complete solution and that hints have reciprocal page
references. All 141 independent finite-difference, quadrature, and geometric spot
checks pass. These numerical checks cover selected nonsingular inputs; they do
not replace the domain and convergence arguments in the manuscript.

Production site and PDF layout results are recorded in PROJECT_STATUS.md after
publication. The PDF requires visual inspection of the introduction, the first
worked problem, continuation headers, hints, and the longer revised calculations.
