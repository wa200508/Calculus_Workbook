# Second expansion: parameter integrals and geometric accumulation

Authored November 6, 2026 by Codex `/root/audit_i4` against baseline `d272310`.
This batch adds **I4-012 through I4-016**. All eleven preexisting I4 statements,
hint ladders, and complete solutions were compared against the baseline and
preserved exactly. Each new problem has a complete typed statement, three
graduated hints, intermediate calculations, method reasoning, domain analysis,
and checks. The solutions were derived before the source additions were written.

This note records author analytical work and supplemental numerical evidence.
Independent reviewer findings, integrated build checks, and external reader
feedback are separate kinds of evidence and are not claimed here.

## Selection and source map

| ID | Backlog mapping | Coverage |
|---|---|---|
| I4-012 | 18, Gaussian on a rotated ellipsoid | Positive matrix root, determinant/measure, changing integration domain, symmetric perturbation |
| I4-013 | 15, hyperboloidal shell | Bounded solid, volume sections, lateral vector area, both cap orientations, flux theorem |
| I4-014 | 17, weighted ellipse | Arc-length weight, complete elliptic parameter convention, moment recurrence, uniform second-order approximation |
| I4-015 | New proposal 39 | Whole-space Gaussian matrix moments, normalization/covariance, ordered matrix perturbation, spectral domination |
| I4-016 | New proposal 40 | Two-exponent logarithmic difference, endpoint extensions, justified interchange, nonunique joint boundary limits |

## I4-012: Gaussian on a rotated ellipsoid

For SPD `Q`, spectral decomposition gives the unique symmetric positive root
`S=Q^(1/2)` with positive determinant `sqrt(det Q)`. The map `u=S x`
simultaneously transforms the quadratic sublevel ellipsoid to the unit ball
and the exponent to `-|u|^2`. Its inverse volume scale is `1/sqrt(det Q)`.
The radial integral is evaluated by integration by parts, giving

`N(Q)=C/sqrt(det Q)`,
`C=pi^(3/2) erf(1)-2pi/e=4pi integral_0^1 r^2 exp(-r^2)dr>0`.

The root, rather than an arbitrary eigenvector orientation, fixes the positive
Jacobian. A reflected orthogonal eigenbasis appears twice in the root and
cannot change the volume sign.

For a differentiable SPD path, transforming at every input fixes the domain
before taking a derivative. Factoring the determinant perturbation and expanding
`det(I+epsilon B)` to first order yields
`N'=-N tr(Q_0^-1 H)/2`. This derivation keeps arbitrary matrix order and avoids
any derivative of a potentially changing eigenbasis. It includes domain motion;
holding the original ellipsoid fixed while differentiating only the exponent
would be a different calculation. A local positive eigenvalue gap bounds the
transformed measure factor and its derivative, justifying the fixed-domain
differentiation. A zero eigenvalue gives an infinite cylindrical sublevel set
without decay in the null coordinate, so it lies outside this argument.

For the off-diagonal path in the statement the eigenvalues are `3+t`, `1-t`,
and `4`; the complete SPD interval is `(-3,1)`. Direct determinant evaluation
gives `N(t)=C/[2 sqrt(4-(1+t)^2)]`, derivative `C/(6 sqrt(3))` at zero, and
trace `tr(Q_0^-1 H)=-2/3`, agreeing with the general formula.

Independent numerical checks integrate the original first-coordinate slices
analytically through `erf`, then perform two-dimensional quadrature in the
remaining Cartesian coordinates. This route completes the square rather than
using the positive matrix root. Four off-diagonal values and a finite-difference
perturbation derivative agree with the formulas.

## I4-013: hyperboloidal shell

Each horizontal section has radius `R(z)=a sqrt(1+z^2/c^2)`. Integrating its
area on `[-H,H]` gives volume `2pi a^2(H+H^3/(3c^2))`. The lateral
parameterization `p(theta,z)=(R cos(theta),R sin(theta),z)` has outward vector
area factor `(R cos(theta),R sin(theta),-R dR/dz)` when its tangents are crossed
in the order `theta` then `z`. Its positive radial component fixes the outward
orientation; the unit normal retains the axial tilt.

