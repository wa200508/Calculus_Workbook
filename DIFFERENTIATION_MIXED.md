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

### D4-007 — A finite value with an oscillating slope

**Objects and dependencies.** $x\ne0$ is an independent dimensionless real scalar. The dependent positive real scalar is

$$
f(x)=(1+x^2)^{\sin(1/x)},
$$

where the real power uses the logarithm of its positive base. Determine the continuous extension at zero, its derivative at zero, and whether the derivative of that extension is continuous there. Obtain an explicit derivative for $x\ne0$ and justify any limiting conclusions independently of differentiating an error term.

### D4-008 — A coupled exponential constraint

**Objects and dependencies.** $x$ is an independent dimensionless real scalar. Near $(x,y)=(0,1)$, the dependent dimensionless real scalar $y=g(x)$ satisfies

$$
x\exp(g(x))+g(x)\exp(x)=1,\qquad g(0)=1.
$$

Establish a unique smooth branch on some open interval containing zero. Determine its first two derivatives at zero and a quadratic approximation with a justified remainder as $x\to0$. Check the approximation in the original constraint; no global branch formula is required.

### D4-009 — A response selected by a bounded maximum

**Objects and dependencies.** $t\in\mathbb R$ is an independent dimensionless real scalar. The dimensionless real coordinate $x$ is restricted to $[0,1]$. Define the real scalar response

$$
M(t)=\max_{0\le x\le1}\bigl(tx-x^4\bigr).
$$

Determine the maximizing coordinate and a formula for $M(t)$ for every real $t$. Determine the first and second derivatives where they exist, and the orders of differentiability at every change in the maximizing coordinate's formula.

### D4-010 — A matrix exponential across a change of regime

**Objects and dependencies.** $t\in\mathbb R$ is an independent dimensionless real scalar. The dependent real $2\times2$ matrix and its real matrix exponential are

$$
\mathbf A(t)=\begin{bmatrix}0&1\\-t&0\end{bmatrix},\qquad
\mathbf E(t)=\exp(\mathbf A(t))
=\sum_{n=0}^{\infty}\frac{\mathbf A(t)^n}{n!}.
$$

Determine $\mathbf E(t)$ and $\frac{d}{dt}(\mathbf E(t))$ for positive, negative, and zero $t$. Establish the connection between the formulas at zero and decide whether the scalar-inspired expression $\exp(\mathbf A(t))\frac{d}{dt}(\mathbf A(t))$ gives the derivative.

### D4-011 — A scalar response on symmetric positive matrices

**Objects and dependencies.** $a,b,c$ are independent dimensionless real parameters restricted so that the real symmetric matrix

$$
\mathbf A(a,b,c)=\begin{bmatrix}a&b\\b&c\end{bmatrix}
$$

is positive definite. Define the dependent real scalar

$$
f(a,b,c)=\ln(\det(\mathbf A(a,b,c)))
+\operatorname{tr}(\mathbf A(a,b,c)^{-1}),
$$

where the trace is the sum of the diagonal entries. State its open parameter domain and compute its three partial derivatives. Compare them with the entry derivatives obtained by allowing all four entries of a general real $2\times2$ matrix to vary independently near $\mathbf A(a,b,c)$. Explain the off-diagonal contribution when symmetry is imposed.

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

### D4-007

1. The logarithm of the function is a bounded oscillatory factor times $\ln(1+x^2)$.
2. Estimate the function's difference quotient at zero before examining derivatives at nonzero inputs.
3. In the nonzero derivative, $\ln(1+x^2)/x^2$ tends to one; choose sequences on which $\cos(1/x)$ equals one and minus one.

### D4-008

1. Evaluate the partial derivative of the defining level function with respect to its second input at $(0,1)$.
2. Differentiate the full composition twice, retaining both mixed contributions on the second differentiation.
3. Substitute $1+\alpha x+\beta x^2$ into the original constraint and match the coefficients of $x$ and $x^2$.

### D4-009

1. The derivative of the objective with respect to the bounded coordinate is $t-4x^3$.
2. The critical coordinate lies inside $[0,1]$ only for a bounded range of the parameter; otherwise an endpoint maximizes.
3. The first parameter derivative of the interior value simplifies because its coordinate satisfies the critical-point equation; examine one-sided derivatives at both transitions.

