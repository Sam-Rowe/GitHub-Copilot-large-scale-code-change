#!/usr/bin/env python3
"""
Simple static site generator for GitHub Pages
Converts markdown book files to HTML with navigation
"""

import os
import re
import markdown
from pathlib import Path
import argparse


def read_summary(book_dir):
    """Read SUMMARY.md and extract chapter information"""
    summary_path = book_dir / "SUMMARY.md"
    if not summary_path.exists():
        return []
    
    chapters = []
    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract chapter links using regex
    pattern = r'-\s*\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, content)
    
    for title, filename in matches:
        chapters.append({
            'title': title,
            'filename': filename.split('#')[0],  # Remove anchor
            'html_filename': filename.split('#')[0].replace('.md', '.html')
        })
    
    return chapters


def generate_navigation(chapters, current_file=None):
    """Generate HTML navigation menu"""
    nav_html = '''<nav class="navigation" id="navigation">
<div class="nav-header">
    <h2>Using GitHub Copilot for Large Scale Change</h2>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
        <svg class="collapse-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 3H3v18h18V3z"/>
            <path d="M9 9h6v6H9z"/>
            <path d="M3 9h6"/>
            <path d="M3 15h6"/>
        </svg>
        <svg class="expand-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M3 3h6v6H3z"/>
            <path d="M15 3h6v6h-6z"/>
            <path d="M15 15h6v6h-6z"/>
            <path d="M3 15h6v6H3z"/>
        </svg>
    </button>
</div>
<ul class="nav-list">
'''
    
    for chapter in chapters:
        class_attr = ' class="current"' if current_file == chapter['filename'] else ''
        nav_html += f'  <li{class_attr}><a href="{chapter["html_filename"]}">{chapter["title"]}</a></li>\n'
    
    nav_html += '</ul>\n</nav>\n'
    return nav_html


