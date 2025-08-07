# Real-World Workflows

Practical workflows evolve as tools mature, but several durable patterns consistently help teams deliver large-scale change safely. This chapter presents an end-to-end example, generalises the approach to multiple contexts, and highlights techniques for legacy codebases.

## End-to-end walkthrough: language and platform migration (open source)

An open-source example demonstrates a pragmatic path for migrating a small library from Node.js to Swift whilst preserving behaviour:

- Source project: [i-ching (Node.js)](https://github.com/Sam-Rowe/i-ching)
- Target project: [IChing-Swift-Library (Swift)](https://github.com/Sam-Rowe/IChing-Swift-Library)

Step-by-step approach:

1. Strengthen tests in the source repository to capture intended behaviour for core algorithms and edge cases; contribute improvements upstream where appropriate via pull request.
2. Scaffold the target project using standard tooling for the destination language/platform (for example, Swift Package Manager).
3. Extract and document core algorithms and data structures from the source; identify library equivalents in the target ecosystem.
4. Plan the migration in small chunks (for example, by feature or module). Capture the plan in `plan.md` to coordinate agentic and manual steps.
5. Generate tests first in the target language to lock in behaviour; prioritise high-value and high-risk paths.
6. Implement incrementally using Copilot suggestions, reviewing each change for correctness, performance, and idiomatic style.
7. Cross-verify behaviour using a small CLI or script that exercises both implementations with identical inputs.
8. Update documentation and prompt files as patterns stabilise; record lessons learned to improve subsequent chunks.

## Patterns that generalise across contexts

- Solo developers and small teams: Keep scope tight, automate tests early, and rely on prompt files to reduce repetition.
- Open-source maintainers: Maintain clear contribution guidelines, small PRs, and deterministic test suites to support drive-by contributions using Copilot.
- Enterprise teams: Use instruction files, CODEOWNERS, branch policies, and staging environments; measure outcomes and publish dashboards for stakeholders.

Across all contexts, design for reviewability: small changes, clear intent, and fast feedback.

## Handling legacy codebases

Legacy systems benefit from systematic discovery and incremental change:

1. Discovery: Generate lightweight architecture notes (context, containers, key flows) and dependency graphs.
2. Golden tests: Add characterisation tests around critical paths to preserve behaviour during refactors.
3. Seams: Identify boundaries (adapters, gateways) to isolate changes; introduce interfaces where missing.
4. Strangler pattern: Route a small, stable slice through a modernised component while the legacy remains intact.
5. Data safety: Rehearse migrations with anonymised samples; add verification queries and back-out plans.
6. Operational readiness: Extend logging, metrics, and tracing before deep changes to aid diagnosis.

Copilot supports these steps by accelerating scaffolds, tests, and repetitive refactors, but human judgement sets boundaries and validates outcomes.

## Collaboration practices

- Keep changes small and thematic; prefer PRs that map to a single chunk.
- Define review service-level expectations (SLE) and use CODEOWNERS to route changes.
- Use consistent commit messages and checklists; automate linting and tests in CI.
- Document decisions (lightweight ADRs) when behaviour or architecture changes.

## Agent-mode considerations

When using agentic workflows:

- Keep a human-in-the-loop; require green tests and a review before merge.
- Cap changeset size and runtime per cycle; prefer multiple short cycles over one long run.
- Provide the agent with instruction files, test commands, and explicit in-scope paths.
- Enable rapid rollback (feature flags or revert-friendly commits).

## Validation and metrics

Track outcomes to ensure value and safety:

- Throughput: cycle time, lead time, PR size
- Quality: change failure rate, defect escape rate, flaky test rate
- Coverage and safety: coverage ratio on critical paths, mutation score (where applicable)
- Operations: mean time to recovery (MTTR), incident volume linked to transformed areas

## Key Takeaways

- Anchor behaviour with tests, then migrate in small, reviewable chunks.
- Use instruction and prompt files to make agentic and manual steps repeatable.
- For legacy systems, create seams and apply the strangler pattern to reduce risk.
- Maintain collaboration hygiene: small PRs, clear ownership, automated checks.
- Validate outcomes with agreed metrics to sustain stakeholder confidence.

