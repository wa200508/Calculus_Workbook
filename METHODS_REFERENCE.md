# Calculus methods reference

This reference concludes the introduction. Each method is presented with its
operative form, applicability conditions, and useful structural indicators.
The subsequent chapters contain mixed problem sets; no single method is assigned
to a chapter. Scalars are real unless complex values are declared explicitly.
All fixed parameters are held fixed in the displayed operations.

## Differentiation and local representations

### Elementary derivatives and primitives

The independent input $x$ and the fixed parameter $p$ are real scalars. The
following formulas apply on the indicated real domains. Each primitive is
understood on a connected interval of that domain; $C$ is an arbitrary constant
on that interval.

| Scalar expression | Derivative with respect to $x$ | Primitive with respect to $x$ | Real-domain restriction |
|---|---|---|---|
| $x^p$ | $\frac{d}{dx}(x^p)=px^{p-1}$ | $\int x^p\,dx=\frac{x^{p+1}}{p+1}+C$, $p\ne-1$ | $x>0$ suffices for arbitrary real $p$; integer powers may have larger domains |
| $1/x$ | $\frac{d}{dx}(1/x)=-1/x^2$ | $\int (1/x)\,dx=\ln|x|+C$ | $x\ne0$ |
| $\exp(x)$ | $\frac{d}{dx}(\exp(x))=\exp(x)$ | $\int\exp(x)\,dx=\exp(x)+C$ | All real $x$ |
| $\ln(x)$ | $\frac{d}{dx}(\ln(x))=1/x$ | $\int\ln(x)\,dx=x\ln(x)-x+C$ | $x>0$ |
| $\sin(x)$ | $\frac{d}{dx}(\sin(x))=\cos(x)$ | $\int\sin(x)\,dx=-\cos(x)+C$ | All real $x$ |
| $\cos(x)$ | $\frac{d}{dx}(\cos(x))=-\sin(x)$ | $\int\cos(x)\,dx=\sin(x)+C$ | All real $x$ |
| $\tan(x)$ | $\frac{d}{dx}(\tan(x))=1/\cos^2(x)$ | $\int\tan(x)\,dx=-\ln|\cos(x)|+C$ | $\cos(x)\ne0$ |
| $\sinh(x)$ | $\frac{d}{dx}(\sinh(x))=\cosh(x)$ | $\int\sinh(x)\,dx=\cosh(x)+C$ | All real $x$ |
| $\cosh(x)$ | $\frac{d}{dx}(\cosh(x))=\sinh(x)$ | $\int\cosh(x)\,dx=\sinh(x)+C$ | All real $x$ |
| $\tanh(x)$ | $\frac{d}{dx}(\tanh(x))=1/\cosh^2(x)$ | $\int\tanh(x)\,dx=\ln(\cosh(x))+C$ | All real $x$ |

Inverse-function derivatives often identify a primitive more efficiently than
algebraic expansion. With the standard real branches,

$$
\begin{aligned}
\frac{d}{dx}(\arcsin(x))&=\frac{1}{\sqrt{1-x^2}},&&-1<x<1,\\
\frac{d}{dx}(\arccos(x))&=-\frac{1}{\sqrt{1-x^2}},&&-1<x<1,\\
\frac{d}{dx}(\arctan(x))&=\frac{1}{1+x^2},&&x\in\mathbb R,\\
\frac{d}{dx}(\operatorname{arsinh}(x))&=\frac{1}{\sqrt{1+x^2}},&&x\in\mathbb R,\\
\frac{d}{dx}(\operatorname{arcosh}(x))&=\frac{1}{\sqrt{x^2-1}},&&x>1,\\
\frac{d}{dx}(\operatorname{artanh}(x))&=\frac{1}{1-x^2},&&-1<x<1.
\end{aligned}
$$

