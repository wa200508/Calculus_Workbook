# D3 · Fields, phase, and geometric domains

A derivative may be formally correct and still be used outside its domain. In
field calculations, the source point may be excluded, a square root may change
from real to imaginary, and a smooth surface may fail to be a graph in the
chosen coordinates. These examples progress from a scalar waveguide parameter
to vector fields, implicit geometry, and matrix-valued sensitivity.

## Rules and conventions

All spatial coordinates and differentiation parameters below are real scalars.
A complex scalar output is differentiated with respect to a real input by
differentiating its real and imaginary parts. The symbol $\mathrm{i}$ denotes
the fixed imaginary unit, with $\mathrm{i}^2=-1$; it is not an index.
The Euclidean gradient of a scalar field $f(x,y,z)$ is a real or complex column
vector of its three coordinate partial derivatives. The other two independent
coordinates are held fixed in each entry.

For a scalar level set $F(x,y,z)=0$, a local graph $z=g(x,y)$ is guaranteed near
a point only when $F$ is continuously differentiable there and
$\frac{\partial}{\partial z}(F(x,y,z))\ne0$ at that point. A surface can remain
smooth when this particular graph representation fails.

## Problems

### D3-001 — Waveguide sensitivity at cutoff

**Objects and dependencies.** $\omega>0$ is an independent real scalar angular frequency. The real scalars $c>0$ (wave speed) and $\omega_c>0$ (cutoff frequency) are fixed. Define the nonnegative real scalar propagation constant

$$
\beta(\omega)=\frac{1}{c}\sqrt{\omega^2-\omega_c^2},\qquad \omega\ge\omega_c.
$$

Find $\frac{d}{d\omega}(\beta(\omega))$ on its differentiability domain, the right-hand behavior at cutoff, and the group velocity $v_g(\omega)=1/[\frac{d}{d\omega}(\beta(\omega))]$ for $\omega>\omega_c$. Describe why extending this real formula below cutoff is invalid.

### D3-002 — Spatial gradient of a complex Green kernel

**Objects and dependencies.** $x,y,z$ are independent real scalar observation coordinates. Fixed real scalars $x_s,y_s,z_s$ locate a source. The fixed real scalar wavenumber is $k\ge0$. Define

$$
R(x,y,z)=\sqrt{(x-x_s)^2+(y-y_s)^2+(z-z_s)^2},\qquad
G(x,y,z)=\frac{\exp(-\mathrm{i}kR(x,y,z))}{4\pi R(x,y,z)}.
$$

The real distance satisfies $R(x,y,z)>0$; $G(x,y,z)$ is complex scalar-valued. Find the complex column vector $\nabla_{x,y,z}G(x,y,z)$, with the source and $k$ held fixed. State its behavior as the source is approached.

### D3-003 — RF phase and the branch cut

**Objects and dependencies.** $\omega$ is an independent real scalar. $X(\omega),Y(\omega)$ are differentiable real scalar functions; $H(\omega)=X(\omega)+\mathrm{i}Y(\omega)$ is a complex scalar response. The principal phase $\phi(\omega)=\operatorname{atan2}(Y(\omega),X(\omega))$ takes values in $(-\pi,\pi]$. Find its derivative away from zeros and the principal branch cut, and apply the result to $H(\omega)=\exp(\mathrm{i}\omega)$ near $\omega=\pi$. Distinguish principal phase from a locally unwrapped phase.

### D3-004 — An ellipsoid is smooth where its height graph fails

**Objects and dependencies.** Fixed real semiaxes $a,b,c$ are positive. $x,y,z$ are independent real coordinates of the scalar level function

$$
F(x,y,z)=\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}-1.
$$

On the upper ellipsoid, the dependent real scalar height is
$z=g(x,y)=c\sqrt{1-x^2/a^2-y^2/b^2}$. Find its two partial derivatives on their open domain. Find the outward real unit normal to the full ellipsoid, including the equator, and explain the difference between a graph singularity and a surface singularity.

### D3-005 — Hyperboloid normal and an indefinite quadratic form

**Objects and dependencies.** Fixed real scalars $a,c>0$ are lengths. $u\in\mathbb R$ and $v\in[0,2\pi)$ are independent dimensionless real parameters. Define the real column vector

$$
\mathbf r(u,v)=\begin{bmatrix}a\cosh(u)\cos(v)\\a\cosh(u)\sin(v)\\c\sinh(u)\end{bmatrix}.
$$

