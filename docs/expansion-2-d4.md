# Second practice expansion: five nonlinear and parameter problems

Prepared November 6, 2026 by the Codex D4 author agent, from baseline
`d272310f466aaa0ea8c5cf585481c5ab39321dbc` (`d272310`). Scope: the new problems
D4-012 through D4-016 in `DIFFERENTIATION_MIXED.md`. Every previous D4 problem,
hint ladder, and solution body was preserved exactly. The five additions have
explicit types and dependencies, exactly three hints, complete intermediate
calculations, domain analysis, and independent checks.

This note records author derivation and supplementary numerical verification.
A different reviewer derives these problems independently before consulting the
author solutions. No independent human review, reader trial, or new PDF layout
inspection is claimed by the author note.

## Proposal mapping

| Problem | Source proposal | Scope |
|---|---|---|
| D4-012 | Backlog 2 | Principal arctangent folds and a continuous angle lift |
| D4-013 | Backlog 5 | A simple response zero and the impossibility of a phase continuation |
| D4-014 | Backlog 26, extended | Shared-entry determinant differentiation, two inverse derivatives, and conditioning |
| D4-015 | New proposal 33 | A globally selected cubic branch with a controlled fold expansion |
| D4-016 | New proposal 34 | Uniform smoothing, nonuniform derivative limits, and curvature concentration |

New proposal numbers identify this expansion's planning additions; shared
backlog/status files are updated during root integration rather than by this
chapter's author.

## D4-012: folded arctangent

Let the unrestricted angle be `theta(x)=2*arctan(x)`, whose values lie in
`(-pi,pi)`. The double-angle identity establishes equality of tangents at every
admissible input. Choosing the principal arctangent range gives the three exact
relations `f=theta+pi` on `x<-1`, `f=theta` on `-1<x<1`, and `f=theta-pi` on
`x>1`. Thus each excluded input has left limit `pi/2`, right limit `-pi/2`, and
right-minus-left jump `-pi`.

Direct quotient and chain differentiation simplifies independently to
`2/(1+x^2)`. The cancellation is allowed only on the original domain, and a
matching limit of derivatives cannot remove a jump in function values.
The unique continuous lift normalized to zero at zero subtracts pi on the left
component and adds pi on the right component, filling in the two missing angle
values as `-pi/2` and `pi/2`. It is exactly `2*arctan(x)` on the whole real line.
This lift changes original values on two components and therefore is not an
extension of the original principal-valued function. The angle ambiguity here
is modulo pi because the specified relation is a tangent relation.

Supplementary checks used direct original-function values, independent
`2*arctan(x)` values with the correct offsets, finite differences on all three
components including inputs close to the exclusions, and one-sided limits.
All 33 comparisons passed.

## D4-013: phase zero

Factoring with `theta=omega*tau/2` gives
`H=2*i*exp(-i*theta)*sin(theta)`. The zeros are exactly `2*pi*n/tau` for integer
`n`, and magnitude is `2*abs(sin(theta))`. In the interval between consecutive
zeros indexed by `n`, the sine has constant sign `(-1)^n`; the selected phase is
`pi/2-omega*tau/2+n*pi`, with derivative `-tau/2`. Every other continuous phase
on that same connected interval differs by a fixed multiple of `2*pi`.

At a zero plus signed displacement delta, the response is
`i*tau*delta+tau^2*delta^2/2+O(delta^3)`. Its magnitude is
`tau*abs(delta)+O(abs(delta)^3)`. The normalized response approaches `-i` from
the left and `i` from the right. Since those limits are opposite, no assignment
at the zero or interval-dependent multiples of `2*pi` can produce a continuous
phase through it. The complex response itself remains smooth and its frequency
derivative is `i*tau` at each zero.

The independent complex logarithmic derivative is
`(tau/2)*(cot(theta)-i)`. Its imaginary part checks the phase slope; its real
part displays the magnitude's logarithmic divergence. The restriction to
nonzero response is retained throughout that check.

The 225 supplementary comparisons included positive and negative zero indices,
three fixed times, phase reconstruction at several locations in each interval,
direct complex finite differences, normalized one-sided limits, and leading
magnitude coefficients. All passed.

## D4-014: determinant path, inverse sensitivity, and conditioning

The matrix is the product of the real shear `[[1,t],[0,1]]` and its transpose,
so it is positive definite for every real input. Its determinant is identically
one and its inverse is the polynomial matrix `[[1,-t],[-t,1+t^2]]`.
The trace identity gives zero logarithmic-determinant derivative, matching direct
scalar differentiation. In its entry contraction the terms are
`2*t-t-t=0`: varying only one shared off-diagonal entry would omit a required
contribution.

Differentiating the inverse identity gives the ordered first derivative
`-R*(dA/dt)*R`. A second product differentiation gives
`2*R*(dA/dt)*R*(dA/dt)*R-R*(d^2A/dt^2)*R`.
The two repeated positive chains have the same order because of the inverse
identity, not an assumption that the factors commute. Explicit products reduce
them to `R` and `2*[[1,-t],[-t,t^2]]` respectively. They yield first derivative
`[[0,-1],[-1,2*t]]` and second derivative `[[0,0],[0,2]]`, independently checked
by differentiating the polynomial entries.

