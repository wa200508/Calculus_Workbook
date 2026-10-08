# Pilot examples for reviewing the notation

These examples use notation standard version 0.2 and test the solution granularity. Textual labels indicate the future color styling. Question and solution sections are separate here; typesetting will place solutions on separate pages.

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

### I2-001 — Evaluate a definite integral

**Objects and dependencies.** $x$ is a scalar integration variable in $[0,1]$. Define the scalar-valued function $q(x)=2x(x^2+1)^3$. All quantities are real. Integrate with respect to $x$, with lower limit $x=0$ and upper limit $x=1$. Find the scalar number

$$
\int_{0}^{1} q(x)\,dx
=\int_{0}^{1} 2x(x^2+1)^3\,dx.
$$

## Hint ladders

### D2-001

1. Which expression is raised to the fourth power?
2. Define the inner function $g(x)=3x^2+1$, and the outer function $h(u)=u^4$. Then $f(x)=h(g(x))$.
3. Differentiate $h(u)$ with respect to $u$, evaluate at $u=g(x)$, and multiply by the derivative of $g(x)$ with respect to $x$.

### I2-001

1. Compare the factor $2x$ with the derivative of the expression $x^2+1$.
2. Try the new scalar coordinate $u=g(x)=x^2+1$.
3. The original endpoints $x=0$ and $x=1$ become $u=1$ and $u=2$. The transformed integrand is $u^3$.

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

## Tutor entry point

Example request: “Help me with I2-001, Step 6. I understand the new bounds but not what happened to the factor $2x$. Use the notation standard and give me one step at a time.”

## Review questions before drafting full chapters

- Are the round grouping parentheses and nearby “held fixed” statements easy to follow?
- Do the pilot algebra steps give enough detail, or should common arithmetic move into expandable side explanations in a digital edition?
- Does the outer-function/inner-function setup make substitution and the chain rule easier to follow?

Practice variants and their complete solutions will be added when these pilots become chapter material.
