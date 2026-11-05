# Reference audit, November 5, 2026

Reviewer: Codex agent `/root/audit_references`. Baseline: commit `8963e97`.
Scope: the complete notation chapter, methods reference, quick reference,
supporting-tools appendix, and notation literature review. This is an analytical
review of the stated formulas and hypotheses. It is not external reader feedback
or a certification of every linked source. Root integration records the final
revision, generated-source checks, and PDF layout checks separately.

## Findings and corrections

No wrong coefficient, sign, elementary primitive, matrix-factor order, or
hyperbolic inverse branch was found in these references. The corrections concern
conditions under which the formulas are valid and a distinction between chart
identification and coordinate degeneracy:

1. **Methods reference, paths and partial derivatives.** The chain-rule statement
   assumed only a scalar field and a differentiable path. It now assumes the
   field is differentiable at the path point. Existence of coordinate partials
   alone does not suffice. For example, define
   $f(x,y)=x^3/(x^2+y^2)$ away from the origin and $f(0,0)=0$.
   At the origin the coordinate partials are $1$ and $0$. On the differentiable
   path $(x(t),y(t))=(t,t)$, however, $f(t,t)=t/2$, whose derivative is $1/2$.
   Substitution of the partials into the chain-rule right-hand side would give
   $1$. The omitted differentiability hypothesis is therefore substantive.
2. **Methods reference, termwise integration.** Uniform convergence on a finite
   interval was stated without a condition making the summands integrable. The
   sufficient condition is now a series of continuous functions on a finite
   closed interval. For instance, the series with first term $1/x$ on $(0,1]$
   (assigned value zero at zero) and all subsequent terms zero converges
   uniformly to its first term on $[0,1]$, but has no finite integral. Uniform
   convergence alone cannot establish the integrals in the claimed operation.
3. **Both references, parameter differentiation.** The required known integrable
   parameter slice is now explicitly inside the same neighborhood where the
   derivative domination and differentiability hold. A known integral at an
   unrelated parameter cannot establish local existence. For example, let
   $q(x,t)=c(t)/x$ on $0<x<1$, with smooth $c(t)=1$ near $t=0$ and $c(t)=0$
   near $t=2$. The parameter derivative is zero near zero, yet the integrals
   there diverge; integrability at $t=2$ is irrelevant. With an integrable slice
   in the neighborhood, the mean-value bound
   $|q(x,t)-q(x,t_*)|\le |t-t_*|M(x)$ supplies local integrability and the
   dominated difference-quotient argument.
4. **Composition and quick-reference chain rules.** Local differentiability
   assumptions are made explicit beside the formulas: the inner scalar map,
   both scalar path components, and the vector field in the Jacobian path
   rule. The quick reference's introductory differentiability convention already
   supplies a general safeguard; these changes make each entry's sufficient
   hypotheses visible locally. Taking an identity outer map and inner
   $g(x)=|x|$ shows why inner differentiability matters.
5. **Quick-reference logarithmic differentiation and multipliers.** Local
   differentiability of the scalar function is now stated; the objective and
   constraint are both assumed continuously differentiable nearby. Regularity
   of the single constraint is spelled out as
   $\nabla c\ne0$. The previous phrase "regular constrained" already excluded
   a vanishing constraint gradient; this is an explicit clarification of that
   condition. For example, the constraint $x^2+y^2=0$ admits only the origin,
   but the objective $f(x,y)=x$ cannot satisfy a multiplier equation there.

6. **Methods reference, coordinate measures.** An angular seam is an
   identification of chart edges, whereas a pole can be a degeneracy of the
   coordinate Jacobian. The text now distinguishes them rather than calling
   both degeneracies. Measure-zero edges do not excuse interior multiple
   coverage. For example, $\mathbf r(u,v)=(\cos v,\sin v,u)$ is regular
   even along $v=0$, while $v=0$ and $v=2\pi$ represent the same seam.

The quick reference retains its independent conventions, equations, column
markers, and section structure. Its four-page PDF layout must be checked after
generation; it is not inferred from the small source-text changes.

## Notation chapter

