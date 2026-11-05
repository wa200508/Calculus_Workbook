# Analytical audit: fields and geometric constraints

Reviewed November 5, 2026 by the Codex `audit_d3` agent. The reviewed manuscript
is `DIFFERENTIATION_FIELDS.md` at baseline commit `8963e97` (the full revision is
`8963e970e9ec23d4114203b205fccc9b7ca1c85d`). This is an analytical review of all
seven existing problems, their statements, three hints, complete calculations,
domain qualifications, and checks. No mathematical correction was required in
this chapter. Numerical checks described below supplement these derivations.

## D3-001: waveguide sensitivity at cutoff

Differentiating the positive square root on the open domain gives
$d\beta/d\omega=\omega/(c\sqrt{\omega^2-\omega_c^2})$. Its reciprocal is the
stated positive group velocity. At the boundary, direct factorization of
$\beta(\omega_c+h)/h$ gives
$\sqrt{2\omega_c+h}/(c\sqrt h)$, proving the divergent right difference quotient
without substituting into an interior derivative. The high-frequency and cutoff
limits, and units of both derivatives and velocity, agree. For the stated
$\exp(\mathrm{i}\omega t-\mathrm{i}\beta z)$ convention, setting
$\beta=-\mathrm{i}\alpha$ gives $\exp(-\alpha z)$, so the evanescent sign is
correct. All three hints lead to the stated calculation. No finding.

## D3-002: spatial gradient of a complex Green kernel

Differentiation first in a positive independent radial coordinate produces
$-\exp(-\mathrm{i}kR)(1+\mathrm{i}kR)/(4\pi R^2)$. Multiplication by the unit
displacement vector gives precisely the stated vector and its minus sign.
An independent check is the differential along an arbitrary displacement
$\mathbf h$: the distance changes to first order by
$(\mathbf r-\mathbf r_s)^{\mathsf T}\mathbf h/R$, giving the same three
components without separately differentiating Cartesian coordinates. With the
Euclidean norm for a complex vector, the exact magnitude is
$\sqrt{1+k^2R^2}/(4\pi R^2)$, which establishes the stated fixed-$k$
near-source asymptotic. The source is excluded throughout. No finding.

## D3-003: RF phase and the branch cut

On a nonzero response, the imaginary part of the logarithmic derivative
$(dH/d\omega)/H$ is
$(X(dY/d\omega)-Y(dX/d\omega))/(X^2+Y^2)$. This is an independent derivation
of the quotient-and-chain-rule calculation in the manuscript. It also proves
that the result remains valid at a nonzero imaginary-axis crossing, where the
particular $Y/X$ chart fails. For $H=\exp(\mathrm{i}\omega)$ it equals one.
The principal phase at $\omega=\pi$ has unequal one-sided limits, whereas the
unwrapped phase $\omega$ has derivative one there. Zeros and branch jumps are
distinguished correctly; no derivative is assigned to the discontinuous
principal phase. No finding.

## D3-004: ellipsoid height and surface normal

The two height partials follow from differentiating the square root on the
strict projected ellipse. An independent implicit calculation gives
$-F_x/F_z=-c^2x/(a^2g)$ and $-F_y/F_z=-c^2y/(b^2g)$; substituting the positive
height reproduces both displayed formulas. Normalizing the level gradient
cancels its common factor two. Its dot product with the outward radial vector is
positive on the ellipsoid, establishing orientation. The gradient vanishes only
at the origin, which is off the level surface. At an equatorial point at least
one of $F_x,F_y$ remains nonzero, so an alternate chart exists even though the
height chart fails. No finding.

## D3-005: one-sheet hyperboloid

Direct component cross multiplication gives
$(-ac\cosh^2u\cos v,-ac\cosh^2u\sin v,
a^2\sinh u\cosh u)^{\mathsf T}$. Its radial component is negative, so the
manuscript correctly reverses its direction for the requested normal. Factoring
$a\cosh u$ gives exactly the stated strictly positive cross-product norm.
As an independent orientation and regularity check, the gradient of
$x^2/a^2+y^2/a^2-z^2/c^2-1$ on the parameterization is a positive scalar
multiple of the stated outward normal. The parameterization satisfies the
surface equation by the hyperbolic identity. The angular seam is a periodic
identification and has no vanishing tangent cross product. No finding.

## D3-006: matrix-defined anisotropic scalar field

The double-sum differentiation correctly includes both occurrences of the input.
Alternatively, expanding $q(\mathbf x+\mathbf h)$ gives the linear term
$\mathbf h^{\mathsf T}(\mathbf Q+\mathbf Q^{\mathsf T})\mathbf x$ and quadratic
remainder $\mathbf h^{\mathsf T}\mathbf Q\mathbf h$. Symmetry therefore gives
the same $2\mathbf Q\mathbf x$ gradient, and the outer reciprocal-square-root
derivative yields the stated result. Positive definiteness gives the full
punctured-space real domain. For an indefinite symmetric matrix the real field
exists only on the open set $q>0$; the excluded zero cone can contain nonzero
points. The statement does not incorrectly extend the real formula to $q<0$.
The isotropic specialization is correct. No finding.

## D3-007: coupled field response

The derivative of the defining system gives
$d\mathbf j/dt=-\mathbf A^{-1}(d\mathbf A/dt)\mathbf j$ with the correct
multiplication order. The inverse determinant, both solution components, and
both expanded derivative numerators are correct for fixed complex right-hand
sides. An independent derivation uses the fixed eigenvectors
$\mathbf e_+=(1,1)^{\mathsf T}$ and $\mathbf e_-=(1,-1)^{\mathsf T}$:

$$
\mathbf j(t)=\frac{b_1+b_2}{2(1+t)}\mathbf e_+
+\frac{b_1-b_2}{2(1-t)}\mathbf e_-.
$$

Differentiating these two scalar coefficients recovers the displayed component
derivatives. Near $t=1$, the second mode diverges precisely when $b_1\ne b_2$.
Thus $(1,0)^{\mathsf T}$ gives the stated divergence and inconsistent singular
system; $(1,1)^{\mathsf T}$ gives a finite extended branch but not an inverse at
the singular parameter. The latter system has rank one and infinitely many
solutions, as stated. The original exclusions $t=\pm1$ are preserved after
cancellation. No finding.

## Verification and remaining scope

The independent supplementary script `/workspace/scratch/audit-d3-checks.py`
checks translated-source complex gradients, normals and cross products at varied
parameters, and the fixed-eigenbasis matrix solution against the component
solution. It uses only Python's standard library and nonsingular sample inputs.
Its successful execution is recorded by the integrating reviewer. Existing
finite-difference checks are additional evidence, not a proof at excluded
parameters. External reader feedback, independent human review, bibliographic
link availability, and rendered layout are outside this analytical chapter audit.