The square roots in these real formulas are nonnegative. Endpoint continuity
of an inverse function does not imply a finite endpoint derivative. The
antiderivative of $1/(1-x^2)$ also has real branches outside $(-1,1)$:
$\frac12\ln|(1+x)/(1-x)|+C$ applies on each interval excluding $x=\pm1$.
Arguments such as $g(x)$ require the corresponding chain factor or substitution;
the displayed formulas do not remove that dependence.

### Linearity, products, quotients, and compositions

For an independent real scalar $x$, fixed scalars $a,b$, and differentiable
scalar functions $u(x),v(x)$,

$$
\begin{aligned}
\frac{d}{dx}\left(au(x)+bv(x)\right)&=a\frac{d}{dx}\left(u(x)\right)+b\frac{d}{dx}\left(v(x)\right),\\
\frac{d}{dx}\left(u(x)v(x)\right)&=\frac{d}{dx}\left(u(x)\right)v(x)+u(x)\frac{d}{dx}\left(v(x)\right),\\
\frac{d}{dx}\left(\frac{u(x)}{v(x)}\right)&=\frac{\frac{d}{dx}(u(x))v(x)-u(x)\frac{d}{dx}(v(x))}{v(x)^2},\quad v(x)\ne0.
\end{aligned}
$$

For $f(x)=h(g(x))$, with independent real scalar argument $t$ of the outer
function $h(t)$, the chain rule is

$$
\frac{d}{dx}\left(f(x)\right)
=\left.\frac{d}{dt}\left(h(t)\right)\right|_{t=g(x)}\frac{d}{dx}\left(g(x)\right).
$$

The inner value must lie in the differentiability domain of the outer function.
Factoring, polynomial division, or a different representation may reduce the
number of rule applications. Cancellation preserves exclusions from the original
domain. Several nested arguments may be represented by separately named functions.

### Logarithmic differentiation and variable powers

For differentiable real scalar $f(x)>0$,

$$
\frac{d}{dx}\left(\ln(f(x))\right)=\frac{\frac{d}{dx}(f(x))}{f(x)}.
$$

A positive base $a(x)$ with real exponent $b(x)$ gives
$f(x)=a(x)^{b(x)}=\exp(b(x)\ln(a(x)))$, hence

$$
\frac{d}{dx}\left(f(x)\right)
=f(x)\left(\frac{d}{dx}(b(x))\ln(a(x))
+b(x)\frac{\frac{d}{dx}(a(x))}{a(x)}\right).
$$

This representation is useful when both base and exponent depend on the input,
or when products and powers would otherwise generate many terms. For nonzero
real $f(x)$, $\ln|f(x)|$ has the same logarithmic derivative on each connected
component. Complex logarithms require a selected local branch.

### Implicit differentiation and coordinate charts

For a continuously differentiable scalar level function $F(x,y,z)$ and a local
scalar height $z=g(x,y)$ satisfying $F(x,y,g(x,y))=0$,

$$
\frac{\partial}{\partial x}\left(g(x,y)\right)
=-\left.\frac{\frac{\partial}{\partial x}(F(x,y,z))}{\frac{\partial}{\partial z}(F(x,y,z))}\right|_{z=g(x,y)},
\qquad \frac{\partial}{\partial z}\left(F(x,y,z)\right)\ne0.
$$

The independent coordinate $y$ is held fixed. A vanishing denominator can mean
that the selected height chart fails while another chart remains regular.
The full gradient, rather than one coordinate partial derivative, tests regularity
of the level surface. The same principle applies to implicit scalar relations
$F(x,y)=0$ and locally defined $y=g(x)$.

### Paths, partial derivatives, and second derivatives

For a scalar field $f(x,y)$ and a differentiable real path with components
$x(t),y(t)$, the dependent scalar $p(t)=f(x(t),y(t))$ satisfies

$$
\frac{d}{dt}\left(p(t)\right)
=\left.\frac{\partial}{\partial x}(f(x,y))\right|_{x=x(t),y=y(t)}\frac{d}{dt}(x(t))
+\left.\frac{\partial}{\partial y}(f(x,y))\right|_{x=x(t),y=y(t)}\frac{d}{dt}(y(t)).
$$

