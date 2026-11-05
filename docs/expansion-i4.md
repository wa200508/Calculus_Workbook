# Expansion evidence: five parameter and geometry problems

Added November 5, 2026 by the Codex `audit_i4` author, after the correction
checkpoint `606a472`. This batch adds I4-007 through I4-011 to the authoritative
`INTEGRATION_MIXED.md`. The original six problems and their IDs are preserved.
Each addition has a typed statement, exactly three hints, a complete solution,
method reasoning, intermediate algebra, domain analysis, and a check. This note
records derivations and author verification; a separate review by the primary
editor or another reviewer is recorded separately.

## Selection and coverage

| Published ID | Backlog proposal | Added practice |
|---|---|---|
| I4-007 | 13, oblique ellipsoidal cap | Transforming a geometric constraint and measure together; full piecewise domains and tangent derivatives |
| I4-008 | 8, nearby poles | Stable exact cancellation, repeated denominators, differentiating an improper integral |
| I4-009 | 32, matrix resolvent integral | Entrywise matrix integration, spectral bounds, noncommuting perturbations and dominated differentiation |
| I4-010 | 11, moving Gaussian truncation | Oriented moving bounds, independent Leibniz and moving-coordinate derivations, controlled limits |
| I4-011 | 23, circular aperture transform | Defining a special function through the calculation, signed parameters, removable limits, explicit Taylor error |

The matrix integral supplements the beta plan's matrix differentiation goals
with a substantive matrix-valued integration problem. The cap, Gaussian, and
aperture problems also require parameter derivatives or limiting arguments rather
than only a definite-integral value.

## I4-007: oblique ellipsoidal cap

The scaling `x=D u`, with `D=diag(a,b,c)`, gives Jacobian `abc` and plane normal
`m=D n`. Thus its support distance is
`rho=|m|=sqrt(a^2 n_1^2+b^2 n_2^2+c^2 n_3^2)`, rather than the length of the
original normal. Orthogonal rotation of the unit ball gives circular sections
with area `pi(1-s^2)`. Integrating from `h/rho` to one yields
`pi abc (1-h/rho)^2 (2+h/rho)/3` between tangent offsets. Outside, the volume is
the complete ellipsoid or zero. At the upper tangent the region contains one
point, so its volume is zero even though the set is nonempty.

Differentiation inside the support gives
`-pi abc (1-h^2/rho^2)/rho`. The quadratic disappearing-cap factors show directly
that both endpoint derivatives are zero. The function is continuously
differentiable, but its interior second derivative has nonzero one-sided limits
at the two tangent offsets, unlike the zero exterior derivative. Section area
equals `-|n| V'(h)`, because offset increments move planes a distance
`dh/|n|`; the non-unit-normal factor is explicit. Complementary caps and the
spherical case independently check the result and its constants.

Numerical verification integrated original Cartesian `x` interval lengths over
the original `yz` ellipse with an oblique normal. This calculation does not use
the scaled-ball rotation. Seven cases included full and zero volumes, tangent
offsets, and three genuine caps. Additional finite differences and complementary
volumes checked five offsets, including tangencies.

## I4-008: nearby poles

The integrand is bounded at zero for positive parameters and has an `x^-4`
tail. Partial fractions initially give a difference divided by `b^2-a^2`.
Cancellation before numerical substitution gives the stable positive expression
`pi/[2ab(a+b)]`. The coincident value `pi/(4a^3)` is separately derived by
differentiating `integral dx/(x^2+a^2)=pi/(2a)` under a uniform local positive
parameter bound. This verifies the repeated denominator without relying solely
on a limit of the simplified formula.

The original integral's partial derivative in `a` has integrable local bound
`2M/(x^2+m^2)^3` when both parameters lie between positive `m` and `M`. Its
value is `-J(a,b)(1/a+1/(a+b))`. The diagonal derivative is the sum of two
partials, a distinction made explicitly. The small-`a` divergence agrees with
the nonintegrable endpoint kernel at `a=0`. Symmetry, monotonicity, and cubic
scaling independently verify the expression.

Numerical quadrature maps the half-line directly to a finite interval, without
partial fractions. Checks include equality, a relative parameter difference of
`1e-10`, and disparate scales. Finite differences verify the partial derivative;
separate quadrature of the single-denominator integral verifies the coincident
parameter differentiation argument.

## I4-009: accumulated matrix response

