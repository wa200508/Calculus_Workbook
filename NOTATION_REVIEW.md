# Literature review and notation decisions

Reviewed October 5, 2026. Scope: selected introductory calculus textbook sections, a university matrix-calculus course, a matrix-calculus reference, a tensor survey, and continuum-mechanics notes. This is a targeted notation review, not an exhaustive survey or a study demonstrating that one notation improves learning for everyone.

## Recommendation

Use established Leibniz operator notation with round grouping parentheses and complete function arguments. Pair it with local type declarations, dependency statements, and explicit held-fixed instructions. The symbols should transfer to other books; the extra explanation should reduce reliance on memory.

The recommendation is an editorial judgment tailored to this reader. The references establish usage and mathematical distinctions, not a uniquely “best” personal notation.

## Findings and decisions

### R1 — Ordinary derivatives

OpenStax explicitly lists the operator form $\frac{d}{dx}\left(f(x)\right)$ alongside prime and quotient-style notation. It also discusses higher derivatives. **Decision:** adopt that operator form; retain $d^2/dx^2$ with an initial nested expansion. Prime and dot notation belong in a translation guide, not worked calculations. [OpenStax, Calculus Volume 1, §3.2](https://openstax.org/books/calculus-volume-1/pages/3-2-the-derivative-as-a-function).

### R2 — Partial derivatives

OpenStax defines partial derivatives by changing one coordinate while the other stays fixed, and uses both fraction and subscript notation. **Decision:** retain the standard partial symbol, show all function arguments, and state the held-fixed inputs in nearby text. Our insistence on repeating the instruction is a teaching convention. [OpenStax, Calculus Volume 3, §4.3](https://openstax.org/books/calculus-volume-3/pages/4-3-partial-derivatives).

### R3 — Dependencies and the chain rule

OpenStax's multivariable chain rule distinguishes independent, intermediate, and dependent variables and uses dependency trees. **Decision:** show $z(t)=f(x(t),y(t))$ explicitly and show where each partial derivative is evaluated. A partial derivative in independent coordinates must not be confused with a derivative along a path. [OpenStax, Calculus Volume 3, §4.5](https://openstax.org/books/calculus-volume-3/pages/4-5-the-chain-rule).

### R4 — Substitution and integrals

OpenStax uses ordinary integral bounds and differentials, supplies a definite-substitution theorem, and demonstrates changing endpoints. **Decision:** use conventional integral notation with an adjacent variable-and-bounds statement. Explain differential identities before using them. Our earlier blanket exclusion of differential notation was unnecessarily restrictive; fully explained notation can remain standard. [OpenStax, Calculus Volume 1, §5.5](https://openstax.org/books/calculus-volume-1/pages/5-5-substitution).

### R5 — Gradients, Jacobians, and derivative maps

MIT's course treats derivatives as linear operators. For a map from $n$ inputs to $m$ outputs, the Jacobian is $m\times n$. For a scalar output in Euclidean coordinates, the gradient is a column vector and the derivative is represented by its transpose. **Decision:** keep these objects distinct, explicitly state shapes, and introduce derivative maps for general matrix-valued functions. We choose $\mathrm D$ instead of the course's prime notation, with round parentheses for the increment argument. [MIT 18.S096, Lecture Notes and Readings, Lecture 1](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/pages/lecture-notes-and-readings/).

### R6 — Matrix derivatives and constraints

The Matrix Cookbook defines a scalar function's matrix derivative through derivatives with respect to entries. Its structured-matrix section distinguishes constrained entries from independent entries. **Decision:** show entry derivatives first, specify the matrix-gradient shape, and name independent parameters for constrained matrices. Do not import an unexplained matrix derivative fraction from another source. [Petersen and Pedersen, The Matrix Cookbook, November 15, 2012, §§2 and 2.8](https://math.uwaterloo.ca/~hwolkowi/matrixcookbook).

### R7 — Tensor typography and index meaning

Kolda and Bader use bold lowercase vectors, bold uppercase matrices, and bold script higher-order tensors, with ordinary scalar component symbols. They distinguish order from rank and note alternative conventions. **Decision:** adopt that visual distinction, using the available bold calligraphic font, while explicitly declaring tensor spaces and bases when discussing geometric tensors. Typography alone cannot explain the object. [Kolda and Bader, Tensor Decompositions and Applications, SIAM Review 51(3), 2009, §2](https://www.kolda.net/publication/TensorReview.pdf).

### R8 — Summation shorthand

Stanford continuum-mechanics notes place explicit sums beside their Einstein-convention equivalents and expand the component equations. **Decision:** retain explicit sums and limits in our solutions; teach the implicit convention only as a way to read outside references. This is an intentional accessibility choice within ordinary mathematics. [Stanford ME338A, Continuum Mechanics, Lecture Notes 01, §1.1.1.1](https://biomechanics.stanford.edu/me338/me338_n01.pdf).

## Delimiter and symbol policy

These are editorial decisions informed by the review:

- Round parentheses group derivative operands. Square brackets display vectors and matrices. Closed intervals retain their conventional square brackets, with endpoint inequalities spelled out when introduced.
- Tensor components use declared indices. Square brackets are not a universal tensor marker.
- Ordinary integrands do not receive decorative wrappers. Group sums only where grouping clarifies the expression.
- Evaluation bars mean substitution at specified inputs. “Held fixed” appears in words, so those two instructions cannot be mistaken for one another.
- Use $\arcsin(x)$ for the inverse sine and $1/\sin(x)$ for its reciprocal. Use $(\sin(x))^2$ to expose a function power.
- Use $\det(\mathbf A)$ for a determinant and absolute-value bars for scalar magnitude.
- A short translation guide will expose outside shorthand without changing the notation used in the book's worked steps.

## Changes from version 0.1

Round derivative operands replace square operands; redundant parentheses around the operator are removed. Ordinary integral bounds replace variable-tagged bounds, with explicit endpoint statements retained in prose. Held-fixed prose replaces bulky operator subscripts. Higher-order operator notation is taught through expansion rather than excluded. Differential substitution notation is explained rather than treated as intrinsically suspect. The new standard also addresses inverse, norm, determinant, index, and shape ambiguities.
