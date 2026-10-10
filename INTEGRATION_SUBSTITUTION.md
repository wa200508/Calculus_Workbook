# I2 · Substitution with every dependency visible

Substitution is a main integration method. Identify an inner function and its
derivative, account for any fixed coefficient, and change both bounds in a definite
integral. For an indefinite integral, substitute back into the original variable.

## Rule to consult

Here $x$ is a real scalar integration variable, $g(x)$ is a continuously
differentiable real scalar function, and $h(u)$ is a continuous real scalar
function on the image of the interval used. The new real scalar coordinate
$u=g(x)$ depends on $x$ before the change of variable. Inside the transformed
integral, $u$ is the integration variable. For fixed real endpoints $a,b$,

$$
\int_a^b h(g(x))\frac{d}{dx}\left(g(x)\right)\,dx
=\int_{g(a)}^{g(b)}h(u)\,du.
$$

The bounds on the right are computed with the same function $g(x)$.
Do not carry the old bounds into the new variable. For an indefinite integral,
if $H(u)$ is an antiderivative of $h(u)$, then

$$
\int h(g(x))\frac{d}{dx}\left(g(x)\right)\,dx=H(g(x))+C,
$$

where the real scalar $C$ is independent of $x$. Check the result by the chain rule.

## Problems

### I2-001 — Evaluate a definite integral

**Objects and dependencies.** $x$ is a scalar integration variable in $[0,1]$. Define the scalar-valued function $q(x)=2x(x^2+1)^3$. All quantities are real. Integrate with respect to $x$, with lower limit $x=0$ and upper limit $x=1$. Find the scalar number

$$
\int_{0}^{1} q(x)\,dx
=\int_{0}^{1} 2x(x^2+1)^3\,dx.
$$

### I2-002 — A derivative match needing a fixed multiplier

**Objects and dependencies.** $x$ is a real scalar integration variable;
$q(x)=x(1+x^2)^4$ is real scalar-valued on all real inputs. Find the scalar
antiderivative family $\int q(x)\,dx$.

### I2-003 — A cubic inside an exponential

**Objects and dependencies.** $x$ is a real scalar integration variable from
$x=0$ to $x=1$. The real scalar function is $q(x)=3x^2\exp(x^3)$.
Find the real scalar number $\int_0^1q(x)\,dx$.

### I2-004 — A trigonometric input inside a reciprocal

**Objects and dependencies.** $x$ is a real scalar angle in radians and is the
integration variable. Define $q(x)=\cos(x)/(2+\sin(x))$ with real scalar output.
The denominator is at least one, so every real input is allowed. Find
$\int q(x)\,dx$.

### I2-005 — Transforming reversed endpoints

**Objects and dependencies.** $x$ is a real scalar integration variable with
lower limit $x=1$ and upper limit $x=0$. The real scalar function is
$q(x)=2x/(1+x^2)$. Find the real scalar number $\int_1^0q(x)\,dx$.

## Hint ladders

### I2-001

1. Compare the factor $2x$ with the derivative of the expression $x^2+1$.
2. Try the new scalar coordinate $u=g(x)=x^2+1$.
3. The original endpoints $x=0$ and $x=1$ become $u=1$ and $u=2$. The transformed integrand is $u^3$.

### I2-002

1. The inner expression is $1+x^2$, whose derivative is $2x$.
2. Write $x=(1/2)(2x)$ rather than dropping the missing two.
3. Integrate $(1/2)u^4$ and replace $u$ by $1+x^2$ afterward.

### I2-003

1. Compare $3x^2$ with the derivative of $x^3$.
2. With $u=g(x)=x^3$, the new bounds are $u=0$ and $u=1$.
3. An antiderivative of $\exp(u)$ is $\exp(u)$.

### I2-004

1. The denominator's derivative is the numerator.
2. Set $u=g(x)=2+\sin(x)$; its values are positive.
3. Integrate $1/u$ and then display the original input of the logarithm.

### I2-005

1. The derivative of the denominator matches the numerator.
2. The old lower endpoint $x=1$ becomes $u=2$, and the old upper endpoint $x=0$ becomes $u=1$.
3. Subtract the value at $u=2$ from the value at $u=1$.

## Complete solutions

### I2-001

**Step 1 — SETUP.** The original scalar variable is $x\in[0,1]$, and the scalar integrand is $q(x)=2x(x^2+1)^3$. Introduce

$$
g(x)=x^2+1,\qquad u=g(x),\qquad h(u)=u^3.
$$

Both $g$ and $h$ are scalar-valued functions. The new coordinate $u$ depends on $x$ until we rewrite the integral in terms of $u$. Polynomials have the continuity and differentiability needed for the substitution theorem.

**Step 2 — CHOICE.** The integrand contains a power of $x^2+1$ and the factor $2x$, which is the derivative of $x^2+1$. This is the reverse of the chain-rule pattern.

**Step 3 — CALCULUS.**