A partial derivative and a derivative along a constrained path are different
operations. Second derivatives differentiate the complete first-derivative
expression, including every dependent factor. Interchanging mixed partials
requires appropriate regularity, such as continuous second partial derivatives
on a neighborhood of the point.

### Inverse functions, phase, and endpoint limits

For a differentiable one-to-one scalar function $g(x)$ with nonzero derivative,
its local inverse $h(u)$ satisfies

$$
\frac{d}{du}\left(h(u)\right)
=\frac{1}{\left.\frac{d}{dx}(g(x))\right|_{x=h(u)}}.
$$

An inverse branch may require an interval restriction. A finite symbolic
expression does not establish differentiability across a phase jump, cusp,
or excluded point. At a domain endpoint, a one-sided difference quotient is
examined separately. A continuous extension can exist without a finite derivative.
Complex scalar outputs differentiated with respect to real parameters are
handled componentwise; this does not assume complex analyticity.

## Antiderivatives and finite integrals

### Direct substitution and inverse-coordinate substitution

For a continuously differentiable real scalar $g(x)$ and continuous scalar
$h(u)$ on the required image interval,

$$
\int_a^b h(g(x))\frac{d}{dx}\left(g(x)\right)\,dx
=\int_{g(a)}^{g(b)}h(u)\,du.
$$

The direct chain-rule form does not require $g$ to be one-to-one. An inverse
coordinate formula instead requires a valid inverse branch $x=\xi(u)$ and the
factor $\frac{d}{du}(\xi(u))$. A map with turning points may require partition
into branches. Limits, orientation, integrand, and measure are transformed together.
An unmatched derivative factor cannot be discarded.

### Integration by parts and recurrences

For continuously differentiable scalar functions $u(x),v(x)$ on a finite interval,

$$
\int_a^b u(x)\frac{d}{dx}\left(v(x)\right)\,dx
=u(b)v(b)-u(a)v(a)-\int_a^b\frac{d}{dx}\left(u(x)\right)v(x)\,dx.
$$

This is useful when one factor simplifies under differentiation and another has
an accessible primitive. Repeated applications can produce a recurrence for a
family of integrals or an equation involving the original integral. On unbounded
intervals, every boundary term and remainder integral requires its own limit.
A boundary expression is not set to zero solely because the integrand decays.

### Rational functions and partial fractions

Polynomial division separates a rational scalar function into a polynomial and
a proper rational remainder. Factorization over the real numbers then permits
terms associated with real linear factors and irreducible quadratic factors,
including their repeated powers. Coefficients are determined by polynomial
identity or evaluation at suitable inputs. The decomposition retains every
excluded denominator zero. Logarithmic primitives carry absolute values on
real connected components; irreducible quadratics commonly lead to arctangents.

### Trigonometric and hyperbolic coordinates

Power reduction, angle addition, and conversion to exponentials can expose a
substitution or an integration-by-parts pattern. The tangent half-angle coordinate
$u=\tan(x/2)$ gives

$$
\sin x=\frac{2u}{1+u^2},\qquad \cos x=\frac{1-u^2}{1+u^2},
\qquad \frac{d}{du}\left(2\arctan u\right)=\frac{2}{1+u^2}
$$

