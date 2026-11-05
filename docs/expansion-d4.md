# Five additions to nonlinear scalar and parameter practice

Prepared November 5, 2026 by the Codex D4 expansion agent after the correction
checkpoint `606a472`. This note covers D4-007 through D4-011, added to
`DIFFERENTIATION_MIXED.md`. The six existing problems and their identifiers are
preserved. Each addition has a direct statement, explicit types/dependencies,
three graduated hints, full calculation, domain analysis, and an independent
check. The proposal numbers below refer to `PROBLEM_BACKLOG.md`.

This is author derivation and verification evidence. An independent second
review of these additions is separate from the baseline audit of D4-001–006.
No human reader trial or PDF layout review is claimed here.

## D4-007: finite value, oscillating slope — proposal 1

Taking the logarithm gives `sin(1/x)*ln(1+x^2)`, whose absolute value is at most
`x^2`. The exponential inequality bounds the original difference quotient and
establishes the unique extension value one and derivative zero. Exact product
and chain differentiation at nonzero inputs gives the stated derivative.
The coefficient `ln(1+x^2)/x^2` tends to one; sequences with cosine one and minus
one yield derivative limits minus one and one. This proves discontinuity of the
derivative without incorrectly differentiating a value remainder.

Domain: the base is positive everywhere, but the original exponent requires a
nonzero input. The extension and its derivative at zero are proved separately.
Independent checks compare finite differences of the original exponential
representation with the exact derivative, test the two sequence families, and
verify the difference-quotient bound at both signs of a small input.

## D4-008: coupled exponential constraint — proposal 3

For `F(x,y)=x*exp(y)+y*exp(x)-1`, the height partial is one at `(0,1)`, so the
implicit function theorem provides a unique smooth local branch. The first
composition derivative gives slope `-(e+1)`. Retaining both mixed contributions
in the second derivative gives `2*(e+1)^2-1`. The quadratic coefficient is
therefore `(e+1)^2-1/2`.

A direct substitution of the proposed polynomial into the original constraint
cancels both the linear and quadratic residual terms. A local positive lower
bound on the height partial then converts the cubic residual into a cubic
branch-error bound by the mean value theorem. This independently supports the
Taylor remainder. The solution claims only the local branch guaranteed by the
theorem, avoiding an unsupported global domain assertion.

Independent numerical checks solve the original constraint by Newton iteration,
compare central differences for both derivatives, and compare the branch with
the quadratic approximation at positive and negative small inputs.

## D4-009: bounded maximum response — proposal 6

The coordinate derivative `t-4*x^3` determines the unique maximizing coordinate:
zero for `t<=0`, `(t/4)^(1/3)` for `0<t<4`, and one for `t>=4`. Substitution yields
values zero, `3*(t/4)^(4/3)`, and `t-1`. One-sided difference quotients prove that
the value is continuously differentiable across both transitions. Its second
derivative diverges from the right at zero and has unequal one-sided values at
four, so neither transition has a second derivative.

The compact coordinate interval supplies existence. Sign changes of the
coordinate derivative establish maximality rather than assuming a stationary
point is a maximum. Differentiating the unsimplified interior maximizing value
cancels the coordinate-rate contribution and independently checks that the
parameter derivative equals the maximizing coordinate. Fine-grid numerical
maximization independently bounds the value at both transitions and within all
three parameter regimes; finite differences check slopes and curvature away
from transitions.

## D4-010: matrix exponential change of regime — proposal 25

The exact identity `A(t)^2=-t*I` separates the exponential into even and odd
coefficient series `C(t)` and `S(t)`. Both are entire scalar power series. For
positive input they give cosine and sine divided by the square root; for
negative input they give hyperbolic cosine and hyperbolic sine divided by the
square root. At zero both coefficients are one.

Termwise differentiation gives `dC/dt=-S/2` and `dS/dt=(C-S)/(2*t)` away from
zero, with the series value `-1/6` at zero. The matrix product rule differentiates
the coefficient and the matrix factor separately. The resulting zero derivative
is `[[-1/2,-1/6],[-1,-1/2]]`. Directly differentiating the original matrix power
series at the nilpotent zero matrix reproduces this value through its first
three terms. The product `exp(A)*dA/dt` instead gives `[[-1,0],[-1,0]]` at zero.
Explicit unequal matrix products explain why the scalar-inspired shortcut fails.

Domain: no real parameter is excluded; apparent square-root quotient
singularities are removable and the entire coefficient series justify crossing
zero. A direct numerical matrix exponential power sum, independent of the closed
forms, is compared with the values and finite-difference derivatives at negative,
zero, and positive inputs. The determinant identity `C^2+t*S^2=1` supplies an
additional check across all regimes.

## D4-011: constrained positive matrix response — proposal 28

The open parameter domain is `a>0` and `Delta=ac-b^2>0`, which also implies
`c>0`. Explicit inversion gives `f=ln(Delta)+(a+c)/Delta`. Direct scalar
logarithmic and quotient differentiation produces the three parameter
partials with all numerator terms displayed.

For comparison, the scalar response is extended to general real matrices near
the given positive matrix with positive determinant. Differentiating the inverse
identity gives the ordered inverse derivative; a determinant increment expansion
and cyclicity of the trace yield the unconstrained entry gradient
`G=A^(-1)-A^(-2)` at the symmetric input. Symmetry of the actual parameter
increment produces parameter derivatives `(G11,G12+G21,G22)`, including the
factor of two for the shared off-diagonal parameter. This distinguishes the
open four-entry extension from the three-parameter positive definite domain.

Independent checks use scalar finite differences in each constrained parameter
and separately perturb each of all four entries of the unconstrained extension.
Samples include nonzero positive and negative off-diagonal entries. Diagonal
specialization, interchange of the diagonal parameters, and the identity matrix
are checked in the manuscript as well.

## Executed supplementary checks

`/workspace/scratch/expansion-d4-checks.py` executed 109 independent numerical
comparisons successfully on November 5, 2026, using Python's standard library.
The script includes finite differences, Newton solution of the original
implicit constraint, fine-grid maximization, direct matrix power summation,
and separately varied unconstrained matrix entries. It is supplementary working
evidence, not a maintained repository test. Numerical samples supplement the
analytical arguments and do not establish branch existence or endpoint
regularity.

The manuscript parser also confirmed eleven matching statements, hint ladders,
and solutions in this chapter, exactly three hints per problem, and the required
SETUP, CHOICE, CALCULUS, ALGEBRA, DOMAIN, and CHECK labels in all five additions.
Root integration will update the total inventory, maintained checks, generated
sources, and release status; those shared files were not changed by this agent.
