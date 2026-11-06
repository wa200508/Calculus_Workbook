# Independent review of the second integration expansion

Review date: 2026-11-06. Reviewer: independent integration review agent
`audit_reference_exercises`. Starting repository baseline: `d272310`.
Reviewed additions: I4-012–016 and I3-015–019, in the authors' completed
working-tree manuscripts. The I4-014 speed expression was subsequently moved
to a display for page fit without changing its mathematics.

## Method and result

I derived the ten expected results before reading the authors' solutions and
recorded those calculations in the session scratch file
`/workspace/scratch/integration-expansion-2-expectations.md`. I then read every
new statement, all three hints, and every solution step, checking types,
dependencies, dimensions, orientations, algebra, endpoint prescriptions,
parameter ranges, differentiation hypotheses, and stated error estimates.

All ten additions pass this independent analytical review in their final
wording. A third reader identified one local hypothesis omission in I3-015:
the initially stated dilogarithm derivative formula included its endpoint
`s=1`. The author restricted it to `s<1`, `s != 0`, retained the removable
derivative at zero, and explicitly stated that the left derivative diverges
at one. I verified that correction in the final source. It does not change
the principal-value answer or either endpoint limit. No other mathematical
correction was required by this review.

The maintained stdlib script `scripts/check_integration_expansion_2.py`
passes **197 labeled checks**, covering every addition. Its comparison
helpers reject nonfinite real/complex operands, nonfinite or negative
tolerances, and invalid interval bounds/slack. This is supplementary
numerical evidence, not a replacement for the analytical arguments below.

## Per-problem analytical checks

### I4-012 — Gaussian on a rotated ellipsoid

For SPD `Q`, the positive square-root substitution gives unit-ball measure
`det(Q)^(-1/2) dy`. The radial constant is
`C = pi^(3/2) erf(1) - 2 pi/e`, so the integral is `C/sqrt(det Q)`.
The source correctly transforms the moving domain before differentiating;
it does not discard its boundary motion. Jacobi's determinant derivative
gives `-N tr(Q^(-1)H)/2`, with a local positive spectral gap controlling
domination. No commutation of `Q` and its perturbation is needed.

For the specified example, the eigenvalues are `3+t, 1-t, 4`, the SPD
interval is `(-3,1)`, `N(0)=C/(2 sqrt(3))`, and
`N'(0)=C/(6 sqrt(3))`. The determinant and orientation signs agree.
The maintained checker instead integrates original-direction Cartesian
rays up to their ellipsoidal boundary, checks a general rotated SPD case
and the sphere, and differentiates that independent quadrature. Excluded
SPD endpoints are tested as zero determinants, not evaluated as finite
Gaussian integrals.

### I4-013 — Hyperboloidal shell

Original horizontal sections have radius `R(z)=a sqrt(1+z^2/c^2)`.
Their integrated area gives volume
`2 pi a^2 (H+H^3/(3c^2))`. The outward lateral vector area is
`(R cos(theta),R sin(theta),-R R') dtheta dz`, whose dot product
with `F=(x,y,z)` is the constant `a^2`.
Thus the lateral flux is `4 pi a^2 H`; each cap contributes
`pi a^2 H(1+H^2/c^2)`, including the lower cap with its downward
normal. Their sum is three times the volume. The specified positive
length hypotheses make all surfaces and orientations well defined.

The numerical checks independently integrate sections, each signed cap,
and the lateral parameterization for different aspect ratios and a
near-cylindrical case. They do not replace a positive-height surface by
the degenerate `H=0` object.

### I4-014 — Weighted ellipse

With `m=1-b^2/a^2`, the original line integral reduces to
`4a^3 integral sin^2(u) sqrt(1-m sin^2(u)) du`. Integrating the derivative
of `sin(u)cos(u)sqrt(1-m sin^2(u))` verifies the reduction

`4a^3 ((2m-1)E(m)+(1-m)K(m))/(3m)`.

Both special functions use the parameter `m`, consistently with I3-017.
The circle is evaluated by its continuous limit `pi a^3`; direct
substitution into the divided expression would give `0/0`.
The geometric bounds `pi a^2 b <= W <= pi a^3` are correct.
Taylor expansion at fixed `a`, uniformly for `0 <= m <= m0 < 1`, yields
`pi a^3(1-3m/8-5m^2/64)` and a nonpositive remainder with magnitude
at most `35 pi a^3 m^3/[1024(1-m0)^(5/2)]`. The factor follows from
the third derivative of the square root and the integral of `sin^8`.
No uniformity at the collapsed-ellipse limit is claimed.

Original full-angle line quadrature is compared with AGM evaluation of
`K` and an independently integrated binomial series for `E`. Circle,
near-circle, eccentric, geometric-bound, and signed Taylor-remainder
cases pass.