Find the tangent vectors, their cross product, and a unit normal pointing away from the axis on the one-sheet hyperboloid $x^2/a^2+y^2/a^2-z^2/c^2=1$. Decide whether any finite parameter value makes the surface singular. The interval in $v$ identifies the same angular seam at its ends.

### D3-006 — A matrix-defined anisotropic scalar field

**Objects and dependencies.** $\mathbf x\in\mathbb R^3$ is an independent real column vector with coordinates $x_1,x_2,x_3$. $\mathbf Q$ is a fixed real symmetric positive-definite $3\times3$ matrix; $\mathbf x^{\mathsf T}$ is its input's row transpose. Define the real scalar functions

$$
q(\mathbf x)=\mathbf x^{\mathsf T}\mathbf Q\mathbf x,\qquad
\Phi(\mathbf x)=q(\mathbf x)^{-1/2},\qquad \mathbf x\ne\mathbf0.
$$

Find the real column vector $\nabla_{\mathbf x}\Phi(\mathbf x)$ with $\mathbf Q$ held fixed, showing the component differentiation of $q(\mathbf x)$. Explain what changes if positive definiteness is replaced by an indefinite symmetric matrix.

### D3-007 — Sensitivity of a CEM matrix solve near singularity

**Objects and dependencies.** $t$ is an independent dimensionless real scalar. A fixed complex column vector is $\mathbf b=[b_1,b_2]^{\mathsf T}$. Define the real $2\times2$ matrix and dependent complex column vector

$$
\mathbf A(t)=\begin{bmatrix}1&t\\t&1\end{bmatrix},\qquad
\mathbf j(t)=\mathbf A(t)^{-1}\mathbf b,\qquad t\ne-1,1.
$$

Find $\frac{d}{dt}(\mathbf j(t))$ without treating matrix division as scalar division. Also find the component formulas and determine the behavior near $t=1$ for $\mathbf b=[1,0]^{\mathsf T}$ and $\mathbf b=[1,1]^{\mathsf T}$. This small system models a parameter-dependent discretized field equation; it is not a full electromagnetic solver.

## Hint ladders

### D3-001

1. The radicand is positive only above cutoff; the derivative of a square root includes its reciprocal.
2. Differentiation gives a factor $2\omega$, which cancels the square root rule's two.
3. At cutoff, the difference quotient scales as the reciprocal square root of the frequency increment.

### D3-002

1. The observation coordinates enter the kernel through the scalar distance.
2. Differentiate $\exp(-\mathrm{i}kR)/(4\pi R)$ first with respect to a separate scalar distance variable.
3. Each coordinate derivative of the distance is a displacement component divided by the distance.

### D3-003

1. A local angle derivative can be computed without selecting a global inverse tangent.
2. On a chart with $X(\omega)\ne0$, differentiate $\arctan(Y(\omega)/X(\omega))$ plus a locally constant multiple of $\pi$.
3. The resulting denominator is $X(\omega)^2+Y(\omega)^2$; the principal phase still jumps on the negative real axis.

### D3-004

1. The square root's argument is strictly positive on the interior of the projected ellipse.
2. Implicit differentiation gives the same height derivative when the $z$ partial derivative of $F(x,y,z)$ is nonzero.
3. The full gradient of $F(x,y,z)$ never vanishes on the ellipsoid, even when its $z$ component vanishes.

### D3-005

1. Differentiate each of the three components with respect to one parameter at a time.
2. The cross product can be expanded using its three scalar components.
3. Compare its direction with the gradient of the hyperboloid's level function.

### D3-006

1. Expand the quadratic form as a double sum over matrix entries.
2. Differentiating with respect to $x_\ell$ produces one contribution from each occurrence of $\mathbf x$.
3. Symmetry combines the contributions into $2(\mathbf Q\mathbf x)_\ell$ before the outer chain rule is applied.

### D3-007

1. The identity $\mathbf A(t)\mathbf j(t)=\mathbf b$ can be differentiated while $\mathbf b$ is fixed.
2. Multiplication by $\mathbf A(t)^{-1}$ is on the left; the order of the matrices matters.
3. The determinant is $1-t^2$. A compatible right-hand side can cancel a pole in the solution, although the matrix remains singular at the excluded value.

## Complete solutions

### D3-001

**Step 1 — SETUP.** The variable is the real scalar $\omega$; $c$ and $\omega_c$ are fixed. The output $\beta(\omega)$ is real on $[\omega_c,\infty)$ and smooth on $(\omega_c,\infty)$. The derivative is sought on that open interval first.

