# D2 · Products, quotients, and compositions

Look at the whole expression before choosing a rule. A product has two changing
factors; a quotient has a changing denominator; a composition feeds one function
into another. The examples show how to recognize and combine these structures.

## Rules to consult

Here $x$ is an independent real scalar. $u(x)$ and $v(x)$ are differentiable real
scalar functions. Each derivative below is a real scalar output. At inputs where
$v(x)\ne0$, the product and quotient rules are

$$
\frac{d}{dx}\left(u(x)v(x)\right)
=\frac{d}{dx}\left(u(x)\right)v(x)+u(x)\frac{d}{dx}\left(v(x)\right),
$$

$$
\frac{d}{dx}\left(\frac{u(x)}{v(x)}\right)
=\frac{\frac{d}{dx}\left(u(x)\right)v(x)-u(x)\frac{d}{dx}\left(v(x)\right)}{(v(x))^2}.
$$

The product rule itself does not require $v(x)\ne0$. For a composition
$f(x)=h(g(x))$, let $t$ be an auxiliary independent real scalar input for $h(t)$.
Assuming both derivatives exist at the inputs used, the chain rule is

$$
\frac{d}{dx}\left(f(x)\right)
=\left.\frac{d}{dt}\left(h(t)\right)\right|_{t=g(x)}
\frac{d}{dx}\left(g(x)\right).
$$

Differentiate the outer function in its own input, evaluate that derivative at
the inner function, and multiply by the inner derivative. Repeat this process
for nested compositions. The elementary rules needed below are

$$
\begin{aligned}
\frac{d}{dt}\left(\exp(t)\right)&=\exp(t),\\
\frac{d}{dt}\left(\ln(t)\right)&=\frac1t,\qquad t>0,\\
\frac{d}{dt}\left(\sin(t)\right)&=\cos(t),\\
\frac{d}{dt}\left(\cos(t)\right)&=-\sin(t).
\end{aligned}
$$

Sine and cosine inputs are in radians. The exponential has every real input;
the real logarithm requires a positive input. Powers use the rules and domains
from [scalar differentiation foundations](DIFFERENTIATION_SCALARS.md).

## Problems

### D2-001 — Differentiate a composition

**Objects and dependencies.** $x\in\mathbb R$ is an independent scalar variable. The scalar-valued function $f:\mathbb R\to\mathbb R$ is

$$
f(x)=(3x^2+1)^4.
$$

There are no other variables or parameters. Find the scalar-valued derivative

$$
\frac{d}{dx}\left(f(x)\right).
$$

### D2-002 — A polynomial times a sine

**Objects and dependencies.** $x$ is an independent real scalar angle in radians.
The real scalar function $f(x)=x^2\sin(x)$ is defined for all real $x$. No parameters
vary. Find $\frac{d}{dx}\left(f(x)\right)$ and its value at $x=\pi$, where $\pi$ is
the fixed circle constant.

### D2-003 — A quotient with an excluded input

**Objects and dependencies.** $x$ is an independent real scalar with $x\ne1$.
The real scalar function is $f(x)=(x^2+1)/(x-1)$. Find the scalar-valued derivative
$\frac{d}{dx}\left(f(x)\right)$ and its value at $x=2$.

### D2-004 — An exponential of a quadratic

**Objects and dependencies.** $x$ is an independent real scalar. Define the real
scalar function $f(x)=\exp(2x^2-3)$ on all real inputs. Find
$\frac{d}{dx}\left(f(x)\right)$ and its value at $x=0$.

### D2-005 — A logarithm with a changing input

**Objects and dependencies.** $x$ is an independent real scalar. Define the real
scalar function $f(x)=\ln(1+x^2)$ on all real inputs, since $1+x^2>0$.
Find $\frac{d}{dx}\left(f(x)\right)$ and its value at $x=1$.

### D2-006 — A root with a changing input

**Objects and dependencies.** $x$ is an independent real scalar. Define the real
scalar function $f(x)=\sqrt{1+x^2}$, taking the nonnegative square root. Find
$\frac{d}{dx}\left(f(x)\right)$ for every real $x$ and evaluate at $x=0$.

### D2-007 — Three layers of dependence

