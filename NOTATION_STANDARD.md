# Calculus workbook notation standard

Status: recommended standard, version 0.2, revised October 5, 2026 after a targeted literature review. This is a consistent selection of established conventions, with explicit teaching annotations. It is not a claim that all fields use one universal notation.

## 1. Reading contract

Use **Leibniz operator notation with full arguments**, ordinary parentheses for grouping, and explicit type and dependency declarations. Avoid inventing symbols to replace established calculus notation. The literature basis and reasons for the choices are recorded in [the literature review](NOTATION_REVIEW.md).

Every problem and solution begins with four items:

1. **Objects and types:** scalar, vector with dimension, matrix with dimensions, or tensor with order, space, and component shape.
2. **Dependencies:** independent inputs, dependent outputs, intermediate functions, and fixed parameters.
3. **Domain and assumptions:** allowed inputs, excluded values, and regularity or sign conditions used.
4. **Operation and output:** what is being differentiated or integrated, with respect to which variable, what stays fixed, and the output type.

Repeat declarations in the solution so it can be read independently. Full function arguments stay visible in calculus expressions. A vector or matrix argument may be written as a single object only when its components and dependencies are displayed locally. Long expressions are split into named, fully defined steps rather than compressed into unexplained symbols.

## 2. Delimiters, types, and dependencies

### Give delimiters predictable jobs

| Notation | Meaning in this book | Safeguard |
|---|---|---|
| $f(x,y)$ | Function value at the listed inputs | Parentheses immediately after a function name contain its arguments |
| $(a+b)$ | Grouping | Larger parentheses group the entire operand of a derivative |
| A displayed bracketed column or rectangular array | Vector or matrix representation | State its type and shape; do not use a one-line tuple as an unexplained vector |
| $[a,b]$ | Closed interval | Preserve this standard meaning; in first uses also write $a\leq x\leq b$ |
| $\{x: x>0\}$ | Set | Braces are not the default grouping delimiter |
| $A_{ij}(t)$, $T_{ijk}(t)$ | Scalar components | Declare the parent object, basis, index ranges, and dependencies |

Square brackets do not universally mean “tensor.” They also conventionally denote intervals and sometimes operator arguments. Our deliberate local convention is to avoid square brackets for derivative operands and ordinary algebraic grouping. We retain them for arrays and closed intervals because changing those conventions would introduce a different confusion.

For nested grouping, use parentheses of different sizes. If a formula becomes hard to track, break it into displayed steps. Delimiters alone never determine an object's type.

### Object typography

| Object | Convention | Example declaration |
|---|---|---|
| Scalar | Ordinary italic | $x\in\mathbb R$: independent real scalar |
| Scalar-valued function | Ordinary letter, all inputs visible | $z=f(x,y)\in\mathbb R$: dependent scalar output |
| Vector | Bold lowercase | $\mathbf r(t)\in\mathbb R^3$: column vector depending on scalar $t$ |
| Matrix | Bold uppercase | $\mathbf A(t)\in\mathbb R^{m\times n}$: matrix depending on scalar $t$ |
| Tensor of order three or higher | Bold calligraphic uppercase | $\boldsymbol{\mathcal T}(t)$: tensor with declared space, order, basis, and component shape |

These typography conventions are established choices, not universal rules. Scalar entries use ordinary type: $r_i(t)$, $A_{ij}(t)$, and $T_{ijk}(t)$. Tensor order is not called tensor rank: rank has other meanings.

For this book, a function name and a function value are distinct: $f$ names the function; $f(x,y)$ supplies its inputs. We do not write $z=f$ when we mean $z=f(x,y)$.

Fixed parameters appear after a semicolon, as in $f(x;a)=ax^2$, and are also described in words. This semicolon is an organizational convention, not a different calculus operation. If a parameter starts varying, announce that fact and write its dependence explicitly.

For independent scalar coordinates $x,y$ and a dependent scalar $z=f(x,y)$, say that $x$ and $y$ vary independently. For motion along a path, display instead

$$
t\longmapsto (x(t),y(t))\longmapsto z(t)=f(x(t),y(t)).
$$