$$
\begin{aligned}
\frac{d}{dx}\left(g(x)\right)
&=\frac{d}{dx}\left(x^2+1\right)\\
&=\frac{d}{dx}\left(x^2\right)+\frac{d}{dx}\left(1\right)\\
&=2x+0=2x.
\end{aligned}
$$

The last removal of $+0$ is an **ALGEBRA** simplification.

**Step 4 — ALGEBRA: match the integrand.** Since the factors are scalars,

$$
2x(x^2+1)^3=(x^2+1)^3(2x)
=h(g(x))\frac{d}{dx}\left(g(x)\right).
$$

**Step 5 — ALGEBRA: transform both bounds.**

$$
\begin{aligned}
x=0&\quad\Longrightarrow\quad u=g(0)=0^2+1=0+1=1,\\
x=1&\quad\Longrightarrow\quad u=g(1)=1^2+1=1+1=2.
\end{aligned}
$$

**Step 6 — CALCULUS: apply the substitution theorem.**

$$
\begin{aligned}
\int_{0}^{1} 2x(x^2+1)^3\,dx
&=\int_{0}^{1}
\left(h(g(x))\frac{d}{dx}\left(g(x)\right)\right)\,dx\\
&=\int_{g(0)}^{g(1)} h(u)\,du\\
&=\int_{1}^{2} u^3\,du.
\end{aligned}
$$

The whole integral changes coordinates, including the integration variable and both bounds. The derivative factor is accounted for by the theorem.

**Step 7 — CALCULUS: find an antiderivative.** The power rule for integration is

$$
\int u^p\,du=\frac{u^{p+1}}{p+1}+C,\qquad p\ne-1,
$$

on an interval where the powers and this rule are defined. Here $p=3$ is a fixed scalar exponent and $u\in[1,2]$. Choose one antiderivative $H(u)$:

$$
H(u)=\frac{u^{3+1}}{3+1}=\frac{u^4}{4}.
$$

The exponent and denominator simplifications are **ALGEBRA**. A definite integral needs one antiderivative; any added constant cancels in the endpoint difference.

**Step 8 — CALCULUS: evaluate at the endpoints.**

$$
\int_{1}^{2} u^3\,du=H(2)-H(1)=\frac{2^4}{4}-\frac{1^4}{4}.
$$

**Step 9 — ALGEBRA.**

$$
\begin{aligned}
2^4&=2\cdot2\cdot2\cdot2=16,\\
1^4&=1\cdot1\cdot1\cdot1=1,\\
\frac{2^4}{4}-\frac{1^4}{4}
&=\frac{16}{4}-\frac{1}{4}
=\frac{16-1}{4}
=\frac{15}{4}.
\end{aligned}
$$

**Result.**

$$
\boxed{\int_{0}^{1} 2x(x^2+1)^3\,dx=\frac{15}{4}.}
$$

**Step 10 — CHECK: differentiate the original-variable antiderivative.** Define the scalar-valued function $Q(x)=(x^2+1)^4/4$. The constant-multiple and chain rules give

$$
\frac{d}{dx}\left(Q(x)\right)
=\frac14\,4(x^2+1)^3(2x).
$$

**ALGEBRA:** $(1/4)\cdot4=1$, so this becomes $2x(x^2+1)^3=q(x)$, the original integrand. Also,

$$
Q(1)-Q(0)=\frac{(1^2+1)^4}{4}-\frac{(0^2+1)^4}{4}
=\frac{2^4}{4}-\frac{1^4}{4}=\frac{15}{4}.
$$

**Recognition cue.** Look for an inner expression whose derivative appears as a multiplying factor. A near match may need a constant adjustment, which must be written explicitly.

### I2-002

**Step 1 — SETUP.** $x$ is the real scalar integration variable and
$q(x)=x(1+x^2)^4$ is real scalar-valued. Let $g(x)=1+x^2$ and
$h(u)=u^4$, with independent real scalar input $u$ when defining $h(u)$.
Before substitution $u=g(x)$ is dependent on $x$. All real $x$ are allowed.

**Step 2 — CHOICE.** The factor $x$ is one half of the inner derivative.
Keep that adjustment outside the integral.

**Step 3 — CALCULUS: compute the inner derivative.**

$$
\frac{d}{dx}\left(g(x)\right)=\frac{d}{dx}\left(1+x^2\right)=0+2x=2x.
$$

**Step 4 — ALGEBRA: match every factor.**

$$
x(1+x^2)^4=\frac12(2x)(1+x^2)^4
=\frac12h(g(x))\frac{d}{dx}\left(g(x)\right).
$$

No division by $x$ was used; the identity holds at $x=0$ too.

**Step 5 — CALCULUS: change variable and integrate.**

$$
\int q(x)\,dx=\frac12\int u^4\,du
=\frac12\frac{u^{4+1}}{4+1}+C.
$$

**Step 6 — ALGEBRA: simplify and substitute back.**

$$
4+1=5,\qquad \frac12\frac{u^5}{5}=\frac{u^5}{2\cdot5}=\frac{u^5}{10},
$$

$$
\int q(x)\,dx=\frac{(1+x^2)^5}{10}+C.
$$