The ordered positive eigenvalues are
`(t^2+2 +/- abs(t)*sqrt(t^2+4))/2`, with the smaller also equal to the reciprocal
of the larger. The absolute value is necessary for ordered labels on both
sides of zero. The repeated eigenvalue at zero introduces no matrix or inverse
singularity. As the absolute input grows, the larger eigenvalue behaves as
`t^2`, the smaller as `t^-2`, and the Euclidean operator-norm condition number as
`t^4`. The inverse response to the fixed second-coordinate unit vector is
`[-t,1+t^2]`, whose norm grows as `t^2`. This makes the distinction between
constant determinant and bounded response explicit.

The 188 supplementary comparisons evaluated ordered matrix chains, first and
second entrywise finite differences, trace contractions, inverse identities,
eigenvalue sum/product/positivity, growing responses, and asymptotic ratios at
both large positive and negative inputs. All passed.

## D4-015: cubic branch and fold endpoint

The function `y^3-3*y` has positive derivative on `y>1`, tends to `-2` at its
left endpoint and to infinity at its right endpoint. It therefore defines a
unique selected inverse on exactly `x>-2`. This global range argument precedes
the local inverse theorem, so the domain does not rely on an unsupported global
continuation claim. The separate cubic behavior at input `x=2` does not create
a fold on this selected branch: the selected value there is two and its height
partial is nine.

Implicit composition differentiation gives
`dg/dx=1/(3*(g^2-1))` and
`d^2g/dx^2=-2*g/(9*(g^2-1)^3)`.
The branch extends continuously to value one at input minus two. Setting
`delta=x+2` and `u=g(x)-1` gives the exact relation
`delta=u^2*(3+u)`. The smooth map `W(u)=u*sqrt(3+u)` has derivative `sqrt(3)` at
zero. Its local inverse in `s=sqrt(delta)` has first derivative `1/sqrt(3)`
and second derivative `-1/9` there. Bounded third derivative of that inverse
justifies
`g(-2+delta)=1+sqrt(delta)/sqrt(3)-delta/18+O(delta^(3/2))`.

The derivative limits are established from the exact implicit formulas, without
differentiating a big-O value estimate:
`sqrt(delta)*dg/dx -> 1/(2*sqrt(3))` and
`delta^(3/2)*d^2g/dx^2 -> -1/(4*sqrt(3))`.
The endpoint extension's own difference quotient instead diverges with leading
coefficient `1/sqrt(3)` after multiplication by `sqrt(delta)`, consistent with a
square-root fold and no finite right derivative. Direct substitution of the
quadratic polynomial in the square-root coordinate cancels the cubic term in
that coordinate, independently checking the expansion's first coefficients.

The 32 supplementary comparisons solved the original constraint by monotone
bisection, checked both finite-difference derivatives in the interior, tested
the expansion error against its predicted order, and checked the two scaled
blowup coefficients and the endpoint difference quotient. All passed.

## D4-016: uniform approximation and concentrated curvature

Factoring the larger exponential gives the exact identity
`f_epsilon(x)=abs(x)+epsilon*ln(1+exp(-2*abs(x)/epsilon))`.
The value error lies between zero and `epsilon*ln(2)`, with equality at zero,
so the approximation is uniform on the whole line. With epsilon fixed positive,
chain differentiation gives `tanh(x/epsilon)` and
`rho_epsilon(x)=1/(epsilon*cosh(x/epsilon)^2)`.

The first derivative approaches the sign function away from zero, with error
at most `2*exp(-2*delta/epsilon)` on `abs(x)>=delta>0`. On every fixed
neighborhood of zero the supremum of its error relative to the pointwise sign
limit remains one, so convergence there is not uniform. This does not contradict
uniform convergence of the values or confer a derivative on the absolute value
at zero.

The nonnegative second derivative has total integral two and mass
`2*tanh(c)` on `[-c*epsilon,c*epsilon]`. Its mass outside `[-delta,delta]` is
`4/(exp(2*delta/epsilon)+1)`, at most `4*exp(-2*delta/epsilon)`.
It tends pointwise to zero at every nonzero input while its value at zero
diverges. Thus a global integrable majorant for the family near epsilon zero
would contradict its constant total integral.

For a bounded continuous real function psi, define its local oscillation
`eta(delta)=sup_(abs(x)<=delta) abs(psi(x)-psi(0))` and bound its magnitude by
`M`. Positivity, the total mass, and the tail bound give test-function error
at most `2*eta(delta)+8*M*exp(-2*delta/epsilon)`.
Taking the positive-width limit first at fixed delta and then shrinking delta
proves the limit `2*psi(0)` without interchanging an uncontrolled pointwise
second-derivative limit. Fixed positive epsilon and fixed positive distance
from zero are distinguished wherever estimates require them.

The 87 supplementary comparisons checked stable original-function evaluations,
first and second derivative finite differences, exact scaled-interval mass,
tail quadrature, uniform value bounds, away-from-zero slope bounds, and several
bounded continuous test functions, including constant and odd tests. All passed.

## Executed checks and remaining integration work

`/workspace/scratch/expansion2-d4-checks.py` executed **565** supplementary
standard-library comparisons successfully on November 6, 2026. These numerical
samples support the author derivations; they do not replace the domain, branch,
endpoint, or concentration arguments. The scratch program is author working
evidence rather than a maintained repository test.

The chapter parser confirmed 16 unique matching statements, hint ladders, and
solutions, exactly three hints in every ladder, and the required SETUP, CHOICE,
CALCULUS, ALGEBRA, DOMAIN, and CHECK labels in all five additions. Parsed bodies
of all 11 prior statements, hint ladders, and solutions match baseline `d272310`
exactly. The manuscript is frozen for the independent review. Root integration
will update shared inventories, maintained checks, generated sources, and status;
this author did not edit those files or commit changes.
