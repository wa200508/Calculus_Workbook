# Calculus quick reference

Four pages accompany the notation chapter and methods reference. Unless specified
otherwise, all inputs, parameters, and function values are real scalars; parameters
are fixed during the stated operation. Every primitive is defined on a connected
interval of its domain. Independent coordinates are held fixed in partial
derivatives unless a path dependence is displayed. The conditions stated below
are sufficient conditions, rather than exhaustive versions of the theorems.

## 1. Notation and elementary formulas

### Objects and dependencies

$x,t,u$: independent scalar inputs. $a,b,p$: fixed scalar parameters.
$z=f(x,y)$: dependent scalar value with independent coordinates $x,y$.
$f(x;a)$: scalar function with fixed parameter $a$.
$\mathbf r(t)\in\mathbb R^n$: dependent column vector.
$\mathbf A(t)\in\mathbb R^{m\times n}$: dependent matrix.
$\boldsymbol{\mathcal T}(t)$: tensor with specified space, basis, order, and index ranges;
$T_{ijk}(t)$ denotes a scalar component. Sums are explicit.

### Operators, evaluation, and constants

$$
\frac{d}{dx}(f(x)),\qquad
\frac{\partial}{\partial x}(f(x,y))\quad(y\text{ fixed}).
$$

$$
\left.\frac{d}{dx}(f(x))\right|_{x=a},\qquad
\left.F(x)\right|_{x=a}^{x=b}=F(b)-F(a).
$$

Evaluation follows differentiation. The operator operand is parenthesized;
square brackets represent arrays or closed intervals. Prime marks and time dots
are not used. A definite integral binds its integration variable.

$$
\int f(x,y)\,dx=F(x,y)+C(y),\quad y\text{ fixed}.
$$

$C(y)$ is independent of $x$. Vector and matrix primitives have constants of the
same output shape. $|s|$: scalar absolute value; $\lVert\mathbf v\rVert$: specified
vector norm; $\det(\mathbf A)$: determinant. $f^{-1}$ denotes a defined inverse
function; $1/f(x)$ denotes a reciprocal. $\mathbf A^{\mathsf T}$ denotes transpose.

### Elementary derivatives

$x$ is independent; $p$ is fixed. Power formulas below hold for $x>0$ and any
real $p$; integer powers can have larger domains.

$$
\begin{aligned}
\frac{d}{dx}(x^p)&=px^{p-1},&
\frac{d}{dx}(1/x)&=-1/x^2,\\
\frac{d}{dx}(\exp(x))&=\exp(x),&
\frac{d}{dx}(\ln|x|)&=1/x,\\
\frac{d}{dx}(\sin(x))&=\cos(x),&
\frac{d}{dx}(\cos(x))&=-\sin(x),\\
\frac{d}{dx}(\tan(x))&=1/(\cos(x))^2.
\end{aligned}
$$

Reciprocal and logarithm formulas require $x\ne0$; the tangent formula requires
$\cos(x)\ne0$. Exponential, sine, and cosine formulas hold for all real $x$.

<!-- column -->

### Elementary primitives

$x$ is the integration variable; $C$ is independent of $x$.

$$
\begin{aligned}
\int x^p\,dx&=\frac{x^{p+1}}{p+1}+C&& (p\ne-1),\\
\int\frac{1}{x}\,dx&=\ln|x|+C&&(x\ne0),\\
\int\exp(x)\,dx&=\exp(x)+C,\\
\int\ln(x)\,dx&=x\ln(x)-x+C&&(x>0),\\
\int\sin(x)\,dx&=-\cos(x)+C,\\
\int\cos(x)\,dx&=\sin(x)+C,\\
\int\tan(x)\,dx&=-\ln|\cos(x)|+C&&(\cos(x)\ne0).
\end{aligned}
$$

The power domain is as in the derivative table. Logarithmic primitives on
disconnected intervals have independent constants.

### Hyperbolic functions and inverse branches

Hyperbolic derivatives and primitives hold for all real $x$.

$$
\begin{aligned}
\frac{d}{dx}(\sinh(x))&=\cosh(x),&\int\sinh(x)\,dx&=\cosh(x)+C,\\
\frac{d}{dx}(\cosh(x))&=\sinh(x),&\int\cosh(x)\,dx&=\sinh(x)+C,\\
\frac{d}{dx}(\tanh(x))&=\frac{1}{(\cosh(x))^2},\\
\int\tanh(x)\,dx&=\ln(\cosh(x))+C.
\end{aligned}
$$

