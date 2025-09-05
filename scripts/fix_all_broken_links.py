#!/usr/bin/env python3
"""
Comprehensive Broken Link Fixer for Kristina's Academic Success Dashboard
Fixes all broken links by either correcting them or removing them entirely.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

class ComprehensiveLinkFixer:
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
    
    def fix_google_fonts(self, content, file_path):
        """Fix all Google Fonts links to use proper URLs."""
        fixes = 0
        
        # Fix broken Google Fonts base URLs
        font_fixes = [
            # Fix broken base URLs
            (r'href="https://fonts\.googleapis\.com"', 'href="https://fonts.googleapis.com/css2?family=Vend+Sans:wght@400;500;600;700;800;900&display=swap"'),
            (r'href="https://fonts\.gstatic\.com"', 'href="https://fonts.googleapis.com/css2?family=Vend+Sans:wght@400;500;600;700;800;900&display=swap"'),
            (r'src="https://fonts\.googleapis\.com"', 'src="https://fonts.googleapis.com/css2?family=Vend+Sans:wght@400;500;600;700;800;900&display=swap"'),
            (r'src="https://fonts\.gstatic\.com"', 'src="https://fonts.googleapis.com/css2?family=Vend+Sans:wght@400;500;600;700;800;900&display=swap"'),
            
            # Fix preconnect links
            (r'<link rel="preconnect" href="https://fonts\.googleapis\.com"[^>]*>', '<link rel="preconnect" href="https://fonts.googleapis.com">'),
            (r'<link rel="preconnect" href="https://fonts\.gstatic\.com"[^>]*>', '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'),
        ]
        
        for pattern, replacement in font_fixes:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Fixed Google Fonts link in {file_path.name}")
        
        return content, fixes
    
    def fix_course_materials_links(self, content, file_path):
        """Fix course materials links to use proper @course_materials/ path."""
        fixes = 0
        
        # Fix course materials links
        course_material_fixes = [
            # Fix formula sheet links
            (r'href="[^"]*formula[^"]*"', lambda m: m.group(0).replace('formula', 'course_materials/formula_sheets')),
            (r'href="[^"]*All_Sections_Guide[^"]*"', 'href="course_materials/formula_sheets/All_Sections_Guide.md"'),
            (r'href="[^"]*Chapter_6_Formula_Sheet[^"]*"', 'href="course_materials/formula_sheets/Chapter_6_Formula_Sheet.md"'),
            (r'href="[^"]*Chapter_7_Formula_Sheet[^"]*"', 'href="course_materials/formula_sheets/Chapter_7_Formula_Sheet.md"'),
            (r'href="[^"]*Unit_1_Formula_Sheet[^"]*"', 'href="course_materials/formula_sheets/Unit_1_Formula_Sheet.md"'),
            (r'href="[^"]*Unit_4_Formula_Sheet[^"]*"', 'href="course_materials/formula_sheets/Unit_4_Formula_Sheet.md"'),
            
            # Fix instruction links
            (r'href="[^"]*Hawkes_Learning_Setup[^"]*"', 'href="course_materials/instructions/Hawkes_Learning_Setup.md"'),
            
            # Fix resource links
            (r'href="[^"]*Chapter_Resources[^"]*"', 'href="course_materials/resources/Chapter_Resources.md"'),
            
            # Fix sample assignment links
            (r'href="[^"]*Week_1_Attendance_Sample[^"]*"', 'href="course_materials/sample_assignments/Week_1_Attendance_Sample.md"'),
            
            # Fix syllabus links
            (r'href="[^"]*Course_Schedule[^"]*"', 'href="course_materials/syllabus_and_schedule/Course_Schedule_Fall_2025.md"'),
        ]
        
        for pattern, replacement in course_material_fixes:
            if re.search(pattern, content):
                if callable(replacement):
                    content = re.sub(pattern, replacement, content)
                else:
                    content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Fixed course materials link in {file_path.name}")
        
        return content, fixes
    
    def remove_broken_asset_links(self, content, file_path):
        """Remove links to assets that don't exist in source files."""
        fixes = 0
        
        # Remove links to dist assets from source files
        if 'dist/' not in str(file_path):
            dist_asset_patterns = [
                r'<link[^>]*href="/assets/[^"]*"[^>]*>',
                r'<script[^>]*src="/assets/[^"]*"[^>]*></script>',
                r'<img[^>]*src="/assets/[^"]*"[^>]*>',
            ]
            
            for pattern in dist_asset_patterns:
                if re.search(pattern, content):
                    content = re.sub(pattern, '', content)
                    fixes += 1
                    self.fixes_applied.append(f"Removed dist asset link in {file_path.name}")
        
        return content, fixes
    
    def remove_broken_archived_links(self, content, file_path):
        """Remove links to archived files that don't exist."""
        fixes = 0
        
        # Remove links to files that don't exist
        broken_file_patterns = [
            r'<a[^>]*href="[^"]*english_tutor\.html"[^>]*>.*?</a>',
            r'<a[^>]*href="[^"]*CTLE_HTML_Templates/[^"]*"[^>]*>.*?</a>',
        ]
        
        for pattern in broken_file_patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, '', content)
                fixes += 1
                self.fixes_applied.append(f"Removed broken archived link in {file_path.name}")
        
        return content, fixes
    
    def fix_favicon_links(self, content, file_path):
        """Fix favicon links to use proper paths."""
        fixes = 0
        
        # Fix favicon links to use public directory
        favicon_fixes = [
            (r'href="/favicon\.ico"', 'href="public/favicons/favicon.ico"'),
            (r'href="/favicon-32x32\.png"', 'href="public/favicons/favicon-32x32.png"'),
            (r'href="/favicon-16x16\.png"', 'href="public/favicons/favicon-16x16.png"'),
            (r'href="/apple-touch-icon\.png"', 'href="public/favicons/apple-touch-icon.png"'),
            (r'href="/apple-touch-icon-152x152\.png"', 'href="public/favicons/apple-touch-icon-152x152.png"'),
            (r'href="/apple-touch-icon-167x167\.png"', 'href="public/favicons/apple-touch-icon-167x167.png"'),
            (r'href="/android-chrome-192x192\.png"', 'href="public/favicons/android-chrome-192x192.png"'),
            (r'href="/android-chrome-512x512\.png"', 'href="public/favicons/android-chrome-512x512.png"'),
            (r'href="/site\.webmanifest"', 'href="public/site.webmanifest"'),
        ]
        
        for pattern, replacement in favicon_fixes:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Fixed favicon link in {file_path.name}")
        
        return content, fixes
    
    def fix_english_file_links(self, content, file_path):
        """Fix or remove links to English files that have complex paths."""
        fixes = 0
        
        # Check if English files exist and fix links
        english_files = [
            'english/✍ Submit- Critical Reading Discussion (Due-8:22).txt',
            'english/Ways to Organize CompareContrast Essay.html',
            'english/Topic Ideas - Copy (1).html',
            'english/love hate comparison ada.pdf',
        ]
        
        for english_file in english_files:
            file_path_check = self.base_dir / english_file
            if file_path_check.exists():
                # Fix the link
                pattern = rf'href="[^"]*{re.escape(english_file.split("/")[-1])}[^"]*"'
                replacement = f'href="{english_file}"'
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    fixes += 1
                    self.fixes_applied.append(f"Fixed English file link in {file_path.name}")
            else:
                # Remove the link if file doesn't exist
                pattern = rf'<a[^>]*href="[^"]*{re.escape(english_file.split("/")[-1])}[^"]*"[^>]*>.*?</a>'
                if re.search(pattern, content):
                    content = re.sub(pattern, '', content)
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
            content, fixes = self.fix_google_fonts(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_course_materials_links(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.remove_broken_asset_links(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.remove_broken_archived_links(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_favicon_links(content, file_path)
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
        """Run the comprehensive link fixer on all HTML files."""
        print("🔧 Starting comprehensive broken link fixes...")
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
        print(f"🎉 COMPREHENSIVE LINK FIXES COMPLETE")
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
    fixer = ComprehensiveLinkFixer()
    fixer.run()
