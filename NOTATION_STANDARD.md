# Notational conventions

The notation in this book is based on established conventions of calculus and
linear algebra. Function arguments, variable dependencies, object types, and
operation domains are stated explicitly. A consistent selection of conventions
is adopted throughout; uniform usage across all mathematical disciplines is
not presumed. The literature underlying these choices is discussed in
[the notation review](NOTATION_REVIEW.md).

## 1. Objects, domains, and dependencies

Leibniz operator notation is used for derivatives, with complete function
arguments and ordinary parentheses enclosing the operand. The type of each
object is identified by both its notation and its accompanying definition.

Four kinds of information are provided in the statements and solutions of
worked problems:

1. **Objects and types:** scalar quantities; vectors with a specified dimension; matrices with specified dimensions; and tensors with a specified order, space, basis, and component shape.
2. **Dependencies:** independent inputs, dependent outputs, intermediate functions, and fixed parameters.
3. **Domains and assumptions:** admissible inputs, excluded values, and the regularity or sign conditions relevant to the calculation.
4. **Operations and outputs:** the variable of differentiation or integration, quantities held fixed, and the type of the resulting object.

These declarations are repeated where a solution is presented independently
of its problem statement. Function arguments remain explicit in calculus
expressions. A vector or matrix may appear as a single argument when its
components and dependencies have been defined locally. Lengthy expressions
are presented as a sequence of fully defined intermediate expressions.

## 2. Delimiters and object typography

### Delimiters

| Notation | Meaning in this book | Associated convention |
|---|---|---|
| $f(x,y)$ | Function value at the listed inputs | Parentheses immediately following a function name enclose its arguments |
| $(a+b)$ | Grouping | The complete operand of a derivative is enclosed in parentheses |
| A displayed bracketed column or rectangular array | Vector or matrix representation | The object's type and shape are stated with the array |
| $[a,b]$ | Closed interval | Its scalar input satisfies $a\leq x\leq b$ |
| $\{x:x>0\}$ | Set | Braces delimit a set rather than an ordinary algebraic group |
| $A_{ij}(t)$, $T_{ijk}(t)$ | Scalar components | The parent object, basis, index ranges, and dependencies are specified locally |

Square brackets have several established meanings, including closed intervals
and array representations. They therefore do not, by themselves, identify a
tensor. In this book they are retained for arrays and closed intervals;
parentheses are used for derivative operands and algebraic grouping. Nested
groups are distinguished by parentheses of different sizes. Object type is
established by a definition rather than by delimiters alone.

### Object typography

| Object | Convention | Example declaration |
|---|---|---|
| Scalar | Ordinary italic | $x\in\mathbb R$: independent real scalar |
| Scalar-valued function | Ordinary letter with displayed inputs | $z=f(x,y)\in\mathbb R$: dependent scalar output |
| Vector | Bold lowercase | $\mathbf r(t)\in\mathbb R^3$: column vector depending on scalar $t$ |
| Matrix | Bold uppercase | $\mathbf A(t)\in\mathbb R^{m\times n}$: matrix depending on scalar $t$ |
| Tensor of order three or higher | Bold calligraphic uppercase | $\boldsymbol{\mathcal T}(t)$: tensor with a specified space, order, basis, and component shape |

Scalar entries are denoted in ordinary type: $r_i(t)$, $A_{ij}(t)$, and
$T_{ijk}(t)$. Tensor order is distinguished from tensor rank, which has other
mathematical meanings. The typography in the table represents the convention
adopted for this book rather than a universal convention.

### Function arguments and fixed parameters

A function and a value of that function are distinct objects. The symbol $f$
denotes a function; $f(x,y)$ denotes its value at the displayed inputs.
Accordingly, a dependent scalar output is written as $z=f(x,y)$ rather than
$z=f$.

Fixed parameters are separated from variable inputs by a semicolon. For
example, in the real scalar function $f(x;a)=ax^2$, $x$ is an independent real
scalar input and $a$ is a fixed real scalar parameter. The semicolon records
this distinction; it does not denote an additional calculus operation.
When a quantity varies with an input, its dependence is displayed explicitly,
as in $a(x)$.

For a real scalar function $z=f(x,y)$ of two independent real scalar
coordinates, $x$ and $y$ vary independently. A dependence on a single path
parameter is represented instead by

$$
t\longmapsto (x(t),y(t))\longmapsto z(t)=f(x(t),y(t)).
$$

Here $t$ is the independent real scalar parameter; $x(t)$ and $y(t)$ are
dependent real scalar coordinates; and $z(t)$ is the dependent real scalar
output. The parenthesized coordinate pair represents a point and is
separate from the bracketed column-vector representation.

