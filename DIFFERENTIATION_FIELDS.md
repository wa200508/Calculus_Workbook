# D3 · Fields and geometric constraints

## Problems

### D3-001 — Waveguide sensitivity at cutoff

**Objects and dependencies.** $\omega>0$ is an independent real scalar angular frequency. The real scalars $c>0$ (wave speed) and $\omega_c>0$ (cutoff frequency) are fixed. Define the nonnegative real scalar propagation constant

$$
\beta(\omega)=\frac{1}{c}\sqrt{\omega^2-\omega_c^2},\qquad \omega\ge\omega_c.
$$

Find $\frac{d}{d\omega}(\beta(\omega))$ on its differentiability domain, the right-hand behavior at cutoff, and the group velocity $v_g(\omega)=\frac{1}{\frac{d}{d\omega}\left(\beta(\omega)\right)}$ for $\omega>\omega_c$. Describe why extending this real formula below cutoff is invalid.

### D3-002 — Spatial gradient of a complex Green kernel

**Objects and dependencies.** $x,y,z$ are independent real scalar observation coordinates. Fixed real scalars $x_s,y_s,z_s$ locate a source. The fixed real scalar wavenumber is $k\ge0$. Define

$$
R(x,y,z)=\sqrt{(x-x_s)^2+(y-y_s)^2+(z-z_s)^2},\qquad
G(x,y,z)=\frac{\exp(-\mathrm{i}kR(x,y,z))}{4\pi R(x,y,z)}.
$$

The real distance satisfies $R(x,y,z)>0$; $G(x,y,z)$ is complex scalar-valued. Find the complex column vector $\nabla_{x,y,z}G(x,y,z)$, with the source and $k$ held fixed. State its behavior as the source is approached.

### D3-003 — RF phase and the branch cut

**Objects and dependencies.** $\omega$ is an independent real scalar. $X(\omega),Y(\omega)$ are differentiable real scalar functions; $H(\omega)=X(\omega)+\mathrm{i}Y(\omega)$ is a complex scalar response. The principal phase $\phi(\omega)=\operatorname{atan2}(Y(\omega),X(\omega))$ takes values in $(-\pi,\pi]$. Find its derivative away from zeros and the principal branch cut, and apply the result to $H(\omega)=\exp(\mathrm{i}\omega)$ near $\omega=\pi$. Distinguish principal phase from a locally unwrapped phase.

### D3-004 — Ellipsoid height and surface normal

**Objects and dependencies.** Fixed real semiaxes $a,b,c$ are positive. $x,y,z$ are independent real coordinates of the scalar level function

$$
F(x,y,z)=\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}-1.
$$

On the upper ellipsoid, the dependent real scalar height is
$z=g(x,y)=c\sqrt{1-x^2/a^2-y^2/b^2}$. Find its two partial derivatives on their open domain. Find the outward real unit normal to the full ellipsoid, including the equator, and explain the difference between a graph singularity and a surface singularity.

### D3-005 — A one-sheet hyperboloid

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

### D3-007 — A coupled field response

**Objects and dependencies.** $t$ is an independent dimensionless real scalar. A fixed complex column vector is $\mathbf b=[b_1,b_2]^{\mathsf T}$. Define the real $2\times2$ matrix and dependent complex column vector

$$
\mathbf A(t)=\begin{bmatrix}1&t\\t&1\end{bmatrix},\qquad
\mathbf j(t)=\mathbf A(t)^{-1}\mathbf b,\qquad t\ne-1,1.
$$

Find $\frac{d}{dt}(\mathbf j(t))$ without treating matrix division as scalar division. Also find the component formulas and determine the behavior near $t=1$ for $\mathbf b=[1,0]^{\mathsf T}$ and $\mathbf b=[1,1]^{\mathsf T}$. This small system models a parameter-dependent discretized field equation; it is not a full electromagnetic solver.

### D3-008 — A quadratic response near loss of invertibility

**Objects and dependencies.** The positive integer $n$ is fixed. The real symmetric positive-definite matrix $\mathbf A\in\mathbb R^{n\times n}$ and real column vectors $\mathbf b,\mathbf u\in\mathbb R^n$ are fixed. The independent real scalar parameter is $t$. Define

$$
\mathbf B(t)=\mathbf A+t\mathbf u\mathbf u^{\mathsf T},\qquad
s(t)=\mathbf b^{\mathsf T}\mathbf B(t)^{-1}\mathbf b
$$

where the inverse exists. Determine the full real invertibility domain and the first two derivatives of the real scalar response. Include $\mathbf u=\mathbf0$. For $\mathbf u\ne\mathbf0$, determine exactly when the scalar response has a finite extension at the excluded parameter, and explain what that extension says about solutions of $\mathbf B(t)\mathbf y=\mathbf b$ there.

### D3-009 — Energy carried by coupled tensor components

