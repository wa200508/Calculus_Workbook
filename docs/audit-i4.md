# Analytical review: parameter integrals and geometric accumulation

Reviewed November 5, 2026 by the Codex `audit_i4` reviewer against manuscript
revision `8963e970e9ec23d4114203b205fccc9b7ca1c85d`, with the corrections below.
This record covers the statements, three hints, complete calculations, domain
arguments, and checks of I4-001 through I4-006. It is an analytical review by an
AI reviewer, supplemented by numerical checks; it is not external reader or
human peer-review evidence.

## Findings and corrections

1. **I4-001, Step 4: incorrect description of Tonelli's endpoint scope.** The
   previous text said the positive-parameter interchange does not extend to
   `a=0`. In fact, at `a=0<b` the double integrand is nonnegative, so Tonelli
   still applies, with both iterated integrals equal to positive infinity.
   The corrected text distinguishes an allowed interchange of nonnegative
   integrals from the existence of a finite integral. The finite positive-
   parameter answer and the divergent endpoint value were already correct.
2. **I4-003, Step 5: make the uniform tail argument explicit.** The previous
   argument stated the correct type of tail bound without calculating it.
   The revised solution proves the bound `2/(q R)` for every positive
   frequency `q`, lower cutoff `R`, and nonnegative damping. This supports
   convergence of the ordinary undamped integral and interchange of the
   damping limit using uniform tails, without assuming absolute convergence.
3. **I4-006, statement: declare the observation parameter dimensionless.** This
   makes its type agree explicitly with the dimensionless coordinates in
   `x^2+y^2+h^2`.

No incorrect finite integral value, sign, branch, endpoint derivative, or flux
orientation was found in these six problems.

## Problem-by-problem evidence

### I4-001 — A difference of exponential kernels

- For fixed positive `a,b`, the Taylor numerator is `(b-a)x+O(x^2)` and the
  quotient extends to `b-a` at zero. Its absolute tail is bounded by an
  exponentially decreasing function. Hence the original difference, rather
  than either separated term, is absolutely integrable.
- Integrating `exp(-s x)` from `a` to `b` gives the stated kernel. For increasing
  parameter limits Tonelli applies directly; reversing the interval reverses
  the sign. Subsequent integration gives `ln(b/a)`, with sign and zero value
  consistent under interchange or equality of `a,b`.
- At `a=0<b`, the original integrand is nonnegative and has a `1/x` tail. Tonelli
  gives `integral_0^b ds/s=+infinity`, agreeing with the positive-parameter
  limit. This is the conceptual correction described above.
- Independent direct quadrature covered `b>a`, `b<a`, `b=a`, and disparate
  positive parameters. Exponential tail cutoffs were selected using the
  smaller parameter. The parameter derivative in `b` also independently
  yields `1/b`, fixing the dependence on the ratio.

### I4-002 — A logarithmic kernel on a finite interval

- The integrand extends continuously to `a` at zero for every `a>-1`.
  A compact neighborhood of such a parameter has a uniformly positive
  denominator `1+a x`; differentiating under this finite-interval integral
  therefore gives `integral_0^1 dx/(1+a x)`. Its value is
  `ln(1+a)/a`, with value one at `a=0`.
- After division by `x`, logarithm-series terms have uniform summable
  bounds `|a|^n/n` for `|a|<1`. Integrating each monomial gives the
  coefficient `(-1)^(n+1) a^n/n^2`. The signs agree with the first derivative
  at zero.
- Substitution `u=-a x` in the stated real integral definition of the
  dilogarithm gives `J(a)=-Li_2(-a)`; its sign and oriented upper limit also
  work for negative `a`. The real definition is available for all `-a<1`,
  exactly the domain `a>-1`.
- At `a=-1`, the only nonremovable endpoint singularity is logarithmic at
  `x=1`. It is integrable. Monotone convergence applied to the nonnegative
  kernels with `a=-r` gives `-sum(1/n^2)=-pi^2/6`. The derivative instead
  tends to positive infinity.
- Independent quadrature verified the series on positive and negative
  parameters, the parameter derivative including zero, and the endpoint
  value. For the endpoint, the independent substitution `x=1-exp(-t)`
  produces `-t/(exp(t)-1)`, avoiding direct quadrature of a logarithmic
  endpoint.

### I4-003 — A damped difference of oscillatory kernels

- The cosine numerator is `(c^2-b^2)x^2/2+O(x^4)` at zero. For positive
  damping the original quotient is therefore absolutely integrable at both
  endpoints, including when either frequency is zero.
- Differentiation in `c` produces `exp(-a x) sin(c x)`, dominated by
  `exp(-a x)`. Its Laplace integral is `c/(a^2+c^2)`. Integrating in frequency
  from `b` to `c` gives one half of the logarithm of
  `(a^2+c^2)/(a^2+b^2)` and fixes the constant at equal frequencies.
- With `f_a(x)=exp(-a x)/x`, integration by parts against `sin(q x)/q`
  bounds a finite tail by `2 f_a(R)/q <= 2/(q R)`, uniformly for `a>=0`
  and positive `q`. Each undamped tail converges. On finite intervals the
  original cosine difference has a removable endpoint and a uniform bound.
  These two facts justify the damping limit `ln(c/b)` for positive `b,c`.
