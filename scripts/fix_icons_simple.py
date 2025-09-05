#!/usr/bin/env python3
"""
Ultra Simple Icon Accessibility Fixer
Uses string replacement instead of complex regex.
"""

import os
import re
from pathlib import Path

class UltraSimpleIconFixer:
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
        """Fix icon accessibility issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixes = 0
            
            # Remove duplicate aria-labels first
            content = re.sub(r'aria-label="([^"]*)"\s+aria-label="\1"', r'aria-label="\1"', content)
            
            # Simple string replacements for common icons without aria-labels
            icon_fixes = [
                # Navigation icons
                ('<i data-lucide="arrow-left" class="w-4 h-4 mr-2">', '<i data-lucide="arrow-left" class="w-4 h-4 mr-2" aria-label="Go back">'),
                ('<i data-lucide="arrow-right" class="w-4 h-4 mr-2">', '<i data-lucide="arrow-right" class="w-4 h-4 mr-2" aria-label="Go forward">'),
                ('<i data-lucide="arrow-up" class="w-4 h-4 mr-2">', '<i data-lucide="arrow-up" class="w-4 h-4 mr-2" aria-label="Go up">'),
                ('<i data-lucide="arrow-down" class="w-4 h-4 mr-2">', '<i data-lucide="arrow-down" class="w-4 h-4 mr-2" aria-label="Go down">'),
                
                # Content icons
                ('<i data-lucide="lightbulb" class="w-6 h-6 text-text-primary">', '<i data-lucide="lightbulb" class="w-6 h-6 text-text-primary" aria-label="Idea">'),
                ('<i data-lucide="key" class="w-5 h-5 mr-2 text-positive">', '<i data-lucide="key" class="w-5 h-5 mr-2 text-positive" aria-label="Key">'),
                
                # Common patterns
                ('<i data-lucide="lightbulb"', '<i data-lucide="lightbulb" aria-label="Idea"'),
                ('<i data-lucide="key"', '<i data-lucide="key" aria-label="Key"'),
                ('<i data-lucide="arrow-down"', '<i data-lucide="arrow-down" aria-label="Go down"'),
                ('<i data-lucide="arrow-up"', '<i data-lucide="arrow-up" aria-label="Go up"'),
            ]
            
            for old, new in icon_fixes:
                if old in content and 'aria-label=' not in old:
                    content = content.replace(old, new)
                    fixes += 1
                    self.fixes_applied.append(f"Added aria-label to icon in {file_path.name}")
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {fixes} icon accessibility issues in {file_path.name}")
                return fixes
            else:
                print(f"ℹ️  No icon accessibility fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the icon accessibility fixer on all HTML files."""
        print("🎯 Starting ultra simple icon accessibility fixes...")
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
        print(f"🎉 ICON ACCESSIBILITY FIXES COMPLETE")
        print(f"📊 Files processed: {len(html_files)}")
        print(f"🔧 Files fixed: {files_fixed}")
        print(f"✅ Total fixes applied: {total_fixes}")
        
        return total_fixes

if __name__ == "__main__":
    fixer = UltraSimpleIconFixer()
    fixer.run()
