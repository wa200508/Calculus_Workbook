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

### D3-013 — Two fixed foci and a distance response

**Objects and dependencies.** Work in a fixed orthonormal basis of $\mathbb R^3$ with first basis vector $\mathbf e_1=[1,0,0]^{\mathsf T}$. The real length $a>0$ is fixed and $\mathbf x=[x_1,x_2,x_3]^{\mathsf T}$ is an independent real spatial vector. Define the real scalar

$$
f(\mathbf x)=\|\mathbf x-a\mathbf e_1\|+\|\mathbf x+a\mathbf e_1\|,
$$

using the Euclidean norm. Find its gradient and Hessian away from the two foci, determine all stationary points there, and identify its global minimum on the whole space. Examine differentiability at both foci. Determine when the Hessian is positive definite and describe its axial and transverse action on the line through the foci.

### D3-014 — A scalar response unchanged by rescaling

**Objects and dependencies.** The positive integer $n$ is fixed. The dimensionless matrix $\mathbf A\in\mathbb R^{n\times n}$ is fixed and symmetric, and $\mathbf x\in\mathbb R^n\setminus\{\mathbf0\}$ is an independent dimensionless real column vector. Define the real scalar

$$
R(\mathbf x)=\frac{\mathbf x^{\mathsf T}\mathbf A\mathbf x}{\mathbf x^{\mathsf T}\mathbf x}.
$$

Find its gradient and full Hessian. Determine every stationary direction, including repeated eigenvalues, and classify them when the input is restricted to the unit sphere. Give the second variation in tangent directions at a stationary unit vector. Check the results for

$$
\mathbf A=\begin{bmatrix}2&1&0\\1&2&0\\0&0&5\end{bmatrix},
$$

including a nonstationary input and all three eigendirections.

### D3-015 — A changing tensor measured in fixed coordinates

**Objects and dependencies.** Fix orthonormal bases in two copies of $\mathbb R^3$, called reference and spatial space. On an open interval $I$, the independent dimensionless real parameter is $t$. The real matrix $\mathbf F(t)$ maps reference components to spatial components, has continuously differentiable entries, and satisfies $\det(\mathbf F(t))>0$. The real symmetric positive-definite matrix $\mathbf C$ is fixed in spatial coordinates. Define the reference-coordinate matrix and real scalar energy

$$
\begin{aligned}
\mathbf Q(t)&=\det(\mathbf F(t))\mathbf F(t)^{-1}\mathbf C\mathbf F(t)^{-\mathsf T},\\
E(t)&=\mathbf x^{\mathsf T}\mathbf Q(t)\mathbf x,
\end{aligned}
$$

where $\mathbf F(t)^{-\mathsf T}=(\mathbf F(t)^{-1})^{\mathsf T}$ and the dimensionless reference vector $\mathbf x\in\mathbb R^3$ is fixed. Find both derivatives, retaining multiplication order and the determinant contribution. For the path

$$
\mathbf F(t)=\begin{bmatrix}\exp t&t&0\\0&1&t\\0&0&1\end{bmatrix},\qquad
\mathbf C=\mathbf I,
$$

give every component of $\mathbf Q(t)$ and its derivative, and verify the energy calculation independently.

### D3-016 — A positive matrix branch with coupled entries

**Objects and dependencies.** Work in a fixed orthonormal basis of $\mathbb R^n$, where $n$ is a positive integer. The real symmetric positive-definite matrix $\mathbf A_0$ and real symmetric matrix $\mathbf H$ are fixed. For an independent dimensionless real scalar $t$ such that $\mathbf A(t)=\mathbf A_0+t\mathbf H$ remains positive definite, define $\mathbf S(t)$ to be its principal square root: the unique real symmetric positive-definite matrix satisfying $\mathbf S(t)^2=\mathbf A(t)$.

Establish local differentiability of this branch and determine its first two derivatives by equations with unique symmetric solutions. Resolve those equations in an orthonormal eigenbasis at a fixed parameter value without assuming that $\mathbf A(t)$ commutes with $\mathbf H$. For

$$
\mathbf A_0=\begin{bmatrix}1&0\\0&4\end{bmatrix},\qquad
\mathbf H=\begin{bmatrix}1&1\\1&2\end{bmatrix},
$$

find the full real positive-definite parameter domain and evaluate both square-root derivatives at zero. Test the scalar-inspired formula $\frac12\mathbf S(t)^{-1}\mathbf H$ for the first derivative.

### D3-017 — A radial map with changing local scales

**Objects and dependencies.** The independent dimensionless real vector is $\mathbf x\in\mathbb R^3$, in a fixed orthonormal basis. With the Euclidean norm, define the real vector-valued map

$$
\mathbf F(\mathbf x)=(1+\|\mathbf x\|^2)\mathbf x.
$$

Find its Jacobian, determinant, and component second derivatives. Prove that it has a unique inverse $\mathbf G:\mathbb R^3\to\mathbb R^3$ on the whole space, and determine the Jacobian of that inverse, including its radial and transverse eigenvalues and its value at the origin. An implicit scalar description of the inverse radius is sufficient. For fixed increments $\mathbf h,\mathbf k\in\mathbb R^3$, obtain a bilinear formula for $\mathrm D^2\mathbf G(\mathbf y)(\mathbf h,\mathbf k)$ and check the first two inverse derivatives at a nonzero input.

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

### D3-013

1. Differentiate each nonzero displacement norm first; its unit direction also depends on the observation point.
2. The quadratic form of a single norm's Hessian vanishes only along that displacement direction. Compare the two directions before combining their null spaces.
3. The triangle inequality bounds the sum below by the distance between the foci; examine equality and one-sided axial slopes at the foci.