**Step 2 — CHOICE.** The square root is a composition. Its derivative rule requires a strictly positive radicand here; the endpoint therefore needs a separate limit.

**Step 3 — CALCULUS.** With respect to $\omega$,

$$
\frac{d}{d\omega}\left(\beta(\omega)\right)
=\frac{1}{c}\frac{1}{2\sqrt{\omega^2-\omega_c^2}}\frac{d}{d\omega}\left(\omega^2-\omega_c^2\right)
=\frac{\omega}{c\sqrt{\omega^2-\omega_c^2}}.
$$

**Step 4 — ALGEBRA.** For $\omega>\omega_c$ the derivative is positive, so its reciprocal is defined:

$$
v_g(\omega)=\frac{c\sqrt{\omega^2-\omega_c^2}}{\omega}
=c\sqrt{1-\frac{\omega_c^2}{\omega^2}}.
$$

**Step 5 — DOMAIN.** For a real scalar increment $h>0$,

$$
\frac{\beta(\omega_c+h)-\beta(\omega_c)}{h}
=\frac{\sqrt{2\omega_c h+h^2}}{ch}
=\frac{\sqrt{2\omega_c+h}}{c\sqrt h}\longrightarrow+\infty.
$$

There is no finite right derivative at cutoff. Below cutoff the radicand is negative. In the convention $\exp(\mathrm{i}\omega t-\mathrm{i}\beta z)$, a decaying field for $z>0$ has $\beta=-\mathrm{i}\alpha$, where $\alpha=\sqrt{\omega_c^2-\omega^2}/c>0$ is a real attenuation constant. That is a different branch and a different physical regime.

**Step 6 — CHECK.** The derivative has units of inverse velocity. The limits are $v_g(\omega)\to0$ as $\omega\downarrow\omega_c$ and $v_g(\omega)\to c$ as $\omega\to\infty$. Large sensitivity near cutoff is expected; a high-frequency approximation is unreliable there.

**Recognition cue.** A parameter-dependent square root often marks the boundary between regimes. Its endpoint is part of the function's domain without being part of the finite-derivative domain.

### D3-002

**Step 1 — SETUP.** The observation coordinates are independent real scalars, the source and $k$ are fixed, and $G(x,y,z)$ is a complex scalar on the punctured space $R(x,y,z)>0$. The derivative output is a complex $3\times1$ vector.

**Step 2 — CHOICE.** Dependence through distance separates the radial derivative from the coordinate derivatives. A separate positive real scalar $\rho$ gives $g(\rho)=\exp(-\mathrm{i}k\rho)/(4\pi\rho)$ and $G(x,y,z)=g(R(x,y,z))$.

**Step 3 — CALCULUS.** The product rule and chain rule give

$$
\begin{aligned}
\frac{d}{d\rho}\left(g(\rho)\right)
&=\frac{1}{4\pi}\left((-\mathrm{i}k)\exp(-\mathrm{i}k\rho)\rho^{-1}-\exp(-\mathrm{i}k\rho)\rho^{-2}\right),\\
\frac{\partial}{\partial x}\left(R(x,y,z)\right)&=\frac{x-x_s}{R(x,y,z)},\\
\frac{\partial}{\partial y}\left(R(x,y,z)\right)&=\frac{y-y_s}{R(x,y,z)},\\
\frac{\partial}{\partial z}\left(R(x,y,z)\right)&=\frac{z-z_s}{R(x,y,z)}.
\end{aligned}
$$

In each partial derivative the other two coordinates are held fixed.

**Step 4 — ALGEBRA.** Factoring the radial derivative gives

$$
\frac{d}{d\rho}\left(g(\rho)\right)
=-\frac{\exp(-\mathrm{i}k\rho)(1+\mathrm{i}k\rho)}{4\pi\rho^2}.
$$

Multiplication by the distance gradient yields

$$
\nabla_{x,y,z}G(x,y,z)
=-\frac{\exp(-\mathrm{i}kR(x,y,z))(1+\mathrm{i}kR(x,y,z))}{4\pi R(x,y,z)^3}
\begin{bmatrix}x-x_s\\y-y_s\\z-z_s\end{bmatrix}.
$$

**Step 5 — CHECK.** For $k=0$, the Coulomb-kernel gradient is recovered. The displacement vector has magnitude $R(x,y,z)$, so the gradient magnitude behaves as $1/(4\pi R(x,y,z)^2)$ near the source. The kernel itself behaves as $1/(4\pi R(x,y,z))$. Neither formula defines a value at the source. A distributional source equation cannot be inferred by simply substituting $R=0$ into these classical derivatives.

