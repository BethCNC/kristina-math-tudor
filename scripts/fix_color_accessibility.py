#!/usr/bin/env python3
"""
Fix Color Accessibility Issues for Kristina's Academic Success Dashboard
Fixes icon accessibility, background colors, and text color contrast issues.
"""

import os
import re
from pathlib import Path

class ColorAccessibilityFixer:
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
    
    def fix_icon_accessibility(self, content, file_path):
        """Add aria-labels to icons for accessibility."""
        fixes = 0
        
        # Icon accessibility fixes
        icon_fixes = [
            # Navigation icons
            (r'<i data-lucide="arrow-left"([^>]*)>', r'<i data-lucide="arrow-left"\1 aria-label="Go back">'),
            (r'<i data-lucide="arrow-right"([^>]*)>', r'<i data-lucide="arrow-right"\1 aria-label="Go forward">'),
            (r'<i data-lucide="home"([^>]*)>', r'<i data-lucide="home"\1 aria-label="Home">'),
            (r'<i data-lucide="menu"([^>]*)>', r'<i data-lucide="menu"\1 aria-label="Menu">'),
            (r'<i data-lucide="x"([^>]*)>', r'<i data-lucide="x"\1 aria-label="Close">'),
            
            # Content icons
            (r'<i data-lucide="brain"([^>]*)>', r'<i data-lucide="brain"\1 aria-label="Thinking">'),
            (r'<i data-lucide="clock"([^>]*)>', r'<i data-lucide="clock"\1 aria-label="Time">'),
            (r'<i data-lucide="target"([^>]*)>', r'<i data-lucide="target"\1 aria-label="Goal">'),
            (r'<i data-lucide="layers"([^>]*)>', r'<i data-lucide="layers"\1 aria-label="Layers">'),
            (r'<i data-lucide="book"([^>]*)>', r'<i data-lucide="book"\1 aria-label="Book">'),
            (r'<i data-lucide="calculator"([^>]*)>', r'<i data-lucide="calculator"\1 aria-label="Calculator">'),
            (r'<i data-lucide="dollar-sign"([^>]*)>', r'<i data-lucide="dollar-sign"\1 aria-label="Money">'),
            (r'<i data-lucide="ruler"([^>]*)>', r'<i data-lucide="ruler"\1 aria-label="Measurement">'),
            (r'<i data-lucide="bar-chart-3"([^>]*)>', r'<i data-lucide="bar-chart-3"\1 aria-label="Statistics">'),
            (r'<i data-lucide="vote"([^>]*)>', r'<i data-lucide="vote"\1 aria-label="Voting">'),
            (r'<i data-lucide="book-open"([^>]*)>', r'<i data-lucide="book-open"\1 aria-label="Study guide">'),
            (r'<i data-lucide="link"([^>]*)>', r'<i data-lucide="link"\1 aria-label="Link">'),
            (r'<i data-lucide="calendar"([^>]*)>', r'<i data-lucide="calendar"\1 aria-label="Calendar">'),
            (r'<i data-lucide="check"([^>]*)>', r'<i data-lucide="check"\1 aria-label="Check">'),
            (r'<i data-lucide="alert-circle"([^>]*)>', r'<i data-lucide="alert-circle"\1 aria-label="Alert">'),
            (r'<i data-lucide="info"([^>]*)>', r'<i data-lucide="info"\1 aria-label="Information">'),
            (r'<i data-lucide="help-circle"([^>]*)>', r'<i data-lucide="help-circle"\1 aria-label="Help">'),
            (r'<i data-lucide="star"([^>]*)>', r'<i data-lucide="star"\1 aria-label="Star">'),
            (r'<i data-lucide="heart"([^>]*)>', r'<i data-lucide="heart"\1 aria-label="Heart">'),
            (r'<i data-lucide="thumbs-up"([^>]*)>', r'<i data-lucide="thumbs-up"\1 aria-label="Like">'),
            (r'<i data-lucide="download"([^>]*)>', r'<i data-lucide="download"\1 aria-label="Download">'),
            (r'<i data-lucide="upload"([^>]*)>', r'<i data-lucide="upload"\1 aria-label="Upload">'),
            (r'<i data-lucide="search"([^>]*)>', r'<i data-lucide="search"\1 aria-label="Search">'),
            (r'<i data-lucide="filter"([^>]*)>', r'<i data-lucide="filter"\1 aria-label="Filter">'),
            (r'<i data-lucide="settings"([^>]*)>', r'<i data-lucide="settings"\1 aria-label="Settings">'),
            (r'<i data-lucide="user"([^>]*)>', r'<i data-lucide="user"\1 aria-label="User">'),
            (r'<i data-lucide="mail"([^>]*)>', r'<i data-lucide="mail"\1 aria-label="Email">'),
            (r'<i data-lucide="phone"([^>]*)>', r'<i data-lucide="phone"\1 aria-label="Phone">'),
            (r'<i data-lucide="map-pin"([^>]*)>', r'<i data-lucide="map-pin"\1 aria-label="Location">'),
            (r'<i data-lucide="globe"([^>]*)>', r'<i data-lucide="globe"\1 aria-label="Website">'),
            (r'<i data-lucide="external-link"([^>]*)>', r'<i data-lucide="external-link"\1 aria-label="External link">'),
        ]
        
        for pattern, replacement in icon_fixes:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Added aria-label to icon in {file_path.name}")
        
        return content, fixes
    
    def fix_background_colors(self, content, file_path):
        """Fix problematic background colors."""
        fixes = 0
        
        # Background color fixes
        bg_fixes = [
            # Replace problematic background colors with accessible alternatives
            (r'bg-cream', 'bg-surface-secondary'),
            (r'bg-beige', 'bg-surface-secondary'),
            (r'bg-yellow-100', 'bg-warning-light'),
            (r'bg-orange-100', 'bg-warning-light'),
            (r'bg-gray-100', 'bg-surface-secondary'),
        ]
        
        for pattern, replacement in bg_fixes:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Fixed background color in {file_path.name}")
        
        return content, fixes
    
    def fix_text_colors(self, content, file_path):
        """Fix problematic text colors."""
        fixes = 0
        
        # Text color fixes
        text_fixes = [
            # Replace problematic text colors with accessible alternatives
            (r'text-white', 'text-text-primary'),
            (r'text-gray-300', 'text-text-secondary'),
            (r'text-gray-400', 'text-text-secondary'),
            (r'text-yellow-300', 'text-warning'),
            (r'text-orange-300', 'text-warning'),
        ]
        
        for pattern, replacement in text_fixes:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                fixes += 1
                self.fixes_applied.append(f"Fixed text color in {file_path.name}")
        
        return content, fixes
    
    def fix_file(self, file_path):
        """Fix all color accessibility issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_fixes = 0
            
            # Apply all fixes
            content, fixes = self.fix_icon_accessibility(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_background_colors(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.fix_text_colors(content, file_path)
            total_fixes += fixes
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {total_fixes} color accessibility issues in {file_path.name}")
                return total_fixes
            else:
                print(f"ℹ️  No color accessibility fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the color accessibility fixer on all HTML files."""
        print("🎨 Starting color accessibility fixes...")
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
        print(f"🎉 COLOR ACCESSIBILITY FIXES COMPLETE")
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
    fixer = ColorAccessibilityFixer()
    fixer.run()
