#!/usr/bin/env python3
"""
Simple Spacing and Links Fixer for Kristina's Academic Success Dashboard
Uses string replacement instead of complex regex.
"""

import os
import re
from pathlib import Path

class SimpleSpacingFixer:
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
    
    def fix_file(self, file_path):
        """Fix spacing, icon, and link issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixes = 0
            
            # Simple string replacements for spacing
            spacing_fixes = [
                # Add gap to grids
                ('class="grid"', 'class="grid gap-6"'),
                ('class="grid grid-cols-1"', 'class="grid grid-cols-1 gap-6"'),
                ('class="grid grid-cols-2"', 'class="grid grid-cols-2 gap-6"'),
                ('class="grid grid-cols-3"', 'class="grid grid-cols-3 gap-6"'),
                ('class="grid grid-cols-4"', 'class="grid grid-cols-4 gap-6"'),
                
                # Add padding to cards
                ('class="card"', 'class="card p-6"'),
                ('class="bg-white rounded-lg shadow"', 'class="bg-white rounded-lg shadow p-6"'),
                ('class="bg-surface-secondary rounded-lg shadow"', 'class="bg-surface-secondary rounded-lg shadow p-6"'),
                
                # Add margin to main content
                ('<main>', '<main class="py-8 px-4">'),
                ('<main class="container">', '<main class="container py-8 px-4">'),
                
                # Add margin to sections
                ('<section>', '<section class="mb-8">'),
                ('<section class="container">', '<section class="container mb-8">'),
            ]
            
            for old, new in spacing_fixes:
                if old in content:
                    content = content.replace(old, new)
                    fixes += 1
                    self.fixes_applied.append(f"Added spacing in {file_path.name}")
            
            # Fix black text/icons that should be white
            black_fixes = [
                ('text-black', 'text-white'),
                ('text-gray-900', 'text-white'),
                ('text-gray-800', 'text-white'),
            ]
            
            for old, new in black_fixes:
                if old in content:
                    content = content.replace(old, new)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed black text contrast in {file_path.name}")
            
            # Convert markdown links to HTML
            link_fixes = [
                # Convert [text](url) to <a href="url">text</a>
                (r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" class="text-blue-600 hover:text-blue-800 underline">\1</a>'),
            ]
            
            for pattern, replacement in link_fixes:
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    fixes += 1
                    self.fixes_applied.append(f"Converted markdown links in {file_path.name}")
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {fixes} spacing/link issues in {file_path.name}")
                return fixes
            else:
                print(f"ℹ️  No spacing/link fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the simple spacing fixer on all HTML files."""
        print("🔧 Starting simple spacing and links fixes...")
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
        print(f"🎉 SIMPLE SPACING AND LINKS FIXES COMPLETE")
        print(f"📊 Files processed: {len(html_files)}")
        print(f"🔧 Files fixed: {files_fixed}")
        print(f"✅ Total fixes applied: {total_fixes}")
        
        return total_fixes

if __name__ == "__main__":
    fixer = SimpleSpacingFixer()
    fixer.run()
