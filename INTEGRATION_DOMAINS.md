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

### I3-015 — A logarithmic kernel with a moving interior pole

**Objects and dependencies.** $x\in(0,1]$ is a dimensionless real integration coordinate and the fixed real scalar pole location satisfies $0<a<1$. Define the real Cauchy principal value by equal coordinate exclusions,

$$
J(a)=\lim_{\delta\downarrow0}\left(
\int_0^{a-\delta}\frac{\ln x}{x-a}\,dx
+\int_{a+\delta}^1\frac{\ln x}{x-a}\,dx\right),
\qquad 0<\delta<\min(a,1-a).
$$

Determine whether the ordinary improper integral exists, evaluate $J(a)$ in terms of a real dilogarithm defined locally, and find both limits $a\downarrow0$ and $a\uparrow1$. Compare them with the ordinary endpoint integrals obtained by placing the pole exactly at zero or one. The logarithmic endpoint at $x=0$ is approached independently of the symmetric exclusion at the interior pole.

### I3-016 — Surface area with three unequal semiaxes

**Objects and dependencies.** Fixed real lengths satisfy $a>b>c>0$. The real ellipsoid is $x^2/a^2+y^2/b^2+z^2/c^2=1$. Its surface area $S(a,b,c)$ is a real scalar with units of length squared. Obtain an explicit bounded quadrature on a finite rectangle, deriving its surface measure from a parameterization. Account for the coordinate poles and angular seam. Give upper and lower bounds, verify the spherical limit, and supply an explicit rigorous error bound for a rectangular composite midpoint approximation so that a requested numerical accuracy can be checked.

### I3-017 — A circular source observed away from its axis

**Objects and dependencies.** The fixed real ring radius is $a>0$. The real observation parameters satisfy $\rho\ge0$ and $z\in\mathbb R$; $(\rho,z)=(a,0)$ is excluded. The integration coordinate is the dimensionless real angle $0\le\theta\le2\pi$. Evaluate the real scalar kernel integral

$$
P(\rho,z;a)=\int_0^{2\pi}\frac{1}{\sqrt{a^2+\rho^2+z^2-2a\rho\cos\theta}}\,d\theta
$$

using a complete elliptic integral whose convention is defined explicitly. Find the on-axis value and the leading logarithmic behavior, with its coefficient, as the distance $\sqrt{(\rho-a)^2+z^2}$ to the ring tends to zero. Distinguish the parameter of an elliptic integral from its modulus and justify the singular asymptotic used.

### I3-018 — A panel with a linearly varying weight

**Objects and dependencies.** Independent real dimensionless coordinates describe $T=\{(x,y):0\le y\le x\le1\}$. The real scalars $\alpha,\beta,\gamma$ are fixed and need not be positive. The independent real observation distance is $h\ge0$. Define the real scalar

$$
L(h;\alpha,\beta,\gamma)=\iint_T
\frac{\alpha+\beta x+\gamma y}{\sqrt{x^2+y^2+h^2}}\,dx\,dy.
$$

At $h=0$ the origin is excluded and the integral is interpreted as an absolutely convergent improper integral when it exists. Evaluate all three zero-distance moments exactly. For positive $h$, reduce the calculation to nonsingular one-dimensional quadrature by performing the radial integrations explicitly. Determine the right derivative at zero and give a quantitative bound explaining how vanishing weight at the vertex changes the local regularity. State when taking a parameter derivative under the original area integral at zero is justified.

### I3-019 — A finite aperture with quadratic phase

**Objects and dependencies.** The fixed real half-length is $a>0$, the independent real parameter satisfies $k>0$ and has units of inverse length squared, and $x\in[-a,a]$ is a real integration coordinate. The complex scalar amplitude is

$$
I(k;a)=\int_{-a}^a\exp(\mathrm{i}kx^2)\,dx,\qquad \mathrm{i}^2=-1.
$$

Give an exact representation in terms of Fresnel functions defined locally. For fixed $a$ and large $k$, obtain the leading stationary contribution and the first endpoint contribution with an explicit error bound. Justify the ordinary oscillatory integral and any Gaussian-damping limit used in this derivation. An integration by parts that divides by $x$ across the stationary point $x=0$ is not valid. Check the exact representation in the small-$k$ limit as well.

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

### I3-015

1. Subtract $\ln a$ from the numerator before treating the pole; the resulting quotient has a removable value at $x=a$.
2. The coordinate $t=x/a$ turns the regularized numerator into $\ln t$. A primitive of $\ln t/(t-1)$ is a real dilogarithm with argument $1-t$.
3. Differentiating suitable combinations of dilogarithms proves the identities needed to expose the endpoint limits without complex logarithms.

### I3-016

1. Apply the diagonal map with entries $a,b,c$ to the unit-sphere parameterization and calculate its tangent cross product.
2. The angular factor is the norm of $\operatorname{diag}(bc,ac,ab)$ applied to a unit vector. Reflection symmetry reduces the sphere to one octant.
3. Bound the first angular derivatives of that norm using its largest diagonal entry. The integral of distance from the center of an interval of width $\Delta$ is $\Delta^2/4$.