### D3-014

1. Keep the quadratic numerator and squared-norm denominator separate through the first quotient derivative.
2. For the Hessian, differentiate the scalar quotient appearing inside the gradient as well as the other scalar and vector factors.
3. At a stationary unit vector, resolve a tangent increment into eigenspaces of the symmetric matrix; repeated eigenvalues leave flat directions.

### D3-015

1. Differentiate the inverse identity and its transpose before applying the product rule to the three changing factors in $\mathbf Q(t)$.
2. The reference-coordinate matrix $\mathbf L(t)=\mathbf F(t)^{-1}\frac{d}{dt}(\mathbf F(t))$ organizes the ordered terms; its trace is the logarithmic derivative of the determinant.
3. Independently write the energy using the spatial vector $\mathbf F(t)^{-\mathsf T}\mathbf x$ and expand its squared length in the concrete example.

### D3-016

1. Differentiate $\mathbf S(t)\mathbf S(t)=\mathbf A(t)$ without moving either derivative past the other factor.
2. In an eigenbasis of a positive square root, the linear map $\mathbf K\mapsto\mathbf S\mathbf K+\mathbf K\mathbf S$ multiplies entry $(i,j)$ by a positive sum of two eigenvalues.
3. Differentiate the first matrix equation again. The two products of first derivatives remain even though the affine matrix path has zero second derivative.

### D3-017

1. Separate the derivative parallel to $\mathbf x$ from derivatives orthogonal to it.
2. The map preserves direction, while its output radius is $r+r^3$ for an input radius $r\ge0$; local invertibility alone does not prove a global inverse.
3. Differentiate the identity $\mathbf F(\mathbf G(\mathbf y))=\mathbf y$ once and twice, keeping the two first-order inverse increments inside the second derivative of $\mathbf F$.

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

### D3-013

**Step 1 — SETUP.** The value $f(\mathbf x)$ exists and is continuous on all of $\mathbb R^3$. Away from the two foci, define the nonzero displacement vectors, positive distances, and unit directions

$$
\begin{aligned}
\mathbf d_+(\mathbf x)&=\mathbf x-a\mathbf e_1,&
\mathbf d_-(\mathbf x)&=\mathbf x+a\mathbf e_1,\\
r_+(\mathbf x)&=\|\mathbf d_+(\mathbf x)\|,&
r_-(\mathbf x)&=\|\mathbf d_-(\mathbf x)\|,\\
\mathbf u_+(\mathbf x)&=\mathbf d_+(\mathbf x)/r_+(\mathbf x),&
\mathbf u_-(\mathbf x)&=\mathbf d_-(\mathbf x)/r_-(\mathbf x).
\end{aligned}
$$

The gradient is a real $3\times1$ vector and the Hessian $\mathbf H_f(\mathbf x)$ is a real symmetric $3\times3$ matrix.

**Step 2 — CHOICE.** Each norm is smooth where its displacement is nonzero. The Hessian of one distance penalizes changes transverse to its own displacement; whether the sum is strictly positive depends on whether the two displacements have a common direction.

**Step 3 — CALCULUS.** For either sign, component differentiation in the fixed basis gives

$$
\frac{\partial}{\partial x_j}\left(r_\pm(\mathbf x)\right)
=\frac{d_{\pm,j}(\mathbf x)}{r_\pm(\mathbf x)},\qquad
\frac{\partial}{\partial x_j}\left(u_{\pm,i}(\mathbf x)\right)
=\frac{\delta_{ij}}{r_\pm(\mathbf x)}
-\frac{d_{\pm,i}(\mathbf x)d_{\pm,j}(\mathbf x)}{r_\pm(\mathbf x)^3},
$$

where $1\le i,j\le3$ and $\delta_{ij}$ is one when $i=j$ and zero otherwise. Hence

$$
\begin{aligned}
\nabla_{\mathbf x}f(\mathbf x)&=\mathbf u_+(\mathbf x)+\mathbf u_-(\mathbf x),\\
\mathbf H_f(\mathbf x)
&=\frac{\mathbf I-\mathbf u_+(\mathbf x)\mathbf u_+(\mathbf x)^{\mathsf T}}{r_+(\mathbf x)}
+\frac{\mathbf I-\mathbf u_-(\mathbf x)\mathbf u_-(\mathbf x)^{\mathsf T}}{r_-(\mathbf x)}.
\end{aligned}
$$

**Step 4 — ALGEBRA.** For a fixed real increment $\mathbf h$, the Hessian quadratic form is

$$
\begin{aligned}
\mathbf h^{\mathsf T}\mathbf H_f(\mathbf x)\mathbf h
={}&\frac{\|\mathbf h\|^2-(\mathbf u_+(\mathbf x)^{\mathsf T}\mathbf h)^2}{r_+(\mathbf x)}\\
&+\frac{\|\mathbf h\|^2-(\mathbf u_-(\mathbf x)^{\mathsf T}\mathbf h)^2}{r_-(\mathbf x)}\ge0.
\end{aligned}
$$

Each term vanishes precisely when $\mathbf h$ is parallel to its displacement. Off the focal axis the two displacements are not parallel, so their only common null increment is $\mathbf0$: the Hessian is positive definite there. On the axis, $\mathbf x=s\mathbf e_1$ with $s\ne\pm a$, it becomes

$$
\mathbf H_f(s\mathbf e_1)
=\left(\frac1{|s-a|}+\frac1{|s+a|}\right)
(\mathbf I-\mathbf e_1\mathbf e_1^{\mathsf T}).
$$

