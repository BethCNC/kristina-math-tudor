#!/usr/bin/env python3
"""
Focused Color Accessibility Checker for Kristina's Academic Success Dashboard
Checks text colors, icon colors, contrast ratios, and color-related accessibility issues.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
import colorsys

class ColorAccessibilityChecker:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.issues = []
        self.color_issues = []
        
    def find_html_files(self):
        """Find all HTML files to check."""
        html_files = []
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.base_dir.glob(pattern))
        
        # Exclude dist, node_modules, and report files
        return [f for f in html_files if f.is_file() and not any(part in str(f) for part in ['dist', 'node_modules', 'accessibility_report', 'link_check_report']) and f.name not in ['accessibility_report.html', 'link_check_report.html']]
    
    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def rgb_to_hsl(self, rgb):
        """Convert RGB to HSL."""
        r, g, b = [x/255.0 for x in rgb]
        return colorsys.rgb_to_hls(r, g, b)
    
    def get_luminance(self, rgb):
        """Calculate relative luminance of RGB color."""
        r, g, b = [x/255.0 for x in rgb]
        
        # Apply gamma correction
        r = r/12.92 if r <= 0.03928 else ((r + 0.055)/1.055) ** 2.4
        g = g/12.92 if g <= 0.03928 else ((g + 0.055)/1.055) ** 2.4
        b = b/12.92 if b <= 0.03928 else ((b + 0.055)/1.055) ** 2.4
        
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
    
    def get_contrast_ratio(self, color1, color2):
        """Calculate contrast ratio between two colors."""
        lum1 = self.get_luminance(color1)
        lum2 = self.get_luminance(color2)
        
        lighter = max(lum1, lum2)
        darker = min(lum1, lum2)
        
        return (lighter + 0.05) / (darker + 0.05)
    
    def check_color_contrast(self, content, file_path):
        """Check for color contrast issues."""
        issues = []
        
        # Common problematic color combinations
        problematic_combinations = [
            # White text on light backgrounds
            (r'text-white.*bg-[^"]*beige', 'White text on light beige background'),
            (r'text-white.*bg-[^"]*cream', 'White text on cream background'),
            (r'text-white.*bg-[^"]*light', 'White text on light background'),
            (r'text-white.*bg-[^"]*yellow', 'White text on yellow background'),
            (r'text-white.*bg-[^"]*orange', 'White text on orange background'),
            
            # Light text on light backgrounds
            (r'text-gray-300.*bg-[^"]*light', 'Light gray text on light background'),
            (r'text-gray-400.*bg-[^"]*light', 'Light gray text on light background'),
            (r'text-gray-500.*bg-[^"]*light', 'Medium gray text on light background'),
            
            # Dark text on dark backgrounds
            (r'text-gray-800.*bg-[^"]*dark', 'Dark text on dark background'),
            (r'text-gray-900.*bg-[^"]*dark', 'Very dark text on dark background'),
            (r'text-black.*bg-[^"]*dark', 'Black text on dark background'),
        ]
        
        for pattern, description in problematic_combinations:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                for match in matches:
                    issues.append({
                        'type': 'color_contrast',
                        'severity': 'high',
                        'description': description,
                        'location': f'Line containing: {match[:50]}...',
                        'file': file_path.name
                    })
        
        return issues
    
    def check_icon_accessibility(self, content, file_path):
        """Check for icon accessibility issues."""
        issues = []
        
        # Icons without aria-labels or alt text
        icon_patterns = [
            (r'<i[^>]*data-lucide="[^"]*"[^>]*(?!.*aria-label)[^>]*>', 'Icon without aria-label'),
            (r'<svg[^>]*(?!.*aria-label)[^>]*(?!.*alt)[^>]*>', 'SVG icon without accessibility attributes'),
            (r'<img[^>]*src="[^"]*icon[^"]*"[^>]*(?!.*alt)[^>]*>', 'Icon image without alt text'),
        ]
        
        for pattern, description in icon_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                for match in matches:
                    issues.append({
                        'type': 'icon_accessibility',
                        'severity': 'medium',
                        'description': description,
                        'location': f'Line containing: {match[:50]}...',
                        'file': file_path.name
                    })
        
        return issues
    
    def check_text_colors(self, content, file_path):
        """Check for problematic text color classes."""
        issues = []
        
        # Problematic text color classes
        problematic_text_colors = [
            (r'text-white', 'White text - may have contrast issues'),
            (r'text-gray-300', 'Very light gray text - low contrast'),
            (r'text-gray-400', 'Light gray text - may have contrast issues'),
            (r'text-yellow-300', 'Light yellow text - low contrast'),
            (r'text-orange-300', 'Light orange text - low contrast'),
        ]
        
        for pattern, description in problematic_text_colors:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                for match in matches:
                    issues.append({
                        'type': 'text_color',
                        'severity': 'medium',
                        'description': description,
                        'location': f'Text color class: {match}',
                        'file': file_path.name
                    })
        
        return issues
    
    def check_background_colors(self, content, file_path):
        """Check for problematic background color classes."""
        issues = []
        
        # Problematic background color classes
        problematic_bg_colors = [
            (r'bg-beige', 'Beige background - may cause contrast issues'),
            (r'bg-cream', 'Cream background - may cause contrast issues'),
            (r'bg-yellow-100', 'Very light yellow background - low contrast'),
            (r'bg-orange-100', 'Very light orange background - low contrast'),
            (r'bg-gray-100', 'Very light gray background - may cause contrast issues'),
        ]
        
        for pattern, description in problematic_bg_colors:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                for match in matches:
                    issues.append({
                        'type': 'background_color',
                        'severity': 'medium',
                        'description': description,
                        'location': f'Background color class: {match}',
                        'file': file_path.name
                    })
        
        return issues
    
    def check_css_custom_properties(self, content, file_path):
        """Check for problematic CSS custom properties."""
        issues = []
        
        # Look for OKLCH color values that might have contrast issues
        oklch_pattern = r'oklch\([^)]+\)'
        matches = re.findall(oklch_pattern, content, re.IGNORECASE)
        
        for match in matches:
            # Extract lightness value from OKLCH
            lightness_match = re.search(r'oklch\(([^,]+),', match)
            if lightness_match:
                try:
                    lightness = float(lightness_match.group(1))
                    if lightness > 0.8:  # Very light colors
                        issues.append({
                            'type': 'css_color',
                            'severity': 'high',
                            'description': f'Very light OKLCH color (lightness: {lightness}) - may cause contrast issues',
                            'location': f'OKLCH value: {match}',
                            'file': file_path.name
                        })
                except ValueError:
                    pass
        
        return issues
    
    def check_file(self, file_path):
        """Check a single file for color accessibility issues."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_issues = []
            
            # Run all checks
            file_issues.extend(self.check_color_contrast(content, file_path))
            file_issues.extend(self.check_icon_accessibility(content, file_path))
            file_issues.extend(self.check_text_colors(content, file_path))
            file_issues.extend(self.check_background_colors(content, file_path))
            file_issues.extend(self.check_css_custom_properties(content, file_path))
            
            if file_issues:
                print(f"🔍 Found {len(file_issues)} color accessibility issues in {file_path.name}")
                self.issues.extend(file_issues)
            else:
                print(f"✅ No color accessibility issues found in {file_path.name}")
                
        except Exception as e:
            print(f"❌ Error checking {file_path.name}: {e}")
    
    def generate_report(self):
        """Generate accessibility report."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_files_checked': len(self.find_html_files()),
            'total_issues': len(self.issues),
            'issues_by_type': {},
            'issues_by_severity': {},
            'issues': self.issues
        }
        
        # Count issues by type
        for issue in self.issues:
            issue_type = issue['type']
            if issue_type not in report['issues_by_type']:
                report['issues_by_type'][issue_type] = 0
            report['issues_by_type'][issue_type] += 1
        
        # Count issues by severity
        for issue in self.issues:
            severity = issue['severity']
            if severity not in report['issues_by_severity']:
                report['issues_by_severity'][severity] = 0
            report['issues_by_severity'][severity] += 1
        
        return report
    
    def run(self):
        """Run the color accessibility checker."""
        print("🎨 Starting color accessibility check...")
        print("=" * 60)
        
        html_files = self.find_html_files()
        print(f"📄 Found {len(html_files)} HTML files to check")
        
        for file_path in html_files:
            self.check_file(file_path)
        
        # Generate report
        report = self.generate_report()
        
        # Save JSON report
        with open('color_accessibility_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        # Print summary
        print("=" * 60)
        print(f"🎨 COLOR ACCESSIBILITY CHECK COMPLETE")
        print(f"📊 Files checked: {report['total_files_checked']}")
        print(f"⚠️  Total issues found: {report['total_issues']}")
        
        if report['total_issues'] > 0:
            print(f"\n📋 Issues by type:")
            for issue_type, count in report['issues_by_type'].items():
                print(f"  • {issue_type}: {count}")
            
            print(f"\n📋 Issues by severity:")
            for severity, count in report['issues_by_severity'].items():
                print(f"  • {severity}: {count}")
            
            print(f"\n🔍 Top issues:")
            for issue in self.issues[:10]:  # Show first 10
                print(f"  • {issue['file']}: {issue['description']}")
            if len(self.issues) > 10:
                print(f"  ... and {len(self.issues) - 10} more")
        else:
            print("🎉 No color accessibility issues found!")
        
        print(f"\n📄 Detailed report saved to: color_accessibility_report.json")
        
        return report

if __name__ == "__main__":
    checker = ColorAccessibilityChecker()
    checker.run()