### I3-017

1. Rewrite the squared denominator using the half-angle identity and $(a+\rho)^2+z^2$.
2. The elliptic parameter is $m=4a\rho/((a+\rho)^2+z^2)$, and its complementary quantity has a direct geometric meaning.
3. The complete elliptic integral grows logarithmically as its complementary modulus tends to zero. Convert its convention before applying an asymptotic formula.

### I3-018

1. The map $x=u$, $y=uv$ makes the numerator affine in $u$ and contributes the area factor $u$.
2. The two radial integrals have numerators $u$ and $u^2$ over $\sqrt{(1+v^2)u^2+h^2}$. The second involves an inverse hyperbolic sine.
3. A nonzero constant weight contributes a term linear in $h$. The linear weights instead give a remainder bounded by a constant times $h^2\ln(1/h)$.

### I3-019

1. The phase is even. Rescale $x$ so that the exponent is $\mathrm{i}\pi t^2/2$ to identify the exact Fresnel convention.
2. For the complete real-line integral, positive Gaussian damping permits a parameter differential equation. Uniform oscillatory tail bounds justify removing that damping.
3. Subtract the two tails beyond $a$ from the complete integral. Integration by parts is then safe because $x$ is bounded away from zero, and a second tail estimate controls the error.

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

### I3-015

**Step 1 — SETUP AND DOMAIN.** For a fixed interior $a$, the logarithm is integrable at zero because $x-a$ stays bounded away from zero there. At the pole the numerator tends to the nonzero number $\ln a<0$. The left one-sided integral diverges to $+\infty$ and the right one diverges to $-\infty$. The ordinary improper integral therefore does not exist. The equal-exclusion prescription in the statement is needed to assign a principal value.

**Step 2 — CHOICE.** Subtract the pole's numerator value:

$$
\frac{\ln x}{x-a}
=\frac{\ln a}{x-a}+\frac{\ln x-\ln a}{x-a}.
$$

The second quotient extends continuously to $1/a$ at $x=a$. Its only remaining unbounded endpoint is the integrable logarithm at zero. The first term has the elementary symmetric principal value

$$
\operatorname{PV}\int_0^1\frac{\ln a}{x-a}\,dx
=\ln a\ln\left(\frac{1-a}{a}\right).
$$

Consequently

$$
J(a)=\ln a\ln\left(\frac{1-a}{a}\right)
+\int_0^1\frac{\ln x-\ln a}{x-a}\,dx.
$$

**Step 3 — CALCULUS: a real special function.** Define the real dilogarithm for $s\le1$ by

$$
\operatorname{Li}_2(s)=-\int_0^s\frac{\ln(1-t)}t\,dt.
$$

The integrand inside this definition has limiting value $-1$ at zero. For $s=1$ its logarithmic endpoint is integrable. Thus the definition involves no complex logarithm on its stated domain. For $s<1$, $s\ne0$, its derivative is $-\ln(1-s)/s$, with derivative one at zero by continuity. The value at $s=1$ is finite, but its left derivative diverges.

In the regularized integral put $t=x/a$. Its bounds are zero and $1/a$, and the removable point becomes $t=1$:

$$
\int_0^1\frac{\ln x-\ln a}{x-a}\,dx
=\int_0^{1/a}\frac{\ln t}{t-1}\,dt.
$$

The derivative of $-\operatorname{Li}_2(1-t)$ is $\ln t/(t-1)$. Endpoint evaluation therefore gives the exact real expression

$$
J(a)=\ln a\ln\left(\frac{1-a}{a}\right)
+\operatorname{Li}_2(1)-\operatorname{Li}_2\left(1-\frac1a\right).
$$

The last argument is negative, within the real domain just defined.

**Step 4 — ALGEBRA: exposing the endpoint behavior.** Two identities remove the large negative argument. Direct differentiation with respect to $a\in(0,1)$ shows that

$$
\operatorname{Li}_2\left(1-\frac1a\right)
+\operatorname{Li}_2(1-a)+\frac12\ln^2a
$$

has derivative zero; its limit at $a\uparrow1$ is zero. Similarly, the derivative of

$$
\operatorname{Li}_2(a)+\operatorname{Li}_2(1-a)
+\ln a\ln(1-a)
$$

is zero, and its limit at $a\downarrow0$ is $\operatorname{Li}_2(1)$. Substituting these two identities in the previous answer yields

$$
J(a)=2\operatorname{Li}_2(1)-\operatorname{Li}_2(a)-\frac12\ln^2a.
$$

Here $\operatorname{Li}_2(1)=\sum_{m=1}^\infty m^{-2}=\pi^2/6$ is the standard Basel constant. The series follows by integrating the nonnegative geometric expansion in the defining integral; the integral definition already specifies the constant without requiring its closed value. Equivalently,

