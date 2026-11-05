# Nonlinear scalar and parameter problems: analytical audit

Reviewed November 5, 2026 by the Codex D4 audit agent. The reviewed baseline is
`8963e970e9ec23d4114203b205fccc9b7ca1c85d` (`8963e97`). Scope: the statements,
three hints, complete solutions, and checks of D4-001 through D4-006 in
`DIFFERENTIATION_MIXED.md`.

All six existing solutions were rederived analytically. No mathematical error
was found in this collection, so no manuscript correction was made. This is an
agent analytical review, not independent human review or a reader trial.

## D4-001: variable power near zero

The positive base is established on exactly the punctured real line. Writing
the function as an exponential gives the product of the exponent and the
logarithm of the base; differentiation reproduces both terms of the stated
derivative. In particular, the second logarithmic-derivative term tends to two,
not zero.

For the extension, the logarithm of the function is
`2*x*ln|x| + O(x^3*|ln|x||) + O(x^3)`. Division by `x` and the exponential
remainder give the stated difference quotient `2*ln|x| + o(1)` from both sides.
Its limit is negative infinity, so the continuous extension with value one has
no finite derivative. This conclusion does not rely on differentiating an
uncontrolled asymptotic remainder. The hints, positive-base convention, result,
and check agree. Direct numerical differentiation at positive and negative
nonsingular inputs and small-input difference quotients supplement this argument.

## D4-002: inverse hyperbolic angle

Implicit differentiation and the positive sine on the selected inverse-cosine
branch give the first derivative `-1/cosh(x)`. Differentiating it gives
`sinh(x)/cosh(x)^2`. The denominator is positive for every finite real input.
An independent equivalent representation, `theta(x)=2*arctan(exp(-x))`, follows
from the tangent half-angle identity and the angle range; its derivatives and
endpoint limits agree. Finite-difference checks used this second representation
to avoid numerical saturation of the inverse cosine. No branch or sign error
was found in the statement, hints, solution, or endpoint discussion.

## D4-003: logarithmic radical ratio

The strict inequality `sqrt(1+x^2)>|x|` proves positivity of both factors on the
whole real line. Their product is one. Rewriting the ratio as the square of the
positive sum gives twice its logarithm and derivative `2/sqrt(1+x^2)`.
Independently, the function is twice the real inverse hyperbolic sine.
Oddness supplies the negative-input representation without the cancellation in
the positive-sum formula. The proposed positive-input representation removes
the subtractive cancellation requested by the statement; it is not a claim
that naive floating-point evaluation cannot overflow. Original-expression
finite differences and inverse-hyperbolic values agree at moderate samples.

## D4-004: constrained quadric

Solving the quadratic in height yields `(-x+sqrt(2-x^2-2*y^2))/2`. The strict
branch condition is equivalent to a strictly positive radicand. Both explicit
and implicit differentiation give the stated partials. The full level gradient
can vanish only at the origin, which is not on the level surface; loss of the
height chart at the boundary is therefore correctly distinguished from loss of
surface regularity.

On the prescribed path the radicand is one. Both coordinate contributions are
needed in the chain rule and cancel to the derivative `sin(t)/2`. Direct
substitution gives height `(1-cos(t))/2`, an independent path check. Numerical
checks also substitute the computed height into the original quadric and test
both coordinate partials at interior inputs. The hints match the derivation.

## D4-005: continuous phase and delay

Each rational factor has a globally continuous argument because its real part
is one. Their argument difference and the exponential factor give the phase
`2*arctan(omega*tau)-omega*T`, with the required value at zero. Direct complex
quotient differentiation independently gives the stated imaginary logarithmic
derivative. Solving the inequality for its negative reproduces all three cases
`T=0`, `0<T<2*tau`, and `T>=2*tau`, including equality at zero frequency in the
last boundary case.

The response has no real-frequency zero or denominator zero. The qualification
about principal-phase jumps is correct, and no physical causality assumption is
used to infer an unwarranted sign. Response-versus-phase checks and direct
complex finite differences confirm representative cases in each delay regime.

## D4-006: integral with moving endpoints

The integrand and its parameter derivative are smooth on every finite local
rectangle. The moving endpoints remain in such a rectangle in a neighborhood
of any fixed finite parameter. The local Leibniz rule consequently applies
even when the interval reverses orientation. Its three terms are respectively
the upper-boundary contribution, the negative lower-boundary contribution
with exponent `-t^5`, and the negative integral of the differentiated kernel.
All signs and powers agree with independent differentiation.

At zero the boundary contribution is one half and the interior contribution is
`-(1-pi/4)`, giving `pi/4-1/2`. Direct quadrature of the original oriented
integral followed by finite differences confirms the formula on both sides of
zero, including a reversed interval at `t=-1`. The statement correctly avoids
requiring an elementary primitive; the three hints lead to the supplied result.

## Supplementary execution and limitations

The audit ran 76 additional standard-library numerical comparisons in
`/workspace/scratch/audit-d4-checks.py`: scalar and complex finite differences,
independent equivalent expressions, original-equation substitution, and
Simpson quadrature of the moving integral. All passed on November 5, 2026.
The scratch program is supplementary working evidence rather than a maintained
repository test. Numerical samples avoid singular inputs and do not establish
the domain, branch, or limiting arguments above. This review does not include
PDF pagination, website interaction, external reader feedback, or any newly
added problems.
