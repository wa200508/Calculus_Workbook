# Fields and geometric constraints: expansion evidence

Prepared November 5, 2026 by the Codex `audit_d3` agent after the original-book
audit/correction checkpoint `606a472`. The new manuscript entries are D3-008
through D3-012 in `DIFFERENTIATION_FIELDS.md`. Each has a complete statement,
exactly three hints, a reasoned choice of representation, intermediate algebra,
domain analysis, and an independent check. Original problem IDs are unchanged.
This note records the author's derivations and checks; a separate integrating
review remains necessary and external human/reader feedback is not implied.

## D3-008: quadratic response near loss of invertibility

Develops backlog proposal 27. The rank-one inverse is derived by multiplication,
not invoked as an unexplained identity. For nonzero $\mathbf u$,
$\alpha=\mathbf u^{\mathsf T}\mathbf A^{-1}\mathbf u>0$ and the single excluded
parameter is $t_*=-1/\alpha$. Multiplication gives an inverse whenever
$1+t\alpha\ne0$, and the explicit nonzero null vector $\mathbf A^{-1}\mathbf u$
proves singularity at the excluded point. The zero-vector case has the whole
real line as its domain.

Contraction yields $s(t)=\beta-tc^2/(1+t\alpha)$; direct quotient differentiation
gives the first and second derivatives. Rewriting the response with residue
$c^2/\alpha^2$ at $t_*$ proves that the scalar pole cancels exactly when $c=0$.
The null-space compatibility condition independently gives the same criterion
for consistency of the singular linear system. Its family of solutions all
have the same contraction with $\mathbf b$, explaining the finite scalar
extension without assigning an inverse to a singular matrix. A concrete
two-by-two direct inverse checks both the pole and canceled-pole cases.

## D3-009: energy carried by coupled tensor components

Develops backlog proposal 29 with the necessary strengthened assumption that
$\mathbf E(t)$ is $C^2$, rather than merely differentiable, before requesting
two derivatives. All component ranges, both minor symmetries, major symmetry,
and the fixed orthonormal basis are declared. The major symmetry combines the
two first product-rule sums by an explicit exchange of dummy index pairs.
The minor symmetries give the symmetric stress contraction and the factors two
on off-diagonal components. Differentiating again includes the product of two
first derivatives and the term containing a second derivative.

The concrete tensor is anisotropic and satisfies every declared symmetry.
Its four equivalent shear entries explicitly produce the factor $14$ on
$E_{12}^2$ in the energy, rather than a factor obtained by counting only one
matrix entry. Literal expansion along the stated path gives
$W(t)=t^4+(31/2)t^2+5/2$, $dW/dt=4t^3+31t$, and
$d^2W/dt^2=12t^2+31$. The stress contraction and the two parts of the second
derivative give an independent calculation of those polynomials. No positivity
assumption is required for the general derivative identities.

## D3-010: anisotropic energy with turning principal directions

Develops backlog proposal 31. The statement fixes the active counterclockwise
rotation convention and holds the laboratory components of $\mathbf x$ fixed.
The transpose derivative is formed in its correct order, giving
$d\mathbf Q/dt=\mathbf J\mathbf Q-\mathbf Q\mathbf J$. Component multiplication
gives the symmetric trace-zero derivative with its orientation-dependent signs.
The scalar contraction retains both off-diagonal terms. Independently,
$\mathbf y(t)=\mathbf R(t)^{\mathsf T}\mathbf x$ has derivative
$-\mathbf J\mathbf y(t)$, and differentiation of
$ay_1(t)^2+by_2(t)^2$ reproduces the answer. The cases $a=b$, $\mathbf x=0$,
and the signed example $\mathbf x=(1,0)^{\mathsf T}$ at $t=\pi/4$ are checked.
All finite real angles are admissible.

## D3-011: direction traced by three competing components

Develops backlog proposal 30. The strictly positive exponential component makes
the normalization valid for all finite real parameters. The first derivative of
the norm is obtained from its square. The displayed second vector derivative
then includes both copies of the first-vector-derivative term and the derivative
of the scalar normalization factor. All scalar intermediates and both original
vector derivatives are explicit.

Contractions verify $\mathbf n^{\mathsf T}(d\mathbf n/dt)=0$ and
$\mathbf n^{\mathsf T}(d^2\mathbf n/dt^2)=-\|d\mathbf n/dt\|^2$ both by
differentiating the constraint and by substituting the formulas. The latter
identifies the inward component of the acceleration on the unit sphere. A
componentwise Taylor expansion at zero independently confirms the vectors
$(1,0,0)^{\mathsf T}$, $(0,1,1)^{\mathsf T}$, and $(-2,-2,-2)^{\mathsf T}$.
The solution distinguishes the given parameter from arc length.

## D3-012: finite value after a point-source subtraction

Develops backlog proposal 22. A finite-interval exponential representation
establishes the continuous radial value $-\mathrm{i}k$ and right radial
derivative $-k^2/2$ without subtractive cancellation. Its parameter derivative
is justified on a compact rectangle; the positive-radius quotient derivative
is also computed explicitly. Taylor's integral remainder gives the quantitative
bound $|k|^4r^3/24$ after division by radius.

The spatial field has leading correction $-(k^2/2)\|\mathbf x\|$. For nonzero
$k$, opposite one-sided coordinate difference quotients disagree, proving that
even a coordinate partial derivative fails at the origin. The ordinary radial
gradient is restricted to nonzero spatial points. For $k=0$ the extended field
is identically zero and is differentiable everywhere. The real-part
trigonometric identity independently identifies the cusp; its imaginary part
has only an even quadratic leading correction.

## Executed checks

The standard-library script `/workspace/scratch/expansion-d3-checks.py` ran
successfully: **187 numerical checks passed**. It uses Gaussian elimination of
the original changing matrix for the rank-one response, a literal 81-entry
tensor contraction, direct rotation multiplication, finite differences of the
original normalized vector, and a stable trigonometric radial representation.
Inputs include canceled scalar poles, zero perturbation vectors, equal
eigenvalues, nonzero negative parameters, and positive/negative/zero wavenumbers.
These checks supplement the analytical arguments; no finite sample establishes
the excluded-point or full-domain claims by itself.

The manuscript parser was run directly and found twelve matching IDs in each
of the problem, hint, and solution sections. Full site/PDF generation, layout,
and regression integration are handled by the integrating reviewer.
