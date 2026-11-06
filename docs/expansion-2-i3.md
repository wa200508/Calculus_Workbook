# Second expansion: five advanced integral problems

Date: November 6, 2026. Author/reviewer: Codex agent `audit_i3`.
Baseline: `d272310f466aaa0ea8c5cf585481c5ab39321dbc`.
Changed manuscript: `INTEGRATION_DOMAINS.md`, adding I3-015 through I3-019.
All fourteen previous statements, hint ladders, and complete solutions were
preserved exactly. The new problems each have a fully typed statement, exactly
three graduated hints, and complete calculations with domain qualifications
and independent checks. No shared counts, generated sources, or publication
configuration were edited by this agent.

## I3-015 — Logarithmic principal value (backlog proposal 12)

For fixed `0<a<1`, separate the numerator into its pole value `ln(a)` and
the difference `ln(x)−ln(a)`. The former has symmetric principal value
`ln(a) ln((1−a)/a)`. The latter divided by `x−a` has removable value `1/a`
at the pole and an integrable logarithmic endpoint at zero. Scaling `t=x/a`
and integrating the real dilogarithm derivative gives

`J(a)=ln(a)ln((1−a)/a)+Li₂(1)−Li₂(1−1/a)`.

The real dilogarithm is defined locally by its integral for real arguments
at most one, so no complex branch convention is concealed. Differentiating
and fixing constants at endpoints proves the two functional identities
needed to reduce the answer to

`J(a)=2Li₂(1)−Li₂(a)−(ln(a))²/2 = π²/3−Li₂(a)−(ln(a))²/2`.

This exposes both endpoint limits: negative infinity at zero and `π²/6`
at one. The endpoint at one is an ordinary convergent integral because the
numerator cancels the pole there; at an interior pole the two one-sided
integrals diverge separately, and at zero the logarithmic primitive diverges.
The value at `a=1/2` is independently `π²/4`.

Independent review by agent `audit_d4` caught a derivative-domain wording
omission in the initial draft: writing the derivative formula for all
nonzero arguments in the stated real domain would include `s=1`. The
published draft now restricts that formula to `s<1`, separately states the
derivative one at zero, and notes the divergent left derivative at one.
The finite value at one and every final principal-value formula were
unchanged. This was a real endpoint-hypothesis correction, not a numerical
failure.

The supplemental checks integrate the pole-subtracted quotient independently
after the logarithmic coordinate `x=exp(−t)`. Its transformed integrand is
`(t+ln(a))/expm1(t+ln(a))`, with removable value one. Seven interior parameters
including near-endpoint values agree with the dilogarithm result. Finite
symmetric exclusions satisfy the explicit omitted regularized-interval bound
`2δ/(a−δ)`. Endpoint and half-interval checks also pass.

## I3-016 — Triaxial ellipsoid area (backlog proposal 14)

The angular tangent cross product is

`(bc sin²θ cosφ, ac sin²θ sinφ, ab sinθ cosθ)`.

Its norm equals `sin(θ) ||diag(bc,ac,ab)n||` for the unit spherical vector
`n`. Octant reflection gives an explicit bounded double quadrature on
`[0,π/2]²`. Since the norm factor lies between `bc` and `ab`, the area lies
between `4πbc` and `4πab`. The positive lower norm prevents a quadrature
singularity. The map's pole degeneracies and its seam identification are
explained separately; neither is a singularity of the ellipsoid itself.
The spherical limit is `4πr²`.

Cauchy--Schwarz bounds the norm's theta derivative by `ab` and its phi
derivative by `ab sin(θ)`. For the complete octant integrand this gives
Lipschitz bounds `√2 ab` and `ab`. Integrating the distance from each
midpoint over every cell yields the explicit absolute quadrature error

`|S−S_NM| ≤ (π³ab/4)(√2/N+1/M)`.

The solution supplies a direct selection rule for the mesh from a requested
absolute tolerance and distinguishes floating-point evaluation from this
mathematical discretization error. No convergence rate is inferred merely
from agreement of successive grids.

Independent checks use the coordinate `z=cos(θ)` to remove the sine measure
and evaluate a different finite quadrature. Three nonspherical axis sets
and a sphere agree with the original midpoint sums within their stated
bounds. Numerical angular derivatives obey the Lipschitz bounds.

## I3-017 — Off-axis circular kernel (backlog proposal 19)

Put `d=√((a+ρ)²+z²)` and `δ=√((ρ−a)²+z²)>0`. Half-angle factorization gives
parameter `m=4aρ/d²`, with complementary modulus `κ′=√(1−m)=δ/d`. The locally
defined complete elliptic integral uses the **parameter** convention
`K(m)=∫₀^(π/2)(1−m sin²u)^(−1/2)du`, matching the new I4 elliptic-integral
problem. Reflection of the angular integral gives the exact result
`P=4K(m)/d`. At `ρ=0` it gives `2π/√(a²+z²)`, independently recovered by
the constant original integrand.

