# I1 · Scalar antiderivatives and definite integrals

An indefinite integral asks for a family of antiderivatives. A definite integral
asks for a scalar number when its endpoints and all parameters are fixed. Begin
by identifying which task is requested, then keep the integration variable visible.

## Rules to consult

For independent real scalar $x$ on an interval where the expressions are defined,
and fixed real scalar exponent $p\ne-1$,

$$
\int x^p\,dx=\frac{x^{p+1}}{p+1}+C.
$$

The real scalar constant $C$ is independent of $x$. In each example the derivative
of the proposed antiderivative is checked. On a connected interval excluding zero,

$$
\int\frac1x\,dx=\ln(|x|)+C.
$$

For a continuous real scalar function $q(x)$ on a closed interval with fixed
real endpoints $a,b$, and an antiderivative $F(x)$,

$$
\int_a^b q(x)\,dx=F(b)-F(a),\qquad
\frac{d}{dx}\left(F(x)\right)=q(x).
$$

When the upper limit is smaller than the lower limit, reverse the sign.
The definite integral is signed accumulation; it does not automatically equal area.

## Problems

### I1-001 — Integrate a polynomial term by term

**Objects and dependencies.** $x$ is a real scalar integration variable and
$q(x)=6x^2-4x+5$ is a real scalar function. Find the real scalar antiderivative
family $\int q(x)\,dx$ on all real inputs. State which quantity is constant.

### I1-002 — The reciprocal rule and two separate intervals

**Objects and dependencies.** $x$ is a real scalar integration variable with
$x\ne0$. The real scalar function is $q(x)=3/x$. Find $\int q(x)\,dx$ on each
of the intervals $x>0$ and $x<0$. Explain whether the arbitrary constants must match.

### I1-003 — Evaluate at both endpoints

**Objects and dependencies.** $x$ is a real scalar integration variable.
$q(x)=2x+3$ is real scalar-valued. Find the real scalar number
$\int_{-1}^{2}q(x)\,dx$, with lower limit $x=-1$ and upper limit $x=2$.

### I1-004 — Reverse an exponential chain rule

**Objects and dependencies.** $x$ is a real scalar integration variable and
$q(x)=\exp(3x)$ is a real scalar function on all real inputs. Find
$\int q(x)\,dx$ and verify the coefficient of the antiderivative.

### I1-005 — Integrate a trigonometric sum

**Objects and dependencies.** $x$ is a real scalar angle in radians and is the
integration variable. The real scalar function is $q(x)=2\cos(x)-3\sin(x)$.
Find $\int q(x)\,dx$ on all real inputs.

### I1-006 — Signed accumulation versus area

**Objects and dependencies.** $x$ is a real scalar integration variable on
$[-1,1]$. The real scalar function is $q(x)=x$. Find both real scalar numbers
$\int_{-1}^{1}q(x)\,dx$ and $\int_{-1}^{1}|q(x)|\,dx$.

## Hint ladders

### I1-001

1. Integrate the three terms separately.
2. Raise each power by one and divide by that new exponent.
3. Keep one arbitrary constant for the combined family; differentiate to check.

### I1-002

1. The exponent minus one is excluded from the ordinary power rule.
2. On positive inputs use $\ln(x)$; on negative inputs use $\ln(-x)$.
3. The derivative of $\ln(|x|)$ is $1/x$ on either interval, but neither interval crosses zero.

### I1-003

1. Find one antiderivative of $2x+3$.
2. Evaluate at $x=2$ and $x=-1$ separately.
3. Subtract the lower-endpoint value, including its sign.

### I1-004

1. Differentiating $\exp(3x)$ produces an extra factor three.
2. Try a fixed multiple of $\exp(3x)$.
3. Choose the multiple that makes the derivative's coefficient exactly one.

### I1-005

1. The derivative of $\sin(x)$ is $\cos(x)$.
2. The derivative of $\cos(x)$ is $-\sin(x)$.
3. Check both coefficients and the minus sign by differentiation.

### I1-006

1. The positive and negative parts can cancel in a signed integral.
2. For the absolute value, use $|x|=-x$ on $[-1,0]$ and $|x|=x$ on $[0,1]$.
3. Evaluate the two nonnegative contributions separately and add them.