Thus its axial eigenvalue is zero, and its two transverse eigenvalues are the displayed positive coefficient. This holds both between and outside the foci.

**Step 5 — DOMAIN AND STATIONARITY.** The gradient vanishes exactly when $\mathbf u_+(\mathbf x)=-\mathbf u_-(\mathbf x)$. The displacements must then be opposite parallel vectors. Since $\mathbf d_-(\mathbf x)-\mathbf d_+(\mathbf x)=2a\mathbf e_1$, the point lies on the focal axis, and their opposite signs require $-a<s<a$. These are all the differentiable stationary points. On the remaining axis the gradient is $2\mathbf e_1$ for $s>a$ and $-2\mathbf e_1$ for $s<-a$.

The triangle inequality applied to $\mathbf d_-(\mathbf x)-\mathbf d_+(\mathbf x)$ gives $f(\mathbf x)\ge2a$. Equality holds precisely on the closed line segment $\{s\mathbf e_1:-a\le s\le a\}$. This closed segment is the complete set of global minimizers, including the two points where the derivative formulas do not apply.

At the positive focus, for $|h|<2a$,

$$
f((a+h)\mathbf e_1)=|h|+|2a+h|=2a+h+|h|.
$$

Its left and right axial slopes are zero and two. At the negative focus the corresponding expression is $2a-h+|h|$, whose slopes are minus two and zero. Thus neither focus is differentiable, even though both minimize the continuous function.

**Step 6 — CHECK.** At the midpoint, the Hessian is $(2/a)(\mathbf I-\mathbf e_1\mathbf e_1^{\mathsf T})$, consistent with a constant value along the minimizing segment. At $\mathbf x=[0,b,0]^{\mathsf T}$ with $b\ne0$, write $r=\sqrt{a^2+b^2}$. The formulas give

$$
\nabla_{\mathbf x}f(\mathbf x)=\begin{bmatrix}0\\2b/r\\0\end{bmatrix},\qquad
\mathbf H_f(\mathbf x)=\operatorname{diag}\left(\frac{2b^2}{r^3},\frac{2a^2}{r^3},\frac2r\right).
$$

Independently, restricting to $\mathbf x=[0,b,0]^{\mathsf T}$ gives $f=2\sqrt{a^2+b^2}$, with first and second derivatives $2b/r$ and $2a^2/r^3$. Restricting instead to $[0,b,h]^{\mathsf T}$ gives $2\sqrt{a^2+b^2+h^2}$, whose second derivative at zero is $2/r$. These agree with the indicated transverse entries, all strictly positive off the axis.

**Discussion.** A flat family of minimizers and a nonsmooth minimum can occur in the same convex distance problem. The direction of each displacement determines which second variations vanish.

### D3-014

**Step 1 — SETUP.** Put $s(\mathbf x)=\mathbf x^{\mathsf T}\mathbf x>0$ and $q(\mathbf x)=\mathbf x^{\mathsf T}\mathbf A\mathbf x$, so $R(\mathbf x)=q(\mathbf x)/s(\mathbf x)$. Symmetry gives $\nabla_{\mathbf x}q(\mathbf x)=2\mathbf A\mathbf x$ and $\nabla_{\mathbf x}s(\mathbf x)=2\mathbf x$. All derivatives below are in the fixed Euclidean basis on the open punctured space.

**Step 2 — CHOICE.** The numerator and denominator both change with the input. Retaining the scalar quotient inside the gradient makes its stationary equation transparent, but that quotient must itself be differentiated when forming the Hessian.

**Step 3 — CALCULUS.** The quotient rule gives

$$
\nabla_{\mathbf x}R(\mathbf x)
=\frac{2}{s(\mathbf x)}\bigl(\mathbf A\mathbf x-R(\mathbf x)\mathbf x\bigr).
$$

For the full Hessian, its $(i,j)$ entry, with $1\le i,j\le n$, follows by differentiating $2(\mathbf A\mathbf x)_i/s(\mathbf x)-2q(\mathbf x)x_i/s(\mathbf x)^2$:

$$
\begin{aligned}
\frac{\partial}{\partial x_j}\left(\frac{\partial}{\partial x_i}(R(\mathbf x))\right)
={}&\frac{2A_{ij}}{s(\mathbf x)}-\frac{2q(\mathbf x)\delta_{ij}}{s(\mathbf x)^2}\\
&-\frac{4(\mathbf A\mathbf x)_i x_j+4x_i(\mathbf A\mathbf x)_j}{s(\mathbf x)^2}
+\frac{8q(\mathbf x)x_ix_j}{s(\mathbf x)^3}.
\end{aligned}
$$

Here $\delta_{ij}$ is the identity-matrix entry. Thus, with the real vector $\mathbf v(\mathbf x)=\mathbf A\mathbf x-R(\mathbf x)\mathbf x$, the same symmetric Hessian is

$$
\mathbf H_R(\mathbf x)
=\frac{2}{s(\mathbf x)}\bigl(\mathbf A-R(\mathbf x)\mathbf I\bigr)
-\frac{4}{s(\mathbf x)^2}
\bigl(\mathbf x\mathbf v(\mathbf x)^{\mathsf T}+\mathbf v(\mathbf x)\mathbf x^{\mathsf T}\bigr).
$$

The two outer products contain the terms arising from both varying scalar factors; deleting either would destroy the full Hessian.