### D4-010

1. Compute $\mathbf A(t)^2$ and separate the even and odd powers in the exponential series.
2. The two scalar coefficient series remain defined at zero even when their trigonometric or hyperbolic forms appear to divide by zero.
3. Differentiate both scalar coefficients and the matrix factor; compare the actual derivative at zero with the proposed product there.

### D4-011

1. Write the determinant as $\Delta=ac-b^2$ and the trace of the inverse as $(a+c)/\Delta$.
2. For a general matrix increment $\mathbf H$, differentiate the inverse identity before taking its trace.
3. A change of $b$ changes both off-diagonal entries: its parameter derivative is the sum of two entry derivatives.

## Complete solutions

### D4-001

**Step 1 — SETUP.** The real base $a(x)=\ln(1+x^2)$ is positive for $x\ne0$. The real exponent is $b(x)=\arctan x$, and the output $f(x)>0$ is differentiable on each component of the punctured real line.

**Step 2 — CHOICE.** Both the base and the exponent vary with $x$, so differentiating the power involves two contributions. Taking a logarithm turns the power into the product $b(x)\ln(a(x))$. Equivalently, $f(x)=\exp(b(x)\ln(a(x)))$; either representation keeps both contributions visible.

**Step 3 — CALCULUS.** The two inner derivatives are

$$
\frac{d}{dx}(a(x))=\frac{2x}{1+x^2},
\qquad
\frac{d}{dx}(b(x))=\frac{1}{1+x^2}.
$$

Differentiation of $\ln(f(x))=b(x)\ln(a(x))$ gives

$$
\frac{1}{f(x)}\frac{d}{dx}(f(x))
=\frac{d}{dx}(b(x))\ln(a(x))
+\frac{b(x)}{a(x)}\frac{d}{dx}(a(x)).
$$

Multiplication by $f(x)$ and substitution of the two derivatives yield

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

**Discussion.** Variable powers require both derivatives and an explicit positive-base domain. Extension of the value and extension of a finite derivative are separate questions.

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

**Discussion.** An inverse-function derivative can simplify considerably after the defining relation and branch sign are retained.

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

**Discussion.** Algebraic equivalence can improve both differentiation and numerical evaluation. The stable representation depends on the sign of the input.

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

**Discussion.** A complicated height formula may simplify on a constrained path. The graph domain and the path dependence are assessed separately.

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

**Step 6 — CHECK.** The quotient rule, followed by division by the nonzero response, gives

$$
\frac{1}{H(\omega;\tau,T)}
\frac{\partial}{\partial\omega}\left(H(\omega;\tau,T)\right)
=\mathrm{i}\left(\frac{2\tau}{1+\omega^2\tau^2}-T\right).
$$

This logarithmic derivative is purely imaginary, consistent with the constant magnitude. The negative phase derivative has units of time.

**Discussion.** A continuous phase representation separates parameter sensitivity from branch artifacts. A mathematical response formula alone does not impose additional physical constraints.

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

**Step 4 — DOMAIN.** For $t$ in a sufficiently small closed interval around any finite value, every integration interval lies inside one bounded interval of $s$. The resulting rectangle in $(s,t)$ is compact. The kernel and its parameter derivative are continuous there and hence bounded. The local differentiation theorem therefore applies for every real $t$, including values at which the endpoints coincide or reverse order.

**Step 5 — ALGEBRA.** At $t=0$ the boundary terms reduce to $1/2$ and zero. The remaining integral is

$$
\int_0^1\frac{s^2}{1+s^2}\,ds
=\int_0^1\left(1-\frac{1}{1+s^2}\right)\,ds=1-\frac\pi4.
$$

**Step 6 — RESULT AND CHECK.** The requested derivative is $\frac{d}{dt}(F(t))|_{t=0}=\pi/4-1/2$. Also $F(0)=\pi/4$. The first boundary contribution is positive at zero, while the interior contribution is negative; both are needed to obtain the stated slope. Independent finite differences of the original integral verify the value.

**Discussion.** A derivative of an integral can be tractable even when its parameter-dependent antiderivative is not. Endpoint motion and interior dependence produce distinct terms.

### D4-007

**Step 1 — SETUP.** The base $1+x^2$ is positive on the entire real line. For $x\ne0$, the exponent is real and the function is smooth on each component of the punctured line. The missing input is examined before the derivative is extended.