**Recognition cue.** A radial chain rule reduces component work, but it preserves the excluded source point. Differentiation strengthens the singularity and can change whether a later integral exists.

### D3-003

**Step 1 — SETUP.** The input is a real scalar $\omega$, and the output phase is real. A smooth local phase requires $H(\omega)\ne0$ and a chart avoiding the selected branch cut. $X(\omega)$ and $Y(\omega)$ both depend on $\omega$.

**Step 2 — CHOICE.** On a local chart with $X(\omega)\ne0$, a constant angular correction distinguishes $\operatorname{atan2}$ from $\arctan(Y/X)$. The correction has zero derivative on that chart.

**Step 3 — CALCULUS.** The chain and quotient rules give

$$
\frac{d}{d\omega}\left(\phi(\omega)\right)
=\frac{1}{1+(Y(\omega)/X(\omega))^2}
\frac{X(\omega)\frac{d}{d\omega}(Y(\omega))-Y(\omega)\frac{d}{d\omega}(X(\omega))}{X(\omega)^2}.
$$

**Step 4 — ALGEBRA.** Since $1+(Y/X)^2=(X^2+Y^2)/X^2$ on this chart,

$$
\frac{d}{d\omega}\left(\phi(\omega)\right)
=\frac{X(\omega)\frac{d}{d\omega}(Y(\omega))-Y(\omega)\frac{d}{d\omega}(X(\omega))}{X(\omega)^2+Y(\omega)^2}.
$$

A chart using $Y(\omega)\ne0$ gives the same expression. The expression therefore applies at $X=0,Y\ne0$ too, when the local phase is smooth.