**Step 4 — ALGEBRA AND STATIONARITY.** The gradient vanishes exactly when $\mathbf A\mathbf x=R(\mathbf x)\mathbf x$. By the spectral theorem this means that $\mathbf x$ is any nonzero vector in one eigenspace of $\mathbf A$. In particular, a repeated eigenvalue permits every nonzero combination within its eigenspace, rather than only the chosen basis eigenvectors. At such a point with eigenvalue $\lambda$,

$$
\mathbf H_R(\mathbf x)=\frac{2}{\|\mathbf x\|^2}(\mathbf A-\lambda\mathbf I).
$$

The radial direction has zero second variation, consistent with $R(c\mathbf x)=R(\mathbf x)$ for every nonzero real $c$.

**Step 5 — DOMAIN AND SPHERE CLASSIFICATION.** Let $\mathbf u$ be a stationary unit vector with eigenvalue $\lambda$. A tangent increment $\mathbf h$ satisfies $\mathbf u^{\mathsf T}\mathbf h=0$. The second derivative of the restriction to the sphere at that stationary point is

$$
2\mathbf h^{\mathsf T}(\mathbf A-\lambda\mathbf I)\mathbf h.
$$

For example, the spherical path $(\mathbf u+\epsilon\mathbf h)/\|\mathbf u+\epsilon\mathbf h\|$ has first derivative $\mathbf h$ at zero; its second-derivative contribution involving the ambient gradient vanishes because that gradient is zero.

Choose an orthonormal eigenbasis $\mathbf w_1,\ldots,\mathbf w_n$ with eigenvalues $\lambda_1,\ldots,\lambda_n$. Writing $\mathbf h=\sum_{j=1}^n h_j\mathbf w_j$ makes this second variation

$$
2\sum_{j=1}^n(\lambda_j-\lambda)h_j^2.
$$

The smallest eigenvalue gives all global minima, and the largest gives all global maxima: for any unit $\mathbf z=\sum_{j=1}^n z_j\mathbf w_j$, the value $R(\mathbf z)=\sum_{j=1}^n\lambda_j z_j^2$ is a weighted average of the eigenvalues. An intermediate eigenvalue is a saddle, since directions into lower and higher eigenspaces give opposite signs. A repeated extremal eigenvalue leaves flat tangent directions within its eigenspace and a sphere of minimizers or maximizers. If the extremal eigenvalue is simple and $n>1$, the other tangent eigenvalues have a strict sign, so each of its two unit eigenvectors is a strict local extremum on the sphere. If every eigenvalue is equal, the response is constant and the Hessian vanishes, including when $n=1$.

**Step 6 — CHECK.** In the specified three-dimensional example, the unit eigenvectors and eigenvalues are

$$
\frac{1}{\sqrt2}\begin{bmatrix}1\\-1\\0\end{bmatrix}\ (\lambda=1),\qquad
\frac{1}{\sqrt2}\begin{bmatrix}1\\1\\0\end{bmatrix}\ (\lambda=3),\qquad
\begin{bmatrix}0\\0\\1\end{bmatrix}\ (\lambda=5).
$$

The tangent Hessian eigenvalues are respectively $(4,8)$, $(-4,4)$, and $(-8,-4)$, giving a minimum, a saddle, and a maximum. At the nonstationary input $\mathbf x=[1,0,1]^{\mathsf T}$, direct evaluation gives $s(\mathbf x)=2$, $q(\mathbf x)=7$, and

$$
\nabla_{\mathbf x}R(\mathbf x)=\begin{bmatrix}-3/2\\1\\3/2\end{bmatrix},\qquad
\mathbf H_R(\mathbf x)=\begin{bmatrix}3/2&0&0\\0&-3/2&-1\\0&-1&-3/2\end{bmatrix}.
$$

As an independent scaling check, differentiating $\nabla R(c\mathbf x)=c^{-1}\nabla R(\mathbf x)$ at $c=1$ requires $\mathbf H_R(\mathbf x)\mathbf x=-\nabla R(\mathbf x)$, which these explicit values satisfy. For a repeated-eigenvalue check, $\mathbf A=\operatorname{diag}(1,1,4)$ makes every unit vector in the plane spanned by the first two basis vectors a minimizer, with zero tangential curvature within that circle and curvature six toward the third direction.

**Discussion.** Rescaling invariance removes one ambient direction of change, while repeated eigenvalues create additional flat directions. Classification on the sphere separates those effects from increases and decreases between different eigenspaces.

### D3-015

**Step 1 — SETUP.** Define the positive scalar, inverse matrix, and reference-coordinate rate matrix

$$
m(t)=\det(\mathbf F(t)),\qquad
\mathbf K(t)=\mathbf F(t)^{-1},\qquad
\mathbf L(t)=\mathbf K(t)\frac{d}{dt}\left(\mathbf F(t)\right).
$$

The two bases stay fixed during differentiation. The inverse maps spatial components back to reference components, so $\mathbf Q(t)=m(t)\mathbf K(t)\mathbf C\mathbf K(t)^{\mathsf T}$ has both indices in reference coordinates. It is symmetric positive definite: for any nonzero reference vector $\mathbf z$, its energy is $m(t)(\mathbf K(t)^{\mathsf T}\mathbf z)^{\mathsf T}\mathbf C(\mathbf K(t)^{\mathsf T}\mathbf z)>0$.

**Step 2 — CHOICE.** Volume change and changes of both inverse factors contribute separately. The derivative of an inverse follows from the defining identity, while the determinant derivative follows by factoring out the current invertible matrix. Neither calculation requires commuting two matrix factors.

