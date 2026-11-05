# Independent review of the integration expansion

Reviewed November 5, 2026 by Codex agent `audit_reference_exercises`.
The review covers the ten new statements, their three hints, complete worked
solutions, domain discussions, and checks: I4-007 through I4-011 and I3-010
through I3-014. These additions follow the correction checkpoint `606a472`;
the final expansion revision is recorded in the project review ledger.

Expected formulas and domain traps were derived independently from the proposed
statements before reading the completed solutions. The subsequent comparison
found agreement with every intended result. A spectral-gap naming issue in
I4-009 was identified by the coordinating reviewer and corrected by its author;
the corrected distinction is verified below. No unresolved mathematical finding
remains in these ten additions after that correction. This is an independent
agent review, not human peer review or external reader feedback.

## I4-007 — An oblique ellipsoidal cap

Scaling with $\mathbf D=\operatorname{diag}(a,b,c)$ produces the unit ball,
volume Jacobian $abc$, and transformed normal $\mathbf m=\mathbf D\mathbf n$.
Its length is $\rho=\sqrt{a^2n_1^2+b^2n_2^2+c^2n_3^2}>0$. Rotation then
leaves the volume unchanged and reduces the interior case to
$\pi abc\int_{h/\rho}^1(1-s^2)\,ds$. This independently yields

$$
V(h)=\frac{\pi abc}{3}(1-h/\rho)^2(2+h/\rho)
\quad(-\rho<h<\rho).
$$

The full volume at $h\le-\rho$ is $4\pi abc/3$; the volume at
$h\ge\rho$ is zero. Both tangent-plane equality cases and the interior
derivative $-\pi abc(1-h^2/\rho^2)/\rho$ are correct. Quadratic vanishing
of the cap proves that the derivative is zero at either tangent offset; the
second derivative fails to exist there. The section-area factor
$A_{\rm sec}(h)=-\lVert\mathbf n\rVert V'(h)$ follows because a change
$dh$ in plane offset moves the plane by $dh/\lVert\mathbf n\rVert$.
It is essential for a nonunit normal and has the correct area units.

As an independent numerical reduction, the maintained checker slices along
the original scaled $z$ coordinate. Each slice is a disk cut by an oblique
line, evaluated by the circular-segment area formula. Its quadrature agrees
with the cap expression for positive, negative, zero, tangent, full, and empty
offsets and with interior first derivatives. This slicing direction differs
from the transformed normal used in the worked solution.

## I4-008 — Two nearby poles off the real axis

Unequal-parameter partial fractions independently give
$[\pi/(2a)-\pi/(2b)]/(b^2-a^2)$, which simplifies to

$$
J(a,b)=\frac{\pi}{2ab(a+b)}\qquad(a,b>0).
$$

The coincident result $J(a,a)=\pi/(4a^3)$ also follows directly by
differentiating $\int_0^\infty(x^2+a^2)^{-1}\,dx=\pi/(2a)$.
The manuscript's local bound $2M/(x^2+m^2)^2$ justifies that check;
its bound $2M/(x^2+m^2)^3$ justifies the requested partial derivative of
the original two-parameter integrand. The formula
$\partial_a J=-J(1/a+1/(a+b))$ is correct. In particular the partial
derivative at equality is $-3\pi/(8a^4)$, whereas differentiating along
the diagonal gives twice that value. The zero-parameter divergence and the
asymptotic coefficient $\pi/(2ab^2)$ are correct.

The checker integrates the original rational kernel after $x=\tan\theta$,
without performing a partial-fraction subtraction. It tests unequal, exactly
equal, and nearly equal parameters and compares finite differences with the
partial derivative while keeping the other parameter fixed.

## I4-009 — An accumulated matrix response

For $\mathbf R(s)=(\mathbf A+s\mathbf I)^{-1}$, differentiating the inverse
identity gives $\partial_s\mathbf R=-\mathbf R^2$ and hence

$$
\int_0^\infty\mathbf R(s)^2\,ds=\mathbf A^{-1}.
$$

For the perturbation, the two required terms are
$-\mathbf R_0\mathbf H\mathbf R_0^2-\mathbf R_0^2\mathbf H\mathbf R_0$.
These are also $\partial_s(\mathbf R_0\mathbf H\mathbf R_0)$, yielding
$-\mathbf A_0^{-1}\mathbf H\mathbf A_0^{-1}$ after endpoint evaluation.
The order is correct for noncommuting symmetric perturbations.

