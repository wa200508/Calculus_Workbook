# Path to beta.1

Recorded October 18, 2026, at the user's request. **The next substantive push is
to drive toward a beta release.** This plan captures the assessment and direction;
it does not declare the existing alpha manuscript ready for beta.

## Baseline and intended outcome

The current edition is 0.4.0-alpha.7: 52 complete worked problems, comprising
28 challenging mixed problems and 24 simpler reference exercises. The book has
135 pages, a stable notation chapter, a methods reference, and a four-page quick
reference included in the book and also published separately. Site and PDF
publication are established. The last recorded validation has 16 content tests
and 141 numerical spot checks; these counts will change as coverage grows.

Presentation and publishing are sufficiently established for beta preparation.
The remaining gates are breadth of challenging practice, complete analytical
review, and reader/usability validation. The design can support this work;
necessary corrections and layout repairs remain part of it.

## 1. Expand the challenging problem collection

The planning target is **about 12 additional substantial problems**, bringing
the main collection to roughly 40 mixed graduate problems alongside the existing
24 reference exercises. The count is a scope target; mathematical quality and
representative coverage determine readiness.

Start with the concrete proposals in [PROBLEM_BACKLOG.md](PROBLEM_BACKLOG.md).
Its recommended first group is proposals 1, 7, 8, 13, 19, 20, 22, 23, 25, 27,
29, and 31. Prioritize the matrix/tensor entries first, then difficult geometry
and oscillatory or singular integrals. Proposal 32, the matrix-valued resolvent
integral, is a useful substitution or addition to cover matrix integration.
Selection may change when derivations expose redundancy or unsuitable scope;
record the reason and preserve the coverage goals.

The beta collection should provide substantive practice in:

- Matrix functions and systems, multiplication order, singular limits, and
  constrained matrix variations; matrix-valued integration as well as derivatives.
- Tensor contractions, component dependencies, symmetries, and changing bases.
- Difficult geometry and electromagnetic/CEM settings, including coordinate
  charts, surface measures, near-source kernels, and excluded sources.
- Oscillation, improper convergence, parameter limits, branches, and exceptional
  cases where a tempting operation fails or unexpectedly becomes useful.

Each new problem requires a direct statement, declared types and dependencies,
three graduated hints, a full worked solution with explicit algebra, domain
analysis, a reasoned method choice, and an independent check. Mix the problems
among appropriate settings; retain stable published IDs. The complete 32-problem
backlog is available for later expansion and need not be exhausted before beta.

## 2. Audit every included solution and reference

Maintain [BETA_REVIEW.md](BETA_REVIEW.md) as the audit record. Review all 52
existing problems and every new addition. Previous targeted repairs are useful
evidence, but are not a completed whole-manuscript audit.

For each problem, verify:

- Statement, types, dimensions, dependencies, fixed quantities, and requested output.
- Every derivative, primitive, algebraic transformation, sign, and matrix order.
- Domain exclusions, connected components, branch choices, orientations, endpoints,
  and removable versus genuine singularities.
- Hypotheses for limit, derivative, sum, and integral interchanges; convergence and
  remainder arguments, including exceptional parameter values.
- An independent derivation, identity, geometric argument, or numerical check
  suited to the result. Numerical checks supplement analytical arguments.
- Agreement among the statement, hints, result, complete solution, and check.

Also audit the notation chapter, methods reference, quick reference, and tricks
appendix for formula accuracy, sufficient hypotheses, and consistent conventions.
Record concrete findings, fixes, evidence, reviewer/agent, and revision. Mark an
item complete only after its recorded review is actually performed. Leave any
unavailable independent human review or reader feedback explicitly pending.

## 3. Validate the reader's working path

Conduct an end-to-end editorial and layout pass through the book. Representative
reader trials should include several difficult problems across the main settings,
using the PDF or site and the quick reference. Record where a reader cannot
follow a dependency, an algebra step, a hint, or a domain qualification.

Reader/usability checks include:

- The printed statement immediately precedes its worked solution; references and
  continuation headers are correct throughout the expanded edition.
- Definitions, equations and their conditions, and tables remain usable across
  page breaks. Both quick-reference editions remain four pages and share their body.
- The reference sheet requires no surrounding book context. Text labels retain
  their meaning in grayscale; mathematical typography remains legible in print.
- Website navigation, search, mobile reading, keyboard operation of hint/solution
  disclosures, and mathematics rendering work on representative pages.
- Problems remain understandable without author intervention, with enough
  intermediate calculation to recover from getting stuck. External reader
  feedback, when obtained, is documented rather than inferred from automated tests.

## Beta release checklist

- [ ] Roughly 40 substantial mixed problems plus the 24 reference exercises, with
  representative matrix/tensor, geometry, and oscillatory/singular coverage.
- [ ] Every included problem has a completed analytical audit record.
- [ ] Introductory references and supporting identities have been audited.
- [ ] Editorial, full-book layout, and representative reader/usability reviews
  are recorded; blocking findings are resolved and remaining limitations listed.
- [ ] Content tests, independent mathematical checks, production site checks,
  and standalone/embedded PDF layout checks pass for the release revision.
- [ ] Generated sources match the manuscript; links, citations, and attribution
  have been checked, and both final PDFs have been visually inspected.
- [ ] Publication supports beta tags and prerelease metadata. The current PDF
  workflow accepts only `v*-alpha.*`; its tag filter, release title/notes, and
  hardcoded alpha labels in site and PDF sources need a consistent beta treatment.
- [ ] The tagged release publishes the complete book and standalone quick
  reference, and the deployed site's download links point to the verified edition.

Beta is a prerelease for broader use and feedback. The licensing and accuracy
notice remain applicable. No stable major release is authorized by this plan.
Choose the beta version when the release criteria are met; keep development
editions labelled alpha until then.

## Working rhythm and handoff

Develop a small complete batch, check it, commit it, and push it before moving
on. Update the problem inventory/count assertions and meaningful validation when
adding problems; retain checks that detect missing statements, hints, or solutions.
Update the review ledger and PROJECT_STATUS.md at substantive checkpoints.

At handoff, state the latest pushed revision, problems added or audited, checks
actually run, unresolved findings, and the next concrete task. The immediate next
task is to select and fully solve the first matrix/tensor expansion batch.
