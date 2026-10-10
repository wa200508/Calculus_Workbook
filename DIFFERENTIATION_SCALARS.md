# D1 · Scalar differentiation foundations

Alpha chapter. This chapter develops powers, sums, fixed parameters, domains, and
evaluation. [Products, quotients, and compositions](DIFFERENTIATION_RULES.md)
extends this foundation with exponential, logarithmic, and trigonometric examples. Every problem below has hints, a complete
solution, and a check.

## What this chapter trains

Before reaching for a rule, identify the independent variable and inspect the
expression. Sometimes rewriting the algebra makes the calculus much simpler.
Your goal is to produce both a derivative and a statement of where it is valid.

All functions here have scalar inputs and scalar outputs. A derivative with
respect to a scalar input is a scalar-valued function; evaluating it at a
specified input gives a scalar number.

### A repeatable approach

1. **Declare:** identify the function, its inputs, fixed parameters, and domain.
2. **Inspect:** separate sums; distinguish fixed coefficients from changing expressions.
3. **Rewrite if useful:** turn roots and reciprocals into powers, or simplify a fraction without losing its original domain.
4. **Differentiate:** name each rule and retain the function arguments.
5. **Simplify:** show the coefficient and exponent arithmetic.
6. **Evaluate if requested:** substitute only after calculating the derivative.
7. **Check:** compare with the definition, check a sign, or use another valid calculation. State what that check actually establishes.

### When these rules are sufficient

A sum of constant multiples of powers of the independent variable fits this
chapter. A changing expression raised to a power, such as $(x^2+1)^4$, requires
the chain rule introduced in [D2-001](DIFFERENTIATION_RULES.md). A product of changing
factors or a quotient that does not simplify may require the product or quotient
rule. Never differentiate the factors of a product separately and multiply the
results.

## Rules with their assumptions

In this rule sheet $x$ is an independent real scalar, $c$ and $p$ are fixed real
scalar parameters, and $u(x),v(x)$ are scalar functions differentiable at the
inputs under consideration. The output of each derivative is scalar.

### Constant and constant-multiple rules

$$
\frac{d}{dx}\left(c\right)=0,
\qquad
\frac{d}{dx}\left(cu(x)\right)
=c\frac{d}{dx}\left(u(x)\right).
$$

“Constant” means independent of the chosen variable. A letter such as $a$ can be
a constant with respect to $x$ even though different problems assign it different
values. A function such as $a(x)$ is not a fixed coefficient.

### Sum and difference rules

$$
\frac{d}{dx}\left(u(x)+v(x)\right)
=\frac{d}{dx}\left(u(x)\right)
+\frac{d}{dx}\left(v(x)\right).
$$

For a difference, retain the minus sign between the derivatives. Apply these rules
repeatedly to longer sums, writing each term explicitly.

### Power rule

For a fixed real exponent $p$ and $x>0$,

$$
\frac{d}{dx}\left(x^p\right)=p x^{p-1}.
$$

Nonnegative integer powers are differentiable for all real $x$; handle the
constant power $x^0=1$ directly with the constant rule. Negative integer powers
require $x\ne0$. Fractional powers need their own real-domain check. The positive
domain version avoids ambiguous real powers of negative inputs, but it does not
say that every rational power is restricted to positive inputs.

This rule concerns $x^p$ with a fixed exponent. It does not directly apply to
$p^x$, where the exponent changes, or to a power of an inner function without
accounting for that function's derivative.

### Definition for checking a derivative

Declare $h$ as a nonzero real scalar increment. At an interior input $x$ where
the two-sided limit exists,

$$
\frac{d}{dx}\left(f(x)\right)
=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
$$

Require $x+h$ to lie in the function's domain. You may divide by $h$ before
taking the limit because the quotient uses nonzero increments. Substituting
$h=0$ into that quotient before simplifying would divide by zero.

