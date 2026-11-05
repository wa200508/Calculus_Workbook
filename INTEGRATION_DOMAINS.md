# I3 · Oscillatory and singular integrals

## Problems

### I3-001 — Sine over a half-period

**Objects and dependencies.** $x\in[0,\pi]$ is an independent real scalar angle in radians and the integration variable. The real scalar integrand is $q(x)=\sin x$. Evaluate $\int_0^\pi q(x)\,dx$. Assess whether the coordinate $u=g(x)=\sin x$ permits evaluation over one transformed interval without a branch partition.

### I3-002 — An oscillatory ratio on a finite interval

**Objects and dependencies.** $x\in[0,L]$ is a real scalar integration coordinate. The fixed length $L>0$ and fixed real wavenumber $k$ satisfy $kx$ dimensionless. For $x>0$ let $q(x;k)=\sin(kx)/x$. Evaluate the real scalar number $J(k,L)=\int_0^Lq(x;k)\,dx$, stating the extension at $x=0$, the case $k=0$, and a small-$|kL|$ approximation with an error bound. The semicolon separates the varying coordinate from the fixed parameter inside the integrand.

### I3-003 — Damping a conditionally convergent oscillatory integral

**Objects and dependencies.** $x\ge0$ is the real integration coordinate; $k>0$ is a fixed real wavenumber. The real scalar damping parameter $\epsilon>0$ has the same units as $k$. The scalar integrand has its removable value $k$ at zero. Define

$$
F(\epsilon;k)=\int_0^\infty \exp(-\epsilon x)\frac{\sin(kx)}{x}\,dx.
$$

Evaluate $F(\epsilon;k)$ using differentiation with respect to $\epsilon$. Determine the ordinary improper integral with $\epsilon=0$, and distinguish its convergence from absolute convergence. Any interchange of a derivative or a limit with the integral requires a stated justification.

### I3-004 — A finite aperture integral at phase matching

**Objects and dependencies.** $z\in[0,L]$ is a real integration coordinate and $L>0$ a fixed length. The independent real scalar $\Delta$ is a wavenumber mismatch. $\mathrm{i}^2=-1$ is fixed. Evaluate the complex scalar amplitude

$$
A(\Delta;L)=\int_0^L\exp(\mathrm{i}\Delta z)\,dz
$$

including $\Delta=0$, and obtain a form that makes its magnitude and phase center apparent. Explain why division by $\Delta$ does not establish a singular physical amplitude at phase matching.

### I3-005 — A reciprocal kernel with an interior pole

**Objects and dependencies.** $x$ is a dimensionless real integration coordinate on $[-1,1]$. A fixed real scalar $a$ satisfies $-1<a<1$. The real scalar function $q(x;a)=1/(x-a)$ is undefined at $x=a$. Determine whether $\int_{-1}^1q(x;a)\,dx$ exists as an ordinary improper integral, and evaluate its Cauchy principal value with equal exclusions $a-\delta,a+\delta$ for real $\delta>0$ small enough. Describe what happens when $a$ is an endpoint.

### I3-006 — Near a line source: differentiation under an integral

**Objects and dependencies.** $s\in[-L,L]$ is a real scalar source coordinate, with fixed real length $L>0$. The independent real scalar observation distance is $\rho>0$. The real dimensionless scalar kernel integral is

$$
P(\rho;L)=\int_{-L}^L\frac{1}{\sqrt{\rho^2+s^2}}\,ds.
$$

Evaluate $P(\rho;L)$, find $\frac{\partial}{\partial\rho}\left(P(\rho;L)\right)$ with $L$ held fixed both from the closed form and under the integral sign, and describe the limit $\rho\downarrow0$. A constant charge and permittivity prefactor would convert $P$ into an electrostatic potential.

### I3-007 — A weakly singular CEM panel integral

**Objects and dependencies.** Independent real dimensionless coordinates $x,y$ describe the triangle $T=\{(x,y):0\le y\le x\le1\}$. The real scalar integrand is $q(x,y)=1/\sqrt{x^2+y^2}$ away from $(0,0)$. Evaluate

$$
K=\int_0^1\int_0^x\frac{1}{\sqrt{x^2+y^2}}\,dy\,dx
$$

as a nonnegative improper area integral using $x=u$, $y=uv$. The new independent real coordinates satisfy $0<u\le1$, $0\le v\le1$. Find the Jacobian explicitly. Compare this with replacing the denominator by $x^2+y^2$.

### I3-008 — An ellipsoidal weighted volume

**Objects and dependencies.** Fixed real lengths $a,b,c>0$ define the ellipsoid $E=\{(x,y,z):x^2/a^2+y^2/b^2+z^2/c^2\le1\}$. The independent real coordinates are $x,y,z$. Define the real dimensionless scalar $q(x,y,z)=x^2/a^2+y^2/b^2+z^2/c^2$. Evaluate the real scalar weighted volume

$$
W(a,b,c)=\iiint_E\exp(-q(x,y,z))\,dx\,dy\,dz.
$$

The error function, if needed, is defined for real scalar $s$ by $\operatorname{erf}(s)=\frac{2}{\sqrt\pi}\int_0^s\exp(-t^2)\,dt$, where $t$ is a dummy real integration variable. Show the transformed domain and the volume Jacobian, not only the transformed exponential.

### I3-009 — Finite and infinite surface area of a hyperboloid

**Objects and dependencies.** The fixed real length is $\ell>0$ and the fixed real cutoff parameter is $U\ge0$. Independent dimensionless real parameters satisfy $-U\le u\le U$, $0\le v<2\pi$. Define the real column vector

$$
\mathbf r(u,v)=\begin{bmatrix}\ell\cosh(u)\cos(v)\\\ell\cosh(u)\sin(v)\\\ell\sinh(u)\end{bmatrix}.
$$

Find the real scalar area $S(U;\ell)$ of this band on $x^2+y^2-z^2=\ell^2$. Determine whether the complete one-sheet hyperboloid has finite area. The angular seam is counted once.

### I3-010 — A squared aperture kernel

**Objects and dependencies.** $x\ge0$ is a real length coordinate and the integration variable. The independent real wavenumber $a$ makes $ax$ dimensionless. Define the real scalar

$$
Q(a)=\int_0^\infty\left(\frac{\sin(ax)}{x}\right)^2\,dx,
$$

with the integrand extended to $a^2$ at $x=0$. Evaluate $Q(a)$ for every real $a$, establish absolute convergence, and determine its differentiability in $a$. Assess the integral of the formally differentiated kernel both at nonzero $a$ and at zero. Give a bound for the error made by truncating the original integral at a finite positive length.

### I3-011 — A logarithmic moment at an endpoint

**Objects and dependencies.** $x\in(0,1]$ is a dimensionless real integration coordinate. The requested output is the real scalar improper integral

$$
M=\int_0^1\frac{\ln^2x}{1+x}\,dx.
$$

Evaluate $M$ in terms of a convergent series or a named constant whose definition is supplied. For each positive integer $N$, obtain an explicit error bound for a finite approximation with $N$ terms. Justify any interchange of an infinite sum and the improper integral, and give an independent integral representation with a controlled tail.

### I3-012 — A shrinking layer and its parameter derivative

**Objects and dependencies.** $x\in[0,1]$ is a dimensionless real integration coordinate and $a>0$ is an independent dimensionless real parameter. The real scalar function is

$$
F(a)=\int_0^1\frac{a}{x^2+a^2}\,dx.
$$

Determine $F(a)$, its derivative for positive $a$, and its limit as $a\downarrow0$. Compare that limit with integrating the almost-everywhere pointwise limit of the kernel. For fixed real $c>0$, quantify the contribution from $0\le x\le ca$ when $ca\le1$. Find a controlled expansion through the cubic term, and distinguish the continuous extension of $F$ from the value obtained by setting $a=0$ in the kernel before integration.

### I3-013 — Two closed paths around an excluded axis

**Objects and dependencies.** Independent real dimensionless Cartesian coordinates satisfy $x^2+y^2>0$. The real column vector field is

$$
\mathbf F(x,y,z)=\frac{1}{x^2+y^2}\begin{bmatrix}-y\\x\\0\end{bmatrix}.
$$

