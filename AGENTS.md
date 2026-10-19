# Working on Calculus Workbook

The next development milestone is **beta.1**. The book remains alpha until the
beta criteria have been met. Future substantive work should advance the content
expansion, mathematical audit, and reader/usability review recorded in
[docs/BETA_PLAN.md](docs/BETA_PLAN.md).

Before starting work, read:

1. [PROJECT_STATUS.md](PROJECT_STATUS.md) for the current edition and verified state.
2. [docs/BETA_PLAN.md](docs/BETA_PLAN.md) for priorities and release criteria.
3. [docs/BETA_REVIEW.md](docs/BETA_REVIEW.md) for the problem-by-problem audit record.
4. [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md)
   for manuscript conventions, generation, checks, and publication.

The user wants a graduate workbook centered on hard mixed problems, complete
calculations, and domain management. Difficulty should arise from deciding how
to solve a clearly stated problem. Preserve the established notation and the
academic, descriptive prose. Algebra is blue; supporting identities and
expansions are purple; domain qualifications are amber.

The root Markdown files are authoritative. Both TeX documents and the reading
site are generated. The four-page quick reference is included in the main book
and supplied separately; its shared text must remain independently readable,
with no references to other parts of the workbook. Preserve its four-page layout.

The user has requested frequent meaningful commits and incremental pushes to
`main` at `git@github.com:wa200508/Calculus_Workbook.git`. Push tested checkpoints
during the work. Keep the review ledger and project status accurate; distinguish
numerical spot checks, analytical review, visual inspection, and reader feedback.
A passing build does not establish mathematical correctness.