**Objects and dependencies.** Work in a fixed orthonormal basis of $\mathbb R^3$. All indices $i,j,k,l$ range independently from one to three; every sum is explicit. The fixed real fourth-order tensor has components satisfying

$$
C_{ijkl}=C_{jikl}=C_{ijlk},\qquad C_{ijkl}=C_{klij}.
$$

The independent real scalar is $t$ in an open interval $J$. The real symmetric matrix $\mathbf E(t)$ has twice continuously differentiable components $E_{ij}(t)=E_{ji}(t)$. Define the real scalar energy

$$
W(t)=\frac12\sum_{i=1}^3\sum_{j=1}^3\sum_{k=1}^3\sum_{l=1}^3
C_{ijkl}E_{ij}(t)E_{kl}(t).
$$

Find its first two derivatives, showing which symmetry combines the product-rule terms and how off-diagonal entries are counted. Check the calculation for an anisotropic tensor whose nonzero entries are $C_{1111}=2$, $C_{2222}=3$, $C_{3333}=5$, and the four entries generated by the minor symmetries from each of $C_{1212}=7$, $C_{1313}=11$, $C_{2323}=13$. For that check take

$$
\mathbf E(t)=\begin{bmatrix}t^2&t&0\\t&t&0\\0&0&1\end{bmatrix}.
$$

### D3-010 — An anisotropic energy with turning principal directions

**Objects and dependencies.** The independent dimensionless real angle is $t$. In a fixed orthonormal laboratory basis of $\mathbb R^2$, define

$$
\mathbf R(t)=\begin{bmatrix}\cos t&-\sin t\\\sin t&\cos t\end{bmatrix},\qquad
\mathbf D=\begin{bmatrix}a&0\\0&b\end{bmatrix},\qquad
\mathbf Q(t)=\mathbf R(t)\mathbf D\mathbf R(t)^{\mathsf T},
$$

where the real scalars $a,b>0$ are fixed. The columns of $\mathbf R(t)$ give the actively rotating principal directions in the fixed laboratory basis. A fixed real column vector $\mathbf x=[x_1,x_2]^{\mathsf T}$ defines the real scalar energy $V(t)=\mathbf x^{\mathsf T}\mathbf Q(t)\mathbf x$. Find the matrix derivative and the energy derivative, retaining all product-rule terms. Check the equal-eigenvalue case and verify the energy derivative independently using the components of $\mathbf x$ in the rotating principal directions.

### D3-011 — A direction traced by three competing components

**Objects and dependencies.** The independent real scalar $t$ is dimensionless. In a fixed orthonormal basis of $\mathbb R^3$, the dependent real column vectors are

$$
\mathbf v(t)=\begin{bmatrix}\exp t\\\sin t\\t\end{bmatrix},\qquad
\mathbf n(t)=\frac{\mathbf v(t)}{\|\mathbf v(t)\|},
$$

where the norm is Euclidean. Find the first two derivatives of $\mathbf n(t)$ for every finite real $t$. Verify the two identities obtained by differentiating $\mathbf n(t)^{\mathsf T}\mathbf n(t)=1$ once and twice. Evaluate the vector and both derivatives at zero, and identify the component of the second derivative along $\mathbf n(t)$.

### D3-012 — A finite value left after a point-source subtraction

**Objects and dependencies.** The real scalar wavenumber $k$ is fixed. The independent real radial distance is $r>0$, and the complex scalar function is

$$
q(r;k)=\frac{\exp(-\mathrm{i}kr)-1}{r},\qquad \mathrm{i}^2=-1.
$$

Determine its continuous extension to $r=0$, its derivative for $r>0$, and its right radial derivative at zero. Then let $\mathbf x\in\mathbb R^3$ be an independent real column vector and define the complex scalar field $Q(\mathbf x;k)=q(\|\mathbf x\|;k)$, including the extended value at the origin. Decide whether this field is differentiable at $\mathbf x=\mathbf0$ as a function of three real coordinates. Treat $k=0$ separately and quantify the local expansion used in the argument.

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

### D3-008

1. The only changing matrix term has range contained in the span of $\mathbf u$.
2. Put $\mathbf v=\mathbf A^{-1}\mathbf u$ and compute $\mathbf B(t)\mathbf v$; then test an inverse of the form $\mathbf A^{-1}-c(t)\mathbf v\mathbf v^{\mathsf T}$.
3. The scalar $\mathbf u^{\mathsf T}\mathbf A^{-1}\mathbf b$ controls whether the singular direction is present in the response.

### D3-009

1. Differentiate both factors depending on $t$ before combining any terms.
2. Exchange the index pair $(i,j)$ with $(k,l)$ in one product-rule sum and use the major symmetry.
3. A contraction of symmetric matrices includes each off-diagonal entry twice; the four equivalent tensor shear entries therefore all contribute to the energy.

### D3-010

