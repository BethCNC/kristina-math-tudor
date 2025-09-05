#!/usr/bin/env python3
"""
Simple Accessibility Fix Script for Kristina's Academic Success Dashboard
Fixes the most critical contrast and accessibility issues.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

class SimpleAccessibilityFixer:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.fixes_applied = []

    def find_html_files(self):
        """Find all HTML files in the project."""
        html_files = []
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.base_dir.glob(pattern))
        # Exclude archived and dist files for now
        return [f for f in html_files if f.is_file() and not any(part in str(f) for part in ['_archived', 'dist', 'node_modules']) and f.name not in ['accessibility_report.html', 'link_check_report.html']]

    def fix_contrast_issues(self, html_file: Path):
        """Fix contrast issues in an HTML file."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return False
        
        original_content = content
        fixes_applied = []
        
        # Fix white text on light backgrounds - replace with dark text
        content = re.sub(
            r'class="([^"]*)\btext-white\b([^"]*)"',
            r'class="\1text-text-primary\2"',
            content
        )
        
        # Fix text-inverse-primary (white text) on light backgrounds
        content = re.sub(
            r'class="([^"]*)\btext-text-inverse-primary\b([^"]*)"',
            r'class="\1text-text-primary\2"',
            content
        )
        
        # Add borders to light backgrounds for better definition
        content = re.sub(
            r'class="([^"]*)\bbg-background-secondary\b([^"]*)"',
            r'class="\1bg-background-secondary border border-border\2"',
            content
        )
        
        content = re.sub(
            r'class="([^"]*)\bbg-background-tertiary\b([^"]*)"',
            r'class="\1bg-background-tertiary border border-border\2"',
            content
        )
        
        # Ensure proper text color on colored backgrounds
        content = re.sub(
            r'class="([^"]*)\bbg-positive\b([^"]*)"',
            r'class="\1bg-positive text-white\2"',
            content
        )
        
        content = re.sub(
            r'class="([^"]*)\bbg-brand\b([^"]*)"',
            r'class="\1bg-brand text-white\2"',
            content
        )
        
        content = re.sub(
            r'class="([^"]*)\bbg-warning\b([^"]*)"',
            r'class="\1bg-warning text-white\2"',
            content
        )
        
        content = re.sub(
            r'class="([^"]*)\bbg-danger\b([^"]*)"',
            r'class="\1bg-danger text-white\2"',
            content
        )
        
        if content != original_content:
            fixes_applied.append("Fixed contrast issues")
        
        # Write the fixed content back
        if fixes_applied:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False

    def fix_adhd_accessibility(self, html_file: Path):
        """Fix ADHD accessibility issues by adding better spacing and structure."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return False
        
        original_content = content
        fixes_applied = []
        
        # Add spacing around headings
        content = re.sub(
            r'<h([1-6])([^>]*)>([^<]+)</h[1-6]>',
            r'<h\1\2 class="mt-8 mb-4">\3</h\1>',
            content,
            flags=re.IGNORECASE
        )
        
        # Improve list formatting
        content = re.sub(
            r'<ul([^>]*)>',
            r'<ul\1 class="space-y-2">',
            content,
            flags=re.IGNORECASE
        )
        
        content = re.sub(
            r'<ol([^>]*)>',
            r'<ol\1 class="space-y-2">',
            content,
            flags=re.IGNORECASE
        )
        
        # Add spacing to paragraphs
        content = re.sub(
            r'<p([^>]*)>',
            r'<p\1 class="mb-4">',
            content,
            flags=re.IGNORECASE
        )
        
        if content != original_content:
            fixes_applied.append("Fixed ADHD accessibility issues")
        
        # Write the fixed content back
        if fixes_applied:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False

    def fix_accessibility_patterns(self, html_file: Path):
        """Fix general accessibility issues."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return False
        
        original_content = content
        fixes_applied = []
        
        # Fix missing alt text on images
        content = re.sub(
            r'<img([^>]*?)src="([^"]*)"([^>]*?)(?:alt="([^"]*)")?([^>]*?)>',
            lambda m: f'<img{m.group(1)}src="{m.group(2)}"{m.group(3)}alt="{m.group(4) if m.group(4) else "Image"}"{m.group(5)}>' if not m.group(4) else m.group(0),
            content,
            flags=re.IGNORECASE
        )
        
        # Fix form inputs without labels - add basic labels
        content = re.sub(
            r'<input([^>]*?)type="text"([^>]*?)>',
            r'<label for="input-\1" class="sr-only">Text input</label><input\1type="text"id="input-\1"\2>',
            content,
            flags=re.IGNORECASE
        )
        
        content = re.sub(
            r'<input([^>]*?)type="email"([^>]*?)>',
            r'<label for="input-\1" class="sr-only">Email input</label><input\1type="email"id="input-\1"\2>',
            content,
            flags=re.IGNORECASE
        )
        
        if content != original_content:
            fixes_applied.append("Fixed general accessibility issues")
        
        # Write the fixed content back
        if fixes_applied:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False

    def update_design_system_css(self):
        """Update the CSS to use Vend Sans font and improve contrast."""
        css_file = self.base_dir / "src/styles/globals.css"
        
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return False
        
        original_content = content
        
        # Update font imports to use Vend Sans instead of Host Grotesk
        content = re.sub(
            r'@import url\(\'https://fonts\.googleapis\.com/css2\?family=Host\+Grotesk[^\']*\'\);',
            '@import url(\'https://fonts.googleapis.com/css2?family=Vend+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap\');',
            content
        )
        
        # Update font family references
        content = re.sub(
            r'"Host Grotesk"',
            '"Vend Sans"',
            content
        )
        
        # Improve contrast by using darker backgrounds for better text visibility
        content = re.sub(
            r'--color-mooonstone-50: oklch\(0\.985 0\.007 53\.4\);',
            '--color-mooonstone-50: oklch(0.95 0.01 53.4);',
            content
        )
        
        content = re.sub(
            r'--color-mooonstone-100: oklch\(0\.976 0\.012 51\.3\);',
            '--color-mooonstone-100: oklch(0.92 0.015 51.3);',
            content
        )
        
        # Ensure text colors have sufficient contrast
        content = re.sub(
            r'--color-text-primary: #1f2937;',
            '--color-text-primary: #111827;',
            content
        )
        
        if content != original_content:
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False

    def run_fixes(self):
        """Run all accessibility fixes."""
        print("🔧 Starting accessibility fixes for Kristina's Academic Success Dashboard")
        print("=" * 70)
        
        html_files = self.find_html_files()
        print(f"📄 Found {len(html_files)} HTML files to fix")
        
        files_fixed = 0
        
        for html_file in html_files:
            print(f"🔍 Fixing {html_file.name}...")
            file_fixes = []
            
            # Apply all fixes
            if self.fix_contrast_issues(html_file):
                file_fixes.append("contrast")
            
            if self.fix_adhd_accessibility(html_file):
                file_fixes.append("ADHD accessibility")
            
            if self.fix_accessibility_patterns(html_file):
                file_fixes.append("general accessibility")
            
            if file_fixes:
                files_fixed += 1
                print(f"  ✅ Applied fixes: {', '.join(file_fixes)}")
                self.fixes_applied.append({
                    'file': str(html_file),
                    'fixes': file_fixes
                })
            else:
                print(f"  ℹ️  No fixes needed")
        
        # Update CSS
        print(f"\n🎨 Updating design system CSS...")
        if self.update_design_system_css():
            print(f"  ✅ Updated CSS with Vend Sans font and improved contrast")
            self.fixes_applied.append({
                'file': 'src/styles/globals.css',
                'fixes': ['font update', 'contrast improvement']
            })
        else:
            print(f"  ℹ️  No CSS updates needed")
        
        # Summary
        print("\n" + "=" * 70)
        print("🔧 ACCESSIBILITY FIXES SUMMARY")
        print("=" * 70)
        print(f"Files processed: {len(html_files)}")
        print(f"Files fixed: {files_fixed}")
        print(f"Total fixes applied: {len(self.fixes_applied)}")
        
        if self.fixes_applied:
            print("\n📋 Fixes Applied:")
            for fix in self.fixes_applied:
                print(f"  📄 {fix['file']}: {', '.join(fix['fixes'])}")
        
        print("\n🎉 Accessibility fixes completed!")
        print("\n📝 Next steps:")
        print("1. Run the accessibility checker again to verify fixes")
        print("2. Test the pages in a browser to ensure they look correct")
        print("3. Run the link checker to verify all links work")
        
        return self.fixes_applied

    def save_fix_report(self, filename="accessibility_fixes_report.json"):
        """Save the fixes report to a JSON file."""
        report = {
            'fixes_applied': self.fixes_applied,
            'fix_time': datetime.now().isoformat(),
            'summary': {
                'total_files_fixed': len(self.fixes_applied),
                'fixes_by_type': {}
            }
        }
        
        # Count fixes by type
        for fix in self.fixes_applied:
            for fix_type in fix['fixes']:
                report['summary']['fixes_by_type'][fix_type] = report['summary']['fixes_by_type'].get(fix_type, 0) + 1
        
        report_path = self.base_dir / filename
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n📄 Fixes report saved to: {report_path}")

def main():
    """Main function to run the accessibility fixes."""
    fixer = SimpleAccessibilityFixer()
    fixes = fixer.run_fixes()
    fixer.save_fix_report()
    
    if fixes:
        print(f"\n✅ Successfully applied {len(fixes)} accessibility fixes!")
        exit(0)
    else:
        print(f"\n⚠️  No fixes were needed or applied.")
        exit(0)

if __name__ == "__main__":
    main()