- If exactly one frequency is zero, the logarithmic formula diverges with
  the sign stated in the manuscript. If both vanish, the integrand is zero.
- Independent quadrature used a product-of-sines expression for the cosine
  difference to avoid cancellation at zero. Cases included both zero-
  frequency alternatives, equal frequencies, and both signs of the result.

### I4-004 — A weighted logarithm with limiting parameter values

- The substitution `x=cos(theta)` on `(0,pi)` reverses the bounds and has
  negative derivative. These signs cancel, and the positive square root is
  `sin(theta)`, giving the stated angular logarithm integral.
- For each interior parameter a positive lower bound on
  `1+lambda cos(theta)` justifies parameter differentiation. The decomposition
  into a constant and the reciprocal cosine denominator is valid away from
  zero. At zero the derivative integral is zero by reflection.
- The half-angle substitution gives the positive quadratic
  `(1+lambda)+(1-lambda)u^2` and hence the reciprocal integral
  `pi/sqrt(1-lambda^2)`. Integrating the derivative and imposing `J(0)=0`
  yields `pi ln((1+sqrt(1-lambda^2))/2)`. Direct differentiation and evenness
  independently verify the result.
- At either endpoint, the angular logarithm has an integrable logarithmic
  singularity. The displayed lower bound `(1+cos(theta))/2` supplies a
  parameter-independent integrable logarithmic majorant near `lambda=1`.
  Reflection covers the other endpoint. Both values are `-pi ln(2)`.
  At `lambda=1`, the angular derivative is asymptotic to a negative constant
  times `(pi-theta)^(-2)`; the other endpoint is reflected. Thus neither
  gives a finite endpoint parameter derivative.
- Independent angular quadrature checked five interior parameters and the
  endpoint value. The endpoint calculation used an exponential approach to
  the angular endpoint to resolve the integrable logarithm.

### I4-005 — Flux through a translated ellipsoid

- Substitution of the origin into the ellipsoid inequality shows that the
  source is inside exactly when `|d|<a`. At `d=+/-a` it lies on the surface;
  these values are excluded from the statement.
- Direct coordinate differentiation gives zero divergence of
  `r/|r|^3` on the punctured space. For an exterior source the field is smooth
  on a neighborhood of the complete bounded volume, so the flux is zero.
- For an interior source, a sufficiently small ball lies within the ellipsoid.
  The punctured-volume theorem has an inward radial normal on its inner
  sphere. The radial flux of that sphere with its own outward normal is
  `(1/epsilon^2)(4 pi epsilon^2)=4 pi`, so the outer ellipsoid flux is positive
  `4 pi`. This verifies the sign as well as source placement.
- Consequently the two one-sided limits at `d=a` are `4 pi` and zero in the
  order stated. These limits do not prescribe a value for the excluded
  source-on-surface integral.
- An independent triaxial surface parameterization was integrated numerically
  at the central source, two positive/negative interior translations, and
  two positive/negative exterior translations. The direct fluxes agree with
  the excision result without using a spherical integration boundary.

### I4-006 — A panel kernel at positive observation distance

- For each positive `h` the kernel is continuous on the compact triangle.
  The map `x=u,y=u v` is one-to-one for `u>0`; its collapsed boundary is
  negligible and its absolute Jacobian is `u`. Integrating that radial
  coordinate gives `(sqrt(1+v^2+h^2)-h)/(1+v^2)` with the correct lower
  endpoint contribution for positive `h`.
- With `A=1+h^2` and `v=sqrt(A) sinh(t)`, the remaining numerator splits as
  `1+h^2/(1+A sinh(t)^2)`. The second coordinate `w=tanh(t)` gives the
  primitive `h atan(h w)`. Evaluating both endpoints and subtracting
  `h integral_0^1 dv/(1+v^2)` reproduces the displayed closed form.
- Rationalization gives a nonnegative remainder, bounded by
  `(h^2/2) integral_0^1 (1+v^2)^(-3/2)dv = h^2/(2 sqrt(2))`.
  Thus the continuous value is `arsinh(1)` and the right derivative is
  `-pi/4`; the bound establishes the difference-quotient limit directly.
- At each fixed positive `h`, compactness justifies differentiating under
  the area integral. The derivative kernel tends to zero away from the
  vertex as `h` decreases to zero. Its integral has the nonzero limit above,
  so an integrable dominating function uniform in `h` cannot exist.
- Independent polar coordinates on the triangle give upper radius
  `sec(theta)`, `0<=theta<=pi/4`, and the integral
  `integral (sqrt(sec(theta)^2+h^2)-h)dtheta`. Quadrature of this expression
  verifies the closed form and remainder bounds from very small to large
  positive `h`. Quadrature of its derivative confirms approach to `-pi/4`.

## Verification scope

The accompanying independent standard-library script
`/workspace/scratch/audit-i4-checks.py` passed **40** quadrature, derivative,
and remainder-bound checks during this review. The transient workspace script
is supplemental evidence; the analytical arguments above explain domain and
convergence conclusions that finite numerical samples cannot establish.
Manuscript generation, site/PDF builds, layout inspection, and release validation
are integration tasks recorded separately by the primary editor.