## 3. Derivatives

### One independent scalar variable

For a differentiable real scalar-valued function $f(x)$ of an independent
real scalar input $x$, the derivative is denoted by

$$
\frac{d}{dx}\left(f(x)\right).
$$

The operator $d/dx$ denotes differentiation with respect to $x$; the
parenthesized expression is its operand. The differentiation variable and
the function's input are therefore visible in the same expression. Prime
marks and time dots are replaced by this operator notation in worked
calculations. An additional pair of parentheses around the operator itself
is not part of the adopted convention.

The second derivative is represented by the established higher-order
operator, whose repeated-operation meaning is

$$
\frac{d^2}{dx^2}\left(f(x)\right)
=\frac{d}{dx}\left(\frac{d}{dx}\left(f(x)\right)\right).
$$

The superscript $2$ indicates two successive differentiations rather than
the square of the derivative. Intermediate derivatives are displayed in
worked higher-order calculations.

Evaluation of the derivative at a fixed real scalar input $a$ is denoted by

$$
\left.\frac{d}{dx}\left(f(x)\right)\right|_{x=a}.
$$

The vertical bar denotes evaluation of the differentiated expression.
Differentiation precedes substitution of the specified input. This
operation differs from differentiation of the constant value $f(a)$.

### Several independent scalar variables

For a differentiable real scalar function $f(x,y)$ of independent real
scalar inputs $x,y$, partial differentiation is written as

$$
\frac{\partial}{\partial x}\left(f(x,y)\right),
\qquad y\text{ held fixed}.
$$

The variable of differentiation is given in the denominator of the
operator. The other independent inputs and fixed parameters are identified
in accompanying text. Where different choices of fixed quantities lead to
different results, the held-fixed quantities are stated with each relevant
expression. A subscripted evaluation bar is reserved for evaluation and is
not also used to denote a held-fixed quantity.

The symbols $d$ and $\partial$ distinguish ordinary and partial
differentiation. In a partial derivative, one independent coordinate varies
while the others are held fixed. Ordinary differentiation applies to an
expression with one independent scalar input, including a composition
whose coordinates depend on a single path parameter.

For a differentiable real scalar function $f(x,y)$ and differentiable real
scalar paths $x(t),y(t)$ with independent real scalar parameter $t$, the
path derivative is represented by

$$
\begin{aligned}
\frac{d}{dt}\left(f(x(t),y(t))\right)
={}&\left.\frac{\partial}{\partial x}\left(f(x,y)\right)
\right|_{x=x(t),\,y=y(t)}
\frac{d}{dt}\left(x(t)\right)\\
&+\left.\frac{\partial}{\partial y}\left(f(x,y)\right)
\right|_{x=x(t),\,y=y(t)}
\frac{d}{dt}\left(y(t)\right).
\end{aligned}
$$

In the first partial derivative $y$ is held fixed; in the second $x$ is
held fixed. Each partial derivative is formed in the independent
coordinates, evaluated on the path, and multiplied by the corresponding
coordinate rate. The resulting path derivative is scalar-valued.

Mixed partial derivatives are initially represented as nested operations,
with their order stated in words. Equality after reversal of that order
requires appropriate hypotheses and is not implied by the notation.

### Vector and matrix outputs

For a single scalar input, differentiation of vector components is
performed in a fixed basis. For example, $t$ is an independent real scalar,
$\mathbf r(t)$ is a two-component real column vector, and $r_1(t),r_2(t)$
are differentiable real scalar component functions:

$$
\mathbf r(t)=\begin{bmatrix}r_1(t)\\r_2(t)\end{bmatrix},
\qquad
\frac{d}{dt}\left(\mathbf r(t)\right)
=\begin{bmatrix}
\frac{d}{dt}\left(r_1(t)\right)\\
\frac{d}{dt}\left(r_2(t)\right)
\end{bmatrix}.
$$

The derivative is a column vector with the same number of components.
Round derivative-operand delimiters are thereby distinguished from square
vector-display delimiters. Matrix and tensor derivatives are accompanied
by the corresponding shape declarations.

For a differentiable real vector-valued function
$\mathbf F(x_1,\ldots,x_n)\in\mathbb R^m$ of independent real scalar
coordinates $x_1,\ldots,x_n$, the Jacobian is an $m\times n$ matrix with
real scalar entries

$$
J_{ij}(x_1,\ldots,x_n)
=\frac{\partial}{\partial x_j}\left(F_i(x_1,\ldots,x_n)\right).
$$