1. Both rotation factors depend on the angle, while $\mathbf D$ is fixed.
2. The constant matrix $\mathbf J=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ satisfies $\frac{d}{dt}(\mathbf R(t))=\mathbf J\mathbf R(t)$ and $\mathbf J^{\mathsf T}=-\mathbf J$.
3. For the independent check, the principal-direction components are $\mathbf y(t)=\mathbf R(t)^{\mathsf T}\mathbf x$ and their derivative is $-\mathbf J\mathbf y(t)$.

### D3-011

1. Differentiate the squared norm before the norm itself.
2. Introduce the scalar dot products $\mathbf v(t)^{\mathsf T}\frac{d}{dt}(\mathbf v(t))$ and its derivative to organize the second derivative.
3. Differentiating the normalization identity twice produces both a second-derivative term and the squared length of the first derivative.

### D3-012

1. The constant and first few powers in the complex exponential determine different orders after division by $r$.
2. The identity $q(r;k)=-\mathrm{i}k\int_0^1\exp(-\mathrm{i}krs)\,ds$ avoids a quotient at zero.
3. Along a line through the spatial origin, the radial distance is the absolute value of the signed line parameter.

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

**Discussion.** A parameter-dependent square root often marks the boundary between regimes. Its endpoint is part of the function's domain without being part of the finite-derivative domain.

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

**Discussion.** A radial chain rule reduces component work, but it preserves the excluded source point. Differentiation strengthens the singularity and can change whether a later integral exists.

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

**Discussion.** A finite algebraic derivative expression does not repair a discontinuity in the function being differentiated.

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

**Discussion.** The failure of one coordinate chart is not the failure of the underlying geometry. The denominator in implicit differentiation identifies which chart is available.

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

**Discussion.** The sign in an indefinite quadratic form changes the geometry, while normal orientation still depends on the order of a cross product.

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

**Discussion.** A matrix property can justify a domain assumption, rather than merely make the algebra shorter.

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

**Discussion.** The sensitivity of a matrix solve depends on the right-hand side as well as proximity to a singular matrix. Cancellation in one solution does not extend the inverse operator.

### D3-008

**Step 1 — SETUP.** The matrix $\mathbf A$ is invertible and its inverse is symmetric positive definite. Define the fixed real vector and three real scalars

$$
\mathbf v=\mathbf A^{-1}\mathbf u,\qquad
\alpha=\mathbf u^{\mathsf T}\mathbf A^{-1}\mathbf u,\qquad
c=\mathbf u^{\mathsf T}\mathbf A^{-1}\mathbf b,\qquad
\beta=\mathbf b^{\mathsf T}\mathbf A^{-1}\mathbf b.
$$

If $\mathbf u=\mathbf0$, then $\mathbf B(t)=\mathbf A$ for every $t$, $s(t)=\beta$, and both requested derivatives are zero. From now on $\mathbf u\ne\mathbf0$, so $\alpha>0$ and $\mathbf v\ne\mathbf0$.

**Step 2 — CHOICE.** Multiplication by the changing term depends on only one scalar projection. Indeed,

$$
\mathbf B(t)\mathbf v
=\mathbf A\mathbf A^{-1}\mathbf u+t\mathbf u\mathbf u^{\mathsf T}\mathbf A^{-1}\mathbf u
=(1+t\alpha)\mathbf u.
$$

This identifies $t_*=-1/\alpha$ as a singular parameter and suggests correcting the original inverse only along $\mathbf v\mathbf v^{\mathsf T}$.

**Step 3 — ALGEBRA.** For $t\ne t_*$, put

$$
\mathbf M(t)=\mathbf A^{-1}-\frac{t}{1+t\alpha}\mathbf v\mathbf v^{\mathsf T}.
$$

Symmetry gives $\mathbf u^{\mathsf T}\mathbf A^{-1}=\mathbf v^{\mathsf T}$. Direct multiplication, with matrix order retained, gives

$$
\begin{aligned}
\mathbf B(t)\mathbf M(t)
&=\mathbf I+t\mathbf u\mathbf v^{\mathsf T}
-\frac{t}{1+t\alpha}\bigl(\mathbf B(t)\mathbf v\bigr)\mathbf v^{\mathsf T}\\
&=\mathbf I+t\mathbf u\mathbf v^{\mathsf T}-t\mathbf u\mathbf v^{\mathsf T}
=\mathbf I.
\end{aligned}
$$

A square matrix with a right inverse is invertible. Thus the full domain is $\mathbb R\setminus\{t_*\}$, and the displayed $\mathbf M(t)$ is its inverse. At $t=t_*$ the nonzero null vector $\mathbf v$ proves that the exclusion is necessary.

**Step 4 — CALCULUS.** Contracting the inverse with $\mathbf b$ on both sides gives

$$
s(t)=\beta-\frac{tc^2}{1+t\alpha}.
$$

The quotient derivative has numerator $(1+t\alpha)-t\alpha=1$, so

