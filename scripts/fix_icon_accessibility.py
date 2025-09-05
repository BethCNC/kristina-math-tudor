#!/usr/bin/env python3
"""
Fix Icon Accessibility Issues for Kristina's Academic Success Dashboard
Adds proper aria-labels to all icons and removes duplicates.
"""

import os
import re
from pathlib import Path

class IconAccessibilityFixer:
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
    
    def fix_duplicate_aria_labels(self, content, file_path):
        """Remove duplicate aria-label attributes."""
        fixes = 0
        
        # Remove duplicate aria-label attributes
        pattern = r'aria-label="([^"]*)"\s+aria-label="\1"'
        if re.search(pattern, content):
            content = re.sub(pattern, r'aria-label="\1"', content)
            fixes += 1
            self.fixes_applied.append(f"Removed duplicate aria-label in {file_path.name}")
        
        return content, fixes
    
    def add_missing_aria_labels(self, content, file_path):
        """Add aria-labels to icons that don't have them."""
        fixes = 0
        
        # Icon name to aria-label mapping
        icon_labels = {
            'arrow-left': 'Go back',
            'arrow-right': 'Go forward',
            'arrow-up': 'Go up',
            'arrow-down': 'Go down',
            'home': 'Home',
            'menu': 'Menu',
            'x': 'Close',
            'brain': 'Thinking',
            'clock': 'Time',
            'target': 'Goal',
            'layers': 'Layers',
            'book': 'Book',
            'calculator': 'Calculator',
            'dollar-sign': 'Money',
            'ruler': 'Measurement',
            'bar-chart-3': 'Statistics',
            'vote': 'Voting',
            'book-open': 'Study guide',
            'link': 'Link',
            'calendar': 'Calendar',
            'check': 'Check',
            'alert-circle': 'Alert',
            'info': 'Information',
            'help-circle': 'Help',
            'star': 'Star',
            'heart': 'Heart',
            'thumbs-up': 'Like',
            'download': 'Download',
            'upload': 'Upload',
            'search': 'Search',
            'filter': 'Filter',
            'settings': 'Settings',
            'user': 'User',
            'mail': 'Email',
            'phone': 'Phone',
            'map-pin': 'Location',
            'globe': 'Website',
            'external-link': 'External link',
            'lightbulb': 'Idea',
            'key': 'Key',
            'play': 'Play',
            'pause': 'Pause',
            'stop': 'Stop',
            'refresh': 'Refresh',
            'edit': 'Edit',
            'trash': 'Delete',
            'copy': 'Copy',
            'share': 'Share',
            'lock': 'Lock',
            'unlock': 'Unlock',
            'eye': 'View',
            'eye-off': 'Hide',
            'plus': 'Add',
            'minus': 'Remove',
            'chevron-left': 'Previous',
            'chevron-right': 'Next',
            'chevron-up': 'Expand',
            'chevron-down': 'Collapse',
            'more-horizontal': 'More options',
            'more-vertical': 'More options',
        }
        
        # Find all icons without aria-labels
        icon_pattern = r'<i data-lucide="([^"]+)"([^>]*?)(?<!aria-label="[^"]*")>'
        matches = re.findall(icon_pattern, content)
        
        for icon_name, attributes in matches:
            if icon_name in icon_labels:
                # Add aria-label to the icon
                new_attributes = f'{attributes} aria-label="{icon_labels[icon_name]}"'
                old_icon = f'<i data-lucide="{icon_name}"{attributes}>'
                new_icon = f'<i data-lucide="{icon_name}"{new_attributes}>'
                
                content = content.replace(old_icon, new_icon, 1)
                fixes += 1
                self.fixes_applied.append(f"Added aria-label to {icon_name} icon in {file_path.name}")
        
        return content, fixes
    
    def fix_file(self, file_path):
        """Fix all icon accessibility issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_fixes = 0
            
            # Apply all fixes
            content, fixes = self.fix_duplicate_aria_labels(content, file_path)
            total_fixes += fixes
            
            content, fixes = self.add_missing_aria_labels(content, file_path)
            total_fixes += fixes
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed {total_fixes} icon accessibility issues in {file_path.name}")
                return total_fixes
            else:
                print(f"ℹ️  No icon accessibility fixes needed in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error fixing {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the icon accessibility fixer on all HTML files."""
        print("🎯 Starting icon accessibility fixes...")
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
        
        if self.fixes_applied:
            print("\n📋 Fixes applied:")
            for fix in self.fixes_applied[:15]:  # Show first 15
                print(f"  • {fix}")
            if len(self.fixes_applied) > 15:
                print(f"  ... and {len(self.fixes_applied) - 15} more")
        
        return total_fixes

if __name__ == "__main__":
    fixer = IconAccessibilityFixer()
    fixer.run()
