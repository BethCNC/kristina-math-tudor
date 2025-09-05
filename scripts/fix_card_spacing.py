#!/usr/bin/env python3
"""
Fix Card Spacing Issues for Kristina's Academic Success Dashboard
Specifically fixes vertical spacing between card sections.
"""

import os
import re
from pathlib import Path

class CardSpacingFixer:
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
    
    def fix_card_spacing(self, content, file_path):
        """Fix spacing between card sections."""
        fixes = 0
        
        # Fix Quick Actions grid spacing
        if 'grid sm:grid-cols-2 lg:grid-cols-4 gap-4 gap-6 gap-6' in content:
            content = content.replace(
                'grid sm:grid-cols-2 lg:grid-cols-4 gap-4 gap-6 gap-6',
                'grid sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-12'
            )
            fixes += 1
            self.fixes_applied.append(f"Fixed Quick Actions grid spacing in {file_path.name}")
        
        # Add margin to Quick Actions section
        if '<!-- Quick Actions -->' in content:
            # Find the Quick Actions section and add margin
            content = re.sub(
                r'(<!-- Quick Actions -->\s*<div class="grid[^"]*">)',
                r'\1',
                content
            )
            # Add margin-bottom to the closing div of Quick Actions
            content = re.sub(
                r'(</div>\s*</section>\s*<!-- Calendar Section -->)',
                r'</div>\n        </section>\n\n        <!-- Calendar Section -->',
                content
            )
            fixes += 1
            self.fixes_applied.append(f"Added margin between Quick Actions and Calendar in {file_path.name}")
        
        # Fix duplicate gap classes
        gap_fixes = [
            ('gap-4 gap-6 gap-6', 'gap-6'),
            ('gap-6 gap-6', 'gap-6'),
            ('gap-4 gap-4', 'gap-4'),
        ]
        
        for old, new in gap_fixes:
            if old in content:
                content = content.replace(old, new)
                fixes += 1
                self.fixes_applied.append(f"Fixed duplicate gap classes in {file_path.name}")
        
        # Add proper spacing between major sections
        section_spacing_fixes = [
            # Add margin between Quick Actions and Calendar
            (r'(</div>\s*</section>\s*<!-- Calendar Section -->)', 
             r'</div>\n        </section>\n\n        <!-- Calendar Section -->'),
            
            # Add margin between Calendar and Math Tutor
            (r'(</section>\s*<!-- Math Tutor Section -->)', 
             r'</section>\n\n        <!-- Math Tutor Section -->'),
            
            # Add margin between Math Tutor and Writing Coach
            (r'(</section>\s*<!-- Writing Coach Section -->)', 
             r'</section>\n\n        <!-- Writing Coach Section -->'),
        ]
        
        for pattern, replacement in section_spacing_fixes:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Added section spacing in {file_path.name}")
        
        return content, fixes
    
    def fix_file(self, file_path):
        """Fix card spacing issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_fixes = 0
            
            # Apply spacing fixes
            content, fixes = self.fix_card_spacing(content, file_path)
            total_fixes += fixes
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {total_fixes} card spacing issues in {file_path.name}")
                return total_fixes
            else:
                print(f"ℹ️  No card spacing fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the card spacing fixer on all HTML files."""
        print("🔧 Starting card spacing fixes...")
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
        print(f"🎉 CARD SPACING FIXES COMPLETE")
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
    fixer = CardSpacingFixer()
    fixer.run()