**Step 2 — CHOICE.** The exponent oscillates without a limit, but it multiplies a small logarithm after taking the logarithm of the function. A bound on that product controls the value and its difference quotient without requiring a limit of the exponent.

**Step 3 — ALGEBRA.** Define the real scalar $L(x)=\sin(1/x)\ln(1+x^2)$. The inequality $0\le\ln(1+x^2)\le x^2$ gives $|L(x)|\le x^2$. Since $f(x)=\exp(L(x))$ and $|\exp(u)-1|\le\exp(|u|)|u|$ for real $u$,

$$
|f(x)-1|\le\exp(x^2)x^2.
$$

Thus $f(x)\to1$ and the unique continuous extension $\widetilde f$ has $\widetilde f(0)=1$. Its difference quotient obeys

$$
\left|\frac{\widetilde f(x)-\widetilde f(0)}{x}\right|
\le\exp(x^2)|x|\longrightarrow0.
$$

**Step 4 — CALCULUS.** The extension is differentiable at zero with derivative zero. At a nonzero input, product and chain differentiation instead give

$$
\frac{d}{dx}\left(L(x)\right)
=-\frac{\cos(1/x)}{x^2}\ln(1+x^2)
+\sin(1/x)\frac{2x}{1+x^2},
$$

and therefore

$$
\frac{d}{dx}\left(f(x)\right)
=f(x)\left(
\frac{2x\sin(1/x)}{1+x^2}
-\frac{\ln(1+x^2)}{x^2}\cos(1/x)\right),\qquad x\ne0.
$$

**Step 5 — DOMAIN.** The coefficient $\ln(1+x^2)/x^2$ tends to one, while $f(x)\to1$ and the other bracketed term tends to zero. For positive integers $n$, define $x_n=1/(2\pi n)$ and $y_n=1/((2n+1)\pi)$. Both tend to zero; their sine factors vanish and their cosine factors equal one and minus one respectively. The displayed derivative consequently tends to $-1$ along $x_n$ and to $1$ along $y_n$. The derivative of the extension is not continuous at zero.

**Step 6 — CHECK.** The bound on the original difference quotient proves the zero derivative directly, whereas the two sequences use an exact derivative formula at nonzero inputs. These are different limits and are consistent: a function can be differentiable at a point without its nearby derivatives converging to that derivative. In particular, differentiating the value estimate $\widetilde f(x)=1+O(x^2)$ would not justify a derivative estimate here.

### D4-008

**Step 1 — SETUP.** Let $F(x,y)=x\exp(y)+y\exp(x)-1$ on $\mathbb R^2$. This real scalar function is smooth, $F(0,1)=0$, and

$$
\frac{\partial}{\partial y}\left(F(x,y)\right)=x\exp(y)+\exp(x),
\qquad
\left.\frac{\partial}{\partial y}\left(F(x,y)\right)\right|_{x=0,y=1}=1.
$$

The implicit function theorem therefore supplies a unique smooth branch $y=g(x)$ near $(0,1)$, with $g(0)=1$.

**Step 2 — CHOICE.** The constraint need not be solved explicitly. Its first derivative determines the slope through a nonzero coefficient of the height derivative. Differentiating the same identity again determines the curvature, with each dependence of that coefficient retained.

**Step 3 — CALCULUS.** With the other coordinate held fixed in each partial derivative,

$$
\begin{aligned}
\frac{\partial}{\partial x}\left(F(x,y)\right)&=\exp(y)+y\exp(x),\\
\frac{\partial^2}{\partial x^2}\left(F(x,y)\right)&=y\exp(x),\\
\frac{\partial}{\partial y}\left(\frac{\partial}{\partial x}\left(F(x,y)\right)\right)
&=\exp(y)+\exp(x),\\
\frac{\partial^2}{\partial y^2}\left(F(x,y)\right)&=x\exp(y).
\end{aligned}
$$

The first composition derivative is

$$
0=\exp(g(x))+g(x)\exp(x)
+\bigl(x\exp(g(x))+\exp(x)\bigr)\frac{d}{dx}\left(g(x)\right).
$$

Evaluation at zero gives

