# Analytical audit: oscillatory and singular integrals

Reviewed November 5, 2026 by Codex agent `audit_i3`, against baseline commit
`8963e970e9ec23d4114203b205fccc9b7ca1c85d`. Scope: all nine existing problems,
their statements, three hints, complete calculations, checks, and domain claims
in `INTEGRATION_DOMAINS.md`. This is an analytical agent review supplemented by
numerical checks. It is not independent human review or a full PDF layout review.

## Finding and correction

**I3-008, Step 4:** the original text grouped the angular seam with the places
where spherical coordinates are singular. In the displayed Jacobian, the
absolute determinant is `abc r² sin θ`, which is nonzero at azimuth zero or
`2π` when `r > 0` and `0 < θ < π`. The seam identifies two parameter values;
it is not a local Jacobian degeneracy. The revised paragraph distinguishes
that identification from the center and poles. The zero-volume exception and
the final integral are unchanged. No erroneous final value was found in the
nine existing problems.

## Per-problem derivations and checks

| ID | Analytical derivation, domain review, and independent verification | Outcome |
|---|---|---|
| I3-001 | On `[0,π/2]`, `x = arcsin u` has positive derivative; on `[π/2,π]`, `x = π − arcsin u` has negative derivative and reversed bounds. Each contributes `∫₀¹ u/√(1−u²) du = 1`. Both inverse derivatives have an integrable endpoint singularity. A single function of `sin x` times `cos x` cannot represent `sin x` on both branches, because reflected points have the same sine and opposite cosine. Direct endpoint evaluation of `−cos x` gives 2 independently. | Correct. |
| I3-002 | Scaling `u = kx` gives `Si(kL)` for `k ≠ 0`; orientation gives the sign for negative `k`. The continuous kernel value is `k`, and `k = 0` is treated without dividing by the parameter. Integrating the cubic sine approximation yields `kL − k³L³/18`. Taylor's fifth-order bound integrates to `|k|⁵L⁵/600`. Differentiation in the endpoint gives `sin(kL)/L`. An independently integrated sine power series agrees numerically for positive, negative, and zero `k`. | Correct. |
| I3-003 | For positive damping, local domination of the parameter derivative by `exp(−ε₀x/2)` permits interchange. Complex exponential integration gives derivative `−k/(ε²+k²)`. The limit at infinite damping fixes the primitive as `atan(k/ε)`. Integration by parts against `−cos(kx)/k` gives uniform tails at most `2/(kA)`, including zero damping, so the undamped ordinary limit is `π/2`. On successive sine lobes, the stated lower bounds sum harmonically, proving failure of absolute convergence. The integral of the parameter derivative at zero fails to converge, so that interchange is unavailable even though a right derivative of the evaluated function exists. Damped quadrature and finite undamped truncations satisfy the derived results and bounds. | Correct. |
| I3-004 | Componentwise integration gives `(exp(iΔL)−1)/(iΔ)` for nonzero mismatch, and the original integral gives `L` at zero. Midpoint factorization produces the unnormalized sinc form. Its phase includes an extra `π` on negative sinc intervals and is undefined at amplitude zeros, as stated. The triangle inequality gives magnitude at most `L`. Complex quadrature checks both signs, zero mismatch, and a sinc zero. | Correct. |
| I3-005 | Each one-sided logarithmic primitive diverges separately with the stated sign. Equal interior exclusions cancel to `ln((1−a)/(1+a))`; exclusions with ratio `λ` add `ln λ`. The positive log arguments follow from `−1 < a < 1`. At the endpoints, the remaining one-sided divergence prevents this interior Cauchy prescription. Logarithmic coordinates on each side independently reproduce the symmetric result for three pole locations. | Correct. |
| I3-006 | The substitution `s = ρ sinh u` uses positivity of `ρ` and `cosh u`; transformed endpoints are `±arsinh(L/ρ)`, hence `P = 2 arsinh(L/ρ)`. The fixed-`L` derivative is `−2L/(ρ√(ρ²+L²))`. On a compact neighborhood of any positive `ρ`, the differentiated kernel has a uniform bound on the fixed finite source interval. Direct integration of that kernel via `s/√(ρ²+s²)` gives the same derivative. At zero distance the kernel is `1/|s|`, so the original integral diverges. The near- and far-distance asymptotics have the stated coefficients. Original-coordinate quadrature checks the potential and derivative at three distances. | Correct. |
| I3-007 | The inverse-coordinate map has determinant `u > 0`. The `1/R` kernel times the area Jacobian is `1/√(1+v²)`, whose integral is `arsinh(1)`. The `1/R²` replacement leaves `(1/u)/(1+v²)` and diverges logarithmically. Nonnegative monotone truncation justifies the singular area integral and removes dependence on the particular exhaustion. Independent polar coordinates have angular range `[0,π/4]` and radial bound `sec θ`, yielding `∫ sec θ dθ = ln(1+√2)`. | Correct. |
| I3-008 | The linear scaling has positive determinant `abc`; the spherical map contributes `r² sin θ`. The quadratic form becomes `r²`. Angular integration gives `4πabc`, and integration by parts in radius gives coefficient `π^(3/2) erf(1) − 2π/e = 2.380979718752334`. The upper/lower bounds follow from `e^(−1) ≤ exp(−q) ≤ 1`. Independent integration of the uniformly convergent exponential series gives `4π Σₙ (−1)ⁿ/(n!(2n+3))`, agreeing with that coefficient. The seam determinant check also confirms the terminology correction above. | Correct after seam correction. |
| I3-009 | Differentiating both tangents gives the stated inward-oriented cross product. Area uses its positive norm `ℓ² cosh u √(1+2sinh²u)`, so orientation does not change the result. Scaling `t = sinh u` yields the primitive `t√(1+2t²)/2 + arsinh(√2t)/(2√2)`; direct differentiation verifies it. Oddness gives the stated symmetric-band area. At `U = 0` the area vanishes, its leading term is `4πℓ²U`, and its positive first term grows without bound as `U → ∞`. Original-parameter surface quadrature agrees for three cutoffs including zero. | Correct. |

All statements, hints, solution steps, and checks agree after the single correction.
Units and declared real/complex output types are consistent. Published IDs were
retained.

## Executed numerical evidence

`python3 /workspace/scratch/audit-i3-checks.py` passed **34 checks** on November 5,
2026. The scratch script uses only Python's standard library. It checks original
coordinate quadrature, independent power series, complex components, convergence
bounds, logarithmic pole coordinates, and a nonzero seam Jacobian. These are
finite numerical checks; the convergence and interchange conclusions rest on
the analytical arguments recorded above. The script is supplementary session
material rather than part of the repository's permanent test suite.

## Limits

No external human reader trial, browser interaction, citation-access audit, or
full-book visual pagination review was performed by this agent. The chapter's
application references were assessed for the scope described in its prose,
without claiming those general CEM methods are fully modeled by these examples.
