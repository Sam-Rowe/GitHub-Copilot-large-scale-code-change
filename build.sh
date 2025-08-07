#!/bin/bash

# Build script for GitHub Copilot Large-Scale Code Change book
# This script generates a static website from markdown files

set -e

echo "🔧 Installing Python dependencies..."
pip install -r requirements.txt

echo "📝 Linting Markdown files..."
if command -v markdownlint &> /dev/null; then
    markdownlint book/*.md || echo "⚠️  Markdown linting issues found (continuing anyway)"
else
    echo "ℹ️  markdownlint not found. Install with: npm install -g markdownlint-cli"
fi

echo "🏗️  Generating static site..."
python generate_site.py --book-dir book --output-dir docs

echo "✅ Site generated successfully in 'docs' directory!"
echo ""
echo "📋 Next steps:"
echo "   • To test locally: python -m http.server 8000 --directory docs"
echo "   • Then visit: http://localhost:8000"
echo "   • Commit and push to deploy to GitHub Pages"
