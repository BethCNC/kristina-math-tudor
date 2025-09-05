#!/usr/bin/env python3
"""
Convert Markdown Files to HTML Pages for Kristina's Academic Success Dashboard
Converts all linked markdown files to proper HTML pages with the design system.
"""

import os
import re
from pathlib import Path
import markdown

class MarkdownToHTMLConverter:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.conversions_applied = []
        
    def find_markdown_files(self):
        """Find all markdown files that are linked to in HTML files."""
        markdown_files = []
        
        # Find all HTML files
        html_files = []
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.base_dir.glob(pattern))
        
        # Exclude dist, node_modules, and report files
        html_files = [f for f in html_files if f.is_file() and not any(part in str(f) for part in ['dist', 'node_modules', 'accessibility_report', 'link_check_report', 'color_accessibility_report']) and f.name not in ['accessibility_report.html', 'link_check_report.html', 'color_accessibility_report.html']]
        
        # Find markdown files referenced in HTML
        for html_file in html_files:
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find markdown file references
                markdown_refs = re.findall(r'href="([^"]*\.md)"', content)
                for ref in markdown_refs:
                    # Resolve relative paths
                    if ref.startswith('course_materials/'):
                        md_file = self.base_dir / ref
                    else:
                        md_file = html_file.parent / ref
                    
                    if md_file.exists() and md_file not in markdown_files:
                        markdown_files.append(md_file)
                        
            except Exception as e:
                print(f"Error reading {html_file}: {e}")
        
        return markdown_files
    
    def convert_markdown_to_html(self, md_file):
        """Convert a markdown file to HTML with the design system."""
        try:
            # Read markdown content
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            # Convert markdown to HTML
            html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
            
            # Create HTML page with design system
            html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.get_title_from_markdown(md_content)} - Kristina's Academic Success Dashboard</title>
    <meta name="description" content="Course materials and resources for MAT 143 and ENG 111.">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/public/favicons/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/public/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/public/favicons/favicon-16x16.png">
    
    <!-- Design System -->
    <link rel="stylesheet" href="src/styles/globals.css">
    
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
</head>
<body class="bg-background text-text-primary font-sans antialiased">
    <!-- Header -->
    <header class="bg-background-secondary border border-border/50 backdrop-blur-sm border-b border-border sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <div class="flex items-center space-x-4">
                    <div class="flex items-center space-x-3">
                        <div class="w-8 h-8 rounded-lg bg-brand text-text-primary flex items-center justify-center">
                            <i data-lucide="book-open" class="w-5 h-5 text-text-primary" aria-label="Course materials"></i>
                        </div>
                        <div>
                            <h1 class="font-title-small text-text-primary">{self.get_title_from_markdown(md_content)}</h1>
                            <p class="font-caption text-text-secondary">Course Materials</p>
                        </div>
                    </div>
                </div>
                
                <nav class="hidden md:flex items-center space-x-1" role="navigation" aria-label="Main navigation">
                    <a href="../index.html" class="px-3 py-2 rounded-md font-button text-text-primary hover:bg-background-secondary border border-border border border-border-hover transition-colors">Home</a>
                    <a href="../calendar.html" class="px-3 py-2 rounded-md font-button text-text-primary hover:bg-background-secondary border border-border border border-border-hover transition-colors">Calendar</a>
                    <a href="../tutor.html" class="px-3 py-2 rounded-md font-button text-text-primary hover:bg-background-secondary border border-border border border-border-hover transition-colors">Tutor</a>
                </nav>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="bg-background-secondary border border-border rounded-xl p-8">
            <div class="prose prose-lg max-w-none">
                {html_content}
            </div>
        </div>
    </main>

    <footer class="bg-background-secondary border-t border-border mt-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
            <div class="text-center">
                <p class="font-caption text-text-secondary">&copy; 2025 Kristina's Academic Success Dashboard. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Initialize Lucide Icons -->
    <script>
        lucide.createIcons();
    </script>
</body>
</html>"""
            
            return html_page
            
        except Exception as e:
            print(f"Error converting {md_file}: {e}")
            return None
    
    def get_title_from_markdown(self, md_content):
        """Extract title from markdown content."""
        lines = md_content.split('\n')
        for line in lines:
            if line.startswith('# '):
                return line[2:].strip()
        return "Course Materials"
    
    def create_html_file(self, md_file, html_content):
        """Create HTML file from markdown content."""
        # Determine output path
        if 'course_materials' in str(md_file):
            # For course_materials files, create HTML in the same directory
            html_file = md_file.with_suffix('.html')
        else:
            # For other files, create in root directory
            html_file = self.base_dir / f"{md_file.stem}.html"
        
        try:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.conversions_applied.append(f"Created {html_file.name} from {md_file.name}")
            return html_file
            
        except Exception as e:
            print(f"Error creating {html_file}: {e}")
            return None
    
    def update_html_links(self, html_file, md_file, new_html_file):
        """Update HTML files to link to the new HTML file instead of markdown."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace markdown links with HTML links
            old_link = str(md_file.relative_to(self.base_dir))
            new_link = str(new_html_file.relative_to(self.base_dir))
            
            if old_link in content:
                content = content.replace(old_link, new_link)
                
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.conversions_applied.append(f"Updated links in {html_file.name}")
                return True
                
        except Exception as e:
            print(f"Error updating {html_file}: {e}")
            return False
        
        return False
    
    def run(self):
        """Run the markdown to HTML converter."""
        print("🔧 Starting markdown to HTML conversion...")
        print("=" * 60)
        
        markdown_files = self.find_markdown_files()
        print(f"📄 Found {len(markdown_files)} markdown files to convert")
        
        total_conversions = 0
        
        for md_file in markdown_files:
            print(f"🔄 Converting {md_file.name}...")
            
            # Convert markdown to HTML
            html_content = self.convert_markdown_to_html(md_file)
            if html_content:
                # Create HTML file
                html_file = self.create_html_file(md_file, html_content)
                if html_file:
                    total_conversions += 1
                    print(f"✅ Created {html_file.name}")
        
        print("=" * 60)
        print(f"🎉 MARKDOWN TO HTML CONVERSION COMPLETE")
        print(f"📊 Files converted: {total_conversions}")
        
        if self.conversions_applied:
            print("\n📋 Conversions applied:")
            for conversion in self.conversions_applied:
                print(f"  • {conversion}")
        
        return total_conversions

if __name__ == "__main__":
    converter = MarkdownToHTMLConverter()
    converter.run()