The standard real inverse branches give

$$
\begin{aligned}
\frac{d}{dx}(\arcsin(x))&=\frac{1}{\sqrt{1-x^2}}&&(|x|<1),\\
\frac{d}{dx}(\arccos(x))&=-\frac{1}{\sqrt{1-x^2}}&&(|x|<1),\\
\frac{d}{dx}(\arctan(x))&=\frac{1}{1+x^2}&&(x\in\mathbb R),\\
\frac{d}{dx}(\operatorname{arsinh}(x))&=\frac{1}{\sqrt{1+x^2}}&&(x\in\mathbb R),\\
\frac{d}{dx}(\operatorname{arcosh}(x))&=\frac{1}{\sqrt{x^2-1}}&&(x>1),\\
\frac{d}{dx}(\operatorname{artanh}(x))&=\frac{1}{1-x^2}&&(|x|<1).
\end{aligned}
$$

These identities also identify primitives of the right-hand sides. The real
primitive of $1/(1-x^2)$ extends to each interval avoiding $\pm1$ as
$\tfrac12\ln|(1+x)/(1-x)|+C$. Inverse-function endpoint continuity does not
establish a finite endpoint derivative.

## 2. Differentiation and local behavior

### Linear combinations, products, and quotients

$x$ is independent; $a,b$ are fixed; $u(x),v(x)$ are differentiable scalar functions.

$$
\begin{aligned}
\frac{d}{dx}(au(x)+bv(x))
&=a\frac{d}{dx}(u(x))+b\frac{d}{dx}(v(x)),\\
\frac{d}{dx}(u(x)v(x))
&=\frac{d}{dx}(u(x))v(x)+u(x)\frac{d}{dx}(v(x)),\\
\frac{d}{dx}\left(\frac{u(x)}{v(x)}\right)
&=\frac{\frac{d}{dx}(u(x))v(x)-u(x)\frac{d}{dx}(v(x))}{(v(x))^2}.
\end{aligned}
$$

The quotient requires $v(x)\ne0$. Cancellation retains exclusions inherited
from the original expression. Second derivatives act on the entire first derivative.

### Compositions and inverse functions

$f(x)=h(g(x))$; $t$ is the independent scalar argument of $h(t)$.

$$
\frac{d}{dx}(f(x))
=\left.\frac{d}{dt}(h(t))\right|_{t=g(x)}\frac{d}{dx}(g(x)).
$$

The inner value must lie in the differentiable domain of the outer function.
For a local inverse $h(u)$ of a differentiable scalar $g(x)$,

$$
\frac{d}{du}(h(u))
=\frac{1}{\left.\frac{d}{dx}(g(x))\right|_{x=h(u)}}.
$$

The denominator is nonzero and the inverse branch is specified.

### Logarithmic differentiation and variable powers

For $f(x)\ne0$ on a real interval,

$$
\frac{d}{dx}(\ln|f(x)|)=\frac{\frac{d}{dx}(f(x))}{f(x)}.
$$

For differentiable scalars $a(x)>0,b(x)$ and $f(x)=a(x)^{b(x)}$,

$$
\frac{d}{dx}(f(x))
=f(x)\left(\frac{d}{dx}(b(x))\ln(a(x))
+b(x)\frac{\frac{d}{dx}(a(x))}{a(x)}\right).
$$

For a nonzero complex scalar response $H(\omega)$, with real independent
$\omega$ and $i^2=-1$, a differentiable local phase $\phi(\omega)$ satisfies

$$
\frac{d}{d\omega}(\phi(\omega))
=\operatorname{Im}\left(\frac{\frac{d}{d\omega}(H(\omega))}{H(\omega)}\right).
$$

Zeros and phase jumps require separate treatment. Real-parameter complex
outputs are differentiated componentwise; complex analyticity is not assumed.

<!-- column -->

### Independent coordinates and paths

For differentiable scalar $f(x,y)$ and scalar paths $x(t),y(t)$,
$p(t)=f(x(t),y(t))$ is scalar and $t$ is independent:

$$
\begin{aligned}
\frac{d}{dt}(p(t))
={}&\left.\frac{\partial}{\partial x}(f(x,y))\right|_{x=x(t),y=y(t)}\frac{d}{dt}(x(t))\\
&+\left.\frac{\partial}{\partial y}(f(x,y))\right|_{x=x(t),y=y(t)}\frac{d}{dt}(y(t)).
\end{aligned}
$$