The final text now separately defines $m_*$ as the smallest eigenvalue of
$\mathbf A_0$, rather than reusing the gap $m_0$ of the initially fixed
$\mathbf A$. The local quadratic-form estimate uses
$\lVert\mathbf A(t)-\mathbf A_0\rVert<m_*/2$, the uniform lower bound
$m=m_*/2$, and the derivative bound $2K/(m+s)^3$.
Its integral is $K/m^2$. The endpoint product bound in the next step uses
$\lVert\mathbf H\rVert/(m_*+s)^2$, consistently referring to
$\mathbf A_0$. This corrects the naming issue without conflating two
independently introduced matrices. The zero- and negative-eigenvalue exclusions
are valid for the original matrix integral.

The checker independently integrates all four entries of a two-dimensional
resolvent square. The substitution $s=u/(1-u)$ gives a smooth matrix integrand
$((1-u)\mathbf A+u\mathbf I)^{-2}$ on $[0,1]$. Centered differences of
these numerical integrals agree with the ordered derivative for two verified
noncommuting perturbations and for a repeated-eigenvalue scalar matrix.

## I4-010 — A Gaussian with a moving truncation

The shift $u=t-x$ preserves the oriented definition and gives
$G(t;L)=\int_0^{t+L}\exp(-u^2)\,du$. Thus
$G_t=\exp(-(t+L)^2)$ and
$G_{tt}=-2(t+L)\exp(-(t+L)^2)$. The original-coordinate Leibniz
calculation correctly cancels its upper boundary contribution against part of
the integral derivative. Compact rectangles around each finite parameter
justify these operations even when the integration bounds reverse.

The Gaussian half-line integral has value $\sqrt\pi/2$ by the positive
quadrant calculation. Therefore the two limits are $\pm\sqrt\pi/2$,
with the negative sign at $t\to-\infty$. The bound
$\exp(-T^2)/(2T)$ for the omitted tail is correct for $T=|t+L|>0$;
the excluded central value is handled exactly by $G(-L;L)=0$.

Original-coordinate signed quadrature, first and second finite differences,
and both signed tail bounds pass. The checks include $t=-L$, where the
integration interval has zero length but its first derivative is one.

## I4-011 — A circular aperture transform

Reflection cancels the imaginary part and implies evenness in $q$. Angular
moments and radial integration independently yield

$$
F(q;a)=\pi a^2\sum_{m=0}^\infty
\frac{(-1)^m(qa)^{2m}}{4^m m!(m+1)!}.
$$

This agrees with the locally defined $J_1$ series and gives
$2\pi aJ_1(qa)/q$ for $q\ne0$, with removable value $\pi a^2$ at zero.
The oddness of $J_1$ handles negative wavenumbers without changing the
denominator sign. Uniform convergence on the compact domain justifies the
series integrations and local parameter derivatives.

The cosine remainder is nonnegative and bounded by its fourth-power term.
The disk moments therefore give exactly
$0\le F-(\pi a^2-\pi a^4q^2/8)\le\pi a^6q^4/192$.
The displayed second derivative at zero, scaling, and area units agree.
Direct complex angular/radial quadrature verifies the series result for both
wavenumber signs and zero, and verifies the explicit quadratic error bound.

## I3-010 — A squared aperture kernel

The bounds by $a^2$ near zero and by $x^{-2}$ at infinity establish absolute
convergence for every real parameter. Scaling by $|a|$, then integrating by
parts with vanishing endpoint terms, reduces the constant to
$\int_0^\infty\sin(2u)/u\,du=\pi/2$. Consequently
$Q(a)=\pi|a|/2$, with opposite one-sided slopes at zero.

The formal derivative kernel $\sin(2ax)/x$ is conditionally integrable
for nonzero $a$; its tail is bounded by $1/(|a|A)$ beyond $A$. Uniformity
on parameter neighborhoods separated from zero is enough to justify the local
derivative interchange. The pointwise derivative at zero is instead zero and
does not give a two-sided derivative of $Q$. The supremum-envelope argument
in the text correctly rules out a common integrable absolute derivative bound
near zero. The finite-interval small-parameter expansion has the stated order
and identifies why it cannot reproduce the full cusp.

Original-coordinate quadrature retains the rigorous positive tail interval
$0\le Q-Q_L\le1/L$, rather than assuming that a large cutoff is exact.
Both parameter signs, zero, small positive values, and the conditionally
convergent derivative integrals are checked with their explicit tail bounds.

## I3-011 — A logarithmic moment at an endpoint

