# GitHub Copilot for Large-Scale Code Change

A comprehensive guide to using GitHub Copilot for large-scale code changes, refactoring, and modernisation projects.

## 📖 The Book

The book is located in the [`book/`](./book/) directory and can be read as markdown files. See the [Table of Contents](./book/SUMMARY.md) for navigation.

**🌐 [Read the Book Online](https://sam-rowe.github.io/GitHub-Copilot-large-scale-code-change/)**

## 🚀 Building the Website

This repository includes a static site generator that converts the markdown book into a beautiful website for GitHub Pages.

### Quick Start

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Build the site:**

   ```bash
   ./build.sh
   ```

3. **Test locally:**

   ```bash
   python -m http.server 8000 --directory docs
   # Visit http://localhost.8000
   ```

### Manual Build

You can also run the generator directly:

```bash
python generate_site.py --book-dir book --output-dir docs
```

### GitHub Pages Deployment

The site automatically deploys to GitHub Pages when you push to the `main` branch. The GitHub Actions workflow will:

1. Install dependencies
2. Lint markdown files
3. Generate the static site
4. Deploy to GitHub Pages

## 📝 Contributing

When editing the book:

1. All content should be in well-formatted Markdown
2. Use British English spelling and grammar
3. Run the linter to check formatting: `markdownlint book/*.md`

## 📁 Project Structure

```text
├── book/                    # Book content (Markdown files)
│   ├── SUMMARY.md          # Table of contents
│   ├── 01-introduction.md  # Chapter files
│   └── ...
├── docs/                   # Generated website (auto-generated)
├── .github/workflows/      # GitHub Actions for deployment
├── generate_site.py        # Static site generator
├── build.sh               # Build script
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## 🛠️ Technical Details

The static site generator:

- Converts Markdown to HTML using Python `markdown` library
- Generates navigation from `SUMMARY.md`
- Creates responsive design with mobile support
- Includes syntax highlighting for code blocks
- Follows GitHub's design principles

## 📋 Todo

Drafts:

- [x] Section 1
- [x] Section 2
- [x] Section 3
- [x] Section 4
- [x] Section 5
- [x] Section 6
- [x] Section 7
- [x] Section 8
- [x] Section 9
- [ ] Check references and updates
- [ ] Consider the competitive landscape and weave that into section 3 and 6
- [ ] Where does Copilot break down and how to make that a positive narrative to add into the book?