The positive integers $m,n$ specify the output and input dimensions.
All coordinates $x_k$ with $k\ne j$ are held fixed. Index $i$ selects an
output, with $1\leq i\leq m$; index $j$ selects an input, with
$1\leq j\leq n$. Ellipses denote the general coordinate list; actual
coordinates are enumerated in concrete examples.

For a differentiable real scalar function $f(x,y)$ in ordinary Euclidean
coordinates, the gradient is the column vector

$$
\nabla f(x,y)=
\begin{bmatrix}
\frac{\partial}{\partial x}\left(f(x,y)\right)\\
\frac{\partial}{\partial y}\left(f(x,y)\right)
\end{bmatrix}.
$$

The other coordinate is held fixed in each entry. The scalar function's
Jacobian is the transpose of this gradient and is a one-row matrix. These
objects are distinguished by their defined shapes rather than denoted by
an ambiguous fraction with respect to a vector. The superscript
$\mathsf T$ denotes transpose.

### Matrix and tensor inputs

Derivatives with respect to matrix inputs are described first in terms of
individual scalar entries. For a real scalar function $\phi(\mathbf A)$ of
a real $m\times n$ matrix with independently variable entries, the matrix
gradient $\nabla_{\mathbf A}\phi(\mathbf A)$ has the same shape as
$\mathbf A$. Its $(i,j)$ entry is the scalar partial derivative with
respect to $A_{ij}$, with all other entries held fixed. For a symmetric or
otherwise constrained matrix, the independent parameters are identified
separately; all entries cannot then be regarded as independent inputs.

For a differentiable matrix-valued function $\mathbf F(\mathbf A)$, the
notation $\mathrm D\mathbf F(\mathbf A)(\mathbf H)$ denotes the derivative
at the matrix input $\mathbf A$, applied to the increment matrix
$\mathbf H$. The shapes of both matrices and of the output are specified
with the definition. This expression represents a linear map applied to
an increment rather than matrix division. Parentheses around the
increment argument are used in place of the square brackets found in
some references.

For tensor inputs and outputs, the tensor space, basis, component indices,
and index ranges are specified. In geometric tensor notation, upper and
lower indices have distinct meanings, which are defined with the objects.
Summations are written explicitly. Component differentiation is initially
represented in a fixed basis; variation of the basis introduces additional
terms.

## 4. Integrals

For a real scalar-valued integrand $f(x)$ and fixed real scalar endpoints
$a,b$, definite integration with respect to the real scalar variable $x$
is represented by

$$
\int_a^b f(x)\,dx.
$$

The differential $dx$ identifies the integration variable. The lower
limit is $x=a$ and the upper limit is $x=b$. These endpoint statements
accompany the integral; the bounds themselves contain $a$ and $b$.
Parentheses delimit a sum or other compound integrand where necessary.

Within a definite integral, $x$ is a bound integration variable. When
both limits and all parameters are fixed, the result is a real scalar
number rather than a function of $x$.

For an indefinite integral on an interval where an antiderivative exists,

$$
\int f(x)\,dx=F(x)+C,
\qquad \frac{d}{dx}\left(F(x)\right)=f(x).
$$

The real scalar constant $C$ is independent of $x$. For vector and matrix
outputs, the arbitrary constant has the corresponding output shape.

For a real scalar function with another input $y$ held fixed,

$$
\int f(x,y)\,dx=F(x,y)+C(y),\qquad y\text{ held fixed}.
$$

The integration constant may depend on the input over which integration
was not performed. Definite integration over $x$ may likewise leave a
function of $y$.

Endpoint evaluation of an antiderivative is denoted by

$$
\left.F(x)\right|_{x=a}^{x=b}=F(b)-F(a).
$$

The upper-endpoint value is followed by subtraction of the lower-endpoint
value. Multiple integrals are accompanied by a stated order of integration,
with bounds and a differential for each integration variable. Curve,
surface, and volume integrals have specified domains, measures,
parameterizations where applicable, and orientations where relevant.
Arc-length measure $ds$, surface-area measure $dS$, and vector displacement
are distinct objects and are defined separately.

## 5. Change-of-variable notation

In a scalar change of variable, the new coordinate is written as
$u=g(x)$, where $g(x)$ is a real scalar function of the original real
scalar variable $x$. Before substitution, $u$ depends on $x$; within the
transformed integral, $u$ is the integration variable. The expression
$h(u)$ denotes a real scalar function at that new input.

For a continuously differentiable function $g(x)$ on the interval between
fixed real scalar endpoints $a,b$, and a continuous function $h(u)$ on an
interval containing its image, the change of variable is represented by

