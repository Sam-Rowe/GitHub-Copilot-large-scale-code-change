# Strategies for Using GitHub Copilot Effectively

## Where to start

Successful large-scale change benefits from a deliberate, lightweight plan and strong anchors for behaviour.

1. Anchor with documentation: Create a concise `docs/architecture.md` describing structure, key modules, critical paths, and important dependencies. Reference it in `.github/copilot-instructions.md` so Copilot can consult it automatically.
2. Anchor with tests: Where possible, improve baseline test coverage of critical flows. Tests provide objective signals for behaviour before, during, and after change.
3. Co-design the plan: Ask Copilot to propose a plan to chunk and sequence the work, then refine it with a domain expert who understands the system and goals.
4. Calibrate autonomy and risk: Decide which tasks are safe to automate repeatedly (for example, happy-path unit tests) and which require closer human guidance.
5. Validate continuously: Keep feedback loops tight. Run tests frequently, review small changes quickly, and adjust prompts and patterns as you learn.

## Prompt engineering for large changes

Work within model context limits and make intent explicit.

- Be specific: State the goal, constraints, and acceptance criteria (tests, lints, performance budgets).
- Use repository guidance: Point to instructions and docs rather than pasting long context.
- Prefer incremental prompts: Chain small steps instead of one-shot prompts.
- Control scope: Limit the change to a module, folder, or interface; name the files in scope.
- Preserve behaviour: Ask Copilot to explain risky changes and propose tests for edge cases.
- Expect variability: Non-determinism is normal; if a result is off-track, restate constraints and reduce scope.

Token window considerations:

- Long prompts plus large files can exceed limits; reduce scope and reference docs.
- Break outputs into phases (plan → tests → implementation → refactor) to keep each step reviewable.

## Chunking

Chunking makes work fit model limits and human review. Choose boundaries that preserve behaviour and reduce coupling. See Chapter 4 for detailed strategies. Common patterns:

- By domain (for example, customer, billing)
- By architectural layer (data access → services → presentation)
- By dependency order (leaf modules first)
- By size/complexity (200–500 LOC per chunk)
- By test boundaries (unit/integration/contract)

## Chaining prompts (iterative workflows)

Avoid “one prompt to do it all”. Use repeatable chains.

Example: Increasing test coverage for a module

1. Update `docs/architecture.md` with a brief module overview and critical paths.
2. Using existing tests and recent test output, ask for a coverage improvement plan focused on high-risk paths.
3. Generate and run new unit tests; mock external dependencies.
4. Address issues revealed by the tests with minimal, well-reviewed code changes.
5. Add integration tests for key collaboration points; keep mocks local to unit tests.
6. Update CI to run integration tests appropriately (for example, without mocks in system environments).
7. Repeat for the next module; refine prompts as patterns emerge.

## Shared prompt libraries

Standardise effective prompts and make them discoverable.

- Centralise prompts in `.github/prompts/` where supported; otherwise, maintain a lightweight prompt catalogue in the repo.
- Document when to use each prompt, inputs required, and expected outputs.
- Version prompts alongside code and review changes like code.

## Prompt files (use cases)

Prompt files help encode repeatable tasks such as:

- “Lint and fix this Markdown file using British English”
- “Propose unit tests for this service focusing on edge cases and error paths”
- “Refactor this module to conform to logging and error-handling standards”

Keep prompt files short and point to `.github/copilot-instructions.md`, architecture docs, and standards to avoid duplication.

## Plan-driven and agent-mode workflows

Use a lightweight `plan.md` to capture intent and track progress between sessions. In agent modes (where available), keep changes small and human-in-the-loop:

- Work one chunk at a time; open focused pull requests.
- Run tests and linters after each step; revert or adjust quickly if signals degrade.
- Record learning in the plan and adjust prompts accordingly.

## Risks and guardrails

- Over-reliance on AI suggestions → Keep human review mandatory and tests comprehensive.
- Context contamination → Limit scope, close unrelated files, and state explicit in-scope artefacts.
- Pattern drift across teams → Use instruction files, exemplars, and early cross-team reviews.
- Hallucinated APIs or behaviours → Require compilation, tests, and type checks before acceptance.
- Secret exposure → Never include secrets in prompts; rely on organisation policies and scanners.

## Key Takeaways

- Success starts with clear anchors: documentation, tests, and a co-designed plan.
- Prefer small, iterative prompts and changes over one-shot transformations.
- Chunk by boundaries that preserve behaviour and fit context limits.
- Share and version effective prompts; use prompt files to reduce repetition.
- Maintain strong guardrails: human review, tests, and clear scope per change.