The other independent coordinate is fixed in each partial derivative.
A path derivative includes every dependent coordinate. Reversal of mixed
partial order is justified, for example, by continuous second partials near the point.

### Implicit functions and regular constraints

A continuously differentiable scalar $F(x,y,z)$ defines a local scalar
height $z=g(x,y)$ where $F(x,y,g(x,y))=0$ and its $z$ partial is nonzero:

$$
\frac{\partial}{\partial x}(g(x,y))
=-\left.\frac{\frac{\partial}{\partial x}(F(x,y,z))}
{\frac{\partial}{\partial z}(F(x,y,z))}\right|_{z=g(x,y)}.
$$

Here $y$ is held fixed. A zero denominator can invalidate this height chart
without making the level surface singular. A regular level surface has nonzero
gradient. For scalar objective $f(\mathbf x)$ and constraint $c(\mathbf x)=0$,
with independent vector $\mathbf x\in\mathbb R^n$, regular constrained stationary
points satisfy $\nabla f(\mathbf x)=\lambda\nabla c(\mathbf x)$ for a scalar
$\lambda$. Feasible tangent vectors $\mathbf v$ satisfy
$\nabla c(\mathbf x)\cdot\mathbf v=0$. Boundaries remain separate cases.

### Endpoint derivatives and error notation

For a scalar function with extension $f(a)$, a derivative is determined by

$$
\lim_{h\to0}\frac{f(a+h)-f(a)}{h}.
$$

The allowed domain determines whether the limit is one-sided. An interior
formula alone does not establish differentiability of an extension.

For real scalars $r(x),g(x)$ in a specified limit $x\to a$,
$r(x)=O(g(x))$ means $|r(x)|\le M|g(x)|$ near $a$ for a finite fixed $M$;
$r(x)=o(g(x))$ means $r(x)/g(x)\to0$, where $g(x)\ne0$ off $a$.
A value remainder estimate cannot automatically be differentiated.
An asymptotic expansion need not be convergent. Explicit numerical error
bounds require constants and a stated interval.

## 3. Integration, parameters, and convergence

### Primitives and the fundamental theorem

$q(x)$ is continuous, $a$ is fixed, and $t$ is an independent scalar:

$$
F(t)=\int_a^t q(x)\,dx,\qquad \frac{d}{dt}(F(t))=q(t).
$$

If $\frac{d}{dx}(Q(x))=q(x)$, then $\int_a^bq(x)\,dx=Q(b)-Q(a)$.
For differentiable endpoints and continuous $q(x,t)$ and parameter partial
on a neighborhood of the finite integration region,

$$
\begin{aligned}
\frac{d}{dt}\left(\int_{a(t)}^{b(t)}q(x,t)\,dx\right)
={}&q(b(t),t)\frac{d}{dt}(b(t))\\
&-q(a(t),t)\frac{d}{dt}(a(t))\\
&+\int_{a(t)}^{b(t)}\frac{\partial}{\partial t}(q(x,t))\,dx.
\end{aligned}
$$

### Substitution and inverse coordinates

For $g(x)$ continuously differentiable and $h(u)$ continuous on its image,
with fixed scalar endpoints $a,b$,

$$
\int_a^b h(g(x))\frac{d}{dx}(g(x))\,dx
=\int_{g(a)}^{g(b)}h(u)\,du.
$$

This direct form does not require an inverse. An inverse chart
$x=\xi(u)$ requires a valid branch and the factor
$\frac{d}{du}(\xi(u))$. Turning points may require interval partition.
Integrand, differential, endpoints, and orientation change together.

### Parts, rational forms, and symmetry

For continuously differentiable scalars $u(x),v(x)$ on a finite interval,

$$
\begin{aligned}
\int_a^b u(x)\frac{d}{dx}(v(x))\,dx
={}&u(b)v(b)-u(a)v(a)\\
&-\int_a^b\frac{d}{dx}(u(x))v(x)\,dx.
\end{aligned}
$$

Repeated parts can give a recurrence or an equation for the original integral.
Improper boundary terms require limits. Polynomial division precedes partial
fractions for an improper rational function; repeated linear and irreducible
quadratic factors retain their powers and excluded zeros.

