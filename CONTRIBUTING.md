# Contributing

Corrections, clearer explanations, accessibility improvements, and new worked
examples are welcome. Keep the explicit notation in NOTATION_STANDARD.md.

## Content changes

The root Markdown manuscript files are the source of truth. Generated site pages
and calculus_workbook.tex must be regenerated with `pnpm content`; do not edit
those generated outputs independently. Keep stable problem IDs. A problem needs
its prompt, declared types and dependencies, graduated hints, full solution,
algebra steps, assumptions, and a check.

For mathematical corrections, include the affected problem ID and step, explain
the error, and show the corrected reasoning. Cite primary references when needed.
Do not copy a published problem set or illustration without permission compatible
with the content license and a recorded attribution.

## Development

Use Node.js 22 or later, Python 3.10 or later, and pnpm 10.11.0. Run `pnpm install
--frozen-lockfile`, then `pnpm dev`. Before submitting, run `pnpm check` and
`git diff --exit-code -- calculus_workbook.tex` to check generated-source freshness.
Preview the changed equations and interactions. A successful build is not a
certificate of mathematical correctness.

Pull requests are built and checked and provide a downloadable site artifact.
Production publication occurs only from the main branch. See docs/DEVELOPMENT.md.

By submitting work you own and intend to contribute, you agree it can be distributed
under CC BY-SA 4.0 for educational content and MIT for software, as specified in
LICENSE-CONTENT.md and LICENSE. You retain your copyright. No contributor license
agreement or copyright assignment is required.
