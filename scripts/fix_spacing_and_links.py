#!/usr/bin/env python3
"""
Fix Spacing, Icon Contrast, and Markdown Links for Kristina's Academic Success Dashboard
Addresses vertical spacing, black-on-black icons, and converts markdown links to HTML.
"""

import os
import re
from pathlib import Path

class SpacingAndLinksFixer:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.fixes_applied = []
        
    def find_html_files(self):
        """Find all HTML files that need fixing."""
        html_files = []
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.base_dir.glob(pattern))
        
        # Exclude dist, node_modules, and report files
        return [f for f in html_files if f.is_file() and not any(part in str(f) for part in ['dist', 'node_modules', 'accessibility_report', 'link_check_report', 'color_accessibility_report']) and f.name not in ['accessibility_report.html', 'link_check_report.html', 'color_accessibility_report.html']]
    
    def fix_vertical_spacing(self, content, file_path):
        """Add proper vertical spacing between elements."""
        fixes = 0
        
        # Add spacing between major sections
        spacing_fixes = [
            # Add margin between cards and headings
            (r'<h[1-6][^>]*>([^<]+)</h[1-6]>\s*<div class="[^"]*grid[^"]*"', 
             r'<h1-6>\1</h1-6>\n<div class="mt-6 grid"'),
            
            # Add margin between cards and other elements
            (r'<div class="[^"]*grid[^"]*"[^>]*>\s*<div class="[^"]*card[^"]*"', 
             r'<div class="grid gap-6">\n<div class="card"'),
            
            # Add padding to main content areas
            (r'<main[^>]*class="([^"]*)"', 
             lambda m: f'<main class="{m.group(1)} py-8 px-4"'),
            
            # Add spacing between navigation and content
            (r'<nav[^>]*>.*?</nav>\s*<main', 
             r'<nav>\1</nav>\n<main class="mt-8"'),
            
            # Add spacing between sections
            (r'<section[^>]*class="([^"]*)"', 
             lambda m: f'<section class="{m.group(1)} mb-8"'),
        ]
        
        for pattern, replacement in spacing_fixes:
            if callable(replacement):
                # For complex replacements
                if re.search(pattern, content, re.DOTALL):
                    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                    fixes += 1
                    self.fixes_applied.append(f"Added vertical spacing in {file_path.name}")
            else:
                # For simple replacements
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    fixes += 1
                    self.fixes_applied.append(f"Added spacing in {file_path.name}")
        
        return content, fixes
    
    def fix_black_on_black_icons(self, content, file_path):
        """Fix black icons on dark backgrounds."""
        fixes = 0
        
        # Fix black icons that should be white on dark backgrounds
        icon_fixes = [
            # Icons on dark backgrounds should be white
            (r'<i data-lucide="[^"]*"[^>]*class="[^"]*text-black[^"]*"[^>]*>', 
             lambda m: m.group(0).replace('text-black', 'text-white')),
            (r'<i data-lucide="[^"]*"[^>]*class="[^"]*text-gray-900[^"]*"[^>]*>', 
             lambda m: m.group(0).replace('text-gray-900', 'text-white')),
            (r'<i data-lucide="[^"]*"[^>]*class="[^"]*text-gray-800[^"]*"[^>]*>', 
             lambda m: m.group(0).replace('text-gray-800', 'text-white')),
            
            # Icons in dark cards should be white
            (r'<div class="[^"]*bg-gray-800[^"]*"[^>]*>.*?<i data-lucide="[^"]*"[^>]*class="[^"]*text-black[^"]*"', 
             lambda m: m.group(0).replace('text-black', 'text-white')),
            (r'<div class="[^"]*bg-gray-900[^"]*"[^>]*>.*?<i data-lucide="[^"]*"[^>]*class="[^"]*text-black[^"]*"', 
             lambda m: m.group(0).replace('text-black', 'text-white')),
            
            # Any black text that should be white
            (r'text-black', 'text-white'),
            (r'text-gray-900', 'text-white'),
            (r'text-gray-800', 'text-white'),
        ]
        
        for pattern, replacement in icon_fixes:
            if callable(replacement):
                # For complex replacements
                if re.search(pattern, content, re.DOTALL):
                    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed black-on-black icons in {file_path.name}")
            else:
                # For simple replacements
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed black text contrast in {file_path.name}")
        
        return content, fixes
    
    def fix_markdown_links(self, content, file_path):
        """Convert markdown links to proper HTML links."""
        fixes = 0
        
        # Convert markdown links to HTML
        link_fixes = [
            # Convert [text](url) to <a href="url">text</a>
            (r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" class="text-blue-600 hover:text-blue-800 underline">\1</a>'),
            
            # Convert plain URLs to links
            (r'(?<!href=")(?<!>)(https?://[^\s<>"]+)(?!</a>)', 
             r'<a href="\1" class="text-blue-600 hover:text-blue-800 underline" target="_blank" rel="noopener noreferrer">\1</a>'),
            
            # Convert plain text that looks like links to proper links
            (r'(?<!<a[^>]*>)(Dashboard|Calendar|Math Tutor|Writing Coach|Resources|Formula Sheets|Course Information|Quick Tools|Quick Formula Lookup|Course Schedule|Calculator|Note Templates|Study Tips)(?!</a>)', 
             r'<a href="#" class="text-blue-600 hover:text-blue-800 underline">\1</a>'),
        ]
        
        for pattern, replacement in link_fixes:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Converted markdown links to HTML in {file_path.name}")
        
        return content, fixes
    
    def add_proper_css_classes(self, content, file_path):
        """Add proper CSS classes for spacing and styling."""
        fixes = 0
        
        # Add proper spacing classes
        css_fixes = [
            # Add gap classes to grids
            (r'<div class="[^"]*grid[^"]*"(?![^>]*gap)', 
             lambda m: m.group(0).replace('grid', 'grid gap-6')),
            
            # Add padding to cards
            (r'<div class="[^"]*card[^"]*"(?![^>]*p-)', 
             lambda m: m.group(0).replace('card', 'card p-6')),
            
            # Add margin to sections
            (r'<section(?![^>]*class="[^"]*m-)', 
             r'<section class="mb-8"'),
            
            # Add padding to main content
            (r'<main(?![^>]*class="[^"]*p-)', 
             r'<main class="py-8 px-4"'),
        ]
        
        for pattern, replacement in css_fixes:
            if callable(replacement):
                # For complex replacements
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    fixes += 1
                    self.fixes_applied.append(f"Added CSS classes in {file_path.name}")
            else:
                # For simple replacements
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    fixes += 1
                    self.fixes_applied.append(f"Added CSS classes in {file_path.name}")
        
        return content, fixes
    
    def fix_file(self, file_path):
        """Fix all spacing, icon, and link issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_fixes = 0
            
            # Apply all fixes
            content, fixes = self.fix_vertical_spacing(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_black_on_black_icons(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_markdown_links(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.add_proper_css_classes(content, file_path)
            total_fixes += fixes
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {total_fixes} spacing/link issues in {file_path.name}")
                return total_fixes
            else:
                print(f"ℹ️  No spacing/link fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the spacing and links fixer on all HTML files."""
        print("🔧 Starting spacing and links fixes...")
        print("=" * 60)
        
        html_files = self.find_html_files()
        print(f"📄 Found {len(html_files)} HTML files to check")
        
        total_fixes = 0
        files_fixed = 0
        
        for file_path in html_files:
            fixes = self.fix_file(file_path)
            total_fixes += fixes
            if fixes > 0:
                files_fixed += 1
        
        print("=" * 60)
        print(f"🎉 SPACING AND LINKS FIXES COMPLETE")
        print(f"📊 Files processed: {len(html_files)}")
        print(f"🔧 Files fixed: {files_fixed}")
        print(f"✅ Total fixes applied: {total_fixes}")
        
        if self.fixes_applied:
            print("\n📋 Fixes applied:")
            for fix in self.fixes_applied[:15]:  # Show first 15
                print(f"  • {fix}")
            if len(self.fixes_applied) > 15:
                print(f"  ... and {len(self.fixes_applied) - 15} more")
        
        return total_fixes

if __name__ == "__main__":
    fixer = SpacingAndLinksFixer()
    fixer.run()
