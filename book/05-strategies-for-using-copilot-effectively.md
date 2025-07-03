# Strategies for Using Copilot Effectively

## Where to start

I have seen many patterns of Copilot usage for large scale change and a good plan is always the best place to start. Especially if you follow that up with an agile methodology to adjust and course correct as you adapt your prompts to continue momentum. 

What should the plan contain. 

1) The first part is to ensure there is ample documentation of the original codebase. Getting an architecture.md file that contains an outline of the codebase, the file structure, important endpoints and libraries gives the Copilot an anchor point to ground the future code generation even at scale. Including a reference to architecture.md file in the .github/copilot-instructions.md file ensures that all work with Copilot can include it when needed to 'think' and adapt the context it requires to get the best answers.

2) Tests, this is not always possible but good test coverage of the oringal source is another great anchor point for Copilot as it gives a quantifiable assessment of the code behaviour as it was. 

3) Ask Copilot what it recommends the plan should contain and how to chunk/sample/split up the codebase to make it more manageable. This is vital that a domain expert on the Developer team hand holds Copilot here to understand the codebase and what the best approach is. It is very rarely just to go for a bing bang aproach and knowing how to spilt the code up as you go along to ensure the outcome you want is going to pay dividends later in the process.

4) This is where you need to work out how fast you want to go and how much autonomy (and risk) you want to give to Copilot. If you can map the change of a repeatable part of the process say adding unit tests for happy paths and failure modes of a function into a prompt store it and repeat it. Or go one further and take that prompt and add it to a prompt file and use a plan with Copilot to execute the prompt at scale.

5) Course correct as you go; Always be testing. The output you are generating be it converted code, additional test coverage, or to a more modern framework the output of the process should include lots of tests as well. This is the final anchor point for Copilot and the developer.

In the event you have Documentation, starting tests, end tests and converted code you can ask Copilot to consider these together and ensure they are aligned.

## Prompt engineering for large changes

When prompting for large changes it is important to consider the token window as well as the current codebase alongside the prompt itself.

All LLM's have a maxmium number of tokens that they can aceept as a token window and a maximum number of tokens they can respond with. This can also be constrained byt the IDE and extension as well.

If the code already in the codebase is large and your prompt will generate a large amount of new code this is likely to overwhelm the token window for the LLM or the IDE extensions token window.

This is in effect the first problem I get challenged on when working with customers who want to make large scale code changes. The prompt can be hugely sophistocated but the prompt + source code + response code is way to big to fit in the token window so the results are poor. 

Do not get downhearted though it is a learning experience. This is why we need to break up the work into smaller chunks.

## Chunking

An domain expert on the codebase and the business area is extremely useful in this. It is not impossible without but it is not as likely to be a smooth ride.

A domain expert can help identify how to chunk the code and the change. In my experience with customers this could be to chunk the code by interface and work on a repeatable pattern to convert one interface at a time.

It could be to chunk the change up by folder or module.

Whatever you do to chunk the code the objective is to make it so that the larger code change is split into a series of chunks that can be repeated ( though they don't have to be identical ).

## Chain of prompts

With large changes it can be tempting to try to one shot the prompt, a practice of giving GitHub Copilot one prompt that produces the desired output in one go. It is tempting to think that by giving a clear enough prompt that it will work. However experience has shown that one shot prompting for large changes is not the right way to achieve large changes. It is better to chain prompts together one after another in a repeatable way to make the larger change possible.

Lets consider an example.

A team is trying to increase test coverage of an application. They have chosen to chunk the code by module. The steps might look like this.

1) Augment the /docs/Architecture.md with a section on the module in question.
2) Using the /docs/Architecture.md, the current tests in /tests/* and the output of running the tests create a plan to increase the test coverage for this module
3) Implement Unit tests from the plan
4) Rectify any features in the code identified by new unit tests
5) Implement integration tests from the plan, mock any tests to external resources outside of this codebase
6) Rectify any features in the code identified by the new intergation tests. 
7) Update CI/CD for SIT environment to run new integration tests without the Mocks
8) Rectify any features identified

Now for each step you would have a different prompt, and those prompts can be repeated one after the other for the next module. With a developer watching to ensure that the outcome from each stage is understood and applicable.

### Spreadsheet for chaining prompts

Taking this chain of prompts to the next level, I have seen teams take the prompts and add them to spreadsheets or prompt libraries shared to help a team complete the change at an even larger scale. 

As a group the steps will be worked through for one module/interface/chunk and once a repeatable pattern is emerging with robust prompts they can be tried on the next chunk/module/interface. Eventually the team can divide the work and use the prompt chain across the codebase at the same time.

### Prompt files use cases for chaining prompts

Keeping the prompts outside of the codebase isn't condusive to modern software practices where we keep control of our source and can see the evolution. Well fear not. In VSCode and in the future other IDE's we can keep prompts in the repo as well.

This is a double whamy of amazing.

instructions files get included with every prompt to the LLM so they are in effect ways to automatically ensure good standards and help share where memory is within the repository. Typically I would use the instructions file to tell GitHub Copilot where the architecture.md file is and to include it. I would include instructions for running tests, the naming convetions within my codebase, the testing framework that I am mandating and any other instruciton that must be accompanying every prompt.

Then we have prompt files these allow me to save the prompts that I am going to chain together or prompts that i want to run even more frequently.

Some examples of my personal frequent prompt files include a prompt file to do an LLM style markdown lint. It includes how to run the linting tool in agent mode. Instrucitons to use British English for spellings and grammar. To not change the meaning of any sentances that it wants to fix but to ensure that all sentances are well structured and accessible to a technical audience. It then includes some shorthand I use for markdown links and how to fix them. In this way when I am working on a markdown file I can invoke my markdown lint prompt with a few keystrokes and get a higher quality and consistent output for my works.

### Plan files to chain prompts or drive Agent mode

Taking this one step futher we can work with GitHub copilot to create and use a plan.md file as working memory between agent cycles to first plan out the changes we want then work the plan one step at a time to get us to the end state. 

While it is tempting to create a plan so all encompasing that the whole large scale code change is done with one hit this still isn't the way to go. I have seen best results using Agent mode to work through a plan to do one chunk at a time still. Keeping the Human developer in the loop to test and course correct along the way making the changeset small enough to still have good review in the PR.

Then move onto the next chunk.