## Complete solutions

### I1-001

**Step 1 — SETUP.** $x$ is the real scalar integration variable;
$q(x)=6x^2-4x+5$ has real scalar output. The antiderivative is scalar-valued
and has a fixed real scalar constant $C$ independent of $x$.

**Step 2 — CHOICE.** Each term is a constant multiple of a power of $x$.
Use linearity and the power rule.

**Step 3 — CALCULUS: keep each exponent and denominator visible.**

$$
\int q(x)\,dx
=6\frac{x^{2+1}}{2+1}-4\frac{x^{1+1}}{1+1}+5x+C.
$$

**Step 4 — ALGEBRA: simplify coefficients.**

$$
2+1=3,\qquad 1+1=2,\qquad \frac63=2,\qquad \frac42=2,
$$

$$
\int q(x)\,dx=2x^3-2x^2+5x+C.
$$

**Step 5 — CHECK: differentiate the full family.**

$$
\frac{d}{dx}\left(2x^3-2x^2+5x+C\right)
=2(3x^2)-2(2x)+5(1)+0=6x^2-4x+5=q(x).
$$

The derivative of $C$ is zero precisely because $C$ is independent of $x$.

### I1-002

**Step 1 — SETUP.** $x\ne0$ is the real scalar integration variable and
$q(x)=3/x$ is real scalar-valued. Work separately on the two connected intervals.
Let $C_+$ and $C_-$ be fixed real scalar constants independent of $x$.

**Step 2 — CHOICE.** The ordinary power antiderivative would divide by
$-1+1=0$. Use the logarithm rule instead.

**Step 3 — CALCULUS: give the families on their own intervals.**

$$
\int q(x)\,dx=
\begin{cases}
3\ln(x)+C_+,&x>0,\\
3\ln(-x)+C_-,&x<0.
\end{cases}
$$

Equivalently, the antiderivative is $3\ln(|x|)$ plus a constant on each interval.
There is no requirement that $C_+=C_-$: the original domain is disconnected.

**Step 4 — CHECK: differentiate on both intervals.** For $x>0$,

$$
\frac{d}{dx}\left(3\ln(x)+C_+\right)=3\frac1x+0=\frac3x.
$$

For $x<0$, the input $-x$ of the logarithm is positive. The chain rule gives

$$
\frac{d}{dx}\left(3\ln(-x)+C_-\right)
=3\frac1{-x}(-1)+0.
$$

**Step 5 — ALGEBRA: simplify the negative-input check.**

$$
3\frac{-1}{-x}=3\frac1x=\frac3x=q(x).
$$

Neither family defines an antiderivative across $x=0$, where the integrand is undefined.

### I1-003

**Step 1 — SETUP.** Integrate the real scalar function $q(x)=2x+3$ with respect
to real scalar $x$ from $-1$ to $2$. The endpoints are fixed and the output is a number.

**Step 2 — CHOICE.** The integrand is continuous; use an antiderivative and
subtract the endpoint values.

**Step 3 — CALCULUS: find one antiderivative.** Choose the real scalar function

$$
F(x)=2\frac{x^{1+1}}{1+1}+3x=x^2+3x.
$$

The arbitrary constant can be set to zero because it cancels in the endpoint subtraction.

**Step 4 — ALGEBRA: calculate the endpoints separately.**

$$
F(2)=2^2+3(2)=4+6=10,
$$

$$
F(-1)=(-1)^2+3(-1)=1-3=-2.
$$

**Step 5 — CALCULUS: subtract the lower value.**

$$
\int_{-1}^{2}q(x)\,dx=F(2)-F(-1)=10-(-2).
$$

**Step 6 — ALGEBRA: remove the double negative.** $10-(-2)=10+2=12$.

**Step 7 — CHECK.** $\frac{d}{dx}\left(F(x)\right)=2x+3=q(x)$.
Also the straight-line graph has endpoint heights $q(-1)=1$ and $q(2)=7$.
Its trapezoid area is $((1+7)/2)(2-(-1))=(8/2)(3)=12$, agreeing with the integral.

### I1-004