$$
\begin{aligned}
\frac{d}{dt}\left(s(t)\right)&=-\frac{c^2}{(1+t\alpha)^2},\\
\frac{d^2}{dt^2}\left(s(t)\right)
&=-c^2(-2)\alpha(1+t\alpha)^{-3}
=\frac{2\alpha c^2}{(1+t\alpha)^3}.
\end{aligned}
$$

Both expressions are valid on each component of the invertibility domain. The first derivative is nonpositive on both components; the second changes sign across $t_*$ when $c\ne0$.

**Step 5 — DOMAIN.** Rewriting the response isolates its pole:

$$
s(t)=\beta-\frac{c^2}{\alpha}
+\frac{c^2}{\alpha(1+t\alpha)}
=\beta-\frac{c^2}{\alpha}+\frac{c^2}{\alpha^2(t-t_*)}.
$$

Consequently a finite extension exists exactly when $c=0$, in which case $s(t)=\beta$ throughout its original domain. The scalar extension does not restore the matrix inverse. At $t_*$, any solution of $\mathbf B(t_*)\mathbf y=\mathbf b$ must satisfy
$\mathbf v^{\mathsf T}\mathbf b=(\mathbf B(t_*)\mathbf v)^{\mathsf T}\mathbf y=0$, which is precisely $c=0$. When this condition holds, $\mathbf y_0=\mathbf A^{-1}\mathbf b$ is a solution because

$$
\mathbf B(t_*)\mathbf y_0=\mathbf b+t_*\mathbf u c=\mathbf b.
$$

Every solution is $\mathbf y_0+\lambda\mathbf v$ for a real scalar $\lambda$: the kernel equation gives $\mathbf y=-t_*\mathbf v(\mathbf u^{\mathsf T}\mathbf y)$, so its null space is exactly the span of $\mathbf v$. All these solutions have $\mathbf b^{\mathsf T}\mathbf y=\beta$ since $\mathbf b^{\mathsf T}\mathbf v=c=0$. If $c\ne0$, the singular system is inconsistent and the response has a genuine pole.

**Step 6 — CHECK.** Take $\mathbf A=\operatorname{diag}(2,3)$ and $\mathbf u=[1,1]^{\mathsf T}$. Direct two-by-two inversion gives

$$
\mathbf B(t)^{-1}=\frac{1}{6+5t}
\begin{bmatrix}3+t&-t\\-t&2+t\end{bmatrix},\qquad t\ne-6/5.
$$

For $\mathbf b=[1,0]^{\mathsf T}$, this gives $s(t)=(3+t)/(6+5t)$, with derivatives $-9/(6+5t)^2$ and $90/(6+5t)^3$. The general formulas give the same values from $\alpha=5/6$, $c=1/2$, $\beta=1/2$. For $\mathbf b=[2,-3]^{\mathsf T}$, $c=0$ and direct contraction gives the constant $s(t)=5$, including its finite extension at $-6/5$.

**Discussion.** A single scalar projection decides whether a singular matrix direction reaches a measured response. The measured quantity can extend even when the underlying inverse cannot.

### D3-009

**Step 1 — SETUP.** All components are in the stated fixed basis, so no basis derivatives enter. Twice continuous differentiability on $J$ permits two ordinary derivatives of each finite product and finite sum. Define the symmetric stress-like matrix by its real scalar components

$$
S_{ij}(t)=\sum_{k=1}^3\sum_{l=1}^3 C_{ijkl}E_{kl}(t),\qquad 1\le i,j\le3.
$$

The first minor symmetry gives $S_{ji}(t)=S_{ij}(t)$. No positive-definiteness assumption on the fourth-order tensor is needed to differentiate the energy.

**Step 2 — CHOICE.** Both occurrences of $\mathbf E(t)$ vary. Their product-rule terms are first retained separately; the major symmetry can then combine them by exchanging the two index pairs. Minor symmetry has the separate role of organizing the off-diagonal entries.

**Step 3 — CALCULUS.** Differentiation term by term gives

$$
\begin{aligned}
\frac{d}{dt}\left(W(t)\right)
=\frac12\sum_{i=1}^3\sum_{j=1}^3\sum_{k=1}^3\sum_{l=1}^3 C_{ijkl}
\left(
\frac{d}{dt}\left(E_{ij}(t)\right)E_{kl}(t)
+E_{ij}(t)\frac{d}{dt}\left(E_{kl}(t)\right)
\right).
\end{aligned}
$$

In the second sum, rename its four dummy indices by $(i,j,k,l)\mapsto(k,l,i,j)$. Then $C_{klij}=C_{ijkl}$, so the renamed sum equals the first sum. Therefore

$$
\frac{d}{dt}\left(W(t)\right)
=\sum_{i=1}^3\sum_{j=1}^3\sum_{k=1}^3\sum_{l=1}^3
C_{ijkl}\frac{d}{dt}\left(E_{ij}(t)\right)E_{kl}(t)
=\sum_{i=1}^3\sum_{j=1}^3 S_{ij}(t)\frac{d}{dt}\left(E_{ij}(t)\right).
$$

