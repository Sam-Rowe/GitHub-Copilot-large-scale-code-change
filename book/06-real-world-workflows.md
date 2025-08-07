# Real-World (Style) Workflows

Real world this is changing so fast. What has worked for customers and myself depends on the features I have available to hand. For example building out a list of prompts has worked well for me in the past but with Agent mode it is becoming less relevant to have a list of structured prompts to run one after another than to work on patterns of prompts that can be used in an Agent mode conversation. I suspect in the near future I will have to update this further to account for new ways of working in a fully Agentic way.

## End-to-end walkthroughs

Take a repo like https://github.com/Sam-Rowe/i-ching which I used these practices with to convert from a Node Library to a Swift library https://github.com/Sam-Rowe/IChing-Swift-Library

The first step was to improve the tests that existed. I needed to be able to see when the swift version was deviating from the behaviour of the swift version. Increasing the test coverage and improving the reliability of those tests was important to give me a solid foundation for the change. In this case i offered back a PR to the original author so that the work I was building upon was also updated. At the time of writing that hasn't been merged yet.

Step 2 was to start the new Swift library the initial framework was setup in the IDE as you would normally then i started to work on the code changes. This is where giving AI a chunk of Node code and asking for the essential algorithm's from it, looking for like libraries to use in Swift and building out a plan to convert it to Swift was essential. That plan was then used to start working on the tests in Swift before I could work on implementing the library. 

There was plenty of iterations as i added more tests and more code with GitHub Copliot's help to fill out the swift library to a working state where the tests pass and I had a working CLI tool to use it the same I do for the Node JS version.

## Handling legacy codebases

With large legacy codebases the important part is to break down the code into small enough chunks that can be worked upon within the context of the model.

This usually requires a domain expert who has previous experience of the codebase or of the domain the code is functioning in so that they can prise the code up into smaller chunks that can be worked on independently.

