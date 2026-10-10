# I3 · Oscillation, singularities, and curved domains

The existence of an integral is part of the problem. Oscillation can produce
conditional convergence, a coordinate map can fold an interval onto itself,
and a singular kernel can become integrable because of the area or volume
measure. A formal antiderivative does not settle any of these questions.
The first example uses an elementary sine; the later examples connect the
same care with domains to RF field integrals and curved geometry.

## Rules and conventions

A finite integral of a continuous scalar function is an ordinary integral.
At an excluded point, an improper integral is defined by separate one-sided
limits. A Cauchy principal value instead prescribes a coupled, symmetric
limiting process; it is identified explicitly and is not substituted for an
ordinary integral without a reason.

For a real coordinate map from $(u,v)$ to $(x(u,v),y(u,v))$, the Jacobian matrix
is the $2\times2$ matrix of coordinate partial derivatives. The area factor is
the absolute value of its determinant. In three dimensions the volume factor
is the absolute determinant of the $3\times3$ coordinate Jacobian. A surface
map $\mathbf r(u,v)\in\mathbb R^3$ instead has area factor
$\|\frac{\partial}{\partial u}(\mathbf r(u,v))\times\frac{\partial}{\partial v}(\mathbf r(u,v))\|$.
These factors measure different objects.

## Problems

### I3-001 — Why a sine substitution can erase a nonzero integral

**Objects and dependencies.** $x\in[0,\pi]$ is an independent real scalar angle in radians and the integration variable. The real scalar integrand is $q(x)=\sin x$. Evaluate $\int_0^\pi q(x)\,dx$ using $u=g(x)=\sin x$. Explain why replacing both endpoints by $u=0$ in one integral gives a false answer.

### I3-002 — A sine integral with a removable singularity

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

### I3-005 — A pole inside the interval: improper integral or principal value

**Objects and dependencies.** $x$ is a dimensionless real integration coordinate on $[-1,1]$. A fixed real scalar $a$ satisfies $-1<a<1$. The real scalar function $q(x;a)=1/(x-a)$ is undefined at $x=a$. Determine whether $\int_{-1}^1q(x;a)\,dx$ exists as an ordinary improper integral, and evaluate its Cauchy principal value with equal exclusions $a-\delta,a+\delta$ for real $\delta>0$ small enough. Describe what happens when $a$ is an endpoint.

### I3-006 — Near a line source: differentiation under an integral

**Objects and dependencies.** $s\in[-L,L]$ is a real scalar source coordinate, with fixed real length $L>0$. The independent real scalar observation distance is $\rho>0$. The real dimensionless scalar kernel integral is

$$
P(\rho;L)=\int_{-L}^L\frac{1}{\sqrt{\rho^2+s^2}}\,ds.
$$

Evaluate $P(\rho;L)$, find $\frac{d}{d\rho}(P(\rho;L))$ both from the closed form and under the integral sign, and describe the limit $\rho\downarrow0$. A constant charge and permittivity prefactor would convert $P$ into an electrostatic potential.

### I3-007 — A weakly singular CEM panel integral

**Objects and dependencies.** Independent real dimensionless coordinates $x,y$ describe the triangle $T=\{(x,y):0\le y\le x\le1\}$. The real scalar integrand is $q(x,y)=1/\sqrt{x^2+y^2}$ away from $(0,0)$. Evaluate

$$
K=\int_0^1\int_0^x\frac{1}{\sqrt{x^2+y^2}}\,dy\,dx
$$

as a nonnegative improper area integral using $x=u$, $y=uv$. The new independent real coordinates satisfy $0<u\le1$, $0\le v\le1$. Find the Jacobian explicitly. Compare this with replacing the denominator by $x^2+y^2$.

### I3-008 — A Gaussian-weighted integral inside an ellipsoid

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

**Step 5 — CHECK.** Direct integration gives $[-\cos x]_0^\pi=2$. Nonnegative area cannot vanish merely because a coordinate returns to its initial value. By contrast, $\int_0^\pi\sin x\cos x\,dx=0$ legitimately follows from the direct chain-rule substitution, which does not require an inverse map.

**Recognition cue.** Equal transformed endpoints are meaningful only after the transformed integrand and the applicable substitution theorem have been identified. A folding coordinate map can conceal multiplicity and orientation.

### I3-002

**Step 1 — SETUP.** $x$ is a real length coordinate, $k$ and $L$ are fixed, and the integral is a real dimensionless scalar. The defining formula at $x>0$ has a continuous extension $q(0;k)=k$, including $k=0$.

**Step 2 — CHOICE.** The numerator's derivative does not match a substitution that turns this into an elementary sine primitive. The ratio leads to a special function instead. For $k\ne0$, $u=kx$ is a valid invertible linear coordinate.

