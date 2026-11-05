# I4 · Parameter integrals and geometric accumulation

## Problems

### I4-001 — A difference of exponential kernels

**Objects and dependencies.** $x>0$ is a real integration coordinate. Fixed real scalars $a,b>0$ define the real scalar integral

$$
J(a,b)=\int_0^\infty\frac{\exp(-ax)-\exp(-bx)}{x}\,dx.
$$

Determine its value, convergence at both ends, and behavior as $a\downarrow0$ with $b$ fixed. The ratio $b/a$ is dimensionless.

### I4-002 — A logarithmic kernel on a finite interval

**Objects and dependencies.** $x\in[0,1]$ is a real integration variable and $a>-1$ is an independent real parameter. The real scalar integral is

$$
J(a)=\int_0^1\frac{\ln(1+ax)}{x}\,dx,
$$

with the continuous endpoint value at $x=0$. Determine its parameter derivative, a convergent series for $|a|<1$, and a real special-function representation for all $a>-1$. Decide whether the integral remains finite at $a=-1$ and whether its derivative has a finite limit there.

### I4-003 — A damped difference of oscillatory kernels

**Objects and dependencies.** $x\ge0$ is a real integration coordinate. Fixed real parameters satisfy $a>0$ and $b,c\ge0$. Determine the real scalar integral

$$
K(a,b,c)=\int_0^\infty\exp(-ax)\frac{\cos(bx)-\cos(cx)}{x}\,dx.
$$

Establish convergence before evaluating it, and give its limit as $a\downarrow0$ when $b,c>0$.

### I4-004 — A weighted logarithm with limiting parameter values

**Objects and dependencies.** The real integration variable is $x\in(-1,1)$, and the independent real parameter satisfies $|\lambda|<1$. Evaluate

$$
J(\lambda)=\int_{-1}^1\frac{\ln(1+\lambda x)}{\sqrt{1-x^2}}\,dx.
$$

Determine whether the integral extends to $\lambda=\pm1$ and whether differentiation under the integral remains valid at those endpoints.

### I4-005 — Flux through a translated ellipsoid

**Objects and dependencies.** Fixed real scalars $a,b,c>0$ and $d\in\mathbb R$, with $d\ne\pm a$, define the bounded volume

