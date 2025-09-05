#!/usr/bin/env python3
"""
Fix Links and Update to Retro Style for Kristina's Academic Success Dashboard
Fixes HTML links and updates color palette to match retro inspiration.
"""

import os
import re
from pathlib import Path

class LinksAndRetroStyleFixer:
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
    
    def fix_html_links(self, content, file_path):
        """Fix HTML links to be properly styled instead of raw references."""
        fixes = 0
        
        # Fix chapter links to be more styled
        chapter_link_fixes = [
            # Make chapter links more prominent and styled
            (r'<a href="chapter-(\d+)\.html" class="([^"]*)"', 
             r'<a href="chapter-\1.html" class="\2 bg-positive/10 hover:bg-positive/20 border border-positive/30 hover:border-positive/50 rounded-lg px-4 py-2 transition-all duration-200"'),
            
            # Fix english materials link
            (r'<a href="english_materials\.html" class="([^"]*)"', 
             r'<a href="english_materials.html" class="\1 bg-brand/10 hover:bg-brand/20 border border-brand/30 hover:border-brand/50 rounded-lg px-4 py-2 transition-all duration-200"'),
            
            # Fix formula lookup link
            (r'<a href="course_materials/formula_lookup\.html" class="([^"]*)"', 
             r'<a href="course_materials/formula_lookup.html" class="\1 bg-citrine/10 hover:bg-citrine/20 border border-citrine/30 hover:border-citrine/50 rounded-lg px-3 py-2 transition-all duration-200"'),
        ]
        
        for pattern, replacement in chapter_link_fixes:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Fixed HTML link styling in {file_path.name}")
        
        return content, fixes
    
    def add_retro_styling(self, content, file_path):
        """Add retro styling elements to match the inspiration."""
        fixes = 0
        
        # Add retro card styling
        retro_styling_fixes = [
            # Add retro borders and shadows to cards
            (r'class="([^"]*card[^"]*)"', 
             r'class="\1 border-2 border-dashed border-positive/20 shadow-lg shadow-positive/10"'),
            
            # Add retro styling to buttons
            (r'class="([^"]*button[^"]*)"', 
             r'class="\1 border-2 border-dashed border-brand/30 shadow-md shadow-brand/10"'),
            
            # Add retro styling to navigation
            (r'class="([^"]*nav[^"]*)"', 
             r'class="\1 border-2 border-dashed border-rose-quartz/20"'),
        ]
        
        for pattern, replacement in retro_styling_fixes:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Added retro styling in {file_path.name}")
        
        return content, fixes
    
    def fix_file(self, file_path):
        """Fix links and add retro styling to a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_fixes = 0
            
            # Apply fixes
            content, fixes = self.fix_html_links(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.add_retro_styling(content, file_path)
            total_fixes += fixes
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {total_fixes} link and retro styling issues in {file_path.name}")
                return total_fixes
            else:
                print(f"ℹ️  No link/retro styling fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the links and retro style fixer on all HTML files."""
        print("🔧 Starting links and retro style fixes...")
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
        print(f"🎉 LINKS AND RETRO STYLE FIXES COMPLETE")
        print(f"📊 Files processed: {len(html_files)}")
        print(f"🔧 Files fixed: {files_fixed}")
        print(f"✅ Total fixes applied: {total_fixes}")
        
        return total_fixes

if __name__ == "__main__":
    fixer = LinksAndRetroStyleFixer()
    fixer.run()