Here $t$ is the independent scalar parameter; $x(t)$ and $y(t)$ are dependent scalar coordinates; $z(t)$ is a dependent scalar output. The parenthesized coordinate pair is a point, not an undeclared column vector.

## 3. Derivatives

### One independent scalar variable

Our normal form is

$$
\frac{d}{dx}\left(f(x)\right).
$$

Read it as “differentiate the parenthesized expression with respect to $x$.” The derivative operator is not enclosed in another pair of parentheses. No prime marks, time dots, bare function names as operands, or implicit differentiation variables appear in worked calculations.

For second derivatives, use the established higher-order operator and expand it where introduced:

$$
\frac{d^2}{dx^2}\left(f(x)\right)
=
\frac{d}{dx}\left(\frac{d}{dx}\left(f(x)\right)\right).
$$

The superscript $2$ means “differentiate twice,” not “square the derivative.” Every worked higher-derivative calculation shows the intermediate first derivative. This is clearer than requiring ever-deeper nesting in every formula.

Differentiate first and evaluate second:

$$
\left.\frac{d}{dx}\left(f(x)\right)\right|_{x=a}.
$$

Always calculate the derivative before substituting the specified input.

### Several independent scalar variables

Use the established partial-derivative operator and put the held-fixed instruction beside it:

$$
\frac{\partial}{\partial x}\left(f(x,y)\right),
\qquad y\text{ held fixed}.
$$

A nearby sentence lists all other independent inputs and fixed parameters. This avoids putting a paragraph into an operator subscript. If which quantity stays fixed changes the answer, state it on each affected line. A bar with a subscript is reserved for evaluation, so it is not also used to mean “hold this variable fixed.”

Keep ordinary $d$ and partial $\partial$ distinct. Partial differentiation changes one independent coordinate while holding the others fixed. Ordinary differentiation applies when the expression has one independent scalar input, including a whole path-dependent composition.

For a differentiable scalar-valued function $f(x,y)$ and differentiable scalar paths $x(t),y(t)$, write

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

In the first partial derivative hold $y$ fixed; in the second hold $x$ fixed. Calculate each partial derivative with independent coordinates, evaluate it on the path, and only then multiply by the corresponding input rate.

Mixed partial derivatives are initially written as nested operations, with the order stated in words. Do not assume that reversing the order gives the same result without appropriate hypotheses.

### Vector and matrix outputs

For a single scalar input, differentiate component by component in a fixed basis. For example, $\mathbf r(t)$ is a two-component column vector, and $r_1(t),r_2(t)$ are scalar functions:

$$
\mathbf r(t)=\begin{bmatrix}r_1(t)\\r_2(t)\end{bmatrix},
\qquad
\frac{d}{dt}\left(\mathbf r(t)\right)
=\begin{bmatrix}
\frac{d}{dt}\left(r_1(t)\right)\\
\frac{d}{dt}\left(r_2(t)\right)
\end{bmatrix}.
$$

This separates the round derivative-operand delimiters from the square vector-display delimiters. Matrix and tensor examples likewise declare the derivative's shape.

For vector inputs, introduce named scalar coordinates first. Let $\mathbf F(x_1,\ldots,x_n)\in\mathbb R^m$ be differentiable. Its Jacobian is the $m\times n$ matrix with scalar entries

$$
J_{ij}(x_1,\ldots,x_n)
=\frac{\partial}{\partial x_j}\left(F_i(x_1,\ldots,x_n)\right).
$$

All $x_k$ with $k\ne j$ are held fixed. Index $i$ selects an output, $1\leq i\leq m$; index $j$ selects an input, $1\leq j\leq n$. In concrete examples list the actual coordinates instead of using ellipses.

For a differentiable scalar function $f(x,y)$ in ordinary Euclidean coordinates, define the gradient explicitly:

$$
\nabla f(x,y)=
\begin{bmatrix}
\frac{\partial}{\partial x}\left(f(x,y)\right)\\
\frac{\partial}{\partial y}\left(f(x,y)\right)
\end{bmatrix}.
$$