$$
J(a)=\frac{\pi^2}{3}-\operatorname{Li}_2(a)-\frac12\ln^2a.
$$

**Step 5 — DOMAIN: the two endpoint limits.** The defining integral gives $\operatorname{Li}_2(a)\to0$ as $a\downarrow0$ and $\operatorname{Li}_2(a)\to\operatorname{Li}_2(1)$ as $a\uparrow1$. Hence

$$
\lim_{a\downarrow0}J(a)=-\infty,\qquad
\lim_{a\uparrow1}J(a)=\operatorname{Li}_2(1)=\frac{\pi^2}{6}.
$$

With the pole exactly at zero, the ordinary integral is $\int_0^1\ln x/x\,dx=-\infty$, by its primitive $\ln^2x/2$. With the pole at one, the quotient $\ln x/(x-1)$ has removable value one at $x=1$ and is integrable at zero. Its ordinary integral is

$$
\int_0^1\frac{-\ln x}{1-x}\,dx
=\sum_{n=0}^\infty\int_0^1x^n(-\ln x)\,dx
=\sum_{n=0}^\infty\frac1{(n+1)^2}
=\frac{\pi^2}{6}.
$$

The nonnegative term series justifies this interchange by monotone convergence. Thus the endpoint at one changes the singularity itself: the numerator now vanishes at the pole.

**Step 6 — CHECK.** The regularized quotient is positive on $(0,1)$ because $\ln x$ is strictly increasing. At $a=1/2$ the explicit principal-value logarithm is zero. Splitting the regularized integral at $x=1/2$ and substituting $t=x/a$ gives

$$
J(1/2)=\int_0^2\frac{\ln t}{t-1}\,dt
=\operatorname{Li}_2(1)-\operatorname{Li}_2(-1)
=\frac{\pi^2}{4}.
$$

For the last equality, the alternating series for $\operatorname{Li}_2(-1)$ separates its even and odd terms to give $-\operatorname{Li}_2(1)/2$. This checks the sign and constant independently of the simplified $a$-formula. Numerical integration of the nonsingular subtracted quotient supplies another check without balancing two large pole contributions.

**Discussion.** Subtracting the numerator at a pole separates a prescribed principal value from an ordinary convergent calculation. A pole approaching an endpoint may retain its divergence or become removable, depending on the numerator.

### I3-016

**Step 1 — SETUP.** The ellipsoid is a compact smooth surface. Its level-set gradient cannot vanish on the surface, so any degeneracy in an angular parameterization must be distinguished from a surface singularity. Use independent real angles $0\le\theta\le\pi$ and $0\le\varphi<2\pi$ in

$$
\mathbf r(\theta,\varphi)=\begin{bmatrix}
a\sin\theta\cos\varphi\\b\sin\theta\sin\varphi\\c\cos\theta
\end{bmatrix}.
$$

The output is real scalar area, with no orientation sign.

**Step 2 — CHOICE.** This parameterization is the diagonal linear scaling of a unit sphere. A tangent cross product, rather than a volume determinant, supplies its surface measure. Reflection in each coordinate plane reduces the area calculation to eight identical octants.

**Step 3 — CALCULUS.** The two tangent columns are

$$
\frac{\partial}{\partial\theta}(\mathbf r)=
\begin{bmatrix}a\cos\theta\cos\varphi\\b\cos\theta\sin\varphi\\-c\sin\theta\end{bmatrix},
\qquad
\frac{\partial}{\partial\varphi}(\mathbf r)=
\begin{bmatrix}-a\sin\theta\sin\varphi\\b\sin\theta\cos\varphi\\0\end{bmatrix}.
$$

Their ordered cross product is

$$
\begin{bmatrix}
bc\sin^2\theta\cos\varphi\\
ac\sin^2\theta\sin\varphi\\
ab\sin\theta\cos\theta
\end{bmatrix}.
$$

Define the real unit column $\mathbf n=(\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta)^{\mathsf T}$ and fixed real matrix $\mathbf M=\operatorname{diag}(bc,ac,ab)$. On the full angular domain the cross-product length is $\sin\theta\,g(\theta,\varphi)$, where

$$
g(\theta,\varphi)=\|\mathbf M\mathbf n\|
=\sqrt{b^2c^2\sin^2\theta\cos^2\varphi
+a^2c^2\sin^2\theta\sin^2\varphi+a^2b^2\cos^2\theta}.
$$

**Step 4 — RESULT AND ALGEBRA.** Put $\ell=\pi/2$ and $f(\theta,\varphi)=\sin\theta\,g(\theta,\varphi)$. The explicit finite quadrature is

$$
S(a,b,c)=8\int_0^\ell\int_0^\ell f(\theta,\varphi)\,d\varphi\,d\theta.
$$

Every value under the square root lies between $(bc)^2$ and $(ab)^2$, since $\mathbf n$ is a unit vector and $bc<ac<ab$. Thus $bc\le g\le ab$. In particular the formula is bounded and nonsingular on the closed rectangle. Integrating these bounds over the whole sphere yields