Fixed real parameters obey $A,B,R>0$, $d>R$, and $z_0\in\mathbb R$. Two closed curves, parameterized by the real angle $0\le\theta\le2\pi$, are

$$
\mathbf r_E(\theta)=\begin{bmatrix}A\cos\theta\\B\sin\theta\\z_0\end{bmatrix},
\qquad
\mathbf r_C(\theta)=\begin{bmatrix}d+R\cos\theta\\R\sin\theta\\z_0\end{bmatrix}.
$$

Both are counterclockwise as viewed from positive $z$. Evaluate their oriented circulations $\oint\mathbf F\cdot d\mathbf r$, compute the curl off the excluded axis, and determine why using that curl on the two spanning disks requires different conclusions. Verify each circulation by another calculation or a justified excision argument.

### I3-014 — A source inside a triangular panel

**Objects and dependencies.** Independent real dimensionless coordinates describe the triangle $T=\{(x,y):0\le y\le x\le1\}$. A fixed interior source is the real column vector $\mathbf p=[x_0,y_0]^{\mathsf T}$, with $0<y_0<x_0<1$. Evaluate the real scalar nonnegative improper integral

$$
K(x_0,y_0)=\iint_T\frac{1}{\sqrt{(x-x_0)^2+(y-y_0)^2}}\,dx\,dy.
$$

Partition the panel around its source and specify a map, domain, and Jacobian for each part. Reduce the integral to nonsingular one-dimensional integrals and obtain an explicit real expression. Justify the treatment of the source and provide an independent check; merely applying the vertex map from I3-007 to the whole panel is insufficient.

## Hint ladders

### I3-001

1. The map $u=\sin x$ increases on the first half of the interval and decreases on the second.
2. The inverse branch is $x=\arcsin u$ on the first half and $x=\pi-\arcsin u$ on the second.
3. Both branches contribute positively after their different orientations are accounted for.

### I3-002

1. The limit $\sin(kx)/x\to k$ removes the apparent endpoint singularity.
2. For $k\ne0$, the coordinate $u=kx$ changes the integral to the defining sine integral.
3. A Taylor remainder for $\sin(kx)$, divided by $x$ and integrated, bounds the error.

### I3-003

1. For positive damping, differentiation with respect to $\epsilon$ removes the factor $1/x$.
2. The remaining damped sine integral equals $k/(\epsilon^2+k^2)$.
3. The constant is fixed by $F(\epsilon;k)\to0$ as $\epsilon\to\infty$. Undamped tails need an oscillatory estimate rather than absolute domination.

### I3-004

1. For $\Delta\ne0$, the complex exponential has an elementary antiderivative in $z$.
2. Factoring the numerator about $z=L/2$ leads to a sine divided by its argument.
3. At $\Delta=0$, the original integrand is identically one.

### I3-005

1. The two sides of the pole must have finite limits separately for the ordinary improper integral to exist.
2. The antiderivative on either side is $\ln|x-a|$.
3. Equal logarithmic divergences cancel only under the specified principal-value prescription.

### I3-006

1. The scalar substitution $s=\rho\sinh u$ removes the square root for $\rho>0$.
2. Its endpoints depend on $\rho$; the resulting closed form is twice an inverse hyperbolic sine.
3. Under differentiation with respect to $\rho$, the kernel becomes $-\rho(\rho^2+s^2)^{-3/2}$.

### I3-007

1. On the triangle, $v=y/x$ runs from zero to one for $x>0$.
2. The absolute determinant of the coordinate Jacobian is $u$.
3. One power of $u$ cancels the $1/R$ singularity. A $1/R^2$ kernel retains a logarithmically divergent $u$ integral.

### I3-008

1. Scaling by the three semiaxes maps the ellipsoid to the unit ball.
2. Spherical coordinates on that ball contribute a further factor $r^2\sin\theta$.
3. Integration by parts reduces $\int_0^1r^2\exp(-r^2)\,dr$ to a boundary term and an error-function integral.

### I3-009

1. The surface area measure is the length of the tangent cross product.
2. The identity $\cosh^2u=1+\sinh^2u$ makes $t=\sinh u$ useful.
3. The area becomes an integral of $\sqrt{1+2t^2}$ on a finite symmetric interval, whose size grows without bound as $U$ increases.

### I3-010

1. Near zero, $|\sin(ax)|\le|ax|$; at infinity, $|\sin(ax)|\le1$.
2. Rescaling by $|a|$ separates the parameter. Integration by parts turns the remaining squared sine into a sine-over-coordinate integral.
3. Away from zero the formal derivative is a conditionally convergent integral. At zero, compare the two difference quotients of the evaluated function.

### I3-011

1. A finite geometric identity for $1/(1+x)$ provides a remainder with a known sign.
2. The substitution $x=\exp(-t)$ evaluates $\int_0^1x^n\ln^2x\,dx$ by two integrations by parts.
3. The sum of the absolute integrals is finite. Separate even and odd indices to relate the answer to $\sum_{m=1}^\infty m^{-3}$.

### I3-012

1. The coordinate $u=x/a$ changes the upper bound to $1/a$ and removes $a$ from the integrand.
2. The same coordinate gives the mass in $0\le x\le ca$. At every fixed positive $x$, the original kernel instead tends to zero.
3. Differentiate at a fixed positive parameter before taking any limit. A finite expansion of $1/(1+t^2)$ controls the small-$a$ remainder.

### I3-013

1. On the centered ellipse, the line integrand becomes $AB/(A^2\cos^2\theta+B^2\sin^2\theta)$.
2. The centered ellipse encloses the excluded axis, whereas the entire disk of the displaced circle stays at positive distance from it.
3. Excise a small centered disk from the ellipse's interior. On the displaced circle, $x>0$ permits one continuous real angle throughout the path.

### I3-014

1. Join the source to the three vertices, using the counterclockwise oriented outer edges.
2. On a source-edge subtriangle, use $\mathbf r(u,v)=\mathbf p+u(\mathbf a+v\mathbf e)$, where $\mathbf a$ runs from the source to the first edge vertex and $\mathbf e$ runs along that edge.
3. Its Jacobian is $u\det(\mathbf a,\mathbf e)$. After cancellation of the kernel's radial factor, resolve the edge vector into tangential and perpendicular components.

## Complete solutions

### I3-001

**Step 1 — SETUP.** The input and integration variable is the real angle $x\in[0,\pi]$, and the output integral is a real number. The function $\sin x$ is continuous throughout this interval.

**Step 2 — CHOICE.** The map $g(x)=\sin x$ is not one-to-one on the full interval. The substitution rule for an integrand $h(g(x))\frac{d}{dx}(g(x))$ cannot be applied directly: the original integrand is $\sin x$, not $h(\sin x)\cos x$ for a single globally defined $h$ here. An inverse-coordinate substitution instead needs two branches.

**Step 3 — CALCULUS.** On $0\le x<\pi/2$, the inverse is $x_1(u)=\arcsin u$, with derivative $1/\sqrt{1-u^2}$ and limits $u=0$ to $u=1$. On $\pi/2<x\le\pi$, the inverse is $x_2(u)=\pi-\arcsin u$, with derivative $-1/\sqrt{1-u^2}$ and limits $u=1$ to $u=0$. The inverse derivatives are singular at $u=1$, so both transformed integrals are improper there:

$$
\int_0^\pi\sin x\,dx
=\int_0^1\frac{u}{\sqrt{1-u^2}}\,du
+\int_1^0\frac{-u}{\sqrt{1-u^2}}\,du.
$$

**Step 4 — ALGEBRA.** Reversing the second integral's limits changes its sign. The total is twice the first integral. A primitive on $0<u<1$ is $-\sqrt{1-u^2}$, so

$$
\int_0^\pi\sin x\,dx
=2\lim_{b\uparrow1}\left(-\sqrt{1-b^2}+1\right)=2.
$$

**Step 5 — CHECK.** Direct integration gives $[-\cos x]_0^\pi=2$. The integral represents a positive area. The equal transformed endpoints arose because the coordinate map retraced its values, not because the two halves of the integral canceled. By contrast, $\int_0^\pi\sin x\cos x\,dx=0$ legitimately follows from the direct chain-rule substitution, which does not require an inverse map.