on a chosen inverse chart. Angular poles and interval orientation remain relevant.
For fixed real $a>0$, coordinates $x=a\sin u$, $x=a\tan u$, or $x=a\sinh u$
can resolve square roots of $a^2-x^2$, $a^2+x^2$, or related quadratic expressions.
The identity $\sqrt{q^2}=|q|$ for real $q$ determines the sign of the transformed
root. Hyperbolic identities and their real inverse branches appear in
[T-007](TRICKS_APPENDIX.md#t-007-hyperbolic-identities-and-real-branches).

### Symmetry, partition, and periodicity

On a symmetric finite interval, an integrable odd scalar function has zero
integral; an even integrand permits reduction to half the interval. Absolute
values and piecewise definitions are partitioned at sign changes. Periodicity
can reduce a long finite interval to complete periods and a remainder. For an
improper integral, existence is established before symmetric cancellation is
used. A principal-value prescription is a separately named operation.

### Fundamental theorem and variable limits

For a continuous scalar $q(x)$ and a fixed real base point $a$,
$F(t)=\int_a^t q(x)\,dx$ has derivative $q(t)$ at interior inputs. With
differentiable real scalar endpoints $a(t),b(t)$ and a scalar integrand $q(x,t)$,

$$
\begin{aligned}
\frac{d}{dt}\left(\int_{a(t)}^{b(t)}q(x,t)\,dx\right)
={}&q(b(t),t)\frac{d}{dt}(b(t))
-q(a(t),t)\frac{d}{dt}(a(t))\\
&+\int_{a(t)}^{b(t)}\frac{\partial}{\partial t}\left(q(x,t)\right)\,dx.
\end{aligned}
$$

Continuity of $q$ and its parameter partial derivative on a neighborhood of the
finite integration region is a sufficient local condition. The lower-endpoint
term has a minus sign even when the bounds later reverse their order.

## Parameters, convergence, and representations

### Differentiation with respect to a parameter

For a fixed domain $D$ and scalar $q(x,t)$, a bound on
$|\frac{\partial}{\partial t}(q(x,t))|$ that is integrable over $D$ and valid
uniformly in a neighborhood of the parameter value permits differentiation
under the integral, provided the integral exists at one parameter value and
the integrand has the required measurability and pointwise differentiability.
The new parameter derivative may have a simpler primitive than the original
integrand. Integration back in the parameter introduces a constant independent
of that parameter, which is fixed from a known value or limit. The required
bound may hold near every interior parameter value and fail at its endpoint.

### Improper integrals, comparison, and principal values

Endpoint and interior singularities are treated by independent one-sided limits.
For a nonnegative integrand locally comparable to $x^{-p}$ near zero,
integrability holds for $p<1$; at infinity it holds for $p>1$. In radial area or
volume integrals the Jacobian changes this power count. Signed and oscillatory
integrals may converge conditionally. A Cauchy principal value specifies coupled
exclusions; it need not equal an ordinary improper integral or exist under a
different exclusion prescription.

### Oscillatory integration and damping

Integration by parts against a bounded oscillatory primitive gives tail bounds
when the amplitude decreases sufficiently. Positive exponential damping can
make an integral absolutely convergent and simplify parameter differentiation.
Removing damping requires a separate limit argument, such as convergence on
finite intervals together with a uniform tail estimate. Absolute domination
cannot be assumed for a conditionally convergent limit. Stationary phase and
steepest descent are asymptotic methods with additional smoothness, contour,
and stationary-point hypotheses; they do not provide exact finite-parameter
identities.

### Interchanging limits, sums, and integrals

Dominated convergence requires one integrable dominating function on the domain
under consideration. Monotone convergence applies to increasing nonnegative
measurable sequences. Tonelli's theorem permits rearrangement for nonnegative
integrands; Fubini's theorem provides rearrangement under absolute integrability.
Uniform convergence on a finite interval is a useful sufficient condition for
termwise integration of a function series. Differentiation of a series requires
additional control of the derivative series. A pointwise limit alone supplies
none of these interchanges.

### Series, asymptotics, and special functions

Taylor polynomials retain a remainder estimate; infinite series retain their
convergence domain. An asymptotic expansion orders terms in a specified limit
and need not converge when continued indefinitely. Special functions can provide
an exact representation of a non-elementary primitive or definite integral.
A remaining numerical integral is accompanied by a specified domain, convergence
analysis, and a usable error estimate. Definitions and branch conventions are
stated locally when a special function first appears. Supporting expansions are
collected in [T-002](TRICKS_APPENDIX.md#t-002-taylor-expansions).

## Fields, geometry, and multilinear objects

### Gradients, Jacobians, and constrained variations

A scalar field's Euclidean gradient is a column vector of coordinate partial
derivatives. A vector-valued map's Jacobian is the matrix of its component partials,
with output index first and input index second. Along a path, multiplication of
the Jacobian by the path tangent gives the vector derivative. A Hessian is the
matrix of second scalar partials. A constrained directional derivative requires
a tangent direction satisfying the constraint, rather than an arbitrary coordinate
variation. Lagrange multipliers express regular constrained stationary conditions;
constraint regularity and boundary cases are examined independently.

### Area, volume, and surface measures

For a one-to-one regular coordinate map in two or three dimensions, integration
uses the absolute determinant of the coordinate Jacobian. For an independent
real surface pair $u,v$ and real vector map $\mathbf r(u,v)$, the area factor is

$$
\left\|\frac{\partial}{\partial u}\left(\mathbf r(u,v)\right)
\times\frac{\partial}{\partial v}\left(\mathbf r(u,v)\right)\right\|.
$$

The oriented cross product, rather than its norm, supplies a flux measure.
Line integrals use the path tangent for vector work and its norm for scalar
arc-length integration. Coordinate degeneracies at seams or poles may occupy
sets of measure zero; many-to-one maps require partition or multiplicity accounting.

### Integral theorems and excluded sources

Green's theorem, Stokes' theorem, and the divergence theorem replace suitable
integrals by boundary or interior integrals with consistent orientation and
regularity. For a continuously differentiable real vector field $\mathbf F(x,y,z)$
on a neighborhood of a bounded volume $V$ with piecewise smooth boundary,

$$
\iint_{\partial V}\mathbf F(x,y,z)\cdot\mathbf n(x,y,z)\,dS
=\iiint_V\nabla\cdot\mathbf F(x,y,z)\,dx\,dy\,dz.
$$

The real vector $\mathbf n(x,y,z)$ is the outward unit normal. A source singularity
inside $V$ violates the classical regularity hypothesis. Excision introduces an
additional inner boundary whose orientation and flux must be included. Boundary
conditions and topology can therefore determine an answer before a lengthy
coordinate integration is attempted.

### Matrix systems and tensor components

For a differentiable invertible square matrix $\mathbf A(t)$ and fixed column
vector $\mathbf b$, the dependent vector $\mathbf j(t)=\mathbf A(t)^{-1}\mathbf b$
satisfies

$$
\frac{d}{dt}\left(\mathbf j(t)\right)
=-\mathbf A(t)^{-1}\frac{d}{dt}\left(\mathbf A(t)\right)\mathbf j(t).
$$

Matrix order is retained. Matrix and tensor derivatives can be computed
componentwise after the spaces, shapes, index ranges, and contractions are
specified. For a dependent order-three tensor with scalar components
$T_{ijk}(t)$, its derivative components are $\frac{d}{dt}(T_{ijk}(t))$; its
integral components are $\int_a^bT_{ijk}(t)\,dt$ on a stated real interval.
A tensor representation in a varying basis additionally includes basis derivatives.
Near a singular matrix, sensitivity depends on the right-hand side and cannot
be inferred from a canceled component formula alone.

## Reference sources

These summaries state operative forms and hypotheses rather than reproduce a
published problem sequence. Standard differentiation, integration, and vector
calculus methods are documented in [OpenStax Calculus](https://openstax.org/subjects/math)
and [MIT Calculus with Applications](https://ocw.mit.edu/ans7870/18/18.013a/textbook/index.html).
Parameter-interchange conditions are treated in
[Keith Conrad, Differentiating under the integral sign](https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf).
Special-function definitions are provided by the [NIST Digital Library of Mathematical Functions](https://dlmf.nist.gov/).