**Step 4 — ALGEBRA.** Symmetry of $\mathbf S(t)$ and $\mathbf E(t)$ makes the final contraction

$$
\begin{aligned}
\frac{d}{dt}\left(W(t)\right)
={}&S_{11}(t)\frac{d}{dt}\left(E_{11}(t)\right)
+S_{22}(t)\frac{d}{dt}\left(E_{22}(t)\right)
+S_{33}(t)\frac{d}{dt}\left(E_{33}(t)\right)\\
&+2S_{12}(t)\frac{d}{dt}\left(E_{12}(t)\right)
+2S_{13}(t)\frac{d}{dt}\left(E_{13}(t)\right)
+2S_{23}(t)\frac{d}{dt}\left(E_{23}(t)\right).
\end{aligned}
$$

Thus a symmetric off-diagonal component cannot be counted only once in a full matrix contraction. The major symmetry, rather than either minor symmetry alone, was what combined the two product-rule sums.

**Step 5 — CALCULUS.** Differentiating the four-index first-derivative expression once more gives

$$
\begin{aligned}
\frac{d^2}{dt^2}\left(W(t)\right)
=\sum_{i=1}^3\sum_{j=1}^3\sum_{k=1}^3\sum_{l=1}^3 C_{ijkl}
\left(
\frac{d^2}{dt^2}\left(E_{ij}(t)\right)E_{kl}(t)
+\frac{d}{dt}\left(E_{ij}(t)\right)\frac{d}{dt}\left(E_{kl}(t)\right)
\right).
\end{aligned}
$$

Equivalently, the major symmetry moves the second derivative onto $E_{kl}(t)$ in the first term. If the calculation starts from the original energy instead, its four second-derivative terms consist of two equal acceleration terms and two equal products of first derivatives; the original factor $1/2$ gives exactly the two terms above.

**Step 6 — CHECK.** For the specified anisotropic tensor, the four entries associated with the $12$ shear are $C_{1212}=C_{1221}=C_{2112}=C_{2121}=7$. Since $E_{21}(t)=E_{12}(t)$, these contribute $(1/2)\,4\,7E_{12}(t)^2=14E_{12}(t)^2$. Expanding every nonzero group gives

$$
\begin{aligned}
W(t)={}&E_{11}(t)^2+\frac32E_{22}(t)^2+\frac52E_{33}(t)^2\\
&+14E_{12}(t)^2+22E_{13}(t)^2+26E_{23}(t)^2.
\end{aligned}
$$

For the stated path this becomes

$$
W(t)=t^4+\frac{31}{2}t^2+\frac52,\qquad
\frac{d}{dt}\left(W(t)\right)=4t^3+31t,\qquad
\frac{d^2}{dt^2}\left(W(t)\right)=12t^2+31.
$$

Independently, the nonzero stress entries are $S_{11}(t)=2t^2$, $S_{22}(t)=3t$, $S_{33}(t)=5$, and $S_{12}(t)=S_{21}(t)=14t$. The expanded first contraction gives $2t^2(2t)+3t+2(14t)=4t^3+31t$. In the second derivative, the product of first derivatives contributes $8t^2+31$ and the term containing the second derivative contributes $4t^2$, agreeing with the polynomial result.

**Step 7 — DOMAIN.** These are identities for every $t\in J$. The tensor is fixed and the sums are finite, so no convergence interchange is required. If the components were only once differentiable, the first formula would remain justified but the stated hypotheses would no longer guarantee the second. A varying tensor or a varying basis would introduce additional derivatives not present in this problem.

**Discussion.** Tensor symmetries reduce work only after the roles of their index pairs have been identified. Off-diagonal multiplicities survive even when a matrix path is symmetric.

### D3-010

**Step 1 — SETUP.** Both $\mathbf R(t)$ and $\mathbf Q(t)$ are real $2\times2$ matrices; $\mathbf Q(t)$ is symmetric positive definite for every real $t$. The vector $\mathbf x$ is held fixed in laboratory coordinates. Define the constant real matrix

$$
\mathbf J=\begin{bmatrix}0&-1\\1&0\end{bmatrix},\qquad
\mathbf J^{\mathsf T}=-\mathbf J.
$$

Component differentiation gives

$$
\frac{d}{dt}\left(\mathbf R(t)\right)
=\begin{bmatrix}-\sin t&-\cos t\\\cos t&-\sin t\end{bmatrix}
=\mathbf J\mathbf R(t),\qquad
\frac{d}{dt}\left(\mathbf R(t)^{\mathsf T}\right)
=-\mathbf R(t)^{\mathsf T}\mathbf J.
$$

**Step 2 — CHOICE.** The tensor is represented in the fixed laboratory basis while its principal directions turn. Consequently both rotation factors must be differentiated, with the transpose factor kept on the right.

**Step 3 — CALCULUS.** The matrix product rule gives

