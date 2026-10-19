# Proposed expansion of the worked problem collection

The next development milestone is beta.1; selection and acceptance criteria are
recorded in [BETA_PLAN.md](BETA_PLAN.md), with audit progress in
[BETA_REVIEW.md](BETA_REVIEW.md).

These are 32 original problem proposals for later development, not additions to
the current solved manuscript. They are organized for editorial planning only.
Each needs a complete derivation, three hints, domain analysis, and independent
verification before receiving a published problem ID. The next additions should
be mixed among existing settings rather than grouped by a prescribed technique.

Unless stated otherwise below, integration coordinates and varying parameters
are real scalars. A symbol declared fixed remains fixed during the requested
operation. Matrix and vector shapes are specified where they occur.

## Nonlinear derivatives and limits

1. **A smooth value with an oscillating slope.** For real $x\ne0$, the scalar
   function is $f(x)=(1+x^2)^{\sin(1/x)}$. Determine the continuous extension at
   zero, its derivative there, and whether the derivative is continuous.
   The useful distinction is between a difference quotient and the limit of the
   derivative away from zero. Check against logarithmic expansion and sequences
   approaching zero with different cosine values.
2. **A folded angle.** The scalar function is
   $f(x)=\arctan(2x/(1-x^2))$ for $x\ne\pm1$, with the principal real arctangent.
   Determine the derivative on each interval, the one-sided limits, and a
   continuous angle obtained by adding interval-dependent multiples of $\pi$.
   The challenge is reconstructing the function after a simple derivative appears.
3. **A coupled exponential constraint.** Near $(x,y)=(0,1)$, the dependent real
   scalar $y=g(x)$ satisfies $x\exp(y)+y\exp(x)=1$. Determine its first two
   derivatives at zero and a second-order approximation with a local remainder
   statement. Verify the approximation by substitution into the original relation.
4. **A norm at a collision.** With fixed real $a>0$ and independent vector
   $\mathbf x=(x,y,z)^{\mathsf T}\in\mathbb R^3$, consider the scalar
   $f(\mathbf x)=\|\mathbf x-a\mathbf e_1\|+\|\mathbf x+a\mathbf e_1\|$.
   Determine its gradient and Hessian off the two foci, then classify stationary
   points and differentiability at the foci. The constant vector
   $\mathbf e_1=(1,0,0)^{\mathsf T}$ is fixed.
5. **A phase zero rather than a phase cut.** For real frequency $\omega$ and fixed
   $\tau>0$, the complex scalar response is
   $H(\omega)=1-\exp(-\mathrm i\omega\tau)$. Determine continuous phase choices
   between zeros, their derivatives, and the local behavior at a zero. Comparison
   with the finite-aperture problem tests whether a zero is being confused with
   a removable quotient singularity.
6. **A moving maximum.** For independent real $t$, define the scalar
   $M(t)=\max_{0\le x\le1}\{tx-x^4\}$. Determine its piecewise formula and the
   orders of differentiability at changes in the maximizing point. Direct
   optimization and differentiation of the resulting formula provide separate checks.

## Integrals with parameters and competing limits

7. **A squared aperture kernel.** For fixed real $a>0$, evaluate
   $\int_0^\infty(\sin(ax)/x)^2\,dx$. Determine its dependence on $a$, including
   the extension to negative $a$, and explain what can go wrong in formal
   differentiation of the improper integral at zero.
8. **Two nearby poles off the real axis.** For positive real parameters $a,b$,
   evaluate $\int_0^\infty dx/((x^2+a^2)(x^2+b^2))$ and treat $a=b$ without
   subtracting nearly equal terms. A derivative with respect to a parameter
   provides a check on the coincident case.
9. **A logarithmic moment.** Evaluate
   $\int_0^1\ln^2(x)/(1+x)\,dx$ with a justified series representation and an
   explicit truncation error. The endpoint at zero and interchange of sum and
   integral are both part of the solution.
10. **A shrinking layer.** For real $a>0$, evaluate
    $F(a)=\int_0^1 a/(x^2+a^2)\,dx$ and determine the limit as $a$ decreases to
    zero. Compare the limiting integral with the integral of the pointwise limit,
    and identify the part of the domain carrying the missing contribution.
11. **A Gaussian with a moving truncation.** For real $t$ and fixed $L>0$, define
    $G(t;L)=\int_{-L}^{t}\exp(-(x-t)^2)\,dx$. Determine two derivatives and the
    limits as $t$ tends to either infinity. A shifted coordinate and the
    variable-limit formula should lead to the same result.
12. **A pole approaching an endpoint.** For real $0<a<1$, calculate
    $\operatorname{PV}\int_0^1\ln(x)/(x-a)\,dx$, with the symmetric exclusion
    around $a$ stated explicitly. An exact special-function representation is
    acceptable. Determine which endpoint limits exist and distinguish the
    principal value from ordinary improper integration.

