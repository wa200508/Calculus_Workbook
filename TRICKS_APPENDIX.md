# Tricks and identities

Alpha reference appendix. These are supporting identities, algebraic rewrites,
and approximation tools to consult while working through problems. Main calculus
methods such as substitution, integration by parts, and differentiation rules
belong in the main chapters.

**Purple means a supporting trick.** The label TRICK remains visible in grayscale.
The main chapters use dark blue for algebra, black for calculus rules, and purple
when invoking a supporting tool from this appendix.

## Find a useful tool

| Tool | When to consider it | What it gives |
|---|---|---|
| [T-001 Euler identities](#t-001-euler-identities) | Trigonometric products or oscillations | Exact conversions between complex exponentials and real trigonometric functions |
| [T-002 Taylor expansions](#t-002-taylor-expansions) | A local approximation near a known input | A polynomial plus an error term; an infinite identity only when convergence is justified |
| [T-003 Binomial expansion](#t-003-binomial-expansion) | Powers of a sum | A finite exact expansion for nonnegative integer powers |
| [T-004 Completing the square](#t-004-completing-the-square) | A quadratic is hard to interpret or manipulate | An exact shifted-square form |
| [T-005 Rationalization](#t-005-rationalization) | A difference of roots causes cancellation | An exact equivalent expression on a stated domain |
| [T-006 Logarithm identities](#t-006-logarithm-identities) | Products, quotients, and powers inside a logarithm | Exact sums and differences under real positivity assumptions |

## T-001 Euler identities

**Objects and conditions.** $\theta\in\mathbb R$ is an independent real scalar
angle, measured in radians. $\mathrm i$ is the fixed imaginary scalar with
$\mathrm i^2=-1$. A complex scalar $z=a+\mathrm i b$ has real scalar parts $a,b$;
$\operatorname{Re}(z)=a$ and $\operatorname{Im}(z)=b$.
The complex exponential $\exp(z)$ is a scalar-valued function of a complex scalar
input. Sine and cosine of real angles are real scalars.
The usual notation $e^z$ means the same function as $\exp(z)$, where
$e=\exp(1)$ is the fixed real Euler constant. We use $\exp(z)$ here to keep the
input visible.

**TRICK — exact identities.**

$$
\exp(\mathrm i\theta)=\cos(\theta)+\mathrm i\sin(\theta),
\qquad
\exp(-\mathrm i\theta)=\cos(\theta)-\mathrm i\sin(\theta).
$$

Adding and subtracting these equations gives

$$
\cos(\theta)=\frac{\exp(\mathrm i\theta)+\exp(-\mathrm i\theta)}{2},
\qquad
\sin(\theta)=\frac{\exp(\mathrm i\theta)-\exp(-\mathrm i\theta)}{2\mathrm i}.
$$

At $\theta=\pi$, where $\pi$ is the fixed real circle constant,
$\cos(\pi)=-1$ and $\sin(\pi)=0$, so $\exp(\mathrm i\pi)+1=0$.
These formulas are recorded in [NIST DLMF §4.2](https://dlmf.nist.gov/4.2).

### Worked use: derive double-angle identities

**Step 1 — SETUP.** The same real scalar $\theta$ supplies every angle below.
All expressions containing $\mathrm i$ are complex scalars.

**Step 2 — TRICK: use the exponential addition identity.** The complex
exponential satisfies $\exp(z+w)=\exp(z)\exp(w)$ for complex scalar inputs $z,w$.
With $z=w=\mathrm i\theta$,

$$
\exp(2\mathrm i\theta)
=\exp(\mathrm i\theta)\exp(\mathrm i\theta)
=\left(\cos(\theta)+\mathrm i\sin(\theta)\right)^2.
$$

**Step 3 — ALGEBRA: expand and use the imaginary unit's square.**

$$
\begin{aligned}
\left(\cos(\theta)+\mathrm i\sin(\theta)\right)^2
&=(\cos(\theta))^2
+2\mathrm i\cos(\theta)\sin(\theta)
+\mathrm i^2(\sin(\theta))^2\\
&=(\cos(\theta))^2-(\sin(\theta))^2
+\mathrm i\left(2\cos(\theta)\sin(\theta)\right).
\end{aligned}
$$

**Step 4 — TRICK: compare the real and imaginary parts.** Euler's formula also
gives $\exp(2\mathrm i\theta)=\cos(2\theta)+\mathrm i\sin(2\theta)$.
Equal complex numbers have equal real parts and equal imaginary parts:

$$
\cos(2\theta)=(\cos(\theta))^2-(\sin(\theta))^2,
\qquad
\sin(2\theta)=2\cos(\theta)\sin(\theta).
$$

**Step 5 — CHECK.** At $\theta=0$, the cosine formula gives $1=1-0$ and the
sine formula gives $0=2(1)(0)$. This checks one angle. The preceding exact
identities establish the general result.

**When it helps.** Converting trigonometric expressions into exponentials can
make angle combinations easier to manipulate. Track real and imaginary parts
explicitly when returning to a real-valued problem.

## T-002 Taylor expansions

**Objects and conditions.** $x$ is an independent real scalar and $a$ is a fixed
real expansion center. $f(x)$ is a real scalar-valued function. $N$ is a fixed
nonnegative integer polynomial degree. $k$ is an integer summation index;
$t$ is an auxiliary real scalar input used when writing derivatives before
evaluation. Both $f(t)$ and $f(x)$ are values of the same function at their
displayed inputs. The factorial is $k!=1\cdot2\cdots k$ for $k\ge1$, with $0!=1$.

**TRICK — Taylor polynomial.** Define the fixed scalar coefficients by

$$
c_0=f(a),\qquad
c_k=\frac1{k!}\left.\frac{d^k}{dt^k}\left(f(t)\right)\right|_{t=a},
\qquad 1\leq k\leq N.
$$

Then the scalar polynomial is

$$
P_N(x;a)=\sum_{k=0}^{N}c_k(x-a)^k.
$$

For $N=3$, the full expression is

$$
\begin{aligned}
P_3(x;a)={}&f(a)
+\left.\frac{d}{dt}\left(f(t)\right)\right|_{t=a}(x-a)\\
&+\frac1{2!}\left.\frac{d^2}{dt^2}\left(f(t)\right)\right|_{t=a}(x-a)^2\\
&+\frac1{3!}\left.\frac{d^3}{dt^3}\left(f(t)\right)\right|_{t=a}(x-a)^3.
\end{aligned}
$$

A Maclaurin expansion is the special case $a=0$. The superscript on a derivative
counts repeated differentiation; it does not square or cube the derivative.

### The error is part of the tool

If $f$ has continuous derivatives through order $N+1$ on an interval containing
$a$ and $x$, Taylor's theorem gives a scalar remainder $R_N(x;a)$:

$$
f(x)=P_N(x;a)+R_N(x;a),
$$

$$
R_N(x;a)=\frac1{(N+1)!}
\left.\frac{d^{N+1}}{dt^{N+1}}\left(f(t)\right)\right|_{t=\xi}
(x-a)^{N+1},
$$

for some real scalar $\xi$ between $a$ and $x$ when they differ. If a fixed
nonnegative real scalar $M$ bounds the absolute value of that derivative
throughout the intervening interval, then

$$
|R_N(x;a)|\leq\frac{M|x-a|^{N+1}}{(N+1)!}.
$$

An infinite Taylor series equals $f(x)$ only where the remainder tends to zero
as $N$ increases. Smoothness alone does not guarantee that equality. Keep a
finite approximation marked $\approx$ unless the remainder is included.
See [OpenStax, Calculus Volume 2, §6.3](https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series).

### Common infinite expansions and their valid inputs

Here $x$ is an independent real scalar, and $k$ is an integer summation index.
Each displayed function has a real scalar output. For every real $x$,

$$
\begin{aligned}
\exp(x)&=\sum_{k=0}^{\infty}\frac{x^k}{k!}
=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots,\\
\sin(x)&=\sum_{k=0}^{\infty}\frac{(-1)^k x^{2k+1}}{(2k+1)!}
=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots,\\
\cos(x)&=\sum_{k=0}^{\infty}\frac{(-1)^k x^{2k}}{(2k)!}
=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots.
\end{aligned}
$$

The sine and cosine inputs are angles in radians. The summation formulas
specify every term; the trailing dots only illustrate their pattern. These
series converge to their displayed functions at every real input. Keeping
only finitely many terms requires an approximation sign and an error bound.

The geometric expansion has a narrower range of valid inputs:

$$
\frac{1}{1-x}=\sum_{k=0}^{\infty}x^k
=1+x+x^2+x^3+\cdots,\qquad |x|<1.
$$

Although the function $1/(1-x)$ exists at $x=2$, this series does not converge
there. Check the series' convergence range before replacing a function by a
series. See [OpenStax, Calculus Volume 2, §6.4](https://openstax.org/books/calculus-volume-2/pages/6-4-working-with-taylor-series).

### Worked use: approximate a sine with a stated error

**Step 1 — SETUP.** $f(x)=\sin(x)$ is a real scalar function, with real scalar
angle $x$ in radians. Use center $a=0$ and degree $N=4$. The target input is
$x=1/10$ radians. There are no varying parameters.

**Step 2 — CALCULUS: list the derivatives used by the tool.**

$$
\begin{aligned}
f(t)&=\sin(t),\\
\frac{d}{dt}\left(f(t)\right)&=\cos(t),\\
\frac{d^2}{dt^2}\left(f(t)\right)&=-\sin(t),\\
\frac{d^3}{dt^3}\left(f(t)\right)&=-\cos(t),\\
\frac{d^4}{dt^4}\left(f(t)\right)&=\sin(t),\\
\frac{d^5}{dt^5}\left(f(t)\right)&=\cos(t).
\end{aligned}
$$

At $t=0$, the value and first four derivatives are respectively $0,1,0,-1,0$.
These trigonometric derivative rules are developed in the main calculus material;
here their values supply the expansion coefficients.

**Step 3 — ALGEBRA: build the polynomial and remove zero terms.**

$$
\begin{aligned}
P_4(x;0)
&=0+1(x-0)+\frac0{2!}(x-0)^2
+\frac{-1}{3!}(x-0)^3+\frac0{4!}(x-0)^4\\
&=x-\frac{x^3}{1\cdot2\cdot3}
=x-\frac{x^3}{6}.
\end{aligned}
$$

Although this polynomial's highest nonzero power is three, it is also the
fourth-order Taylor polynomial because its fourth-order coefficient is zero.

**Step 4 — APPROXIMATION: retain the fifth-derivative error bound.** Since
$|\cos(t)|\leq1$ for real $t$, choose the fixed scalar bound $M=1$:

$$
\sin(x)=x-\frac{x^3}{6}+R_4(x;0),
\qquad |R_4(x;0)|\leq\frac{|x|^5}{5!}.
$$

**Step 5 — ALGEBRA: evaluate the polynomial exactly.**

$$
\begin{aligned}
P_4(1/10;0)
&=\frac1{10}-\frac{(1/10)^3}{6}\\
&=\frac1{10}-\frac1{1000\cdot6}\\
&=\frac{600}{6000}-\frac1{6000}
=\frac{599}{6000}.
\end{aligned}
$$

**Step 6 — APPROXIMATION: report the result with its bound.**

$$
\sin(1/10)\approx\frac{599}{6000},
\qquad
\left|\sin(1/10)-\frac{599}{6000}\right|
\leq\frac1{10^5\cdot120}
=\frac1{12\,000\,000}.
$$

This rational bound applies to the exact rational approximation shown. If you
round it to a decimal, include the additional rounding error in the reported bound.

**Step 7 — CHECK.** The correction $x^3/6$ is positive at $x=1/10$, so the
polynomial estimate is slightly smaller than $x$. Also, both the polynomial and
the actual sine are zero at the expansion center. These plausibility checks
supplement the theorem's error bound.

**When it helps.** Expand around an input where function values and derivatives
are simple. A polynomial without an error discussion is an incomplete numerical
approximation.

## T-003 Binomial expansion

**Objects and conditions.** $r,s$ are real or complex scalar expressions.
$n$ is a fixed nonnegative integer, and $k$ is an integer index from zero to $n$.
The binomial coefficient is the scalar integer

$$
\binom nk=\frac{n!}{k!(n-k)!}.
$$

**TRICK — exact finite identity.**

$$
(r+s)^n=\sum_{k=0}^n\binom nk r^{n-k}s^k.
$$

For a zero power, the corresponding factor is $1$; the endpoint terms are
$r^n$ and $s^n$. This is a finite polynomial identity. A fractional exponent
requires a different, generally infinite expansion with convergence conditions.

### Worked use: expand a shifted cubic

**Step 1 — SETUP.** $x$ is an independent real scalar. $h$ is a real scalar
increment. Here take $r=x$, $s=h$, and $n=3$.

**Step 2 — ALGEBRA: calculate the coefficients.**

$$
\begin{aligned}
\binom30&=\frac{3!}{0!3!}=1,\\
\binom31&=\frac{3!}{1!2!}=\frac{6}{1\cdot2}=3,\\
\binom32&=\frac{3!}{2!1!}=\frac{6}{2\cdot1}=3,\\
\binom33&=\frac{3!}{3!0!}=1.
\end{aligned}
$$

**Step 3 — TRICK: write every term.**

$$
\begin{aligned}
(x+h)^3
&=1(x^3)+3(x^2h)+3(xh^2)+1(h^3)\\
&=x^3+3x^2h+3xh^2+h^3.
\end{aligned}
$$

**Step 4 — CHECK.** At $h=0$ the expression reduces to $x^3$; at $x=0$ it
reduces to $h^3$. These checks do not replace the binomial identity but can expose
a missing endpoint term. For a square, the same tool gives
$(x+h)^2=x^2+2xh+h^2$.

**When it helps.** Shifted inputs occur in derivative definitions and series
calculations. The coefficients prevent expansion errors without hiding terms.

## T-004 Completing the square

**Objects and conditions.** $x$ is an independent real scalar; $a,b,c$ are fixed
real scalar coefficients, with $a\ne0$. The scalar expression is $ax^2+bx+c$.

**TRICK — exact identity.**

$$
ax^2+bx+c=a\left(x+\frac{b}{2a}\right)^2+c-\frac{b^2}{4a}.
$$

### Worked use: expose a quadratic's shape

**Step 1 — SETUP.** Let the real scalar function be $q(x)=2x^2-8x+11$ for all
real $x$. The coefficients $2,-8,11$ are fixed.

**Step 2 — ALGEBRA: factor the quadratic coefficient.**

$$
q(x)=2(x^2-4x)+11.
$$

**Step 3 — TRICK: add and subtract the missing square.** Since
$(x-2)^2=x^2-4x+4$,

$$
x^2-4x=(x-2)^2-4.
$$

**Step 4 — ALGEBRA: substitute and simplify.**

$$
\begin{aligned}
q(x)&=2\left((x-2)^2-4\right)+11\\
&=2(x-2)^2-8+11\\
&=2(x-2)^2+3.
\end{aligned}
$$

**Step 5 — CHECK: expand back.**

$$
2(x-2)^2+3=2(x^2-4x+4)+3
=2x^2-8x+8+3=2x^2-8x+11.
$$

The square is nonnegative, so $q(x)\geq3$, with equality at $x=2$. The exact
rewrite exposes that feature without requiring an optimization calculation.

**When it helps.** A shifted-square denominator or root may reveal the right
identity, domain, or later integration method. The rewrite itself does not choose
the calculus method for you.

## T-005 Rationalization

**Objects and conditions.** If $r,s$ are real scalar expressions, the exact
difference-of-squares identity is

$$
(r-s)(r+s)=r^2-s^2.
$$

The factor $r+s$ is often called the conjugate of $r-s$ in this real-root
algebra context. Multiplying a fraction by $(r+s)/(r+s)$ preserves it only when
$r+s\ne0$.

### Worked use: remove a root difference

**Step 1 — SETUP.** $x$ is an independent real scalar with $x>-1$ and $x\ne0$.
Define the real scalar function

$$
f(x)=\frac{\sqrt{1+x}-1}{x}.
$$

The square root is the nonnegative real root. On this domain,
$\sqrt{1+x}+1>0$, so the conjugate multiplier is not zero.

**Step 2 — TRICK: multiply by one in a useful form.**

$$
f(x)=\frac{\sqrt{1+x}-1}{x}
\frac{\sqrt{1+x}+1}{\sqrt{1+x}+1}.
$$

**Step 3 — ALGEBRA: multiply the numerators and cancel on the allowed domain.**

$$
\begin{aligned}
f(x)&=\frac{(\sqrt{1+x}-1)(\sqrt{1+x}+1)}{x(\sqrt{1+x}+1)}\\
&=\frac{(\sqrt{1+x})^2-1^2}{x(\sqrt{1+x}+1)}\\
&=\frac{1+x-1}{x(\sqrt{1+x}+1)}\\
&=\frac{x}{x(\sqrt{1+x}+1)}\\
&=\frac1{\sqrt{1+x}+1},\qquad x>-1,\quad x\ne0.
\end{aligned}
$$

**Step 4 — CHECK.** At the allowed input $x=3$, the original expression gives
$(\sqrt4-1)/3=(2-1)/3=1/3$; the rewritten expression gives $1/(\sqrt4+1)=1/3$.
The original function remains undefined at $x=0$. The rewritten expression has
a value there and supplies a continuous extension, not a new value of the original
function. See D1-004 for the same domain distinction.

**When it helps.** A root difference may be hard to simplify or numerically
evaluate near cancellation. Rationalization preserves exact equality where its
divisions are allowed. It can prepare an expression for a limit calculation.

## T-006 Logarithm identities

**Objects and conditions.** $r,s$ are positive real scalar expressions and $p$
is a fixed real scalar exponent. The natural logarithm $\ln(r)$ is real. On
these real domains,

$$
\ln(rs)=\ln(r)+\ln(s),\qquad
\ln\left(\frac r s\right)=\ln(r)-\ln(s),\qquad
\ln(r^p)=p\ln(r).
$$

These identities need positivity in this real formulation. Complex logarithms
require branch choices and do not permit these unrestricted rewrites. See the
exponential and logarithm definitions in [NIST DLMF §4.2](https://dlmf.nist.gov/4.2).

### Worked use: expose a product and power inside a logarithm

**Step 1 — SETUP.** $x>0$ is an independent real scalar. The real scalar
function is

$$
q(x)=\ln\left(\frac{(x^2+1)^3}{x^2}\right).
$$

On this domain, $x^2+1>0$ and $x^2>0$, so both logarithms introduced below
have positive arguments.

**Step 2 — TRICK: separate the quotient.**

$$
q(x)=\ln\left((x^2+1)^3\right)-\ln(x^2).
$$

**Step 3 — TRICK: move the fixed powers outside.**

$$
q(x)=3\ln(x^2+1)-2\ln(x),\qquad x>0.
$$

**Step 4 — CHECK.** At $x=1$, the original expression is
$\ln((1+1)^3/1)=\ln(8)$. The new expression is $3\ln(2)-2\ln(1)=3\ln(2)$,
which equals $\ln(8)$ by the power identity, with $\ln(1)=0$.

**When it helps.** Revealing sums and fixed multipliers can organize a later
derivative calculation. This algebraic rewrite does not eliminate the dependence
of $x^2+1$ on $x$.

For a version declared on $x\ne0$, including negative inputs, the last expression
would instead be $3\ln(x^2+1)-2\ln(|x|)$. The absolute value keeps the real
logarithm's input positive; the expression $\ln(x)$ must not be carried into a
negative-input domain.

## Use a trick deliberately

Identify the structure it matches, check its domain, show the exact replacement,
and then return to the calculus problem. Keep an error term or error bound when
using an approximation. If a trick makes the expression longer or obscures its
dependencies, keep the original form and choose another approach.