The primary source [NIST DLMF Equation 19.12.1](https://dlmf.nist.gov/19.12.E1)
was opened and verified on November 6, 2026. The text explicitly converts its
modulus-based notation to the book's parameter convention. Its complementary
expansion and the constant stated after Equation 19.12.3 give
`K(1−ε²)=ln(4/ε)+O(ε²ln(1/ε))`. Therefore

`P=(4/d)[ln(4d/δ)+O((δ/d)²ln(d/δ))]`

and, for fixed ring radius and any approach to the ring,

`P=(2/a)ln(8a/δ)+o(1)`.

Replacing `d` by `2a` changes the expression by a term bounded in order by
`δ ln(a/δ)/a²`, which tends to zero, so the additive constant is retained.
The exact-source angular kernel has two inverse-angle endpoint tails,
providing an independent explanation of the coefficient `2/a`. Off-ring
bounds are `2π/d ≤ P ≤ 2π/δ`.

Checks compare original-angle quadrature with arithmetic-geometric-mean
elliptic evaluation, including the axis and a near-ring observation. They
also check evenness in `z`, the geometric bounds, and convergence of the
explicit logarithmic asymptotic along both vertical and radial approaches.

## I3-018 — Weighted panel and zero-distance derivative (backlog proposal 21)

The problem extends the backlog's zero-distance linear-weight integral to
nonnegative observation distance. The signed weight is bounded on the panel,
so an integrable multiple of `1/√(x²+y²)` dominates the absolute integrand
for every distance. The integral is therefore absolutely convergent even
at zero, regardless of the signs of the weights.

The Duffy map `x=u,y=uv` has Jacobian `u` and `c(v)=√(1+v²)`. Exact radial
integration gives

`A₀=(√(c²+h²)−h)/c²=1/(√(c²+h²)+h)`

and

`A₁=√(c²+h²)/(2c²)−h² asinh(c/h)/(2c³)`.

The remaining bounded integral is
`∫₀¹[αA₀+(β+γv)A₁]dv` for positive `h`. At zero the three moments are
`asinh(1)`, `asinh(1)/2`, and `(√2−1)/2`.

The exact right derivative at zero is `−πα/4`, determined only by the
vertex value of the weight. Rationalization and monotonicity of the radial
moments give the explicit bound

`|L(h)−L(0)+(πα/4)h| ≤ (h²/2)[|α|+(|β|+|γ|)asinh(√2/h)]`.

Thus a vanishing vertex weight removes the term linear in distance. When
`α=0`, the weight has magnitude at most a constant times radial distance,
and the distance-derivative integrands are dominated by an integrable
multiple of `1/R`. This justifies derivative interchange at zero with
value zero, and a continuously differentiable even distance extension.
For nonzero `α`, the zero pointwise derivative cannot reproduce the
nonzero integrated right derivative; that interchange fails. The text
makes no unsupported second-derivative claim from the logarithmic bound.

Independent polar moments verify all three exact values and the constant
weight's derivative coefficient. Supplemental numerical checks use direct
Cartesian integration in `y`, followed by one-dimensional quadrature in
`x`, for positive distances and mixed signed weights. They also verify the
signed-combination remainder bounds and right difference quotients.

## I3-019 — Finite Fresnel aperture (backlog proposal 24)

The locally defined Fresnel convention has phase `πt²/2`. Rescaling the even
finite integral gives

`I(k;a)=√(2π/k)[C(a√(2k/π))+iS(a√(2k/π))]`.

The complete real-line oscillatory integral is evaluated using positive
Gaussian damping. For each positive damping value, differentiation in the
real parameter `k` and an ordinary integration by parts give
`Gε′(k)=iGε(k)/(2(ε−ik))`, with real Gaussian initial value `√(π/ε)`.
Solving the scalar equation selects the root positive at `k=0` and yields
`Gε=√π/√(ε−ik)`. A separate monotone-amplitude integration by parts gives
uniform damped and undamped tails at most `1/(kA)` on either half-line,
proving both ordinary convergence and the validity of removing the damping.
The limit is `G=√(π/k)exp(iπ/4)`.

Integrating by parts only on tails separated from zero gives

`I=√(π/k)exp(iπ/4)+exp(ika²)/(ika)+R`,

`|R|≤1/(k²a³)`.

The error bound follows from one more tail integration by parts and the
absolute integral of `x^(−4)`. Both endpoint contributions and their phase
sign are retained. The text never divides by the vanishing phase derivative
at the interior stationary point. For small parameter the independent
finite Taylor bound is
`|I−2a−2ika³/3|≤k²a⁵/5`, which checks the Fresnel normalization.

Independent agent `audit_d4` and the primary agent rederived the Gaussian
ODE, uniform tails, endpoint sign, and remainder constant with agreement.
Supplemental checks compare direct finite complex quadrature with the
Fresnel scaling, the asymptotic enclosure, the wrong-sign endpoint alternative,
and the small-parameter bound. Gaussian-damped numerical integrals check the
complex-root branch independently; finite damped and undamped tails obey
the uniform bounds.

## Executed evidence and scope

`python3 /workspace/scratch/expansion2-i3-checks.py` passed **157 independent
numerical checks** on November 6, 2026, using only Python's standard library.
The checks use independent coordinates, direct quadrature, series, and
arithmetic-geometric-mean evaluation; they do not prove the analytical
convergence and interchange claims by themselves.

The content parser accepted **19** matching I3 statement/hint/solution IDs.
All five additions have exactly three hints and the required SETUP, CHOICE,
CALCULUS, ALGEBRA, DOMAIN, and CHECK material. The fourteen previous entries
were compared against `d272310` without changes. The manuscript was frozen
for root-level layout compilation after the endpoint-domain correction and
a successful supplemental run. Site/PDF checks and broader review evidence
are recorded by the primary agent; this note does not claim external human
review, a new release, or full-book usability verification.