$$
V_d=\left\{(x,y,z):\frac{(x-d)^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\le1\right\}.
$$

The independent spatial coordinates are real. The real vector field is $\mathbf F(x,y,z)=[x,y,z]^{\mathsf T}/(x^2+y^2+z^2)^{3/2}$ away from the origin. Determine its flux through $\partial V_d$ with outward orientation, and the two limits as $d$ approaches $a$ from opposite sides.

### I4-006 — A panel kernel at positive observation distance

**Objects and dependencies.** Independent real dimensionless coordinates satisfy $0\le y\le x\le1$. The independent real dimensionless observation parameter is $h>0$. Evaluate the real scalar integral

$$
K(h)=\int_0^1\int_0^x\frac{1}{\sqrt{x^2+y^2+h^2}}\,dy\,dx.
$$

Determine its continuous limit at $h=0$, its right derivative there, and an explicit bound on the error in its linear small-$h$ approximation. Explain whether the limit of the parameter derivative may be passed through the original area integral.

### I4-007 — An oblique ellipsoidal cap

**Objects and dependencies.** Fixed positive real lengths $a,b,c$ and a fixed nonzero dimensionless real column vector $\mathbf n=[n_1,n_2,n_3]^{\mathsf T}$ define an ellipsoid. The independent real offset $h$ has units of length. For independent Cartesian coordinates $x,y,z$, determine the real scalar volume

$$
V(h)=\iiint_{\substack{x^2/a^2+y^2/b^2+z^2/c^2\le1\\n_1x+n_2y+n_3z\ge h}}dx\,dy\,dz.
$$

Give a formula for every real $h$, including the full-volume and zero-volume cases. Determine its first derivative, including at the two tangent-plane offsets, and its relation to the area of the planar section. The vector $\mathbf n$ is not assumed to be a unit vector.

### I4-008 — Two nearby poles off the real axis

**Objects and dependencies.** The integration coordinate $x\ge0$ and the parameters $a,b>0$ are dimensionless real scalars. Determine

$$
J(a,b)=\int_0^\infty\frac{1}{(x^2+a^2)(x^2+b^2)}\,dx
$$

in a form that remains well conditioned when $a$ and $b$ are nearly equal. Evaluate the coincident case directly by a parameter derivative, find $\frac{\partial}{\partial a}(J(a,b))$ with $b$ fixed, and describe the behavior as $a\downarrow0$ with positive $b$ fixed.

### I4-009 — An accumulated matrix response

**Objects and dependencies.** $n$ is a fixed positive integer, $\mathbf I_n$ is the real $n\times n$ identity, and $\mathbf A$ is a real symmetric positive-definite $n\times n$ matrix. The real coordinate $s\ge0$ is integrated entrywise. All quantities are dimensionless. Determine the real matrix

$$
\mathbf M(\mathbf A)=\int_0^\infty(\mathbf A+s\mathbf I_n)^{-2}\,ds,
$$

where the power means the matrix product of two inverses. Next let $\mathbf A(t)$ be a continuously differentiable symmetric positive-definite matrix on an open real interval. At a fixed input $t_0$, set $\mathbf A_0=\mathbf A(t_0)$ and $\mathbf H=\left.\frac{d}{dt}(\mathbf A(t))\right|_{t=t_0}$. Determine $\left.\frac{d}{dt}(\mathbf M(\mathbf A(t)))\right|_{t=t_0}$, justify differentiating through the improper integral, and retain the order of factors without assuming that $\mathbf A_0$ and $\mathbf H$ commute.

### I4-010 — A Gaussian with a moving truncation

**Objects and dependencies.** The independent input $t\in\mathbb R$, fixed $L>0$, and integration coordinate $x$ are dimensionless real scalars. The real scalar response is the oriented integral

$$
G(t;L)=\int_{-L}^{t}\exp(-(x-t)^2)\,dx.
$$

Determine its first two derivatives for all real $t$, its limits as $t\to\pm\infty$, and a quantitative bound on the error in either limiting value. Verify the first derivative both in the original coordinate and after a coordinate shift. In particular, the definition retains its orientation when $t<-L$.

### I4-011 — A circular aperture transform

**Objects and dependencies.** The fixed radius $a>0$ and integration coordinate $r\in[0,a]$ are real lengths; the angle $\theta\in[0,2\pi]$ is dimensionless. The independent real transverse wavenumber $q$ has units of inverse length. Determine the complex scalar area transform

$$
F(q;a)=\int_0^a\int_0^{2\pi}\exp(\mathrm i q r\cos\theta)r\,d\theta\,dr,
\qquad \mathrm i^2=-1.
$$

Give a Bessel-function representation with the required functions defined locally. Resolve the value at $q=0$, the dependence on the sign of $q$, and an explicit error bound for a quadratic small-$q$ approximation.

## Hint ladders

### I4-001

1. The numerator cancels at the singular endpoint.
2. The quotient can be expressed as an integral of $\exp(-sx)$ over the parameter interval from $a$ to $b$.
3. The order of integration is justified by a fixed sign, or by absolute integrability on the compact positive parameter interval.

### I4-002

1. The removable value at zero is $a$, and the parameter derivative is a rational integrand.
2. The logarithm series can be integrated termwise inside its convergence interval.
3. An endpoint logarithmic singularity can be integrable even when the parameter derivative is not.

### I4-003

1. The cosine difference is quadratic at the zero endpoint.
2. Differentiation with respect to one frequency removes the reciprocal coordinate.
3. The integration constant can be fixed at equal frequencies.

### I4-004

1. An angular coordinate removes the square-root weight.
2. Parameter differentiation separates the new angular integrand into a constant and a reciprocal linear cosine factor.
3. The tangent half-angle coordinate evaluates the remaining rational integral.

### I4-005

1. The source lies inside the volume exactly when $|d|<a$.
2. The divergence vanishes away from the source, but the theorem requires a regular field throughout the integration volume.
3. Excision of a small source-centered ball adds an oppositely oriented inner boundary.

### I4-006

1. The triangle-to-square coordinate $x=u,y=uv$ separates the radial distance from direction.
2. Integration in $u$ leaves a one-dimensional integral involving $\sqrt{1+v^2+h^2}$.
3. The difference of square roots gives an explicit quadratic remainder bound and reveals the endpoint parameter slope.

### I4-007

1. Scale the ellipsoid to a unit ball and transform the plane at the same time.
2. A rotation aligns the transformed plane normal with one coordinate without changing volume.
3. Integrate the circular sections from the normalized plane offset to one; the derivative includes the length of the original normal.

### I4-008

1. Unequal parameters allow partial fractions in $x^2$.
2. Combine the two integrated terms algebraically before taking a nearly coincident limit.
3. Differentiating $\int_0^\infty(x^2+a^2)^{-1}dx$ checks the repeated denominator directly.

### I4-009

1. Differentiate the resolvent in the integration coordinate $s$ first.
2. The derivative of the square in the perturbation parameter has two ordered product terms.
3. A uniform positive eigenvalue bound gives integrable domination; those two terms are also an $s$ derivative of an ordered product.

### I4-010

1. The relative coordinate $u=t-x$ leaves only one moving bound.
2. In the original coordinate, the boundary term and part of the integrand derivative cancel.
3. The Gaussian half-line integral is evaluated by squaring it and using polar coordinates; compare a tail with $u\exp(-u^2)$.

### I4-011

1. Reflection of the angular coordinate cancels the imaginary part and makes the answer even in $q$.
2. Integrate the exponential series in angle and radius on this compact domain.
3. The angular moments define the relevant Bessel series; a Taylor bound on the real cosine gives a uniform approximation error.

## Complete solutions

### I4-001

**Step 1 — SETUP.** The parameters $a,b$ are positive and fixed, and $x$ is the integration coordinate. At zero, expansion of the numerator gives $(b-a)x+O(x^2)$, so the kernel has the finite limit $b-a$. At infinity its absolute value is bounded by $2\exp(-\min(a,b)x)/x$ beyond $x=1$.

**Step 2 — CHOICE.** The parameter representation removes the apparent reciprocal singularity before either exponential integral is separated. The two separate integrals would each diverge at zero.

**Step 3 — CALCULUS.** With $x>0$ fixed,

$$
\int_a^b\exp(-sx)\,ds=\frac{\exp(-ax)-\exp(-bx)}{x}.
$$

For $b\ge a$, the integrand in this representation is nonnegative, so Tonelli's theorem permits interchange. For $b<a$, the reversed parameter interval changes the sign and the same argument applies to its magnitude. Thus

$$
J(a,b)=\int_a^b\left(\int_0^\infty\exp(-sx)\,dx\right)ds
=\int_a^b\frac1s\,ds=\ln(b/a).
$$

**Step 4 — DOMAIN.** As $a\downarrow0$, the answer tends to $+\infty$. At $a=0,b>0$, the numerator tends to one at infinity, leaving a nonintegrable $1/x$ tail. Tonelli's theorem still permits the interchange for this nonnegative kernel, but both iterated integrals have value $+\infty$; it does not produce a finite integral at the endpoint.

**Step 5 — CHECK.** $J(a,a)=0$ and $J(a,b)=-J(b,a)$. For $b>a$ the original integrand is nonnegative and the logarithm is positive. Differentiation with respect to $b>0$ gives $1/b$, also obtained directly by integrating $\exp(-bx)$.

**Discussion.** Cancellation within an integrand can be essential to its existence. Separating the canceled terms before integration can create two undefined quantities.

### I4-002

**Step 1 — SETUP.** For $a>-1$, $1+ax$ remains positive on the interval, and the quotient has limiting value $a$ as $x$ tends to zero. The output is real and dimensionless.

**Step 2 — CHOICE.** Parameter differentiation removes the logarithm and supplies a useful representation even though an elementary primitive of the original kernel is unavailable.

**Step 3 — CALCULUS.** On a neighborhood of each $a>-1$, the denominator $1+ax$ has a positive uniform lower bound. Consequently,

$$
\frac{d}{da}\left(J(a)\right)=\int_0^1\frac1{1+ax}\,dx
=\begin{cases}\ln(1+a)/a,&a\ne0,\\1,&a=0.\end{cases}
$$

The zero-parameter value follows directly from the rational integral, without division by zero.

**Step 4 — TRICK: convergent series.** The logarithm expansion in [T-002](TRICKS_APPENDIX.md#t-002-taylor-expansions) is uniformly convergent in $x\in[0,1]$ for each fixed $|a|<1$. After division by $x$, the $n$th term has absolute value at most $|a|^n/n$ on $0\le x\le1$. The sum of these bounds is finite for $|a|<1$, so termwise integration is justified. In particular,

$$
\frac{\ln(1+ax)}{x}
=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}a^n x^{n-1}}{n},
\qquad
\int_0^1x^{n-1}\,dx=\frac1n.
$$

