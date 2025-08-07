# GitHub Copilot and Large Codebases

Working effectively across a large codebase requires reliable context, predictable patterns, and disciplined decomposition. This chapter explains how Copilot uses code context (local and remote indexing), how to augment that context with instructions and prompt files, and practical chunking strategies that scale.

## Local indexing

Modern IDEs index the workspace to improve symbol search, navigation, and context available to Copilot. In addition, language servers (Language Server Protocol, LSP) expose structure—types, signatures, references—that helps Copilot generate syntactically valid and idiomatic code. Local indexing is particularly valuable when working offline, on private repositories, or when rapidly iterating in a branch.

Research continues on code representations optimised for large language models (LLMs), aiming to preserve relationships between files, symbols, and architectural boundaries so that changes remain coherent across a codebase.

## Remote indexing

For repositories hosted on GitHub.com, Copilot can leverage repository indexes maintained by GitHub to enrich context. This avoids expensive local scans for very large repositories and improves retrieval of related files during suggestions. Remote indexing is complementary to local indexing; together they provide faster, more relevant context without manual curation.

## Augmenting context with instructions and prompts

Before instruction files and prompt files were available, teams often built up chat context step by step to guide the model. With repository-scoped guidance, prompts can be shorter and more reliable.

Recommended approach:

- Add `.github/copilot-instructions.md` to define coding standards, documentation locations, testing conventions, and terminology
- Reference high-signal docs (for example, `docs/architecture.md`, `docs/coding-standards.md`) so Copilot can consult them without re-prompting
- Create prompt files for repeatable workflows (where supported), such as test expansion, refactor plans, or lint-and-fix routines

Example progressive prompting (now simplified via instructions):

- Create a high-level architecture overview at `docs/architecture_overview.md`
- Generate a domain-specific architecture note, for example `docs/customer_api_architecture.md`
- Propose a plan to increase test coverage for the Customer API
- Implement additional unit tests; mock external dependencies
- Refine tests to align with naming conventions and coding standards

With instructions and prompt files in place, the prompts can be shorter, for example:

- "Create a plan to increase the test coverage for the Customer API"
- "Implement these additional unit tests for the Customer API"

Where supported, prompt files (for example, `.github/prompts/improve-test-coverage.prompt.md`) can encapsulate multi-step guidance and point to the instruction file and relevant documents.

## Chunking strategies

Effective chunking balances sufficient context for the LLM with human reviewability and token limits.

### Strategy 1: Domain-driven chunking

Approach: Divide the codebase by business domains or functional areas rather than technical layers.

Implementation:

- Group related features, entities, and business logic together
- Chunk by customer-facing features (for example, authentication, billing, user management)
- Maintain domain boundaries to preserve business context

Benefits:

- Preserves business logic relationships
- Reduces cross-domain dependencies in prompts
- Enables domain experts to guide AI assistance effectively

Example structure:

```text
/customer-domain/
  ├── api/
  ├── services/
  ├── models/
  └── tests/
/billing-domain/
  ├── api/
  ├── services/
  ├── models/
  └── tests/
```

### Strategy 2: Architectural layer chunking

Approach: Separate code by architectural concerns (presentation, business logic, data access).

Implementation:

- Process one architectural layer at a time
- Maintain interface contracts between layers
- Focus AI attention on layer-specific patterns and conventions

Benefits:

- Clear separation of concerns for AI processing
- Consistent patterns within each layer
- Easier to validate architectural compliance

Example workflow:

1. Transform data access layer (repositories, DAOs)
2. Update business logic layer (services, domain models)
3. Modify presentation layer (controllers, views)
4. Update cross-cutting concerns (logging, security)

### Strategy 3: Dependency-aware chunking

Approach: Chunk code based on dependency relationships to minimise coupling issues.

Implementation:

- Start with leaf nodes (no dependencies)
- Work upwards through the dependency tree
- Use dependency analysis tools to identify optimal chunk boundaries

Benefits:

- Reduces compilation and runtime errors
- Maintains system stability during transformation
- Enables incremental testing and validation

Copilot integration:

- Use dependency graphs referenced from `.github/copilot-instructions.md`
- Include dependency documentation for context
- Prompt for dependency impact analysis

### Strategy 4: File size and complexity chunking

Approach: Divide based on file size, cyclomatic complexity, or lines of code.

