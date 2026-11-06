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

### D4-012 — A folded angle and its continuous lift

**Objects and dependencies.** $x\in\mathbb R\setminus\{-1,1\}$ is an independent dimensionless real scalar. The dependent real angle is

$$
f(x)=\arctan\left(\frac{2x}{1-x^2}\right),
$$

where the principal real arctangent takes values in $(-\pi/2,\pi/2)$. Determine the derivative and the exact relation between $f(x)$ and $2\arctan x$ on every connected component of its domain. Determine all one-sided limits at the excluded inputs. Construct a continuous real angle $\Theta(x)$ on the entire real line, with $\Theta(0)=0$, that differs from $f(x)$ by an integer multiple of $\pi$ wherever $f$ is defined, and find its derivative. Distinguish this lift from a continuous extension of $f$ itself.

### D4-013 — A phase zero in a complex response

**Objects and dependencies.** $\omega\in\mathbb R$ is an independent real angular frequency, and $\tau>0$ is a fixed real time. The dependent dimensionless complex scalar response is

$$
H(\omega;\tau)=1-\exp(-\mathrm i\omega\tau),\qquad \mathrm i^2=-1.
$$

Determine every real-frequency zero and the magnitude away from and near each zero. On every connected interval between zeros, find a continuous real phase $\phi(\omega;\tau)$ satisfying $H=|H|\exp(\mathrm i\phi)$ and its frequency derivative. Decide whether any choice of phase can be continuously extended through a zero while representing the response on both sides. Check the derivative using the complex logarithmic derivative with $\tau$ held fixed.

### D4-014 — Constant determinant along a changing matrix response

**Objects and dependencies.** $t\in\mathbb R$ is an independent dimensionless real scalar. Define the dependent real $2\times2$ matrix, real scalar, and inverse matrix

$$
\mathbf A(t)=\begin{bmatrix}1+t^2&t\\t&1\end{bmatrix},\qquad
h(t)=\ln(\det(\mathbf A(t))),\qquad
\mathbf R(t)=\mathbf A(t)^{-1}.
$$

Establish their domains and determine $\frac{d}{dt}(h(t))$ both directly and by a trace identity, explicitly accounting for the shared off-diagonal parameter. Derive ordered matrix formulas for the first two derivatives of $\mathbf R(t)$ and evaluate their entries. Determine the two eigenvalues of $\mathbf A(t)$ and its Euclidean operator-norm condition number $\kappa_2(\mathbf A(t))=\|\mathbf A(t)\|_2\|\mathbf A(t)^{-1}\|_2$, including their leading behavior as $|t|\to\infty$. Explain how a constant determinant coexists with the changing response $\mathbf j(t)=\mathbf R(t)\mathbf b$ for fixed real column $\mathbf b=[0,1]^{\mathsf T}$.

### D4-015 — A cubic constraint at the edge of a branch

**Objects and dependencies.** $x$ is an independent dimensionless real scalar. A dependent dimensionless real scalar $y=g(x)$ is required to satisfy

$$
g(x)^3-3g(x)=x,\qquad g(x)>1.
$$

Determine the complete real-input domain on which this requirement defines exactly one value, and its first two derivatives in terms of $g(x)$. Determine the continuous extension at the finite endpoint of that domain. Obtain an expansion there through the term linear in the endpoint distance, with a justified remainder, and determine the corresponding derivative blowup. Any assertion about a branch beyond a local neighborhood must be justified.

### D4-016 — A smooth approximation to an absolute value

**Objects and dependencies.** $x\in\mathbb R$ is an independent dimensionless real scalar. The real parameter $\epsilon>0$ is held fixed in $x$ derivatives. Define the dependent real scalar

$$
f_\epsilon(x)=\epsilon\ln\bigl(2\cosh(x/\epsilon)\bigr).
$$

