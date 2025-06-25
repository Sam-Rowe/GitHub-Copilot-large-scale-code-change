# Strategies for Using Copilot Effectively

## Where to start

I have seen many patterns of Copilot usage for large scale change and a good plan is always the best place to start. Especially if you follow that up with an agile methodology to adjust and course correct as you adapt your prompts to continue momentum. 

What should the plan contain. 

1) The first part is to ensure there is ample documentation of the original codebase. Getting an architecture.md file that contains an outline of the codebase, the file structure, important endpoints and libraries gives the Copilot an anchor point to ground the future code generation even at scale. Including a reference to architecture.md file in the .github/copilot-instructions.md file ensures that all work with Copilot can include it when needed to 'think' and adapt the context it requires to get the best answers.

2) Tests, this is not always possible but good test coverage of the oringal source is another great anchor point for Copilot as it gives a quantifiable assessment of the code behaviour as it was. 

3) Ask Copilot what it recommends the plan should contain and how to chunk/sample/split up the codebase to make it more manageable. This is vital that a domain expert on the Developer team hand holds Copilot here to understand the codebase and what the best approach is. It is very rarely just to go for a bing bang aproach and knowing how to spilt the code up as you go along to ensure the outcome you want is going to pay dividends later in the process.

4) This is where you need to work out how fast you want to go and how much autonomy (and risk) you want to give to Copilot. If you can map the change of a repeatable part of the process say adding unit tests for happy paths and failure modes of a function into a prompt store it and repeat it. Or go one further and take that prompt and add it to a prompt file and use a plan with Copilot to execute the prompt at scale. 

5) Course correct as you go; Always be testing. The output you are generating be it converted code, additional test coverage, or to a more modern framework the output of the process should include lots of tests as well. This is the final anchor point for Copilot and the developer. 

In the event you have Documentation, starting tests, end tests and converted code you can ask Copilot to consdier these together and ensure they are aligned.

## Prompt engineering for large changes

## Chain of prompts

### Spreadsheet for chaining prompts

### Prompt files use cases for chaining prompts

### Plan files to chain prompts or drive Agent mode

## Lessons learned from interviews