**Step 1 — SETUP.** $x$ is a real scalar integration variable;
$q(x)=\exp(3x)$ is real scalar-valued on all real inputs. Let $A$ be a fixed
real scalar coefficient to determine and let $C$ be independent of $x$.

**Step 2 — CHOICE.** Try $F(x)=A\exp(3x)$ and choose $A$ so its derivative
matches the integrand. The inner function $g(x)=3x$ has derivative three.

**Step 3 — CALCULUS: differentiate the candidate.**

$$
\frac{d}{dx}\left(F(x)\right)=A\exp(3x)\frac{d}{dx}\left(3x\right)
=A\exp(3x)(3).
$$

**Step 4 — ALGEBRA: match coefficients.** To make this equal to $q(x)$,
solve $3A=1$, giving $A=1/3$ because three is nonzero.

**Step 5 — CALCULUS: state the family.**

$$
\int q(x)\,dx=\frac13\exp(3x)+C.
$$

**Step 6 — CHECK.**

$$
\frac{d}{dx}\left(\frac13\exp(3x)+C\right)
=\frac13\exp(3x)(3)+0
=\left(\frac13\cdot3\right)\exp(3x)=q(x).
$$

Omitting the coefficient $1/3$ would give three times the required integrand.

### I1-005

**Step 1 — SETUP.** $x$ is a real scalar integration variable in radians;
$q(x)=2\cos(x)-3\sin(x)$ is real scalar-valued. The constant $C$ is a real
scalar independent of $x$. All real inputs are allowed.

**Step 2 — CHOICE.** Use linearity, the sine derivative, and the cosine derivative.
Keep the negative sign of the cosine derivative visible.

**Step 3 — CALCULUS: integrate each term.**

$$
\int q(x)\,dx=2\sin(x)+3\cos(x)+C.
$$

**Step 4 — CHECK: differentiate before simplifying signs.**

$$
\frac{d}{dx}\left(2\sin(x)+3\cos(x)+C\right)
=2\cos(x)+3(-\sin(x))+0.
$$

**Step 5 — ALGEBRA: simplify the sign.**

$$
2\cos(x)+3(-\sin(x))+0=2\cos(x)-3\sin(x)=q(x).
$$

The positive coefficient on $\cos(x)$ in the antiderivative is needed to
produce the negative sine term in the integrand.

### I1-006

**Step 1 — SETUP.** $x$ is a real scalar integration variable on $[-1,1]$.
$q(x)=x$ is real scalar-valued. Both requested integrals have fixed limits and
real scalar number outputs.

**Step 2 — CHOICE.** Integrate $x$ directly for signed accumulation; split
at zero before integrating $|x|$.

**Step 3 — CALCULUS: evaluate the signed integral.**

$$
\int_{-1}^{1}q(x)\,dx
=\left.\frac{x^2}{2}\right|_{x=-1}^{x=1}
=\frac{1^2}{2}-\frac{(-1)^2}{2}.
$$

**Step 4 — ALGEBRA: show the cancellation.**

$$
\frac{1^2}{2}-\frac{(-1)^2}{2}=\frac12-\frac12=0.
$$

**Step 5 — CALCULUS: split the nonnegative integral.**

$$
\begin{aligned}
\int_{-1}^{1}|q(x)|\,dx
&=\int_{-1}^{0}(-x)\,dx+\int_0^1 x\,dx\\
&=\left.-\frac{x^2}{2}\right|_{x=-1}^{x=0}
+\left.\frac{x^2}{2}\right|_{x=0}^{x=1}.
\end{aligned}
$$

**Step 6 — ALGEBRA: subtract each lower endpoint.**

$$
\left(-\frac{0^2}{2}-\left(-\frac{(-1)^2}{2}\right)\right)
+\left(\frac{1^2}{2}-\frac{0^2}{2}\right)
=\left(0+\frac12\right)+\left(\frac12-0\right)=1.
$$

**Step 7 — CHECK.** The absolute-value graph consists of two right triangles,
each of base one and height one. Their total area is
$2(1\cdot1/2)=1$. The signed integral is zero because the negative triangle
and positive triangle have opposite signed contributions.