Determine its first two $x$ derivatives and a uniform error bound for approximating $|x|$ on the entire real line. Analyze the limit of its first derivative both near and away from zero. For the second derivative, compute the total integral over $\mathbb R$, the integral over $[-c\epsilon,c\epsilon]$ for fixed real $c>0$, and an explicit tail bound outside a fixed interval $[-\delta,\delta]$, $\delta>0$. Use those results to justify its integral limit against any bounded continuous real function $\psi(x)$ as $\epsilon\downarrow0$.

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

### D4-012

1. The double-angle identity determines the tangent of $2\arctan x$, but the principal arctangent selects only one interval of angles.
2. Locate $2\arctan x$ relative to $-\pi/2$ and $\pi/2$ on each of the three input intervals.
3. Derivative formulas ignore added constant multiples of $\pi$; one-sided function limits determine which multiples a continuous lift requires.

### D4-013

1. Factor the response around half its frequency-dependent angle.
2. Between consecutive zeros, the sign of $\sin(\omega\tau/2)$ is constant and supplies a constant phase contribution.
3. At a zero the leading response is $\mathrm i\tau$ times the signed frequency displacement; compare its normalized one-sided limits.

### D4-014

1. The matrix is a product of a real shear and its transpose. Its determinant and inverse can also be computed directly.
2. Differentiate $\mathbf A(t)\mathbf R(t)=\mathbf I$ twice, retaining multiplication order. Both off-diagonal entries vary in the trace calculation.
3. The positive eigenvalues have product one and sum $t^2+2$; find the smaller one by taking the reciprocal of the larger one.

### D4-015

1. Examine the range and monotonicity of $y^3-3y$ on the required interval $y>1$ before using implicit differentiation.
2. At the finite endpoint write $y=1+u$; the input displacement becomes $u^2(3+u)$.
3. The map $u\mapsto u\sqrt{3+u}$ has a nonzero derivative at zero. Its smooth local inverse supplies an expansion in the square root of the input displacement.

### D4-016

1. Rewrite $2\cosh(x/\epsilon)$ using the exponential of $|x|/\epsilon$ before comparing values.
2. The first derivative is a hyperbolic tangent. The second derivative has a simple primitive, even when its peak becomes unbounded.
3. Split a test-function integral into $|x|\le\delta$ and its complement. Continuity controls the first part and the explicit tail controls the second.

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

### D4-012

**Step 1 — SETUP.** The rational input to the principal arctangent is real on the three intervals $(-\infty,-1)$, $(-1,1)$, and $(1,\infty)$. The function is smooth separately on these intervals. Its angle range is fixed before differentiating or reconstructing it from a trigonometric identity.

**Step 2 — CHOICE.** Let $\theta(x)=2\arctan x$, which ranges over $(-\pi,\pi)$. The double-angle identity gives $\tan(\theta(x))=2x/(1-x^2)$ at admissible inputs. Equality of tangents determines an angle only up to an integer multiple of $\pi$; the principal range determines which multiple occurs.

**Step 3 — ALGEBRA.** When $x<-1$, the angle $\theta(x)$ lies in $(-\pi,-\pi/2)$, so adding $\pi$ selects the principal range. When $-1<x<1$, no adjustment is needed. When $x>1$, subtracting $\pi$ selects that range. Therefore

$$
f(x)=
\begin{cases}
2\arctan x+\pi,&x<-1,\\
2\arctan x,&-1<x<1,\\
2\arctan x-\pi,&x>1.
\end{cases}
$$

**Step 4 — CALCULUS.** Direct differentiation also checks that the same derivative holds on all three components. For $u(x)=2x/(1-x^2)$,

$$
\frac{d}{dx}\left(u(x)\right)
=\frac{2(1-x^2)+4x^2}{(1-x^2)^2}
=\frac{2(1+x^2)}{(1-x^2)^2},
$$

while

$$
1+u(x)^2
=\frac{(1-x^2)^2+4x^2}{(1-x^2)^2}
=\frac{(1+x^2)^2}{(1-x^2)^2}.
$$

The arctangent chain rule consequently gives