## Geometry and surface integrals

13. **An oblique ellipsoidal cap.** The volume is
    $x^2/a^2+y^2/b^2+z^2/c^2\le1$ and
    $n_1x+n_2y+n_3z\ge h$, with fixed positive $a,b,c$ and fixed nonzero real
    vector $\mathbf n=(n_1,n_2,n_3)^{\mathsf T}$. Determine the scalar cap volume
    as a piecewise function of the real offset $h$, including empty and full caps.
14. **A triaxial surface area.** For fixed $a>b>c>0$, reduce the surface area of
    $x^2/a^2+y^2/b^2+z^2/c^2=1$ to a convergent integral suitable for numerical
    evaluation. Account for coordinate poles and verify the spherical limit.
    An elliptic-integral expression is a possible extension, not a required
    elementary simplification.
15. **A hyperboloidal shell.** For fixed positive $a,c,H$, determine the volume
    inside $x^2/a^2+y^2/a^2-z^2/c^2\le1$ with $|z|\le H$, and the flux of the
    real vector field $(x,y,z)^{\mathsf T}$ across its complete boundary.
    The caps and the curved surface have different outward normals.
16. **Circulation around an excluded axis.** The real vector field is
    $\mathbf F(x,y,z)=(-y,x,0)^{\mathsf T}/(x^2+y^2)$ on $x^2+y^2>0$.
    Determine its circulation around an ellipse encircling the axis and around
    a displaced circle that does not. Explain the regularity obstruction in
    applying Stokes' theorem to a spanning disk that meets the axis.
17. **An ellipse with a nonuniform line weight.** For fixed $a>b>0$, the planar
    vector path is $\mathbf r(t)=(a\cos t,b\sin t)^{\mathsf T}$, $0\le t\le2\pi$.
    Evaluate or reduce to standard elliptic integrals
    $\int_C x^2\,ds$, and obtain a controlled nearly circular approximation.
18. **A Gaussian on a rotated ellipsoid.** With a fixed real symmetric positive
    definite $3\times3$ matrix $\mathbf Q$, evaluate
    $\int_{\mathbf x^{\mathsf T}\mathbf Q\mathbf x\le1}
    \exp(-\mathbf x^{\mathsf T}\mathbf Q\mathbf x)\,d^3\mathbf x$.
    The solution should account for the determinant, rotation, and positive
    square root of the matrix. Here $d^3\mathbf x=dx\,dy\,dz$.

## Electromagnetic kernels and numerical integration

19. **An off-axis ring potential.** For fixed ring radius $a>0$, the scalar
    potential is the angular integral of
    $(a^2+\rho^2+z^2-2a\rho\cos\theta)^{-1/2}$ over $0\le\theta\le2\pi$,
    where $\rho\ge0$ and $z$ are observation parameters. Obtain an elliptic
    representation, the on-axis limit, and the nature of the singularity at
    $(\rho,z)=(a,0)$.
20. **A source inside a triangular panel.** On the triangle $0\le y\le x\le1$,
    take a fixed interior source $(x_0,y_0)$. Reduce
    $\iint ((x-x_0)^2+(y-y_0)^2)^{-1/2}\,dx\,dy$ to nonsingular integrals by
    partitioning the triangle around the source. The partition and each Jacobian
    are part of the work; comparison with numerical quadrature supplies a check.
21. **A linearly weighted panel.** On the same triangle with a source at its
    origin, evaluate $\iint (\alpha+\beta x+\gamma y)/\sqrt{x^2+y^2}\,dx\,dy$,
    for fixed real scalar weights $\alpha,\beta,\gamma$. Relate the separate
    moments to a general linear testing function.
22. **Subtracting a Green-kernel singularity.** For fixed real $k$ and positive
    radial distance $r$, analyze
    $q(r;k)=(\exp(-\mathrm i k r)-1)/r$. Find its continuous extension and radial
    derivative at zero, then decide whether $q(\|\mathbf x\|;k)$ is differentiable
    as a function of the real vector $\mathbf x\in\mathbb R^3$ at the origin.
    Radial and spatial differentiability are distinct questions.
23. **A circular aperture transform.** For fixed $a>0$ and independent real
    transverse wavenumber $q$, calculate
    $\int_0^a\int_0^{2\pi}\exp(\mathrm i q r\cos\theta)r\,d\theta\,dr$.
    Give a Bessel representation, the value at zero, and a small-$q$ error estimate.
24. **A rapidly oscillating finite integral.** For fixed real $a>0$ and varying
    $k>0$, analyze $\int_{-a}^{a}\exp(\mathrm i kx^2)\,dx$. Compare an exact
    integral representation with its large-$k$ behavior. The stationary point at
    zero prevents a uniform integration-by-parts argument based on $1/x$.

## Matrices, constraints, and tensor contractions