For integrable scalar $f(x)$ on $[-a,a]$, $a>0$, oddness gives zero integral;
evenness gives $2\int_0^a f(x)\,dx$. Absolute values are partitioned at sign
changes. Periodic integrands permit complete periods plus a remainder.
Improper existence precedes symmetric cancellation.

<!-- column -->

### Differentiation under an integral

For fixed domain $D$ and scalar $q(x,t)$, an integrable bound for
$|\frac{\partial}{\partial t}(q(x,t))|$, uniform near the parameter value,
permits

$$
\frac{d}{dt}\left(\int_Dq(x,t)\,dx\right)
=\int_D\frac{\partial}{\partial t}(q(x,t))\,dx,
$$

with measurability, pointwise differentiability in $t$, and existence of the
integral at one parameter value. Integration back in $t$ introduces a constant
independent of $t$, determined from a known value or limit. Endpoint parameter
values may require a new bound.

### Improper integrals and principal values

At a singular point, independent one-sided limits define the ordinary improper
integral. For nonnegative functions comparable to $x^{-p}$, integrability near
zero requires $p<1$; at infinity it requires $p>1$. Area and volume Jacobians
alter the effective exponent.

A Cauchy principal value couples exclusions. For fixed $a<c<b$,

$$
\operatorname{PV}\int_a^b f(x)\,dx
=\lim_{\varepsilon\to0^+}\left(
\int_a^{c-\varepsilon}f(x)\,dx+\int_{c+\varepsilon}^b f(x)\,dx\right).
$$

Existence of this limit does not imply ordinary improper convergence.

### Limits, series, and order of integration

**Dominated convergence:** measurable pointwise limits with a single
integrable bound permit passage of the limit through the integral.
**Monotone convergence:** increasing nonnegative measurable sequences permit it.
**Tonelli:** nonnegative measurable integrands permit order exchange.
**Fubini:** absolute integrability permits order exchange.
Uniform convergence on a finite interval permits termwise integration of a
continuous function series. Termwise differentiation needs derivative control.
Pointwise convergence alone is insufficient.

### Oscillation, damping, and representations

Integration by parts against a bounded oscillatory primitive can bound tails
when amplitude decay and derivative control suffice. Positive exponential
damping may restore absolute convergence. Its removal needs a limiting argument,
such as convergence on finite intervals and a uniform tail bound.
Stationary phase and steepest descent give asymptotic estimates under additional
hypotheses. Special functions are valid exact answers when their definition,
branch, and domain are given. Numerical answers retain a domain and error estimate.

## 4. Geometry, matrix calculus, and supporting tools

### Gradient, Jacobian, Hessian, and path tangent

$f(\mathbf x)\in\mathbb R$, $\mathbf F(\mathbf x)\in\mathbb R^m$;
$\mathbf x=(x_1,\ldots,x_n)^{\mathsf T}$ has independent real coordinates.
The gradient is an $n$-component column vector, the Jacobian is $m\times n$,
and the Hessian is $n\times n$:

$$
\begin{aligned}
(\nabla f(\mathbf x))_j&=\frac{\partial}{\partial x_j}(f(\mathbf x)),\\
J_{ij}(\mathbf x)&=\frac{\partial}{\partial x_j}(F_i(\mathbf x)),\\
H_{ij}(\mathbf x)&=\frac{\partial}{\partial x_j}
\left(\frac{\partial}{\partial x_i}(f(\mathbf x))\right).
\end{aligned}
$$

The other coordinates are held fixed; $1\le i\le m$ for $J$, and
$1\le i,j\le n$ for $H$. Along differentiable vector path $\mathbf x(t)$,

$$
\frac{d}{dt}(\mathbf F(\mathbf x(t)))
=\mathbf J(\mathbf x(t))\frac{d}{dt}(\mathbf x(t)).
$$

### Coordinate measures and orientations

For a one-to-one regular map $\mathbf x(\mathbf u)\in\mathbb R^n$ with
Jacobian $\mathbf J(\mathbf u)$, $dV=|\det(\mathbf J(\mathbf u))|\,du_1\cdots du_n$.
The coordinates $u_1,\ldots,u_n$ are independent; the transformed integrand is
evaluated at $\mathbf x(\mathbf u)$. Overlap requires partition or multiplicity.

For regular vector surface $\mathbf r(u,v)\in\mathbb R^3$,

$$
dS=\left\lVert\frac{\partial}{\partial u}(\mathbf r(u,v))
\times\frac{\partial}{\partial v}(\mathbf r(u,v))\right\rVert\,du\,dv.
$$