def generate_css():
    """Generate CSS styles for the site"""
    return """
:root {
    --primary-color: #0366d6;
    --text-color: #24292e;
    --bg-color: #ffffff;
    --border-color: #e1e4e8;
    --code-bg: #f6f8fa;
    --nav-bg: #f8f9fa;
    --nav-header-bg: #24292e;
    --nav-header-text: #ffffff;
    --shadow: rgba(0, 0, 0, 0.1);
}

@media (prefers-color-scheme: dark) {
    :root {
        --primary-color: #58a6ff;
        --text-color: #f0f6fc;
        --bg-color: #0d1117;
        --border-color: #30363d;
        --code-bg: #161b22;
        --nav-bg: #161b22;
        --nav-header-bg: #21262d;
        --nav-header-text: #f0f6fc;
        --shadow: rgba(0, 0, 0, 0.3);
    }
}

* {
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--bg-color);
    margin: 0;
    padding: 0;
    transition: background-color 0.3s ease, color 0.3s ease;
}

.container {
    display: flex;
    min-height: 100vh;
}

.navigation {
    width: 300px;
    background-color: var(--nav-bg);
    border-right: 1px solid var(--border-color);
    overflow-y: auto;
    transition: transform 0.3s ease, background-color 0.3s ease;
    position: relative;
    z-index: 1000;
}

.nav-header {
    background-color: var(--nav-header-bg);
    color: var(--nav-header-text);
    padding: 20px;
    position: sticky;
    top: 0;
    z-index: 1001;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border-color);
}

.nav-header h2 {
    margin: 0;
    font-size: 1.1em;
    font-weight: 600;
    line-height: 1.3;
}

.nav-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
    border-radius: 6px;
    transition: background-color 0.2s;
    color: var(--nav-header-text);
    position: relative;
}

.nav-toggle:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

.nav-toggle svg {
    display: block;
    transition: opacity 0.3s ease, transform 0.3s ease;
}

.collapse-icon {
    opacity: 1;
}

.expand-icon {
    position: absolute;
    top: 8px;
    left: 8px;
    opacity: 0;
}

.navigation.collapsed .collapse-icon {
    opacity: 0;
}

.navigation.collapsed .expand-icon {
    opacity: 1;
}

.hamburger {
    display: block;
    width: 20px;
    height: 2px;
    background-color: var(--nav-header-text);
    margin: 2px 0;
    transition: 0.3s;
    border-radius: 1px;
}

.nav-list {
    list-style: none;
    padding: 0;
    margin: 0;
    padding: 20px;
}

.nav-list li {
    margin-bottom: 5px;
}

.nav-list a {
    display: block;
    padding: 12px 16px;
    text-decoration: none;
    color: var(--text-color);
    border-radius: 6px;
    transition: background-color 0.2s, color 0.2s;
    font-size: 14px;
    line-height: 1.4;
}

.nav-list a:hover {
    background-color: var(--border-color);
}

.nav-list .current a {
    background-color: var(--primary-color);
    color: white;
}

.content {
    flex: 1;
    padding: 40px;
    max-width: none;
    width: 100%;
    margin: 0;
    transition: margin-left 0.3s ease;
}

/* Ensure content takes full available width */
.content > * {
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

h1, h2, h3, h4, h5, h6 {
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 600;
    line-height: 1.25;
    color: var(--text-color);
}

h1 {
    font-size: 2em;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 10px;
}

h2 {
    font-size: 1.5em;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 8px;
}

p {
    margin-bottom: 16px;
    color: var(--text-color);
}

code {
    background-color: var(--code-bg);
    padding: 2px 4px;
    border-radius: 3px;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
    font-size: 85%;
    color: var(--text-color);
}

pre {
    background-color: var(--code-bg);
    border-radius: 6px;
    padding: 16px;
    overflow: auto;
    margin-bottom: 16px;
    border: 1px solid var(--border-color);
}

pre code {
    background-color: transparent;
    padding: 0;
}

blockquote {
    border-left: 4px solid var(--border-color);
    padding-left: 16px;
    margin-left: 0;
    color: var(--text-color);
    opacity: 0.8;
}

a {
    color: var(--primary-color);
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

.footer {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid var(--border-color);
    text-align: center;
    color: var(--text-color);
    opacity: 0.7;
    font-size: 14px;
}

/* Mobile styles */
@media (max-width: 768px) {
    .navigation {
        position: fixed;
        top: 0;
        left: 0;
        height: 100vh;
        transform: translateX(-100%);
        width: 280px;
        box-shadow: 2px 0 10px var(--shadow);
    }
    
    .navigation.open {
        transform: translateX(0);
    }
    
    .nav-toggle {
        display: flex;
    }
    
    .content {
        padding: 20px;
        margin-left: 0;
        width: 100%;
    }
    
    .content.nav-open {
        margin-left: 0;
    }
    
    .mobile-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 999;
        display: none;
    }
    
    .mobile-overlay.show {
        display: block;
    }
}

/* Desktop toggle button (hidden by default) */
@media (min-width: 769px) {
    .nav-toggle {
        display: flex;
    }
    
    .navigation.collapsed {
        width: 60px;
    }
    
    .navigation.collapsed .nav-header h2 {
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s ease;
        width: 0;
        overflow: hidden;
    }
    
    .navigation.collapsed .nav-list {
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s ease;
        display: none;
    }
    
    .navigation.collapsed .nav-header {
        justify-content: center;
        padding: 20px 10px;
    }
    
    .navigation.collapsed .nav-toggle {
        position: relative;
        z-index: 1002;
    }
}
"""