25. **A matrix exponential across a change of regime.** For independent real $t$,
    define the real matrix $\mathbf A(t)=\begin{pmatrix}0&1\\-t&0\end{pmatrix}$.
    Determine $\exp(\mathbf A(t))$ and its derivative for positive, zero, and
    negative $t$. Its power series supplies the connection between the
    trigonometric and hyperbolic formulas and a check at zero.
26. **A logarithmic determinant along a constrained path.** For independent
    real $t$, let $\mathbf A(t)=\begin{pmatrix}1+t^2&t\\t&1\end{pmatrix}$.
    Differentiate the scalar $\ln\det\mathbf A(t)$ directly and through the
    trace formula. Explain why separately treating the two off-diagonal entries
    as independent would give an incorrect path calculation if only one varied.
27. **Sensitivity of a quadratic response.** With fixed real symmetric positive
    definite matrix $\mathbf A\in\mathbb R^{n\times n}$, fixed vectors
    $\mathbf b,\mathbf u\in\mathbb R^n$, and real parameter $t$, determine the
    first two derivatives of
    $s(t)=\mathbf b^{\mathsf T}(\mathbf A+t\mathbf u\mathbf u^{\mathsf T})^{-1}\mathbf b$.
    Find the full invertibility domain and examine exceptional cancellations.
28. **A constrained matrix gradient.** For a symmetric positive definite
    $2\times2$ real matrix with independent parameters $a,b,c$ and entries
    $\begin{pmatrix}a&b\\b&c\end{pmatrix}$, differentiate the scalar
    $f(a,b,c)=\ln(ac-b^2)+\operatorname{tr}(\mathbf A^{-1})$.
    Compare the parameter gradient with the unconstrained entry derivatives.
29. **A fourth-order energy contraction.** In a fixed orthonormal basis, let
    $C_{ijkl}$ be fixed real components with specified minor and major symmetries,
    and let $E_{ij}(t)$ be the components of a differentiable real symmetric
    $3\times3$ matrix. Differentiate
    $W(t)=\frac12\sum_{i,j,k,l=1}^3C_{ijkl}E_{ij}(t)E_{kl}(t)$ twice.
    Every contraction is expanded sufficiently to show which symmetry combines
    terms; an anisotropic numerical tensor supplies an independent check.
30. **A normalized vector and its curvature.** With independent real $t$,
    define $\mathbf v(t)=(\exp(t),\sin t,t)^{\mathsf T}$ and
    $\mathbf n(t)=\mathbf v(t)/\|\mathbf v(t)\|$. Find two derivatives and verify
    the identities obtained by differentiating $\mathbf n(t)^{\mathsf T}\mathbf n(t)=1$.
    The vector is nonzero for all real $t$.
31. **A rotating anisotropic tensor.** For a real angle $t$, let
    $\mathbf R(t)=\begin{pmatrix}\cos t&-\sin t\\\sin t&\cos t\end{pmatrix}$
    and let $\mathbf D=\operatorname{diag}(a,b)$ with fixed $a,b>0$.
    Differentiate $\mathbf Q(t)=\mathbf R(t)\mathbf D\mathbf R(t)^{\mathsf T}$
    and the scalar energy $\mathbf x^{\mathsf T}\mathbf Q(t)\mathbf x$ for a fixed
    real vector $\mathbf x\in\mathbb R^2$. Equal eigenvalues provide a limiting check.
32. **An integral of a matrix-valued resolvent.** For a fixed real symmetric
    positive definite $n\times n$ matrix $\mathbf A$, evaluate
    $\int_0^\infty(\mathbf A+s\mathbf I)^{-2}\,ds$ entrywise and determine how
    the result changes under a differentiable symmetric perturbation of
    $\mathbf A$. Matrix multiplication order is retained throughout.

## References for development

These references support the mathematical methods and definitions behind the
proposals. The statements above are original editorial proposals rather than
transcriptions of source exercises.

- [NIST DLMF 19.2](https://dlmf.nist.gov/19.2): definitions and branch conventions
  for elliptic integrals, relevant to the ring, ellipse, and ellipsoid problems.
- [NIST DLMF 10.9](https://dlmf.nist.gov/10.9): angular integral representations of
  Bessel functions, relevant to the circular aperture.
- [NIST DLMF 2.3](https://dlmf.nist.gov/2.3): asymptotic analysis of real-variable
  integrals, including oscillatory and stationary-phase problems.
- [MIT 18.S096 lecture notes](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/pages/lecture-notes-and-readings/):
  derivatives as linear maps, matrix calculus, and derivatives of matrix functions.

The first expansion could develop proposals 1, 7, 8, 13, 19, 20, 22, 23, 25, 27,
29, and 31. Together they add twelve substantially different decisions about
representation, geometry, and domain, while extending the existing notation and
application settings. The remaining proposals provide a second group with more
asymptotic, constrained, and special-function work.