$$
0=e+1+\left.\frac{d}{dx}\left(g(x)\right)\right|_{x=0},
\qquad
\left.\frac{d}{dx}\left(g(x)\right)\right|_{x=0}=-(e+1).
$$

**Step 4 — CALCULUS AND ALGEBRA.** A second differentiation of the composition includes two equal mixed terms. Writing them together gives

$$
\begin{aligned}
0={}&g(x)\exp(x)
+2\bigl(\exp(g(x))+\exp(x)\bigr)\frac{d}{dx}\left(g(x)\right)\\
&+x\exp(g(x))\left(\frac{d}{dx}\left(g(x)\right)\right)^2
+\bigl(x\exp(g(x))+\exp(x)\bigr)\frac{d^2}{dx^2}\left(g(x)\right).
\end{aligned}
$$

At zero the coefficient of the squared slope vanishes and the coefficient of the second derivative is one. Hence

$$
\begin{aligned}
0&=1-2(e+1)^2+\left.\frac{d^2}{dx^2}\left(g(x)\right)\right|_{x=0},\\
\left.\frac{d^2}{dx^2}\left(g(x)\right)\right|_{x=0}&=2(e+1)^2-1.
\end{aligned}
$$

**Step 5 — DOMAIN AND APPROXIMATION.** The smooth local branch has a bounded third derivative on a sufficiently small closed interval containing zero. Taylor's theorem on that interval gives

$$
g(x)=1-(e+1)x+\left((e+1)^2-\frac12\right)x^2+O(x^3),\qquad x\to0.
$$

The remainder statement concerns this local branch; no claim of global uniqueness or a globally nonzero height partial is needed.

**Step 6 — CHECK.** Let $p(x)=1+\alpha x+\beta x^2$, where $\alpha=-(e+1)$ and $\beta=(e+1)^2-1/2$. Expanding the original constraint directly gives

$$
\begin{aligned}
x\exp(p(x))&=ex+e\alpha x^2+O(x^3),\\
p(x)\exp(x)&=1+(\alpha+1)x+(\beta+\alpha+1/2)x^2+O(x^3).
\end{aligned}
$$

The coefficient of $x$ in their sum is $e+\alpha+1=0$, and the coefficient of $x^2$ is $(e+1)\alpha+\beta+1/2=0$. Thus $F(x,p(x))=O(x^3)$. By shrinking the neighborhood, the height partial stays at least $1/2$ on the segment between $p(x)$ and $g(x)$. The mean value theorem then also gives $|p(x)-g(x)|\le2|F(x,p(x))|=O(|x|^3)$, independently checking the approximation and its remainder order.

### D4-009

**Step 1 — SETUP.** For each fixed real $t$, the objective $q(x;t)=tx-x^4$ is continuous on the compact interval $[0,1]$, so a maximum exists. The optimizing coordinate may move or remain at a boundary as $t$ changes.

**Step 2 — CHOICE.** The derivative in the bounded coordinate determines where the objective increases and decreases. Endpoint constraints must be imposed before the interior stationary coordinate is inserted into the value.

**Step 3 — CALCULUS.** Holding $t$ fixed,

$$
\frac{\partial}{\partial x}\left(q(x;t)\right)=t-4x^3.
$$

For $t\le0$ this is nonpositive on $[0,1]$ and the unique maximum is at zero. For $t\ge4$ it is nonnegative there and the unique maximum is at one. When $0<t<4$, the derivative changes sign from positive to negative at $r(t)=(t/4)^{1/3}$, which lies strictly inside the interval. Consequently the maximizing coordinate is

$$
x_*(t)=
\begin{cases}
0,&t\le0,\\
(t/4)^{1/3},&0<t<4,\\
1,&t\ge4.
\end{cases}
$$

**Step 4 — ALGEBRA.** In the interior regime, $t=4r(t)^3$, so $tr(t)-r(t)^4=3r(t)^4$. Including both constrained regimes gives

$$
M(t)=
\begin{cases}
0,&t\le0,\\
3(t/4)^{4/3},&0<t<4,\\
t-1,&t\ge4.
\end{cases}
$$

The neighboring values agree at zero and at four, where they are zero and three respectively.

**Step 5 — CALCULUS.** Direct differentiation on the open regimes gives

$$
\frac{d}{dt}\left(M(t)\right)=
\begin{cases}
0,&t<0,\\
(t/4)^{1/3},&0<t<4,\\
1,&t>4.
\end{cases}
$$