**Step 3 — CALCULUS.** Its derivative is $du/dx=k$, its inverse derivative is $dx/du=1/k$, and its bounds are $u=0$ to $u=kL$. Thus

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

**Recognition cue.** A familiar sine inside a ratio need not have an elementary antiderivative. A special-function definition and a controlled approximation are valid, distinct forms of a solution.

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

**Recognition cue.** Oscillatory cancellation can make an integral converge without absolute convergence. A limit at the edge of a parameter domain needs its own argument.

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

**Step 5 — ALGEBRA.** Define the real scalar function $\operatorname{sinc}_0(s)=\sin(s)/s$ for $s\ne0$, with $\operatorname{sinc}_0(0)=1$. The subscript distinguishes this unnormalized convention from $\sin(\pi s)/(\pi s)$. Then

$$
A(\Delta;L)=L\exp(\mathrm{i}\Delta L/2)\operatorname{sinc}_0(\Delta L/2),\qquad
|A(\Delta;L)|=L|\operatorname{sinc}_0(\Delta L/2)|.
$$

**Step 6 — CHECK.** The limiting value at zero is $L$, and $|A|\le L$ follows independently from the triangle inequality for the original integral. The exponential locates the phase center at the midpoint; when the real sinc factor is negative it contributes an additional phase of $\pi$. At its zeros the amplitude is zero and its phase is undefined.

**Recognition cue.** A quotient singularity introduced by a parameterized antiderivative may be removable even though the formula with division is undefined there. Phase still needs separate treatment at amplitude zeros.

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

**Recognition cue.** Cancellation of divergences is a prescription, not proof that an ordinary improper integral exists. Symmetry is useful only after the definition of the integral is fixed.

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

**Recognition cue.** A near-source limit can invalidate interchange rules that are harmless at every fixed positive observation distance. Parameter-dependent transformed bounds cannot be treated as constants in a later derivative.

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

**Recognition cue.** The word singular does not determine integrability. The kernel, the dimension of the integration measure, and the coordinate Jacobian must be considered together.

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

The coordinate singularities at the center, poles, and seam occupy sets of zero volume; the map is regular and one-to-one in the interior away from those sets.

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

**Recognition cue.** A nonlinear integrand can become radial after a linear geometric change. The Jacobian supplies the volume scale and the radial power; dropping either changes the problem.

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

**Step 5 — CALCULUS.** The transformed integral is $2\pi\ell^2\int_{-T}^T\sqrt{1+2t^2}\,dt$. A further real coordinate $w$ with $t=\sinh w/\sqrt2$ gives $dt/dw=\cosh w/\sqrt2$ and $\sqrt{1+2t^2}=\cosh w$. The identity $\cosh^2w=(1+\cosh(2w))/2$ then gives the primitive

$$
B(t)=\frac{t}{2}\sqrt{1+2t^2}+\frac{1}{2\sqrt2}\operatorname{arsinh}(\sqrt2t).
$$

**Step 6 — ALGEBRA.** The function $B(t)$ is odd. Endpoint subtraction yields

$$
S(U;\ell)=2\pi\ell^2\left(T\sqrt{1+2T^2}+\frac{\operatorname{arsinh}(\sqrt2T)}{\sqrt2}\right),\qquad T=\sinh U.
$$

**Step 7 — CHECK AND DOMAIN.** Differentiation of $B(t)$ with respect to $t$ gives $\sqrt{1+2t^2}$, verifying the primitive. At $U=0$ the area is zero, and for small $U$ it behaves as $4\pi\ell^2U$. As $U\to\infty$, $T\to\infty$ and already $T\sqrt{1+2T^2}\to\infty$, so the complete surface has infinite area. The finite-band calculation cannot supply a finite area for the unbounded surface by leaving off its limits.

**Recognition cue.** A regular surface can have infinite total area. Coordinate smoothness and convergence of an integral over a noncompact domain answer different questions.

## Application references

The problems and solutions here are original. The real sine integral is defined
in [NIST DLMF, Section 6.2](https://dlmf.nist.gov/6.2).
The singular-panel example illustrates a basic coordinate mechanism related to
[Reid, Johnson, and White, Generalized Taylor-Duffy Method for Efficient Evaluation of Galerkin Integrals in Boundary-Element Method Computations](https://arxiv.org/abs/1312.1703).
That paper concerns more general CEM integrals than this single-triangle model.
The geometric measure conventions follow the change-of-variables framework in
[MIT, Calculus with Applications, Section 24.2](https://ocw.mit.edu/ans7870/18/18.013a/textbook/chapter24/section02.html).
