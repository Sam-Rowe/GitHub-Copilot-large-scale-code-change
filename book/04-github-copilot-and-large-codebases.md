# GitHub Copilot and Large Codebases

## Local indexing

VSCode and other IDEs can index the codebase locally to provide better context for GitHub Copilot. This allows Copilot to understand the structure and relationships within the code, leading to more accurate suggestions.

In the case of agentic and agent tools they can also lean on LSP ( Language Server Protocol ) to provide the context of the codebase to the LLM. This allows the LLM to understand the codebase better and ensure hallucinations that are not syntactically correct are not generated.

There are research projects that are looking at how to index codebases for LLMs to use as context. These projects are looking at how to create a more efficient indexing system that can be used by LLMs to understand the codebase better and provide more accurate suggestions. This includes research into how to index codebase such that the internal structure and relationships within the code are preserved, allowing the LLM to understand the codebase in a way to make changes across the codebase in a more managed way by understanding the relationships between files and functions.

## Remote indexing

When the Codebase is in GitHub ( not GitHub Enterprise Server ) the indexing can be done remotely. This allows Copilot to access the index of the codebase without needing to generate it locally. This is useful for large codebases where local indexing may not be feasible due to resource constraints. Indexing a repository can be computationally expensive and searching through a large codebase without an index can be slow and inefficient. By leveraging the remote index that GitHub uses for Codesearch for GitHub Copilot it allows GitHub Copilot to provide more accurate suggestions and include the correct files in the context of the prompt when making changes to the codebase.

## Prompts and Instructions to augment indexing

Prior to GitHub & VSCode introducing the ability to use custom instructions and prompt files within the codebase it was important to build a stream of thought through multiple prompts in the chat context to ensure that the LLM had the right context to make changes to the codebase. This is done by providing a series of prompts that built on each other, allowing the LLM to understand the codebase better and make more accurate suggestions.

This might look like:

- "Can you explain the architecture of this codebase and store it in a file caled /docs/architecture_overview.md"
- "Considering the Routes for the web API relating to the Customer, create a detailed architecture overview of the Customer API in the file /docs/Customer_API_Architecture.md"
- "Using the architecture overview in /docs/Customer_API_Architecture.md, create a plan to increase the test coverage for the Customer API"
- "Consider the plan for increasing the test coverage and examine any possibility to include mocking Data access in the test case for faster use in local tests but maintain the ability to run the tests against the SIT Datastore in CI/CD"
- "Implement these additional unit tests for the customer API"
- "Refine the test cases to ensure they align to the company's coding standards and naming conventions as documented in /docs/Coding_Standards.md"

Including GitHub Copilot instructions files in the codebase is the best way to ensure that the prompts can be smaller and more targeted. This can be achieved by including in the [.github/instructions.md](https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions) file that GitHub Copilot includes to provide additional context to the LLM.

That way creating or updating the architecture overview and creating the arhcitecture detail for each of the API sections can be done in separate prompts and then use the instrcutions files to point to them. This means that GitHub Copilot can use these documentation files to uderstand the codebase without having to be prompted in each chat to include it. Adding into the instructions file the location of the coding standards file also means that GitHub Copilot can use this to refine the test cases without having to be prompted in each chat. The same can be true for instrucitons on how to create tests and when to mock data access.

Then the prompts can be simplifed to:

- "Create a plan to increas the test coverage for the Customer API"
- "Implement these additional unit tests for the customer API"

