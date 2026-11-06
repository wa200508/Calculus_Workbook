# Independent review of the second differentiation expansion

Date: November 6, 2026. Reviewer: Codex agent `/root/audit_references`.
Baseline before this expansion: `d272310`.
Scope: D4-012--016 and D3-013--017, including each final statement, three hints,
complete solution, domain discussion, and check.

## Method and outcome

I derived the expected results and exceptions for the ten assigned topics before
reading the authors' new solutions and recorded them in a separate working note.
I then compared every part of the frozen manuscripts with those calculations.
The final D3-017 statement additionally requested the second derivative of the
inverse, beyond the initial topic brief; I checked that part by differentiating
the composed inverse identity and by finite differences of a numerical inversion
of the original map.

**All ten analytical reviews passed. No mathematical discrepancy was found, and
no author manuscript was changed by this reviewer.** This is an independent
agent review, not a claim that every possible error has been excluded.

The new maintained script `scripts/check_differentiation_expansion_2.py` passed
**756 independent numerical spot checks**. It uses original-function finite
differences, bisection of the implicit cubic, full pivoted matrix operations,
a separately implemented spectral square root, Sylvester linear solves, and
Newton inversion of the original radial map. It does not import the authors'
supplementary scripts. Its numerical comparison helper directly rejects
nonfinite arguments and invalid tolerances; scaling before subtraction avoids
overflow in comparisons of opposite large finite values. Python compilation
and a whitespace-error check also passed.

## D4-012: folded angle

The double-angle identity and principal arctangent range give exactly three
pieces: $2\arctan x+\pi$ for $x<-1$, $2\arctan x$ for $|x|<1$, and
$2\arctan x-\pi$ for $x>1$. Direct quotient differentiation gives the common
derivative $2/(1+x^2)$ on those three open components. It does not fill the
excluded inputs: at each of $-1,1$, the left and right value limits are
$\pi/2$ and $-\pi/2$.

The displayed lift subtracts $\pi$ on the left component and adds $\pi$ on
the right, making the global function $2\arctan x$. The normalization at zero
and continuity uniquely determine the integer multiples. This is an angle
lift modulo $\pi$, not an assertion that the original principal-valued
function extends continuously through either jump. All four limits, the
quotient algebra, and the hint sequence agree with the derivation. Numerical
checks evaluate the original arctangent on each component and near each side
of both excluded points.

**Result:** passed without correction.

## D4-013: phase at a response zero

The factorization
$1-e^{-i\omega\tau}=2i e^{-i\omega\tau/2}\sin(\omega\tau/2)$ gives zeros
$\omega_n=2\pi n/\tau$, magnitude $2|\sin(\omega\tau/2)|$, and the phase
$\pi/2-\omega\tau/2+n\pi$ on the interval between successive zeros. This
phase lies in the stated right-half-plane angle range; other continuous
choices on the same component differ by fixed multiples of $2\pi$.

The frequency derivative is $-\tau/2$ away from zeros. The independent
logarithmic derivative is $(\tau/2)(\cot(\omega\tau/2)-i)$, with the correct
imaginary part and a real part diverging like the reciprocal displacement.
Near any zero, the complex expansion is
$i\tau\delta+\tau^2\delta^2/2+O(\delta^3)$ and the magnitude is
$\tau|\delta|+O(|\delta|^3)$. The normalized one-sided limits are opposite
unit-complex numbers, so no $2\pi$ phase corrections can create a continuous
phase across that zero. This obstruction is a response zero rather than a
principal phase cut. Original complex values and arguments provide numerical
checks for positive and negative zero indices and on both sides of zeros.

**Result:** passed without correction.

## D4-014: determinant, inverse, and conditioning

The shear factorization proves positive definiteness for every real parameter,
and direct calculation gives determinant one. The trace calculation retains
both off-diagonal rates and correctly cancels to zero. A single varied
off-diagonal entry would give a different, incorrect path derivative.

Differentiating $AR=I$ gives $R'=-RA'R$ and
$R''=2RA'RA'R-RA''R$, with the two positive terms having identical order.
Independent entry differentiation of
$R=[[1,-t],[-t,1+t^2]]$ gives the stated first and second matrices. The ordered
products listed in the solution multiply out correctly.

The positive eigenvalues have sum $t^2+2$ and product one; their expressions
with $|t|\sqrt{t^2+4}$ and the stable reciprocal formula for the smaller
eigenvalue are correct. The condition number is the square of the larger
eigenvalue and grows like $t^4$. A repeated eigenvalue at zero does not make
the smooth matrix or inverse singular. The selected response vector, its two
derivatives, and its $t^2$ norm growth are consistent with the inverse.
Numerical checks use pivoted inversion and determinant elimination, while
independent power iteration evaluates the operator norms for the conditioning
comparison.

