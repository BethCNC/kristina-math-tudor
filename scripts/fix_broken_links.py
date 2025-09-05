#!/usr/bin/env python3
"""
Broken Link Fixer for Kristina's Academic Success Dashboard
Fixes all broken links identified in the link check report.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

class BrokenLinkFixer:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.fixes_applied = []
        
        # Load the broken links report
        self.load_broken_links()
        
    def load_broken_links(self):
        """Load the broken links from the report."""
        report_path = self.base_dir / "link_check_report.json"
        if not report_path.exists():
            print("❌ No link check report found. Run check_links.py first.")
            return
            
        with open(report_path, 'r') as f:
            self.report = json.load(f)
            
        self.broken_links = []
        for link in self.report.get('external_links', []):
            if link.get('status') == 'BROKEN':
                self.broken_links.append(link)
        for link in self.report.get('file_links', []):
            if link.get('status') == 'BROKEN':
                self.broken_links.append(link)
                
        print(f"📊 Found {len(self.broken_links)} broken links to fix")
    
    def find_html_files(self):
        """Find all HTML files that need fixing."""
        html_files = []
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.base_dir.glob(pattern))
        
        # Exclude dist, node_modules, and report files
        return [f for f in html_files if f.is_file() and not any(part in str(f) for part in ['dist', 'node_modules', 'accessibility_report', 'link_check_report']) and f.name not in ['accessibility_report.html', 'link_check_report.html']]
    
    def fix_font_links(self, content, file_path):
        """Fix broken Google Fonts links."""
        fixes = 0
        
        # Fix broken fonts.googleapis.com and fonts.gstatic.com links
        # These are often just base URLs without proper paths
        patterns_to_fix = [
            (r'href="https://fonts\.googleapis\.com"', 'href="https://fonts.googleapis.com/css2?family=Vend+Sans:wght@400;500;600;700;800;900&display=swap"'),
            (r'href="https://fonts\.gstatic\.com"', 'href="https://fonts.googleapis.com/css2?family=Vend+Sans:wght@400;500;600;700;800;900&display=swap"'),
            (r'src="https://fonts\.googleapis\.com"', 'src="https://fonts.googleapis.com/css2?family=Vend+Sans:wght@400;500;600;700;800;900&display=swap"'),
            (r'src="https://fonts\.gstatic\.com"', 'src="https://fonts.googleapis.com/css2?family=Vend+Sans:wght@400;500;600;700;800;900&display=swap"'),
        ]
        
        for pattern, replacement in patterns_to_fix:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Fixed font link in {file_path.name}")
        
        return content, fixes
    
    def fix_missing_english_tutor(self, content, file_path):
        """Fix references to missing english_tutor.html."""
        fixes = 0
        
        # Replace references to english_tutor.html with tutor.html
        if 'english_tutor.html' in content:
            content = content.replace('english_tutor.html', 'tutor.html')
            fixes += 1
            self.fixes_applied.append(f"Fixed english_tutor.html reference in {file_path.name}")
        
        return content, fixes
    
    def fix_dist_asset_links(self, content, file_path):
        """Fix links to dist assets that don't exist in source."""
        fixes = 0
        
        # Fix links to dist assets - these should be relative to the built files
        # or removed if they're in source files
        if 'dist/' in str(file_path):
            # This is a dist file, keep the asset links as they are
            return content, fixes
        
        # For source files, remove or fix dist asset references
        dist_asset_patterns = [
            r'href="/assets/[^"]*"',
            r'src="/assets/[^"]*"',
        ]
        
        for pattern in dist_asset_patterns:
            if re.search(pattern, content):
                # Remove these links from source files
                content = re.sub(pattern, '', content)
                fixes += 1
                self.fixes_applied.append(f"Removed dist asset link in {file_path.name}")
        
        return content, fixes
    
    def fix_archived_file_links(self, content, file_path):
        """Fix links to archived files."""
        fixes = 0
        
        # Fix common archived file references
        archived_fixes = {
            'index.html': 'index.html',  # Keep as is
            'formula_lookup.html': 'formula_lookup.html',  # Keep as is
            'chapter-1.html': 'chapter-1.html',  # Keep as is
            'chapter-4.html': 'chapter-4.html',  # Keep as is
            'chapter-5.html': 'chapter-5.html',  # Keep as is
            'chapter-6.html': 'chapter-6.html',  # Keep as is
            'chapter-7.html': 'chapter-7.html',  # Keep as is
            'chapter-10.html': 'chapter-10.html',  # Keep as is
            'chapter-11.html': 'chapter-11.html',  # Keep as is
            'chapter-13.html': 'chapter-13.html',  # Keep as is
            'calendar.html': 'calendar.html',  # Keep as is
        }
        
        for old_link, new_link in archived_fixes.items():
            if old_link in content and old_link != new_link:
                content = content.replace(old_link, new_link)
                fixes += 1
                self.fixes_applied.append(f"Fixed archived file link in {file_path.name}")
        
        return content, fixes
    
    def fix_english_file_links(self, content, file_path):
        """Fix links to English course files."""
        fixes = 0
        
        # Fix links to English files that have complex paths
        english_fixes = {
            'english/Course Overview and Introduction_MRCE.html/Course Overview and Introduction_MRCE.html': 'english/Course Overview and Introduction_MRCE.html/Course Overview and Introduction_MRCE.html',
            'english/Course Schedule (8-Week)_MRCE.html/Course Schedule (8-Week)_MRCE.html': 'english/Course Schedule (8-Week)_MRCE.html/Course Schedule (8-Week)_MRCE.html',
        }
        
        for old_link, new_link in english_fixes.items():
            if old_link in content:
                # Check if the file actually exists
                file_path_check = self.base_dir / old_link
                if not file_path_check.exists():
                    # Remove the link if file doesn't exist
                    content = re.sub(rf'href="{re.escape(old_link)}"[^>]*>', '', content)
                    content = re.sub(rf'src="{re.escape(old_link)}"[^>]*>', '', content)
                    fixes += 1
                    self.fixes_applied.append(f"Removed non-existent English file link in {file_path.name}")
        
        return content, fixes
    
    def fix_file(self, file_path):
        """Fix all broken links in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_fixes = 0
            
            # Apply all fixes
            content, fixes = self.fix_font_links(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_missing_english_tutor(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_dist_asset_links(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_archived_file_links(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_english_file_links(content, file_path)
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
        """Run the broken link fixer on all HTML files."""
        print("🔧 Starting broken link fixes...")
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
        print(f"🎉 BROKEN LINK FIXES COMPLETE")
        print(f"📊 Files processed: {len(html_files)}")
        print(f"🔧 Files fixed: {files_fixed}")
        print(f"✅ Total fixes applied: {total_fixes}")
        
        if self.fixes_applied:
            print("\n📋 Fixes applied:")
            for fix in self.fixes_applied[:10]:  # Show first 10
                print(f"  • {fix}")
            if len(self.fixes_applied) > 10:
                print(f"  ... and {len(self.fixes_applied) - 10} more")
        
        return total_fixes

if __name__ == "__main__":
    fixer = BrokenLinkFixer()
    fixer.run()