Implementation:

- Target 200–500 lines of code per chunk for practical AI processing
- Break down complex files before transformation
- Group simple, related files together

Benefits:

- Stays within practical token limits
- Reduces cognitive load for review
- Enables focused AI suggestions

Practical guidelines:

- Large files (>1000 LOC): break into smaller modules first
- Medium files (200–1000 LOC): process individually
- Small files (<200 LOC): group by relationship

### Strategy 5: Test-driven chunking

Approach: Organise chunks around testable units and existing test boundaries.

Implementation:

- Use existing test suites to define chunk boundaries
- Ensure each chunk includes its corresponding tests
- Maintain test coverage throughout transformation

Benefits:

- Preserves validation capability
- Enables continuous verification
- Maintains code behaviour contracts

Copilot workflow:

1. Include existing tests in chunk context
2. Generate new tests alongside code changes
3. Validate transformed code against test suites

### Strategy 6: API and interface chunking

Approach: Chunk around stable API boundaries and public interfaces.

Implementation:

- Group code by public API endpoints
- Maintain interface contracts during transformation
- Process internal implementation separately from public interfaces

Benefits:

- Preserves external contracts
- Enables incremental deployment
- Reduces breaking changes

Example for REST APIs:

- Chunk by endpoint groups (`/api/users/*`, `/api/orders/*`)
- Include route definitions, handlers, and related business logic
- Transform supporting services in separate chunks

### Strategy 7: Timeline-based chunking

Approach: Divide work by development phases or sprint boundaries.

Implementation:

- Align chunks with delivery milestones
- Prioritise high-value or high-risk areas first
- Enable parallel development streams

Benefits:

- Maintains development velocity
- Enables risk management
- Supports agile delivery practices

Copilot planning:

- Create phase-specific instruction files
- Use milestone-based prompt libraries
- Track transformation progress across phases

### Chunking decision matrix

When selecting a chunking strategy, consider:

| Factor | Domain | Layer | Dependency | Size | Test | API | Timeline |
|--------|--------|-------|------------|------|------|-----|----------|
| Business logic preservation | ⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Technical complexity | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ |
| Team coordination | ⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| AI context quality | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Risk management | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |

### Combining strategies

In practice, successful transformations often combine multiple strategies:

1. Phase 1: use dependency-aware chunking to identify transformation order
2. Phase 2: apply domain-driven chunking for business logic areas
3. Phase 3: use API chunking for public interfaces
4. Phase 4: apply file-size chunking for remaining components

### Copilot-specific considerations

Token window optimisation:

- Include only essential context files per chunk
- Use `.github/copilot-instructions.md` to provide background context
- Reference documentation rather than including full specifications

Prompt efficiency:

- Create chunk-specific prompt templates or prompt files
- Maintain chunk documentation for consistent AI context

Quality assurance:

- Include validation criteria in chunk definitions
- Use automated testing to verify chunk boundaries
- Document chunk relationships for human reviewers

## Documentation strategies

Documentation is a multiplier for Copilot effectiveness. Prioritise high-signal, low-noise artefacts that the model can reference consistently:

- Architecture overview: `docs/architecture.md` with system context, bounded contexts, major data flows
- Module READMEs: local purpose, key entry points, dependencies, and testing instructions
- API contracts: OpenAPI/Swagger, GraphQL schemas, protobuf/IDLs kept alongside implementations
- Coding standards: language- and framework-specific conventions; naming, error handling, logging
- Testing conventions: unit/integration/contract strategies; fixtures, mocks, and environment guidance
- Dependency documentation: diagrams or generated graphs, version policies, deprecation timelines
- Decision records: lightweight ADRs for significant architectural choices

Practices:

- Co-locate docs with code; link from `.github/copilot-instructions.md`
- Keep documents concise; prefer links and references over duplication
- Automate generation where possible (for example, API specs, dependency graphs)
- Treat documentation updates as part of the definition of done

## Key Takeaways

- Indexing (local and remote) improves suggestion relevance; pair it with high-signal documentation.
- Instruction and prompt files reduce prompt length and increase consistency across teams.
- Chunking is essential: choose boundaries that protect behaviour and fit context limits.
- Keep changes small, testable, and reviewable; encode validation into your workflow.
- Documentation is part of the system: make it discoverable, current, and referenced by Copilot.
