# Literature review and notation decisions

Reviewed October 5, 2026. Scope: selected introductory calculus textbook sections, a university matrix-calculus course, a matrix-calculus reference, a tensor survey, and continuum-mechanics notes. This is a targeted notation review, not an exhaustive survey or a study demonstrating that one notation improves learning for everyone.

## Conventions adopted in this book

The book uses Leibniz derivative operators with round parentheses and complete
function arguments. Nearby definitions state the object types, dependencies, and
quantities held fixed. These choices preserve familiar mathematical symbols while
making less of their interpretation depend on memory or surrounding context.

The references document established usage and distinctions between mathematical
objects. The choice among compatible conventions is editorial; there is no single
notation that serves every discipline or every reader equally well.

## Findings and decisions

### R1 — Ordinary derivatives

OpenStax explicitly lists the operator form $\frac{d}{dx}\left(f(x)\right)$ alongside prime and quotient-style notation. It also discusses higher derivatives. The operator form is adopted here. Higher derivatives retain $d^2/dx^2$, with a nested expansion at their first appearance. Worked calculations use this notation consistently in place of primes and dots. [OpenStax, Calculus Volume 1, §3.2](https://openstax.org/books/calculus-volume-1/pages/3-2-the-derivative-as-a-function).

### R2 — Partial derivatives

OpenStax defines partial derivatives by changing one coordinate while the other stays fixed, and uses both fraction and subscript notation. The book retains the partial derivative symbol, includes the function arguments, and states nearby which inputs are held fixed. Repeating that information makes each calculation easier to read independently. [OpenStax, Calculus Volume 3, §4.3](https://openstax.org/books/calculus-volume-3/pages/4-3-partial-derivatives).

### R3 — Dependencies and the chain rule

OpenStax's multivariable chain rule distinguishes independent, intermediate, and dependent variables and uses dependency trees. The dependence $z(t)=f(x(t),y(t))$ and the evaluation points of the partial derivatives are displayed here. This distinguishes differentiation in an independent coordinate from differentiation along a path. [OpenStax, Calculus Volume 3, §4.5](https://openstax.org/books/calculus-volume-3/pages/4-5-the-chain-rule).

### R4 — Substitution and integrals

OpenStax uses ordinary integral bounds and differentials, supplies a definite-substitution theorem, and demonstrates changing endpoints. Conventional integral bounds and differentials are retained here. The variable and bounds are described in the accompanying statement, and differential identities are explained when introduced. [OpenStax, Calculus Volume 1, §5.5](https://openstax.org/books/calculus-volume-1/pages/5-5-substitution).

### R5 — Gradients, Jacobians, and derivative maps

MIT's course treats derivatives as linear operators. For a map from $n$ inputs to $m$ outputs, the Jacobian is $m\times n$. For a scalar output in Euclidean coordinates, the gradient is a column vector and the derivative is represented by its transpose. The gradient, Jacobian, and derivative map are distinguished here by their definitions and shapes. The derivative map is denoted by $\mathrm D$, with round parentheses around its increment argument. [MIT 18.S096, Lecture Notes and Readings, Lecture 1](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/pages/lecture-notes-and-readings/).

### R6 — Matrix derivatives and constraints

The Matrix Cookbook defines a scalar function's matrix derivative through derivatives with respect to entries. Its structured-matrix section distinguishes constrained entries from independent entries. Entry derivatives and the shape of the matrix gradient are stated before a compact matrix formula is used. When entries are constrained, the independent parameters are named separately. [Petersen and Pedersen, The Matrix Cookbook, November 15, 2012, §§2 and 2.8](https://math.uwaterloo.ca/~hwolkowi/matrixcookbook).

### R7 — Tensor typography and index meaning

Kolda and Bader use bold lowercase vectors, bold uppercase matrices, and bold script higher-order tensors, with ordinary scalar component symbols. They distinguish order from rank and note alternative conventions. The same visual distinction is adopted here with a bold calligraphic font. Geometric tensors also have declared spaces and bases, since typography alone does not specify the object. [Kolda and Bader, Tensor Decompositions and Applications, SIAM Review 51(3), 2009, §2](https://www.kolda.net/publication/TensorReview.pdf).

### R8 — Summation shorthand

Stanford continuum-mechanics notes place explicit sums beside their Einstein-convention equivalents and expand the component equations. Worked solutions retain the summation signs and limits. This makes each contraction visible even to a reader who does not routinely use the Einstein convention. [Stanford ME338A, Continuum Mechanics, Lecture Notes 01, §1.1.1.1](https://biomechanics.stanford.edu/me338/me338_n01.pdf).

## Delimiter and symbol policy

These are editorial decisions informed by the review:

- Round parentheses group derivative operands. Square brackets display vectors and matrices. Closed intervals retain their conventional square brackets, with endpoint inequalities spelled out when introduced.
- Tensor components use declared indices. Square brackets are not a universal tensor marker.
- Ordinary integrands retain their usual notation. Parentheses group terms when needed to make the expression unambiguous.
- Evaluation bars mean substitution at specified inputs. The quantities held fixed are described in words, distinguishing that information from evaluation at a point.
- The inverse sine is $\arcsin(x)$; the reciprocal of the sine is $1/\sin(x)$. A square of the sine is written as $(\sin(x))^2$ or the conventional $\sin^2(x)$.
- Determinants are written as $\det(\mathbf A)$, while absolute-value bars denote scalar magnitude.