$$
\frac{d}{dx}\left(f(x)\right)=\frac{2}{1+x^2},\qquad x\ne-1,1.
$$

**Step 5 — DOMAIN: the two jumps.** The exact piecewise relation supplies all four endpoint limits:

$$
\begin{aligned}
\lim_{x\to-1^-}f(x)&=\pi/2,&
\lim_{x\to-1^+}f(x)&=-\pi/2,\\
\lim_{x\to1^-}f(x)&=\pi/2,&
\lim_{x\to1^+}f(x)&=-\pi/2.
\end{aligned}
$$

Each right-minus-left jump is $-\pi$. No assigned value at either excluded input can make the original function continuous there, even though its derivative formula has the same finite one-sided limit of one.

**Step 6 — ALGEBRA AND CHECK: a continuous lift.** Define

$$
\Theta(x)=
\begin{cases}
f(x)-\pi,&x<-1,\\
-\pi/2,&x=-1,\\
f(x),&-1<x<1,\\
\pi/2,&x=1,\\
f(x)+\pi,&x>1.
\end{cases}
$$

Then $\Theta(x)=2\arctan x$ for every real input. It is smooth, has $\Theta(0)=0$, and satisfies

$$
\frac{d}{dx}\left(\Theta(x)\right)=\frac{2}{1+x^2},\qquad x\in\mathbb R.
$$

On each connected interval, a continuous difference between two angles with the same tangent must be a fixed integer multiple of $\pi$. Continuity at the missing inputs and the normalization at zero select exactly the displayed multiples. The lift changes values on the outer intervals; it is not a continuous extension of the original principal-valued function. Its explicit expression and the separate quotient differentiation independently check the derivative.

### D4-013

**Step 1 — SETUP.** The response is a smooth complex function of every real frequency. Its zeros occur when $\exp(-\mathrm i\omega\tau)=1$, namely

$$
\omega_n=\frac{2\pi n}{\tau},\qquad n\in\mathbb Z.
$$

The nonzero-frequency components for phase calculations are the intervals $I_n=(\omega_n,\omega_{n+1})$.

**Step 2 — CHOICE.** Factoring around half the angle separates a smooth exponential from a real sine. On each interval between zeros, the sign of that sine is fixed and can be included as a constant phase rather than discarded when taking a magnitude.

**Step 3 — ALGEBRA.** With the dependent real angle $\theta(\omega;\tau)=\omega\tau/2$,

$$
\begin{aligned}
H(\omega;\tau)
&=\exp(-\mathrm i\theta)\bigl(\exp(\mathrm i\theta)-\exp(-\mathrm i\theta)\bigr)\\
&=2\mathrm i\exp(-\mathrm i\theta)\sin\theta,\\
|H(\omega;\tau)|&=2|\sin\theta|.
\end{aligned}
$$

For $\omega\in I_n$, the sine has sign $(-1)^n$. One continuous real phase there is consequently

$$
\phi_n(\omega;\tau)=\frac\pi2-\frac{\omega\tau}{2}+n\pi,
\qquad
H(\omega;\tau)=|H(\omega;\tau)|\exp(\mathrm i\phi_n(\omega;\tau)).
$$

This choice lies in $(-\pi/2,\pi/2)$ on each interval. Every other continuous real phase on that same interval differs by a fixed multiple of $2\pi$.

**Step 4 — CALCULUS.** Holding $\tau$ fixed gives

$$
\frac{\partial}{\partial\omega}\left(\phi_n(\omega;\tau)\right)=-\frac\tau2,
\qquad \omega\in I_n.
$$

This derivative is asserted only where the response is nonzero. The derivative of the smooth complex response itself is

$$
\frac{\partial}{\partial\omega}\left(H(\omega;\tau)\right)
=\mathrm i\tau\exp(-\mathrm i\omega\tau),
$$

which equals $\mathrm i\tau$ at every zero.

**Step 5 — DOMAIN: approaching a zero.** Write $\omega=\omega_n+\delta$, with real displacement $\delta\to0$ and fixed $\tau$. Taylor expansion gives