### I4-015 — Gaussian matrix moment

After translating by the stated fixed center, parity and one-dimensional
Gaussian moments give `Z=pi^(3/2)/sqrt(det A)`,
`M=(Z/2)A^(-1)`, and covariance `Sigma=A^(-1)/2`.
The matrix derivative must retain the order `A^(-1) H A^(-1)`.
The source correctly obtains

`M' = -Z tr(A^(-1)H) A^(-1)/4 - Z A^(-1)H A^(-1)/2`

and `Sigma'=-A^(-1)H A^(-1)/2`. Local Gaussian majorants with
degree-two/four polynomial factors justify the original-integral
derivatives. The fixed center is not inadvertently differentiated.
For the example the off-diagonal covariance is `-1/10` at zero and
its derivative is `-7/50`; the SPD interval and normalization agree.

Original Cartesian cube quadrature computes normalization, all six
independent moment entries, and original-kernel perturbation derivatives.
Two genuinely noncommuting perturbation cases check both derivative
terms and normalized covariance derivatives. A second Cartesian grid
checks discretization in the representative last case, which has the
largest eigenvalue. The tested matrices have a positive lower bound
at least `.8`; Gaussian polynomial tails outside the cube of half-width
7 are smaller than `1e-11`. These finite numerical checks do not assert
that all SPD perturbations are uniformly controlled by that same bound.

### I4-016 — Logarithmic difference quotient

The identity `(x^a-x^b)/ln x = integral_b^a x^s ds` gives both the sign
and an integrable absolute bound for `a,b>-1`. Parameter integration
then gives `ln((a+1)/(b+1))`; its partials are `1/(a+1)` and
`-1/(b+1)`. The removable value at `x=1` is `a-b`.
At `x=0`, equal exponents give the identically zero quotient even
when negative; unequal negative exponents can give an unbounded but
integrable endpoint. The source keeps these cases distinct.

Writing `alpha=a+1`, `beta=b+1` exposes the joint boundary: ratios
`alpha/beta -> r` give `ln r`; zero/infinite ratios give divergent
limits. There is no joint continuous extension at `(-1,-1)`.
Placing just one exponent exactly at `-1` produces the correctly
signed divergent integral. Numerical checks use the original quotient
under `x=exp(-u/rate)`, with the slowest decay scaled to one; signed,
equal, negative-exponent, partial-derivative, and fixed-ratio boundary
paths all pass. The retained tail after scaled coordinate 40 is
exponentially negligible for those checks.

### I3-015 — Interior logarithmic pole

For `0<a<1`, the ordinary one-sided integrals diverge with opposite
signs; only the specified equal-coordinate principal value is assigned.
Subtracting `ln a` leaves a removable quotient and gives the pole
counterterm `ln a ln((1-a)/a)`. The real dilogarithm primitive and its
reflection/inversion identities yield

`J(a)=pi^2/3-Li_2(a)-(ln a)^2/2`.

The endpoint limits are `-infinity` at zero and `pi^2/6` at one.
The exactly placed endpoint kernels respectively remain divergent or
become removable, as the source explains. The midpoint value is
`pi^2/4`. The corrected special-function derivative hypothesis described
above excludes the non-differentiable endpoint while retaining its
finite function value.

The checker subtracts the pole before integrating, then uses `x=exp(-t)`
to obtain the ordinary integrand `w/expm1(w)`, with `w=t+ln a`.
It compares this with a convergent dilogarithm series and reflection
identity and carries the explicit omitted-tail bound
`(2/a)exp(-40)(41+|ln a|)`. It never asks a quadrature routine to
cross the unregularized pole or treats the PV as an ordinary integral.
The ordinary removable endpoint at `a=1` is independently integrated
as `t/expm1(t)` after the same logarithmic coordinate change; its
omitted tail is bounded by `41 exp(-40)/(1-exp(-40))`.

### I3-016 — Triaxial ellipsoid surface area

The two tangent derivatives have the stated cross product, whose norm
is `sin(theta) ||diag(bc,ac,ab)n||`. Eight octants give the correct
finite rectangle, with no orientation sign in area. The angular poles
and identified seam are zero-measure coordinate sets; the level-set
gradient establishes regularity of the actual surface.
Singular-value bounds give `4 pi bc <= S <= 4 pi ab`, and uniform
convergence to a common positive radius gives `4 pi r^2`.

The supplied midpoint error estimate is deliberately conservative but
rigorous. The derivative bounds `|f_theta|<=sqrt(2)ab` and
`|f_phi|<=ab`, combined with mean distances `Delta/4` in each cell,
give exactly `pi^3 ab (sqrt(2)/N+1/M)/4`. The source properly excludes
floating-point evaluation error from that mathematical quadrature bound.

