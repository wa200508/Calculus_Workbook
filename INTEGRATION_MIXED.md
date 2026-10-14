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

**Objects and dependencies.** Independent real dimensionless coordinates satisfy $0\le y\le x\le1$. The independent real observation parameter is $h>0$. Evaluate the real scalar integral

$$
K(h)=\int_0^1\int_0^x\frac{1}{\sqrt{x^2+y^2+h^2}}\,dy\,dx.
$$

Determine its continuous limit at $h=0$, its right derivative there, and an explicit bound on the error in its linear small-$h$ approximation. Explain whether the limit of the parameter derivative may be passed through the original area integral.

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

**Step 4 — DOMAIN.** As $a\downarrow0$, the answer tends to $+\infty$. At $a=0,b>0$, the numerator tends to one at infinity, leaving a nonintegrable $1/x$ tail. The positive-parameter interchange does not extend to that endpoint.

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

**Step 5 — DOMAIN.** For positive $b,c$, the damping limit is $\ln(c/b)$. The undamped ordinary integral also exists: integration by parts bounds each cosine tail divided by $x$ by a constant times $1/(bA)$ or $1/(cA)$ beyond $A>0$. The same bounds are uniform in $a\ge0$ because $\exp(-ax)/x$ decreases. Finite-interval convergence and these bounds justify the damping limit. If $b=0<c$, the limit diverges to $+\infty$; if $c=0<b$, it diverges to $-\infty$. If both vanish, the integral is identically zero.

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