| Sections reviewed | Analytical checks and result |
|---|---|
| Objects, domains, dependencies | Scalar/vector/matrix/tensor declarations and independent versus fixed quantities are consistent; a matrix argument does not imply independent entries when a structure is imposed. |
| Delimiters and typography | Function values, operands, arrays, intervals, transpose, and tensor order/rank are distinguished consistently. No mathematical correction required. |
| Scalar and higher derivatives | The second-derivative operator expands as two successive derivatives, and evaluation is performed afterward. |
| Partial and path derivatives | The displayed path rule assumes a differentiable field and path, evaluates each partial on the path, and retains both coordinate rates. Mixed-partial equality is correctly conditional. |
| Vector and matrix outputs | The Jacobian shape is output-by-input; a scalar function's derivative row is the transpose of its Euclidean gradient column. Component differentiation is correctly restricted to a fixed basis. |
| Matrix and tensor inputs | Entry gradients have the original matrix shape; constrained entries require separate parameters; the derivative map is linear in its increment. Varying bases require basis derivatives. |
| Integrals | Bound variables, endpoint subtraction, output-shaped constants, and the possible dependence of constants on other coordinates are correct. A primitive is asserted only where one exists. |
| Substitution | The direct theorem assumes a continuously differentiable coordinate map and continuous outer integrand on the image interval; an inverse is unnecessary. For $g(x)=x^2$, $h(u)=1$, and bounds $-1,1$, both sides correctly vanish despite the fold. |
| Related symbols and remainders | Scalar magnitude, determinant, norm, inverse, and reciprocal are distinguished. The warning against differentiating a value-only remainder is correct: $r(x)=x^2\sin(1/x^2)$ is $O(x^2)$ but its derivative contains an unbounded $-2\cos(1/x^2)/x$ term. |
| Labels | Color labels carry textual meanings and do not assert mathematical hypotheses by themselves. |

## Methods and quick-reference formulas

| Area | Derivation or independent check |
|---|---|
| Powers, reciprocal, exponential, logarithmic, trigonometric primitives | Differentiating every listed primitive recovers its integrand; the exceptional exponent $p=-1$, logarithm components, and tangent poles are stated. The $x>0$ power domain is a sufficient convention for arbitrary real exponents. |
| Hyperbolic functions | Definitions using exponentials give the derivatives and $\cosh^2x-\sinh^2x=1$; $\cosh x>0$ makes the primitive $\ln(\cosh x)$ real everywhere. |
| Inverse derivatives | Differentiating the defining identities on their stated real branches gives the listed square-root signs. Arcosh has derivative only for $x>1$; artanh uses $|x|<1$; the logarithmic primitive of $1/(1-x^2)$ also works on the two exterior components. |
| Linearity/product/quotient rules | The quotient numerator has the correct subtraction order and denominator square. Fixed coefficients remain fixed. |
| Compositions and variable powers | Differentiating $\exp(b(x)\ln(a(x)))$ retains both varying factors and requires $a(x)>0$. The derivative of $\ln|f|$ is the same on each nonzero real component. |
| Phase | Writing $H=r\exp(i\phi)$ gives $H^{-1}dH/d\omega=r^{-1}dr/d\omega+i\,d\phi/d\omega$. Taking the imaginary part gives the quick-reference rule. A zero or branch jump is excluded. |
| Implicit functions | Differentiation of $F(x,y,g(x,y))=0$ gives the stated minus sign and denominator. Nonzero $F_z$ is a sufficient local graph condition, not a requirement that every chart remain valid. |
| Paths and mixed partials | Both scalar and vector rules follow from a differentiable derivative map applied to the path tangent; the repaired local assumptions are recorded above. Continuous second partials are a valid sufficient interchange condition. |
| Endpoint derivatives | A continuous extension does not establish differentiability. The prescribed one-sided or two-sided difference quotient supplies the appropriate test. |
| Direct and inverse substitution | The chain-rule version does not require injectivity; an inverse-coordinate map needs a branch, derivative factor, and orientation. Turning points cannot be erased by equating transformed bounds. |
| Integration by parts | Integration of $d(uv)/dx$ gives the displayed boundary signs. Infinite-interval boundary terms require limits independently of the integrand's decay. |
| Rational decomposition | Polynomial division and repeated real linear/quadratic factors are correctly described; real logarithms retain absolute values and excluded denominator zeros. |
| Trigonometric/hyperbolic coordinates | With $u=\tan(x/2)$, the rational sine/cosine expressions and inverse derivative $2/(1+u^2)$ are correct on an angular chart. Quadratic roots retain $\sqrt{q^2}=|q|$. |
| Symmetry | Odd/even simplifications require an integrable symmetric domain. Principal values are correctly distinguished from ordinary improper limits. |
| Fundamental theorem and moving endpoints | Both endpoint rates and the interior parameter derivative appear, with a minus sign at the lower endpoint even for reversed bounds. Stated continuity near the finite region is sufficient. |
| Parameter differentiation | Integrable local derivative domination justifies difference quotients once an integrable slice in the same neighborhood is specified. A constant obtained by integrating back may depend on other fixed parameters. |
| Improper convergence and principal values | The local power thresholds $p<1$ at zero and $p>1$ at infinity follow from the primitive of $x^{-p}$. The single-pole principal value uses equal cutoffs and does not imply two separate finite one-sided limits. |
| Oscillation and damping | The text requires a separate damping-removal argument and does not claim absolute domination at a conditionally convergent endpoint. Stationary-phase and contour methods remain explicitly conditional. |
| Limits and sums | Dominated/monotone convergence, Tonelli, and absolute-integrability Fubini are described with their essential hypotheses. Continuous summands on a closed finite interval make the uniform-series integration statement sufficient. |
| Series and Taylor remainder | The expansions of exponential, sine, cosine, logarithm, and arctangent have the correct coefficients and orders. The Taylor bound follows by bounding the integral remainder, or by the Lagrange remainder under the stated continuous-derivative assumption. |
| Gradient/Jacobian/Hessian | Declared shapes and index orders are consistent. The Hessian entry convention is explicit, so symmetry is not assumed when second partials fail to commute. |
| Measures | Scalar area/volume uses an absolute determinant; flux uses an oriented cross product. A path tangent and its norm correctly distinguish vector work from scalar arc length. Seams and multiplicity are discussed. |
| Integral theorems | The divergence formula has the outward normal and a field smooth on a neighborhood of the volume. Excluded sources require excision and an oriented inner boundary. |
| Matrix and tensor operations | Differentiating $AA^{-1}=I$ on the left by $A^{-1}$ yields $d(A^{-1})/dt=-A^{-1}(dA/dt)A^{-1}$. Multiplication by fixed $b$ gives the solve derivative without commuting factors. Fixed-basis component integration and varying-basis corrections are correctly distinguished. |