The transformed moments are
$\int_0^1x^n\ln^2x\,dx=2/(n+1)^3$. Both integrations by parts and their
boundary terms are correct. The finite geometric identity gives a positive
remainder $R_N$ with sign $(-1)^N$ in the full answer and bound
$R_N\le2/(N+1)^3$. The odd/even partial-sum ordering is correct.
Absolute summability of the term integrals independently justifies passing to
the infinite series. Separating its even and odd terms yields
$M=3\zeta(3)/2$.

The direct substitution $x=\exp(-t)$ gives the independent nonsingular
integral $\int_0^\infty t^2/(\exp t+1)\,dt$. Its tail is at most
$\exp(-T)(T^2+2T+2)$, exactly as stated. The checker compares this
quadrature with independent positive-series upper and lower bounds for
$\zeta(3)$ and tests the signed finite geometric remainders.

## I3-012 — A shrinking layer and its parameter derivative

The scale $u=x/a$ gives $F(a)=\arctan(1/a)=\pi/2-\arctan a$ for positive
$a$, so its limit is $\pi/2$. The text correctly calls the kernel limit
zero almost everywhere rather than at every point: its value at zero diverges.
The exact mass in $[0,ca]$ is $\arctan c$, while the contribution of any
fixed interval $[\delta,1]$ tends to zero. The nonintegrable envelope
$1/(2x)$ correctly explains the missing common majorant.

Differentiating the positive-parameter kernel gives
$(x^2-a^2)/(x^2+a^2)^2$, with primitive $-x/(x^2+a^2)$ and integral
$-1/(1+a^2)$. Its pointwise limit $x^{-2}$ is not integrable, explaining
the second failed interchange. The exact cubic expansion has remainder
$-\int_0^a t^4/(1+t^2)\,dt\in[-a^5/5,0]$. The continuous extension and
the zero-kernel assignment at the endpoint are correctly distinguished.

Original-coordinate quadrature resolves several narrowing layers. Separate
checks verify first derivatives, the cubic remainder, the retained mass in
$[0,ca]$, and the vanishing contribution away from zero.

## I3-013 — Two closed paths around an excluded axis

For the positively oriented ellipse, direct parameterization yields
$AB/(A^2\cos^2\theta+B^2\sin^2\theta)$. The tangent-coordinate integral
in each quadrant is $\pi/2$, giving $2\pi$ in total.
The two nontrivial curl partials are equal, so the curl is zero everywhere
off the excluded axis. Stokes applies on the displaced disk because
$x\ge d-R>0$; it cannot be applied on the full centered ellipse disk.
The resulting displaced-circle circulation is zero.

The angle derivative on the displaced circle and the annular excision
calculation independently verify the two answers. Inner-circle clockwise
orientation is accounted for correctly. Numerical parameter integrals check
round and eccentric ellipses, reversed orientation, and displaced circles,
including a circle close to the excluded axis.

## I3-014 — A source inside a triangular panel

The preliminary disk bound $2\pi\epsilon$ proves local integrability
without relying on the later coordinate cancellation. The three
source-centered subtriangles have positive determinants
$y_0$, $1-x_0$, and $x_0-y_0$. For each map the Jacobian is $ud_j$ and
the source distance is $u\lVert\mathbf a_j+v\mathbf e_j\rVert$.
Cancellation and nonnegative exhaustion therefore leave exactly the three
nonsingular edge integrals in the text. Strict interior placement makes every
edge distance $h_j>0$; overlap boundaries have zero area.

The orthogonal edge decomposition independently gives
$h_j[\operatorname{arsinh}((t_j+L_j)/h_j)-
\operatorname{arsinh}(t_j/h_j)]$. Substitution agrees with every explicit
$K_j$, including the diagonal edge's factor $1/\sqrt2$. The stated positive
upper bound $2+\sqrt2$ follows from the edge integrands. Reflection symmetry
and the centroid value are correct; the centroid's diagonal contribution is
$\sqrt2\operatorname{arsinh}(3)/3$.

The maintained checker uses the independent Cartesian inner integral and
$x=x_0\pm s^2$ to handle its integrable logarithmic singularity. Four
interior source locations and the exact centroid expression agree with the
closed source-edge formula. No singular inner integral is evaluated as a
finite number at $x=x_0$.

## Verification and limits

`python3 scripts/check_integration_expansion.py` passes all **106** labeled
quadrature, finite-difference, remainder, and parameter-case checks using only
the Python standard library. Improper-integral comparisons retain explicit
tail bounds. Finite quadratures and finite differences also have ordinary
floating-point and discretization tolerances; they are independent spot checks,
not certified interval arithmetic. The analytical review above supplies the
domain and interchange arguments. Full-book layout and reader usability are
separate reviews.