**Discussion.** Equal transformed endpoints are meaningful only after the transformed integrand and the applicable substitution theorem have been identified. A folding coordinate map can conceal multiplicity and orientation.

### I3-002

**Step 1 — SETUP.** $x$ is a real length coordinate, $k$ and $L$ are fixed, and the integral is a real dimensionless scalar. The defining formula at $x>0$ has a continuous extension $q(0;k)=k$, including $k=0$.

**Step 2 — CHOICE.** The numerator's derivative does not match a substitution that turns this into an elementary sine primitive. The ratio leads to a special function instead. For $k\ne0$, $u=g(x;k)=kx$ is a valid invertible linear coordinate, with real scalar inverse $x=h(u;k)=u/k$.

**Step 3 — CALCULUS.** With $k$ held fixed, the coordinate derivatives are $\frac{\partial}{\partial x}\left(g(x;k)\right)=k$ and $\frac{\partial}{\partial u}\left(h(u;k)\right)=1/k$. The transformed bounds are $u=0$ to $u=kL$. Thus

$$
J(k,L)=\int_0^{kL}\frac{\sin u}{u}\,du=\operatorname{Si}(kL).
$$

Here the real sine integral is defined by $\operatorname{Si}(s)=\int_0^s\sin(u)/u\,du$ with the limiting integrand value one at zero. For $k<0$ the oriented limits already include the sign. For $k=0$, the original integrand is zero everywhere and $J(0,L)=0$; no division by zero is used.