## Supporting-tools appendix

| Entry | Checked reasoning and result |
|---|---|
| T-001 Euler identities | Addition/subtraction of conjugate exponentials gives sine and cosine; squaring the exponential and equating real/imaginary parts gives the double-angle formulas. Every sign is correct. |
| T-002 Taylor | The coefficients, factorials, and stated differentiability/remainder assumptions are consistent. The sine example is a fourth-order polynomial with zero fourth-order coefficient; $P_4(1/10)=599/6000$ and the fifth-derivative bound is $1/12{,}000{,}000$. Geometric/logarithm/arctangent series retain their convergence conditions. |
| T-003 Binomial | Coefficients $1,3,3,1$ recover the shifted cubic. The finite identity is restricted to nonnegative integer degree, so no convergence issue is introduced. |
| T-004 Completing the square | Expansion of $a(x+b/(2a))^2+c-b^2/(4a)$ recovers $ax^2+bx+c$. The worked example has minimum $3$ at $x=2$. |
| T-005 Rationalization | The nonzero conjugate multiplier is justified on the stated domain, and cancellation preserves $x\ne0$. The extended value is distinguished from the original function. |
| T-006 Logarithms | All real product/quotient/power rewrites require positive arguments. The negative-input version correctly uses $\ln|x|$. Complex branch qualifications are retained. |
| T-007 Hyperbolic branches | Exponential definitions verify all three identities. Positive $\cosh$ resolves the root; arsinh is real on all real inputs and arcosh selects the nonnegative branch for inputs at least one. |

## Literature and authoring consistency

The R1--R8 notation decisions agree with the definitions adopted in the notation
chapter: operator rather than prime notation; independent partial coordinates;
explicit path dependencies; conventional integral bounds; output-by-input
Jacobians; entry derivatives with constrained inputs identified; tensor order
distinguished from rank; and explicit sums. The delimiter policy permits the
conventional $\sin^2(x)$ as well as $(\sin(x))^2$, consistent with existing
formulas. The authoring checklist correctly requires types, dependencies,
domains, intermediate algebra, and a problem-specific check.

This pass checks internal consistency of these literature summaries, not a new
external literature search or the availability of every linked PDF. No claim of
human reader validation, mobile usability, grayscale print quality, or complete
physical PDF inspection is made here.