**Step 3 — CALCULUS.** Differentiating $\mathbf F(t)\mathbf K(t)=\mathbf I$ gives

$$
\frac{d}{dt}\left(\mathbf K(t)\right)
=-\mathbf K(t)\frac{d}{dt}\left(\mathbf F(t)\right)\mathbf K(t)
=-\mathbf L(t)\mathbf K(t).
$$

Transposing the entire identity gives $\frac{d}{dt}(\mathbf K(t)^{\mathsf T})=-\mathbf K(t)^{\mathsf T}\mathbf L(t)^{\mathsf T}$. For a real increment $h\to0$, continuous differentiability gives

$$
\mathbf F(t+h)=\mathbf F(t)\bigl(\mathbf I+h\mathbf L(t)+o(h)\bigr).
$$

The first-order determinant expansion $\det(\mathbf I+h\mathbf L)=1+h\operatorname{tr}(\mathbf L)+O(h^2)$ therefore yields

$$
\frac{d}{dt}\left(m(t)\right)=m(t)\operatorname{tr}(\mathbf L(t)).
$$

**Step 4 — ALGEBRA.** Applying the product rule to the determinant and the two inverse factors gives

$$
\begin{aligned}
\frac{d}{dt}\left(\mathbf Q(t)\right)
={}&m(t)\operatorname{tr}(\mathbf L(t))\mathbf K(t)\mathbf C\mathbf K(t)^{\mathsf T}\\
&-m(t)\mathbf L(t)\mathbf K(t)\mathbf C\mathbf K(t)^{\mathsf T}\\
&-m(t)\mathbf K(t)\mathbf C\mathbf K(t)^{\mathsf T}\mathbf L(t)^{\mathsf T}\\
={}&\operatorname{tr}(\mathbf L(t))\mathbf Q(t)
-\mathbf L(t)\mathbf Q(t)-\mathbf Q(t)\mathbf L(t)^{\mathsf T}.
\end{aligned}
$$

The last two terms are transposes of one another, preserving symmetry without requiring $\mathbf L(t)$ to be symmetric. Since $\mathbf x$ is fixed,

$$
\begin{aligned}
\frac{d}{dt}\left(E(t)\right)
&=\mathbf x^{\mathsf T}\frac{d}{dt}\left(\mathbf Q(t)\right)\mathbf x\\
&=\operatorname{tr}(\mathbf L(t))E(t)
-2\mathbf x^{\mathsf T}\mathbf L(t)\mathbf Q(t)\mathbf x.
\end{aligned}
$$

Here the two ordered scalar contractions are equal by transposing the complete scalar; this does not imply equality of their matrix factors.

**Step 5 — CALCULUS: the specified path.** For the upper-triangular example, direct multiplication verifies

$$
\begin{aligned}
m(t)&=\exp t,\\
\mathbf K(t)&=\begin{bmatrix}\exp(-t)&-t\exp(-t)&t^2\exp(-t)\\0&1&-t\\0&0&1\end{bmatrix},\\
\mathbf L(t)&=\begin{bmatrix}1&\exp(-t)&-t\exp(-t)\\0&0&1\\0&0&0\end{bmatrix}.
\end{aligned}
$$

In particular, $\operatorname{tr}(\mathbf L(t))=1$, consistent with the determinant derivative. Multiplying $m(t)\mathbf K(t)\mathbf K(t)^{\mathsf T}$ gives every component:

$$
\mathbf Q(t)=\begin{bmatrix}
\exp(-t)(1+t^2+t^4)&-t-t^3&t^2\\
-t-t^3&\exp(t)(1+t^2)&-t\exp t\\
t^2&-t\exp t&\exp t
\end{bmatrix}.
$$

Direct differentiation of those components yields

$$
\frac{d}{dt}\left(\mathbf Q(t)\right)=\begin{bmatrix}
\exp(-t)(-1+2t-t^2+4t^3-t^4)&-1-3t^2&2t\\
-1-3t^2&\exp(t)(1+2t+t^2)&-(1+t)\exp t\\
2t&-(1+t)\exp t&\exp t
\end{bmatrix}.
$$

At zero this is $\begin{bmatrix}-1&-1&0\\-1&1&-1\\0&-1&1\end{bmatrix}$, also obtained from $\mathbf Q(0)=\mathbf I$ and $\mathbf I-\mathbf L(0)-\mathbf L(0)^{\mathsf T}$.

**Step 6 — CHECK.** Put $\mathbf y(t)=\mathbf K(t)^{\mathsf T}\mathbf x$, a spatial vector. For the example,

$$
\mathbf y(t)=\begin{bmatrix}
\exp(-t)x_1\\
x_2-t\exp(-t)x_1\\
x_3-tx_2+t^2\exp(-t)x_1
\end{bmatrix},\qquad E(t)=\exp(t)\|\mathbf y(t)\|^2.
$$

Expanding these three squares independently gives

$$
\begin{aligned}
E(t)={}&\exp(-t)(1+t^2+t^4)x_1^2
+\exp(t)(1+t^2)x_2^2+\exp(t)x_3^2\\
&-2(t+t^3)x_1x_2+2t^2x_1x_3-2t\exp(t)x_2x_3.
\end{aligned}
$$

Its derivative consequently has diagonal terms $\frac{d}{dt}(Q_{ii}(t))x_i^2$ for $1\le i\le3$ and cross terms
$-2(1+3t^2)x_1x_2+4tx_1x_3-2(1+t)\exp(t)x_2x_3$, exactly matching the full tensor derivative. At zero the energy slope is $-x_1^2+x_2^2+x_3^2-2x_1x_2-2x_2x_3$. A separate determinant check gives