The field-normal vector-area product is
`R^2-z R dR/dz=a^2`, not `R^2`. The axial term cancels the height-dependent
part, producing lateral flux `4pi a^2 H`. The top normal is positive vertical
and the bottom normal negative vertical. Both field-normal products equal `H`,
so the two caps together give `2pi a^2H(1+H^2/c^2)`. Their sum is
`6pi a^2H+2pi a^2H^3/c^2`, equal to three times the volume.

The smooth field, bounded solid, and piecewise smooth boundary meet the
divergence theorem's hypotheses; joining circles have zero surface measure.
The cylinder limit at fixed `a,H` is checked separately in the volume, lateral
flux, and cap flux. No singular-source or open-surface replacement is used.

Numerical checks for three sets of positive lengths integrate the actual vector
area expression with finite-difference radius tangents, the two cap disks, and
the original volume sections. They independently check the decomposition and
the total divergence relation.

## I4-014: weighted ellipse

Direct path speed gives
`W=4a^3 integral_0^(pi/2) sin(theta)^2 sqrt(1-m sin(theta)^2)dtheta`,
where `m=1-b^2/a^2`. The complete integrals `K(m)` and `E(m)` are defined by
their angular integrals, explicitly with parameter `m` rather than modulus.
For moments `L_j=integral sin(theta)^(2j)/sqrt(1-m sin(theta)^2)dtheta`,
the identities are `L_0=K`, `E=K-m L_1`.

Integrating the derivative of
`sin(theta)cos(theta)sqrt(1-m sin(theta)^2)` gives
`K-2(1+m)L_1+3m L_2=0`, since that function vanishes at both endpoints.
Eliminating `L_1,L_2` gives

`W=4a^3[(1-m)K+(2m-1)E]/(3m)` for `0<m<1`.

For the nearly circular regime, the expansion is derived from the regular
weighted angular integral rather than by canceling nearly equal complete
integrals. The third derivative of `sqrt(1-z)` is negative and bounded in
magnitude by `3/[8(1-m_0)^(5/2)]` for `0<=z<=m_0<1`. Taylor's theorem and
the explicit second, fourth, sixth, and eighth sine moments therefore give

`W=pi a^3[1-3m/8-5m^2/64]+R`,
`-35pi a^3 m^3/[1024(1-m_0)^(5/2)] <= R <= 0`.

The eighth moment, rather than the sixth, enters the remainder because the
coordinate weight supplies an additional sine square. The circular value is
`pi a^3` directly, avoiding the removable `0/0` in the complete-integral
formula. Speed bounds also give `pi a^2 b<=W<=pi a^3`. The approximation is
uniform only up to a fixed `m_0<1`, with no claim of uniformity in the collapsed
ellipse limit.

Numerical checks compare direct original-path quadrature with independently
integrated `K/E` values, include the exact circle and a tiny parameter, and
verify the signed remainder bound at nine combinations of `m,m_0`.

## I4-015: Gaussian matrix moment

Translation removes the fixed center. With `u=A^(1/2)(x-m)`, Gaussian product
integrals give normalization `Z=pi^(3/2)/sqrt(det A)`. All off-diagonal isotropic
moments vanish by oddness and absolute integrability. Integration by parts gives
the scalar second moment `sqrt(pi)/2`; the other two scalar coordinates each
contribute `sqrt(pi)`. Transforming the two moment vectors as well as the volume
measure gives `M=(Z/2)A^-1`. The normalized density has mean `m` and covariance
`Sigma=(1/2)A^-1`.

At any fixed path input, with symmetric perturbation `H`, the derivatives are

`Z'=-Z tr(A^-1 H)/2`,
`M'=-(Z/4) tr(A^-1 H) A^-1-(Z/2)A^-1 H A^-1`,
`Sigma'=-(1/2)A^-1 H A^-1`.

