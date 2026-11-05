# Five new oscillatory, concentration, and singular-source problems

Added November 5, 2026 by Codex agent `audit_i3`, after the correction checkpoint
`606a472`. Scope: new problems I3-010 through I3-014 in
`INTEGRATION_DOMAINS.md`; all nine previous published IDs and calculations were
retained. The additions have complete statements, three graduated hints each,
method-choice explanations, explicit calculations, domain/convergence analysis,
and independent checks. The derivations below record the author-agent review;
a second review and complete publication checks are integrated by the primary
agent. No human reader review is claimed.

## Proposal map and analytical checks

| ID | Backlog proposal | Derivation and domain reasoning | Independent verification |
|---|---|---|---|
| I3-010 | 7, squared aperture kernel | The kernel is bounded by `a²` near zero and by `x^(−2)` at infinity, hence absolutely integrable for every real parameter. Scaling by `|a|` separates the parameter. Integration by parts has vanishing endpoint terms and reduces the universal coefficient to the ordinary sine integral with frequency two, giving `Q(a) = π|a|/2`. The cusp prevents differentiation at zero. Away from zero, the formal derivative integral is conditionally convergent and has locally uniform oscillatory tail bounds; the text explicitly permits that justified interchange rather than incorrectly denying it. At zero, the pointwise derivative is zero but neither two-sided differentiability nor a common integrable absolute majorant holds. The original omitted tail is at most `1/L`. | Original-coordinate finite quadrature is compared with the result using the rigorous omitted-tail interval for six signed or zero parameters. Four finite derivative integrals obey their independent conditional tail bound. A fixed-cutoff small-parameter expansion independently identifies the failure of uniformity at lengths of order `1/|a|`. |
| I3-011 | 9, logarithmic moment | The exact finite geometric identity gives an explicit signed remainder before any infinite interchange is used. The identity `∫₀¹ x^n ln²x dx = 2/(n+1)³` follows by logarithmic substitution and two integrations by parts. The remainder after `N` terms is positive up to the factor `(−1)^N` and is at most `2/(N+1)³`. The sum of absolute term integrals is finite, which separately justifies interchange. Even/odd splitting yields `3ζ(3)/2`, with `ζ(3)` defined by its positive series. | The original integral becomes the smooth positive integral `∫₀∞ t²/(exp(t)+1) dt`, with explicit tail bound `exp(−T)(T²+2T+2)`. Its numerical value agrees with the constant and with the signed remainder bounds for five truncation counts. The elementary interval bound `1 ≤ M ≤ 2` provides another check. |
| I3-012 | 10, shrinking layer | Rescaling `u = x/a` gives `F(a) = atan(1/a) = π/2 − atan(a)` for positive `a`. The integrated limit is `π/2`, while the almost-everywhere kernel limit is zero. The interval `[0,ca]` carries exactly `atan(c)` when contained in the domain; fixed intervals away from zero carry vanishing mass. Maximizing the kernel in `a` gives the nonintegrable envelope `1/(2x)`. Local positive-parameter differentiation is justified on a compact rectangle and integrates exactly to `−1/(1+a²)`. The derivative kernels have nonintegrable positive pointwise limit, so their limit interchange also fails. An exact finite identity gives `F(a) = π/2 − a + a³/3 + E(a)` with `−a⁵/5 ≤ E(a) ≤ 0`. The continuous scalar extension and naive integrated kernel assignment are distinguished. | Direct original-kernel quadrature and quadrature of the signed derivative kernel agree at four positive parameters, including a narrow layer. Three shrinking-interval integrals agree with their masses, and three local expansions obey the rigorous signed bound. The ordinary value `a = 1` independently gives `π/4` and derivative `−1/2`. |
| I3-013 | 16, circulation around an excluded axis | The field and both paths have explicit real types and positive orientation. Direct ellipse parameterization gives `AB/(A² cos²θ + B² sin²θ)`, whose four quadrant integrals sum to `2π`. Coordinate partials show curl zero off the axis. The centered spanning disk violates the regularity hypothesis, whereas the displaced disk lies in `x ≥ d−R > 0` and gives zero circulation by Stokes. | A globally continuous real angle on the displaced circle differentiates to its original line integrand and returns to its initial value. Excision of a centered disk from the ellipse gives a smooth annular surface; the inner clockwise boundary sign reproduces the outer value from the known centered-circle integral. Numerical direct line integrals verify three axis ratios and three displaced circles. |
| I3-014 | 20, source inside triangular panel | A polar disk estimate proves local integrability with source-neighborhood contribution at most `2πε`. Three counterclockwise edges generate a partition around the interior source. The source-edge map has Jacobian columns `(a_j + v e_j, u e_j)` and determinants `u y₀`, `u(1−x₀)`, and `u(x₀−y₀)`, all positive. Its radial factor cancels the `1/R` kernel. Each remaining edge integral is bounded on its closed interval because the source-to-edge distance is positive. Tangential/perpendicular decomposition evaluates it as a difference of real inverse hyperbolic sines, yielding three explicit expressions for the complete integral. Monotone source truncation and zero-area shared boundaries justify addition of the pieces. | Independent direct integration in the original Cartesian `y` coordinate gives a one-dimensional logarithmically singular integral in `x`. Separate square-coordinate substitutions on either side of `x₀` provide stable numerical comparison without using the source-edge maps. Five interior sources, including near-edge examples, agree. Reflection `(x₀,y₀) → (1−y₀,1−x₀)` and the explicit centroid value provide analytical checks. Each Jacobian is additionally verified at two parameter pairs; the global bound `K ≤ 2+√2` holds. |

## Executed checks

On November 5, 2026:

- `python3 /workspace/scratch/expansion-i3-checks.py` passed **63 independent
  numerical checks**, using only Python's standard library. The scratch script
  is supplementary session material for the primary agent to integrate into the
  permanent mathematical checking suite as appropriate.
- The repository's `problem_sections` parser accepted all **14** I3 statement,
  hint, and complete-solution IDs with matching sets. Each addition has exactly
  three numbered hints and all six required categories: SETUP, CHOICE,
  CALCULUS, ALGEBRA, DOMAIN, and CHECK.

Finite numerical checks supplement the analytical convergence and interchange
arguments; they do not replace them. A full site/PDF build and visual layout
inspection are not claimed by this individual agent. The book remains alpha
until the separately documented beta requirements are met.