$$
H(\omega_n+\delta;\tau)
=\mathrm i\tau\delta+\frac{\tau^2\delta^2}{2}+O(\delta^3),
\qquad
|H(\omega_n+\delta;\tau)|=\tau|\delta|+O(|\delta|^3).
$$

Thus the magnitude vanishes linearly and has opposite one-sided slopes. The normalized response has opposite one-sided limits:

$$
\lim_{\delta\downarrow0}\frac{H(\omega_n+\delta;\tau)}{|H(\omega_n+\delta;\tau)|}=\mathrm i,
\qquad
\lim_{\delta\uparrow0}\frac{H(\omega_n+\delta;\tau)}{|H(\omega_n+\delta;\tau)|}=-\mathrm i.
$$

For the displayed phase choices the left limit is $-\pi/2$ and the right limit is $\pi/2$. Adding interval-dependent multiples of $2\pi$ cannot identify the two opposite unit-complex limits. No continuous real phase representing both sides can therefore be extended through the zero. This obstruction comes from a response zero, while the response itself remains smooth.

**Step 6 — CHECK: the complex logarithmic derivative.** At a nonzero response, the preceding factorization gives

$$
\begin{aligned}
\frac{\frac{\partial}{\partial\omega}\left(H(\omega;\tau)\right)}{H(\omega;\tau)}
&=\frac{\mathrm i\tau\exp(-2\mathrm i\theta)}{2\mathrm i\exp(-\mathrm i\theta)\sin\theta}\\
&=\frac\tau2\bigl(\cot\theta-\mathrm i\bigr).
\end{aligned}
$$

Its imaginary part is the phase derivative $-\tau/2$. Its real part is the derivative of $\ln|H|$, which diverges like $1/\delta$ at a zero. The finite phase slope on each open interval consequently does not imply that a phase value exists at the excluded frequencies.

### D4-014

**Step 1 — SETUP.** Define the real shear matrix $\mathbf S(t)=\begin{bmatrix}1&t\\0&1\end{bmatrix}$. Then $\mathbf A(t)=\mathbf S(t)\mathbf S(t)^{\mathsf T}$. The shear is invertible for every real $t$, so $\mathbf v^{\mathsf T}\mathbf A(t)\mathbf v=\|\mathbf S(t)^{\mathsf T}\mathbf v\|^2>0$ for every nonzero real column $\mathbf v$. Thus $\mathbf A(t)$ is positive definite and all requested functions are defined on the entire real line.

**Step 2 — CHOICE.** The determinant is simple enough to compute directly, but a trace calculation reveals how both constrained off-diagonal variations enter its derivative. The inverse identity supplies ordered derivatives without replacing matrix products by scalar quotients. Spectral quantities then measure behavior that the determinant alone does not describe.

**Step 3 — ALGEBRA AND CALCULUS: the determinant.** Direct calculation gives

$$
\det(\mathbf A(t))=(1+t^2)-t^2=1,
\qquad h(t)=0,\qquad \frac{d}{dt}\left(h(t)\right)=0.
$$

The explicit inverse and matrix derivatives are

$$
\begin{aligned}
\mathbf R(t)&=\begin{bmatrix}1&-t\\-t&1+t^2\end{bmatrix},\\
\frac{d}{dt}\left(\mathbf A(t)\right)&=\begin{bmatrix}2t&1\\1&0\end{bmatrix},&
\frac{d^2}{dt^2}\left(\mathbf A(t)\right)&=\begin{bmatrix}2&0\\0&0\end{bmatrix}.
\end{aligned}
$$

For an invertible matrix, differentiation of the logarithmic determinant gives the trace of the inverse times its derivative. Here its product is

$$
\mathbf R(t)\frac{d}{dt}\left(\mathbf A(t)\right)
=\begin{bmatrix}t&1\\1-t^2&-t\end{bmatrix},
\qquad
\frac{d}{dt}\left(h(t)\right)
=\operatorname{tr}\left(\mathbf R(t)\frac{d}{dt}\left(\mathbf A(t)\right)\right)=t-t=0.
$$

