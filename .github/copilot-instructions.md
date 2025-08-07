the book/*.md files are Markdown files that contain the book. All contents must be well formatted Markdown.
Use `markdownlint **/*.md` to run the markdown linter on all Markdown files in the book directory.
The book is written in British English, so please highlight any spelling and grammar issues that do not conform to British English standards.
Adhere to STYLE_GUIDE.md for voice, terminology, inclusive language, and structural conventions when generating or editing book content. Always include a Key Takeaways section and apply the Quality Checklist before finalising changes.
The build.sh script is responsible for building the static site from the Markdown files. It should be run from the root of the repository after installing the python dependencies in requirements.txt.