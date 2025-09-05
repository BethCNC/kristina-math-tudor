#!/usr/bin/env python3
"""
Fix HTML Structure Issues for Kristina's Academic Success Dashboard
Fixes malformed attributes, duplicate classes, and spacing issues.
"""

import os
import re
from pathlib import Path

class HTMLStructureFixer:
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
    
    def fix_malformed_attributes(self, content, file_path):
        """Fix malformed HTML attributes."""
        fixes = 0
        
        # Fix duplicate class attributes
        if 'class="' in content and 'class="' in content[content.find('class="')+1:]:
            # Remove duplicate class attributes
            content = re.sub(r'class="([^"]*)"\s+class="([^"]*)"', r'class="\1 \2"', content)
            fixes += 1
            self.fixes_applied.append(f"Fixed duplicate class attributes in {file_path.name}")
        
        # Fix malformed class attributes
        content = re.sub(r'class="([^"]*)"\s+class="([^"]*)"', r'class="\1 \2"', content)
        
        # Fix duplicate border classes
        content = re.sub(r'border border-border border border-border', 'border border-border', content)
        content = re.sub(r'border border-border border border-border-hover', 'border border-border hover:border-border-hover', content)
        
        if 'border border-border border border-border' in content:
            fixes += 1
            self.fixes_applied.append(f"Fixed duplicate border classes in {file_path.name}")
        
        return content, fixes
    
    def fix_spacing_divs(self, content, file_path):
        """Remove unnecessary spacing divs."""
        fixes = 0
        
        # Remove empty spacing divs
        spacing_divs = [
            '<div class="mb-4"></div>',
            '<div class="mb-3"></div>',
            '<div class="mt-8 mb-4"></div>',
            '<div class="mt-4 mb-4"></div>',
        ]
        
        for div in spacing_divs:
            if div in content:
                content = content.replace(div, '')
                fixes += 1
                self.fixes_applied.append(f"Removed spacing divs in {file_path.name}")
        
        return content, fixes
    
    def fix_duplicate_classes(self, content, file_path):
        """Fix duplicate CSS classes."""
        fixes = 0
        
        # Fix duplicate text classes
        content = re.sub(r'text-text-primary text-text-primary', 'text-text-primary', content)
        content = re.sub(r'text-text-secondary text-text-secondary', 'text-text-secondary', content)
        
        # Fix duplicate background classes
        content = re.sub(r'bg-background bg-background', 'bg-background', content)
        content = re.sub(r'bg-background-secondary bg-background-secondary', 'bg-background-secondary', content)
        
        if 'text-text-primary text-text-primary' in content or 'bg-background bg-background' in content:
            fixes += 1
            self.fixes_applied.append(f"Fixed duplicate CSS classes in {file_path.name}")
        
        return content, fixes
    
    def add_proper_spacing(self, content, file_path):
        """Add proper spacing classes."""
        fixes = 0
        
        # Add proper spacing to main content
        if '<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">' in content:
            content = content.replace(
                '<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">',
                '<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">'
            )
            fixes += 1
            self.fixes_applied.append(f"Added proper main spacing in {file_path.name}")
        
        # Add proper spacing to sections
        content = re.sub(r'<section([^>]*class="[^"]*mb-8[^"]*")', r'<section\1', content)
        content = re.sub(r'<section([^>]*class="[^"]*")', r'<section\1 class="mb-12"', content)
        
        # Add proper spacing to grids
        content = re.sub(r'<div class="grid([^"]*)"', r'<div class="grid\1 gap-6"', content)
        
        if 'gap-6' in content:
            fixes += 1
            self.fixes_applied.append(f"Added proper grid spacing in {file_path.name}")
        
        return content, fixes
    
    def fix_file(self, file_path):
        """Fix all HTML structure issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_fixes = 0
            
            # Apply all fixes
            content, fixes = self.fix_malformed_attributes(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_spacing_divs(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_duplicate_classes(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.add_proper_spacing(content, file_path)
            total_fixes += fixes
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {total_fixes} HTML structure issues in {file_path.name}")
                return total_fixes
            else:
                print(f"ℹ️  No HTML structure fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the HTML structure fixer on all HTML files."""
        print("🔧 Starting HTML structure fixes...")
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
        print(f"🎉 HTML STRUCTURE FIXES COMPLETE")
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
    fixer = HTMLStructureFixer()
    fixer.run()
