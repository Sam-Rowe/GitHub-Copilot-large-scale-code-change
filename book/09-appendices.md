# Appendices

High-value references to support day-to-day use of this book and to accelerate adoption at scale.

## Glossary

- AI-assisted development: Using AI tools (such as GitHub Copilot) to augment software delivery.
- Agent / agentic workflow: An automated sequence where the tool plans and executes steps with human oversight.
- Bounded context: A domain-driven design boundary within which a model is consistent.
- Characterisation test: A test that captures current behaviour to protect it during refactors.
- Chunking: Splitting work into small, reviewable changes that fit model limits and human review.
- CODEOWNERS: A repository mechanism to route reviews to specific teams or individuals.
- Instruction file: Repository-scoped guidance for Copilot (for example, `.github/copilot-instructions.md`).
- Prompt file: A reusable, versioned prompt for repeatable tasks (for example, `.github/prompts/*.prompt.md`).
- Strangler pattern: Incrementally replacing legacy capability by routing traffic to a new implementation.
- MTTR: Mean time to recovery; time taken to restore service after an incident.
- Change failure rate: Percentage of changes that cause incidents requiring remediation.

## Quick reference checklists

Planning checklist

- Define scope, constraints, and acceptance criteria
- Choose chunking strategy (domain, layer, dependency, size, API, test)
- Establish documentation anchors (`docs/architecture.md`, standards) and link in instructions
- Ensure baseline tests exist for critical paths; add characterisation tests where needed
- Decide review gates, CODEOWNERS, and CI policy

Review and governance checklist

- Scope aligns to stated module/interface; small and focused
- Tests added/updated; CI green; coverage on critical paths acceptable
- Coding standards, naming, logging, and error handling followed
- Security/dependency scans clean; licences compliant
- Documentation updated (README/ADR/architecture note) as needed

## Prompt library (templates)

Test expansion (module-focused)

- Goal: Increase unit tests for the specified module covering happy paths, error paths, and edge cases.
- Inputs: Source files in scope; existing tests; recent test output.
- Constraints: British English; do not change behaviour; follow naming and structure standards.
- Steps: Propose cases → generate tests → run → adjust as needed.

Refactor to standard logging

- Goal: Apply project logging pattern to the specified files.
- Inputs: Logging standard reference; files in scope.
- Constraints: Preserve behaviour; add structured error handling as per standards.
- Steps: Identify calls → replace/augment → add tests for error paths.

Markdown lint and language tidy

- Goal: Fix markdownlint issues and British English spelling/grammar in the specified file.
- Constraints: Do not change meaning; keep headings and lists well-formed.
- Steps: Lint → fix → re-run lint → summarise changes.

## Tooling and commands

- Lint all Markdown (macOS/zsh):
  - `npx markdownlint '**/*.md'`
- Build the static site (from repo root):
  - `python3 -m venv .venv && source .venv/bin/activate`
  - `pip install -r requirements.txt`
  - `./build.sh`

## Further reading and resources

- [GitHub Copilot documentation](https://docs.github.com/copilot)
- [Copilot customisation (instructions and prompts)](https://code.visualstudio.com/docs/copilot/copilot-customization)
- [Domain-Driven Design (bounded contexts)](https://www.domainlanguage.com/ddd/)
- [Strangler Fig pattern (incremental modernisation)](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [Contract testing with Pact](https://docs.pact.io/)

## Key Takeaways

- Use the glossary and checklists to standardise language and execution across teams.
- Keep prompt templates short; point them to instruction files and high-signal docs.
- Treat documentation and tooling as part of the system; automate where possible.
- Validate outcomes with agreed metrics to sustain confidence and guide iteration.