**Result:** passed without correction.

## D4-015: upper cubic branch and fold

On $y>1$, the cubic $y^3-3y$ is strictly increasing and has range $(-2,\infty)$.
This proves the complete input domain, not just local existence. Implicit
differentiation gives
$g'=1/[3(g^2-1)]$ and $g''=-2g/[9(g^2-1)^3]$. In particular, $x=2$ is
regular on the selected upper branch even though other roots of the cubic
meet there.

At the domain endpoint, $u=g(-2+\delta)-1$ satisfies
$\delta=u^2(3+u)$ exactly. Inverting the smooth local relation
$\sqrt\delta=u\sqrt{3+u}$ gives
$u=\sqrt{\delta/3}-\delta/18+O(\delta^{3/2})$. The local inverse's bounded
third derivative supplies the remainder in the square-root coordinate. The
exact interior derivative formulas separately yield the blowup coefficients
$1/(2\sqrt3)$ and $-1/(4\sqrt3)$ after the stated rescaling. The endpoint
difference quotient is also infinite, with its distinct square-root leading
coefficient correctly distinguished from that of the interior derivative.
The value and derivatives at $x=0$ and the residual cancellation in the
endpoint check are correct. Numerical bisection solves the original cubic
before taking finite differences and testing the fold expansion.

**Result:** passed without correction.

## D4-016: soft absolute value and curvature concentration

Factoring the larger exponential gives exactly
$f_\epsilon-|x|=\epsilon\ln(1+e^{-2|x|/\epsilon})$. The uniform bound
$0\le f_\epsilon-|x|\le\epsilon\ln2$ is sharp at zero. Direct derivatives
are $\tanh(x/\epsilon)$ and
$1/(\epsilon\cosh^2(x/\epsilon))$, and the latter is positive for every
finite input. First-derivative convergence is uniform away from zero and
fails to be uniform on any fixed neighborhood of it; the limiting absolute
value has no derivative there.

The curvature primitive gives total mass two and mass $2\tanh c$ in an
interval of width $2c\epsilon$. The exact tail
$4/(e^{2\delta/\epsilon}+1)$ and its exponential upper bound are correct.
The nonzero mass despite an almost-everywhere zero pointwise limit correctly
rules out an integrable uniform majorant. For a bounded continuous test
function, the text's inner-outer split gives
$2\eta(\delta)+8M e^{-2\delta/\epsilon}$, so the two-stage limit is
justified without assuming global uniform continuity. Original-function
differences and independent mass, scaled-interval, tail, and test-function
quadrature all agree numerically.

**Result:** passed without correction.

## D3-013: two-focus distance response

Differentiating each nonzero displacement norm gives its unit displacement
gradient and transverse-projection Hessian. The sum's quadratic form is
nonnegative; its null space is the intersection of the two displacement
directions. Thus the Hessian is positive definite off the full focal axis
and has zero axial and positive transverse eigenvalues on the axis away from
the foci. This remains true outside the minimizing segment; positive
semidefiniteness alone does not make those outer points stationary.

Opposite unit displacements identify exactly the open focal segment as the
differentiable stationary set. Triangle-inequality equality identifies the
closed segment as the global minimum set, including its nondifferentiable
endpoints. The one-sided axial slopes at the two foci are respectively
$(0,2)$ and $(-2,0)$. The midpoint and off-axis checks are correct, including
all three diagonal Hessian entries of the off-axis example. Original norm-sum
finite differences verify every gradient and mixed Hessian entry, while
explicit focus differences verify the cusp slopes.

**Result:** passed without correction.

## D3-014: full Rayleigh-quotient Hessian

With $s=x^{\mathsf T}x$, $\rho=R(x)$, and $v=Ax-\rho x$, direct quotient
differentiation gives gradient $2v/s$ and full Hessian
$2(A-\rho I)/s-4(xv^{\mathsf T}+vx^{\mathsf T})/s^2$. The component formula
contains all denominator and numerator derivatives and matches this symmetric
matrix expression.

Stationary vectors are exactly the nonzero vectors in eigenspaces. Repeated
eigenvalues permit every combination within the corresponding eigenspace,
not only a chosen basis. At stationarity the Hessian reduces to
$2(A-\lambda I)/\|x\|^2$; its tangent restriction at a unit vector gives
the stated second variation. Weighted-average values prove global extreme
classification, and signs in lower and higher eigenspaces prove the saddle
classification for intermediate eigenvalues. The cases of repeated extremes,
a scalar matrix, and dimension one are correctly qualified.