In entry form the same contraction is $1\cdot2t+(-t)\cdot1+(-t)\cdot1+(1+t^2)\cdot0=0$. Changing $t$ changes both off-diagonal entries. Retaining only one of their contributions would give the incorrect value $t$.

**Step 4 — CALCULUS: ordered inverse derivatives.** Differentiating $\mathbf A(t)\mathbf R(t)=\mathbf I$ and multiplying on the left by the inverse gives

$$
\frac{d}{dt}\left(\mathbf R(t)\right)
=-\mathbf R(t)\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf R(t).
$$

A further product differentiation gives three terms before the first derivative is substituted:

$$
\begin{aligned}
\frac{d^2}{dt^2}\left(\mathbf R(t)\right)
={}&-\frac{d}{dt}\left(\mathbf R(t)\right)\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf R(t)\\
&-\mathbf R(t)\frac{d^2}{dt^2}\left(\mathbf A(t)\right)\mathbf R(t)
-\mathbf R(t)\frac{d}{dt}\left(\mathbf A(t)\right)\frac{d}{dt}\left(\mathbf R(t)\right)\\
={}&2\mathbf R(t)\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf R(t)
\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf R(t)
-\mathbf R(t)\frac{d^2}{dt^2}\left(\mathbf A(t)\right)\mathbf R(t).
\end{aligned}
$$

The two positive terms have exactly the same retained order; no commutation has been assumed.

**Step 5 — ALGEBRA: evaluating the derivatives.** The products needed for the first derivative are

$$
\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf R(t)
=\begin{bmatrix}t&1-t^2\\1&-t\end{bmatrix},
\qquad
\mathbf R(t)\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf R(t)
=\begin{bmatrix}0&1\\1&-2t\end{bmatrix}.
$$

The ordered products in the second derivative reduce to

$$
\begin{aligned}
\mathbf R(t)\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf R(t)
\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf R(t)
&=\mathbf R(t),\\
\mathbf R(t)\frac{d^2}{dt^2}\left(\mathbf A(t)\right)\mathbf R(t)
&=2\begin{bmatrix}1&-t\\-t&t^2\end{bmatrix}.
\end{aligned}
$$

Consequently,

$$
\frac{d}{dt}\left(\mathbf R(t)\right)=\begin{bmatrix}0&-1\\-1&2t\end{bmatrix},
\qquad
\frac{d^2}{dt^2}\left(\mathbf R(t)\right)=\begin{bmatrix}0&0\\0&2\end{bmatrix}.
$$

**Step 6 — DOMAIN AND SPECTRAL BEHAVIOR.** The positive eigenvalues have sum $T(t)=t^2+2$ and product one, so

$$
\lambda_\pm(t)=\frac{t^2+2\pm|t|\sqrt{t^2+4}}2,
\qquad
\lambda_-(t)=\frac1{\lambda_+(t)}.
$$

The reciprocal formula for the smaller eigenvalue also avoids subtracting nearly equal large quantities. Both eigenvalues equal one at zero; the repeated eigenvalue introduces no singularity in the polynomial matrix or inverse entries. Positive definiteness gives $\|\mathbf A(t)\|_2=\lambda_+(t)$ and $\|\mathbf R(t)\|_2=1/\lambda_-(t)$. Hence

$$
\kappa_2(\mathbf A(t))=\lambda_+(t)^2.
$$

As $|t|\to\infty$, division of the formula for $\lambda_+$ by $t^2$ shows that its ratio to $t^2$ tends to one. Therefore

$$
\lambda_+(t)\sim t^2,\qquad
\lambda_-(t)\sim t^{-2},\qquad
\kappa_2(\mathbf A(t))\sim t^4.
$$

The determinant is their product, not a bound on either eigenvalue or their ratio.

**Step 7 — CHECK: a changing response.** For the stated fixed vector,