Consequently,

$$
J(a)=\sum_{n=1}^\infty\frac{(-1)^{n+1}a^n}{n^2}.
$$

**Step 5 — CALCULUS: special-function representation.** For a real scalar $z<1$, the real dilogarithm is defined by

$$
\operatorname{Li}_2(z)=-\int_0^z\frac{\ln(1-u)}{u}\,du,
$$

where the quotient $\ln(1-u)/u$ has limiting value $-1$ at zero. The minus sign outside the integral is part of the definition. The coordinate $u=-ax$ gives $J(a)=-\operatorname{Li}_2(-a)$ for $a\ne0$, and both expressions vanish at $a=0$. This integral definition also covers $a>1$, where the displayed power series cannot be used.

**Step 6 — DOMAIN AND CHECK.** At $a=-1$, the logarithmic endpoint is integrable: near $x=1$, $1/x$ is bounded and $|\ln(1-x)|$ has a finite integral. For $a=-r$ with $0<r<1$, the nonnegative kernels $-\ln(1-rx)/x$ increase as $r$ tends to one. Monotone convergence therefore identifies the endpoint integral with the series limit $J(-1)=-\sum_{n=1}^\infty1/n^2$. However, $\ln(1+a)/a\to+\infty$ as $a\downarrow-1$. A finite function value does not provide a finite endpoint parameter derivative. The first series coefficient is one, agreeing with the derivative at zero. The dilogarithm convention follows [NIST DLMF 25.12](https://dlmf.nist.gov/25.12).

**Discussion.** The domain of an exact integral representation can exceed the convergence domain of its local series. Parameter differentiation can strengthen an endpoint singularity.

### I4-003

**Step 1 — SETUP.** The parameters are fixed inside the integral. Near zero the cosine difference is $(c^2-b^2)x^2/2+O(x^4)$; division by $x$ leaves an integrable linear behavior. Positive damping ensures absolute convergence at infinity.

**Step 2 — CHOICE.** The derivative with respect to $c$ has an elementary damped sine integral. The condition $K(a,b,b)=0$ fixes the parameter integration constant.

**Step 3 — CALCULUS.** The parameter derivative integrand is bounded by $\exp(-ax)$, independently of nearby $c$, so

$$
\frac{\partial}{\partial c}\left(K(a,b,c)\right)
=\int_0^\infty\exp(-ax)\sin(cx)\,dx=\frac{c}{a^2+c^2}.
$$

The last equality follows by taking the imaginary part of $\int_0^\infty\exp((-a+\mathrm{i}c)x)\,dx=1/(a-\mathrm{i}c)$, an application of [T-001](TRICKS_APPENDIX.md#t-001-euler-identities).

**Step 4 — CALCULUS AND ALGEBRA.** Integrating in the real frequency coordinate $s$ from $b$ to $c$ gives

$$
K(a,b,c)=\int_b^c\frac{s}{a^2+s^2}\,ds
=\frac12\ln\left(\frac{a^2+c^2}{a^2+b^2}\right).
$$

**Step 5 — DOMAIN.** For positive $b,c$, the damping limit is $\ln(c/b)$. To identify it with the undamped ordinary integral, set $f_a(x)=\exp(-ax)/x$ for $x>0$, including $a=0$. For a fixed positive frequency $q$ and real cutoffs $S>R>0$, integration by parts against $\sin(qx)/q$ gives

$$
\left|\int_R^S f_a(x)\cos(qx)\,dx\right|
\le\frac{f_a(R)+f_a(S)+\int_R^S\left|\frac{d}{dx}(f_a(x))\right|\,dx}{q}
=\frac{2f_a(R)}{q}\le\frac{2}{qR}.
$$

The equality uses that $f_a$ is decreasing. The bound applies uniformly in $a\ge0$ and makes both positive-frequency tails small. On each finite interval, the cosine difference divided by $x$ extends continuously to zero and is dominated independently of $a\ge0$. Finite-interval dominated convergence and the tail bounds therefore identify the damping limit with the ordinary undamped integral. If $b=0<c$, the limit diverges to $+\infty$; if $c=0<b$, it diverges to $-\infty$. If both vanish, the integral is identically zero.

**Step 6 — CHECK.** Interchanging $b,c$ negates both the original integrand and the logarithmic answer. At equal frequencies both vanish. The logarithm's argument is positive for $a>0$, including zero frequencies.

**Discussion.** A difference of oscillatory kernels can regularize one endpoint while damping controls the other. Each endpoint and each zero-frequency case has a separate convergence argument.

### I4-004

**Step 1 — SETUP.** For $|\lambda|<1$, the logarithm has a positive argument throughout the interval. The square-root endpoint singularities are integrable. The output is a real scalar.

**Step 2 — CHOICE.** The denominator $\sqrt{1-x^2}$ suggests $x=\cos\theta$ on $0<\theta<\pi$. On this interval the positive square root is $\sin\theta$, which cancels the magnitude of the coordinate derivative. Differentiation with respect to $\lambda$ then removes the logarithm, leaving an angular integral that can be converted to a rational one.

**Step 3 — CALCULUS.** The reversed angular bounds and negative coordinate derivative give

$$
J(\lambda)=\int_0^\pi\ln(1+\lambda\cos\theta)\,d\theta,
\qquad
\frac{d}{d\lambda}\left(J(\lambda)\right)=\int_0^\pi\frac{\cos\theta}{1+\lambda\cos\theta}\,d\theta.
$$

For each interior parameter, a local positive lower bound on the denominator justifies the derivative interchange.

**Step 4 — ALGEBRA.** For $\lambda\ne0$, the integrand is $\lambda^{-1}(1-(1+\lambda\cos\theta)^{-1})$. The real coordinate $u=\tan(\theta/2)$ has inverse derivative $2/(1+u^2)$ and bounds zero to infinity. It gives

$$
\int_0^\pi\frac{1}{1+\lambda\cos\theta}\,d\theta
=\int_0^\infty\frac{2}{(1+\lambda)+(1-\lambda)u^2}\,du
=\frac\pi{\sqrt{1-\lambda^2}}.
$$

Both quadratic coefficients are positive on the assumed domain; scaling $u$ by $\sqrt{(1-\lambda)/(1+\lambda)}$ reduces the final evaluation to an arctangent.

**Step 5 — CALCULUS.** Thus the derivative for nonzero interior $\lambda$ is $\pi(1-1/\sqrt{1-\lambda^2})/\lambda$. The condition $J(0)=0$ fixes its primitive:

$$
J(\lambda)=\pi\ln\left(\frac{1+\sqrt{1-\lambda^2}}{2}\right),\qquad |\lambda|<1.
$$

Differentiation of this expression and multiplication by the conjugate of $1+\sqrt{1-\lambda^2}$ verifies the derivative.

**Step 6 — DOMAIN.** At $\lambda=1$, the angular logarithm near $\theta=\pi$ behaves as $2\ln(\pi-\theta)-\ln2$, which is integrable. At $\lambda=-1$ the same occurs at zero. The limits of the interior integral equal the endpoint integrals: for $1/2\le\lambda\le1$ and $0\le\theta<\pi$,

$$
\frac{1+\cos\theta}{2}\le1+\lambda\cos\theta\le2.
$$

It follows that

$$
|\ln(1+\lambda\cos\theta)|
\le\ln2+\left|\ln\left(\frac{1+\cos\theta}{2}\right)\right|.
$$

The right-hand side is integrable and independent of $\lambda$. Dominated convergence justifies the limit at $\lambda=1$; reflection gives the limit at $\lambda=-1$. Both endpoint values are $-\pi\ln2$. The derivative instead diverges negatively at $\lambda\uparrow1$ and positively at $\lambda\downarrow-1$; the derivative kernels are not integrable at the singular endpoint.

**Step 7 — CHECK.** Reflection $x\mapsto-x$ gives $J(-\lambda)=J(\lambda)$. The answer is even and vanishes at zero. Expansion gives $J(\lambda)=-\pi\lambda^2/4+O(\lambda^4)$, agreeing with the first nonzero term obtained by integrating the logarithm series against the even weight.

**Discussion.** A geometric weight may identify a coordinate, while a parameter derivative identifies a second reduction. Existence of endpoint integrals does not establish endpoint derivative interchange.

### I4-005

**Step 1 — SETUP.** The surface is smooth and compact. The origin is not on it because $d\ne\pm a$, so the real scalar flux exists as an ordinary surface integral. The source is inside precisely when $d^2/a^2<1$.

**Step 2 — CHOICE.** The geometric placement of the excluded source determines whether the classical divergence theorem applies directly. Surface parameterization would introduce unnecessary algebra without resolving that regularity issue.

**Step 3 — CALCULUS.** The distance from the origin is $R(x,y,z)=\sqrt{x^2+y^2+z^2}>0$. Coordinate differentiation gives

$$
\nabla\cdot\mathbf F(x,y,z)
=\frac{3}{R(x,y,z)^3}-\frac{3(x^2+y^2+z^2)}{R(x,y,z)^5}=0.
$$

For $|d|>a$, the field is smooth on a neighborhood of $V_d$ and the flux is zero.

**Step 4 — DOMAIN: excision of the source.** For $|d|<a$, a ball of sufficiently small positive radius $\epsilon$ fits inside $V_d$. On the punctured volume the divergence theorem gives

$$
0=\iint_{\partial V_d}\mathbf F(x,y,z)\cdot\mathbf n(x,y,z)\,dS
-\iint_{R(x,y,z)=\epsilon}\mathbf F(x,y,z)\cdot\mathbf n_{\rm radial}(x,y,z)\,dS.
$$

The inner boundary has the negative radial orientation relative to the punctured volume. On its sphere, the radial field component is $1/\epsilon^2$ and the area is $4\pi\epsilon^2$, so the outward ellipsoid flux is $4\pi$.

**Step 5 — RESULT AND CHECK.** The flux is $4\pi$ for $|d|<a$ and zero for $|d|>a$. Consequently the limits at $d=a$ are $4\pi$ from below and zero from above. A continuous deformation preserving the source placement preserves the answer. At $d=a$ the source reaches the surface and the ordinary smooth-field hypotheses used above fail; this excluded case is not assigned either value by substitution. The point-source flux principle is documented in [MIT, Electrostatics and Potentials](https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter28/section04.html).

**Discussion.** A zero classical divergence away from a source does not imply zero flux through a surface enclosing that source. Domain topology and orientation can replace a difficult explicit surface integral.

### I4-006

**Step 1 — SETUP.** For each $h>0$ the kernel is real and continuous on the closed triangle. The output is a real scalar. The limiting kernel at zero has the integrable vertex singularity studied in I3-007.

**Step 2 — CHOICE.** A triangle-to-square map exposes the area Jacobian and permits the radial coordinate to be integrated first. The remaining expression supports both exact evaluation and a uniform small-distance estimate.

**Step 3 — CALCULUS.** With real $x(u,v)=u$, $y(u,v)=uv$ on the unit square, the absolute Jacobian is $u$. Integration in $u$ gives

$$
K(h)=\int_0^1\int_0^1\frac{u}{\sqrt{u^2(1+v^2)+h^2}}\,du\,dv
=\int_0^1\frac{\sqrt{1+v^2+h^2}-h}{1+v^2}\,dv.
$$

The lower radial endpoint contributes $h$, since $h>0$.

**Step 4 — TRICK: hyperbolic representation.** The abbreviation $A=1+h^2$ denotes a positive scalar that is fixed during integration in $v$. The coordinate $v=\sqrt A\sinh t$ gives

$$
\frac{\sqrt{A+v^2}}{1+v^2}\,dv
=\frac{A\cosh^2t}{1+A\sinh^2t}\,dt
=\left(1+\frac{h^2}{1+A\sinh^2t}\right)dt.
$$

The identities are those of [T-007](TRICKS_APPENDIX.md#t-007-hyperbolic-identities-and-real-branches). The additional coordinate $w=\tanh t$ satisfies

$$
\frac{d}{dt}(w(t))=1-w(t)^2,
\qquad
\sinh^2t=\frac{w^2}{1-w^2}.
$$

Thus the remaining integral becomes

$$
\begin{aligned}
\int\frac{h^2}{1+A\sinh^2t}\,dt
&=\int\frac{h^2}{1+A w^2/(1-w^2)}\frac{1}{1-w^2}\,dw\\
&=\int\frac{h^2}{1+(A-1)w^2}\,dw\\
&=\int\frac{h^2}{1+h^2w^2}\,dw
=h\arctan(hw)+C.
\end{aligned}
$$

Here $h>0$ is fixed during integration, and $C$ is independent of $w$.

**Step 5 — CALCULUS.** Since $t=\operatorname{arsinh}(v/\sqrt A)$ and $w=v/\sqrt{A+v^2}$, endpoint evaluation gives

$$
K(h)=\operatorname{arsinh}\left(\frac1{\sqrt{1+h^2}}\right)
+h\arctan\left(\frac{h}{\sqrt{2+h^2}}\right)-\frac{\pi h}{4}.
$$

**Step 6 — ALGEBRA: a controlled remainder.** A more transparent form for small $h$ is

$$
K(h)=\ln(1+\sqrt2)-\frac{\pi h}{4}+E(h),
$$

where rationalizing the difference of roots yields

$$
\begin{aligned}
E(h)&=\int_0^1\frac{h^2}{(1+v^2)(\sqrt{1+v^2+h^2}+\sqrt{1+v^2})}\,dv,\\
0\le E(h)&\le\frac{h^2}{2}\int_0^1(1+v^2)^{-3/2}\,dv
=\frac{h^2}{2\sqrt2}.
\end{aligned}
$$

**Step 7 — DOMAIN AND CHECK.** The extension has $K(0)=\ln(1+\sqrt2)$ and right derivative $-\pi/4$. At each positive $h$, differentiation under the original finite area integral is valid and its kernel derivative is $-h(x^2+y^2+h^2)^{-3/2}$. At every nonzero spatial point that derivative tends to zero as $h\downarrow0$. Passing that pointwise limit through the area integral would give zero, contradicting the established slope. No integrable domination uniform through the source limit is available. Direct quadrature at fixed positive distances verifies the closed form; the remainder bound verifies the endpoint derivative without differentiating an asymptotic error symbol.

**Discussion.** Near-singular parameter limits can concentrate a derivative in an arbitrarily small spatial region. The coordinate reduction makes that contribution visible.

### I4-007

**Step 1 — SETUP.** The ellipsoid is compact, and its cap has finite nonnegative volume for every real $h$. Define the fixed real diagonal matrix $\mathbf D=\operatorname{diag}(a,b,c)$ and the real column vectors $\mathbf x=[x,y,z]^{\mathsf T}$ and $\mathbf u=[u_1,u_2,u_3]^{\mathsf T}$. The coordinate map $\mathbf x=\mathbf D\mathbf u$ has positive volume Jacobian $abc$.

**Step 2 — CHOICE.** Scaling removes the unequal semiaxes, while an orthogonal rotation can then remove the obliquity of the plane. The plane normal must undergo the scaling along with the ellipsoid; using $\|\mathbf n\|$ alone would lose the dependence on its direction relative to the semiaxes.

**Step 3 — ALGEBRA.** In the scaled coordinates the region satisfies

$$
\|\mathbf u\|^2\le1,\qquad
\mathbf m^{\mathsf T}\mathbf u\ge h,\qquad
\mathbf m=\mathbf D\mathbf n,
\qquad \rho=\|\mathbf m\|=\sqrt{a^2n_1^2+b^2n_2^2+c^2n_3^2}>0.
$$

An orthogonal change of coordinates takes $s=\mathbf m^{\mathsf T}\mathbf u/\rho$ as its last coordinate. Its absolute Jacobian is one. At fixed $s\in[-1,1]$, the other two coordinates fill a disk of area $\pi(1-s^2)$, and the plane condition becomes $s\ge\zeta$, where $\zeta=h/\rho$.

**Step 4 — CALCULUS.** For $-1<\zeta<1$, Fubini's theorem applies to the bounded indicator of the cap and gives

$$
\begin{aligned}
V(h)&=\pi abc\int_\zeta^1(1-s^2)\,ds\\
&=\pi abc\left(\frac23-\zeta+\frac{\zeta^3}{3}\right)
=\frac{\pi abc}{3}(1-\zeta)^2(2+\zeta).
\end{aligned}
$$

The factored last form avoids subtracting nearly equal constant and linear terms when the cap is small. The full result is

$$
V(h)=\begin{cases}
4\pi abc/3,&h\le-\rho,\\
\displaystyle\frac{\pi abc}{3}(1-h/\rho)^2(2+h/\rho),&-\rho<h<\rho,\\
0,&h\ge\rho.
\end{cases}
$$

At $h=\rho$ the cap consists of one tangent point and has zero volume. At $h=-\rho$ the inequality includes the whole ellipsoid.

**Step 5 — CALCULUS AND DOMAIN.** Differentiating inside the middle interval gives

$$
\frac{d}{dh}(V(h))=-\frac{\pi abc}{\rho}\left(1-\frac{h^2}{\rho^2}\right),
\qquad |h|<\rho.
$$

Outside this interval the derivative is zero. The factored formula shows that the disappearing cap volume is quadratic in the distance to the tangent offset; by reflection the missing volume at the opposite endpoint is also quadratic. Thus the derivative exists and equals zero at both $h=\pm\rho$. It is continuous everywhere. The interior second derivative $2\pi abc h/\rho^3$ has nonzero one-sided limits at those endpoints, whereas the exterior second derivative is zero; the volume function is not twice differentiable there.

**Step 6 — CHECK: physical sections.** Let $A_{\rm sec}(h)$ be the ordinary planar area of the section at $\mathbf n^{\mathsf T}\mathbf x=h$ for $|h|<\rho$. Its planes move a perpendicular distance $dh/\|\mathbf n\|$ when their offsets increase by $dh$. Resolving Euclidean volume into sections therefore gives

$$
-\frac{d}{dh}(V(h))=\frac{A_{\rm sec}(h)}{\|\mathbf n\|},
\qquad
A_{\rm sec}(h)=\frac{\pi abc\|\mathbf n\|}{\rho}\left(1-\frac{h^2}{\rho^2}\right).
$$

The normal-length factor is required because $\mathbf n$ need not be a unit vector. Independently, central symmetry implies $V(h)+V(-h)=4\pi abc/3$, which the formula satisfies. For a sphere of radius $a=b=c=R$ with a unit normal and cap height $H=R-h$, it reduces to $\pi H^2(3R-H)/3$ on $0\le H\le2R$.

**Discussion.** A linear scaling changes both the integration measure and the plane normal. The tangent cases are best checked with the cap volume itself, rather than by extending a formula beyond the region that produced it.

### I4-008

**Step 1 — SETUP.** For positive $a,b$ the integrand is continuous at zero with value $1/(a^2b^2)$. For $x\ge1$ it is bounded by $x^{-4}$, so the improper integral converges absolutely. No pole lies on the real integration interval.

**Step 2 — CHOICE.** Partial fractions reduce the unequal-parameter case to two familiar convergent integrals. Their combined expression should be simplified before evaluating nearby parameters. A parameter derivative handles the repeated denominator without dividing by a small parameter difference.

**Step 3 — CALCULUS.** For $a\ne b$,

$$
\frac{1}{(x^2+a^2)(x^2+b^2)}
=\frac{1}{b^2-a^2}\left(\frac{1}{x^2+a^2}-\frac{1}{x^2+b^2}\right).
$$

The coordinate $x=a u$ gives $\int_0^\infty(x^2+a^2)^{-1}dx=\pi/(2a)$ by the arctangent primitive. Consequently,

$$
J(a,b)=\frac{\pi}{2(b^2-a^2)}\left(\frac1a-\frac1b\right).
$$

**Step 4 — ALGEBRA.** Factoring before cancellation gives

$$
J(a,b)=\frac{\pi(b-a)}{2ab(b-a)(b+a)}
=\frac{\pi}{2ab(a+b)},\qquad a\ne b.
$$

The last expression involves only positive sums and products and avoids the subtraction of nearly equal terms. Its continuous value at $a=b$ is $\pi/(4a^3)$.

**Step 5 — CALCULUS: the coincident case.** To verify that value directly, let $P(a)=\int_0^\infty(x^2+a^2)^{-1}dx$. On a compact parameter neighborhood $0<m\le a\le M$, its derivative kernel is bounded in magnitude by $2M/(x^2+m^2)^2$, which is integrable. Therefore

$$
\frac{d}{da}(P(a))=-2a\int_0^\infty\frac{1}{(x^2+a^2)^2}\,dx
=-\frac{\pi}{2a^2},
$$

and the repeated-denominator integral is $J(a,a)=\pi/(4a^3)$. Thus the stable expression applies for every positive pair, including equality.

**Step 6 — CALCULUS AND DOMAIN.** Local positive lower bounds on both parameters also dominate the derivative of the original integrand. With $b$ held fixed,

$$
\begin{aligned}
\frac{\partial}{\partial a}(J(a,b))
&=-2a\int_0^\infty\frac{1}{(x^2+a^2)^2(x^2+b^2)}\,dx\\
&=-\frac{\pi}{2ab(a+b)}\left(\frac1a+\frac{1}{a+b}\right).
\end{aligned}
$$

For instance, on $m\le a,b\le M$ the first derivative kernel is bounded by $2M/(x^2+m^2)^3$. This justifies the displayed interchange locally. As $a\downarrow0$ with $b>0$ fixed, $J(a,b)$ behaves as $\pi/(2ab^2)$ and diverges. At $a=0$ the original kernel has a nonintegrable $x^{-2}$ singularity at zero; the positive-parameter domain is essential.

**Step 7 — CHECK.** The formula is symmetric in $a,b$ and decreases strictly as either parameter increases, in agreement with the positive integrand. Scaling both parameters by $\lambda>0$ and setting $x=\lambda u$ multiplies the integral by $\lambda^{-3}$, which the result respects. At equality, the partial derivative with $b$ held fixed is $-3\pi/(8a^4)$. The derivative of $J(a,a)=\pi/(4a^3)$ along the diagonal is twice that value, since both parameters then vary. Direct quadrature checks unequal and nearly coincident cases without using the partial-fraction subtraction.

**Discussion.** A removable singularity in a derived expression may be numerically damaging even when the original integral is regular. Algebraic simplification and an independent parameter calculation resolve different parts of that issue.

### I4-009

**Step 1 — SETUP.** Positive definiteness gives a smallest eigenvalue $m_0>0$. For every real $s\ge0$, define the symmetric resolvent $\mathbf R(s)=(\mathbf A+s\mathbf I_n)^{-1}$. The norm used here is the matrix operator norm induced by the Euclidean vector norm. The spectral theorem gives

$$
\|\mathbf R(s)\|\le\frac{1}{m_0+s},\qquad
\|\mathbf R(s)^2\|\le\frac{1}{(m_0+s)^2}.
$$

The latter bound is integrable over the half-line and bounds every matrix entry. The improper matrix integral is therefore well defined entrywise and in this norm.

**Step 2 — CHOICE.** The square of the inverse is the derivative of a simpler resolvent in the scalar integration coordinate. This gives a matrix primitive without choosing eigenvectors that might vary with the later perturbation parameter.

**Step 3 — CALCULUS.** Differentiating $(\mathbf A+s\mathbf I_n)\mathbf R(s)=\mathbf I_n$ with $\mathbf A$ held fixed gives

$$
\mathbf R(s)+(\mathbf A+s\mathbf I_n)\frac{d}{ds}(\mathbf R(s))=\mathbf0,
\qquad \frac{d}{ds}(\mathbf R(s))=-\mathbf R(s)^2.
$$

Hence for a real cutoff $S>0$,

$$
\int_0^S\mathbf R(s)^2\,ds
=\mathbf A^{-1}-(\mathbf A+S\mathbf I_n)^{-1}.
$$

The last inverse has norm at most $1/(m_0+S)$ and tends to zero. It follows that

$$
\mathbf M(\mathbf A)=\mathbf A^{-1}.
$$

**Step 4 — CALCULUS: ordered perturbation terms.** For the stated matrix path, set $\mathbf R(t,s)=(\mathbf A(t)+s\mathbf I_n)^{-1}$. The inverse identity, differentiated with $s$ fixed, gives

$$
\frac{\partial}{\partial t}(\mathbf R(t,s))
=-\mathbf R(t,s)\frac{d}{dt}(\mathbf A(t))\mathbf R(t,s).
$$

At $t=t_0$, abbreviate $\mathbf R_0(s)=\mathbf R(t_0,s)$. The product rule then gives two distinct ordered terms:

$$
\left.\frac{\partial}{\partial t}(\mathbf R(t,s)^2)\right|_{t=t_0}
=-\mathbf R_0(s)\mathbf H\mathbf R_0(s)^2
-\mathbf R_0(s)^2\mathbf H\mathbf R_0(s).
$$

Moving $\mathbf H$ through either resolvent is not justified in general.

**Step 5 — DOMAIN: interchange on a parameter neighborhood.** Let $m_*>0$ be the smallest eigenvalue of $\mathbf A_0$. Continuity of the symmetric matrix path supplies a neighborhood of $t_0$ on which $\|\mathbf A(t)-\mathbf A_0\|<m_*/2$. The quadratic-form bound then gives the fixed lower eigenvalue bound $m=m_*/2>0$ throughout this neighborhood. Continuous differentiability also gives a bound $\|\frac{d}{dt}(\mathbf A(t))\|\le K$ on a smaller closed neighborhood. Consequently,

$$
\left\|\frac{\partial}{\partial t}(\mathbf R(t,s)^2)\right\|
\le\frac{2K}{(m+s)^3},\qquad
\int_0^\infty\frac{2K}{(m+s)^3}\,ds=\frac{K}{m^2}<\infty.
$$

This uniform domination justifies differentiation through the entrywise improper integral at $t_0$. The argument is local in the positive-definite region. At a zero eigenvalue the corresponding scalar integral contains $s^{-2}$ at zero; at a negative eigenvalue it has a pole at positive $s$. Those matrices are outside the stated domain.

**Step 6 — ALGEBRA AND CALCULUS.** With $\mathbf H$ fixed during integration in $s$,

$$
\frac{d}{ds}(\mathbf R_0(s)\mathbf H\mathbf R_0(s))
=-\mathbf R_0(s)^2\mathbf H\mathbf R_0(s)
-\mathbf R_0(s)\mathbf H\mathbf R_0(s)^2.
$$

Its value tends to zero as $s\to\infty$, by the bound $\|\mathbf H\|/(m_*+s)^2$. Integrating the ordered derivative terms therefore gives

$$
\left.\frac{d}{dt}(\mathbf M(\mathbf A(t)))\right|_{t=t_0}
=-\mathbf A_0^{-1}\mathbf H\mathbf A_0^{-1}.
$$

**Step 7 — CHECK.** Differentiating the independently established identity $\mathbf A(t)\mathbf M(\mathbf A(t))=\mathbf I_n$ also yields this ordered formula. In a fixed eigenbasis of $\mathbf A_0$ with positive eigenvalues $\lambda_i$, write $\widetilde{\mathbf H}$ for the perturbation in that basis. The derivative's $(i,j)$ entry is $-\widetilde H_{ij}/(\lambda_i\lambda_j)$, which shows why replacing the product by $-\mathbf A_0^{-2}\mathbf H$ would fail for a noncommuting perturbation. For $n=1$ the answer reduces to the scalar derivative of $1/A_0$.

**Discussion.** A scalar integration parameter can provide a useful matrix primitive. A later perturbation requires ordered product rules and a uniform spectral gap; scalar division rules do not supply either condition.

### I4-010

**Step 1 — SETUP.** Both bounds are finite at every finite $t$. The smooth kernel gives a finite oriented integral even when $t<-L$; in that case the response is negative. The parameter $L$ stays fixed throughout differentiation in $t$.

**Step 2 — CHOICE.** A coordinate following the Gaussian center transfers all parameter dependence to one integration endpoint. The original-coordinate Leibniz rule gives a separate check on the cancellation between boundary motion and kernel motion.

**Step 3 — CALCULUS: a relative coordinate.** Set $u=t-x$ with $t$ held fixed during integration. At $x=-L$ the new coordinate is $u=t+L$, and at $x=t$ it is zero; the derivative $dx/du=-1$ reverses the bounds. Thus, with orientation preserved for either sign of $t+L$,

$$
G(t;L)=\int_0^{t+L}\exp(-u^2)\,du
=\frac{\sqrt\pi}{2}\operatorname{erf}(t+L),
\qquad
\operatorname{erf}(v)=\frac{2}{\sqrt\pi}\int_0^v\exp(-u^2)\,du.
$$

The displayed integral defines the real error function locally. The fundamental theorem and chain rule give

$$
\frac{d}{dt}(G(t;L))=\exp(-(t+L)^2),\qquad
\frac{d^2}{dt^2}(G(t;L))=-2(t+L)\exp(-(t+L)^2).
$$

**Step 4 — CALCULUS AND ALGEBRA: the original coordinate.** The parameter derivative of the kernel, with $x$ fixed, is $2(x-t)\exp(-(x-t)^2)$. The moving upper endpoint contributes one, and the fixed lower endpoint contributes zero. Hence

$$
\begin{aligned}
\frac{d}{dt}(G(t;L))
&=1+\int_{-L}^t2(x-t)\exp(-(x-t)^2)\,dx\\
&=1-\left.\exp(-(x-t)^2)\right|_{x=-L}^{x=t}\\
&=1-1+\exp(-(t+L)^2).
\end{aligned}
$$

On a compact neighborhood of any finite input, all integration bounds lie in one bounded $x$ interval; the kernel and its parameter derivatives are continuous there. The Leibniz rule is therefore valid locally for every real $t$, including $t=-L$ and the negatively oriented cases.

**Step 5 — CALCULUS: the Gaussian mass.** Let $I=\int_0^\infty\exp(-u^2)\,du$. The integral is finite, for example by comparison with $\exp(-u)$ for $u\ge1$. Tonelli's theorem for the nonnegative product and polar coordinates in the first quadrant give

$$
I^2=\int_0^{\pi/2}\int_0^\infty\exp(-r^2)r\,dr\,d\theta
=\frac\pi2\cdot\frac12=\frac\pi4.
$$

Since $I>0$, it equals $\sqrt\pi/2$. Oddness of the oriented integral in its upper bound consequently gives

$$
\lim_{t\to+\infty}G(t;L)=\frac{\sqrt\pi}{2},\qquad
\lim_{t\to-\infty}G(t;L)=-\frac{\sqrt\pi}{2}.
$$

**Step 6 — DOMAIN: controlled limiting errors.** For a positive real $T$,

$$
0<\int_T^\infty\exp(-u^2)\,du
\le\frac1T\int_T^\infty u\exp(-u^2)\,du
=\frac{\exp(-T^2)}{2T}.
$$

Taking $T=|t+L|>0$ gives

$$
\left|G(t;L)-\frac{\sqrt\pi}{2}\operatorname{sgn}(t+L)\right|
\le\frac{\exp(-(t+L)^2)}{2|t+L|}.
$$

Here $\operatorname{sgn}(v)$ is one for $v>0$ and minus one for $v<0$. The bound describes either distant limit and is not asserted at $t=-L$, where $G(-L;L)=0$ exactly.

**Step 7 — CHECK.** The first derivative is strictly positive, and the second derivative changes sign at $t=-L$. Both facts agree with the shifted integral: as its upper endpoint increases it accumulates a positive Gaussian, with its largest slope at the Gaussian center. The identity $G(-L+v;L)=-G(-L-v;L)$ and the value $\frac{d}{dt}(G(t;L))|_{t=-L}=1$ check both orientation and translation. Direct original-coordinate quadrature and finite differences provide a separate numerical check.

**Discussion.** A moving integration bound can reverse the sign of an integral without invalidating its definition. Moving the coordinate with the kernel reveals a derivative that is partly concealed by cancellation in the original coordinate.

### I4-011

**Step 1 — SETUP.** The aperture domain is compact and the complex integrand has magnitude one. The integral exists absolutely and has units of area, with $|F(q;a)|\le\pi a^2$. The angular reflection that reverses $\cos\theta$ conjugates the exponential, so the imaginary parts cancel. Thus $F(q;a)$ is real and even in real $q$.

**Step 2 — CHOICE.** The exponential series converges absolutely and uniformly for $0\le r\le a$ and $0\le\theta\le2\pi$ at each fixed $q$. Its angular moments select only even powers. This identifies the special function while also producing a regular formula at zero.

**Step 3 — CALCULUS: angular moments.** Odd cosine moments vanish by reflection. For nonnegative integers $m$, integration by parts gives the recurrence for even moments and its iterated value:

$$
\int_0^{2\pi}(\cos\theta)^{2m}\,d\theta
=2\pi\frac{(2m)!}{2^{2m}(m!)^2}.
$$

For $m\ge1$ the recurrence multiplies the preceding even moment by $(2m-1)/(2m)$, starting from $2\pi$ at $m=0$. Integrating the exponential series termwise therefore gives

$$
\int_0^{2\pi}\exp(\mathrm i z\cos\theta)\,d\theta
=2\pi J_0(z),\qquad
J_0(z)=\sum_{m=0}^\infty\frac{(-1)^m(z/2)^{2m}}{(m!)^2}.
$$

This defines the real order-zero Bessel function for real $z$. The real order-one function needed below is defined by the everywhere convergent series

$$
J_1(z)=\sum_{m=0}^\infty\frac{(-1)^m(z/2)^{2m+1}}{m!(m+1)!}.
$$

The series definitions agree with the angular representation in [NIST DLMF 10.9](https://dlmf.nist.gov/10.9). Only the locally stated series and angular calculation are needed here.

**Step 4 — CALCULUS AND ALGEBRA: radial integration.** Uniform convergence on the finite radial interval also permits termwise integration there:

$$
\begin{aligned}
F(q;a)&=2\pi\int_0^a r J_0(qr)\,dr\\
&=2\pi\sum_{m=0}^\infty
\frac{(-1)^m q^{2m}a^{2m+2}}{2^{2m}(m!)^2(2m+2)}\\
&=\pi a^2\sum_{m=0}^\infty
\frac{(-1)^m(qa)^{2m}}{4^m m!(m+1)!}.
\end{aligned}
$$

For $q\ne0$ this is $2\pi aJ_1(qa)/q$. The complete expression, including zero, is

$$
F(q;a)=\begin{cases}
2\pi aJ_1(qa)/q,&q\ne0,\\
\pi a^2,&q=0.
\end{cases}
$$

**Step 5 — DOMAIN.** The series gives $J_1(z)=z/2+O(z^3)$ at zero, so the quotient has the stated removable limit. The oddness of $J_1$ makes this quotient even in signed $q$, as the original integral requires. No absolute value needs to be inserted into the signed denominator. The finite-domain integral and its series are smooth for every real $q$; differentiating under the integral is locally dominated by bounded powers of $r$.

**Step 6 — TRICK: an explicit small-wavenumber error.** For every real $v$, the Taylor estimate for the cosine gives $|\cos v-1+v^2/2|\le v^4/24$. Also $\cos v\ge1-v^2/2$, so the same remainder is nonnegative. Applying these inequalities to $v=qr\cos\theta$ and integrating yields

$$
F(q;a)=\pi a^2-\frac{\pi a^4q^2}{8}+E(q;a),
$$

because $\int_0^{2\pi}(\cos\theta)^2d\theta=\pi$ and $\int_0^a r^3dr=a^4/4$. The fourth moment and radial integral give the rigorous bound

$$
\begin{aligned}
0\le E(q;a)
&\le\frac{q^4}{24}\left(\int_0^a r^5\,dr\right)
\left(\int_0^{2\pi}(\cos\theta)^4\,d\theta\right)\\
&=\frac{q^4}{24}\cdot\frac{a^6}{6}\cdot\frac{3\pi}{4}
=\frac{\pi a^6q^4}{192}.
\end{aligned}
$$

The inequality holds for all real $q$, while it is a useful small-parameter estimate when $|qa|$ is small. Its error relative to the aperture area is at most $(qa)^4/192$.

**Step 7 — CHECK.** At zero the original integrand is one, so the answer is the geometric disk area. Independently, differentiating the original integral twice at zero gives minus the disk's $x$-coordinate second moment, $-\pi a^4/4$. This agrees with the quadratic coefficient above. Scaling $r=a u$ gives $F(q;a)=a^2F(qa;1)$, also respected by the Bessel formula and the error bound. Direct angular/radial quadrature checks both signs of $q$ and the oscillatory cases.

**Discussion.** A special-function quotient can be regular at a parameter value where its displayed denominator vanishes. A series identifies that value, while a direct Taylor estimate controls the approximation without relying on a formal truncation.