Further simplification can be achieved by using ( experimental at the time of writing ) [prompt files](https://code.visualstudio.com/docs/copilot/copilot-customization#_prompt-files-experimental) to simplify even further. The prompt file could include the glue to the instructions file and only expect the user to provide the piece of code that additional tests are being added to.

Imagine the prompt file is created with the name '.github/prompts/improve-test-coverage.prompt.md'. This might look like this in use:

- "/improve-test-coverage Considering only the Customer API code"

## Chunking strategies

Effective code chunking is essential when working with GitHub Copilot on large codebases. The fundamental challenge is balancing sufficient context for the LLM whilst staying within token limits and maintaining cognitive clarity for both AI and human developers.

### Strategy 1: Domain-driven chunking

**Approach:** Divide the codebase by business domains or functional areas rather than technical layers.

**Implementation:**

- Group related features, entities, and business logic together
- Chunk by customer-facing features (e.g., authentication, billing, user management)
- Maintain domain boundaries to preserve business context

**Benefits:**

- Preserves business logic relationships
- Reduces cross-domain dependencies in prompts
- Enables domain experts to guide AI assistance effectively

**Example structure:**

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

**Approach:** Separate code by architectural concerns (presentation, business logic, data access).

**Implementation:**

- Process one architectural layer at a time
- Maintain interface contracts between layers
- Focus AI attention on layer-specific patterns and conventions

**Benefits:**

- Clear separation of concerns for AI processing
- Consistent patterns within each layer
- Easier to validate architectural compliance

**Example workflow:**

1. Transform data access layer (repositories, DAOs)
2. Update business logic layer (services, domain models)
3. Modify presentation layer (controllers, views)
4. Update cross-cutting concerns (logging, security)

### Strategy 3: Dependency-aware chunking

**Approach:** Chunk code based on dependency relationships to minimise coupling issues.

**Implementation:**

- Start with leaf nodes (no dependencies)
- Work upward through dependency tree
- Use dependency analysis tools to identify optimal chunk boundaries

**Benefits:**

- Reduces compilation and runtime errors
- Maintains system stability during transformation
- Enables incremental testing and validation

**GitHub Copilot integration:**

- Use dependency graphs in `.github/instructions.md`
- Include dependency documentation for context
- Prompt for dependency impact analysis

### Strategy 4: File size and complexity chunking

**Approach:** Divide based on file size, cyclomatic complexity, or lines of code.

**Implementation:**

- Target 200-500 lines of code per chunk for optimal AI processing
- Break down complex files before transformation
- Group simple, related files together

**Benefits:**

- Stays within practical token limits
- Reduces cognitive load for review
- Enables focused AI suggestions

**Practical guidelines:**

- Large files (>1000 LOC): Break into smaller modules first
- Medium files (200-1000 LOC): Process individually
- Small files (<200 LOC): Group by relationship

### Strategy 5: Test-driven chunking

**Approach:** Organise chunks around testable units and existing test boundaries.

**Implementation:**

- Use existing test suites to define chunk boundaries
- Ensure each chunk includes its corresponding tests
- Maintain test coverage throughout transformation

**Benefits:**

- Preserves validation capability
- Enables continuous verification
- Maintains code behaviour contracts

**GitHub Copilot workflow:**

1. Include existing tests in chunk context
2. Generate new tests alongside code changes
3. Validate transformed code against test suites

### Strategy 6: API and interface chunking

**Approach:** Chunk around stable API boundaries and public interfaces.

**Implementation:**

- Group code by public API endpoints
- Maintain interface contracts during transformation
- Process internal implementation separately from public interfaces

**Benefits:**

- Preserves external contracts
- Enables incremental deployment
- Reduces breaking changes

**Example for REST APIs:**

- Chunk by endpoint groups (`/api/users/*`, `/api/orders/*`)
- Include route definitions, handlers, and related business logic
- Transform supporting services in separate chunks

### Strategy 7: Timeline-based chunking

**Approach:** Divide work by development phases or sprint boundaries.

**Implementation:**

- Align chunks with delivery milestones
- Prioritise high-value or high-risk areas first
- Enable parallel development streams

**Benefits:**

- Maintains development velocity
- Enables risk management
- Supports agile delivery practices

**GitHub Copilot planning:**

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

In practice, successful large-scale transformations often combine multiple chunking strategies:

**Hybrid approach example:**

1. **Phase 1:** Use dependency-aware chunking to identify transformation order
2. **Phase 2:** Apply domain-driven chunking for business logic areas
3. **Phase 3:** Use API chunking for public interfaces
4. **Phase 4:** Apply file size chunking for remaining components

### GitHub Copilot-specific considerations

**Token window optimisation:**

- Include only essential context files in each chunk
- Use `.github/instructions.md` to provide background context
- Reference documentation rather than including full specifications

**Prompt efficiency:**

- Create chunk-specific prompt templates
- Use prompt files for repetitive transformation patterns
- Maintain chunk documentation for consistent AI context

**Quality assurance:**

- Include validation criteria in chunk definitions
- Use automated testing to verify chunk boundaries
- Document chunk relationships for human reviewers

The key to successful chunking is finding the right balance between AI context needs, human cognitive limits, and technical constraints. Start with a simple strategy and refine based on your specific codebase characteristics and transformation goals.

## Documentation strategies