The real scalar constant $C$ is independent of $x$.

**Step 7 — CHECK.** By the chain rule,

$$
\frac{d}{dx}\left(\frac{(1+x^2)^5}{10}+C\right)
=\frac1{10}5(1+x^2)^4(2x)+0.
$$

The fixed coefficient is $(1/10)\cdot5\cdot2=10/10=1$, so the derivative
is $x(1+x^2)^4=q(x)$.

### I2-003

**Step 1 — SETUP.** $x$ is the real scalar integration variable from zero to one.
$q(x)=3x^2\exp(x^3)$ has real scalar output. Let $g(x)=x^3$ and
$h(u)=\exp(u)$, with auxiliary independent real scalar input $u$.
All functions used are smooth on the interval; the result is a number.

**Step 2 — CHOICE.** The numerator factor $3x^2$ is exactly the derivative
of the exponential's inner input.

**Step 3 — CALCULUS: compute the derivative and new bounds.**

$$
\frac{d}{dx}\left(g(x)\right)=3x^2,\qquad
u=g(0)=0^3=0,\qquad u=g(1)=1^3=1.
$$

**Step 4 — CALCULUS: transform the whole integral.**

$$
\int_0^1q(x)\,dx
=\int_0^1h(g(x))\frac{d}{dx}\left(g(x)\right)\,dx
=\int_0^1\exp(u)\,du.
$$

The numerical bounds happen to agree, but the variable and its meaning changed.

**Step 5 — CALCULUS: evaluate the antiderivative.**

$$
\int_0^1\exp(u)\,du=\exp(1)-\exp(0).
$$

**Step 6 — ALGEBRA: simplify the constant value.** Since $\exp(0)=1$, the
answer is $\exp(1)-1$. The notation $e=\exp(1)$ denotes a fixed real constant.

**Step 7 — CHECK.** Define the real scalar function $F(x)=\exp(x^3)$.
Its derivative is $\exp(x^3)(3x^2)=q(x)$. Also
$F(1)-F(0)=\exp(1)-1$. This verifies both the integrand match and endpoint result.

### I2-004

**Step 1 — SETUP.** $x$ is a real scalar integration variable in radians.
$q(x)=\cos(x)/(2+\sin(x))$ is real scalar-valued for all real inputs.
Let $g(x)=2+\sin(x)$ and $h(u)=1/u$ for independent real scalar $u>0$.
The actual inner values satisfy $1\le g(x)\le3$.

**Step 2 — CHOICE.** The denominator's derivative appears in the numerator.
Use a reciprocal antiderivative after the change of variable.

**Step 3 — CALCULUS: differentiate the inner function.**

$$
\frac{d}{dx}\left(g(x)\right)=0+\cos(x)=\cos(x).
$$

**Step 4 — CALCULUS: transform and integrate.**

$$
\int q(x)\,dx=\int\frac1u\,du=\ln(u)+C,\qquad u>0.
$$

The scalar constant $C$ is independent of the original input $x$.

**Step 5 — ALGEBRA: restore the original input.**

$$
\int q(x)\,dx=\ln(2+\sin(x))+C.
$$

No absolute value is needed because the logarithm's input is always positive.

**Step 6 — CHECK: differentiate the complete answer.**

$$
\frac{d}{dx}\left(\ln(2+\sin(x))+C\right)
=\frac1{2+\sin(x)}(\cos(x))+0
=\frac{\cos(x)}{2+\sin(x)}=q(x).
$$

The substitution theorem does not require $g(x)$ to be one-to-one. A vanishing
inner derivative at some inputs does not invalidate this antiderivative.

### I2-005

**Step 1 — SETUP.** $x$ is the real scalar integration variable, with fixed
lower limit one and upper limit zero. The real scalar function is
$q(x)=2x/(1+x^2)$. Let $g(x)=1+x^2$ and $h(u)=1/u$ for independent real scalar
$u>0$. The result is a real scalar number.

**Step 2 — CHOICE.** The derivative factor matches the denominator's rate.
Preserve the endpoint order when mapping to the new variable.

**Step 3 — CALCULUS: compute the derivative and endpoint map.**

$$
\frac{d}{dx}\left(g(x)\right)=2x,
\qquad u=g(1)=1+1^2=2,\qquad u=g(0)=1+0^2=1.
$$

**Step 4 — CALCULUS: transform the bounds with the variable.**

$$
\int_1^0q(x)\,dx=\int_2^1\frac1u\,du=\ln(1)-\ln(2).
$$

**Step 5 — ALGEBRA: simplify the sign.** $\ln(1)=0$, so the value is
$0-\ln(2)=-\ln(2)$.

**Step 6 — CHECK.** The real scalar function $F(x)=\ln(1+x^2)$ has derivative
$2x/(1+x^2)=q(x)$ by the chain rule. The original endpoints give
$F(0)-F(1)=\ln(1)-\ln(2)$. In addition, $q(x)\ge0$ on $[0,1]$ and
$q(x)>0$ for $0<x\le1$, so reversing that interval must give a negative integral.