$$
\det(\mathbf Q(t))=m(t)^3\det(\mathbf K(t))^2\det(\mathbf C)
=m(t)\det(\mathbf C),
$$

which equals $\exp t$ in the example.

**Step 7 — DOMAIN.** The general formula is valid throughout $I$ because positive determinant guarantees invertibility and the positive volume factor. Only first derivatives of $\mathbf F(t)$ are needed. The example has positive determinant for every finite real $t$, so no finite parameter is excluded. All coordinates and bases have been specified; there is no unrecorded derivative of a basis or of the fixed spatial tensor.

**Discussion.** A volume factor changes the same energy as two ordered inverse-coordinate factors. Differentiating the congruence requires both sides even when the resulting matrix is symmetric.

### D3-016

**Step 1 — SETUP.** At every admissible parameter, the spectral theorem supplies a positive square root: if $\mathbf A(t)=\mathbf U\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\mathbf U^{\mathsf T}$ with all $\lambda_i>0$, then its principal root is $\mathbf U\operatorname{diag}(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_n})\mathbf U^{\mathsf T}$. We first justify differentiating this branch without assuming differentiable choices of eigenvectors.

**Step 2 — CHOICE AND LOCAL EXISTENCE.** On the finite-dimensional space of real symmetric matrices, consider the smooth equation $\boldsymbol\Phi(\mathbf S,\mathbf A)=\mathbf S^2-\mathbf A=\mathbf0$. Its derivative in a symmetric increment $\mathbf K$ of the first input is

$$
\mathrm D_{\mathbf S}\boldsymbol\Phi(\mathbf S,\mathbf A)(\mathbf K)
=\mathbf S\mathbf K+\mathbf K\mathbf S.
$$

At a positive root, choose an orthonormal eigenbasis of $\mathbf S$ with positive eigenvalues $\sigma_1,\ldots,\sigma_n$. In this basis the $(i,j)$ component of that linear map is $(\sigma_i+\sigma_j)K_{ij}$. Every multiplier is strictly positive, including for repeated eigenvalues. Division by these multipliers defines a unique symmetric solution for every symmetric right-hand side, so the derivative map is invertible.

The implicit function theorem therefore supplies a smooth square-root branch near each positive-definite input. Its values remain positive definite after reducing the neighborhood because that set is open. Uniqueness of the principal positive root makes these local branches agree where they overlap. Thus $\mathbf S(t)$ is smooth throughout its positive-definite parameter domain, and two derivatives of the affine path are justified.

**Step 3 — CALCULUS.** Define the real symmetric matrices $\mathbf K(t)=\frac{d}{dt}(\mathbf S(t))$ and $\mathbf T(t)=\frac{d^2}{dt^2}(\mathbf S(t))$. Differentiation of $\mathbf S(t)\mathbf S(t)=\mathbf A_0+t\mathbf H$ gives the ordered equation

$$
\mathbf S(t)\mathbf K(t)+\mathbf K(t)\mathbf S(t)=\mathbf H.
$$

Differentiating its left side produces four terms. The two first-derivative products coincide with $\mathbf K(t)^2$, so

$$
\mathbf S(t)\mathbf T(t)+\mathbf T(t)\mathbf S(t)=-2\mathbf K(t)^2.
$$

The same invertible linear map from Step 2 determines each derivative uniquely. The zero second derivative of the affine input does not remove the square of the first root derivative.

**Step 4 — ALGEBRA.** At one fixed admissible parameter value, let $\mathbf U$ diagonalize its square root, and write $\widehat{\mathbf H}=\mathbf U^{\mathsf T}\mathbf H\mathbf U$, $\widehat{\mathbf K}=\mathbf U^{\mathsf T}\mathbf K\mathbf U$, and $\widehat{\mathbf T}=\mathbf U^{\mathsf T}\mathbf T\mathbf U$. With all indices from one to $n$,

$$
\widehat K_{ij}=\frac{\widehat H_{ij}}{\sigma_i+\sigma_j},\qquad
\widehat T_{ij}=-\frac{2}{\sigma_i+\sigma_j}
\sum_{k=1}^n\widehat K_{ik}\widehat K_{kj}.
$$

The original derivatives are $\mathbf U\widehat{\mathbf K}\mathbf U^{\mathsf T}$ and $\mathbf U\widehat{\mathbf T}\mathbf U^{\mathsf T}$. The eigenbasis is used to solve already differentiated fixed-basis equations at the chosen parameter; no differentiability of that basis is being assumed.

**Step 5 — DOMAIN: the specified path.** Here

$$
\mathbf A(t)=\begin{bmatrix}1+t&t\\t&4+2t\end{bmatrix},\qquad
\det(\mathbf A(t))=t^2+6t+4.
$$

Positive definiteness requires $1+t>0$ and $t^2+6t+4>0$. The determinant roots are $-3-\sqrt5$ and $-3+\sqrt5$. Intersecting its positive intervals with $t>-1$ leaves exactly

$$
t>-3+\sqrt5.
$$

At zero, $\mathbf S(0)=\operatorname{diag}(1,2)$. The three distinct equations for the first derivative are $2K_{11}(0)=1$, $3K_{12}(0)=1$, and $4K_{22}(0)=2$. Consequently

$$
\mathbf K(0)=\begin{bmatrix}1/2&1/3\\1/3&1/2\end{bmatrix},\qquad
\mathbf K(0)^2=\begin{bmatrix}13/36&1/3\\1/3&13/36\end{bmatrix}.
$$

