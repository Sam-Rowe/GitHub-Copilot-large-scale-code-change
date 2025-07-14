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



## Documentation strategies
