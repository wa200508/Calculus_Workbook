# Analytical audit of the reference exercises

Reviewed November 5, 2026 by Codex agent `audit_reference_exercises`.
The reviewed baseline is commit
`8963e970e9ec23d4114203b205fccc9b7ca1c85d`. This note covers all 24
problems, their three hints, complete solutions, and checks in
DIFFERENTIATION_SCALARS.md, DIFFERENTIATION_RULES.md,
INTEGRATION_SCALARS.md, and INTEGRATION_SUBSTITUTION.md.

Each result was rederived analytically, including intermediate arithmetic and
the stated domain. No mathematical error was found in these four manuscripts;
no correction to their source text was required. This is an agent analytical
review, not independent human peer review or a reader trial.

## Scalar differentiation: D1

### D1-001 — Polynomial differentiation by linearity

The binomial expansion of the difference quotient at an arbitrary real input is

$$
\frac{f(x+h)-f(x)}h
=12x^2-10x+7+(12x-5)h+4h^2,\qquad h\ne0.
$$

Its limit is $12x^2-10x+7$, independently verifying the rule-based solution at
every real input. The manuscript's special check at zero gives $7$ correctly
and explicitly limits the scope of that check. All hints preserve the signs.

### D1-002 — Radicals and negative powers

For $x>0$, rationalization gives the square-root difference quotient
$1/(\sqrt{x+h}+\sqrt x)$, whose limit is $1/(2\sqrt x)$.
For the reciprocal-square term,

$$
\frac{-3/(x+h)^2+3/x^2}{h}
=\frac{3(2x+h)}{x^2(x+h)^2}\longrightarrow\frac6{x^3}.
$$

Consequently the reported derivative $5/(2\sqrt x)+6/x^3$ is correct.
At $x=4$, $5/4+3/32=43/32$. The positive restriction supplies both a smooth
real square root and a nonzero denominator. No omitted boundary derivative is
claimed.

### D1-003 — Differentiation with fixed parameters

For fixed $a,b$, the difference quotient is $2ax+ah+b$, tending to $2ax+b$.
The evaluated result is $2(2)(3)-1=11$. The distinction between fixed parameters
and functions of $x$ is correct in the statement, hints, and check; every real
input is admissible.

### D1-004 — Cancellation and a removable singularity

Factoring gives $f(x)=x+3$ precisely for $x\ne3$. Every allowed input has a
neighborhood on which this equality holds, and hence derivative $1$.
The quotient at the excluded input cannot be defined without specifying an
extension. The manuscript correctly separates the original function from its
continuous extension and does not erase the domain exclusion.

### D1-005 — Difference-quotient derivation

Expanding gives $f(x+h)-f(x)=h(2x+h+2)$ for every real $x,h$.
Division for $h\ne0$, followed by the limit, gives $2x+2$ and hence slope
zero at $x=-1$. Completing the square, $f(x)=(x+1)^2-1$, independently
confirms the horizontal tangent there. The function value $-1$ is correctly
distinguished from the slope.

### D1-006 — Algebraic reduction before differentiation

The quotient rule supplies the independent calculation

$$
\frac{(6x^2-3)x-(2x^3-3x+4)}{x^2}
=\frac{4x^3-4}{x^2}=4x-\frac4{x^2},\qquad x\ne0.
$$

At $x=2$ the result is $8-1=7$. The manuscript's longer difference quotient
also reduces correctly to $8+2h-2/(2+h)$ at that input. The domain remains
punctured after the algebraic reduction.

## Composition differentiation: D2

### D2-001 — Differentiate a composition

Expanding the original polynomial gives
$81x^8+108x^6+54x^4+12x^2+1$. Its derivative is
$648x^7+648x^5+216x^3+24x$, which factors as
$24x(3x^2+1)^3$. This independently confirms the chain-rule factors and their
order of evaluation. The zero-input binomial check and all-real domain are
correct.

### D2-002 — A polynomial times a sine

For the product difference quotient, add and subtract
$x^2\sin(x+h)$ in the numerator. The two limiting terms are
$2x\sin x$ and $x^2\cos x$, giving the reported derivative on all real
inputs. The evaluated result at $\pi$ is $-\pi^2$.
The angle-addition identity and the limit $\sin h/h\to1$ correctly verify
that special slope, including its sign.

### D2-003 — A quotient with an excluded input

Polynomial division gives $f(x)=x+1+2/(x-1)$ for $x\ne1$.
Differentiation yields $1-2/(x-1)^2$, equivalent to
$(x^2-2x-1)/(x-1)^2$. The evaluated slope at $2$ is $-1$.
Neither numerator cancellation nor a removable singularity at $1$ is possible:
the original numerator there is $2$. The solution and hints preserve the
exclusion.

### D2-004 — An exponential of a quadratic

The derivative of the inner quadratic is $4x$, giving
$4x\exp(2x^2-3)$. The exponential is strictly positive for every real input,
so the derivative is negative below zero, positive above zero, and zero at
zero. This agrees with evenness and the global minimum there. No parameter or
domain qualification is missing.

### D2-005 — Logarithmic composition

The logarithm increment at an arbitrary input can be written

$$
f(x+h)-f(x)
=\ln\left(1+\frac{2xh+h^2}{1+x^2}\right).
$$

Using $\ln(1+u)/u\to1$ gives $2x/(1+x^2)$, including zero by continuity
of that limit expression. The denominator is positive for all real $x$; the
evaluated slope at $1$ is $1$. The warning about logarithms of sums is correct.