The inverse factors retain their multiplication order. The moment derivative
has a mass-change term that disappears after covariance normalization. Direct
differentiation of the original moment kernel is also justified: on a local
spectral gap `mu>0` with bounded matrix derivative `K`, its norm is bounded by
`K |y|^4 exp(-mu |y|^2)`, an integrable whole-space function. The normalization
derivative has a lower polynomial bound of the same type. Comparing these two
derivative routes gives the explicit fourth-moment contraction printed in the
solution. Zero eigenvalues destroy decay and a finite normalization; negative
eigenvalues cause exponential growth, so these are excluded genuinely rather
than by notation alone.

For the concrete off-diagonal path, the SPD interval is
`|1+t|<sqrt(6)`. The covariance entry is
`Sigma_12=-(1+t)/[2(6-(1+t)^2)]`, with value `-1/10` and derivative `-7/50`
at zero. Direct ordered multiplication gives the same derivative. The
normalization is `pi^(3/2)/(2sqrt(5))` at zero, so the unnormalized off-diagonal
moment is `-Z/10` and its derivative is `-4Z/25`.

Numerical verification uses direct two-dimensional Gaussian quadrature in the
coupled original block, multiplied by independently integrated third-coordinate
normalization/second moments. Three off-diagonal values verify normalization and
all distinct moment entries. Finite differences of those numerical integrals
verify the mass, unnormalized off-diagonal moment, and normalized covariance
derivatives.

## I4-016: logarithmic difference

The identity `(x^a-x^b)/ln(x)=integral_b^a x^s ds` follows by integrating in
the exponent parameter. On the compact parameter interval between the two
admissible exponents, `alpha=min(a,b)>-1` gives the absolute bound
`|a-b|x^alpha`. It proves original-kernel convergence and absolute double
integrability, so Fubini yields
`I=integral_b^a ds/(s+1)=ln((a+1)/(b+1))` with the correct oriented sign.

The endpoint at one always extends to `a-b`. For distinct exponents the kernel
at zero extends to zero exactly when their minimum is nonnegative. If the
minimum is negative but greater than minus one, the kernel is unbounded, with
the sign of `a-b`, yet the same power bound proves its integrability. On the
diagonal it is identically zero, including for equal negative exponents.

Local exponent lower bounds above minus one dominate the derivative kernels by
an integrable power. Thus the two first partials are `1/(a+1)` and `-1/(b+1)`.
Along the diagonal their contributions cancel, whereas neither partial alone
is a diagonal derivative.

Paths with `a+1=c epsilon`, `b+1=epsilon` give any finite value `ln c` as both
parameters approach minus one. Unequal orders of those distances give either
infinite sign. The original unsplit difference is zero at the separately
specified boundary pair `(-1,-1)`, but this does not give a joint continuous
extension. On either non-diagonal boundary edge the kernel has an uncanceled
`1/(x|ln x|)` singularity and diverges with the stated sign. An exponential
coordinate independently converts the answer to a Frullani difference of
decaying kernels and checks its order/sign.

Numerical quadrature uses that exponential coordinate, rescaled to avoid
unnecessary boundary concentration. Cases include unequal signs of the result,
negative exponents, diagonal cancellation, close exponents, first-partial finite
differences, endpoint-at-one values, and simultaneous boundary paths with three
different limiting ratios.

## Validation scope

The transient standard-library script `/workspace/scratch/expansion2-i4-checks.py`
passed **78** supplemental quadrature, finite-difference, normalization, and remainder
checks. The arguments above, rather than those finite samples, supply the
convergence and domain conclusions. The manuscript parser confirms sixteen
matching problem/hint/solution entries, exactly three hints for every addition,
all required solution labels, and successful conversion through the existing
Markdown-to-TeX converter. The eleven earlier problem entries were compared
section by section to `d272310` and were unchanged. Diff whitespace checks pass.

Shared counts, the project status, review ledger, permanent checks, generated
sources, PDF/website builds, independent review notes, and publication are
integration tasks of the primary editor. No human review or external reader
trial is inferred from this author work.