At zero, the right difference quotient is $3h^{1/3}/4^{4/3}$ for $h>0$ and tends to zero, matching the left slope. At four, both one-sided slopes are one. Thus the first derivative exists everywhere, with values zero and one at the respective transitions, and is continuous.

On the open regimes the second derivative is

$$
\frac{d^2}{dt^2}\left(M(t)\right)=
\begin{cases}
0,&t<0,\\
\dfrac1{12}(t/4)^{-2/3},&0<t<4,\\
0,&t>4.
\end{cases}
$$

**Step 6 — DOMAIN.** At zero the right difference quotient of the first derivative equals $h^{-2/3}/4^{1/3}$ and diverges, while the left quotient is zero. At four the one-sided derivatives of the first derivative are $1/12$ and zero. Therefore $M$ is continuously differentiable on $\mathbb R$ but has no second derivative at either transition. It is smooth within each of the three open regimes.

**Step 7 — CHECK.** Within the interior regime, differentiating the unsimplified maximizing value gives

$$
\frac{d}{dt}\left(tr(t)-r(t)^4\right)
=r(t)+\bigl(t-4r(t)^3\bigr)\frac{d}{dt}\left(r(t)\right)=r(t).
$$

The coordinate-rate term cancels by the stationary equation. In the boundary regimes the same equality $\frac{d}{dt}(M(t))=x_*(t)$ follows by direct differentiation of the boundary values. This independent representation checks the slope and its nonnegative monotone behavior, consistent with a maximum of affine functions of $t$.

### D4-010

**Step 1 — SETUP.** Matrix multiplication gives $\mathbf A(t)^2=-t\mathbf I$, where $\mathbf I$ is the real $2\times2$ identity. Thus $\mathbf A(t)^{2n}=(-t)^n\mathbf I$ and $\mathbf A(t)^{2n+1}=(-t)^n\mathbf A(t)$ for every nonnegative integer $n$.

**Step 2 — CHOICE.** Separating even and odd powers avoids choosing eigenvectors that change character at zero. The resulting two scalar series converge for every real parameter, so they also retain the limiting values needed to differentiate through the change of regime.

**Step 3 — ALGEBRA.** Define real scalar coefficient functions

$$
C(t)=\sum_{n=0}^{\infty}\frac{(-t)^n}{(2n)!},\qquad
S(t)=\sum_{n=0}^{\infty}\frac{(-t)^n}{(2n+1)!}.
$$

Then

$$
\mathbf E(t)=C(t)\mathbf I+S(t)\mathbf A(t)
=\begin{bmatrix}C(t)&S(t)\\-tS(t)&C(t)\end{bmatrix}.
$$

For $t>0$, set $r=\sqrt t$; for $t<0$, set $r=\sqrt{-t}$. The scalar series give

$$
(C(t),S(t))=
\begin{cases}
(\cos(r),\sin(r)/r),&t>0,\\
(1,1),&t=0,\\
(\cosh(r),\sinh(r)/r),&t<0.
\end{cases}
$$

In particular, $\mathbf E(0)=\begin{bmatrix}1&1\\0&1\end{bmatrix}$, also obtained by exponentiating the nilpotent matrix $\mathbf A(0)$ directly.

**Step 4 — CALCULUS.** Termwise differentiation of the everywhere convergent scalar power series gives

$$
\frac{d}{dt}\left(C(t)\right)=-\frac{S(t)}2.
$$

For the other coefficient, let $V(t)=\frac{d}{dt}(S(t))$. Differentiating its trigonometric and hyperbolic forms, and using its series at zero, gives

$$
V(t)=
\begin{cases}
\dfrac{r\cos(r)-\sin(r)}{2r^3},&t>0,\quad r=\sqrt t,\\
-1/6,&t=0,\\
\dfrac{\sinh(r)-r\cosh(r)}{2r^3},&t<0,\quad r=\sqrt{-t}.
\end{cases}
$$

For $t\ne0$ these expressions also satisfy $2tV(t)=C(t)-S(t)$. The product rule with its retained matrix order is

$$
\frac{d}{dt}\left(\mathbf E(t)\right)
=-\frac{S(t)}2\mathbf I+V(t)\mathbf A(t)
+S(t)\begin{bmatrix}0&0\\-1&0\end{bmatrix}.
$$

