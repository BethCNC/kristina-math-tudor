#!/usr/bin/env python3
"""
Fix Critical Contrast Issues for Kristina's Academic Success Dashboard
Targets specific orange-on-orange and black-on-black contrast problems.
"""

import os
import re
from pathlib import Path

class CriticalContrastFixer:
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
    
    def fix_orange_on_orange_text(self, content, file_path):
        """Fix orange text on orange background issues."""
        fixes = 0
        
        # Fix orange text on orange backgrounds
        orange_fixes = [
            # Urgent deadlines card - make text white for contrast
            (r'class="[^"]*bg-orange[^"]*"[^>]*>.*?<[^>]*class="[^"]*text-orange[^"]*"', 
             lambda m: m.group(0).replace('text-orange', 'text-white')),
            
            # Orange text classes that should be white on orange backgrounds
            (r'text-orange-400', 'text-white'),
            (r'text-orange-500', 'text-white'),
            (r'text-orange-600', 'text-white'),
            (r'text-orange-700', 'text-white'),
            (r'text-orange-800', 'text-white'),
            (r'text-orange-900', 'text-white'),
            
            # Specific orange text that should be white
            (r'class="[^"]*text-orange[^"]*"', 'class="text-white"'),
        ]
        
        for pattern, replacement in orange_fixes:
            if callable(replacement):
                # For complex replacements
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed orange-on-orange text in {file_path.name}")
            else:
                # For simple replacements
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed orange text contrast in {file_path.name}")
        
        return content, fixes
    
    def fix_black_on_black_icons(self, content, file_path):
        """Fix black icons on black backgrounds."""
        fixes = 0
        
        # Fix black icons on dark backgrounds
        icon_fixes = [
            # Calendar icon - make it white
            (r'<i data-lucide="calendar"[^>]*class="[^"]*text-black[^"]*"', 
             lambda m: m.group(0).replace('text-black', 'text-white')),
            (r'<i data-lucide="calendar"[^>]*class="[^"]*text-gray-900[^"]*"', 
             lambda m: m.group(0).replace('text-gray-900', 'text-white')),
            (r'<i data-lucide="calendar"[^>]*class="[^"]*text-gray-800[^"]*"', 
             lambda m: m.group(0).replace('text-gray-800', 'text-white')),
            
            # Book icon - make it white
            (r'<i data-lucide="book"[^>]*class="[^"]*text-black[^"]*"', 
             lambda m: m.group(0).replace('text-black', 'text-white')),
            (r'<i data-lucide="book"[^>]*class="[^"]*text-gray-900[^"]*"', 
             lambda m: m.group(0).replace('text-gray-900', 'text-white')),
            (r'<i data-lucide="book"[^>]*class="[^"]*text-gray-800[^"]*"', 
             lambda m: m.group(0).replace('text-gray-800', 'text-white')),
            
            # Any black text on dark backgrounds
            (r'text-black', 'text-white'),
            (r'text-gray-900', 'text-white'),
            (r'text-gray-800', 'text-white'),
        ]
        
        for pattern, replacement in icon_fixes:
            if callable(replacement):
                # For complex replacements
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed black-on-black icon in {file_path.name}")
            else:
                # For simple replacements
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed black text contrast in {file_path.name}")
        
        return content, fixes
    
    def fix_light_blue_on_light_blue(self, content, file_path):
        """Fix light blue icons on light blue backgrounds."""
        fixes = 0
        
        # Fix light blue text/icons on light blue backgrounds
        blue_fixes = [
            # Light blue text that should be darker
            (r'text-blue-300', 'text-blue-800'),
            (r'text-blue-400', 'text-blue-800'),
            (r'text-blue-500', 'text-blue-800'),
            
            # Light blue icons that should be darker
            (r'<i data-lucide="[^"]*"[^>]*class="[^"]*text-blue-300[^"]*"', 
             lambda m: m.group(0).replace('text-blue-300', 'text-blue-800')),
            (r'<i data-lucide="[^"]*"[^>]*class="[^"]*text-blue-400[^"]*"', 
             lambda m: m.group(0).replace('text-blue-400', 'text-blue-800')),
        ]
        
        for pattern, replacement in blue_fixes:
            if callable(replacement):
                # For complex replacements
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed light blue contrast in {file_path.name}")
            else:
                # For simple replacements
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed blue text contrast in {file_path.name}")
        
        return content, fixes
    
    def fix_file(self, file_path):
        """Fix all critical contrast issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_fixes = 0
            
            # Apply all fixes
            content, fixes = self.fix_orange_on_orange_text(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_black_on_black_icons(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_light_blue_on_light_blue(content, file_path)
            total_fixes += fixes
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {total_fixes} critical contrast issues in {file_path.name}")
                return total_fixes
            else:
                print(f"ℹ️  No critical contrast fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the critical contrast fixer on all HTML files."""
        print("🚨 Starting critical contrast fixes...")
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
        print(f"🎉 CRITICAL CONTRAST FIXES COMPLETE")
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
    fixer = CriticalContrastFixer()
    fixer.run()
