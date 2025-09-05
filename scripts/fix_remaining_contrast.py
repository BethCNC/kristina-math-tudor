#!/usr/bin/env python3
"""
Fix Remaining Contrast Issues for Kristina's Academic Success Dashboard
Targets light blue on light blue and light grey on light beige contrast problems.
"""

import os
import re
from pathlib import Path

class RemainingContrastFixer:
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
    
    def fix_light_blue_contrast(self, content, file_path):
        """Fix light blue text/icons on light blue backgrounds."""
        fixes = 0
        
        # Fix light blue text that should be darker
        blue_fixes = [
            # Light blue text that should be darker blue
            (r'text-blue-300', 'text-blue-800'),
            (r'text-blue-400', 'text-blue-800'),
            (r'text-blue-500', 'text-blue-800'),
            
            # Light blue icons that should be darker
            (r'<i data-lucide="brain"[^>]*class="[^"]*text-blue-300[^"]*"', 
             lambda m: m.group(0).replace('text-blue-300', 'text-blue-800')),
            (r'<i data-lucide="brain"[^>]*class="[^"]*text-blue-400[^"]*"', 
             lambda m: m.group(0).replace('text-blue-400', 'text-blue-800')),
            (r'<i data-lucide="plus"[^>]*class="[^"]*text-blue-300[^"]*"', 
             lambda m: m.group(0).replace('text-blue-300', 'text-blue-800')),
            (r'<i data-lucide="plus"[^>]*class="[^"]*text-blue-400[^"]*"', 
             lambda m: m.group(0).replace('text-blue-400', 'text-blue-800')),
            
            # Any light blue text classes
            (r'class="[^"]*text-blue-300[^"]*"', 'class="text-blue-800"'),
            (r'class="[^"]*text-blue-400[^"]*"', 'class="text-blue-800"'),
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
    
    def fix_light_grey_contrast(self, content, file_path):
        """Fix light grey text on light beige backgrounds."""
        fixes = 0
        
        # Fix light grey text that should be darker
        grey_fixes = [
            # Light grey text that should be darker
            (r'text-gray-400', 'text-gray-700'),
            (r'text-gray-500', 'text-gray-700'),
            (r'text-gray-600', 'text-gray-700'),
            
            # Any light grey text classes
            (r'class="[^"]*text-gray-400[^"]*"', 'class="text-gray-700"'),
            (r'class="[^"]*text-gray-500[^"]*"', 'class="text-gray-700"'),
            (r'class="[^"]*text-gray-600[^"]*"', 'class="text-gray-700"'),
        ]
        
        for pattern, replacement in grey_fixes:
            if pattern in content:
                content = content.replace(pattern, replacement)
                fixes += 1
                self.fixes_applied.append(f"Fixed grey text contrast in {file_path.name}")
        
        return content, fixes
    
    def fix_beige_background_contrast(self, content, file_path):
        """Fix text/icons on beige backgrounds."""
        fixes = 0
        
        # Fix text on beige backgrounds
        beige_fixes = [
            # Text that should be darker on beige
            (r'bg-beige.*?text-gray-400', 'bg-beige text-gray-700'),
            (r'bg-beige.*?text-gray-500', 'bg-beige text-gray-700'),
            (r'bg-beige.*?text-blue-300', 'bg-beige text-blue-800'),
            (r'bg-beige.*?text-blue-400', 'bg-beige text-blue-800'),
            
            # Icons that should be darker on beige
            (r'bg-beige.*?<i[^>]*class="[^"]*text-blue-300[^"]*"', 
             lambda m: m.group(0).replace('text-blue-300', 'text-blue-800')),
            (r'bg-beige.*?<i[^>]*class="[^"]*text-blue-400[^"]*"', 
             lambda m: m.group(0).replace('text-blue-400', 'text-blue-800')),
        ]
        
        for pattern, replacement in beige_fixes:
            if callable(replacement):
                # For complex replacements
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed beige background contrast in {file_path.name}")
            else:
                # For simple replacements
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed beige text contrast in {file_path.name}")
        
        return content, fixes
    
    def fix_file(self, file_path):
        """Fix all remaining contrast issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_fixes = 0
            
            # Apply all fixes
            content, fixes = self.fix_light_blue_contrast(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_light_grey_contrast(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_beige_background_contrast(content, file_path)
            total_fixes += fixes
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {total_fixes} remaining contrast issues in {file_path.name}")
                return total_fixes
            else:
                print(f"ℹ️  No remaining contrast fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the remaining contrast fixer on all HTML files."""
        print("🎨 Starting remaining contrast fixes...")
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
        print(f"🎉 REMAINING CONTRAST FIXES COMPLETE")
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
    fixer = RemainingContrastFixer()
    fixer.run()
