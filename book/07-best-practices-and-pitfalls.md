# Best Practices and Pitfalls

## What works well

- Start small and iterate: Smaller, well-scoped prompts and changes outperform large, one-shot attempts.
- Ground with documentation and tests: Provide Copilot with authoritative references and fast feedback.
- Keep humans in the loop: Pair AI assistance with review discipline and explicit acceptance criteria.
- Standardise prompts: Capture effective prompts in instruction and prompt files to scale consistency.
- Prefer repeatable patterns: Apply the same approach across modules to reduce cognitive load and variance.

## Common mistakes (and how to avoid them)

- One-shot prompting for large transformations → Decompose into a chain of small, reviewable steps.
- Vague instructions → Be explicit about scope, constraints, and success criteria (tests, lints, budgets).
- Overstuffing context → Reference docs via instruction files instead of pasting long text into prompts.
- Ignoring variability → If a result drifts, restate constraints, reduce scope, and try again.
- Pattern drift across teams → Use shared instructions, exemplars, and early cross-team reviews.

## Validating and reviewing Copilot-generated code

- Treat Copilot as a fast pair, not a final arbiter.
- Enforce pull request hygiene: small diff size, clear intent, issue links, and passing checks.
- Require compilation, unit tests, and type checks to pass before review.
- Review for behaviour, security, performance, and style—not just syntax.
- Use checklists and CODEOWNERS to ensure the right reviewers see the change.

## Iterative testing and refinement

- Prefer many small cycles (prompt → change → tests → review) over long cycles.
- Maintain characterisation tests to preserve behaviour during refactors.
- Add tests alongside changes; let tests anchor intent and protect against regressions.
- Use mutation testing or contract tests on critical paths where feasible.
- Monitor coverage trends; prioritise risky gaps rather than chasing a single target number.

## Review and governance checklist

- Scope and intent are clear and limited to the stated module or interface
- Coding standards and naming conventions followed
- Tests added/updated; key paths covered; CI is green
- Security and dependency policies respected; scans are clean
- Observability updated if behaviour or interfaces change
- Documentation updated (READMEs, ADRs, or architecture notes as appropriate)

## Key Takeaways

- Small, well-scoped changes with strong tests and reviews deliver safer progress faster.
- Clear instructions, shared prompts, and consistent patterns reduce variance and rework.
- Human oversight is essential: treat Copilot as an accelerator, not a replacement.
- Governance, security, and documentation must evolve with the code—not as an afterthought.
- Prioritise behaviour-preserving refactors and measurable improvements over big-bang changes.