For SPD `A` with spectral gap `m_0`, the resolvent norm is at most
`1/(m_0+s)`. Its square is norm integrable, so the entrywise improper integral
exists. Differentiating the inverse identity in `s` gives `dR/ds=-R^2`.
The finite-cutoff integral is exactly `A^-1-(A+S I)^-1`, with explicit remainder
norm bound `1/(m_0+S)`, proving `M(A)=A^-1`.

For the continuously differentiable SPD path, the inverse derivative is
`-R H R`, and the square's derivative is the ordered sum
`-R H R^2-R^2 H R`. A local spectral gap `m>0` and derivative bound `K` give
the uniform integrable majorant `2K/(m+s)^3`. The differentiated integral can
therefore be integrated entrywise. Its integrand is also
`d(R H R)/ds`, so the answer is `-A_0^-1 H A_0^-1`. No commutation assumption
is used. Differentiating `A M(A)=I` supplies a separate derivation, and the
eigenbasis entry `-H_ij/(lambda_i lambda_j)` identifies the error that a scalar
power rule would introduce. The positive-definite domain excludes both a zero
eigenvalue's divergent lower endpoint and negative eigenvalues' interior poles.

Numerical checks integrate three actual two-by-two matrix resolvents after a
half-line coordinate transformation. Two SPD examples use a symmetric
perturbation that does not commute with the matrix; the repeated-eigenvalue
example checks that no varying-eigenvector argument is needed. Entrywise finite
differences of the numerical integral agree with the ordered perturbation
formula.

## I4-010: moving Gaussian truncation

The coordinate `u=t-x` preserves the oriented integral as
`integral_0^(t+L) exp(-u^2)du`, including negative upper bounds. Its derivatives
are `exp(-(t+L)^2)` and `-2(t+L)exp(-(t+L)^2)`. The original-coordinate
Leibniz rule gives the same first derivative: a boundary term of one cancels
the upper endpoint contribution from the kernel derivative, leaving the lower
endpoint Gaussian. Local compactness justifies this calculation for every finite
input.

The Gaussian mass is derived in the solution by squaring the positive half-line
integral and using polar coordinates, giving `sqrt(pi)/2`. The two limits have
opposite signs. For `T=|t+L|>0`, comparison of a Gaussian tail with
`u exp(-u^2)/T` bounds the error by `exp(-T^2)/(2T)`. The exceptional point
`t=-L` is treated exactly rather than assigned the singular error bound.

Numerical checks integrate the original `x` coordinate directly, including
negative orientation, and use finite differences for both derivatives. The
shifted error-function value and the explicit tail bounds are verified at five
inputs spanning the center and both tails.

## I4-011: circular aperture transform

Compactness justifies integrating the exponential series in angle and radius.
Reflection eliminates the imaginary part and makes the answer even in signed
`q`. The even angular moments give the locally defined Bessel series `J_0`.
Termwise radial integration gives the regular even series
`pi a^2 sum (-1)^m(qa)^(2m)/(4^m m!(m+1)!)` and the representation
`2 pi a J_1(qa)/q` away from zero. The series defines `J_1` locally and shows
its oddness and the removable value `pi a^2` at zero.

Direct cosine Taylor inequalities, rather than a formal series truncation,
give
`F=pi a^2-pi a^4 q^2/8+E`, with `0<=E<=pi a^6 q^4/192` for every real `q`.
The bound is useful when `|qa|` is small. Direct differentiation at zero gives
the disk second moment `-pi a^4/4`, independently checking the quadratic
coefficient. Radius scaling and the geometric area bound give further checks.

Numerical verification uses direct angular/radial cosine quadrature and an
independently evaluated `J_1` series. Seven wavenumbers include zero, both signs,
small arguments, and a strongly oscillatory case. Every sampled quadratic error
satisfies the explicit bound.

## Validation and remaining integration work

The standard-library script `/workspace/scratch/expansion-i4-checks.py` passed
**87 independent quadrature, finite-difference, symmetry, and remainder-bound
checks**. The manuscript parser verifies eleven matching statements/hint
ladders/solutions; all five new entries have exactly three hints, all required
step labels, and successful conversion through the existing Markdown-to-TeX
converter. Whitespace/diff checks passed.

These are author analytical and numerical checks, rather than external human
review. The primary editor integrates permanent regression checks, review-ledger
updates, generated sources, production build checks, and PDF/website layout
validation. No independent external reader result is claimed here.