Flux uses the oriented cross product rather than its norm. A vector path
$\mathbf r(t)$ gives $ds=\lVert\frac{d}{dt}(\mathbf r(t))\rVert\,dt$ and
$d\mathbf r=\frac{d}{dt}(\mathbf r(t))\,dt$.

### Integral theorems and sources

For $\mathbf F(\mathbf x)\in\mathbb R^3$ continuously differentiable near a
bounded volume $V$ with piecewise smooth boundary and outward unit normal $\mathbf n$,

$$
\iint_{\partial V}\mathbf F(\mathbf x)\cdot\mathbf n\,dS
=\iiint_V\nabla\cdot\mathbf F(\mathbf x)\,dV.
$$

Stokes' theorem equates oriented boundary circulation with curl flux through
a spanning surface; Green's theorem is its planar counterpart. Each requires
its own smoothness and consistent boundary orientation. Excluded sources
introduce inner boundaries; classical formulas cannot simply be applied across
singularities. Topology matters for circulation and potentials.

<!-- column -->

### Matrix and tensor derivatives

$t$ is scalar; $\mathbf A(t)\in\mathbb R^{n\times n}$ is differentiable and
invertible; $\mathbf b\in\mathbb R^n$ is fixed;
$\mathbf j(t)=\mathbf A(t)^{-1}\mathbf b$:

$$
\begin{aligned}
\frac{d}{dt}(\mathbf A(t)^{-1})
&=-\mathbf A(t)^{-1}\frac{d}{dt}(\mathbf A(t))\mathbf A(t)^{-1},\\
\frac{d}{dt}(\mathbf j(t))
&=-\mathbf A(t)^{-1}\frac{d}{dt}(\mathbf A(t))\mathbf j(t).
\end{aligned}
$$

Matrix order is retained. For scalar $\phi(\mathbf A)$ on independent matrix
entries, $(\nabla_{\mathbf A}\phi(\mathbf A))_{ij}=\frac{\partial}{\partial A_{ij}}(\phi(\mathbf A))$, with all other entries fixed.
Constraints require independent parameters. $\mathrm D\mathbf F(\mathbf A)(\mathbf H)$
is a linear derivative map applied to an increment of stated shape.
In a fixed basis, tensor derivative and integral components are
$\frac{d}{dt}(T_{ijk}(t))$ and $\int_a^bT_{ijk}(t)\,dt$; component indices range
over the declared tensor shape. A changing basis adds its derivatives.

### Supporting identities and coordinates

For real scalar $x$, fixed $a>0$, and $i^2=-1$,

$$
\begin{aligned}
\exp(ix)&=\cos(x)+i\sin(x),\\
(\sin(x))^2&=\tfrac12(1-\cos(2x)),\\
(\cos(x))^2&=\tfrac12(1+\cos(2x)),\\
(\cosh(x))^2-(\sinh(x))^2&=1.
\end{aligned}
$$

$u=\tan(x/2)$ gives $\sin(x)=2u/(1+u^2)$,
$\cos(x)=(1-u^2)/(1+u^2)$, and inverse differential
$dx=2\,du/(1+u^2)$ on a selected angular chart.
Coordinates $x=a\sin(u)$, $x=a\tan(u)$, $x=a\sinh(u)$, and $x=a\cosh(u)$
address quadratic roots on specified branches; $\sqrt{q^2}=|q|$ for real $q$.

### Taylor formulas and local expansions

For scalar $f(x)$ with $n+1$ continuous derivatives between $a$ and $x$,

$$
f(x)=\sum_{k=0}^{n}\frac{\left.\frac{d^k}{dt^k}(f(t))\right|_{t=a}}{k!}(x-a)^k+R_n(x),
$$

where the $k=0$ derivative means $f(t)$. If the absolute $(n+1)$st derivative
is bounded by $M$ on that interval,
$|R_n(x)|\le M|x-a|^{n+1}/(n+1)!$.
As real $x\to0$,

$$
\begin{aligned}
\exp(x)&=1+x+x^2/2+O(x^3),\\
\sin(x)&=x-x^3/6+O(x^5),\\
\cos(x)&=1-x^2/2+O(x^4),\\
\ln(1+x)&=x-x^2/2+O(x^3),\\
\arctan(x)&=x-x^3/3+O(x^5).
\end{aligned}
$$

These are local statements; integral or derivative interchange needs separate
justification. Supporting identities and expansions are purple in the book.