Thus an explicit formula valid in all three regimes, with the piecewise scalar coefficients above, is

$$
\frac{d}{dt}\left(\mathbf E(t)\right)
=\begin{bmatrix}
-S(t)/2&V(t)\\
-(C(t)+S(t))/2&-S(t)/2
\end{bmatrix}.
$$

The lower-left equality uses $-S(t)-tV(t)=-(C(t)+S(t))/2$, which holds by continuity also at zero. Therefore

$$
\left.\frac{d}{dt}\left(\mathbf E(t)\right)\right|_{t=0}
=\begin{bmatrix}-1/2&-1/6\\-1&-1/2\end{bmatrix}.
$$

**Step 5 — DOMAIN.** Both coefficient series are entire functions of the real parameter. The apparent divisions by $r$ or $t$ introduce no genuine singularity: $C(t)=1-t/2+O(t^2)$, $S(t)=1-t/6+O(t^2)$, and their differentiated series supply the stated limits. Trigonometric and hyperbolic representations describe the same smooth matrix function on different sides of zero.

**Step 6 — CHECK: matrix order.** Direct multiplication gives

$$
\mathbf A(t)\frac{d}{dt}\left(\mathbf A(t)\right)
=\begin{bmatrix}-1&0\\0&0\end{bmatrix},\qquad
\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf A(t)
=\begin{bmatrix}0&0\\0&-1\end{bmatrix}.
$$

The factors do not commute. At zero, the proposed scalar-inspired product is

$$
\mathbf E(0)\left.\frac{d}{dt}\left(\mathbf A(t)\right)\right|_{t=0}
=\begin{bmatrix}-1&0\\-1&0\end{bmatrix},
$$

which differs from the actual derivative. An independent differentiation of the matrix power series has the ordered terms

$$
\frac{d}{dt}\left(\mathbf A(t)^n\right)
=\sum_{j=0}^{n-1}\mathbf A(t)^j
\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf A(t)^{n-1-j}.
$$

At zero, $\mathbf A(0)^2=\mathbf0$ leaves only the terms of degrees one, two, and three in the exponential derivative. They are respectively the derivative of $\mathbf A$, minus $\mathbf I/2$, and $\begin{bmatrix}0&-1/6\\0&0\end{bmatrix}$, reproducing the displayed derivative at zero. The identity $C(t)^2+tS(t)^2=1$ also checks $\det(\mathbf E(t))=1$ on both sides and at the transition.

### D4-011

**Step 1 — SETUP.** Write $\Delta(a,b,c)=ac-b^2$ and $s(a,b,c)=a+c$. The symmetric matrix is positive definite precisely on the open parameter domain

$$
\mathcal U=\{(a,b,c)\in\mathbb R^3:a>0,\ ac-b^2>0\}.
$$

These inequalities imply $c>0$. On this domain the real logarithm and the inverse both exist, and small independent changes of any one parameter remain admissible.

**Step 2 — CHOICE.** The explicit inverse reduces the scalar response to two rational expressions and a logarithm. Comparing its derivatives with a matrix increment calculation then identifies exactly how the symmetry constraint combines entry derivatives.

**Step 3 — ALGEBRA.** The inverse and scalar response are

$$
\mathbf A(a,b,c)^{-1}=\frac1\Delta\begin{bmatrix}c&-b\\-b&a\end{bmatrix},
\qquad
f(a,b,c)=\ln(\Delta)+\frac{s}{\Delta}.
$$

The scalar derivatives of $\Delta$ with respect to $a,b,c$ are $c,-2b,a$, and those of $s$ are $1,0,1$ respectively.

**Step 4 — CALCULUS.** The logarithmic and quotient rules consequently give, with the other two parameters held fixed in each line,

$$
\begin{aligned}
\frac{\partial}{\partial a}\left(f(a,b,c)\right)
&=\frac c\Delta+\frac1\Delta-\frac{sc}{\Delta^2},\\
\frac{\partial}{\partial b}\left(f(a,b,c)\right)
&=-\frac{2b}\Delta+\frac{2bs}{\Delta^2},\\
\frac{\partial}{\partial c}\left(f(a,b,c)\right)
&=\frac a\Delta+\frac1\Delta-\frac{sa}{\Delta^2}.
\end{aligned}
$$

