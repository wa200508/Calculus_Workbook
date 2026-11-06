# Second fields-and-geometry expansion: author evidence

Prepared November 6, 2026 by Codex `audit_d3`, against baseline
`d272310f466aaa0ea8c5cf585481c5ab39321dbc`. The new entries in
`DIFFERENTIATION_FIELDS.md` are D3-013 through D3-017. The author derived these
five entries before composing their statements, hints, and solutions. This is
author evidence; a separate analytical review by another agent remains to be
recorded by the integrating reviewer. No independent human or external reader
review is implied.

| Problem | Proposal | Scope |
|---|---|---|
| D3-013 | Backlog 4 | Distance-sum gradient, full Hessian, stationary segment, nonsmooth foci |
| D3-014 | New proposal 35 | Symmetric quadratic quotient, full Hessian, repeated eigenspaces and sphere classification |
| D3-015 | New proposal 36 | Positive-volume inverse congruence, ordered tensor derivative and energy |
| D3-016 | New proposal 37 | Principal positive matrix square-root branch, Sylvester derivatives and coupled perturbation |
| D3-017 | New proposal 38 | Global radial vector inverse, local scales and second inverse derivative |

## D3-013: two fixed foci and a distance response

The function is defined at the foci, while its displayed classical derivatives
are restricted to their complement. Differentiating each unit displacement gives
the projection $(\mathbf I-\mathbf u\mathbf u^{\mathsf T})/r$ with a positive
distance denominator. The sum is positive semidefinite. Its quadratic form
vanishes only for increments parallel to both displacement vectors. Off the
focal axis those vectors are not parallel, proving positive definiteness. On
the axis the radial eigenvalue is zero and each transverse eigenvalue is
$1/|s-a|+1/|s+a|$.

The zero-gradient condition makes the displacement unit vectors opposite and
therefore puts the point strictly between the foci. The triangle inequality,
including its equality criterion, separately gives the entire closed segment
as the global minimizing set, with value $2a$. The two foci belong to that set
but are not differentiable: exact axial restrictions give slopes $(0,2)$ at
the positive focus and $(-2,0)$ at the negative focus. The midpoint and
perpendicular-bisector calculations independently check the Hessian's zero and
positive directions. No norm derivative at zero is used.

## D3-014: scalar response unchanged by rescaling

The author differentiated the quadratic numerator and positive squared-norm
denominator independently. The full component Hessian includes the two distinct
outer-product terms and the final $8q x_ix_j/s^3$ term. Reassembling it with
$\mathbf v=\mathbf A\mathbf x-R\mathbf x$ produces the symmetric compact
formula. Differentiating the degree-minus-one homogeneity of the gradient gives
the independent identity $\mathbf H_R\mathbf x=-\nabla R$.

Every stationary input is a nonzero vector in an eigenspace, including arbitrary
combinations within a repeated eigenspace. At a stationary point its ambient
Hessian is $2(\mathbf A-\lambda\mathbf I)/\|\mathbf x\|^2$. On the unit sphere,
a normalized tangent path has the same second variation because the ambient
gradient is zero. Expansion in an orthonormal eigenbasis then gives
$2\sum_j(\lambda_j-\lambda)h_j^2$. This proves global extrema at extremal
eigenvalues, saddles at intermediate eigenvalues, and flat tangent directions
for repeated eigenvalues. The all-eigenvalues-equal case is treated as a
constant response, also covering dimension one.

The concrete three-by-three matrix has eigenvalues one, three, and five. Its
tangent curvature pairs are $(4,8)$, $(-4,4)$, and $(-8,-4)$. The nonstationary
input $(1,0,1)^{\mathsf T}$ checks the complete Hessian rather than only its
simplified stationary form. A separate matrix with eigenvalues $(1,1,4)$ checks
the circle of minimizers and its flat tangential direction.

## D3-015: changing tensor measured in fixed coordinates

The fixed reference/spatial bases and the direction of the map are declared so
that both tensor indices and held-fixed energy inputs are unambiguous. With
$m=\det\mathbf F$, $\mathbf K=\mathbf F^{-1}$, and
$\mathbf L=\mathbf K(d\mathbf F/dt)$, differentiating the inverse identity
gives $d\mathbf K/dt=-\mathbf L\mathbf K$ and its transpose gives
$d\mathbf K^{\mathsf T}/dt=-\mathbf K^{\mathsf T}\mathbf L^{\mathsf T}$.
Factoring the incremental deformation and expanding its determinant proves
$dm/dt=m\operatorname{tr}\mathbf L$. The resulting ordered derivative is

$$
\frac{d\mathbf Q}{dt}
=\operatorname{tr}(\mathbf L)\mathbf Q-\mathbf L\mathbf Q-\mathbf Q\mathbf L^{\mathsf T}.
$$