Independent original Cartesian height graphs, regularized at their rim,
agree with the angular quadrature. Sphere, physical axis permutations,
area bounds, and midpoint enclosures pass. Equal axes are tested as the
continuous limiting formula, not as a counterexample to the problem's
strict ordering assumption.

### I3-017 — Off-axis ring

The half-angle identity gives `d^2=(a+rho)^2+z^2`,
`delta^2=(rho-a)^2+z^2`, `m=4a rho/d^2`, and
`P=4K(m)/d`. The hypotheses imply `0<=m<1`. The source explicitly
distinguishes the parameter from DLMF's modulus `sqrt(m)` and its
complement `sqrt(1-m)=delta/d`, consistently with I4-014.
The axis result `2 pi/sqrt(a^2+z^2)`, reflection in `z`, and bounds
`2 pi/d <= P <= 2 pi/delta` are correct.

The cited complementary-modulus expansion includes the necessary
constant `ln 4`. Substitution gives the leading geometric expression
`(2/a)ln(8a/delta)+o(1)` for every approach to the ring with fixed
positive `a`. Replacing `d` by `2a` makes an additive error of order
`delta ln(a/delta)/a^2`, which tends to zero. At the actual source,
the positive logarithmic singularity cannot be canceled by a PV.
Original angular quadrature agrees with the independent AGM, including
axis, both sides of the ring, reflected, and near-ring cases. The
near-ring asymptotic comparisons are finite numerical spot checks;
the source's justified expansion supplies the limiting theorem.

### I3-018 — Linearly weighted triangle

The triangle's vertex kernel is absolutely area-integrable for every
fixed signed affine weight. The positive Duffy Jacobian is `u`.
Both radial primitives are correct, including the `h^2 asinh(c/h)`
term and the rationalized constant-weight primitive. At zero distance
the moments are `asinh(1)`, `asinh(1)/2`, and `(sqrt(2)-1)/2`.

The remainder estimate

`|L(h)-L(0)+pi alpha h/4| <= h^2[|alpha|+(|beta|+|gamma|)asinh(sqrt(2)/h)]/2`

is valid with arbitrary signs, and gives the right derivative
`-pi alpha/4`. The source correctly distinguishes differentiation at
zero: it fails under the original integral when `alpha != 0`, while
for `alpha=0` an integrable `C/R` majorant permits it and gives a
continuous derivative. Its even extension has the stated cusp or
continuous first derivative; no unjustified second derivative is
inferred from an upper remainder bound.

Original Cartesian strip integration agrees with the Duffy primitives
for each pure moment, signed mixtures, zero vertex weight, zero weight,
zero distance, and positive distances. The quantitative derivative
remainder is checked with the signs of the weights retained.

### I3-019 — Finite Fresnel integral

The locally defined Fresnel convention gives
`sqrt(2 pi/k)(C(s)+i S(s))`, `s=a sqrt(2k/pi)`.
The uniform damped-tail bound `1/(kA)` follows by integration by
parts only on `x>=A>0`; it proves separate convergence of the two
ordinary oscillatory tails and justifies the damping limit. It does
not claim absolute convergence of the undamped full-line integral.
The Gaussian parameter ODE, initial value, and square-root branch
produce `sqrt(pi/k) exp(i pi/4)`.

Two further integrations by parts away from the stationary point give
the endpoint term `exp(i k a^2)/(i k a)` and remainder at most
`1/(k^2 a^3)`. The phase sign, length units, and relative error
scaling are correct. At small `k`, the independent Taylor estimate
is `2a+2 i k a^3/3` with error at most `k^2 a^5/5`.

Finite original-coordinate complex quadrature agrees with an independent
Fresnel power series, checks the controlled large-parameter and
small-parameter remainders, the magnitude bound, and the continuous
zero/negative-parameter extensions. Absolutely convergent damped
Gaussian quadrature retains its explicit omitted-tail bound. Undamped
tail checks are finite intervals compared with the proved uniform
bound, not numerical evaluations of a conditionally convergent
infinite interval.

## Scope and limitations

This review covers all ten newly added integration statements, their
hints, and their full solutions. It does not recertify earlier problem
bodies or replace the independent reviews of the new differentiation
chapters. Numerical tests sample admissible cases and limiting
extensions; their generic finite quadratures are not interval-arithmetic
certificates. The analytical review separately verifies all convergence,
interchange, orientation, branch, and explicit error-bound claims.
An independent code reader (`audit_d4`) found no blocking numerical
implementation defect and bounded the worst tested degree-four Gaussian
cube tail by `2.00e-12`. Their review also prompted replacing one
tautological dilogarithm endpoint assertion with the independent ordinary
endpoint integral above, without changing the 197-check count.
Parent-agent structure, build, and regression checks are recorded in
the shared release evidence rather than duplicated here.