**Objects and dependencies.** $x$ is an independent real scalar angle in radians.
The real scalar function is $f(x)=(\sin(2x))^3$. Find
$\frac{d}{dx}\left(f(x)\right)$ for all real $x$ and evaluate at $x=\pi/4$.

## Hint ladders

### D2-001

1. Which expression is raised to the fourth power?
2. Define the inner function $g(x)=3x^2+1$, and the outer function $h(u)=u^4$. Then $f(x)=h(g(x))$.
3. Differentiate $h(u)$ with respect to $u$, evaluate at $u=g(x)$, and multiply by the derivative of $g(x)$ with respect to $x$.

### D2-002

1. Both factors change with $x$; use the product rule.
2. Differentiate $x^2$ and $\sin(x)$ separately.
3. Keep the unchanged factor in each product-rule term; then substitute $x=\pi$.

### D2-003

1. The numerator and denominator have different rates of change.
2. Use the quotient rule with numerator $u(x)=x^2+1$ and denominator $v(x)=x-1$.
3. Expand $2x(x-1)-(x^2+1)$ before evaluating.

### D2-004

1. The exponential's input is a changing quadratic.
2. Set $g(x)=2x^2-3$ and $h(t)=\exp(t)$.
3. Multiply $\exp(g(x))$ by the derivative of $g(x)$.

### D2-005

1. The derivative of a logarithm must include its inner rate of change.
2. Set $g(x)=1+x^2$ and $h(t)=\ln(t)$, with $t>0$.
3. Evaluate $1/t$ at $t=g(x)$ and multiply by $2x$.

### D2-006

1. Rewrite the square root as a power of its entire input.
2. Differentiate $h(t)=t^{1/2}$ on $t>0$ and $g(x)=1+x^2$.
3. Simplify $(1/2)(1+x^2)^{-1/2}(2x)$.

### D2-007

1. There is an outer cube, a sine, and an inner multiplication by two.
2. Differentiate $g(x)=2x$, then $u(x)=\sin(g(x))$.
3. Differentiate the cube of $u(x)$ and retain the inner factor two.

## Complete solutions

### D2-001

**Step 1 — SETUP.** The independent input $x$ is scalar. The output $f(x)=(3x^2+1)^4$ is scalar and is defined for all real $x$. Introduce scalar-valued functions

$$
g(x)=3x^2+1,\qquad h(u)=u^4,\qquad f(x)=h(g(x)).
$$

Here $u$ is an independent scalar input when defining and differentiating $h(u)$. In the composition, set $u=g(x)$, so the inner value depends on $x$.

**Step 2 — CHOICE.** A fourth power surrounds a changing inner expression. The chain rule accounts for both the outer power and the inner rate of change.

**Step 3 — CALCULUS: differentiate the outer function.** The power rule gives

$$
\frac{d}{du}\left(h(u)\right)
=\frac{d}{du}\left(u^4\right)
=4u^3.
$$

**Step 4 — CALCULUS: differentiate the inner function.** Use the sum rule, constant-multiple rule, power rule, and derivative of a constant:

$$
\begin{aligned}
\frac{d}{dx}\left(g(x)\right)
&=\frac{d}{dx}\left(3x^2+1\right)\\
&=3\frac{d}{dx}\left(x^2\right)+\frac{d}{dx}\left(1\right)\\
&=3(2x)+0.
\end{aligned}
$$

**Step 5 — ALGEBRA.** Multiply the numerical factors and remove the zero:

$$
3(2x)+0=(3\cdot2)x+0=6x+0=6x.
$$

**Step 6 — CALCULUS: assemble the chain rule.**

$$
\begin{aligned}
\frac{d}{dx}\left(f(x)\right)
&=\left.\frac{d}{du}\left(h(u)\right)\right|_{u=g(x)}
\frac{d}{dx}\left(g(x)\right)\\
&=\left.\left(4u^3\right)\right|_{u=3x^2+1}(6x)\\
&=4(3x^2+1)^3(6x).
\end{aligned}
$$

**Step 7 — ALGEBRA.** All factors are scalar, so they may be reordered:

$$
4(3x^2+1)^3(6x)=(4\cdot6)x(3x^2+1)^3=24x(3x^2+1)^3.
$$

**Result.**

$$
\boxed{\frac{d}{dx}\left(f(x)\right)=24x(3x^2+1)^3.}
$$

