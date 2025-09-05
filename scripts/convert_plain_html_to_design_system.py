#!/usr/bin/env python3
"""
Convert Plain HTML Files to Design System for Kristina's Academic Success Dashboard
Converts HTML files with inline styles to use the design system.
"""

import os
import re
from pathlib import Path

class PlainHTMLConverter:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.conversions_applied = []
        
    def find_plain_html_files(self):
        """Find HTML files that don't have the design system CSS link."""
        plain_html_files = []
        
        # Find all HTML files
        html_files = []
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.base_dir.glob(pattern))
        
        # Exclude dist, node_modules, and report files
        html_files = [f for f in html_files if f.is_file() and not any(part in str(f) for part in ['dist', 'node_modules', 'accessibility_report', 'link_check_report', 'color_accessibility_report']) and f.name not in ['accessibility_report.html', 'link_check_report.html', 'color_accessibility_report.html']]
        
        # Check which files don't have the design system CSS link
        for html_file in html_files:
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if it has the design system CSS link
                if 'globals.css' not in content and 'src/styles/globals.css' not in content:
                    plain_html_files.append(html_file)
                    
            except Exception as e:
                print(f"Error reading {html_file}: {e}")
        
        return plain_html_files
    
    def convert_to_design_system(self, html_file):
        """Convert a plain HTML file to use the design system."""
        try:
            # Read the file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title from the content
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            title = title_match.group(1) if title_match else "Course Materials"
            
            # Extract body content (everything between <body> and </body>)
            body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
            body_content = body_match.group(1) if body_match else content
            
            # Clean up the body content - remove inline styles and convert to design system classes
            body_content = self.clean_body_content(body_content)
            
            # Create new HTML with design system
            new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Kristina's Academic Success Dashboard</title>
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
                            <h1 class="font-title-small text-text-primary">{title}</h1>
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
                {body_content}
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
            
            return new_html
            
        except Exception as e:
            print(f"Error converting {html_file}: {e}")
            return None
    
    def clean_body_content(self, body_content):
        """Clean up body content by removing inline styles and converting to design system classes."""
        # Remove inline styles
        body_content = re.sub(r'style="[^"]*"', '', body_content)
        
        # Convert common elements to design system classes
        body_content = re.sub(r'<h1([^>]*)>', r'<h1\1 class="text-3xl font-bold text-text-primary mb-6">', body_content)
        body_content = re.sub(r'<h2([^>]*)>', r'<h2\1 class="text-2xl font-semibold text-text-primary mb-4">', body_content)
        body_content = re.sub(r'<h3([^>]*)>', r'<h3\1 class="text-xl font-medium text-text-primary mb-3">', body_content)
        body_content = re.sub(r'<p([^>]*)>', r'<p\1 class="text-text-secondary mb-4">', body_content)
        body_content = re.sub(r'<ul([^>]*)>', r'<ul\1 class="list-disc list-inside text-text-secondary mb-4 space-y-2">', body_content)
        body_content = re.sub(r'<ol([^>]*)>', r'<ol\1 class="list-decimal list-inside text-text-secondary mb-4 space-y-2">', body_content)
        body_content = re.sub(r'<li([^>]*)>', r'<li\1 class="text-text-secondary">', body_content)
        body_content = re.sub(r'<table([^>]*)>', r'<table\1 class="w-full border-collapse border border-border mb-4">', body_content)
        body_content = re.sub(r'<th([^>]*)>', r'<th\1 class="border border-border bg-background-secondary text-text-primary font-semibold p-3">', body_content)
        body_content = re.sub(r'<td([^>]*)>', r'<td\1 class="border border-border text-text-secondary p-3">', body_content)
        
        return body_content
    
    def update_file(self, html_file, new_content):
        """Update the HTML file with the new design system content."""
        try:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            self.conversions_applied.append(f"Converted {html_file.name} to design system")
            return True
            
        except Exception as e:
            print(f"Error updating {html_file}: {e}")
            return False
    
    def run(self):
        """Run the plain HTML to design system converter."""
        print("🔧 Starting plain HTML to design system conversion...")
        print("=" * 60)
        
        plain_html_files = self.find_plain_html_files()
        print(f"📄 Found {len(plain_html_files)} plain HTML files to convert")
        
        total_conversions = 0
        
        for html_file in plain_html_files:
            print(f"🔄 Converting {html_file.name}...")
            
            # Convert to design system
            new_content = self.convert_to_design_system(html_file)
            if new_content:
                # Update the file
                if self.update_file(html_file, new_content):
                    total_conversions += 1
                    print(f"✅ Converted {html_file.name}")
        
        print("=" * 60)
        print(f"🎉 PLAIN HTML TO DESIGN SYSTEM CONVERSION COMPLETE")
        print(f"📊 Files converted: {total_conversions}")
        
        if self.conversions_applied:
            print("\n📋 Conversions applied:")
            for conversion in self.conversions_applied:
                print(f"  • {conversion}")
        
        return total_conversions

if __name__ == "__main__":
    converter = PlainHTMLConverter()
    converter.run()