### D2-006 — Square-root composition

Rationalizing the increment gives

$$
\frac{\sqrt{1+(x+h)^2}-\sqrt{1+x^2}}h
=\frac{2x+h}{\sqrt{1+(x+h)^2}+\sqrt{1+x^2}},
$$

whose limit is $x/\sqrt{1+x^2}$. This confirms the chain-rule result and the
implicit-relation check on all real inputs. The value at zero is zero.

### D2-007 — Nested trigonometric composition

The identity $\sin^3 u=(3\sin u-\sin(3u))/4$ gives an independent
representation. Differentiating it at $u=2x$ yields
$(3/2)(\cos(2x)-\cos(6x))=6\sin^2(2x)\cos(2x)$.
At $x=\pi/4$ the result is zero. The manuscript's shifted cosine-cube check
is valid because that expression is both even and differentiable. No domain
restriction beyond real angles in radians is needed.

## Antiderivatives: I1

### I1-001 — Polynomial antiderivatives by linearity

Termwise integration gives $2x^3-2x^2+5x+C$. Direct differentiation returns
$6x^2-4x+5$ at every real input. The entire real line is connected, so one
constant independent of $x$ describes the complete family; the solution states
this dependence correctly.

### I1-002 — The reciprocal rule and two separate intervals

On $x>0$, differentiation of $3\ln x+C_+$ gives $3/x$.
On $x<0$, differentiation of $3\ln(-x)+C_-$ gives
$3(-1)/(-x)=3/x$. The two constants are independent because the domain has
two connected components. No primitive across zero is asserted, and the
negative-input chain-rule sign is correct.

### I1-003 — Evaluate at both endpoints

The primitive $x^2+3x$ has endpoint values $10$ and $-2$, so the integral is
$12$. Independently, a linear graph has mean endpoint height
$(1+7)/2=4$ over width $3$, also giving $12$. The integrand is continuous
and positive on the interval, and the hints preserve the endpoint order.

### I1-004 — Reverse an exponential chain rule

Differentiation of $A\exp(3x)$ yields $3A\exp(3x)$, so $A=1/3$.
Thus the complete family is $\exp(3x)/3+C$ on the real line. Both the
coefficient equation and its derivative check are correct.

### I1-005 — Integrate a trigonometric sum

Differentiation of $2\sin x+3\cos x+C$ returns
$2\cos x-3\sin x$. The positive cosine coefficient supplies the required
negative sine term. All real inputs are admissible and the arbitrary constant
is independent of $x$.

### I1-006 — Signed accumulation versus area

Oddness gives the signed integral zero. Partition at zero gives
$\int_{-1}^0(-x)\,dx+\int_0^1x\,dx=1/2+1/2=1$.
The primitive evaluations and the two-triangle area check agree, and neither
signed cancellation nor the absolute-value operation is misused.

## Coordinate changes: I2

### I2-001 — Evaluate a definite integral

Direct expansion of the original integrand gives
$2x^7+6x^5+6x^3+2x$. Integrating from zero to one yields
$1/4+1+3/2+1=15/4$, independently confirming the substitution calculation.
The mapped bounds are $1$ and $2$, the derivative factor is $2x$, and the
vanishing derivative at zero is permitted by the direct substitution theorem.

### I2-002 — A derivative match needing a fixed multiplier

Differentiating $(1+x^2)^5/10+C$ gives
$(5/10)(1+x^2)^4(2x)=x(1+x^2)^4$. No division by $x$ is needed, so zero
remains in the domain and the formula holds on the entire real line.
The factor $1/2$ in the substitution is retained correctly.

### I2-003 — A cubic inside an exponential

The original integrand is the derivative of $\exp(x^3)$, so the definite
integral equals $\exp(1)-1$. The new bounds under $u=x^3$ remain zero and
one; $3x^2$ is the exact derivative factor, including at zero.
The exponential primitive, endpoint subtraction, and hints agree.

### I2-004 — A trigonometric input inside a reciprocal

The logarithm input satisfies $1\le2+\sin x\le3$. Differentiating
$\ln(2+\sin x)+C$ therefore gives the original integrand for all real
inputs. Global injectivity of $2+\sin x$ is not required by this direct
chain-rule substitution. The absence of an absolute value is justified by
positivity, and no division by the potentially zero cosine is used.

### I2-005 — Transforming reversed endpoints

The primitive $\ln(1+x^2)$ gives $F(0)-F(1)=-\ln2$.
The substitution maps the lower bound $1$ to $2$ and the upper bound $0$ to
$1$, preserving orientation. Positivity on the forward interval supplies an
independent sign check. All denominators remain positive.

## Supplementary numerical verification and limits

Ninety-two additional standard-library numerical checks passed: 52 central
finite differences of the 13 original derivative functions, 24 finite
differences of six antiderivative families, six direct Simpson quadratures of
the definite integrals, and ten requested derivative-value checks. Inputs
sample both connected components where applicable and retain original rational
function formulas before cancellation. Different integration constants were
used on the two components of I1-002. These checks supplement the analytical
arguments above and do not establish behavior at excluded points.

All 24 statements, their three hints, the worked calculations, and the checks
agree. No unresolved mathematical finding remains in the reviewed reference
exercises. Complete-book pagination, web accessibility, and external reader
feedback are outside this mathematical audit.