These are standard derivative definitions and rules; see
[OpenStax, Calculus Volume 1, §3.1](https://openstax.org/books/calculus-volume-1/pages/3-1-defining-the-derivative)
and [§3.3](https://openstax.org/books/calculus-volume-1/pages/3-3-differentiation-rules).
The problems and worked explanations below are original to this workbook.

## Problems

### D1-001 — A polynomial, term by term

**Objects and dependencies.** $x\in\mathbb R$ is the independent scalar variable.
The scalar function is $f(x)=4x^3-5x^2+7x-9$, defined for every real $x$.
All coefficients are fixed real scalars. Find the scalar-valued function

$$
\frac{d}{dx}\left(f(x)\right).
$$

### D1-002 — A root and a reciprocal

**Objects and dependencies.** $x$ is an independent real scalar with $x>0$.
The scalar function is

$$
f(x)=5\sqrt{x}-\frac{3}{x^2}+2.
$$

The square root is the nonnegative real square root. All coefficients are fixed
scalars. Find the derivative with respect to $x$ and evaluate it at $x=4$.

### D1-003 — Letters that stay fixed

**Objects and dependencies.** $x\in\mathbb R$ is the independent scalar variable.
$a,b\in\mathbb R$ are fixed scalar parameters. The scalar output is

$$
f(x;a,b)=ax^2+bx+4.
$$

Differentiate with respect to $x$, holding $a$ and $b$ fixed. Then evaluate the
derivative at $x=3$ with parameter values $a=2$ and $b=-1$.

### D1-004 — Simplification with a missing input

**Objects and dependencies.** $x$ is an independent real scalar with $x\ne3$.
The scalar function is

$$
f(x)=\frac{x^2-9}{x-3}.
$$

Find its derivative on its domain. A student cancels a factor and concludes that
this original function has derivative $1$ at $x=3$ too. Explain whether that
conclusion follows.

### D1-005 — Build a derivative from its definition

**Objects and dependencies.** $x\in\mathbb R$ is the independent scalar variable.
The scalar function is $f(x)=x^2+2x$. Use the limit definition to calculate its
derivative, without using the power rule as the derivation. Then evaluate the
derivative at $x=-1$.

During the calculation, $h\in\mathbb R$ is a nonzero scalar increment that tends
to zero; it is not a new input of $f$.

### D1-006 — Choose a method for a rational expression

**Objects and dependencies.** $x$ is an independent real scalar with $x\ne0$.
The scalar function is

$$
f(x)=\frac{2x^3-3x+4}{x}.
$$

Find the scalar-valued derivative and the scalar slope at $x=2$.
Choose and explain your method before calculating.

## Hint ladders

### D1-001

1. Identify the four terms and keep the signs attached to them.
2. The fixed coefficients can be taken outside their derivative operators; the constant term has derivative zero.
3. Differentiate $x^3$, $x^2$, and $x$ separately, then multiply their coefficients and simplify their exponents.

### D1-002

1. Rewrite both the root and the reciprocal as powers of the same independent variable.
2. On $x>0$, use $\sqrt{x}=x^{1/2}$ and $1/x^2=x^{-2}$.
3. The derivative of the negative reciprocal term has a positive coefficient because $(-3)(-2)=6$. Evaluate at $x=4$ after differentiating.

### D1-003

1. The symbols $a$ and $b$ are fixed with respect to $x$; they are not functions $a(x)$ and $b(x)$.
2. Treat $a$ just as you would treat the coefficient $4$ in D1-001; treat $b$ just as you would treat $7$.
3. Obtain the derivative with its parameters visible, then substitute $x=3$, $a=2$, and $b=-1$.

### D1-004

1. Can the numerator be factored using a difference-of-squares identity?
2. Write $x^2-9=(x-3)(x+3)$. Cancellation is allowed only when $x-3\ne0$.
3. The simplified formula describes the original function only on $x\ne3$. A formula that fills in the missing value defines a different function.

### D1-005

1. Write $f(x+h)$ using the same function definition, replacing every input $x$ by $x+h$.
2. Expand the square, then subtract all of $f(x)$ inside parentheses.
3. Factor a single $h$ from the numerator, divide for $h\ne0$, and only then take the limit.

### D1-006

1. Inspect the denominator: it is a single power of the independent variable.
2. Divide each numerator term by $x$ separately while preserving the condition $x\ne0$.
3. The resulting expression is a sum of powers. Calculate the derivative, then evaluate its value at $x=2$.

## Complete solutions

### D1-001

**Step 1 — SETUP.** $x\in\mathbb R$ is independent and scalar; $f(x)=4x^3-5x^2+7x-9$
is scalar. The coefficients do not vary with $x$. A polynomial is differentiable
at every real input.

**Step 2 — CHOICE.** This is a sum of constant multiples of powers of $x$.
Use sum, difference, constant-multiple, power, and constant rules.

**Step 3 — CALCULUS: separate the terms.**

$$
\begin{aligned}
\frac{d}{dx}\left(f(x)\right)
&=\frac{d}{dx}\left(4x^3-5x^2+7x-9\right)\\
&=4\frac{d}{dx}\left(x^3\right)
-5\frac{d}{dx}\left(x^2\right)
+7\frac{d}{dx}\left(x\right)
-\frac{d}{dx}\left(9\right)\\
&=4(3x^{3-1})-5(2x^{2-1})+7(1)-0.
\end{aligned}
$$

**Step 4 — ALGEBRA: simplify exponents and coefficients.**

$$
\begin{aligned}
3-1&=2,\qquad 2-1=1,\\
4(3x^2)-5(2x)+7(1)-0
&=(4\cdot3)x^2-(5\cdot2)x+7\\
&=12x^2-10x+7.
\end{aligned}
$$

**Result.**

$$
\boxed{\frac{d}{dx}\left(f(x)\right)=12x^2-10x+7,
\qquad x\in\mathbb R.}
$$

**Step 5 — CHECK: compare at one input with the definition.** At $x=0$, the
formula gives $12(0)^2-10(0)+7=7$. For a nonzero scalar increment $h$,
$f(h)=4h^3-5h^2+7h-9$ and $f(0)=-9$.

**Step 6 — ALGEBRA: form the check's difference quotient.**

$$
\begin{aligned}
\frac{f(h)-f(0)}{h}
&=\frac{4h^3-5h^2+7h-9-(-9)}{h}\\
&=\frac{4h^3-5h^2+7h}{h}\\
&=\frac{h(4h^2-5h+7)}{h}\\
&=4h^2-5h+7,\qquad h\ne0.
\end{aligned}
$$

**Step 7 — CHECK: take the limit.** As $h\to0$, the expression tends to $7$,
matching the derivative at zero. This checks one input; it is not an independent
proof of the formula at every input.

**Recognition cue.** Separate a sum term by term, but keep the signs. A fixed
coefficient stays as a multiplier; a standalone constant contributes zero.

### D1-002

**Step 1 — SETUP.** $x>0$ is the independent real scalar.
$f(x)=5\sqrt{x}-3/x^2+2$ is scalar, with fixed coefficients. The positive domain
both defines the root smoothly and excludes division by zero.

**Step 2 — CHOICE.** Rewriting the root and reciprocal as powers makes the power
rule available for both changing terms.

**Step 3 — ALGEBRA: rewrite the function on its domain.**

$$
\sqrt{x}=x^{1/2},\qquad \frac{1}{x^2}=x^{-2},\qquad
f(x)=5x^{1/2}-3x^{-2}+2,\qquad x>0.
$$

**Step 4 — CALCULUS: apply the rules before simplifying.**

$$
\begin{aligned}
\frac{d}{dx}\left(f(x)\right)
&=5\frac{d}{dx}\left(x^{1/2}\right)
-3\frac{d}{dx}\left(x^{-2}\right)
+\frac{d}{dx}\left(2\right)\\
&=5\left(\frac12 x^{1/2-1}\right)
-3\left((-2)x^{-2-1}\right)+0.
\end{aligned}
$$

**Step 5 — ALGEBRA: handle the signs and powers.**

$$
\begin{aligned}
\frac12-1&=\frac12-\frac22=-\frac12,\\
-2-1&=-3,\qquad (-3)(-2)=6,\\
5\left(\frac12 x^{-1/2}\right)-3\left((-2)x^{-3}\right)+0
&=\frac52 x^{-1/2}+6x^{-3}\\
&=\frac{5}{2\sqrt{x}}+\frac{6}{x^3}.
\end{aligned}
$$

**Step 6 — CALCULUS: evaluate the already calculated derivative.**

$$
\left.\frac{d}{dx}\left(f(x)\right)\right|_{x=4}
=\frac{5}{2\sqrt{4}}+\frac{6}{4^3}.
$$

**Step 7 — ALGEBRA: combine the fractions.**

$$
\begin{aligned}
\sqrt4&=2,\qquad 4^3=4\cdot4\cdot4=64,\\
\frac{5}{2(2)}+\frac6{64}
&=\frac54+\frac3{32}\\
&=\frac{5\cdot8}{4\cdot8}+\frac3{32}\\
&=\frac{40+3}{32}=\frac{43}{32}.
\end{aligned}
$$

**Result.** The derivative is $5/(2\sqrt{x})+6/x^3$ for $x>0$, and its value at
$x=4$ is the scalar number $43/32$.

**Step 8 — CHECK: sign and domain.** Both derivative terms are positive for
$x>0$. This agrees with the behavior of the original terms: $5\sqrt{x}$ increases,
and $-3/x^2$ becomes less negative as $x$ increases. The derivative formula also
retains the restriction $x>0$. This sign check catches a likely sign mistake; it
does not establish the exact magnitude by itself.

**Recognition cue.** Convert roots and reciprocal powers before calculating.
Subtracting a term whose power-rule coefficient is negative produces a positive
term; write the multiplication to see why.

### D1-003

**Step 1 — SETUP.** $x\in\mathbb R$ is the independent scalar.
$a,b\in\mathbb R$ are fixed scalar parameters. The output $f(x;a,b)=ax^2+bx+4$
is scalar. Its derivative with respect to $x$ is taken with both parameters fixed.

**Step 2 — CHOICE.** Apply the same constant-multiple rules as for numerical
coefficients. A parameter's value is not required to perform this derivative.

**Step 3 — CALCULUS.** Holding $a$ and $b$ fixed,

$$
\begin{aligned}
\frac{d}{dx}\left(f(x;a,b)\right)
&=a\frac{d}{dx}\left(x^2\right)
+b\frac{d}{dx}\left(x\right)
+\frac{d}{dx}\left(4\right)\\
&=a(2x)+b(1)+0.
\end{aligned}
$$

**Step 4 — ALGEBRA.**

$$
a(2x)+b(1)+0=2ax+b.
$$

**Step 5 — CALCULUS: substitute the input and parameter values.**

$$
\left.\frac{d}{dx}\left(f(x;a,b)\right)
\right|_{x=3,\,a=2,\,b=-1}
=2(2)(3)+(-1).
$$

**Step 6 — ALGEBRA.**

$$
2(2)(3)+(-1)=4\cdot3-1=12-1=11.
$$

**Result.** The derivative is $2ax+b$, with $a,b$ fixed, for all real $x$.
The requested evaluated slope is the scalar number $11$.

**Step 7 — CHECK: differentiate after fixing the same parameters.** First define
the scalar function $g(x)=f(x;2,-1)=2x^2-x+4$. Its derivative is

$$
\frac{d}{dx}\left(g(x)\right)=2(2x)-1+0=4x-1.
$$

The coefficient simplification is **ALGEBRA**. At $x=3$, $4(3)-1=12-1=11$,
matching the parameterized calculation. This consistency check applies because
the parameters really are fixed. If $a$ were replaced by a function $a(x)$, the
dependencies and required rules would change.

**Recognition cue.** “Constant” is a relationship to the variable of
differentiation, not a requirement that the symbol be a numeral.

### D1-004

**Step 1 — SETUP.** $x\ne3$ is the independent real scalar and
$f(x)=(x^2-9)/(x-3)$ is scalar. The original definition excludes $x=3$.

**Step 2 — CHOICE.** Factor before choosing a quotient rule. The numerator has
a difference-of-squares form.

**Step 3 — TRICK: difference of squares.** Use the identity in
[T-005](TRICKS_APPENDIX.md#t-005-rationalization). For scalar expressions $r,s$,

$$
r^2-s^2=(r-s)(r+s).
$$

With $r=x$ and $s=3$,

$$
x^2-9=x^2-3^2=(x-3)(x+3).
$$

**Step 4 — ALGEBRA: cancel only on the original domain.**

$$
\begin{aligned}
f(x)&=\frac{(x-3)(x+3)}{x-3}\\
&=\frac{x-3}{x-3}(x+3)\\
&=1(x+3)=x+3,\qquad x\ne3.
\end{aligned}
$$

**Step 5 — CALCULUS: differentiate the equivalent local formula.** At each
allowed input $x\ne3$, the function agrees with $x+3$ in a neighborhood:

$$
\frac{d}{dx}\left(f(x)\right)
=\frac{d}{dx}\left(x+3\right)
=\frac{d}{dx}\left(x\right)+\frac{d}{dx}\left(3\right)
=1+0=1.
$$

The last addition is **ALGEBRA**.

**Result.** The derivative is $1$ for $x\ne3$. The original function has no
derivative at $x=3$ because it has no value there. Defining a new scalar function
$\widetilde f(x)=x+3$ for every real $x$ fills that hole; this extension has a
derivative at $3$, but it is a different function with a different domain.

**Step 6 — CHECK: keep the domain in the difference quotient.** For an allowed
input $x\ne3$, take a nonzero scalar increment $h$ small enough that $x+h\ne3$.

**Step 7 — ALGEBRA.**

$$
\frac{f(x+h)-f(x)}{h}
=\frac{(x+h+3)-(x+3)}{h}
=\frac{x+h+3-x-3}{h}
=\frac{h}{h}=1.
$$

**Step 8 — CHECK.** The quotient's limit is $1$ at every allowed input.
This verifies the derivative on the original domain and supplies no derivative
at the excluded input. The student's claim confuses the function with its extension.

**Recognition cue.** Simplification may shorten a formula while leaving a hole
in its domain. Carry the domain alongside the simplified expression.

### D1-005

**Step 1 — SETUP.** $x\in\mathbb R$ is independent, $f(x)=x^2+2x$ is scalar,
and $h\ne0$ is a real scalar increment tending to zero. All inputs $x+h$ are
allowed because the function is defined on all of $\mathbb R$.

**Step 2 — CHOICE.** Use the limit definition. The order is substitution,
expansion, subtraction, division, and then the limit.

**Step 3 — CALCULUS: write the definition with the full function.**

$$
\frac{d}{dx}\left(f(x)\right)
=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
$$

**Step 4 — TRICK: expand the shifted square.** Use
[T-003](TRICKS_APPENDIX.md#t-003-binomial-expansion). The scalar identity
$(r+s)^2=r^2+2rs+s^2$, with $r=x$ and $s=h$, gives

$$
f(x+h)=(x+h)^2+2(x+h)=x^2+2xh+h^2+2x+2h.
$$

The distribution $2(x+h)=2x+2h$ is an **ALGEBRA** step.

**Step 5 — ALGEBRA: subtract the entire original value.**

$$
\begin{aligned}
f(x+h)-f(x)
&=(x^2+2xh+h^2+2x+2h)-(x^2+2x)\\
&=x^2+2xh+h^2+2x+2h-x^2-2x\\
&=(x^2-x^2)+(2x-2x)+2xh+h^2+2h\\
&=2xh+h^2+2h\\
&=h(2x+h+2).
\end{aligned}
$$

**Step 6 — ALGEBRA: divide before letting the increment tend to zero.**

$$
\frac{f(x+h)-f(x)}{h}
=\frac{h(2x+h+2)}{h}
=2x+h+2,\qquad h\ne0.
$$

**Step 7 — CALCULUS: take the limit and then evaluate the derivative.** In the
limit, $x$ stays fixed and $h\to0$:

$$
\frac{d}{dx}\left(f(x)\right)=\lim_{h\to0}(2x+h+2)=2x+2.
$$

$$
\left.\frac{d}{dx}\left(f(x)\right)\right|_{x=-1}=2(-1)+2.
$$

**Step 8 — ALGEBRA.**

$$
2(-1)+2=-2+2=0.
$$

**Result.** The derivative is $2x+2$ for every real $x$; the slope at $x=-1$
is the scalar number $0$. The value $f(-1)=1-2=-1$ is a function value, a
different quantity from its slope.

**Step 9 — CHECK: compare with the power-rule calculation.**

$$
\frac{d}{dx}\left(x^2+2x\right)
=\frac{d}{dx}\left(x^2\right)+2\frac{d}{dx}\left(x\right)
=2x+2(1)=2x+2.
$$

The coefficient simplification is **ALGEBRA**. This agrees with the definition
calculation. Replacing $x$ by $-1$ before differentiating would give the constant
expression $-1$, whose zero derivative would not tell you the general derivative
or justify the slope calculation. Here it would accidentally match the slope.

**Recognition cue.** Subtract the entire old function value in parentheses.
Cancellation of the increment is allowed only while it is nonzero.

### D1-006

**Step 1 — SETUP.** $x\ne0$ is the independent real scalar;
$f(x)=(2x^3-3x+4)/x$ is scalar. The requested slope at $x=2$ is valid because
$2\ne0$. There are no varying parameters.

**Step 2 — CHOICE.** Every numerator term can be divided by the simple
denominator $x$. Rewrite as powers and use sum and power rules. This avoids
introducing an unnecessary quotient-rule calculation.

**Step 3 — ALGEBRA: divide each term without discarding the restriction.**

$$
\begin{aligned}
f(x)&=\frac{2x^3}{x}-\frac{3x}{x}+\frac4x\\
&=2x^{3-1}-3+4x^{-1}\\
&=2x^2-3+4x^{-1},\qquad x\ne0.
\end{aligned}
$$

**Step 4 — CALCULUS: differentiate the rewritten function.**

$$
\begin{aligned}
\frac{d}{dx}\left(f(x)\right)
&=2\frac{d}{dx}\left(x^2\right)
-\frac{d}{dx}\left(3\right)
+4\frac{d}{dx}\left(x^{-1}\right)\\
&=2(2x)-0+4((-1)x^{-1-1}).
\end{aligned}
$$

**Step 5 — ALGEBRA.**

$$
\begin{aligned}
-1-1&=-2,\\
2(2x)-0+4((-1)x^{-2})
&=4x-4x^{-2}=4x-\frac4{x^2}.
\end{aligned}
$$

**Step 6 — CALCULUS: evaluate at the specified input.**

$$
\left.\frac{d}{dx}\left(f(x)\right)\right|_{x=2}
=4(2)-\frac4{2^2}.
$$

**Step 7 — ALGEBRA.**

$$
4(2)-\frac4{2^2}=8-\frac4{4}=8-1=7.
$$

**Result.** The derivative is $4x-4/x^2$ for $x\ne0$, and the slope at $2$
is the scalar number $7$.

**Step 8 — CHECK: verify the slope with a difference quotient.** Declare $h$
as a nonzero scalar increment tending to zero, small enough that $2+h\ne0$.
Using the equivalent formula, $f(2)=2(2)^2-3+4/2=8-3+2=7$.

**Step 9 — TRICK: expand the square at the shifted input.** See
[T-003](TRICKS_APPENDIX.md#t-003-binomial-expansion).

$$
(2+h)^2=2^2+2(2)h+h^2=4+4h+h^2.
$$

**Step 10 — ALGEBRA: form and simplify the quotient.**

$$
\begin{aligned}
f(2+h)&=2(4+4h+h^2)-3+\frac4{2+h}\\
&=8+8h+2h^2-3+\frac4{2+h}\\
&=5+8h+2h^2+\frac4{2+h},\\
f(2+h)-f(2)&=5+8h+2h^2+\frac4{2+h}-7\\
&=8h+2h^2+\frac4{2+h}-2\\
&=8h+2h^2+\frac{4-2(2+h)}{2+h}\\
&=8h+2h^2+\frac{4-4-2h}{2+h}\\
&=8h+2h^2-\frac{2h}{2+h},\\
\frac{f(2+h)-f(2)}h
&=\frac{h(8+2h-2/(2+h))}{h}\\
&=8+2h-\frac2{2+h},\qquad h\ne0.
\end{aligned}
$$

**Step 11 — CHECK: take the limit.**

$$
\lim_{h\to0}\frac{f(2+h)-f(2)}h
=8+0-\frac22=8-1=7.
$$

The last arithmetic is **ALGEBRA**. This independently verifies the requested
slope at $2$, while the differentiation rules supply the general formula.

**Recognition cue.** A rational-looking expression may become a sum of powers.
Inspect the algebra before selecting a differentiation rule.

## What to carry into the next chapter

- A changing inner expression needs its own derivative; see the chain-rule pilot.
- A product of changing factors requires a product rule unless you first expand it validly.
- Fixed parameters remain fixed only when the setup says so.
- A simplified formula does not automatically enlarge the original domain.
- A check at one input verifies that input, not every value of the derivative.

The next chapter will develop product, quotient, and chain-rule choices using
these same declarations and visible algebra steps.
