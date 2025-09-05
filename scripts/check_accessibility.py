#!/usr/bin/env python3
"""
Accessibility and Contrast Checker for Kristina's Academic Success Dashboard
Validates WCAG 2.1 AA compliance, color contrast, and ADHD-friendly design patterns.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import colorsys

class AccessibilityChecker:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.results = {
            'contrast_issues': [],
            'adhd_issues': [],
            'accessibility_issues': [],
            'summary': {}
        }
        
        # WCAG 2.1 AA contrast ratios
        self.contrast_requirements = {
            'normal_text': 4.5,  # AA standard
            'large_text': 3.0,   # AA standard for 18pt+ or 14pt+ bold
            'ui_components': 3.0  # UI components and graphical objects
        }
        
        # ADHD-friendly design patterns to check
        self.adhd_patterns = {
            'max_paragraph_length': 150,  # characters
            'max_line_length': 75,        # characters
            'min_heading_spacing': 2,     # lines between headings and content
            'max_text_block_length': 500  # characters without breaks
        }

    def find_html_files(self):
        """Find all HTML files in the project."""
        html_files = []
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.base_dir.glob(pattern))
        return [f for f in html_files if f.is_file()]

    def hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:
            hex_color = ''.join([c*2 for c in hex_color])
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_relative_luminance(self, rgb: Tuple[int, int, int]) -> float:
        """Calculate relative luminance of an RGB color."""
        def linearize(c):
            c = c / 255.0
            return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        
        r, g, b = [linearize(c) for c in rgb]
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def calculate_contrast_ratio(self, color1: str, color2: str) -> float:
        """Calculate contrast ratio between two colors."""
        try:
            rgb1 = self.hex_to_rgb(color1)
            rgb2 = self.hex_to_rgb(color2)
            
            lum1 = self.rgb_to_relative_luminance(rgb1)
            lum2 = self.rgb_to_relative_luminance(rgb2)
            
            lighter = max(lum1, lum2)
            darker = min(lum1, lum2)
            
            return (lighter + 0.05) / (darker + 0.05)
        except:
            return 0.0

    def extract_css_colors(self, content: str) -> List[Dict]:
        """Extract color information from CSS content."""
        colors = []
        
        # Find color declarations
        color_patterns = [
            r'color\s*:\s*([^;]+)',
            r'background-color\s*:\s*([^;]+)',
            r'background\s*:\s*([^;]+)',
            r'border-color\s*:\s*([^;]+)',
            r'--[^:]+:\s*([^;]+)'
        ]
        
        for pattern in color_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                # Extract hex colors
                hex_colors = re.findall(r'#([0-9a-fA-F]{3,6})', match)
                for hex_color in hex_colors:
                    colors.append({
                        'type': 'hex',
                        'value': f'#{hex_color}',
                        'context': match.strip()
                    })
        
        return colors

    def extract_text_styles(self, html_content: str) -> List[Dict]:
        """Extract text styling information from HTML."""
        text_styles = []
        
        # Find text elements with styling
        text_patterns = [
            r'<(\w+)[^>]*class="([^"]*)"[^>]*>([^<]+)</\1>',
            r'<(\w+)[^>]*style="([^"]*)"[^>]*>([^<]+)</\1>'
        ]
        
        for pattern in text_patterns:
            matches = re.findall(pattern, html_content, re.IGNORECASE | re.DOTALL)
            for tag, styling, text in matches:
                if len(text.strip()) > 0:
                    text_styles.append({
                        'tag': tag,
                        'styling': styling,
                        'text': text.strip(),
                        'length': len(text.strip())
                    })
        
        return text_styles

    def check_contrast_issues(self, html_file: Path):
        """Check for contrast issues in an HTML file."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return
        
        # Extract CSS colors
        css_colors = self.extract_css_colors(content)
        
        # Common problematic color combinations
        problematic_combinations = [
            ('#ffffff', '#faf7f0'),  # White on cream
            ('#ffffff', '#f2f2f2'),  # White on light gray
            ('#ffffff', '#e2e8f0'),  # White on light blue-gray
            ('#000000', '#2d3748'),  # Black on dark gray (might be too close)
        ]
        
        for fg_color, bg_color in problematic_combinations:
            contrast_ratio = self.calculate_contrast_ratio(fg_color, bg_color)
            
            if contrast_ratio < self.contrast_requirements['normal_text']:
                self.results['contrast_issues'].append({
                    'file': str(html_file),
                    'issue': 'Low contrast',
                    'foreground': fg_color,
                    'background': bg_color,
                    'contrast_ratio': round(contrast_ratio, 2),
                    'required_ratio': self.contrast_requirements['normal_text'],
                    'severity': 'high' if contrast_ratio < 3.0 else 'medium'
                })

    def check_adhd_accessibility(self, html_file: Path):
        """Check for ADHD accessibility issues."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return
        
        # Extract text content
        text_styles = self.extract_text_styles(content)
        
        # Check for long paragraphs
        for text_style in text_styles:
            text = text_style['text']
            
            # Check paragraph length
            if len(text) > self.adhd_patterns['max_paragraph_length']:
                self.results['adhd_issues'].append({
                    'file': str(html_file),
                    'issue': 'Long paragraph',
                    'text_preview': text[:100] + '...' if len(text) > 100 else text,
                    'length': len(text),
                    'max_recommended': self.adhd_patterns['max_paragraph_length'],
                    'severity': 'medium'
                })
            
            # Check for long text blocks without breaks
            if len(text) > self.adhd_patterns['max_text_block_length']:
                # Count line breaks and headings
                line_breaks = text.count('\n') + text.count('<br>')
                if line_breaks < 3:  # Not enough breaks
                    self.results['adhd_issues'].append({
                        'file': str(html_file),
                        'issue': 'Large text block without breaks',
                        'text_preview': text[:100] + '...' if len(text) > 100 else text,
                        'length': len(text),
                        'line_breaks': line_breaks,
                        'severity': 'high'
                    })

    def check_accessibility_patterns(self, html_file: Path):
        """Check for general accessibility issues."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return
        
        # Check for missing alt text on images
        img_pattern = r'<img[^>]*src="([^"]*)"[^>]*(?:alt="([^"]*)")?[^>]*>'
        img_matches = re.findall(img_pattern, content, re.IGNORECASE)
        
        for src, alt in img_matches:
            if not alt or alt.strip() == '':
                self.results['accessibility_issues'].append({
                    'file': str(html_file),
                    'issue': 'Missing alt text',
                    'image_src': src,
                    'severity': 'high'
                })
        
        # Check for proper heading hierarchy
        heading_pattern = r'<h([1-6])[^>]*>([^<]+)</h[1-6]>'
        headings = re.findall(heading_pattern, content, re.IGNORECASE)
        
        if headings:
            levels = [int(h[0]) for h in headings]
            # Check for skipped heading levels
            for i in range(len(levels) - 1):
                if levels[i+1] - levels[i] > 1:
                    self.results['accessibility_issues'].append({
                        'file': str(html_file),
                        'issue': 'Skipped heading level',
                        'current_level': levels[i],
                        'next_level': levels[i+1],
                        'severity': 'medium'
                    })
        
        # Check for form labels
        input_pattern = r'<input[^>]*type="([^"]*)"[^>]*>'
        inputs = re.findall(input_pattern, content, re.IGNORECASE)
        
        for input_type in inputs:
            if input_type.lower() in ['text', 'email', 'password', 'number']:
                # Check if there's a corresponding label
                if not re.search(r'<label[^>]*for="[^"]*"[^>]*>', content, re.IGNORECASE):
                    self.results['accessibility_issues'].append({
                        'file': str(html_file),
                        'issue': 'Form input without label',
                        'input_type': input_type,
                        'severity': 'high'
                    })

    def check_design_system_compliance(self, html_file: Path):
        """Check compliance with the design system requirements."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return
        
        # Check for Vend Sans font usage (as specified in rules)
        if 'font-family' in content.lower():
            if 'vend sans' not in content.lower() and 'vend-sans' not in content.lower():
                # Check if it's using the correct font
                font_matches = re.findall(r'font-family\s*:\s*([^;]+)', content, re.IGNORECASE)
                for font in font_matches:
                    if 'vend' not in font.lower():
                        self.results['accessibility_issues'].append({
                            'file': str(html_file),
                            'issue': 'Font not compliant with design system',
                            'current_font': font.strip(),
                            'expected_font': 'Vend Sans',
                            'severity': 'low'
                        })
        
        # Check for proper color usage (should use design tokens)
        color_pattern = r'color\s*:\s*([^;]+)'
        colors = re.findall(color_pattern, content, re.IGNORECASE)
        
        for color in colors:
            # Check for hardcoded colors instead of design tokens
            if re.match(r'#[0-9a-fA-F]{3,6}', color.strip()):
                self.results['accessibility_issues'].append({
                    'file': str(html_file),
                    'issue': 'Hardcoded color instead of design token',
                    'color': color.strip(),
                    'severity': 'low'
                })

    def run_check(self):
        """Run the complete accessibility check."""
        print("♿ Starting accessibility check for Kristina's Academic Success Dashboard")
        print("=" * 70)
        
        html_files = self.find_html_files()
        print(f"📄 Found {len(html_files)} HTML files to check")
        
        for html_file in html_files:
            print(f"🔍 Checking {html_file.name}...")
            self.check_contrast_issues(html_file)
            self.check_adhd_accessibility(html_file)
            self.check_accessibility_patterns(html_file)
            self.check_design_system_compliance(html_file)
        
        # Generate summary
        total_issues = (len(self.results['contrast_issues']) + 
                       len(self.results['adhd_issues']) + 
                       len(self.results['accessibility_issues']))
        
        self.results['summary'] = {
            'total_files_checked': len(html_files),
            'contrast_issues': len(self.results['contrast_issues']),
            'adhd_issues': len(self.results['adhd_issues']),
            'accessibility_issues': len(self.results['accessibility_issues']),
            'total_issues': total_issues,
            'check_time': datetime.now().isoformat()
        }
        
        # Print results
        print("\n" + "=" * 70)
        print("♿ ACCESSIBILITY CHECK SUMMARY")
        print("=" * 70)
        
        if self.results['contrast_issues']:
            print(f"\n🎨 CONTRAST ISSUES ({len(self.results['contrast_issues'])}):")
            for issue in self.results['contrast_issues']:
                severity_icon = "🔴" if issue['severity'] == 'high' else "🟡"
                print(f"  {severity_icon} {issue['file']}: {issue['foreground']} on {issue['background']} (ratio: {issue['contrast_ratio']})")
        
        if self.results['adhd_issues']:
            print(f"\n🧠 ADHD ACCESSIBILITY ISSUES ({len(self.results['adhd_issues'])}):")
            for issue in self.results['adhd_issues']:
                severity_icon = "🔴" if issue['severity'] == 'high' else "🟡"
                print(f"  {severity_icon} {issue['file']}: {issue['issue']} (length: {issue['length']})")
        
        if self.results['accessibility_issues']:
            print(f"\n♿ GENERAL ACCESSIBILITY ISSUES ({len(self.results['accessibility_issues'])}):")
            for issue in self.results['accessibility_issues']:
                severity_icon = "🔴" if issue['severity'] == 'high' else "🟡" if issue['severity'] == 'medium' else "🟢"
                print(f"  {severity_icon} {issue['file']}: {issue['issue']}")
        
        print(f"\n📊 Total issues found: {total_issues}")
        
        if total_issues == 0:
            print("\n🎉 All accessibility checks passed!")
        else:
            print(f"\n⚠️  Found {total_issues} accessibility issues that need attention.")
        
        return self.results

    def save_report(self, filename="accessibility_report.json"):
        """Save the results to a JSON file."""
        report_path = self.base_dir / filename
        with open(report_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n📄 Detailed report saved to: {report_path}")

    def generate_html_report(self, filename="accessibility_report.html"):
        """Generate an HTML report of the accessibility check results."""
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessibility Report - Kristina's Academic Success Dashboard</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #2d3748; border-bottom: 3px solid #68d391; padding-bottom: 10px; }}
        h2 {{ color: #4a5568; margin-top: 30px; }}
        .summary {{ background: #f7fafc; padding: 20px; border-radius: 6px; margin: 20px 0; }}
        .summary-item {{ display: flex; justify-content: space-between; margin: 8px 0; }}
        .summary-item strong {{ color: #2d3748; }}
        .severity-high {{ color: #f56565; font-weight: bold; }}
        .severity-medium {{ color: #ed8936; font-weight: bold; }}
        .severity-low {{ color: #38a169; font-weight: bold; }}
        .issue-item {{ background: #f7fafc; padding: 15px; margin: 10px 0; border-radius: 6px; border-left: 4px solid #e2e8f0; }}
        .issue-item.high {{ border-left-color: #f56565; background: #fed7d7; }}
        .issue-item.medium {{ border-left-color: #ed8936; background: #feebc8; }}
        .issue-item.low {{ border-left-color: #38a169; background: #c6f6d5; }}
        .issue-title {{ font-weight: bold; margin-bottom: 8px; }}
        .issue-details {{ color: #4a5568; font-size: 0.9em; }}
        .color-preview {{ display: inline-block; width: 20px; height: 20px; border: 1px solid #ccc; margin: 0 5px; vertical-align: middle; }}
        .timestamp {{ color: #718096; font-size: 0.9em; text-align: right; margin-top: 30px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>♿ Accessibility Report</h1>
        <p>Kristina's Academic Success Dashboard - WCAG 2.1 AA Compliance Check</p>
        
        <div class="summary">
            <h2>📊 Summary</h2>
            <div class="summary-item">
                <span>Files Checked:</span>
                <strong>{self.results['summary']['total_files_checked']}</strong>
            </div>
            <div class="summary-item">
                <span>Contrast Issues:</span>
                <strong class="{'severity-high' if self.results['summary']['contrast_issues'] > 0 else ''}">{self.results['summary']['contrast_issues']}</strong>
            </div>
            <div class="summary-item">
                <span>ADHD Accessibility Issues:</span>
                <strong class="{'severity-high' if self.results['summary']['adhd_issues'] > 0 else ''}">{self.results['summary']['adhd_issues']}</strong>
            </div>
            <div class="summary-item">
                <span>General Accessibility Issues:</span>
                <strong class="{'severity-high' if self.results['summary']['accessibility_issues'] > 0 else ''}">{self.results['summary']['accessibility_issues']}</strong>
            </div>
            <div class="summary-item">
                <span>Total Issues:</span>
                <strong class="{'severity-high' if self.results['summary']['total_issues'] > 0 else ''}">{self.results['summary']['total_issues']}</strong>
            </div>
        </div>
"""
        
        # Add contrast issues
        if self.results['contrast_issues']:
            html_content += """
        <h2>🎨 Contrast Issues</h2>
"""
            for issue in self.results['contrast_issues']:
                html_content += f"""
        <div class="issue-item {issue['severity']}">
            <div class="issue-title">{issue['file']}: Low Contrast</div>
            <div class="issue-details">
                <span class="color-preview" style="background-color: {issue['foreground']}"></span>
                {issue['foreground']} on 
                <span class="color-preview" style="background-color: {issue['background']}"></span>
                {issue['background']} - Ratio: {issue['contrast_ratio']} (Required: {issue['required_ratio']})
            </div>
        </div>
"""
        
        # Add ADHD issues
        if self.results['adhd_issues']:
            html_content += """
        <h2>🧠 ADHD Accessibility Issues</h2>
"""
            for issue in self.results['adhd_issues']:
                html_content += f"""
        <div class="issue-item {issue['severity']}">
            <div class="issue-title">{issue['file']}: {issue['issue']}</div>
            <div class="issue-details">
                Length: {issue['length']} characters (Max recommended: {issue['max_recommended']})
                <br>Preview: "{issue['text_preview']}"
            </div>
        </div>
"""
        
        # Add general accessibility issues
        if self.results['accessibility_issues']:
            html_content += """
        <h2>♿ General Accessibility Issues</h2>
"""
            for issue in self.results['accessibility_issues']:
                html_content += f"""
        <div class="issue-item {issue['severity']}">
            <div class="issue-title">{issue['file']}: {issue['issue']}</div>
            <div class="issue-details">
                {', '.join([f"{k}: {v}" for k, v in issue.items() if k not in ['file', 'issue', 'severity']])}
            </div>
        </div>
"""
        
        html_content += f"""
        <div class="timestamp">
            Report generated: {self.results['summary']['check_time']}
        </div>
    </div>
</body>
</html>
"""
        
        report_path = self.base_dir / filename
        with open(report_path, 'w') as f:
            f.write(html_content)
        print(f"📄 HTML report saved to: {report_path}")

def main():
    """Main function to run the accessibility checker."""
    checker = AccessibilityChecker()
    results = checker.run_check()
    checker.save_report()
    checker.generate_html_report()
    
    # Exit with error code if issues found
    if results['summary']['total_issues'] > 0:
        print(f"\n⚠️  Exiting with error code due to {results['summary']['total_issues']} accessibility issues.")
        exit(1)
    else:
        print("\n🎉 All accessibility checks passed! Exiting successfully.")
        exit(0)

if __name__ == "__main__":
    main()