The second derivative equations give $2T_{11}(0)=-13/18$, $3T_{12}(0)=-2/3$, and $4T_{22}(0)=-13/18$, hence

$$
\mathbf T(0)=\begin{bmatrix}-13/36&-2/9\\-2/9&-13/72\end{bmatrix}.
$$

In contrast, the proposed scalar-inspired rule at zero gives

$$
\frac12\mathbf S(0)^{-1}\mathbf H
=\begin{bmatrix}1/2&1/2\\1/4&1/2\end{bmatrix}.
$$

It is not even symmetric and differs from the unique root derivative. When $\mathbf S$ and $\mathbf H$ commute, their common diagonal representation does reduce the first equation to the scalar rule; the present example has no such commutation.

**Step 6 — CHECK.** An independent two-by-two square-root expression follows from the characteristic equation. Set

$$
d(t)=\sqrt{t^2+6t+4},\qquad
\mathbf B(t)=\frac{\mathbf A(t)+d(t)\mathbf I}{\sqrt{5+3t+2d(t)}}.
$$

On the full positive-definite domain, the numerator and scalar denominator are positive definite and positive respectively. The characteristic identity $\mathbf A(t)^2-(5+3t)\mathbf A(t)+d(t)^2\mathbf I=\mathbf0$ gives $\mathbf B(t)^2=\mathbf A(t)$, so uniqueness identifies $\mathbf B(t)=\mathbf S(t)$. Around zero, ordinary scalar Taylor expansions give

$$
d(t)=2+\frac32t-\frac5{16}t^2+O(t^3),\qquad
\sqrt{5+3t+2d(t)}=3+t-\frac{13}{48}t^2+O(t^3).
$$

Substitution and scalar division yield, entrywise,

$$
\begin{aligned}
\mathbf S(t)
={}&\begin{bmatrix}1&0\\0&2\end{bmatrix}
+t\begin{bmatrix}1/2&1/3\\1/3&1/2\end{bmatrix}\\
&+t^2\begin{bmatrix}-13/72&-1/9\\-1/9&-13/144\end{bmatrix}+O(t^3).
\end{aligned}
$$

The linear coefficient is $\mathbf K(0)$ and twice the quadratic coefficient is $\mathbf T(0)$, independently confirming every derivative entry. The scalar expansions have bounded higher derivatives on a sufficiently small closed interval around zero; their remainder orders are therefore justified.

**Discussion.** The positive branch makes an ordered linear matrix equation invertible. Off-diagonal sensitivities depend on sums of two root eigenvalues, even when the original matrix path is affine.

### D3-017

**Step 1 — SETUP.** Put $r(\mathbf x)=\|\mathbf x\|$. Although the norm itself needs care at zero, the map uses only its square $x_1^2+x_2^2+x_3^2$ and is polynomial on the whole space. Define its real $3\times3$ Jacobian by $J_{ij}(\mathbf x)=\frac{\partial}{\partial x_j}(F_i(\mathbf x))$, with $1\le i,j\le3$.

**Step 2 — CHOICE.** A direction-preserving radial map can be analyzed on each ray, while its local derivative separates radial and transverse increments. The global inverse must be proved from the radius map as well as from the nonvanishing Jacobian.

**Step 3 — CALCULUS.** Component differentiation gives

$$
J_{ij}(\mathbf x)=(1+r(\mathbf x)^2)\delta_{ij}+2x_ix_j,
\qquad
\mathbf J(\mathbf x)=(1+r(\mathbf x)^2)\mathbf I+2\mathbf x\mathbf x^{\mathsf T}.
$$

If $\mathbf x\ne\mathbf0$, multiplication by a transverse vector $\mathbf h$ with $\mathbf x^{\mathsf T}\mathbf h=0$ gives $(1+r(\mathbf x)^2)\mathbf h$, while multiplication by $\mathbf x$ gives $(1+3r(\mathbf x)^2)\mathbf x$. Thus

$$
\det(\mathbf J(\mathbf x))=(1+r(\mathbf x)^2)^2(1+3r(\mathbf x)^2)>0.
$$

At zero the Jacobian is $\mathbf I$, with the same determinant formula. A second component differentiation gives

$$
\frac{\partial}{\partial x_k}\left(\frac{\partial}{\partial x_j}(F_i(\mathbf x))\right)
=2x_k\delta_{ij}+2x_j\delta_{ik}+2x_i\delta_{jk},\qquad 1\le i,j,k\le3.
$$

For fixed real increments $\mathbf u,\mathbf v$, contracting explicitly over the second and third indices yields

$$
\mathrm D^2\mathbf F(\mathbf x)(\mathbf u,\mathbf v)
=2\bigl((\mathbf x^{\mathsf T}\mathbf v)\mathbf u
+(\mathbf x^{\mathsf T}\mathbf u)\mathbf v
+(\mathbf u^{\mathsf T}\mathbf v)\mathbf x\bigr).
$$

For example, its $i$th component is the finite sum of the displayed component derivative times $u_jv_k$, summed over $j=1,2,3$ and $k=1,2,3$ separately.

**Step 4 — ALGEBRA AND GLOBAL INVERSION.** For an input radius $r\ge0$, the output radius is $\rho=r+r^3$. This scalar map has derivative $1+3r^2>0$, value zero at zero, and tends to infinity. It is therefore a continuous bijection from $[0,\infty)$ to itself. Moreover the factor $1+r^2$ is positive, so a nonzero vector and its image have exactly the same direction.