def generate_html_template(title, content, navigation, is_index=False):
    """Generate complete HTML page"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - GitHub Copilot Large-Scale Code Change</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="mobile-overlay" id="mobileOverlay"></div>
    <div class="container">
        {navigation}
        <main class="content" id="content">
            {content}
            <div class="footer">
                <p>Generated from Markdown with ❤️ for GitHub Pages</p>
            </div>
        </main>
    </div>
    <script>
        // Navigation toggle functionality
        document.addEventListener('DOMContentLoaded', function() {{
            const navToggle = document.getElementById('navToggle');
            const navigation = document.getElementById('navigation');
            const content = document.getElementById('content');
            const mobileOverlay = document.getElementById('mobileOverlay');
            
            function toggleNav() {{
                const isSmallScreen = window.innerWidth <= 768;
                
                if (isSmallScreen) {{
                    // Mobile behavior
                    navigation.classList.toggle('open');
                    mobileOverlay.classList.toggle('show');
                }} else {{
                    // Desktop behavior - just collapse the navigation, don't move content
                    navigation.classList.toggle('collapsed');
                }}
            }}
            
            function closeNav() {{
                navigation.classList.remove('open');
                mobileOverlay.classList.remove('show');
            }}
            
            navToggle.addEventListener('click', toggleNav);
            mobileOverlay.addEventListener('click', closeNav);
            
            // Close mobile nav when clicking on a link
            const navLinks = navigation.querySelectorAll('a');
            navLinks.forEach(link => {{
                link.addEventListener('click', () => {{
                    if (window.innerWidth <= 768) {{
                        closeNav();
                    }}
                }});
            }});
            
            // Handle window resize
            window.addEventListener('resize', () => {{
                if (window.innerWidth > 768) {{
                    navigation.classList.remove('open');
                    mobileOverlay.classList.remove('show');
                }} else {{
                    // Reset desktop collapsed state on mobile
                    navigation.classList.remove('collapsed');
                }}
            }});
        }});
    </script>
</body>
</html>"""


def process_markdown_file(file_path, chapters, output_dir):
    """Process a single markdown file and generate HTML"""
    with open(file_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Initialize markdown processor with extensions
    md = markdown.Markdown(extensions=['codehilite', 'fenced_code', 'tables', 'toc'])
    
    # Convert markdown to HTML
    html_content = md.convert(markdown_content)
    
    # Extract title from first h1 or use filename
    title_match = re.search(r'^#\s+(.+)', markdown_content, re.MULTILINE)
    title = title_match.group(1) if title_match else file_path.stem.replace('-', ' ').title()
    
    # Generate navigation
    current_filename = file_path.name
    navigation = generate_navigation(chapters, current_filename)
    
    # Generate complete HTML
    html_page = generate_html_template(title, html_content, navigation)
    
    # Write HTML file
    output_file = output_dir / file_path.name.replace('.md', '.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_page)
    
    print(f"Generated: {output_file}")
    return output_file


def generate_index_page(chapters, output_dir, book_dir):
    """Generate index.html from introduction or README"""
    # Try to use 01-introduction.md as index, fallback to README.md
    intro_file = book_dir / "01-introduction.md"
    readme_file = book_dir.parent / "README.md"
    
    source_file = intro_file if intro_file.exists() else readme_file
    
    if source_file.exists():
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = "# GitHub Copilot Large-Scale Code Change\n\nWelcome to the book!"
    
    md = markdown.Markdown(extensions=['codehilite', 'fenced_code', 'tables', 'toc'])
    html_content = md.convert(content)
    
    navigation = generate_navigation(chapters)
    html_page = generate_html_template("Home", html_content, navigation, True)
    
    index_file = output_dir / "index.html"
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(html_page)
    
    print(f"Generated index: {index_file}")


def main():
    parser = argparse.ArgumentParser(description='Generate static site from markdown book')
    parser.add_argument('--book-dir', default='book', help='Directory containing markdown files')
    parser.add_argument('--output-dir', default='docs', help='Output directory for HTML files')
    args = parser.parse_args()
    
    book_dir = Path(args.book_dir)
    output_dir = Path(args.output_dir)
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Read chapter information from SUMMARY.md
    chapters = read_summary(book_dir)
    
    # Generate CSS file
    css_file = output_dir / "styles.css"
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(generate_css())
    print(f"Generated: {css_file}")
    
    # Process all markdown files in the book directory
    markdown_files = list(book_dir.glob("*.md"))
    markdown_files = [f for f in markdown_files if f.name != "SUMMARY.md"]
    
    for md_file in sorted(markdown_files):
        process_markdown_file(md_file, chapters, output_dir)
    
    # Generate index page
    generate_index_page(chapters, output_dir, book_dir)
    
    print(f"\nStatic site generated in '{output_dir}' directory!")
    print("To serve locally, run: python -m http.server 8000 --directory docs")
    print("Then visit: http://localhost:8000")


if __name__ == "__main__":
    main()