**Step 8 — CHECK.** At $x=0$, the formula gives $24(0)(1)^3=0$. Independently, the derivative definition at zero is

$$
\lim_{\varepsilon\to0}\frac{f(\varepsilon)-f(0)}{\varepsilon}.
$$

Here $\varepsilon$ is a nonzero scalar increment tending to zero. For the check, the binomial identity
$(a+b)^4=a^4+4a^3b+6a^2b^2+4ab^3+b^4$, with $a=1$, $b=3\varepsilon^2$, gives the following **IDENTITY and ALGEBRA** steps:

$$
\begin{aligned}
f(\varepsilon)&=1+4(3\varepsilon^2)+6(3\varepsilon^2)^2+4(3\varepsilon^2)^3+(3\varepsilon^2)^4\\
&=1+12\varepsilon^2+54\varepsilon^4+108\varepsilon^6+81\varepsilon^8,\\
f(0)&=1,\\
\frac{f(\varepsilon)-f(0)}{\varepsilon}
&=\frac{12\varepsilon^2+54\varepsilon^4+108\varepsilon^6+81\varepsilon^8}{\varepsilon}\\
&=12\varepsilon+54\varepsilon^3+108\varepsilon^5+81\varepsilon^7.
\end{aligned}
$$

Each term tends to zero, so the limit is zero. This checks the answer at one input; it is not a separate proof of the derivative formula at every input.

**Recognition cue.** Find the outside operation, then identify every input it receives. The inner derivative is required even when the inner expression looks simple.

### D2-002

**Step 1 — SETUP.** $x$ is an independent real scalar angle in radians.
$f(x)=x^2\sin(x)$ is real scalar-valued. Let $u(x)=x^2$ and $v(x)=\sin(x)$;
both are real scalar functions on all real inputs. The output derivative is scalar.

**Step 2 — CHOICE.** This is a product of two changing factors. Differentiating
both and multiplying would omit the product rule's two terms.

**Step 3 — CALCULUS: differentiate each factor and apply the product rule.**

$$
\frac{d}{dx}\left(u(x)\right)=2x,\qquad
\frac{d}{dx}\left(v(x)\right)=\cos(x),
$$

$$
\frac{d}{dx}\left(f(x)\right)
=(2x)\sin(x)+x^2\cos(x).
$$

**Step 4 — ALGEBRA: evaluate after differentiating.** Since $\sin(\pi)=0$ and
$\cos(\pi)=-1$,

$$
\left.\frac{d}{dx}\left(f(x)\right)\right|_{x=\pi}
=(2\pi)(0)+\pi^2(-1)=0-\pi^2=-\pi^2.
$$

**Step 5 — TRICK: use an angle-addition identity.** For real scalar angles
$a,b$ in radians,

$$
\sin(a+b)=\sin(a)\cos(b)+\cos(a)\sin(b).
$$