$$
\int_a^b h(g(x))\frac{d}{dx}\left(g(x)\right)\,dx
=\int_{g(a)}^{g(b)}h(u)\,du.
$$

On the left, the variable is $x$ and the endpoints are $a,b$. On the
right, the variable is $u$ and the endpoints are $g(a),g(b)$. An inverse
of $g(x)$ is not required by this form of the substitution theorem. A
formulation involving an inverse may require domain restrictions and a
specified branch.

The substitution, its derivative, the matching factors, and both
transformed endpoints are displayed in worked definite-integral
calculations. In indefinite-integral results, the original input is
restored and the antiderivative relation is verified by differentiation.

The differential identity $du=2x\,dx$ corresponds to the real scalar
relation $u=g(x)=x^2+1$. The differential of $u$ is the derivative of
$g(x)$ multiplied by the differential of $x$. This notation expresses a
differential relation; cancellation of the letters $d$ and $x$ is not
its justification. Division by a derivative is valid only where that
derivative is nonzero.

## 6. Related symbols and distinctions

- **Finite change and differential.** $\Delta x$ denotes a finite real scalar
  increment. A differential represents the linear part of a change and
  need not equal the exact finite change. The derivative-map expression
  $\mathrm Df(x,y)(\Delta x,\Delta y)$ is accompanied by its defining
  partial-derivative formula.
- **Function inverse and reciprocal.** $1/f(x)$ denotes a reciprocal where
  $f(x)\ne0$. The expression $f^{-1}(y)$ denotes a defined inverse function.
  The inverse sine is written as $\arcsin(x)$.
- **Function powers.** The square of a sine value is written as
  $(\sin(x))^2$. The function's input and the power applied to its value
  are thereby displayed separately.
- **Matrix inverse and reciprocal.** $\mathbf A^{-1}$ denotes a matrix
  inverse when it exists. Entrywise reciprocals are defined separately;
  a matrix quotient is not part of the adopted notation.
- **Absolute value, determinant, and norm.** $|s|$ denotes the absolute
  value of a scalar $s$; $\det(\mathbf A)$ denotes the determinant of a
  square matrix; and $\lVert\mathbf v\rVert$ denotes a specified norm of
  a vector. The chosen norm is defined with its use.
- **Products.** Scalar multiplication, dot products, cross products,
  matrix products, tensor products, and contractions are identified
  when introduced. The order of matrix factors is retained. Entrywise
  products are explicitly identified.
- **Summations.** Summation signs and their limits are displayed, with
  stated ranges for free indices. Individual terms are expanded in
  initial low-dimensional examples. Implicit Einstein summation is not
  used in worked calculations.
- **Tensors and arrays.** Multilinear tensors and multidimensional data
  arrays are related through specified representations; they are not
  treated as identical objects without a definition of that relation.
- **Equality and approximation.** The symbol $=$ denotes exact equality;
  $\approx$ denotes an approximation. An approximation is accompanied
  by its validity conditions and an error estimate, or by a statement
  that no error bound has been established.

## 7. Labels and color conventions

Numbered steps identify the successive operations in worked solutions.
Their textual labels and colors distinguish the roles of those operations.

| Label | Meaning | Appearance |
|---|---|---|
| SETUP | Types, dependencies, domain, and target | Ordinary text |
| CHOICE | The reason a method applies to the given expression | Ordinary text |
| CALCULUS | A named derivative or integral rule | Ordinary mathematical text |
| ALGEBRA | Expansion, factoring, cancellation, or rearrangement | Dark blue with an ALGEBRA label |
| IDENTITY | An exact identity applied to the expression | Dark blue with an IDENTITY label |
| TRICK | A supporting identity, rewrite, or approximation from the tricks appendix | Purple with a TRICK label and an appendix reference |
| APPROXIMATION | A replacement with stated validity conditions | Dark blue with an APPROXIMATION label |
| CHECK | Verification of the result, domain, dimensions, or plausibility | Ordinary text |

Color supplements the textual labels, which remain meaningful in grayscale.
Calculus operations and algebraic simplifications are presented on separate
lines. Unsimplified expressions precede their simplified forms; factors,
signs, and conditions for cancellation are displayed explicitly.

Supporting tools from [the tricks appendix](TRICKS_APPENDIX.md) are denoted
in purple, including instances that could also be classified as identities
or approximations. Algebra in the main chapters is denoted in dark blue.
Substitution and integration by parts are classified as main calculus
methods rather than supporting tricks.

Each problem is identified by a stable code, such as D2-001. Its statement,
hints, and complete solution are presented in separate sections. Numbered
solution steps provide references to particular stages of the calculation.