$$
\mathbf j(t)=\begin{bmatrix}-t\\1+t^2\end{bmatrix},\qquad
\frac{d}{dt}\left(\mathbf j(t)\right)=\begin{bmatrix}-1\\2t\end{bmatrix},\qquad
\frac{d^2}{dt^2}\left(\mathbf j(t)\right)=\begin{bmatrix}0\\2\end{bmatrix}.
$$

Substitution gives $\mathbf A(t)\mathbf j(t)=\mathbf b$, and the response norm grows like $t^2$. Independently differentiating the polynomial entries of the explicit inverse reproduces both ordered inverse derivatives. The matrix and response can consequently become large and ill conditioned while the determinant remains exactly one.

### D4-015

**Step 1 — SETUP.** For a real scalar $y>1$, define $q(y)=y^3-3y$. Its derivative is $3(y^2-1)>0$, and its endpoint limits are $\lim_{y\downarrow1}q(y)=-2$ and $\lim_{y\to\infty}q(y)=\infty$. Continuity and strict monotonicity show that it maps $(1,\infty)$ bijectively onto $(-2,\infty)$. This proves the complete branch domain, rather than extending a local implicit solution without justification.

**Step 2 — CHOICE.** On this branch the height derivative of the cubic constraint is nonzero, so implicit differentiation gives derivatives without an explicit cubic-root formula. At the finite boundary that derivative vanishes. A square-root input coordinate then resolves the branch's fold and permits a controlled endpoint expansion.

**Step 3 — CALCULUS.** The inverse branch $g(x)>1$ is smooth on $x>-2$ by the inverse function theorem. Differentiating its defining identity once and twice gives

$$
\begin{aligned}
3(g(x)^2-1)\frac{d}{dx}\left(g(x)\right)&=1,\\
6g(x)\left(\frac{d}{dx}\left(g(x)\right)\right)^2
+3(g(x)^2-1)\frac{d^2}{dx^2}\left(g(x)\right)&=0.
\end{aligned}
$$

Solving these equations in their stated order yields

$$
\frac{d}{dx}\left(g(x)\right)=\frac1{3(g(x)^2-1)},
\qquad
\frac{d^2}{dx^2}\left(g(x)\right)=-\frac{2g(x)}{9(g(x)^2-1)^3},\qquad x>-2.
$$

Thus the branch is increasing and strictly concave.

**Step 4 — ALGEBRA: the endpoint relation.** As $x\downarrow-2$, monotonic inversion gives $g(x)\downarrow1$. The unique continuous endpoint value is $g(-2)=1$, with the strict inequality replaced by equality at that single extended input. For real $\delta=x+2>0$ and $u=g(x)-1>0$, the constraint becomes exactly

$$
\delta=3u^2+u^3=u^2(3+u).
$$

In particular, $u/\sqrt\delta=1/\sqrt{3+u}\to1/\sqrt3$. Inputs $x<-2$ admit no value $g(x)>1$, since the range proved in Step 1 excludes them.

**Step 5 — CALCULUS AND APPROXIMATION.** Set the real local coordinate $s=\sqrt\delta>0$. The relation is $s=W(u)$, where $W(u)=u\sqrt{3+u}$ is smooth for $u$ near zero. Its first two derivatives at zero are

$$
\left.\frac{d}{du}\left(W(u)\right)\right|_{u=0}=\sqrt3,
\qquad
\left.\frac{d^2}{du^2}\left(W(u)\right)\right|_{u=0}=\frac1{\sqrt3}.
$$

The inverse function theorem supplies a smooth local inverse $u=V(s)$ with $V(0)=0$. Differentiating $W(V(s))=s$ gives

$$
\left.\frac{d}{ds}\left(V(s)\right)\right|_{s=0}=\frac1{\sqrt3},
\qquad
\left.\frac{d^2}{ds^2}\left(V(s)\right)\right|_{s=0}
=-\frac{(1/\sqrt3)(1/\sqrt3)^2}{\sqrt3}=-\frac19.
$$