For each $\mathbf y\ne\mathbf0$, let $\rho=\|\mathbf y\|$ and let $r\ge0$ be the unique solution of $r+r^3=\rho$. Then

$$
\mathbf G(\mathbf y)=\frac{r}{\rho}\mathbf y
=\frac{1}{1+r^2}\mathbf y,\qquad \mathbf G(\mathbf0)=\mathbf0.
$$

This constructs an inverse and proves both existence and uniqueness on the whole space. The inverse function theorem applies at every input because the Jacobian is invertible there. Its smooth local inverses agree with the unique global inverse just constructed, making $\mathbf G$ smooth everywhere, including at zero.

**Step 5 — CALCULUS: first inverse derivative.** In the remaining formulas, $\mathbf x=\mathbf G(\mathbf y)$ and $r=\|\mathbf x\|$. Differentiating the inverse identity gives

$$
\mathrm D\mathbf G(\mathbf y)=\mathbf J(\mathbf x)^{-1}
=\frac{1}{1+r^2}\mathbf I
-\frac{2}{(1+r^2)(1+3r^2)}\mathbf x\mathbf x^{\mathsf T}.
$$

Multiplication by $(1+r^2)\mathbf I+2\mathbf x\mathbf x^{\mathsf T}$ verifies the inverse: the coefficient of $\mathbf x\mathbf x^{\mathsf T}$ is

$$
\frac{2}{1+r^2}-\frac{2}{1+3r^2}
-\frac{4r^2}{(1+r^2)(1+3r^2)}=0.
$$

For nonzero $\mathbf y$, its radial eigenvalue is $1/(1+3r^2)$ and its two transverse eigenvalues are $1/(1+r^2)$. At zero all three are one and $\mathrm D\mathbf G(\mathbf0)=\mathbf I$. Independently differentiating the scalar inverse radius gives $dr/d\rho=1/(1+3r^2)$; changing direction at fixed radius gives the factor $r/\rho=1/(1+r^2)$, confirming both local scales.

**Step 6 — CALCULUS: second inverse derivative.** Define $\mathbf B=\mathbf J(\mathbf x)^{-1}$, $\mathbf u=\mathbf B\mathbf h$, and $\mathbf v=\mathbf B\mathbf k$ for the given fixed increments. Differentiating $\mathbf F(\mathbf G(\mathbf y))=\mathbf y$ twice, once in each increment, gives

$$
\mathbf J(\mathbf x)\mathrm D^2\mathbf G(\mathbf y)(\mathbf h,\mathbf k)
+\mathrm D^2\mathbf F(\mathbf x)(\mathbf u,\mathbf v)=\mathbf0.
$$

Multiplying by the inverse on the left therefore gives the explicit symmetric bilinear expression

$$
\mathrm D^2\mathbf G(\mathbf y)(\mathbf h,\mathbf k)
=-2\mathbf B\bigl((\mathbf x^{\mathsf T}\mathbf v)\mathbf u
+(\mathbf x^{\mathsf T}\mathbf u)\mathbf v
+(\mathbf u^{\mathsf T}\mathbf v)\mathbf x\bigr).
$$

It vanishes at $\mathbf y=\mathbf0$, where $\mathbf x=\mathbf0$ and $\mathbf B=\mathbf I$. There is no singular norm derivative hidden in this formula.

**Step 7 — CHECK.** For $\mathbf y=2\mathbf e_1$, the input radius is $r=1$ and $\mathbf x=\mathbf e_1$. Direct substitution gives

$$
\mathbf J(\mathbf e_1)=\operatorname{diag}(4,2,2),\qquad
\mathrm D\mathbf G(2\mathbf e_1)=\operatorname{diag}(1/4,1/2,1/2),
$$

and the determinant of the forward Jacobian is sixteen. The second-derivative formula gives

$$
\mathrm D^2\mathbf G(2\mathbf e_1)(\mathbf e_1,\mathbf e_1)=-\frac3{32}\mathbf e_1,\qquad
\mathrm D^2\mathbf G(2\mathbf e_1)(\mathbf e_2,\mathbf e_2)=-\frac18\mathbf e_1.
$$

For an independent radial check, differentiating $dr/d\rho=1/(1+3r^2)$ gives $d^2r/d\rho^2=-6r/(1+3r^2)^3$, whose value at $r=1$ is $-3/32$. For the transverse check, take $\mathbf y=[2,h,0]^{\mathsf T}$. Then $\rho=2+h^2/4+O(h^4)$ and $r=1+h^2/16+O(h^4)$, so $G_1(\mathbf y)=1-h^2/16+O(h^4)$ and its second derivative at zero is $-1/8$, as required.

**Step 8 — DOMAIN.** Both the forward and inverse maps are defined and smooth on all of $\mathbb R^3$. Every scalar denominator in the derivative formulas is strictly positive. The implicit radius description selects a unique nonnegative root and needs neither additional algebraic branches nor an exclusion of the spatial origin.

**Discussion.** A radial scalar equation establishes the global inverse, while radial and transverse local scales determine its derivatives. A nonzero Jacobian supplies the local step of that argument.

## Application references

These are original review problems. The waveguide model is motivated by
[MIT 6.013, Lecture 16](https://www.ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/d9425aa2b1acd0c1fc121965ad7eafec_MIT6_013S09_lec16.pdf).
Singular Green kernels and discretized field systems occur in the integral-equation
work discussed by [Tihon and Craeye, All-analytical evaluation of the singular integrals involved in the Method of Moments](https://arxiv.org/abs/1911.12660).
The small scalar and matrix models isolate calculus issues; their solutions do
not constitute full waveguide or antenna designs.