It preserves symmetry without assuming a symmetric rate matrix or commuting
factors. The energy derivative combines its two scalar ordered contractions
only after transposing the complete scalar. The concrete triangular path has
positive determinant for every finite real parameter. Its inverse is verified
by multiplication, and every component of the tensor and derivative is given.
Expanding $\exp(t)\|\mathbf F(t)^{-\mathsf T}\mathbf x\|^2$ independently checks
the energy coefficients. The invariant $\det\mathbf Q=m\det\mathbf C$ gives a
separate three-dimensional determinant check. Only a $C^1$ path is required for
these first derivatives.

## D3-016: positive matrix branch with coupled entries

The positive spectral square root is defined first. Smooth dependence is then
proved using the implicit map $\mathbf S^2-\mathbf A$ on the finite-dimensional
space of symmetric matrices. Its derivative sends $\mathbf K$ to
$\mathbf S\mathbf K+\mathbf K\mathbf S$. In a fixed eigenbasis of the
evaluated positive root, the entry multipliers are strictly positive
$\sigma_i+\sigma_j$, proving invertibility even for repeated eigenvalues.
The implicit function theorem and uniqueness of the positive root give the
needed smooth branch without assuming differentiable eigenvectors.

Differentiating in the original fixed basis gives
$\mathbf S\mathbf K+\mathbf K\mathbf S=\mathbf H$ and
$\mathbf S\mathbf T+\mathbf T\mathbf S=-2\mathbf K^2$ for the affine input.
Their entrywise spectral solutions and the finite sum in the second equation
retain all multiplication order. For the concrete path, Sylvester's criterion
gives the full positive-definite domain $t>-3+\sqrt5$, with no admissible lower
determinant-positive interval. At zero, the first derivative has diagonal
entries $1/2$ and off-diagonal entries $1/3$; the second derivative has entries
$(-13/36,-2/9,-13/72)$ in its upper triangle.

The proposed scalar shortcut is nonsymmetric in this example and disagrees
with the unique symmetric derivative. An independent two-by-two expression
for the positive root is proved from the characteristic equation. Scalar
expansion of its determinant square root and denominator reproduces every
first- and second-derivative entry, with a justified cubic remainder.

## D3-017: radial map with changing local scales

The forward map is polynomial, so differentiating the norm at zero is
unnecessary. Its Jacobian is $(1+r^2)\mathbf I+2\mathbf x\mathbf x^{\mathsf T}$,
with radial eigenvalue $1+3r^2$ and two transverse eigenvalues $1+r^2$.
All are positive, and their product gives the determinant. The component
second derivatives and their bilinear contraction are derived explicitly.

Global inversion is proved separately: the map preserves direction and the
radius map $r+r^3$ is a continuous strictly increasing bijection of the
nonnegative half-line onto itself. This constructs a unique inverse everywhere.
The local inverse theorem then makes that global inverse smooth at every
point, including the origin. The inverse Jacobian is verified by multiplication
and independently by the radial scalar inverse and the transverse scale.

A second differentiation of the inverse identity gives the ordered bilinear
formula with two first-order inverse increments inside the forward second
derivative. At zero it is zero. At output $2\mathbf e_1$, the inverse Jacobian
is $\operatorname{diag}(1/4,1/2,1/2)$, and its second derivative on the two equal
increments $\mathbf e_1$ and $\mathbf e_2$ gives respectively
$-3\mathbf e_1/32$ and $-\mathbf e_1/8$. Scalar radial differentiation and a
transverse input expansion independently check those values.

## Executed checks and preservation

The standard-library script `/workspace/scratch/expansion2-d3-checks.py` ran
successfully: **590 independent numerical checks passed**. It uses finite
differences of the original distance sum and quadratic quotient; pivoted
elimination of the original deformation matrix and its determinant/inverse
energy; an orthogonal spectral construction of the positive two-by-two root;
and bisection of the original monotone radius equation for the vector inverse.
Sample cases include both focal-axis regimes, both foci's one-sided slopes,
repeated spectra, a constant quotient, a second nonidentity spatial tensor,
noncommuting square-root perturbations, positive and negative parameters within
the matrix domain, the spatial origin, and off-axis inverse inputs. Finite
differences check the full quotient Hessian and all inverse second-component
derivatives, not only a radial special case.

The manuscript parser found seventeen matching IDs in each of the problem,
hint, and solution sections. Each of the twelve original statements, hint
ladders, and solutions was compared against the parsed baseline `d272310` and
preserved exactly. `git diff --check` passed for the manuscript. Full site/PDF
checks and the separate analytical review belong to the integration stage.
Numerical samples supplement the proofs; they do not prove the full-domain,
global-inverse, stationary-set, or nonsmooth-point claims by themselves.