All eigendirections, tangent Hessian eigenvalues, and the nonstationary
example's gradient and Hessian multiply out correctly. The scaling identity
$H_R(x)x=-\nabla R(x)$ independently verifies the full Hessian. Numerical
checks differentiate original quotient values, include every mixed Hessian
entry, and cover repeated and scalar spectra as well as direction-dependent
limits at the excluded origin for a nonscalar matrix.

**Result:** passed without correction.

## D3-015: ordered determinant and inverse transport

Keeping both coordinate bases fixed, write $m=\det F$, $K=F^{-1}$, and
$L=KF'$. The inverse derivative is $K'=-LK$, its transpose derivative has
the corresponding reversed order, and the determinant rate is
$m'=m\operatorname{tr}L$. Their product rule gives
$Q'=\operatorname{tr}(L)Q-LQ-QL^{\mathsf T}$ exactly. The energy formula
combines the two ordered scalar contractions by transposition of the whole
scalar, not by commuting matrices. The stated symmetry, definiteness, and
reference/spatial coordinate types are consistent.

For the triangular example, all inverse and rate entries, all six distinct
$Q$ entries, and all six derivative entries agree with direct multiplication
and differentiation. Independently expanding
$m\|K^{\mathsf T}x\|^2$ gives the same energy and cross-term derivatives.
The determinant identity in dimension three is
$\det Q=m\det C$, as stated. Numerical checks use full determinant and
inverse operations for both the printed identity tensor and a separate
positive-definite tensor with off-diagonal entries. They also verify the
congruence identity and differentiate the spatial-vector energy directly.

**Result:** passed without correction.

## D3-016: positive square root and noncommuting perturbation

The derivative of $S\mapsto S^2$ on symmetric increments is the Sylvester
map $X\mapsto SX+XS$. At a positive root its eigenbasis multipliers are
$\sigma_i+\sigma_j>0$. This proves invertibility even for repeated
eigenvalues, enabling the local implicit-function argument. Unique positive
roots identify overlapping local branches, so differentiating the affine
path twice is justified without differentiating eigenvectors.

The two equations are $SK+KS=H$ and $ST+TS=-2K^2$. Both the factor two and
the eigenbasis sum in the second equation are correct. For the example,
Sylvester's criterion gives the full domain $t>-3+\sqrt5$; positive
determinant on a distant negative-definite interval cannot enlarge it.
The printed first derivative at zero and second derivative
$[[-13/36,-2/9],[-2/9,-13/72]]$ agree with the independent derivation.
The scalar-inspired formula is generally nonsymmetric and fails in this
example. Both scalar expansions used in the independent characteristic-
equation check have the correct quadratic coefficients and justified local
remainders.

The maintained tests construct a separate spectral square root and check its
square before taking differences. Sylvester linear solves then supply the
comparison derivatives at several admissible inputs, including a separate
repeated-eigenvalue path. Both sides of the example's SPD boundary and the
negative-definite determinant-positive trap are tested.

**Result:** passed without correction.

## D3-017: global radial inverse and its second derivative

The polynomial map has Jacobian $(1+r^2)I+2xx^{\mathsf T}$, radial eigenvalue
$1+3r^2$, transverse eigenvalues $1+r^2$, and determinant
$(1+r^2)^2(1+3r^2)$. Its second component derivatives and the symmetric
bilinear contraction agree with direct differentiation. A positive Jacobian
alone would establish only local inversion; the strictly increasing radius
map $r+r^3$ from zero to infinity and direction preservation supply the
necessary global existence and uniqueness.

The inverse Jacobian is
$I/(1+r^2)-2xx^{\mathsf T}/((1+r^2)(1+3r^2))$, where $x=G(y)$. Its radial
and transverse eigenvalues are the reciprocals of the forward values.
At zero it is the identity; the global inverse is smooth there by the local
inverse theorem and uniqueness, despite the radius notation. A direct bound
$\|G(y)-y\|\le\|y\|^3$ also independently verifies that derivative.

Differentiating $F(G(y))=y$ twice gives
$D^2G(y)(h,k)=-J(x)^{-1}D^2F(x)(J(x)^{-1}h,J(x)^{-1}k)$, exactly the printed
bilinear formula. Its zero value at the origin and both explicit nonzero
second-derivative checks are correct. In particular, the transverse example's
radius and first-component expansions have the correct coefficients.
Newton solutions of the original scalar radius equation supply independent
inverse values for finite differences of every first and second component
derivative, including mixed increments and the origin.

**Result:** passed without correction.

## Limits of the evidence

The analytical review and numerical checks are distinct from the authors'
derivations. Finite differences and quadrature are spot checks, not proofs
of global inversion, differentiability, asymptotics, or concentration. No
independent human reader trial, browser accessibility assessment, visual PDF
inspection, or fresh external citation verification is claimed by this note.
Root integration records generated-source, production-site, and PDF checks
and the final reviewed source revision separately.
