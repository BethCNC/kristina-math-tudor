#!/usr/bin/env python3
"""
Fix Remaining Broken Links for Kristina's Academic Success Dashboard
Fixes the final issues: duplicate paths, missing favicons, and malformed links.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

class RemainingLinkFixer:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.fixes_applied = []
        
    def find_html_files(self):
        """Find all HTML files that need fixing."""
        html_files = []
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.base_dir.glob(pattern))
        
        # Exclude dist, node_modules, and report files
        return [f for f in html_files if f.is_file() and not any(part in str(f) for part in ['dist', 'node_modules', 'accessibility_report', 'link_check_report']) and f.name not in ['accessibility_report.html', 'link_check_report.html']]
    
    def fix_duplicate_course_materials_paths(self, content, file_path):
        """Fix duplicate course_materials paths."""
        fixes = 0
        
        # Fix duplicate course_materials paths
        duplicate_patterns = [
            (r'course_materials/course_materials/', 'course_materials/'),
            (r'formula_sheets_sheets_lookup\.html', 'formula_lookup.html'),
        ]
        
        for pattern, replacement in duplicate_patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Fixed duplicate path in {file_path.name}")
        
        return content, fixes
    
    def fix_missing_favicon_links(self, content, file_path):
        """Fix or remove links to missing favicon files."""
        fixes = 0
        
        # Check if favicon files exist
        favicon_files = [
            'public/favicons/favicon.ico',
            'public/favicons/favicon-32x32.png',
            'public/favicons/favicon-16x16.png',
            'public/favicons/apple-touch-icon.png',
            'public/favicons/apple-touch-icon-152x152.png',
            'public/favicons/apple-touch-icon-167x167.png',
            'public/favicons/android-chrome-192x192.png',
            'public/favicons/android-chrome-512x512.png',
            'public/site.webmanifest',
        ]
        
        for favicon_file in favicon_files:
            file_path_check = self.base_dir / favicon_file
            if not file_path_check.exists():
                # Remove the link if file doesn't exist
                pattern = rf'<link[^>]*href="{re.escape(favicon_file)}"[^>]*>'
                if re.search(pattern, content):
                    content = re.sub(pattern, '', content)
                    fixes += 1
                    self.fixes_applied.append(f"Removed missing favicon link in {file_path.name}")
        
        return content, fixes
    
    def fix_missing_english_files(self, content, file_path):
        """Remove links to English files that don't exist."""
        fixes = 0
        
        # Check if English files exist and remove links to non-existent ones
        english_files = [
            'english/Course Overview and Introduction_MRCE.html/Course Overview and Introduction_MRCE.html',
            'english/Course Schedule (8-Week)_MRCE.html/Course Schedule (8-Week)_MRCE.html',
        ]
        
        for english_file in english_files:
            file_path_check = self.base_dir / english_file
            if not file_path_check.exists():
                # Remove the link if file doesn't exist
                pattern = rf'<a[^>]*href="{re.escape(english_file)}"[^>]*>.*?</a>'
                if re.search(pattern, content):
                    content = re.sub(pattern, '', content)
                    fixes += 1
                    self.fixes_applied.append(f"Removed non-existent English file link in {file_path.name}")
        
        return content, fixes
    
    def remove_ctle_template_links(self, content, file_path):
        """Remove links to CTLE template files that don't exist."""
        fixes = 0
        
        # Remove CTLE template links
        ctle_patterns = [
            r'<link[^>]*href="[^"]*CTLE_HTML_Templates/[^"]*"[^>]*>',
            r'<img[^>]*src="[^"]*CTLE_HTML_Templates/[^"]*"[^>]*>',
        ]
        
        for pattern in ctle_patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, '', content)
                fixes += 1
                self.fixes_applied.append(f"Removed CTLE template link in {file_path.name}")
        
        return content, fixes
    
    def fix_file(self, file_path):
        """Fix all remaining broken links in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_fixes = 0
            
            # Apply all fixes
            content, fixes = self.fix_duplicate_course_materials_paths(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_missing_favicon_links(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_missing_english_files(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.remove_ctle_template_links(content, file_path)
            total_fixes += fixes
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {total_fixes} issues in {file_path.name}")
                return total_fixes
            else:
                print(f"ℹ️  No fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the remaining link fixer on all HTML files."""
        print("🔧 Starting remaining broken link fixes...")
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
        print(f"🎉 REMAINING LINK FIXES COMPLETE")
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
    fixer = RemainingLinkFixer()
    fixer.run()
