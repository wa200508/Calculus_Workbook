# D4 · Nonlinear scalar and parameter problems

## Problems

### D4-001 — A variable power near an excluded input

**Objects and dependencies.** $x$ is an independent real scalar, $x\ne0$. The real scalar function is

$$
f(x)=\bigl(\ln(1+x^2)\bigr)^{\arctan x}.
$$

Determine its derivative on its domain and whether it has a continuous, differentiable extension at $x=0$. The real power is defined through the logarithm of its positive base.

### D4-002 — An angle defined by a hyperbolic function

**Objects and dependencies.** $x\in\mathbb R$ is an independent dimensionless real scalar. The dependent real angle is $\theta(x)=\arccos(\tanh x)$ in $(0,\pi)$. Determine its first and second derivatives, with a representation valid for every finite real $x$.

### D4-003 — A logarithmic ratio of radicals

**Objects and dependencies.** $x\in\mathbb R$ is an independent real scalar and

$$
f(x)=\ln\left(\frac{\sqrt{1+x^2}+x}{\sqrt{1+x^2}-x}\right).
$$

Determine the real domain, the derivative, and an equivalent expression that avoids subtracting nearly equal positive quantities for large positive $x$.

### D4-004 — A coupled quadric and a constrained path

**Objects and dependencies.** The real scalar level function is $F(x,y,z)=x^2+2xz+2z^2+y^2-1$. On its upper height branch, the dependent scalar $z=g(x,y)$ satisfies $F(x,y,g(x,y))=0$ and $x+2g(x,y)>0$. Determine the height and its partial derivatives on their open domain. Along the real path $x(t)=\cos t$, $y(t)=\sin t/\sqrt2$, determine $\frac{d}{dt}(g(x(t),y(t)))$ and verify it using both a path formula and the explicit height.

### D4-005 — A complex response with a delay parameter

**Objects and dependencies.** $\omega\in\mathbb R$ is an independent real angular frequency. Fixed real times $\tau>0$ and $T\ge0$ define the complex scalar response

$$
H(\omega;\tau,T)=\frac{1+\mathrm{i}\omega\tau}{1-\mathrm{i}\omega\tau}\exp(-\mathrm{i}\omega T),\qquad \mathrm{i}^2=-1.
$$

Determine a continuous real phase with value zero at $\omega=0$, its frequency derivative, and the scalar quantity $-\frac{\partial}{\partial\omega}(\phi(\omega;\tau,T))$. State when the latter is negative and what happens if the principal phase is used instead.

### D4-006 — An integral with two moving endpoints

**Objects and dependencies.** $t\in\mathbb R$ is an independent dimensionless real scalar. The real integration variable is $s$, and the real scalar function is

$$
F(t)=\int_{t^2}^{\exp t}\frac{\exp(-ts^2)}{1+s^2}\,ds.
$$

Determine its derivative for finite real $t$ and evaluate it at zero. The integral is oriented if the endpoints reverse order. A general elementary closed form for $F(t)$ is not required.

## Hint ladders

### D4-001

1. The base and exponent both depend on the independent variable.
2. A logarithm of the function converts its exponent into a multiplicative factor.
3. Near zero, the logarithm of the base behaves as $2\ln|x|$, while $\arctan x$ behaves as $x$.

### D4-002

1. The defining relation $\cos(\theta(x))=\tanh x$ can be differentiated implicitly.
2. The selected angle range determines the sign of its sine.
3. The identity $1-\tanh^2x=1/\cosh^2x$ resolves the square root.

### D4-003

1. The two radical expressions have a useful product.
2. The product is one, and each factor is positive.
3. The logarithmic ratio reduces to twice a logarithm, with an inverse hyperbolic interpretation.

### D4-004

1. The quadratic equation in the height has discriminant proportional to $2-x^2-2y^2$.
2. The height branch specifies the sign of the square root.
3. Along the prescribed path the radicand is identically one.

### D4-005

1. The rational factor has unit magnitude and conjugate numerator and denominator.
2. A continuous phase is the difference of their local arguments, plus the exponential phase.
3. The negative phase derivative need not be positive for the stated mathematical response.

### D4-006