$$
\begin{aligned}
\frac{d}{dt}\left(\mathbf Q(t)\right)
&=\mathbf J\mathbf R(t)\mathbf D\mathbf R(t)^{\mathsf T}
-\mathbf R(t)\mathbf D\mathbf R(t)^{\mathsf T}\mathbf J\\
&=\mathbf J\mathbf Q(t)-\mathbf Q(t)\mathbf J.
\end{aligned}
$$

The order cannot be collapsed by moving $\mathbf D$ through a rotation when $a\ne b$.

**Step 4 — ALGEBRA.** Multiplying the rotation matrices explicitly gives

$$
\mathbf Q(t)=\begin{bmatrix}
a\cos^2t+b\sin^2t&(a-b)\sin t\cos t\\
(a-b)\sin t\cos t&a\sin^2t+b\cos^2t
\end{bmatrix}.
$$

The identities $2\sin t\cos t=\sin(2t)$ and $\cos^2t-\sin^2t=\cos(2t)$ then yield

$$
\frac{d}{dt}\left(\mathbf Q(t)\right)
=(a-b)\begin{bmatrix}-\sin(2t)&\cos(2t)\\\cos(2t)&\sin(2t)\end{bmatrix}.
$$

It is symmetric, as required for the derivative of a symmetric matrix, and has zero trace, consistent with the fixed trace $a+b$.

**Step 5 — CALCULUS.** Since $\mathbf x$ is fixed, the energy derivative is

$$
\begin{aligned}
\frac{d}{dt}\left(V(t)\right)
&=\mathbf x^{\mathsf T}\frac{d}{dt}\left(\mathbf Q(t)\right)\mathbf x\\
&=(a-b)\left(\sin(2t)(x_2^2-x_1^2)+2\cos(2t)x_1x_2\right).
\end{aligned}
$$

The cross term contains a factor two because the two off-diagonal entries both contribute to the scalar contraction.

**Step 6 — CHECK.** The principal-direction coordinates of the same fixed vector are

$$
\mathbf y(t)=\mathbf R(t)^{\mathsf T}\mathbf x
=\begin{bmatrix}x_1\cos t+x_2\sin t\\-x_1\sin t+x_2\cos t\end{bmatrix}.
$$

Differentiating these components gives $\frac{d}{dt}(y_1(t))=y_2(t)$ and $\frac{d}{dt}(y_2(t))=-y_1(t)$. Therefore the independent energy representation $V(t)=ay_1(t)^2+by_2(t)^2$ gives

$$
\frac{d}{dt}\left(V(t)\right)=2(a-b)y_1(t)y_2(t).
$$

Expansion of their product gives
$y_1(t)y_2(t)=\tfrac12\sin(2t)(x_2^2-x_1^2)+\cos(2t)x_1x_2$, reproducing the laboratory-coordinate result. For $\mathbf x=[1,0]^{\mathsf T}$ at $t=\pi/4$, direct differentiation of $a\cos^2t+b\sin^2t$ gives $b-a$, including its sign.

**Step 7 — DOMAIN.** All entries are smooth for every real angle; there is no singular orientation. If $a=b$, then $\mathbf Q(t)=a\mathbf I$ and both derivatives vanish. The same energy derivative is zero for $\mathbf x=\mathbf0$. The chosen active rotation fixes the sign: the vector coordinates in the rotating directions evolve by $-\mathbf J$, while those directions themselves evolve by $\mathbf J$.

**Discussion.** A tensor can have constant eigenvalues and a changing energy for a fixed vector. The changing orientation and the fixed-coordinate convention determine the derivative.

### D3-011

**Step 1 — SETUP.** The first component $\exp t$ is strictly positive, so $\mathbf v(t)\ne\mathbf0$ for every finite real $t$. Its first two derivatives are

$$
\frac{d}{dt}\left(\mathbf v(t)\right)
=\begin{bmatrix}\exp t\\\cos t\\1\end{bmatrix},\qquad
\frac{d^2}{dt^2}\left(\mathbf v(t)\right)
=\begin{bmatrix}\exp t\\-\sin t\\0\end{bmatrix}.
$$

Introduce three real scalar functions to keep the normalization calculation readable:

$$
\begin{aligned}
r(t)&=\sqrt{\exp(2t)+\sin^2t+t^2}>0,\\
p(t)&=\mathbf v(t)^{\mathsf T}\frac{d}{dt}\left(\mathbf v(t)\right)
=\exp(2t)+\sin t\cos t+t,\\
z(t)&=\frac{d}{dt}\left(p(t)\right)
=2\exp(2t)+\cos(2t)+1.
\end{aligned}
$$

**Step 2 — CHOICE.** Differentiating $r(t)^2=\mathbf v(t)^{\mathsf T}\mathbf v(t)$ supplies the normalization derivatives without expanding three separate quotients twice. The two appearances of the vector give

$$
2r(t)\frac{d}{dt}\left(r(t)\right)=2p(t),\qquad
\frac{d}{dt}\left(r(t)\right)=\frac{p(t)}{r(t)}.
$$