Taking $a=\pi$ and $b=h$, with real scalar increment $h$, gives
$\sin(\pi+h)=0\cos(h)+(-1)\sin(h)=-\sin(h)$.
This identity follows from the [Euler identities](TRICKS_APPENDIX.md#t-001-euler-identities).

**Step 6 — CHECK.** The difference quotient at this input, with real scalar
increment $h\ne0$, is

$$
\frac{f(\pi+h)-f(\pi)}h
=(\pi+h)^2\frac{\sin(\pi+h)}h.
$$

Using the identity from Step 5, the limit as
$h\to0$ is $\pi^2(-1)=-\pi^2$, using $\lim_{h\to0}\sin(h)/h=1$ in radians.
This independently verifies the requested evaluated derivative.

### D2-003

**Step 1 — SETUP.** $x\ne1$ is an independent real scalar and
$f(x)=(x^2+1)/(x-1)$ is real scalar-valued. Let $u(x)=x^2+1$ and $v(x)=x-1$.
All coefficients are fixed. The derivative is scalar-valued on this domain.

**Step 2 — CHOICE.** The denominator changes and does not cancel. Use the quotient rule.

**Step 3 — CALCULUS: retain the quotient rule's subtraction.**

$$
\frac{d}{dx}\left(u(x)\right)=2x,\qquad
\frac{d}{dx}\left(v(x)\right)=1,
$$

$$
\frac{d}{dx}\left(f(x)\right)
=\frac{(2x)(x-1)-(x^2+1)(1)}{(x-1)^2}.
$$

**Step 4 — ALGEBRA: expand the numerator.**

$$
(2x)(x-1)-(x^2+1)(1)
=2x^2-2x-x^2-1=(2-1)x^2-2x-1=x^2-2x-1.
$$

Therefore

$$
\frac{d}{dx}\left(f(x)\right)=\frac{x^2-2x-1}{(x-1)^2},\qquad x\ne1.
$$

At $x=2$, the scalar value is

$$
\frac{2^2-2(2)-1}{(2-1)^2}=
\frac{4-4-1}{1^2}=\frac{-1}{1}=-1.
$$

**Step 5 — CHECK: differentiate an equivalent rewrite.** Since
$(x-1)(x+1)+2=x^2-1+2=x^2+1$,

$$
f(x)=x+1+\frac{2}{x-1},\qquad x\ne1.
$$

The chain and sum rules give

$$
\frac{d}{dx}\left(f(x)\right)=1-\frac{2}{(x-1)^2}
=\frac{(x-1)^2-2}{(x-1)^2}
=\frac{x^2-2x+1-2}{(x-1)^2}.
$$

This matches the result. The excluded input remains excluded.

### D2-004

**Step 1 — SETUP.** $x$ is an independent real scalar;
$f(x)=\exp(2x^2-3)$ is real scalar-valued on all real inputs. Define
$g(x)=2x^2-3$ and $h(t)=\exp(t)$, where $t$ is an independent real scalar
input for the outer function. In $f(x)=h(g(x))$, its input depends on $x$.

**Step 2 — CHOICE.** Differentiate the exponential at its inner input, then
account for how that input changes.

**Step 3 — CALCULUS: calculate both derivatives.**

$$
\frac{d}{dt}\left(h(t)\right)=\exp(t),\qquad
\frac{d}{dx}\left(g(x)\right)=2(2x)-0.
$$

**Step 4 — ALGEBRA: simplify the inner derivative.**

$$
2(2x)-0=(2\cdot2)x=4x.
$$

**Step 5 — CALCULUS: apply the chain rule.**

$$
\frac{d}{dx}\left(f(x)\right)
=\left.\exp(t)\right|_{t=2x^2-3}(4x)
=\exp(2x^2-3)(4x).
$$

**Step 6 — ALGEBRA: evaluate.** At $x=0$, $2(0)^2-3=-3$ and $4(0)=0$;
the value is $\exp(-3)(0)=0$.

**Step 7 — CHECK.** $f(-x)=\exp(2(-x)^2-3)=f(x)$, so the differentiable graph
is symmetric about zero and has derivative zero there. Also $\exp(2x^2-3)>0$,
so the derivative has the sign of $x$, consistent with a minimum at zero.
These are plausibility checks; the chain rule establishes the formula.

### D2-005

**Step 1 — SETUP.** $x$ is an independent real scalar and
$f(x)=\ln(1+x^2)$ is real scalar-valued. Define $g(x)=1+x^2$ and $h(t)=\ln(t)$
for independent real scalar $t>0$. Since $g(x)\ge1$, every real $x$ is allowed.

**Step 2 — CHOICE.** The logarithm rule is applied to $t$, then evaluated at
$t=g(x)$. Its input has a separate derivative.

**Step 3 — CALCULUS: differentiate both layers.**

$$
\frac{d}{dt}\left(h(t)\right)=\frac1t,\qquad
\frac{d}{dx}\left(g(x)\right)=0+2x=2x,
$$

$$
\frac{d}{dx}\left(f(x)\right)
=\left.\frac1t\right|_{t=1+x^2}(2x)=\frac{1}{1+x^2}(2x).
$$

**Step 4 — ALGEBRA: simplify and evaluate.**

$$
\frac{1}{1+x^2}(2x)=\frac{2x}{1+x^2},\qquad
\left.\frac{d}{dx}\left(f(x)\right)\right|_{x=1}
=\frac{2(1)}{1+1^2}=\frac2{1+1}=\frac22=1.
$$

**Step 5 — CHECK.** The denominator is always positive. The derivative vanishes
at zero and changes from negative to positive there, consistent with
$f(x)\ge\ln(1)=0=f(0)$. Do not replace $\ln(1+x^2)$ by $\ln(1)+\ln(x^2)$:
logarithm rules separate products, not sums.

### D2-006

**Step 1 — SETUP.** $x$ is an independent real scalar. The real scalar functions
are $g(x)=1+x^2$, $h(t)=t^{1/2}$ for independent real scalar $t>0$, and
$f(x)=h(g(x))$. The inner value is at least one, so all real $x$ are allowed.

**Step 2 — CHOICE.** The root is a power of a changing expression; use the
power rule for the outer input and the chain rule for the composition.

**Step 3 — CALCULUS: differentiate both layers.**

$$
\frac{d}{dt}\left(h(t)\right)=\frac12t^{1/2-1},\qquad
\frac{d}{dx}\left(g(x)\right)=2x.
$$

**Step 4 — ALGEBRA: subtract the exponents.**

$$
\frac12-1=\frac12-\frac22=-\frac12,
\qquad t^{-1/2}=\frac1{\sqrt t},\quad t>0.
$$

**Step 5 — CALCULUS: assemble the chain rule.**

$$
\frac{d}{dx}\left(f(x)\right)=\frac1{2\sqrt{1+x^2}}(2x).
$$

**Step 6 — ALGEBRA: simplify and evaluate.**

$$
\frac{2x}{2\sqrt{1+x^2}}=\frac{x}{\sqrt{1+x^2}},\qquad
\left.\frac{d}{dx}\left(f(x)\right)\right|_{x=0}
=\frac0{\sqrt{1+0}}=\frac01=0.
$$

**Step 7 — CHECK: differentiate a defining relation.** Since $(f(x))^2=1+x^2$,
the chain rule implies

$$
2f(x)\frac{d}{dx}\left(f(x)\right)=2x.
$$

Dividing by $2f(x)>0$ gives $x/f(x)=x/\sqrt{1+x^2}$, which agrees.

### D2-007

**Step 1 — SETUP.** $x$ is an independent real scalar angle in radians.
Let $g(x)=2x$, $u(x)=\sin(g(x))$, and $f(x)=(u(x))^3$; all outputs are real
scalars. Use auxiliary independent real scalar inputs $t$ for $h(t)=\sin(t)$
and $s$ for $p(s)=s^3$. All real $x$ are allowed.

**Step 2 — CHOICE.** Track the three operations from the inside out: multiply
by two, take a sine, and take a cube.

**Step 3 — CALCULUS: differentiate the inner composition.**

$$
\frac{d}{dx}\left(g(x)\right)=2,\qquad
\frac{d}{dt}\left(h(t)\right)=\cos(t),
$$

$$
\frac{d}{dx}\left(u(x)\right)
=\left.\cos(t)\right|_{t=2x}(2)=2\cos(2x).
$$

**Step 4 — CALCULUS: differentiate the outer cube.**

$$
\frac{d}{ds}\left(p(s)\right)=3s^2,
$$

$$
\frac{d}{dx}\left(f(x)\right)
=\left.3s^2\right|_{s=\sin(2x)}\left(2\cos(2x)\right).
$$

**Step 5 — ALGEBRA: multiply constants and evaluate.**

$$
3(\sin(2x))^2(2\cos(2x))
=(3\cdot2)(\sin(2x))^2\cos(2x)
=6(\sin(2x))^2\cos(2x).
$$

At $x=\pi/4$, $2x=2(\pi/4)=\pi/2$, $\sin(\pi/2)=1$, and
$\cos(\pi/2)=0$. The derivative's value is $6(1)^2(0)=0$.

**Step 6 — TRICK: use the angle-addition identity.** For real scalar angles
$a,b$ in radians, $\sin(a+b)=\sin(a)\cos(b)+\cos(a)\sin(b)$.
At $a=\pi/2$ and $b=2h$, for real scalar increment $h$,

$$
\sin(\pi/2+2h)=1\cos(2h)+0\sin(2h)=\cos(2h).
$$

This is another use of the [Euler identities](TRICKS_APPENDIX.md#t-001-euler-identities).

**Step 7 — CHECK.** Substitution into the original function gives
$f(\pi/4+h)=(\sin(\pi/2+2h))^3=(\cos(2h))^3$.
This expression is even in $h$ and differentiable,
so its derivative at $h=0$ is zero. This checks the evaluated slope; the chain-rule
calculation establishes the general formula.