$$
4\pi bc\le S(a,b,c)\le4\pi ab.
$$

**Step 5 — DOMAIN: poles, seam, and limit.** At $\theta=0$ or $\pi$, the azimuthal tangent vanishes because all azimuths represent the same pole. The surface remains regular there in another chart. At $\varphi=0$ and $2\pi$ the same meridian is identified, but the cross product does not vanish away from the poles. These coordinate sets have zero surface area, and the angular seam is counted once.

As $a,b,c$ tend to the same positive length $r$, the function $g$ tends uniformly to $r^2$. The area tends to $8r^2\int_0^\ell\int_0^\ell\sin\theta\,d\varphi\,d\theta=4\pi r^2$. The uniform bound above also supplies domination for this limiting calculation.

**Step 6 — CALCULUS: a rigorous numerical error bound.** For positive integers $N,M$, let $\Delta\theta=\ell/N$, $\Delta\varphi=\ell/M$, and use the midpoint sum

$$
S_{N,M}=8\Delta\theta\Delta\varphi
\sum_{i=0}^{N-1}\sum_{j=0}^{M-1}
f\left((i+\tfrac12)\Delta\theta,(j+\tfrac12)\Delta\varphi\right).
$$

Since $g=\|\mathbf M\mathbf n\|>0$, differentiation of the norm and the Cauchy--Schwarz inequality give

$$
|\partial_\theta g|\le\|\mathbf M\partial_\theta\mathbf n\|\le ab,
\qquad
|\partial_\varphi g|\le\|\mathbf M\partial_\varphi\mathbf n\|\le ab\sin\theta.
$$

Here $\|\partial_\theta\mathbf n\|=1$ and $\|\partial_\varphi\mathbf n\|=\sin\theta$. On the octant rectangle it follows that

$$
|\partial_\theta f|\le ab(\sin\theta+\cos\theta)\le\sqrt2ab,
\qquad |\partial_\varphi f|\le ab\sin^2\theta\le ab.
$$

Within a single cell, integrate the bound on the difference between $f$ and its midpoint value. The average distances from the midpoint in the two coordinate directions are $\Delta\theta/4$ and $\Delta\varphi/4$. Summing over the rectangle and multiplying by eight gives

$$
\begin{aligned}
|S-S_{N,M}|
&\le8\ell^2\left(\frac{\sqrt2ab\Delta\theta}{4}
+\frac{ab\Delta\varphi}{4}\right)\\
&=\frac{\pi^3ab}{4}\left(\frac{\sqrt2}{N}+\frac1M\right).
\end{aligned}
$$

This is a conservative absolute error bound in units of area. For a requested tolerance $\eta>0$, any $N,M$ making its right-hand side at most $\eta$ provide a certified quadrature enclosure. One explicit choice is $N=M\ge\pi^3ab(\sqrt2+1)/(4\eta)$, rounded up to a positive integer. Floating-point evaluation error, if material, is additional to this mathematical quadrature bound.

**Step 7 — CHECK.** In the spherical case the integrand becomes $r^2\sin\theta$, and its exact integral recovers $4\pi r^2$ without an elliptic formula. Independently, exchanging two physical axes cannot change the area: the full-sphere norm expression is invariant under the corresponding permutation of the components of $\mathbf n$, even though a chosen octant parameterization looks different. Numerically refined midpoint sums can be compared using the explicit error bounds of both sums, rather than treating their agreement alone as proof of an error estimate.

**Discussion.** An explicit bounded quadrature with a controlled error is a complete representation of a surface area. Coordinate degeneracies and approximation accuracy can be resolved without forcing an elementary antiderivative.

### I3-017

**Step 1 — SETUP.** Define two positive real lengths for an off-ring observation,

$$
d=\sqrt{(a+\rho)^2+z^2},\qquad
\delta=\sqrt{(\rho-a)^2+z^2}>0.
$$

The original denominator lies between $\delta$ and $d$, so its integrand is positive and continuous over a compact angular interval. The output has units of inverse length.

**Step 2 — CHOICE.** The half-angle identity gives

$$
a^2+\rho^2+z^2-2a\rho\cos\theta
=d^2-4a\rho\cos^2(\theta/2).
$$

Define the dimensionless real elliptic parameter

$$
m=\frac{4a\rho}{d^2},\qquad
1-m=\frac{\delta^2}{d^2}>0.
$$

Thus $0\le m<1$. The real modulus is $\kappa=\sqrt m$, whereas the complementary modulus is $\kappa'=\sqrt{1-m}=\delta/d$.

**Step 3 — CALCULUS: the elliptic representation.** In this problem the complete elliptic integral is defined with its parameter as argument:

$$
K(m)=\int_0^{\pi/2}\frac1{\sqrt{1-m\sin^2u}}\,du,
\qquad 0\le m<1.
$$

