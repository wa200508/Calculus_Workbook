# D1 · Scalar reference exercises

## Problems

### D1-001 — Polynomial differentiation by linearity

**Objects and dependencies.** $x\in\mathbb R$ is the independent scalar variable.
The scalar function is $f(x)=4x^3-5x^2+7x-9$, defined for every real $x$.
All coefficients are fixed real scalars. Find the scalar-valued function

$$
\frac{d}{dx}\left(f(x)\right).
$$

### D1-002 — Radicals and negative powers

**Objects and dependencies.** $x$ is an independent real scalar with $x>0$.
The scalar function is

$$
f(x)=5\sqrt{x}-\frac{3}{x^2}+2.
$$

The square root is the nonnegative real square root. All coefficients are fixed
scalars. Find the derivative with respect to $x$ and evaluate it at $x=4$.

### D1-003 — Differentiation with fixed parameters

**Objects and dependencies.** $x\in\mathbb R$ is the independent scalar variable.
$a,b\in\mathbb R$ are fixed scalar parameters. The scalar output is

$$
f(x;a,b)=ax^2+bx+4.
$$

Differentiate with respect to $x$, holding $a$ and $b$ fixed. Then evaluate the
derivative at $x=3$ with parameter values $a=2$ and $b=-1$.

### D1-004 — Cancellation and a removable singularity

**Objects and dependencies.** $x$ is an independent real scalar with $x\ne3$.
The scalar function is

$$
f(x)=\frac{x^2-9}{x-3}.
$$

Find its derivative on its domain. A student cancels a factor and concludes that
this original function has derivative $1$ at $x=3$ too. Explain whether that
conclusion follows.

### D1-005 — Difference-quotient derivation

**Objects and dependencies.** $x\in\mathbb R$ is the independent scalar variable.
The scalar function is $f(x)=x^2+2x$. Use the limit definition to calculate its
derivative, without using the power rule as the derivation. Then evaluate the
derivative at $x=-1$.

During the calculation, $h\in\mathbb R$ is a nonzero scalar increment that tends
to zero; it is not a new input of $f$.

### D1-006 — Algebraic reduction before differentiation

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
2. The constant-multiple rule applies to the fixed parameters $a,b$ in the same way as to numerical coefficients.
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
Linearity and the power rule apply directly; no product or chain-rule decomposition is required.

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

**Discussion.** Linearity preserves each signed coefficient.
Constants and constant multiples are distinguished before rule application.

### D1-002

**Step 1 — SETUP.** $x>0$ is the independent real scalar.
$f(x)=5\sqrt{x}-3/x^2+2$ is scalar, with fixed coefficients. The positive domain
both defines the root smoothly and excludes division by zero.

**Step 2 — CHOICE.** Rewriting the root and reciprocal as powers makes the power
rule applicable to both nonconstant terms.

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

**Discussion.** A power representation unifies the radical and reciprocal terms.
Subtracting a term whose power-rule coefficient is negative produces a positive
term; write the multiplication to see why.

### D1-003

**Step 1 — SETUP.** $x\in\mathbb R$ is the independent scalar.
$a,b\in\mathbb R$ are fixed scalar parameters. The output $f(x;a,b)=ax^2+bx+4$
is scalar. Its derivative with respect to $x$ is taken with both parameters fixed.

**Step 2 — CHOICE.** The constant-multiple rule applies because $a,b$ are independent of $x$.
Symbolic parameter values can be retained throughout the differentiation.

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

**Discussion.** “Constant” is a relationship to the variable of
differentiation, not a requirement that the symbol be a numeral.

### D1-004

**Step 1 — SETUP.** $x\ne3$ is the independent real scalar and
$f(x)=(x^2-9)/(x-3)$ is scalar. The original definition excludes $x=3$.

**Step 2 — CHOICE.** The difference-of-squares factorization permits cancellation on the stated
domain, reducing the derivative calculation to a linear function.

**Step 3 — TRICK: difference of squares.** For scalar expressions $r,s$,
the identity from [T-005](TRICKS_APPENDIX.md#t-005-rationalization) is

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
$\widetilde f(x)=x+3$ for every real $x$ defines a continuous extension at the excluded point. This extension has a
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

**Step 8 — CHECK AND DOMAIN.** The quotient's limit is $1$ at every allowed input.
This verifies the derivative on the original domain and supplies no derivative
at the excluded input. The student's claim confuses the function with its extension.

**Discussion.** Cancellation preserves the excluded point in the original domain.
The reduced expression and its continuous extension represent different functions.

### D1-005

**Step 1 — SETUP.** $x\in\mathbb R$ is independent, $f(x)=x^2+2x$ is scalar,
and $h\ne0$ is a real scalar increment tending to zero. All inputs $x+h$ are
allowed because the function is defined on all of $\mathbb R$.

**Step 2 — CHOICE.** The difference quotient is reduced algebraically for nonzero increments
before its limit is taken. This ordering prevents division by zero.

**Step 3 — CALCULUS: write the definition with the full function.**

$$
\frac{d}{dx}\left(f(x)\right)
=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
$$

**Step 4 — TRICK: the shifted square.** The expansion is
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
expression $-1$, whose zero derivative does not determine the derivative function
or justify evaluation of its slope. The agreement at this particular input is coincidental and does not validate
that order of operations.

**Discussion.** Parentheses preserve the subtraction of the complete
reference value in the difference quotient. Increment cancellation is valid
only before the limiting operation, while the increment is nonzero.

### D1-006

**Step 1 — SETUP.** $x\ne0$ is the independent real scalar;
$f(x)=(2x^3-3x+4)/x$ is scalar. The requested slope at $x=2$ is valid because
$2\ne0$. There are no varying parameters.

**Step 2 — CHOICE.** The monomial denominator permits termwise division on $x\ne0$.
The reduced sum of powers can be differentiated by linearity, avoiding a
quotient-rule expansion while retaining the original exclusion.

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

**Discussion.** Algebraic reduction can expose a sum of powers inside a rational
expression. Rule selection follows the reduced structure and its preserved domain.