1. The parameter enters the upper endpoint, lower endpoint, and integrand.
2. The derivative therefore has two boundary terms and an integral term.
3. At zero the remaining rational integral can be decomposed as $s^2/(1+s^2)=1-1/(1+s^2)$.

## Complete solutions

### D4-001

**Step 1 — SETUP.** The real base $a(x)=\ln(1+x^2)$ is positive for $x\ne0$. The real exponent is $b(x)=\arctan x$, and the output $f(x)>0$ is differentiable on each component of the punctured real line.

**Step 2 — CHOICE.** The variable exponent prevents direct use of the fixed-exponent power rule. The representation $f(x)=\exp(b(x)\ln(a(x)))$ separates the two dependencies.

**Step 3 — CALCULUS.** The chain and product rules give

$$
\frac{d}{dx}\left(f(x)\right)
=f(x)\left(\frac{\ln(\ln(1+x^2))}{1+x^2}
+\frac{2x\arctan x}{(1+x^2)\ln(1+x^2)}\right),\qquad x\ne0.
$$

**Step 4 — TRICK: local expansion.** The real Taylor expansions in [T-002](TRICKS_APPENDIX.md#t-002-taylor-expansions) give $\ln(1+x^2)=x^2(1+O(x^2))$ and $\arctan x=x+O(x^3)$ as $x\to0$. Consequently,

$$
\ln(f(x))=2x\ln|x|+O(x^3|\ln|x||)+O(x^3)\longrightarrow0.
$$

**Step 5 — DOMAIN.** The unique continuous extension has value $\widetilde f(0)=1$. Since $\exp(s)-1=s+O(s^2)$ near $s=0$, its difference quotient satisfies

$$
\frac{\widetilde f(x)-\widetilde f(0)}{x}
=2\ln|x|+o(1)\longrightarrow-\infty.
$$

The error from the exponential, divided by $x$, is $O(|x|\ln^2|x|)\to0$. Thus the extension has no finite derivative at zero.

**Step 6 — CHECK.** For $x\ne0$, the original derivative formula divided by $f(x)$ is the derivative of $\ln(f(x))$. Its second term tends to two, while the first tends to $-\infty$, consistent with the endpoint analysis. A finite function limit does not supply differentiability.

**Recognition cue.** Variable powers require both derivatives and an explicit positive-base domain. Extension of the value and extension of a finite derivative are separate questions.

### D4-002

**Step 1 — SETUP.** At every finite real input, $-1<\tanh x<1$, and $0<\theta(x)<\pi$. The inverse cosine branch and its derivatives are therefore defined.

**Step 2 — CHOICE.** Implicit differentiation of the defining cosine relation avoids a nested inverse-function quotient and makes the sign choice visible.

**Step 3 — CALCULUS.** Differentiation with respect to $x$ gives

$$
-\sin(\theta(x))\frac{d}{dx}\left(\theta(x)\right)=\frac{1}{\cosh^2x}.
$$

**Step 4 — TRICK: hyperbolic identities.** By [T-007](TRICKS_APPENDIX.md#t-007-hyperbolic-identities-and-real-branches), and the positive sine on the chosen branch,

$$
\sin(\theta(x))=\sqrt{1-\tanh^2x}=\frac{1}{\cosh x}.
$$

**Step 5 — ALGEBRA.** Division by the strictly positive sine gives

$$
\frac{d}{dx}\left(\theta(x)\right)=-\frac{1}{\cosh x}.
$$

**Step 6 — CALCULUS.** Differentiation of the complete first derivative yields

$$
\frac{d}{dx}\left(\frac{d}{dx}\left(\theta(x)\right)\right)
=\frac{\sinh x}{\cosh^2x}.
$$

**Step 7 — CHECK AND DOMAIN.** $\cosh x\ge1$ excludes finite denominator zeros. At $x=0$, the angle is $\pi/2$, its first derivative is $-1$, and its second derivative is zero. The angle decreases from a limit of $\pi$ to a limit of zero as $x$ increases; those limiting angles are not attained at finite inputs.

**Recognition cue.** An inverse-function derivative can simplify considerably after the defining relation and branch sign are retained.

### D4-003

**Step 1 — SETUP.** The independent variable is real, and the square root is nonnegative. For every finite $x$, $\sqrt{1+x^2}>|x|$, so both logarithmic factors are positive and the domain is all of $\mathbb R$.

**Step 2 — CHOICE.** The conjugate product can remove the denominator before the logarithm is differentiated. This avoids a long quotient-rule calculation and preserves positivity.

**Step 3 — ALGEBRA.** The exact identity

$$
(\sqrt{1+x^2}+x)(\sqrt{1+x^2}-x)=1+x^2-x^2=1
$$

implies that the ratio is $(\sqrt{1+x^2}+x)^2$. Thus

$$
f(x)=2\ln(\sqrt{1+x^2}+x).
$$

**Step 4 — CALCULUS.** Logarithmic and chain differentiation give

$$
\frac{d}{dx}\left(f(x)\right)
=2\frac{x/\sqrt{1+x^2}+1}{\sqrt{1+x^2}+x}.
$$

**Step 5 — ALGEBRA.** The numerator is $(x+\sqrt{1+x^2})/\sqrt{1+x^2}$, so cancellation on the positive domain gives $\frac{d}{dx}(f(x))=2/\sqrt{1+x^2}$.

**Step 6 — TRICK AND CHECK.** The real inverse identity in [T-007](TRICKS_APPENDIX.md#t-007-hyperbolic-identities-and-real-branches) gives $f(x)=2\operatorname{arsinh}x$. For large positive $x$ this representation avoids the small difference in the original denominator. For negative $x$, oddness gives $f(x)=-2\ln(\sqrt{1+x^2}-x)$, avoiding cancellation in the other factor. The reciprocal factors also show $f(-x)=-f(x)$ directly.

**Recognition cue.** Algebraic equivalence can improve both differentiation and numerical evaluation. The stable representation depends on the sign of the input.

### D4-004

**Step 1 — SETUP.** Independent real $x,y$ determine a dependent real height. The path parameter $t$ is an independent real angle. The condition $x+2g(x,y)>0$ selects one height branch.

**Step 2 — CHOICE.** A quadratic solution establishes the graph domain; implicit differentiation organizes the coordinate partials. The derivative along the path then combines both partials, rather than holding either path coordinate fixed.

**Step 3 — ALGEBRA.** The quadratic formula gives

$$
g(x,y)=\frac{-x+\sqrt{D(x,y)}}2,\qquad D(x,y)=2-x^2-2y^2>0.
$$

On this branch $2x+4g(x,y)=2\sqrt{D(x,y)}$.

**Step 4 — CALCULUS.** The level partials are $2x+2z$, $2y$, and $2x+4z$. Hence

$$
\frac{\partial}{\partial x}(g(x,y))=-\frac12-\frac{x}{2\sqrt{D(x,y)}},\qquad
\frac{\partial}{\partial y}(g(x,y))=-\frac{y}{\sqrt{D(x,y)}}.
$$

**Step 5 — ALGEBRA AND DOMAIN.** On the path, $D(x(t),y(t))=2-\cos^2t-\sin^2t=1$. Every finite real $t$ remains strictly inside the graph domain. At $D=0$ the two height branches meet and the height partials are not supplied by these formulas; the full quadric surface remains regular because its gradient vanishes only at the origin, which is not on $F=0$.

**Step 6 — CALCULUS.** The path derivatives are $-\sin t$ and $\cos t/\sqrt2$, so

$$
\begin{aligned}
\frac{d}{dt}\left(g(x(t),y(t))\right)
&=\left(-\frac12-\frac{\cos t}{2}\right)(-\sin t)
-\frac{\sin t}{\sqrt2}\frac{\cos t}{\sqrt2}\\
&=\frac{\sin t}{2}+\frac{\cos t\sin t}{2}-\frac{\sin t\cos t}{2}
=\frac{\sin t}{2}.
\end{aligned}
$$

**Step 7 — CHECK.** Direct substitution gives $g(x(t),y(t))=(1-\cos t)/2$, whose derivative agrees. Cancellation of the mixed path contributions is a consequence of this specific constraint, not permission to omit either coordinate derivative.

**Recognition cue.** A complicated height formula may simplify on a constrained path. The graph domain and the path dependence are assessed separately.

### D4-005

**Step 1 — SETUP.** The parameters $\tau,T$ are fixed, and the response is nonzero for every real $\omega$. Its magnitude is one because $|1+\mathrm{i}\omega\tau|=|1-\mathrm{i}\omega\tau|$.

**Step 2 — CHOICE.** A continuous phase can be assembled from the two factors whose real parts equal one, avoiding principal-argument jumps during differentiation.

**Step 3 — CALCULUS.** The required real phase and its derivative are

$$
\phi(\omega;\tau,T)=2\arctan(\omega\tau)-\omega T,\qquad
\frac{\partial}{\partial\omega}\left(\phi(\omega;\tau,T)\right)
=\frac{2\tau}{1+\omega^2\tau^2}-T.
$$

**Step 4 — ALGEBRA.** The negative derivative is $T-2\tau/(1+\omega^2\tau^2)$. For $T=0$ it is negative for every finite frequency. For $0<T<2\tau$ it is negative precisely when

$$
|\omega|<\frac{\sqrt{2\tau/T-1}}{\tau}.
$$

For $T\ge2\tau$ it is nonnegative everywhere, with equality at zero when $T=2\tau$.

**Step 5 — DOMAIN.** A principal phase agrees locally with this phase plus an integer multiple of $2\pi$. Its derivative agrees on each smooth chart, but it is undefined at any branch jump. No causality or passivity assumption has been imposed on this mathematical frequency response; such physical conditions cannot be inferred from its unit magnitude.

**Step 6 — CHECK.** The quotient rule or a complex logarithmic derivative gives $\frac{\partial}{\partial\omega}(H)/H=\mathrm{i}(2\tau/(1+\omega^2\tau^2)-T)$, a purely imaginary scalar consistent with constant magnitude. The negative derivative has units of time.

**Recognition cue.** A continuous phase representation separates parameter sensitivity from branch artifacts. A mathematical response formula alone does not impose additional physical constraints.

### D4-006

**Step 1 — SETUP.** Both endpoints are finite nonnegative real scalars for finite $t$. The kernel $q(s,t)=\exp(-ts^2)/(1+s^2)$ is real and smooth for all real $s,t$.

**Step 2 — CHOICE.** A primitive of the parameter-dependent kernel is unnecessary. The variable-limit rule accounts separately for its parameter dependence and both endpoint velocities.

**Step 3 — CALCULUS.** With $s$ fixed, $\frac{\partial}{\partial t}(q(s,t))=-s^2\exp(-ts^2)/(1+s^2)$. The endpoint derivatives are $2t$ and $\exp t$. Consequently,

$$
\begin{aligned}
\frac{d}{dt}\left(F(t)\right)
={}&\frac{\exp t\,\exp(-t\exp(2t))}{1+\exp(2t)}
-\frac{2t\exp(-t^5)}{1+t^4}\\
&-\int_{t^2}^{\exp t}\frac{s^2\exp(-ts^2)}{1+s^2}\,ds.
\end{aligned}
$$

**Step 4 — DOMAIN.** On a neighborhood of any finite $t$, the endpoints and integrand partial are contained in a compact rectangle and remain bounded. The local differentiation theorem therefore applies for every real $t$, including values at which the endpoints coincide or reverse order.

**Step 5 — ALGEBRA.** At $t=0$ the boundary terms reduce to $1/2$ and zero. The remaining integral is

$$
\int_0^1\frac{s^2}{1+s^2}\,ds
=\int_0^1\left(1-\frac{1}{1+s^2}\right)\,ds=1-\frac\pi4.
$$

**Step 6 — RESULT AND CHECK.** The requested derivative is $\frac{d}{dt}(F(t))|_{t=0}=\pi/4-1/2$. Also $F(0)=\pi/4$. The first boundary contribution is positive at zero, while the interior contribution is negative; both are needed to obtain the stated slope. Independent finite differences of the original integral verify the value.

**Recognition cue.** A derivative of an integral can be tractable even when its parameter-dependent antiderivative is not. Endpoint motion and interior dependence produce distinct terms.