**Step 4 — TRICK: Taylor expansion with remainder.** The supporting expansion and error convention are described in [T-002](TRICKS_APPENDIX.md#t-002-taylor-expansions). For real $k,x$, Taylor's theorem gives

$$
\sin(kx)=kx-\frac{(kx)^3}{6}+r(x;k),\qquad |r(x;k)|\le\frac{|kx|^5}{120}.
$$

Dividing by $x>0$ and integrating over the finite interval gives

$$
J(k,L)=kL-\frac{k^3L^3}{18}+E(k,L),\qquad
|E(k,L)|\le\frac{|k|^5L^5}{600}.
$$

**Step 5 — CHECK.** With respect to the real endpoint $L$, the fundamental theorem gives $\frac{\partial}{\partial L}(J(k,L))=\sin(kL)/L$ for $L>0$. This agrees with the special-function expression. The integral is odd in $k$, and the approximation preserves that property. Small $|kL|$ controls the stated error; a small value of $k$ alone is insufficient when $L$ is large.

**Discussion.** A familiar sine inside a ratio need not have an elementary antiderivative. A special-function definition and a controlled approximation are valid, distinct forms of a solution.

### I3-003

**Step 1 — SETUP.** The integration coordinate is real $x\ge0$, while $k>0$ is fixed and $\epsilon>0$ varies. The integrand is bounded at zero after extension and is absolutely integrable at infinity when $\epsilon>0$.

**Step 2 — CHOICE.** Differentiation with respect to damping removes $1/x$. Near any fixed $\epsilon_0>0$, the absolute value of the differentiated integrand is bounded by $\exp(-\epsilon_0x/2)$ for $\epsilon\ge\epsilon_0/2$. This integrable bound justifies differentiation under the integral sign locally.

**Step 3 — CALCULUS.** With $k$ held fixed,

$$
\frac{\partial}{\partial\epsilon}\left(F(\epsilon;k)\right)
=-\int_0^\infty\exp(-\epsilon x)\sin(kx)\,dx.
$$

**Step 4 — TRICK: Euler identity.** The supporting identity is listed in [T-001](TRICKS_APPENDIX.md#t-001-euler-identities). The imaginary part of $\exp((-\epsilon+\mathrm{i}k)x)$ is $\exp(-\epsilon x)\sin(kx)$. Since $\epsilon>0$, its boundary value at infinity is zero, and

$$
\int_0^\infty\exp((-\epsilon+\mathrm{i}k)x)\,dx
=\frac{1}{\epsilon-\mathrm{i}k}
=\frac{\epsilon+\mathrm{i}k}{\epsilon^2+k^2}.
$$

The imaginary part is $k/(\epsilon^2+k^2)$.

**Step 5 — CALCULUS.** Integration with respect to the real damping parameter gives $F(\epsilon;k)=-\arctan(\epsilon/k)+C(k)$, where the scalar $C(k)$ is independent of $\epsilon$.

**Step 6 — ALGEBRA.** The estimate $|\sin(kx)|/x\le k$ gives $|F(\epsilon;k)|\le k/\epsilon$, hence $F\to0$ as $\epsilon\to\infty$. Therefore

$$
F(\epsilon;k)=\frac{\pi}{2}-\arctan(\epsilon/k)=\arctan(k/\epsilon).
$$

**Step 7 — DOMAIN: the undamped limit.** Absolute domination by $|\sin(kx)|/x$ is unavailable on the infinite interval. For any real $A>0$, let $f_\epsilon(x)=\exp(-\epsilon x)/x$, including $\epsilon=0$. This positive function decreases to zero. Integration by parts against the bounded primitive $-\cos(kx)/k$ gives, for $B>A$,

$$
\left|\int_A^B f_\epsilon(x)\sin(kx)\,dx\right|
\le\frac{f_\epsilon(A)+f_\epsilon(B)+\int_A^B|\frac{d}{dx}(f_\epsilon(x))|\,dx}{k}
=\frac{2f_\epsilon(A)}{k}\le\frac{2}{kA}.
$$

The same uniform tail bound holds as $B\to\infty$. On the finite interval $[0,A]$, the integrands converge under a bounded domination as $\epsilon\downarrow0$. Finite-interval convergence plus the uniform tail bound justifies the limit:

$$
\int_0^\infty\frac{\sin(kx)}{x}\,dx
=\lim_{\epsilon\downarrow0}F(\epsilon;k)=\frac{\pi}{2},\qquad k>0.
$$

**Step 8 — CHECK: absolute convergence fails.** In the coordinate $u=kx$, each interval $[n\pi+\pi/6,n\pi+5\pi/6]$ has $|\sin u|\ge1/2$. For integers $n\ge1$, its contribution to $\int|\sin u|/u\,du$ is at least $1/[3(n+1)]$. The harmonic lower bound diverges. Thus the undamped integral is conditionally convergent. Its differentiated damping integral at $\epsilon=0$ would contain $\int_0^\infty\sin(kx)\,dx$, whose ordinary limit does not exist. The interchange valid for positive damping is not valid at the endpoint.

**Discussion.** Oscillatory cancellation can make an integral converge without absolute convergence. A limit at the edge of a parameter domain needs its own argument.

### I3-004

**Step 1 — SETUP.** The real coordinate $z$ is integrated from zero to the fixed length $L$. The mismatch $\Delta$ is a real parameter. The amplitude is complex scalar-valued and has units of length.

**Step 2 — CHOICE.** A complex exponential can be integrated componentwise with respect to the real coordinate. The case $\Delta=0$ is separated before division by the parameter.

**Step 3 — CALCULUS.** For $\Delta\ne0$, a primitive in $z$ is $\exp(\mathrm{i}\Delta z)/(\mathrm{i}\Delta)$, so

$$
A(\Delta;L)=\frac{\exp(\mathrm{i}\Delta L)-1}{\mathrm{i}\Delta}.
$$

For $\Delta=0$, integration of one gives $A(0;L)=L$ directly.

**Step 4 — TRICK: Euler identity.** The supporting identity is listed in [T-001](TRICKS_APPENDIX.md#t-001-euler-identities). Factoring about the midpoint gives

$$
\exp(\mathrm{i}\Delta L)-1
=\exp(\mathrm{i}\Delta L/2)\left(\exp(\mathrm{i}\Delta L/2)-\exp(-\mathrm{i}\Delta L/2)\right)
=2\mathrm{i}\exp(\mathrm{i}\Delta L/2)\sin(\Delta L/2).
$$

**Step 5 — ALGEBRA.** The real scalar function $\operatorname{sinc}_0(s)=\sin(s)/s$ is defined for $s\ne0$, with $\operatorname{sinc}_0(0)=1$. The subscript distinguishes this unnormalized convention from $\sin(\pi s)/(\pi s)$. Then

$$
A(\Delta;L)=L\exp(\mathrm{i}\Delta L/2)\operatorname{sinc}_0(\Delta L/2),\qquad
|A(\Delta;L)|=L|\operatorname{sinc}_0(\Delta L/2)|.
$$

**Step 6 — CHECK.** The limiting value at zero is $L$, and $|A|\le L$ follows independently from the triangle inequality for the original integral. The exponential locates the phase center at the midpoint; when the real sinc factor is negative it contributes an additional phase of $\pi$. At its zeros the amplitude is zero and its phase is undefined.

**Discussion.** A quotient singularity introduced by a parameterized antiderivative may be removable even though the formula with division is undefined there. Phase still needs separate treatment at amplitude zeros.

### I3-005

**Step 1 — SETUP.** $x$ is the integration variable; the fixed real pole location $a$ is inside $(-1,1)$. The scalar function is continuous on each side of $a$ but not at $a$.

**Step 2 — CHOICE.** The ordinary improper integral requires two separate finite limits. The antiderivative $\ln|x-a|$ is valid on each connected side, and does not justify crossing the pole in one endpoint subtraction.

**Step 3 — CALCULUS.** For positive real cutoffs $\delta_-,\delta_+$,

$$
\begin{aligned}
\int_{-1}^{a-\delta_-}\frac{1}{x-a}\,dx&=\ln\delta_- -\ln(1+a)\longrightarrow-\infty,\\
\int_{a+\delta_+}^{1}\frac{1}{x-a}\,dx&=\ln(1-a)-\ln\delta_+\longrightarrow+\infty.
\end{aligned}
$$

The ordinary integral does not exist. The expression $-\infty+\infty$ has no assigned value.

**Step 4 — ALGEBRA: the specified principal value.** Setting both cutoffs equal to a real scalar $\delta$ before taking the limit gives

$$
\operatorname{PV}\int_{-1}^{1}\frac{1}{x-a}\,dx
=\lim_{\delta\downarrow0}\left(\ln\delta-\ln(1+a)+\ln(1-a)-\ln\delta\right)
=\ln\left(\frac{1-a}{1+a}\right).
$$

The ratio is positive for $-1<a<1$.

**Step 5 — CHECK.** At $a=0$, the principal value is zero by odd symmetry. If instead $\delta_-=\lambda\delta_+$ with a fixed real $\lambda>0$, the coupled limit differs by $\ln\lambda$. This shows why a limiting prescription matters. At $a=1$ or $a=-1$, only a one-sided endpoint divergence remains and the stated interior symmetric principal value is unavailable. A finite-part regularization would be another explicitly defined operation.

**Discussion.** Cancellation of divergences is a prescription, not proof that an ordinary improper integral exists. Symmetry is useful only after the definition of the integral is fixed.

### I3-006

**Step 1 — SETUP.** The source coordinate $s$ is integrated over the fixed finite interval $[-L,L]$. The parameter $\rho>0$ is a real distance, and $P(\rho;L)$ is a real dimensionless scalar. The kernel is continuous for every such parameter.

**Step 2 — CHOICE.** The hyperbolic coordinate $s=h(u;\rho)=\rho\sinh u$ is one-to-one for fixed $\rho>0$. It turns $\sqrt{\rho^2+s^2}$ into $\rho\cosh u$; positivity prevents an absolute-value ambiguity.

**Step 3 — CALCULUS.** Holding $\rho$ fixed during the substitution,

$$
\frac{\partial}{\partial u}\left(h(u;\rho)\right)=\rho\cosh u,\qquad
u_-=-\operatorname{arsinh}(L/\rho),\quad u_+=\operatorname{arsinh}(L/\rho).
$$

The integral is therefore

$$
P(\rho;L)=\int_{u_-}^{u_+}1\,du=2\operatorname{arsinh}(L/\rho)
=2\ln\left(\frac{L+\sqrt{L^2+\rho^2}}{\rho}\right).
$$

The logarithm's argument is dimensionless and positive. The bounds in the transformed coordinate depend on $\rho$ even though the original bounds do not.

**Step 4 — CALCULUS.** Differentiating the closed form with $L$ fixed gives

$$
\frac{\partial}{\partial\rho}\left(P(\rho;L)\right)
=\frac{2}{\sqrt{1+(L/\rho)^2}}\left(-\frac{L}{\rho^2}\right)
=-\frac{2L}{\rho\sqrt{\rho^2+L^2}}.
$$

**Step 5 — CALCULUS: differentiation under the integral.** On a neighborhood of any fixed $\rho_0>0$, the kernel and its $\rho$ derivative are continuous and bounded on the finite source interval. This justifies

$$
\frac{\partial}{\partial\rho}\left(P(\rho;L)\right)
=-\int_{-L}^{L}\frac{\rho}{(\rho^2+s^2)^{3/2}}\,ds.
$$

The derivative with respect to $s$ of $s/\sqrt{\rho^2+s^2}$ is $\rho^2/(\rho^2+s^2)^{3/2}$, with $\rho$ fixed. Endpoint evaluation thus gives

$$
-\frac{1}{\rho}\left[\frac{s}{\sqrt{\rho^2+s^2}}\right]_{s=-L}^{s=L}
=-\frac{2L}{\rho\sqrt{\rho^2+L^2}}.
$$

The square brackets here delimit endpoint evaluation, not a derivative operand or an object type.

**Step 6 — CHECK AND DOMAIN.** For small positive $\rho/L$, the potential grows like $2\ln(2L/\rho)$ and its derivative like $-2/\rho$. At $\rho=0$ the original kernel is $1/|s|$ and its integral diverges. The positive-distance justification is not uniform through the line source. For large $\rho/L$, $P(\rho;L)$ behaves like $2L/\rho$, as expected from the nearly constant kernel across the short source segment.

**Discussion.** A near-source limit can invalidate interchange rules that are harmless at every fixed positive observation distance. Parameter-dependent transformed bounds cannot be treated as constants in a later derivative.

### I3-007

**Step 1 — SETUP.** The integral is a real nonnegative area integral on the triangle, with the origin excluded and approached by a limit. The dimensionless map is $x(u,v)=u$, $y(u,v)=uv$. It is one-to-one for $u>0$, with inverse $u=x$, $v=y/x$.

**Step 2 — CHOICE.** The new coordinate $u$ measures distance toward the singular vertex while $v$ describes direction inside the triangle. The Jacobian may compensate the kernel's singularity. The edge $u=0$ collapses to the vertex and is handled by a limit.

**Step 3 — CALCULUS.** The real $2\times2$ coordinate Jacobian is

$$
\mathbf J(u,v)=\begin{bmatrix}
\frac{\partial}{\partial u}(x(u,v))&\frac{\partial}{\partial v}(x(u,v))\\
\frac{\partial}{\partial u}(y(u,v))&\frac{\partial}{\partial v}(y(u,v))
\end{bmatrix}
=\begin{bmatrix}1&0\\v&u\end{bmatrix},\qquad |\det\mathbf J(u,v)|=u.
$$

**Step 4 — ALGEBRA.** Since $u>0$, the distance is $\sqrt{u^2+u^2v^2}=u\sqrt{1+v^2}$. On the truncated triangle $x\ge\delta>0$, both kernel and Jacobian are regular. Their product gives

$$
K=\lim_{\delta\downarrow0}\int_\delta^1\int_0^1
\frac{u}{u\sqrt{1+v^2}}\,dv\,du
=\int_0^1\frac{1}{\sqrt{1+v^2}}\,dv
=\operatorname{arsinh}(1)=\ln(1+\sqrt2).
$$

Nonnegativity ensures that this increasing truncation gives the improper area integral, independent of the way nested neighborhoods of the vertex are removed.

**Step 5 — DOMAIN.** For the stronger scalar kernel $1/(x^2+y^2)$, the transformed integral is instead

$$
\lim_{\delta\downarrow0}\int_\delta^1\frac{1}{u}\,du\int_0^1\frac{1}{1+v^2}\,dv
=\lim_{\delta\downarrow0}(-\ln\delta)\frac{\pi}{4}=+\infty.
$$

No oscillatory or signed cancellation is available in this nonnegative example.

**Step 6 — CHECK.** The transformed $1/R$ integrand is bounded between $1/\sqrt2$ and one on a unit square, so the answer lies between those numbers; $\ln(1+\sqrt2)$ does. This vertex example illustrates the Duffy coordinate idea used in singular panel integration. More general CEM kernels, interior source positions, and vector testing functions require their own transformations and convergence analysis.

**Discussion.** The word singular does not determine integrability. The kernel, the dimension of the integration measure, and the coordinate Jacobian must be considered together.

### I3-008

**Step 1 — SETUP.** The independent Cartesian coordinates are real. The integrand is a positive scalar and the answer has units of volume. All semiaxes are fixed and positive, so the domain is compact with no integrand singularity.

**Step 2 — CHOICE.** The ellipsoidal quadratic form suggests scaling to the unit ball, followed by spherical coordinates. The transformed domain and measure are changed along with the function.

**Step 3 — CALCULUS: coordinate map.** Independent real coordinates satisfy $0\le r\le1$, $0\le\theta\le\pi$, $0\le\varphi<2\pi$. Define

$$
\begin{aligned}
x(r,\theta,\varphi)&=ar\sin\theta\cos\varphi,\\
y(r,\theta,\varphi)&=br\sin\theta\sin\varphi,\\
z(r,\theta,\varphi)&=cr\cos\theta.
\end{aligned}
$$

The real $3\times3$ Jacobian has columns given by partial differentiation with respect to $r,\theta,\varphi$:

$$
\mathbf J(r,\theta,\varphi)=\begin{bmatrix}
a\sin\theta\cos\varphi&ar\cos\theta\cos\varphi&-ar\sin\theta\sin\varphi\\
b\sin\theta\sin\varphi&br\cos\theta\sin\varphi&br\sin\theta\cos\varphi\\
c\cos\theta&-cr\sin\theta&0
\end{bmatrix}.
$$

**Step 4 — ALGEBRA.** Factoring $a,b,c$ from the rows and $r$ from each of the last two columns leaves determinant $\sin\theta$. Thus $|\det\mathbf J|=abc\,r^2\sin\theta$. Substitution into $q$ gives

$$
q(x(r,\theta,\varphi),y(r,\theta,\varphi),z(r,\theta,\varphi))
=r^2\bigl(\sin^2\theta(\cos^2\varphi+\sin^2\varphi)+\cos^2\theta\bigr)=r^2.
$$

The Jacobian degenerates at the center and poles. The angular seam instead identifies the same spatial points at $\varphi=0$ and $\varphi=2\pi$; it does not make the Jacobian vanish away from the center and poles. These exceptional sets have zero volume, and the map is regular and one-to-one in the remaining coordinate interior.

**Step 5 — CALCULUS.** The full transformed integral is

$$
W(a,b,c)=abc\int_0^{2\pi}\int_0^\pi\int_0^1\exp(-r^2)r^2\sin\theta\,dr\,d\theta\,d\varphi
=4\pi abc\int_0^1r^2\exp(-r^2)\,dr.
$$

For integration by parts in $r$, the factor $r\exp(-r^2)$ has primitive $-(1/2)\exp(-r^2)$, while the remaining factor $r$ has derivative one. Therefore

$$
\int_0^1r^2\exp(-r^2)\,dr
=-\frac{1}{2\exp(1)}+\frac12\int_0^1\exp(-r^2)\,dr
=-\frac{1}{2\exp(1)}+\frac{\sqrt\pi}{4}\operatorname{erf}(1).
$$

**Step 6 — RESULT AND CHECK.** The weighted volume is

$$
W(a,b,c)=abc\left(\pi^{3/2}\operatorname{erf}(1)-\frac{2\pi}{\exp(1)}\right).
$$

On the ellipsoid, $0\le q\le1$, so the result must lie between $4\pi abc/(3\exp(1))$ and the unweighted volume $4\pi abc/3$. The dimensionless coefficient is approximately $2.381$, within those bounds. A determinant without its absolute value would incorrectly make volume depend on orientation if a coordinate direction were reversed.

**Discussion.** A nonlinear integrand can become radial after a linear geometric change. The Jacobian supplies the volume scale and the radial power; dropping either changes the problem.

### I3-009

**Step 1 — SETUP.** The real independent parameters are $u,v$; $\ell$ and $U$ are fixed. The output is real scalar surface area with units of length squared. The band is compact for finite $U$; the full hyperboloid is not.

**Step 2 — CHOICE.** The area is computed from the tangent cross product rather than from a volume Jacobian or a single height graph. The calculation in D3-005 applies with $a=c=\ell$.

**Step 3 — CALCULUS.** The two tangent vectors are

$$
\begin{aligned}
\frac{\partial}{\partial u}\left(\mathbf r(u,v)\right)&=\ell\begin{bmatrix}\sinh u\cos v\\\sinh u\sin v\\\cosh u\end{bmatrix},\\
\frac{\partial}{\partial v}\left(\mathbf r(u,v)\right)&=\ell\begin{bmatrix}-\cosh u\sin v\\\cosh u\cos v\\0\end{bmatrix}.
\end{aligned}
$$

Their cross product is $\ell^2[-\cosh^2u\cos v,-\cosh^2u\sin v,\sinh u\cosh u]^{\mathsf T}$, so its length is $\ell^2\cosh u\sqrt{\cosh^2u+\sinh^2u}$. The length is positive for every finite $u$.

**Step 4 — TRICK: hyperbolic identity.** The real identities are listed in [T-007](TRICKS_APPENDIX.md#t-007-hyperbolic-identities-and-real-branches). Since $\cosh^2u+\sinh^2u=1+2\sinh^2u$,

$$
S(U;\ell)=2\pi\ell^2\int_{-U}^U\cosh u\sqrt{1+2\sinh^2u}\,du.
$$

The coordinate $t=g(u)=\sinh u$ is globally increasing, with derivative $\cosh u>0$. Its bounds are $-T,T$, where the fixed real scalar $T=\sinh U\ge0$.

**Step 5 — CALCULUS.** The transformed integral is $2\pi\ell^2\int_{-T}^T\sqrt{1+2t^2}\,dt$. A further real coordinate $w$ with $t=h(w)=\sinh w/\sqrt2$ gives $\frac{d}{dw}\left(h(w)\right)=\cosh w/\sqrt2$ and $\sqrt{1+2t^2}=\cosh w$. The identity $\cosh^2w=(1+\cosh(2w))/2$ then gives the primitive

$$
B(t)=\frac{t}{2}\sqrt{1+2t^2}+\frac{1}{2\sqrt2}\operatorname{arsinh}(\sqrt2t).
$$

**Step 6 — ALGEBRA.** The function $B(t)$ is odd. Endpoint subtraction yields

$$
S(U;\ell)=2\pi\ell^2\left(T\sqrt{1+2T^2}+\frac{\operatorname{arsinh}(\sqrt2T)}{\sqrt2}\right),\qquad T=\sinh U.
$$

**Step 7 — CHECK AND DOMAIN.** Differentiation of $B(t)$ with respect to $t$ gives $\sqrt{1+2t^2}$, verifying the primitive. At $U=0$ the area is zero, and for small $U$ it behaves as $4\pi\ell^2U$. As $U\to\infty$, $T\to\infty$ and already $T\sqrt{1+2T^2}\to\infty$, so the complete surface has infinite area. The finite-band calculation cannot supply a finite area for the unbounded surface by leaving off its limits.

**Discussion.** A regular surface can have infinite total area. Coordinate smoothness and convergence of an integral over a noncompact domain answer different questions.

### I3-010

**Step 1 — SETUP.** The kernel is nonnegative and has the finite value $a^2$ at zero. Its two useful bounds are

$$
0\le\left(\frac{\sin(ax)}x\right)^2\le a^2,
\qquad
0\le\left(\frac{\sin(ax)}x\right)^2\le\frac1{x^2}\quad(x>0).
$$

The first controls the origin and the second controls infinity, so the integral is absolutely convergent for every fixed real $a$. The output has units of inverse length and is even in $a$. At $a=0$ its value is zero directly.

**Step 2 — CHOICE.** For nonzero $a$, the coordinate $u=|a|x$ preserves orientation and gives

$$
Q(a)=|a|C,\qquad C=\int_0^\infty\frac{\sin^2u}{u^2}\,du.
$$

A parameter derivative is unnecessary for this reduction. Integration by parts converts the squared kernel to the already justified oscillatory integral in I3-003.

**Step 3 — CALCULUS.** On a finite interval $0<\delta<R$, the derivative of $\sin^2u$ is $\sin(2u)$ and a primitive of $u^{-2}$ is $-u^{-1}$. Thus

$$
\int_\delta^R\frac{\sin^2u}{u^2}\,du
=\left.-\frac{\sin^2u}{u}\right|_{u=\delta}^{u=R}
+\int_\delta^R\frac{\sin(2u)}u\,du.
$$

The upper boundary term has absolute value at most $1/R$. At the lower boundary, $\sin^2\delta/\delta\le\delta$. Both terms vanish in the corresponding limits. The ordinary sine integral, whose convergence follows from the uniform tail estimate in I3-003, is $\pi/2$. Therefore $C=\pi/2$.

**Step 4 — RESULT AND ALGEBRA.** The complete answer and its derivatives away from zero are

$$
Q(a)=\frac\pi2|a|,\qquad
\frac{d}{da}(Q(a))=
\begin{cases}\pi/2,&a>0,\\-\pi/2,&a<0.\end{cases}
$$

The right difference quotient at zero is $\pi/2$ and the left one is $-\pi/2$. The function is continuous at zero but is not differentiable there.

**Step 5 — DOMAIN: the parameter derivative.** For each fixed $x>0$, differentiation of the kernel gives $\sin(2ax)/x$, with limiting value $2a$ at $x=0$. If $a\ne0$, its ordinary improper integral is $\pi\operatorname{sgn}(a)/2$, agreeing with the evaluated derivative. Here $\operatorname{sgn}(a)$ equals one for positive $a$ and minus one for negative $a$.

This derivative integral is conditionally, rather than absolutely, convergent. Nevertheless, differentiation can be justified locally away from zero. For $A>0$, integration by parts against a bounded cosine primitive gives

$$
\left|\int_A^\infty\frac{\sin(2ax)}x\,dx\right|
\le\frac1{|a|A}.
$$

On a neighborhood of a fixed $a_0\ne0$, $|a|\ge|a_0|/2$, so these derivative tails converge uniformly. Finite-interval differentiation followed by this uniform tail limit is valid. At zero that argument fails: the pointwise kernel derivative is zero, but the integral has no two-sided derivative. There is also no integrable absolute domination of all derivative kernels near zero. For any fixed $b>0$ and $x\ge\pi/(4b)$, the admissible choice $a=\pi/(4x)$ gives $|\sin(2ax)|/x=1/x$.

**Step 6 — CHECK.** For a finite positive cutoff $L$, positivity and the tail bound give the directly usable estimate

$$
0\le Q(a)-\int_0^L\left(\frac{\sin(ax)}x\right)^2\,dx\le\frac1L.
$$

As a separate finite-interval check, the expansion $\sin(ax)/x=a+O(a^3x^2)$ at fixed $L$ gives the truncated integral $a^2L+O(a^4L^3)$ as $a\to0$. It has zero slope at zero, while the full integral has a cusp. The missing behavior comes from lengths comparable to $1/|a|$, which leave every fixed finite integration interval.

**Discussion.** Absolute convergence of an integral does not ensure absolute convergence of its parameter derivative. A nonzero-parameter interchange may be justified by oscillatory tails while failing at an exceptional parameter.

### I3-011

**Step 1 — SETUP.** The logarithm is real on $0<x\le1$, and the integrand is nonnegative. Its only unbounded endpoint is zero. Since $1/(1+x)\le1$, convergence follows from $\int_0^1\ln^2x\,dx=2$, evaluated below. No principal-value prescription is involved.

**Step 2 — CHOICE.** A finite geometric expansion retains an exact remainder, so the endpoint and truncation error can be controlled before an infinite sum is introduced. For a positive integer $N$,

$$
\frac1{1+x}=\sum_{n=0}^{N-1}(-1)^nx^n+(-1)^N\frac{x^N}{1+x}.
$$

**Step 3 — CALCULUS.** For an integer $n\ge0$, put $x=\exp(-t)$, with inverse differential $dx=-\exp(-t)\,dt$. The bounds reverse from $t=\infty$ to zero, and

$$
\int_0^1x^n\ln^2x\,dx
=\int_0^\infty t^2\exp(-(n+1)t)\,dt
=\frac{2}{(n+1)^3}.
$$

For the last equality, integration by parts first replaces the integral by $2/(n+1)$ times $\int_0^\infty t\exp(-(n+1)t)\,dt$; a second integration by parts gives $1/(n+1)^2$. All boundary terms vanish because the exponential dominates these fixed powers of $t$.

**Step 4 — ALGEBRA: exact remainder.** Multiplication of the finite identity by $\ln^2x$ and integration give

$$
M=S_N+(-1)^NR_N,\qquad
S_N=2\sum_{m=1}^N\frac{(-1)^{m-1}}{m^3},\qquad
R_N=\int_0^1\frac{x^N\ln^2x}{1+x}\,dx.
$$

The remainder is positive and has the explicit bound

$$
0<R_N\le\int_0^1x^N\ln^2x\,dx=\frac{2}{(N+1)^3}.
$$

Thus an even partial sum underestimates $M$ and an odd partial sum overestimates it. The displayed bound is valid for every positive integer $N$.

**Step 5 — DOMAIN: sum and integral.** In the open interval $0<x<1$ the infinite geometric expansion converges pointwise. Its terms are absolutely summable after integration, because

$$
\sum_{n=0}^\infty\int_0^1|(-1)^nx^n\ln^2x|\,dx
=2\sum_{m=1}^\infty\frac1{m^3}<\infty.
$$

The last series converges by comparison with $\int_1^\infty t^{-3}\,dt$. Absolute integrability of the term series justifies exchanging the sum and integral. The single endpoint $x=1$ does not affect that conclusion. Equivalently, the exact finite remainder tends to zero and establishes the same limit without an interchange theorem.

Define the real constant $\zeta(3)=\sum_{m=1}^\infty m^{-3}$. The even terms of this positive series sum to $\zeta(3)/8$, and its odd terms sum to $7\zeta(3)/8$. Their difference yields

$$
M=2\sum_{m=1}^\infty\frac{(-1)^{m-1}}{m^3}
=\frac32\zeta(3)\approx1.8030853547.
$$

**Step 6 — CHECK: a different integral.** The same coordinate $x=\exp(-t)$ applied directly to the original kernel, without expanding it, gives

$$
M=\int_0^\infty\frac{t^2}{\exp t+1}\,dt.
$$

This integrand is regular at zero and decays exponentially at infinity. For every real cutoff $T>0$ its omitted positive tail satisfies

$$
0\le\int_T^\infty\frac{t^2}{\exp t+1}\,dt
\le\int_T^\infty t^2\exp(-t)\,dt
=\exp(-T)(T^2+2T+2).
$$

Quadrature of this nonsingular representation agrees with the alternating sum within the stated errors. Independently, $1/2\le1/(1+x)\le1$ gives $1\le M\le2$, consistent with the answer.

**Discussion.** A logarithmically singular endpoint need not prevent a useful series calculation. Integrating absolute term bounds or retaining a finite exact remainder supplies the justification that a formal geometric expansion alone lacks.

### I3-012

**Step 1 — SETUP.** For every fixed $a>0$, the real kernel is smooth and positive throughout the compact interval. Its value at the endpoint $x=0$ is $1/a$, which is finite for that fixed parameter but grows as $a\downarrow0$.

**Step 2 — CHOICE.** The coordinate $u=x/a$ measures distance in units of the parameter. Its inverse is $x=au$, with positive derivative $a$ and transformed bounds zero to $1/a$.

**Step 3 — CALCULUS.** Substitution gives

$$
F(a)=\int_0^{1/a}\frac1{1+u^2}\,du
=\arctan(1/a)=\frac\pi2-\arctan a,\qquad a>0.
$$

The second identity uses the principal real arctangent and positivity of $a$. Therefore $\lim_{a\downarrow0}F(a)=\pi/2$.

**Step 4 — DOMAIN: where the contribution lies.** At each fixed $x>0$, the original kernel tends to zero. Its almost-everywhere pointwise limit has integral zero; the unbounded value at the single endpoint does not supply a nonzero area. To see the concentration explicitly, for fixed $c>0$ and $ca\le1$,

$$
\int_0^{ca}\frac{a}{x^2+a^2}\,dx=\arctan c.
$$

As $a\downarrow0$ this shrinking interval retains the fraction $2\arctan(c)/\pi$ of the limiting total. For any fixed $0<\delta<1$, the complementary fixed interval obeys

$$
0\le\int_\delta^1\frac{a}{x^2+a^2}\,dx
\le a\int_\delta^1\frac1{x^2}\,dx
=a\left(\frac1\delta-1\right)\longrightarrow0.
$$

A fixed multiple $ca$ does not capture all the mass: the limiting remainder beyond it is $\pi/2-\arctan c$, which tends to zero only as $c\to\infty$. An integrable majorant independent of $a$ near zero is unavailable. For $0<x<b$, maximization over $0<a\le b$ includes $a=x$ and gives the nonintegrable envelope $1/(2x)$.

**Step 5 — CALCULUS: differentiation at positive distance.** Around any fixed $a_0>0$, the kernel and its $a$ derivative are continuous on a compact rectangle with $a\ge a_0/2$. Differentiation under the integral is justified there:

$$
\begin{aligned}
\frac{d}{da}(F(a))
&=\int_0^1\frac{x^2-a^2}{(x^2+a^2)^2}\,dx\\
&=\left.-\frac{x}{x^2+a^2}\right|_{x=0}^{x=1}
=-\frac1{1+a^2}.
\end{aligned}
$$

This agrees with differentiation of the arctangent form. For each fixed $x>0$ the derivative kernel tends to $1/x^2$, whose integral diverges. Interchanging this limit and integral would therefore fail as well, even though $\lim_{a\downarrow0}\frac{d}{da}(F(a))=-1$ is finite.

**Step 6 — ALGEBRA: a controlled local expansion.** For $0\le t\le a$, the exact identity

$$
\frac1{1+t^2}=1-t^2+\frac{t^4}{1+t^2}
$$

gives

$$
F(a)=\frac\pi2-a+\frac{a^3}{3}+E(a),\qquad
E(a)=-\int_0^a\frac{t^4}{1+t^2}\,dt,\qquad
-\frac{a^5}{5}\le E(a)\le0.
$$

In particular this supplies a small-parameter approximation through the cubic term with an explicit error bound, rather than only a formal expansion.

**Step 7 — CHECK AND EXTENSION.** The continuous scalar extension has $F(0)=\pi/2$ and right derivative $-1$, as the expansion shows. Assigning the kernel its pointwise value zero for $a=0$ and $x>0$ instead gives an integral equal to zero; any assigned value at $x=0$ leaves that integral unchanged. That assignment does not produce the continuous extension of the integrated function. At the ordinary parameter value $a=1$, the original integral and the formula both give $\pi/4$, while the derivative gives $-1/2$.

**Discussion.** A parameter can move an order-one contribution into a region whose width tends to zero. The integrated function can have a smooth one-sided extension even when pointwise parameter substitution loses that contribution.

### I3-013

**Step 1 — SETUP.** The field is smooth wherever $x^2+y^2>0$. Both stated curves remain in that domain. The ellipse encloses the excluded axis; the displaced circle and its planar disk have $x\ge d-R>0$. Their positive boundary orientation corresponds to the upward normal $\mathbf e_z=[0,0,1]^{\mathsf T}$.

**Step 2 — CHOICE.** Direct parameterization computes the ellipse's circulation without crossing the axis. The curl calculation then determines where Stokes' theorem can be used, while excision supplies a second argument for the path whose spanning disk meets the singularity.

**Step 3 — CALCULUS: the centered ellipse.** Its tangent vector is $[-A\sin\theta,B\cos\theta,0]^{\mathsf T}$, so

$$
\mathbf F(\mathbf r_E(\theta))\cdot\frac{d}{d\theta}(\mathbf r_E(\theta))
=\frac{AB}{A^2\cos^2\theta+B^2\sin^2\theta}.
$$

The four quadrant contributions are equal. In the first quadrant the real coordinate $t=\tan\theta$ has inverse derivative $1/(1+t^2)$ and bounds zero to infinity. Hence

$$
\begin{aligned}
\oint_E\mathbf F\cdot d\mathbf r
&=4\int_0^\infty\frac{AB}{A^2+B^2t^2}\,dt\\
&=4\lim_{T\to\infty}\arctan\left(\frac BA T\right)
=2\pi.
\end{aligned}
$$

The apparent improper bound comes from the angular coordinate; the original line integrand is continuous and bounded.

**Step 4 — ALGEBRA AND DOMAIN: the curl.** Write $D=x^2+y^2>0$. All $z$ derivatives vanish, and

$$
\frac{\partial}{\partial x}\left(\frac{x}{D}\right)
=\frac{y^2-x^2}{D^2},\qquad
\frac{\partial}{\partial y}\left(-\frac{y}{D}\right)
=\frac{y^2-x^2}{D^2}.
$$

Consequently $\nabla\times\mathbf F=\mathbf0$ throughout its domain. The ellipse's full spanning disk contains a point on the excluded axis, so the field is not continuously differentiable on a neighborhood of that disk. Applying the classical Stokes theorem to that disk would violate its hypotheses.

The displaced disk lies strictly in $x>0$, where those hypotheses hold. Its curl flux is zero, so

$$
\oint_C\mathbf F\cdot d\mathbf r=0.
$$

**Step 5 — CHECK: a single angle on the displaced path.** Direct parameterization gives

$$
\mathbf F(\mathbf r_C(\theta))\cdot\frac{d}{d\theta}(\mathbf r_C(\theta))
=\frac{R^2+dR\cos\theta}{d^2+R^2+2dR\cos\theta}.
$$

Because $d+R\cos\theta>0$, one continuous real angle is

$$
\phi(\theta)=\arctan\left(\frac{R\sin\theta}{d+R\cos\theta}\right).
$$

The quotient inside it has derivative $(dR\cos\theta+R^2)/(d+R\cos\theta)^2$. Multiplication by the arctangent derivative gives exactly the displayed line integrand. Therefore its integral is $\phi(2\pi)-\phi(0)=0$, independently confirming the disk calculation.

**Step 6 — CHECK: excision and orientation.** Choose a real radius $0<\rho<\min(A,B)$ and remove the centered disk of radius $\rho$ from the ellipse's interior at height $z_0$. On the remaining surface the field is smooth and its curl is zero. The induced boundary consists of the outer ellipse counterclockwise and the inner circle clockwise. Stokes' theorem gives

$$
0=\oint_E\mathbf F\cdot d\mathbf r
-\oint_{\rho\text{ circle, counterclockwise}}\mathbf F\cdot d\mathbf r.
$$

On that centered circle the line integrand equals one, so its counterclockwise circulation is $2\pi$. This recovers the ellipse's value. Reversing either curve's orientation negates its circulation.

**Discussion.** A zero curl is a local statement on the field's domain. Computing circulation from a spanning surface also requires that the entire surface avoid excluded sources, with every boundary component oriented consistently.

### I3-014

**Step 1 — SETUP AND DOMAIN.** The source is strictly inside the panel, and the integrand is nonnegative away from it. The portion of the panel inside a disk of real radius $\epsilon>0$ centered at the source contributes at most

$$
\int_0^{2\pi}\int_0^\epsilon\frac1r\,r\,dr\,d\theta=2\pi\epsilon.
$$

The area singularity is therefore locally integrable. Away from that disk the integrand is continuous on a compact set, so the complete integral is finite. Nonnegativity permits monotone exhaustions of the source, without a signed cancellation prescription.

**Step 2 — CHOICE: a source-centered partition.** The counterclockwise vertices are

$$
\mathbf v_1=\begin{bmatrix}0\\0\end{bmatrix},\quad
\mathbf v_2=\begin{bmatrix}1\\0\end{bmatrix},\quad
\mathbf v_3=\begin{bmatrix}1\\1\end{bmatrix},\quad
\mathbf v_4=\mathbf v_1.
$$

Joining $\mathbf p$ to these vertices creates three subtriangles with disjoint interiors. On subtriangle $j$, for $j=1,2,3$, define fixed real columns $\mathbf a_j=\mathbf v_j-\mathbf p$ and $\mathbf e_j=\mathbf v_{j+1}-\mathbf v_j$. Independent real coordinates $0<u\le1$, $0\le v\le1$ give the map

$$
\mathbf r_j(u,v)=\mathbf p+u(\mathbf a_j+v\mathbf e_j).
$$

The source corresponds to the collapsed edge $u=0$, while $u=1$ traces the outer edge. For $u>0$ the map is one-to-one in the subtriangle interior.

**Step 3 — CALCULUS: all three Jacobians.** The two Jacobian columns are $\mathbf a_j+v\mathbf e_j$ and $u\mathbf e_j$. Define the fixed positive scalar $d_j=\det(\mathbf a_j,\mathbf e_j)$. Then

$$
\det\mathbf J_j(u,v)
=u\det(\mathbf a_j+v\mathbf e_j,\mathbf e_j)=ud_j.
$$

The actual edge data and determinants are

$$
\begin{aligned}
\mathbf a_1&=\begin{bmatrix}-x_0\\-y_0\end{bmatrix},&
\mathbf e_1&=\begin{bmatrix}1\\0\end{bmatrix},&d_1&=y_0>0,\\
\mathbf a_2&=\begin{bmatrix}1-x_0\\-y_0\end{bmatrix},&
\mathbf e_2&=\begin{bmatrix}0\\1\end{bmatrix},&d_2&=1-x_0>0,\\
\mathbf a_3&=\begin{bmatrix}1-x_0\\1-y_0\end{bmatrix},&
\mathbf e_3&=\begin{bmatrix}-1\\-1\end{bmatrix},&d_3&=x_0-y_0>0.
\end{aligned}
$$

Here $\mathbf J_j$ is a real $2\times2$ matrix. Positivity of all three determinants records that the source lies to the left of each oriented outer edge.

**Step 4 — ALGEBRA: cancellation at the source.** Since $u>0$,

$$
\|\mathbf r_j(u,v)-\mathbf p\|=u\|\mathbf a_j+v\mathbf e_j\|.
$$

On a truncated subtriangle $u\ge\delta>0$, the ordinary change-of-variables theorem applies. Multiplication by its area Jacobian cancels the radial factor:

$$
K_j=\lim_{\delta\downarrow0}\int_\delta^1\int_0^1
\frac{ud_j}{u\|\mathbf a_j+v\mathbf e_j\|}\,dv\,du
=d_j\int_0^1\frac1{\|\mathbf a_j+v\mathbf e_j\|}\,dv.
$$

The removed sets shrink to the source, and the nonnegative integrals increase to the full subtriangle integrals. Boundaries shared by the pieces have zero area, so $K=K_1+K_2+K_3$.

**Step 5 — CALCULUS: explicit nonsingular edge integrals.** Write the fixed positive edge length as $L_j=\|\mathbf e_j\|$ and the perpendicular source-to-edge distance as $h_j=d_j/L_j>0$. The tangential coordinate of the initial edge point is $t_j=\mathbf a_j\cdot\mathbf e_j/L_j$. Orthogonal decomposition gives

$$
\|\mathbf a_j+v\mathbf e_j\|
=\sqrt{h_j^2+(t_j+L_jv)^2}.
$$

The real coordinate $s=t_j+L_jv$ has derivative $L_j>0$, so

$$
K_j=h_j\left(
\operatorname{arsinh}\left(\frac{t_j+L_j}{h_j}\right)
-\operatorname{arsinh}\left(\frac{t_j}{h_j}\right)\right).
$$

These formulas are real and finite because every $h_j$ is strictly positive. In fact $\|\mathbf a_j+v\mathbf e_j\|\ge h_j$, so each original edge integrand $d_j/\|\mathbf a_j+v\mathbf e_j\|$ is bounded above by $L_j$ on its closed interval.

**Step 6 — RESULT.** Substituting the three edge data gives

$$
\begin{aligned}
K_1&=y_0\left(\operatorname{arsinh}\left(\frac{1-x_0}{y_0}\right)
+\operatorname{arsinh}\left(\frac{x_0}{y_0}\right)\right),\\
K_2&=(1-x_0)\left(\operatorname{arsinh}\left(\frac{1-y_0}{1-x_0}\right)
+\operatorname{arsinh}\left(\frac{y_0}{1-x_0}\right)\right).
\end{aligned}
$$

For the diagonal edge define fixed real scalars $d=x_0-y_0>0$ and $s=x_0+y_0$. Its contribution is

$$
K_3=\frac d{\sqrt2}\left(\operatorname{arsinh}\left(\frac{s}{d}\right)
+\operatorname{arsinh}\left(\frac{2-s}{d}\right)\right),
\qquad K(x_0,y_0)=K_1+K_2+K_3.
$$

The inverse hyperbolic sine here is its real branch, $\operatorname{arsinh}(w)=\ln(w+\sqrt{1+w^2})$. No complex branch choice is needed. The whole answer is positive and obeys $K\le L_1+L_2+L_3=2+\sqrt2$, from the edge-integrand bounds.

**Step 7 — CHECK: independent Cartesian integration.** For every fixed $x\ne x_0$, direct integration in $y$ over $0\le y\le x$ gives

$$
G(x)=\operatorname{arsinh}\left(\frac{x-y_0}{|x-x_0|}\right)
+\operatorname{arsinh}\left(\frac{y_0}{|x-x_0|}\right).
$$

Thus $K=\int_0^1G(x)\,dx$. The logarithmic divergence at $x=x_0$ is integrable; it is not evaluated as a finite inner integral there. For stable numerical comparison, use $x=x_0-x_0t^2$ on the left and $x=x_0+(1-x_0)t^2$ on the right, with $0\le t\le1$. Both resulting integrands extend to zero at $t=0$, since $t|\ln t|\to0$. This Cartesian reduction is independent of the three source-edge maps and agrees with their answer.

Reflection $(x,y)\mapsto(1-y,1-x)$ also preserves the triangle and distance, so $K(x_0,y_0)=K(1-y_0,1-x_0)$. The explicit formula exchanges $K_1,K_2$ and leaves $K_3$ unchanged under that reflection. At the centroid $(x_0,y_0)=(2/3,1/3)$ it simplifies to

$$
K\left(\frac23,\frac13\right)
=\frac23\left(\operatorname{arsinh}(2)+\operatorname{arsinh}(1)\right)
+\frac{\sqrt2}{3}\operatorname{arsinh}(3).
$$

**Discussion.** An interior source requires several maps with the source at their common collapsed edge. Their positive Jacobians cancel the weak radial singularity while retaining the distinct geometry of each outer edge.

## Application references

The problems and solutions here are original. The real sine integral is defined
in [NIST DLMF, Section 6.2](https://dlmf.nist.gov/6.2).
The singular-panel example illustrates a basic coordinate mechanism related to
[Reid, Johnson, and White, Generalized Taylor-Duffy Method for Efficient Evaluation of Galerkin Integrals in Boundary-Element Method Computations](https://arxiv.org/abs/1312.1703).
That paper concerns more general CEM integrals than this single-triangle model.
The geometric measure conventions follow the change-of-variables framework in
[MIT, Calculus with Applications, Section 24.2](https://ocw.mit.edu/ans7870/18/18.013a/textbook/chapter24/section02.html).