Its third derivative is bounded on a sufficiently small closed interval. Taylor's theorem consequently yields

$$
g(-2+\delta)=1+\frac{\sqrt\delta}{\sqrt3}-\frac{\delta}{18}
+O(\delta^{3/2}),\qquad \delta\downarrow0.
$$

This remainder is justified in the smooth coordinate $s$, even though the original branch has an unbounded $x$ derivative at the endpoint.

**Step 6 — DOMAIN: derivative blowup.** The exact derivative formulas, rather than differentiation of the value remainder, give

$$
\frac{d}{dx}\left(g(-2+\delta)\right)=\frac1{3u(2+u)},
\qquad
\frac{d^2}{dx^2}\left(g(-2+\delta)\right)
=-\frac{2(1+u)}{9u^3(2+u)^3}.
$$

Using $u/\sqrt\delta\to1/\sqrt3$ gives the precise one-sided limits

$$
\lim_{\delta\downarrow0}\sqrt\delta\,\frac{d}{dx}\left(g(x)\right)\bigg|_{x=-2+\delta}
=\frac1{2\sqrt3},
\qquad
\lim_{\delta\downarrow0}\delta^{3/2}\,\frac{d^2}{dx^2}\left(g(x)\right)\bigg|_{x=-2+\delta}
=-\frac1{4\sqrt3}.
$$

The continuous extension has no finite right derivative: its own difference quotient is $u/\delta=1/(u(3+u))\to\infty$. The leading coefficient in this difference quotient differs from that of the interior derivative, as expected for square-root behavior.

**Step 7 — CHECK.** At $x=0$ the selected value is $g(0)=\sqrt3$, giving first derivative $1/6$ and second derivative $-\sqrt3/36$. For a separate endpoint check, put $u_0=\sqrt\delta/\sqrt3-\delta/18$ into $3u_0^2+u_0^3$. The terms of order $\delta^{3/2}$ cancel, leaving $\delta+O(\delta^2)$, consistent with the expansion in the regular square-root coordinate. Finally, strict monotonicity from Step 1 establishes that the selected branch cannot switch to another cubic root within its domain.

### D4-016

**Step 1 — SETUP.** For each fixed positive $\epsilon$, the quantity $2\cosh(x/\epsilon)$ is strictly positive at every real $x$. The function and all its $x$ derivatives are therefore smooth on $\mathbb R$. The joint formulas are smooth for $(x,\epsilon)\in\mathbb R\times(0,\infty)$; estimates that require a positive lower bound on $\epsilon$ need not persist when $\epsilon\downarrow0$.

**Step 2 — CHOICE.** Factoring out the larger exponential separates the target absolute value from an explicit nonnegative error. For the derivative limits, closed forms and exact integral tails are more useful than differentiating a uniform bound on the values.

**Step 3 — ALGEBRA: a uniform value bound.** The identity

$$
2\cosh(x/\epsilon)
=\exp(|x|/\epsilon)\bigl(1+\exp(-2|x|/\epsilon)\bigr)
$$

gives

$$
f_\epsilon(x)=|x|+\epsilon\ln\bigl(1+\exp(-2|x|/\epsilon)\bigr).
$$

Since the exponential inside the logarithm lies between zero and one,

$$
0\le f_\epsilon(x)-|x|\le\epsilon\ln2,\qquad
\sup_{x\in\mathbb R}\bigl|f_\epsilon(x)-|x|\bigr|=\epsilon\ln2.
$$

Equality in the upper bound occurs at zero. Thus the approximation is uniform on the entire real line.

**Step 4 — CALCULUS.** With $\epsilon$ held fixed, the logarithmic chain rule gives

$$
\frac{d}{dx}\left(f_\epsilon(x)\right)
=\epsilon\frac{(2/\epsilon)\sinh(x/\epsilon)}{2\cosh(x/\epsilon)}
=\tanh(x/\epsilon).
$$

Differentiating once more and using $\cosh^2v-\sinh^2v=1$ gives