Put $u=\theta/2$ in the original integral and use reflection symmetry of $\cos^2u$ over $[0,\pi]$. A further replacement of $u$ by $\pi/2-u$ on a half interval gives

$$
P(\rho,z;a)=\frac4dK(m).
$$

This definition uses $m$ where a modulus-based convention writes $\kappa^2$. In particular, the NIST DLMF function denoted $K(\kappa)$ equals the present $K(\kappa^2)$.

**Step 4 — ALGEBRA AND CHECK: the axis.** At $\rho=0$, the parameter is zero and $K(0)=\pi/2$, so

$$
P(0,z;a)=\frac{2\pi}{\sqrt{a^2+z^2}}.
$$

This also follows directly because the original integrand is constant on the ring. It is the continuous on-axis limit: in a neighborhood $0\le\rho\le a/2$, the original denominator is at least $a/2$, so finite-interval dominated convergence applies. The formula is even in $z$, as is the geometry.

**Step 5 — DOMAIN: approaching the ring.** The complementary-modulus expansion in [NIST DLMF, Equation 19.12.1](https://dlmf.nist.gov/19.12.E1), whose constant is specified immediately after Equation 19.12.3, gives for positive $\varepsilon\downarrow0$

$$
K(1-\varepsilon^2)
=\ln\left(\frac4\varepsilon\right)
+O\left(\varepsilon^2\ln\left(\frac1\varepsilon\right)\right).
$$

The DLMF argument is its modulus, so this is its expansion at $\kappa'=\varepsilon$, with $\kappa=\sqrt{1-\varepsilon^2}$. Its leading constant is $\ln4$; dropping that constant would lose the finite term in the ring asymptotic.

With $\varepsilon=\delta/d$ the evaluated kernel becomes

$$
P(\rho,z;a)=\frac4d\left(
\ln\left(\frac{4d}{\delta}\right)
+O\left(\frac{\delta^2}{d^2}\ln\left(\frac d\delta\right)\right)\right).
$$

For fixed $a>0$ and $\delta\downarrow0$, $\rho\to a$ and $d=2a+O(\delta)$. Replacing $d$ by $2a$ in the leading expression changes it by at most a constant times $\delta\ln(a/\delta)/a^2$, which tends to zero. Consequently the particularly simple geometric form is

$$
P(\rho,z;a)=\frac2a\ln\left(\frac{8a}{\delta}\right)+o(1),
\qquad \delta=\sqrt{(\rho-a)^2+z^2}\downarrow0.
$$

Here $o(1)$ denotes an additive term tending to zero with the fixed physical units of $P$. All logarithm arguments are dimensionless. The coefficient of the logarithmic divergence is $2/a$.

**Step 6 — CHECK: local singularity and global bounds.** At the excluded point itself the denominator is $2a|\sin(\theta/2)|$. Near $\theta=0$ it is asymptotic to $a\theta$, and near $2\pi$ it is asymptotic to $a(2\pi-\theta)$. These two ends describe the same local source neighborhood from its two sides; each supplies one logarithmic angular tail. Their combined coefficient agrees with $2/a$. At the exact source the positive angular integral diverges, so no principal value can make this positive singularity an ordinary finite potential.

For every admissible observation, the original denominator bounds also give

$$
\frac{2\pi}{d}\le P(\rho,z;a)\le\frac{2\pi}{\delta}.
$$

The exact axis result lies within these bounds. Direct angular quadrature away from the ring provides an independent check on the elliptic normalization.

**Discussion.** The same geometric distance that identifies the excluded source supplies the complementary elliptic modulus. Converting that convention correctly preserves both the logarithmic coefficient and its constant.

### I3-018

**Step 1 — SETUP AND DOMAIN.** On the compact triangle the weight has magnitude at most $|\alpha|+|\beta|+|\gamma|$. For $h\ge0$ and $(x,y)\ne(0,0)$,

$$
\frac{|\alpha+\beta x+\gamma y|}{\sqrt{x^2+y^2+h^2}}
\le\frac{|\alpha|+|\beta|+|\gamma|}{\sqrt{x^2+y^2}}.
$$

The right-hand side has a finite area integral, as the vertex calculation in I3-007 establishes. Thus signed weights cause no ambiguity: the integral is absolutely convergent even at zero distance, and dominated convergence in $h$ is available for the values themselves.

**Step 2 — CHOICE.** Use independent coordinates $0<u\le1$, $0\le v\le1$ with $x=u$, $y=uv$. The real Jacobian determinant is $u>0$. Define the positive scalar $c(v)=\sqrt{1+v^2}$, so the denominator becomes $\sqrt{c(v)^2u^2+h^2}$. The constant and linear weight parts require two different radial moments.

**Step 3 — CALCULUS: radial primitives for positive distance.** For fixed $v$ abbreviate $c=c(v)>0$ and let

$$
A_0(v,h)=\int_0^1\frac{u}{\sqrt{c^2u^2+h^2}}\,du,
\qquad
A_1(v,h)=\int_0^1\frac{u^2}{\sqrt{c^2u^2+h^2}}\,du.
$$

For $h>0$, substitution of $s=\sqrt{c^2u^2+h^2}$ in the first gives

$$
A_0(v,h)=\frac{\sqrt{c^2+h^2}-h}{c^2}
=\frac1{\sqrt{c^2+h^2}+h}.
$$

For the second, put $w=cu/h$. Then

$$
A_1(v,h)=\frac{h^2}{c^3}\int_0^{c/h}\frac{w^2}{\sqrt{1+w^2}}\,dw.
$$

The identity $w^2=(1+w^2)-1$ and one integration by parts give the primitive
$\bigl(w\sqrt{1+w^2}-\operatorname{arsinh}(w)\bigr)/2$. Consequently

$$
A_1(v,h)=\frac{\sqrt{c^2+h^2}}{2c^2}
-\frac{h^2}{2c^3}\operatorname{arsinh}\left(\frac ch\right).
$$

Here $\operatorname{arsinh}(s)=\ln(s+\sqrt{1+s^2})$ is the real inverse hyperbolic sine. The complete nonsingular one-dimensional representation is

$$
L(h;\alpha,\beta,\gamma)
=\int_0^1\left(\alpha A_0(v,h)+(\beta+\gamma v)A_1(v,h)\right)\,dv,
\qquad h>0.
$$

**Step 4 — ALGEBRA: the exact zero-distance moments.** At $h=0$, direct cancellation in the radial integrals gives $A_0(v,0)=1/c(v)$ and $A_1(v,0)=1/(2c(v))$. Therefore the three moments are

$$
\begin{aligned}
\iint_T\frac1{\sqrt{x^2+y^2}}\,dx\,dy
&=\int_0^1\frac1{\sqrt{1+v^2}}\,dv=\operatorname{arsinh}(1),\\
\iint_T\frac{x}{\sqrt{x^2+y^2}}\,dx\,dy
&=\frac12\operatorname{arsinh}(1),\\
\iint_T\frac{y}{\sqrt{x^2+y^2}}\,dx\,dy
&=\frac12\int_0^1\frac v{\sqrt{1+v^2}}\,dv
=\frac{\sqrt2-1}{2}.
\end{aligned}
$$

Their signed combination is

$$
L(0;\alpha,\beta,\gamma)
=\left(\alpha+\frac\beta2\right)\operatorname{arsinh}(1)
+\frac\gamma2(\sqrt2-1).
$$

**Step 5 — CALCULUS: the right derivative and an explicit remainder.** Rationalization gives, for every $h>0$,

$$
0\le A_0(v,h)-\frac1c+\frac h{c^2}
=\frac{h^2}{c^2(\sqrt{c^2+h^2}+c)}\le\frac{h^2}{2c^3}.
$$

The second radial integral decreases as $h$ increases. Its explicit formula therefore gives

$$
0\le\frac1{2c}-A_1(v,h)
\le\frac{h^2}{2c^3}\operatorname{arsinh}\left(\frac ch\right)
\le\frac{h^2}{2}\operatorname{arsinh}\left(\frac{\sqrt2}{h}\right),
$$

using $1\le c(v)\le\sqrt2$. Integration in $v$, including the signs of the fixed weights by absolute values, yields

$$
\begin{aligned}
\left|L(h)-L(0)+\frac{\pi\alpha}{4}h\right|
\le\frac{h^2}{2}\left(
|\alpha|+(|\beta|+|\gamma|)\operatorname{arsinh}\left(\frac{\sqrt2}{h}\right)
\right).
\end{aligned}
$$

The suppressed arguments in $L(h)$ and $L(0)$ are the same fixed weights. Since $h\operatorname{arsinh}(\sqrt2/h)\to0$, the right derivative exists and is

$$
\left.\frac{\partial}{\partial h}L(h;\alpha,\beta,\gamma)\right|_{h=0^+}
=-\frac{\pi\alpha}{4}.
$$

Only the weight at the vertex controls this derivative. If $\alpha=0$, the change in the integral is bounded by a constant times $h^2\ln(1/h)$ instead of having a nonzero term linear in $h$.

**Step 6 — DOMAIN: when the area derivative can pass through zero.** At a fixed positive $h$, ordinary finite-domain differentiation is justified by a positive lower bound on the denominator. At $h=0$, the pointwise right derivative of the kernel at every nonzero panel point is zero. If $\alpha\ne0$, its area integral is zero while the evaluated right derivative is $-\pi\alpha/4$, so passing the derivative through the area integral fails.

For $\alpha=0$ let $R=\sqrt{x^2+y^2}$ and $C=\sqrt{\beta^2+\gamma^2}$. Cauchy--Schwarz gives $|\beta x+\gamma y|\le CR$. For nonnegative $h$,

$$
\left|\frac{\partial}{\partial h}
\left(\frac{\beta x+\gamma y}{\sqrt{R^2+h^2}}\right)\right|
\le\frac{CRh}{(R^2+h^2)^{3/2}}
\le\frac C R.
$$

The last function is area-integrable. Domination therefore justifies taking the right derivative under the area integral, with value zero. It also shows that this derivative tends continuously to zero from positive $h$. If the distance is extended to signed $h$ using the same squared denominator, a nonzero $\alpha$ produces a cusp, whereas a vanishing vertex weight gives a continuously differentiable even extension. No second-derivative claim follows from the logarithmic remainder bound alone.

**Step 7 — CHECK.** An independent polar description of the triangle has $0\le\theta\le\pi/4$ and $0\le r\le\sec\theta$. The three zero-distance integrands after including the area measure are $1$, $r\cos\theta$, and $r\sin\theta$. Their radial integrals give respectively

$$
\int_0^{\pi/4}\sec\theta\,d\theta=\operatorname{arsinh}(1),\qquad
\frac12\int_0^{\pi/4}\sec\theta\,d\theta,\qquad
\frac12\int_0^{\pi/4}\frac{\sin\theta}{\cos^2\theta}\,d\theta,
$$

which reproduce all three moments. For the constant weight at positive $h$, the polar radial primitive gives
$\int_0^{\pi/4}(\sqrt{\sec^2\theta+h^2}-h)\,d\theta$.
Its right derivative at zero is $-\pi/4$, independently confirming the vertex coefficient.

**Discussion.** A linear testing weight can remove the leading parameter cusp of a singular panel integral. Absolute convergence of the value and permission to differentiate at zero are separate questions, resolved here by different majorants.

### I3-019

**Step 1 — SETUP.** The phase is real, the output is complex, and the finite-interval integrand is continuous with magnitude one. The phase derivative $2kx$ vanishes at zero. A formula involving its reciprocal can be used only on intervals separated from that stationary point.

**Step 2 — CHOICE AND EXACT REPRESENTATION.** Define real Fresnel functions for real $s$ by

$$
C(s)=\int_0^s\cos\left(\frac\pi2t^2\right)\,dt,
\qquad
S(s)=\int_0^s\sin\left(\frac\pi2t^2\right)\,dt.
$$

Evenness of the original phase and the coordinate $t=\sqrt{2k/\pi}\,x$ give, with $s=a\sqrt{2k/\pi}$,

$$
I(k;a)=\sqrt{\frac{2\pi}{k}}\bigl(C(s)+\mathrm{i}S(s)\bigr).
$$

For the large-parameter calculation, the complete real-line oscillatory integral supplies the stationary contribution; the two tails beyond $a$ supply the endpoint correction.

**Step 3 — DOMAIN: convergence and a uniform damping bound.** For a real damping parameter $\epsilon\ge0$, consider a positive tail starting at $A>0$. On $x\ge A$ let $f_\epsilon(x)=\exp(-\epsilon x^2)/x$, a decreasing positive function tending to zero. Integration by parts against $\exp(\mathrm{i}kx^2)$ gives, for $B>A$,

$$
\begin{aligned}
\left|\int_A^B\exp(-\epsilon x^2)\exp(\mathrm{i}kx^2)\,dx\right|
&\le\frac{f_\epsilon(A)+f_\epsilon(B)+\int_A^B|\frac{d}{dx}(f_\epsilon(x))|\,dx}{2k}\\
&=\frac{f_\epsilon(A)}k\le\frac1{kA}.
\end{aligned}
$$

The formula uses $\frac{d}{dx}\exp(\mathrm{i}kx^2)=2\mathrm{i}kx\exp(\mathrm{i}kx^2)$ only where $x\ge A>0$. Applying the same bound from any later starting point proves the Cauchy criterion, including $\epsilon=0$. The negative tail has the same bound by evenness. The ordinary real-line integral therefore exists with its two tails converging separately. Its absolute integral diverges because the undamped integrand has magnitude one.

On every finite interval, the damped integrands converge under bounded domination as $\epsilon\downarrow0$. The uniform tail bound then shows that their complete integrals tend to the ordinary oscillatory integral. This justifies the damping limit without an integrable absolute majorant on the whole line.

**Step 4 — CALCULUS: the complete Gaussian-damped integral.** For fixed $\epsilon>0$, define the complex scalar

$$
G_\epsilon(k)=\int_{-\infty}^\infty
\exp\left(-\left(\epsilon-\mathrm{i}k\right)x^2\right)\,dx.
$$

Differentiation in the real parameter $k$ is justified by the integrable bound $x^2\exp(-\epsilon x^2)$. Integrating the derivative of $x\exp(- (\epsilon-\mathrm{i}k)x^2)$ over the line, whose boundary terms vanish, gives

$$
\int_{-\infty}^\infty x^2\exp(- (\epsilon-\mathrm{i}k)x^2)\,dx
=\frac{G_\epsilon(k)}{2(\epsilon-\mathrm{i}k)}.
$$

Consequently $\frac{d}{dk}G_\epsilon(k)=\mathrm{i}G_\epsilon(k)/(2(\epsilon-\mathrm{i}k))$. Its initial value is the real Gaussian integral $G_\epsilon(0)=\sqrt{\pi/\epsilon}$. Solving this scalar parameter equation with the square root chosen positive at $k=0$ gives

$$
G_\epsilon(k)=\frac{\sqrt\pi}{\sqrt{\epsilon-\mathrm{i}k}}
=\frac{\sqrt\pi}{(\epsilon^2+k^2)^{1/4}}
\exp\left(\frac{\mathrm{i}}2\arctan\left(\frac k\epsilon\right)\right).
$$

The real Gaussian initial value can itself be obtained by squaring its positive integral, using plane polar coordinates, and then scaling $x$ by $\sqrt\epsilon$. The displayed polar form specifies the complex square-root branch without ambiguity. The justified damping limit now yields

$$
G(k)=\int_{-\infty}^\infty\exp(\mathrm{i}kx^2)\,dx
=\sqrt{\frac\pi k}\exp(\mathrm{i}\pi/4),\qquad k>0.
$$

**Step 5 — CALCULUS AND ALGEBRA: the endpoint term.** Let $T=\int_a^\infty\exp(\mathrm{i}kx^2)\,dx$. On this positive tail, integration by parts gives

$$
T=-\frac{\exp(\mathrm{i}ka^2)}{2\mathrm{i}ka}
+\frac1{2\mathrm{i}k}\int_a^\infty\frac{\exp(\mathrm{i}kx^2)}{x^2}\,dx.
$$

The boundary term at infinity vanishes because of its factor $1/x$. Subtracting both tails from $G(k)$ gives

$$
I(k;a)=\sqrt{\frac\pi k}\exp(\mathrm{i}\pi/4)
+\frac{\exp(\mathrm{i}ka^2)}{\mathrm{i}ka}+R(k;a),
$$

where

$$
R(k;a)=-\frac1{\mathrm{i}k}\int_a^\infty\frac{\exp(\mathrm{i}kx^2)}{x^2}\,dx.
$$

In particular, the endpoint term has factor $1/\mathrm{i}=-\mathrm{i}$, rather than the opposite phase sign.

**Step 6 — DOMAIN AND ERROR BOUND.** Put $U=\int_a^\infty\exp(\mathrm{i}kx^2)/x^2\,dx$, which is already absolutely convergent. A further integration by parts, again away from zero, gives

$$
U=-\frac{\exp(\mathrm{i}ka^2)}{2\mathrm{i}ka^3}
+\frac3{2\mathrm{i}k}\int_a^\infty\frac{\exp(\mathrm{i}kx^2)}{x^4}\,dx.
$$

Bounding the last integral absolutely by $\int_a^\infty x^{-4}\,dx=1/(3a^3)$ proves

$$
|U|\le\frac1{ka^3},\qquad
|R(k;a)|\le\frac1{k^2a^3}.
$$

The leading stationary term has order $k^{-1/2}$, the endpoint term has order $k^{-1}$, and the controlled remainder has order $k^{-2}$ for fixed positive $a$. Relative to the leading magnitude, the remainder is at most $1/(\sqrt\pi(ka^2)^{3/2})$, so the large-parameter regime is identified by the dimensionless quantity $ka^2$.

**Step 7 — CHECK: the opposite parameter limit.** Taylor's formula for a real phase satisfies $|\exp(\mathrm{i}y)-1-\mathrm{i}y|\le y^2/2$. Integration over the finite aperture gives

$$
I(k;a)=2a+\frac{2\mathrm{i}ka^3}{3}+E(k;a),
\qquad |E(k;a)|\le\frac{k^2a^5}{5}.
$$

This verifies the exact Fresnel scale as $k\downarrow0$ and shows why the large-$k$ representation must not be truncated as a small-parameter approximation. Independently, the original integral obeys $|I(k;a)|\le2a$ by the triangle inequality. Finite-interval complex quadrature checks both components of the exact answer and the sign of the endpoint correction.

**Discussion.** A stationary point supplies a different scale from an ordinary endpoint. Splitting the complete integral and its tails preserves that distinction and places every division by a phase derivative in a region where it is valid.

## Application references

The problems and solutions here are original. The real sine integral is defined
in [NIST DLMF, Section 6.2](https://dlmf.nist.gov/6.2).
The singular-panel example illustrates a basic coordinate mechanism related to
[Reid, Johnson, and White, Generalized Taylor-Duffy Method for Efficient Evaluation of Galerkin Integrals in Boundary-Element Method Computations](https://arxiv.org/abs/1312.1703).
That paper concerns more general CEM integrals than this single-triangle model.
The geometric measure conventions follow the change-of-variables framework in
[MIT, Calculus with Applications, Section 24.2](https://ocw.mit.edu/ans7870/18/18.013a/textbook/chapter24/section02.html).