One further derivative gives $\frac{d^2}{dt^2}(r(t))=z(t)/r(t)-p(t)^2/r(t)^3$.

**Step 3 — CALCULUS.** The first normalized derivative is

$$
\frac{d}{dt}\left(\mathbf n(t)\right)
=\frac{1}{r(t)}\frac{d}{dt}\left(\mathbf v(t)\right)
-\frac{p(t)}{r(t)^3}\mathbf v(t).
$$

For the second derivative, the derivative of the first term contributes
$r(t)^{-1}\frac{d^2}{dt^2}(\mathbf v(t))-p(t)r(t)^{-3}\frac{d}{dt}(\mathbf v(t))$.
The derivative of the negative second term contributes

$$
-\frac{z(t)}{r(t)^3}\mathbf v(t)
-\frac{p(t)}{r(t)^3}\frac{d}{dt}\left(\mathbf v(t)\right)
+\frac{3p(t)^2}{r(t)^5}\mathbf v(t).
$$

Combining the two equal vector-derivative terms gives the complete result

$$
\begin{aligned}
\frac{d^2}{dt^2}\left(\mathbf n(t)\right)
={}&\frac{1}{r(t)}\frac{d^2}{dt^2}\left(\mathbf v(t)\right)
-\frac{2p(t)}{r(t)^3}\frac{d}{dt}\left(\mathbf v(t)\right)\\
&-\frac{z(t)}{r(t)^3}\mathbf v(t)
+\frac{3p(t)^2}{r(t)^5}\mathbf v(t).
\end{aligned}
$$

Together with the explicit $r(t),p(t),z(t)$ and vector derivatives above, these formulas specify all three components without implicit dependencies.

**Step 4 — ALGEBRA.** The first identity follows directly from contraction:

$$
\mathbf n(t)^{\mathsf T}\frac{d}{dt}\left(\mathbf n(t)\right)
=\frac{p(t)}{r(t)^2}-\frac{p(t)r(t)^2}{r(t)^4}=0.
$$

It also follows by differentiating the unit-length identity once. Differentiating that zero contraction once more gives

$$
\mathbf n(t)^{\mathsf T}\frac{d^2}{dt^2}\left(\mathbf n(t)\right)
=-\left\|\frac{d}{dt}\left(\mathbf n(t)\right)\right\|^2.
$$

To check the second identity directly, the first-derivative formula gives

$$
\left\|\frac{d}{dt}\left(\mathbf n(t)\right)\right\|^2
=\frac{\left\|\frac{d}{dt}(\mathbf v(t))\right\|^2}{r(t)^2}
-\frac{p(t)^2}{r(t)^4}.
$$

On contracting the second derivative with $\mathbf n(t)$, the last three terms combine to

$$
\frac{\mathbf v(t)^{\mathsf T}\frac{d^2}{dt^2}(\mathbf v(t))-z(t)}{r(t)^2}
+\frac{p(t)^2}{r(t)^4}.
$$

The product rule for $p(t)$ says
$z(t)=\|\frac{d}{dt}(\mathbf v(t))\|^2+\mathbf v(t)^{\mathsf T}\frac{d^2}{dt^2}(\mathbf v(t))$,
so this is precisely the negative squared length above. The component of the second derivative along the unit vector is therefore
$-\|\frac{d}{dt}(\mathbf n(t))\|^2\mathbf n(t)$.

**Step 5 — CHECK.** At zero, $r(0)=1$, $p(0)=1$, and $z(0)=4$. Substitution gives

$$
\mathbf n(0)=\begin{bmatrix}1\\0\\0\end{bmatrix},\qquad
\left.\frac{d}{dt}\left(\mathbf n(t)\right)\right|_{t=0}
=\begin{bmatrix}0\\1\\1\end{bmatrix},\qquad
\left.\frac{d^2}{dt^2}\left(\mathbf n(t)\right)\right|_{t=0}
=\begin{bmatrix}-2\\-2\\-2\end{bmatrix}.
$$

The two identities give zero and $-2$ respectively, with the latter equal to the negative squared length of $[0,1,1]^{\mathsf T}$. Independently, a Taylor expansion gives $r(t)=1+t+3t^2/2+O(t^3)$ and
$\mathbf n(t)=[1-t^2,\ t-t^2,\ t-t^2]^{\mathsf T}+O(t^3)$ componentwise, confirming both derivative vectors.

**Step 6 — DOMAIN.** The formulas apply for all finite real $t$ because the normalizing denominator never vanishes. They describe derivatives with respect to the given parameter, not arc length. The inward component of the second derivative is forced by the unit-sphere constraint; its remaining component depends on how the direction is traversed.

**Discussion.** Normalization couples all components through the changing norm. A unit vector can have a nonzero second derivative even though its length remains constant.

### D3-012