$$
\frac{d^2}{dx^2}\left(f_\epsilon(x)\right)
=\frac1\epsilon\frac{\cosh^2(x/\epsilon)-\sinh^2(x/\epsilon)}{\cosh^2(x/\epsilon)}
=\frac1{\epsilon\cosh^2(x/\epsilon)}.
$$

The function is strictly convex for every positive $\epsilon$.

**Step 5 — DOMAIN: the first derivative limit.** For nonzero $x$, the first derivative tends to $\operatorname{sgn}(x)$ as $\epsilon\downarrow0$; at zero it equals zero for every positive $\epsilon$. Define $\operatorname{sgn}(0)=0$ for this pointwise limit only. For any fixed $\delta>0$,

$$
\left|\tanh(x/\epsilon)-\operatorname{sgn}(x)\right|
=\frac2{\exp(2|x|/\epsilon)+1}
\le2\exp(-2\delta/\epsilon),\qquad |x|\ge\delta.
$$

The convergence is uniform away from zero. It is not uniform on any fixed neighborhood of zero: for each positive $\epsilon$, taking nonzero $x\to0$ makes the difference tend to one. The pointwise derivative limit is discontinuous there, and $|x|$ itself has no derivative at zero. Uniform convergence of the original function values does not supply convergence of their derivatives at that input.

**Step 6 — CALCULUS: the second derivative's mass.** Write the nonnegative real function $\rho_\epsilon(x)=1/(\epsilon\cosh^2(x/\epsilon))$. Its primitive is $\tanh(x/\epsilon)$, so

$$
\int_{-\infty}^{\infty}\rho_\epsilon(x)\,dx=2,
\qquad
\int_{-c\epsilon}^{c\epsilon}\rho_\epsilon(x)\,dx=2\tanh c,\qquad c>0.
$$

The omitted mass outside a fixed interval has the exact value and bound

$$
\int_{|x|>\delta}\rho_\epsilon(x)\,dx
=2\bigl(1-\tanh(\delta/\epsilon)\bigr)
=\frac4{\exp(2\delta/\epsilon)+1}
\le4\exp(-2\delta/\epsilon).
$$

For each nonzero fixed $x$, $\rho_\epsilon(x)\to0$, while $\rho_\epsilon(0)=1/\epsilon$ diverges. The total integral remains two, concentrated near zero. There cannot be a single integrable majorant for this family near $\epsilon=0$: such a bound and the almost-everywhere zero limit would force the total integrals to tend to zero.

**Step 7 — DOMAIN AND CHECK: an integral limit.** Let $\psi$ be any bounded continuous real function on $\mathbb R$, with $M=\sup_x|\psi(x)|<\infty$. Each integral of $\rho_\epsilon\psi$ is absolutely convergent. For a fixed $\delta>0$, define the local oscillation $\eta(\delta)=\sup_{|x|\le\delta}|\psi(x)-\psi(0)|$, which tends to zero as $\delta\downarrow0$. Splitting into the fixed inner interval and its complement gives

$$
\begin{aligned}
\left|\int_{\mathbb R}\rho_\epsilon(x)\psi(x)\,dx-2\psi(0)\right|
&\le2\eta(\delta)+2M\int_{|x|>\delta}\rho_\epsilon(x)\,dx\\
&\le2\eta(\delta)+8M\exp(-2\delta/\epsilon).
\end{aligned}
$$

First let $\epsilon\downarrow0$ with $\delta$ fixed, then let $\delta\downarrow0$. This proves

$$
\lim_{\epsilon\downarrow0}\int_{\mathbb R}
\frac{\psi(x)}{\epsilon\cosh^2(x/\epsilon)}\,dx=2\psi(0).
$$

For the independent constant test $\psi(x)=1$, this is exactly the total mass calculation. An odd bounded continuous test has zero integral by symmetry for every $\epsilon$, consistent with its value at zero. The limit records the change of two between the left and right slopes of the absolute value, while its pointwise second derivative away from zero remains zero.