Hold the other coordinate fixed in each entry. The gradient is a column vector; the scalar function's Jacobian is its transpose, a one-row matrix. We do not use an unexplained fraction “with respect to a vector” for both objects. The superscript $\mathsf T$ means transpose, never a derivative.

### Matrix inputs and tensor inputs

Start with derivatives with respect to individual scalar entries. For a scalar function $\phi(\mathbf A)$ of a real $m\times n$ matrix with independently variable entries, the matrix gradient $\nabla_{\mathbf A}\phi(\mathbf A)$ has the same shape as $\mathbf A$. Its $(i,j)$ entry is the scalar partial derivative with respect to $A_{ij}$, holding all other entries fixed. If the matrix is symmetric or otherwise constrained, identify its independent parameters before differentiating; its entries cannot all be treated as independent.

For a general differentiable matrix-valued function $\mathbf F(\mathbf A)$, use the established derivative-map form $\mathrm D\mathbf F(\mathbf A)(\mathbf H)$ after defining it: it is the derivative at input $\mathbf A$, applied to the increment matrix $\mathbf H$. Declare both matrices' shapes, the output shape, and all parameters. This is a linear map applied to an increment, not matrix division. The final parentheses replace the square argument brackets used in some references.

Tensor calculations specify the tensor space, basis, component indices, and index ranges. For geometric tensors, upper and lower indices have distinct roles and must be explained; no implicit summation is allowed. Fixed-basis component differentiation is introduced first. Moving bases require additional terms.

## 4. Integrals

Use the usual definite-integral form:

$$
\int_a^b f(x)\,dx.
$$

Immediately identify $x$ as the scalar integration variable, with lower limit $x=a$ and upper limit $x=b$. The differential $dx$ remains on every integral. Parentheses group a sum when needed; a simple integrand does not need an extra wrapper. We do not routinely write $x=$ inside the bounds: the nearby variable-and-bounds statement supplies that clarity while keeping the expression familiar.

The symbol $x$ inside a definite integral is a bound integration variable. If the bounds are fixed and there are no other inputs, the result is a scalar number, not a function of $x$.

For an indefinite integral on an appropriate interval,

$$
\int f(x)\,dx=F(x)+C,
\qquad \frac{d}{dx}\left(F(x)\right)=f(x).
$$

Here $C$ is an arbitrary scalar constant independent of $x$. For vector and matrix outputs, the arbitrary constant has the output's shape.

With other inputs held fixed,

$$
\int f(x,y)\,dx=F(x,y)+C(y),\qquad y\text{ held fixed}.
$$

The integration constant may depend on the input that was not integrated over. Definite integration over $x$ can likewise leave a function of $y$.

Write endpoint evaluation without another set of square brackets:

$$
\left.F(x)\right|_{x=a}^{x=b}=F(b)-F(a).
$$

Always show the subtraction. For multiple integrals, specify the order in words and give each integral its own bounds and differential. For curve, surface, and volume integrals, specify domain, measure, parameterization when used, and orientation when relevant. Arc length $ds$, surface area $dS$, and a vector displacement are different objects, each introduced with a definition and component formula.

## 5. Substitution without hidden steps

Introduce scalar functions $g(x)$ and $h(u)$ and a new scalar coordinate $u=g(x)$. Before the substitution, $u$ depends on $x$; in the transformed integral, $u$ is the integration variable.

For continuously differentiable $g$ on $[a,b]$ and continuous $h$ on an interval containing its image,

$$
\int_a^b h(g(x))\frac{d}{dx}\left(g(x)\right)\,dx
=\int_{g(a)}^{g(b)}h(u)\,du.
$$

On the left, integrate over $x$ from $a$ to $b$. On the right, integrate over $u$ from $g(a)$ to $g(b)$. This form does not require an inverse for $g$. A substitution using an inverse may need domain restrictions and a branch choice.

Required steps: define the substitution; compute its derivative; match every factor; transform both bounds; write the complete new integral; evaluate; check. For indefinite integration, substitute back and verify by differentiation.

Differential notation such as $du=2x\,dx$ is conventional, not inherently invalid. We teach its meaning before using it: when $u=g(x)=x^2+1$, the differential of $u$ is the derivative of $g(x)$ multiplied by the differential of $x$. In early worked solutions the full substitution formula remains visible. Never present canceling the letters $d$ and $x$ as a proof, and never divide by a possibly zero derivative without justification.