**Step 1 — SETUP.** The radial output is complex, with differentiation performed in the real scalar $r$. For fixed real $k$, integration of the elementary exponential on the unit interval gives the identity

$$
q(r;k)=-\mathrm{i}k\int_0^1\exp(-\mathrm{i}krs)\,ds,
\qquad r>0.
$$

It is valid also when $k=0$, because both sides then vanish. The finite-interval representation has no singular denominator.

**Step 2 — CHOICE.** The integral representation determines the limit and right derivative at zero directly. A Taylor expansion then identifies the first spatial term introduced by replacing $r$ with a norm. These operations ask different differentiability questions.

**Step 3 — CALCULUS.** Continuity of the exponential on the compact $s$ interval gives

$$
q(0;k)=-\mathrm{i}k.
$$

The quotient rule for positive $r$ gives

$$
\frac{\partial}{\partial r}\left(q(r;k)\right)
=\frac{-\mathrm{i}kr\exp(-\mathrm{i}kr)-\exp(-\mathrm{i}kr)+1}{r^2}
=\frac{1-(1+\mathrm{i}kr)\exp(-\mathrm{i}kr)}{r^2}.
$$

Differentiating the finite-interval representation instead gives

$$
\frac{\partial}{\partial r}\left(q(r;k)\right)
=-k^2\int_0^1s\exp(-\mathrm{i}krs)\,ds.
$$

The integrand and its derivative are continuous on a compact rectangle around any finite real $r$. Differentiation under this finite integral is justified, including for its extension to $r=0$. Hence the right radial derivative there is $-k^2\int_0^1s\,ds=-k^2/2$.

**Step 4 — TRICK AND ALGEBRA.** Taylor's formula for the complex exponential along a real argument gives, for $r\ge0$,

$$
q(r;k)=-\mathrm{i}k-\frac{k^2}{2}r+\frac{\mathrm{i}k^3}{6}r^2+\mathcal R(r;k),
\qquad |\mathcal R(r;k)|\le\frac{|k|^4r^3}{24}.
$$

The bound follows from the integral remainder for the cubic exponential polynomial: its fourth derivative along the real argument has magnitude one. Division by $r>0$ leaves the displayed cubic bound, and continuity includes $r=0$. In particular,

$$
Q(\mathbf x;k)-Q(\mathbf0;k)
=-\frac{k^2}{2}\|\mathbf x\|
+\frac{\mathrm{i}k^3}{6}\|\mathbf x\|^2
+\mathcal R(\|\mathbf x\|;k).
$$

**Step 5 — DOMAIN.** Suppose $k\ne0$. Along the signed first coordinate $h$, the distance is $|h|$, so

$$
\frac{Q([h,0,0]^{\mathsf T};k)-Q(\mathbf0;k)}{h}
=-\frac{k^2}{2}\frac{|h|}{h}+O(|h|),\qquad h\to0.
$$

The right limit is $-k^2/2$ and the left limit is $k^2/2$. The first coordinate partial derivative therefore fails to exist; in particular there is no real-linear total derivative from $\mathbb R^3$ to $\mathbb C$ at the origin. For $\mathbf x\ne\mathbf0$, the ordinary radial chain rule does apply:

$$
\nabla_{\mathbf x}Q(\mathbf x;k)
=\left.\frac{\partial}{\partial r}\left(q(r;k)\right)\right|_{r=\|\mathbf x\|}
\frac{\mathbf x}{\|\mathbf x\|}.
$$

Its limits along opposite spatial rays point in opposite directions, consistent with the failed partial derivative.

**Step 6 — CHECK.** For $k=0$, both $q(r;0)$ and $Q(\mathbf x;0)$ are identically zero after extension, so all their derivatives exist and vanish. For $k\ne0$, the real part supplies an independent check:

$$
\operatorname{Re}q(r;k)=\frac{\cos(kr)-1}{r}
=-\frac{2\sin^2(kr/2)}{r}.
$$

Its leading term is $-k^2r/2$, which becomes a nonzero multiple of $-\|\mathbf x\|$ in space. By contrast, the imaginary part is $-\sin(kr)/r=-k+k^3r^2/6+O(r^4)$; its leading correction is quadratic in the spatial coordinates. The real cusp is enough to obstruct differentiability of the complete complex field.

**Discussion.** Removing an infinite kernel value can produce a continuous field with a finite radial derivative while leaving a spatial cusp. A radial derivative at a boundary does not supply a linear derivative in every spatial direction.

## Application references

These are original review problems. The waveguide model is motivated by
[MIT 6.013, Lecture 16](https://www.ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/d9425aa2b1acd0c1fc121965ad7eafec_MIT6_013S09_lec16.pdf).
Singular Green kernels and discretized field systems occur in the integral-equation
work discussed by [Tihon and Craeye, All-analytical evaluation of the singular integrals involved in the Method of Moments](https://arxiv.org/abs/1911.12660).
The small scalar and matrix models isolate calculus issues; their solutions do
not constitute full waveguide or antenna designs.
