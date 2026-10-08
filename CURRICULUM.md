# Curriculum proposal

The book is a review and problem-solving manual. Short concept refreshers support worked problems; readers are not expected to remember a formula or an algebraic manipulation merely because they once took a class.

The two main parts are **Differentiation and differentials** and **Integration**. Within each part, complexity grows from scalar variables and outputs to vector, matrix, and tensor objects. Input dimension and integration geometry form a second organizing axis: an object's type alone does not determine the calculus method.

## Entry toolkit: how to read and use the book

1. The notation standard, dependency diagrams, types, shapes, domains, and units.
2. A diagnostic set for fractions, powers, roots, logarithms, exponentials, factoring, completing the square, equations, inequalities, and trigonometry.
3. A referenced toolbox of exact identities and approximation rules. Each entry has conditions, a worked example, and links to problems using it.
4. Essential reminders about limits, continuity, and what a derivative or integral asks for. Revisit limits later where a method needs them.

Diagnostic results direct readers to local refreshers; they do not block access to calculus chapters.

## Part I: Differentiation and differentials

| Chapter | Scope | Problem-solving focus |
|---|---|---|
| D1 | Scalar input, scalar output | Read dependencies; use elementary, sum, and constant-multiple rules; check from the definition in selected examples |
| D2 | Products, quotients, and compositions | Recognize structure; choose whether to simplify first; fully expose the chain rule |
| D3 | Implicit, inverse, and parametric relationships | Decide what depends on what; solve for a requested rate; handle logarithmic differentiation and domain restrictions |
| D4 | Higher derivatives, local approximation, and optimization | Repeated operations, linearization, Taylor polynomials with errors, critical points, and endpoint checks |
| D5 | Several scalar inputs, scalar output | Partial derivatives, gradients, directional derivatives, Hessians, tangent approximations, and constrained optimization |
| D6 | Vector outputs and vector inputs | Velocity and acceleration; Jacobians; multivariable compositions; derivative as a linear map |
| D7 | Matrix inputs and outputs | Entrywise time derivatives; products and inverses; scalar functions of matrices; explicit index conventions and shape checks |
| D8 | Tensor-valued functions and contractions | Fixed-basis component derivatives; multilinear structure; tensor products and contractions; careful separation of tensor meaning from array storage |

An optional extension follows D8: changing bases, curvilinear coordinates, and covariant derivatives. This is a separate prerequisite-bearing topic, not a silent extension of componentwise differentiation.

## Part II: Integration

| Chapter | Scope | Problem-solving focus |
|---|---|---|
| I1 | Scalar antiderivatives and definite integrals | Meaning, fundamental theorem, bounds, constants, signed accumulation, and basic rules |
| I2 | Change of variable in one dimension | Recognize a composition and its derivative; transform bounds; handle inverse branches and domain restrictions |
| I3 | Integration by parts | Choose factors; expose product-rule origins; repeat operations and solve for a recurring integral |
| I4 | Algebraic and trigonometric methods | Polynomial division, partial fractions, completing the square, trig identities, and trig substitution |
| I5 | Choosing a method for unfamiliar integrals | Mixed practice without method labels; compare valid routes; recognize when elementary antiderivatives are unavailable |
| I6 | Improper integrals and numerical approximation | Limits at singularities and infinity; convergence before evaluation; quadrature and error bounds |
| I7 | Vector, matrix, and tensor outputs over a scalar variable | Component integrals; initial conditions; shape preservation; fixed-basis assumptions and limits of componentwise reasoning |
| I8 | Double and triple integrals | Regions, bounds, order changes, signed and nonnegative integrands, and conditions for interchanging integrals |
| I9 | Multivariable changes of coordinates | Jacobian determinants, absolute values, transformed regions, polar/cylindrical/spherical examples |
| I10 | Curves: scalar accumulation and vector work | Parameterizations, arc-length measure, tangents, orientation, and distinguishing two kinds of line integral |
| I11 | Surfaces: scalar accumulation and vector flux | Surface measure, normal direction, parameterization, and orientation |
| I12 | Connecting local derivatives with global integrals | Green's, divergence, and Stokes' theorems; choose the easier side and check hypotheses |
| I13 | Integrals depending on parameters and mixed objects | Differentiate under an integral with stated conditions; vector/matrix/tensor integrands over regions; explicit contractions |

Optional advanced extensions: differential forms and generalized Stokes; integration on manifolds; matrix exponentials and systems of differential equations; higher-order tensors in applications. These are scoped separately so the core review remains usable.

## Dependencies and reading routes

- The quickest scalar review is D1–D4 followed by I1–I6.
- I2 uses the chain rule from D2; I3 uses the product rule from D2.
- I7 can follow the scalar integration chapters once component notation is understood.
- I8 needs scalar integration and elementary multivariable functions; I9 also needs the Jacobian from D6 and determinant algebra.
- I10–I12 draw on D5–D6 and the relevant integration chapters. Introduce divergence and curl explicitly before their theorems.
- D7–D8 and the tensor portions of I7/I13 have short linear-algebra prerequisite modules. Their unfamiliar concepts are taught locally rather than assumed.

## Repeated chapter structure

1. A short concept refresher and a “what can vary?” map.
2. A rule sheet using only the book's notation, with conditions and output types.
3. Fully worked anchor problems, starting with a single new idea.
4. Near-transfer practice: a changed sign, exponent, bound, dependency, or dimension.
5. Mixed problems with the method name withheld.
6. Failure-analysis problems: diagnose a plausible wrong step.
7. A method-selection page: cues, necessary checks, and common dead ends.
8. Hints and full solutions in separate, clearly indexed sections.

Every practice problem will have a complete solution. Every approximation will identify its regime of validity. Checks include reverse differentiation for antiderivatives, shape and unit checks where applicable, and independent evaluations when useful.

The eventual book should provide both a printable reading experience and stable problem/step references suitable for an LLM tutor. First settle the notation using the pilots, then develop one representative scalar chapter before expanding to the remaining chapters.