## 6. Other notation collisions to prevent

- **Finite change versus differential:** $\Delta x$ is a finite scalar increment. A differential gives the linear part of a change; it is not automatically the exact finite change. Introduce $\mathrm Df(x,y)(\Delta x,\Delta y)$ by its full partial-derivative formula before using it.
- **Function inverse versus reciprocal:** write $1/f(x)$ for a reciprocal and $f^{-1}(y)$ only for a defined inverse function. Use $\arcsin(x)$ rather than $\sin^{-1}(x)$.
- **Function powers:** write $(\sin(x))^2$, not the compressed $\sin^2 x$. Every elementary function shows its input.
- **Matrix inverse versus reciprocal:** $\mathbf A^{-1}$ is a matrix inverse when it exists; entrywise reciprocals are defined separately. Do not use matrix “division.”
- **Absolute value versus determinant:** use $|s|$ for a scalar absolute value, $\det(\mathbf A)$ for a determinant, and $\lVert\mathbf v\rVert$ for a vector norm. Define the chosen norm.
- **Products:** scalar multiplication, vector dot products, cross products, matrix products, tensor products, and contractions are named when introduced. Matrix factors retain their order. Entrywise products are explicitly identified.
- **Summations:** write every summation sign and its limits. State free-index ranges. Expand all terms in first small examples. Einstein summation is explained in the translation guide only.
- **Tensor meaning:** multilinear tensors and multidimensional data arrays are related through chosen representations but are not silently treated as identical concepts.
- **Equality versus approximation:** use $=$ for exact equality and $\approx$ for approximation. State the approximation's conditions and error estimate, or explicitly say that no error bound has been established.

## 7. Worked-solution presentation

Every solution uses numbered steps and textual labels:

| Label | Meaning | Planned print styling |
|---|---|---|
| SETUP | Types, dependencies, domain, target | Normal text |
| CHOICE | Why this method applies; cues to recognize it | Normal text |
| CALCULUS | Derivative or integral rule being applied | Black math with a named rule |
| ALGEBRA | Expansion, factoring, cancellation, solving, rearrangement | Dark blue `#244A73` with an ALGEBRA label |
| IDENTITY | Trigonometric, exponential, logarithmic, or other exact identity | Same dark blue with an IDENTITY label |
| APPROXIMATION | A deliberately approximate replacement | Same dark blue with an APPROXIMATION label and conditions |
| CHECK | Verification, dimensions, units, domain, or plausibility | Normal text |

Color is supplementary: the labels survive grayscale printing and text-only tutoring. Do not make algebra light gray or low contrast. Markdown pilot files use the labels; the typeset book will apply the color styles centrally.

Separate calculus from algebra into distinct lines. Give the unsimplified result before simplifying. Explain each factor, sign, and canceled term. State conditions for division and cancellation. Name an identity and show its general form before substituting the problem's expressions.

Each problem has a stable ID, a problem-only prompt, a graduated hint ladder, a separate complete solution, a verification, a method-recognition note, and a nearby practice variant. Solutions must not sit beside the question in the final page layout.

## 8. Tutor contract

When asked to help with a problem, the tutor uses its ID and this standard. Begin at the learner's last understood step, ask for one manageable next action, and wait. Explain a needed prerequisite locally. Do not skip algebra or switch notation to save space. Give the full solution when requested; otherwise reveal only the next requested hint or step. A valid alternative method is welcome if its assumptions and dependencies are equally explicit.

## 9. Editorial acceptance checklist

- Can the reader identify every object's type and every function input locally?
- Is the differentiation/integration variable explicit, including what is held fixed?
- Are intermediate dependencies, bounds, domains, and arbitrary constants correct?
- Is each equation exact, or explicitly marked approximate?
- Are calculus rules distinguished from algebra and identities?
- Can every transition be reproduced without a hidden manipulation?
- Is there a check appropriate to the problem and a cue explaining the method choice?
- Do the question, hints, and solution share one stable problem ID?