**Step 5 — TRICK: Euler identity.** The supporting identity is listed in [T-001](TRICKS_APPENDIX.md#t-001-euler-identities). For $H(\omega)=\exp(\mathrm{i}\omega)$, $X(\omega)=\cos\omega$ and $Y(\omega)=\sin\omega$. The numerator is $\cos^2\omega+\sin^2\omega=1$, and the denominator is also one. Every smooth local phase has derivative one.

**Step 6 — DOMAIN AND CHECK.** The principal phase approaches $\pi$ from the left at $\omega=\pi$, but approaches $-\pi$ from the right. It is discontinuous there and has no derivative there. The unwrapped choice $\widetilde\phi(\omega)=\omega$ is smooth through that point, with derivative one. At a zero of $H(\omega)$, no phase is defined at all. A group-delay calculation based on phase differentiation depends on both a nonzero response and a consistent local phase choice.

**Recognition cue.** A finite algebraic derivative expression does not repair a discontinuity in the function being differentiated.

### D3-004

**Step 1 — SETUP.** The graph uses independent real $x,y$ in $x^2/a^2+y^2/b^2<1$. Its dependent scalar $g(x,y)>0$ is the upper height. The full level surface also contains the lower half and equator.

**Step 2 — CHOICE.** The graph chain rule gives derivatives in its open domain. The level-set gradient gives a normal without selecting an upper or lower height branch.

**Step 3 — CALCULUS.** Holding $y$ fixed and then $x$ fixed gives

$$
\begin{aligned}
\frac{\partial}{\partial x}\left(g(x,y)\right)&=-\frac{cx}{a^2\sqrt{1-x^2/a^2-y^2/b^2}},\\
\frac{\partial}{\partial y}\left(g(x,y)\right)&=-\frac{cy}{b^2\sqrt{1-x^2/a^2-y^2/b^2}}.
\end{aligned}
$$

For the level function, each of $x,y,z$ is independent during differentiation:

$$
\nabla_{x,y,z}F(x,y,z)=\begin{bmatrix}2x/a^2\\2y/b^2\\2z/c^2\end{bmatrix}.
$$

**Step 4 — ALGEBRA.** Dividing this real vector by its Euclidean length cancels its common factor two:

$$
\mathbf n(x,y,z)=\frac{\begin{bmatrix}x/a^2\\y/b^2\\z/c^2\end{bmatrix}}
{\sqrt{x^2/a^4+y^2/b^4+z^2/c^4}}.
$$

It points outward since $F$ increases away from the ellipsoid.

**Step 5 — DOMAIN AND CHECK.** At the equator $z=0$, the $z$ partial derivative of $F$ vanishes, so the implicit-function theorem does not provide a height graph there. For example, at $(a,0,0)$ the $x$ partial derivative is $2/a\ne0$, and a smooth graph of $x$ in terms of $y,z$ is available. The full gradient could vanish only at $(0,0,0)$, which is not on the ellipsoid. The unit normal is defined at every surface point and has length one.

**Recognition cue.** The failure of one coordinate chart is not the failure of the underlying geometry. The denominator in implicit differentiation identifies which chart is available.

### D3-005

**Step 1 — SETUP.** Independent parameters $u,v$ are real scalars. Both tangent derivatives and their cross product are real $3\times1$ vectors. The fixed parameters $a,c$ are positive.

**Step 2 — CHOICE.** Parametric tangent vectors avoid solving the hyperboloid for a single height branch. Their cross product supplies an oriented normal when it is nonzero.

**Step 3 — CALCULUS.** Component differentiation gives

$$
\begin{aligned}
\frac{\partial}{\partial u}\left(\mathbf r(u,v)\right)&=\begin{bmatrix}a\sinh(u)\cos(v)\\a\sinh(u)\sin(v)\\c\cosh(u)\end{bmatrix},\\
\frac{\partial}{\partial v}\left(\mathbf r(u,v)\right)&=\begin{bmatrix}-a\cosh(u)\sin(v)\\a\cosh(u)\cos(v)\\0\end{bmatrix}.
\end{aligned}
$$

**Step 4 — ALGEBRA.** In the order $u$ tangent crossed with $v$ tangent, the three components are

$$
\mathbf w(u,v)=\begin{bmatrix}
0-ac\cosh^2(u)\cos(v)\\
-ac\cosh^2(u)\sin(v)-0\\
a^2\sinh(u)\cosh(u)(\cos^2(v)+\sin^2(v))
\end{bmatrix}.
$$

**Step 5 — TRICK: hyperbolic identity.** The real identities are listed in [T-007](TRICKS_APPENDIX.md#t-007-hyperbolic-identities-and-real-branches). The identity $\cosh^2(u)-\sinh^2(u)=1$ establishes the surface equation. The identity $\cos^2(v)+\sin^2(v)=1$ and the positivity of $\cosh(u)$ give

$$
\|\mathbf w(u,v)\|=a\cosh(u)\sqrt{c^2\cosh^2(u)+a^2\sinh^2(u)}>0.
$$

**Step 6 — RESULT AND CHECK.** $\mathbf w$ points toward the axis, so the requested real unit normal is

$$
\mathbf n(u,v)=\frac{\begin{bmatrix}c\cosh(u)\cos(v)\\c\cosh(u)\sin(v)\\-a\sinh(u)\end{bmatrix}}
{\sqrt{c^2\cosh^2(u)+a^2\sinh^2(u)}}.
$$

Its dot product with each tangent is zero; its length is one. At $u=0$ it is the horizontal radial unit vector. No finite $u,v$ makes the tangent cross product zero. Periodicity at the angular seam is a coordinate identification rather than a singularity.

**Recognition cue.** The sign in an indefinite quadratic form changes the geometry, while normal orientation still depends on the order of a cross product.

### D3-006

**Step 1 — SETUP.** Independent input $\mathbf x$ has three real scalar coordinates. The symmetric matrix $\mathbf Q$ is fixed. Positive definiteness gives $q(\mathbf x)>0$ whenever $\mathbf x\ne\mathbf0$, so the real scalar reciprocal square root is differentiable there.

**Step 2 — CHOICE.** Component expansion resolves the two appearances of the input before the outer scalar chain rule is applied. The output gradient is a real $3\times1$ column vector.

**Step 3 — ALGEBRA.** With independent indices $i,j$ from one to three,

$$
q(\mathbf x)=\sum_{i=1}^3\sum_{j=1}^3 x_i Q_{ij}x_j.
$$

**Step 4 — CALCULUS.** Differentiation with respect to the scalar coordinate $x_\ell$, with the other coordinates held fixed, gives

$$
\frac{\partial}{\partial x_\ell}\left(q(\mathbf x)\right)
=\sum_{j=1}^3Q_{\ell j}x_j+\sum_{i=1}^3x_iQ_{i\ell}.
$$

**Step 5 — ALGEBRA.** Symmetry gives $Q_{i\ell}=Q_{\ell i}$, so both sums are the same component of $\mathbf Q\mathbf x$. Thus $\nabla_{\mathbf x}q(\mathbf x)=2\mathbf Q\mathbf x$. Without symmetry the result would instead be $(\mathbf Q+\mathbf Q^{\mathsf T})\mathbf x$.

**Step 6 — CALCULUS.** The scalar outer derivative is $-(1/2)q^{-3/2}$, hence

$$
\nabla_{\mathbf x}\Phi(\mathbf x)
=-\frac{\mathbf Q\mathbf x}{(\mathbf x^{\mathsf T}\mathbf Q\mathbf x)^{3/2}}.
$$

**Step 7 — DOMAIN AND CHECK.** For $\mathbf Q=\mathbf I$, the expression becomes $-\mathbf x/\|\mathbf x\|^3$. For an indefinite symmetric $\mathbf Q$, the same real formula is valid only in the open set $q(\mathbf x)>0$; nonzero inputs on the cone $q(\mathbf x)=0$ are also singular. Inputs with $q(\mathbf x)<0$ do not define this real scalar field. Matrix symmetry simplifies differentiation; positive definiteness supplies a separate domain guarantee.

**Recognition cue.** A matrix property can justify a domain assumption, rather than merely make the algebra shorter.

### D3-007

**Step 1 — SETUP.** The variable is the real scalar $t$; $\mathbf b$ is fixed and complex. $\mathbf A(t)$ is a real matrix and $\mathbf j(t)$ a complex $2\times1$ vector. The matrix is invertible exactly when $1-t^2\ne0$.

**Step 2 — CHOICE.** Differentiation of the defining linear system preserves multiplication order and avoids a nonexistent rule for scalar-style matrix division.

**Step 3 — CALCULUS.** The matrix product rule is applied entry by entry:

$$
\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf j(t)
+\mathbf A(t)\frac{d}{dt}\left(\mathbf j(t)\right)=\mathbf0,
\qquad \frac{d}{dt}\left(\mathbf A(t)\right)=\begin{bmatrix}0&1\\1&0\end{bmatrix}.
$$

Multiplication on the left by the inverse gives

$$
\frac{d}{dt}\left(\mathbf j(t)\right)
=-\mathbf A(t)^{-1}\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf A(t)^{-1}\mathbf b.
$$

**Step 4 — ALGEBRA.** The explicit inverse and solution are

$$
\mathbf A(t)^{-1}=\frac{1}{1-t^2}\begin{bmatrix}1&-t\\-t&1\end{bmatrix},\qquad
\mathbf j(t)=\frac{1}{1-t^2}\begin{bmatrix}b_1-tb_2\\b_2-tb_1\end{bmatrix}.
$$

The quotient rule and numerator expansion produce

$$
\frac{d}{dt}\left(\mathbf j(t)\right)
=\frac{1}{(1-t^2)^2}\begin{bmatrix}
-b_2(1-t^2)+2t(b_1-tb_2)\\
-b_1(1-t^2)+2t(b_2-tb_1)
\end{bmatrix}
=\frac{1}{(1-t^2)^2}\begin{bmatrix}2tb_1-(1+t^2)b_2\\2tb_2-(1+t^2)b_1\end{bmatrix}.
$$

**Step 5 — DOMAIN AND CHECK.** For $\mathbf b=[1,0]^{\mathsf T}$, the solution diverges at $t=1$, and the singular system there is inconsistent. For $\mathbf b=[1,1]^{\mathsf T}$, cancellation on $t\ne\pm1$ gives $\mathbf j(t)=[1,1]^{\mathsf T}/(1+t)$ and derivative $-[1,1]^{\mathsf T}/(1+t)^2$. This solution branch has a finite extension at $t=1$, but the matrix inverse still does not exist there; the singular system has infinitely many solutions. Substitution into the original nonsingular system verifies both component formulas.

**Recognition cue.** The sensitivity of a matrix solve depends on the right-hand side as well as proximity to a singular matrix. Cancellation in one solution does not extend the inverse operator.

## Application references

These are original review problems. The waveguide model is motivated by
[MIT 6.013, Lecture 16](https://www.ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/d9425aa2b1acd0c1fc121965ad7eafec_MIT6_013S09_lec16.pdf).
Singular Green kernels and discretized field systems occur in the integral-equation
work discussed by [Tihon and Craeye, All-analytical evaluation of the singular integrals involved in the Method of Moments](https://arxiv.org/abs/1911.12660).
The small scalar and matrix models isolate calculus issues; their solutions do
not constitute full waveguide or antenna designs.