For example, $\Delta-sc=ac-b^2-(a+c)c=-b^2-c^2$ simplifies the first result; the third simplifies in the corresponding way. Thus the real column parameter gradient is

$$
\nabla_{a,b,c}f(a,b,c)=
\begin{bmatrix}
c/\Delta-(c^2+b^2)/\Delta^2\\
-2b/\Delta+2b(a+c)/\Delta^2\\
a/\Delta-(a^2+b^2)/\Delta^2
\end{bmatrix}.
$$

**Step 5 — CALCULUS: independent entry increments.** To compare with unconstrained entries, let $\mathbf B$ range over all real $2\times2$ matrices in a neighborhood of the given positive definite $\mathbf A$, with $\det(\mathbf B)>0$. The real scalar extension is $\phi(\mathbf B)=\ln(\det(\mathbf B))+\operatorname{tr}(\mathbf B^{-1})$. For a fixed real $2\times2$ increment $\mathbf H$, expansion of the determinant gives

$$
\det(\mathbf A+\epsilon\mathbf H)
=\Delta+\epsilon(cH_{11}+aH_{22}-bH_{12}-bH_{21})+O(\epsilon^2).
$$

The coefficient divided by $\Delta$ is $\operatorname{tr}(\mathbf A^{-1}\mathbf H)$. For the inverse map $\mathbf R(\mathbf B)=\mathbf B^{-1}$, differentiating the identity $\mathbf B\mathbf R(\mathbf B)=\mathbf I$ along this increment gives $\mathrm D\mathbf R(\mathbf B)(\mathbf H)=-\mathbf B^{-1}\mathbf H\mathbf B^{-1}$. Hence the scalar increment derivative at $\mathbf A$ is

$$
\mathrm D\phi(\mathbf A)(\mathbf H)
=\operatorname{tr}(\mathbf A^{-1}\mathbf H)
-\operatorname{tr}(\mathbf A^{-1}\mathbf H\mathbf A^{-1})
=\operatorname{tr}\bigl((\mathbf A^{-1}-\mathbf A^{-2})\mathbf H\bigr).
$$

The last equality uses cyclicity of the trace, retaining the order of the inverse derivative before taking that trace. The entry-gradient convention uses $\mathrm D\phi(\mathbf A)(\mathbf H)=\sum_{i,j=1}^2G_{ij}H_{ij}$. Since $\mathbf A$ and its inverse powers are symmetric here,

$$
\mathbf G=\mathbf A^{-1}-\mathbf A^{-2}
=\frac1\Delta\begin{bmatrix}c&-b\\-b&a\end{bmatrix}
-\frac1{\Delta^2}\begin{bmatrix}c^2+b^2&-b(a+c)\\-b(a+c)&a^2+b^2\end{bmatrix}.
$$

**Step 6 — DOMAIN AND ALGEBRA.** Independent entry variations of $\mathbf B$ need not remain symmetric; they are used only in the open set with positive determinant near $\mathbf A$. The actual parameter variations preserve symmetry and have increment

$$
\mathbf H=\begin{bmatrix}\delta a&\delta b\\\delta b&\delta c\end{bmatrix}.
$$

Substitution into the increment derivative yields

$$
\mathrm D\phi(\mathbf A)(\mathbf H)
=G_{11}\delta a+(G_{12}+G_{21})\delta b+G_{22}\delta c.
$$

Therefore the parameter gradient is $(G_{11},2G_{12},G_{22})^{\mathsf T}$. One unconstrained off-diagonal entry derivative alone would miss half the contribution of changing $b$. Symmetry constrains the allowed increments, rather than changing the inverse derivative rule.

**Step 7 — CHECK.** At $b=0$ the original response separates as $\ln(a)+\ln(c)+1/a+1/c$, whose partial derivatives are $1/a-1/a^2$, zero, and $1/c-1/c^2$. These agree with the formulas. Interchanging $a$ and $c$ interchanges the first and third derivatives and preserves the second. At $\mathbf A=\mathbf I$ all three derivatives vanish. Finally, direct scalar differentiation of $\ln(ac-b^2)+(a+c)/(ac-b^2)$ and the independent matrix increment calculation give the same off-diagonal coefficient even for nonzero $b$.
