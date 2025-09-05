#!/usr/bin/env python3
"""
Broken Link Checker for Kristina's Academic Success Dashboard
Scans all HTML files for internal and external links and validates their status.
"""

import os
import re
import requests
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from datetime import datetime

class LinkChecker:
    def __init__(self, base_dir=".", max_workers=10, timeout=10):
        self.base_dir = Path(base_dir)
        self.max_workers = max_workers
        self.timeout = timeout
        self.results = {
            'internal_links': [],
            'external_links': [],
            'broken_links': [],
            'file_links': [],
            'summary': {}
        }
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; LinkChecker/1.0)'
        })

    def find_html_files(self):
        """Find all HTML files in the project."""
        html_files = []
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.base_dir.glob(pattern))
        return [f for f in html_files if f.is_file()]

    def extract_links_from_html(self, html_file):
        """Extract all links from an HTML file."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(html_file, 'r', encoding='latin-1') as f:
                    content = f.read()
            except:
                print(f"⚠️  Could not read {html_file}")
                return []

        links = []
        
        # Find href attributes
        href_pattern = r'href\s*=\s*["\']([^"\']+)["\']'
        href_matches = re.findall(href_pattern, content, re.IGNORECASE)
        
        # Find src attributes (for images, scripts, etc.)
        src_pattern = r'src\s*=\s*["\']([^"\']+)["\']'
        src_matches = re.findall(src_pattern, content, re.IGNORECASE)
        
        for link in href_matches + src_matches:
            links.append({
                'url': link,
                'file': str(html_file),
                'type': 'href' if link in href_matches else 'src'
            })
        
        return links

    def categorize_link(self, link, base_file):
        """Categorize a link as internal, external, or file."""
        url = link['url']
        
        # Skip javascript, mailto, tel, etc.
        if url.startswith(('javascript:', 'mailto:', 'tel:', '#', 'data:')):
            return None
        
        # Check if it's a file path
        if not url.startswith(('http://', 'https://', '//')):
            return {
                'type': 'file',
                'url': url,
                'file': link['file'],
                'link_type': link['type']
            }
        
        # Check if it's internal (same domain)
        parsed_url = urlparse(url)
        if parsed_url.netloc in ['', 'localhost', '127.0.0.1']:
            return {
                'type': 'internal',
                'url': url,
                'file': link['file'],
                'link_type': link['type']
            }
        
        # External link
        return {
            'type': 'external',
            'url': url,
            'file': link['file'],
            'link_type': link['type']
        }

    def check_file_link(self, link_info):
        """Check if a file link exists."""
        url = link_info['url']
        base_file = Path(link_info['file'])
        
        # Handle relative paths
        if url.startswith('/'):
            # Absolute path from project root
            file_path = self.base_dir / url.lstrip('/')
        else:
            # Relative path from current file
            file_path = base_file.parent / url
        
        # Check if file exists
        exists = file_path.exists()
        
        return {
            'url': url,
            'file': link_info['file'],
            'link_type': link_info['link_type'],
            'exists': exists,
            'resolved_path': str(file_path),
            'status': 'OK' if exists else 'BROKEN'
        }

    def check_http_link(self, link_info):
        """Check if an HTTP/HTTPS link is accessible."""
        url = link_info['url']
        
        try:
            response = self.session.head(url, timeout=self.timeout, allow_redirects=True)
            status = 'OK' if response.status_code < 400 else 'BROKEN'
            return {
                'url': url,
                'file': link_info['file'],
                'link_type': link_info['link_type'],
                'status': status,
                'status_code': response.status_code,
                'final_url': response.url
            }
        except requests.exceptions.RequestException as e:
            return {
                'url': url,
                'file': link_info['file'],
                'link_type': link_info['link_type'],
                'status': 'BROKEN',
                'error': str(e),
                'status_code': None
            }

    def run_check(self):
        """Run the complete link check."""
        print("🔍 Starting link check for Kristina's Academic Success Dashboard")
        print("=" * 60)
        
        # Find all HTML files
        html_files = self.find_html_files()
        print(f"📄 Found {len(html_files)} HTML files to check")
        
        # Extract all links
        all_links = []
        for html_file in html_files:
            links = self.extract_links_from_html(html_file)
            all_links.extend(links)
        
        print(f"🔗 Found {len(all_links)} total links")
        
        # Categorize links
        categorized_links = []
        for link in all_links:
            categorized = self.categorize_link(link, link['file'])
            if categorized:
                categorized_links.append(categorized)
        
        # Separate by type
        file_links = [l for l in categorized_links if l['type'] == 'file']
        internal_links = [l for l in categorized_links if l['type'] == 'internal']
        external_links = [l for l in categorized_links if l['type'] == 'external']
        
        print(f"📁 File links: {len(file_links)}")
        print(f"🏠 Internal links: {len(internal_links)}")
        print(f"🌐 External links: {len(external_links)}")
        
        # Check file links
        print("\n📁 Checking file links...")
        file_results = []
        for link in file_links:
            result = self.check_file_link(link)
            file_results.append(result)
            if not result['exists']:
                print(f"  ❌ {result['url']} (in {result['file']})")
        
        # Check external links
        print("\n🌐 Checking external links...")
        external_results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_link = {executor.submit(self.check_http_link, link): link for link in external_links}
            
            for future in as_completed(future_to_link):
                result = future.result()
                external_results.append(result)
                if result['status'] == 'BROKEN':
                    error_msg = f" (Error: {result.get('error', 'Unknown')})" if 'error' in result else f" (Status: {result.get('status_code', 'Unknown')})"
                    print(f"  ❌ {result['url']} (in {result['file']}){error_msg}")
                else:
                    print(f"  ✅ {result['url']}")
        
        # Store results
        self.results['file_links'] = file_results
        self.results['external_links'] = external_results
        self.results['internal_links'] = internal_links
        
        # Generate summary
        broken_files = [r for r in file_results if r['status'] == 'BROKEN']
        broken_external = [r for r in external_results if r['status'] == 'BROKEN']
        
        self.results['summary'] = {
            'total_links': len(all_links),
            'file_links': len(file_links),
            'external_links': len(external_links),
            'internal_links': len(internal_links),
            'broken_file_links': len(broken_files),
            'broken_external_links': len(broken_external),
            'total_broken': len(broken_files) + len(broken_external),
            'check_time': datetime.now().isoformat()
        }
        
        # Print summary
        print("\n" + "=" * 60)
        print("📊 LINK CHECK SUMMARY")
        print("=" * 60)
        print(f"Total links checked: {self.results['summary']['total_links']}")
        print(f"File links: {self.results['summary']['file_links']} ({self.results['summary']['broken_file_links']} broken)")
        print(f"External links: {self.results['summary']['external_links']} ({self.results['summary']['broken_external_links']} broken)")
        print(f"Internal links: {self.results['summary']['internal_links']}")
        print(f"Total broken links: {self.results['summary']['total_broken']}")
        
        if self.results['summary']['total_broken'] == 0:
            print("\n🎉 All links are working correctly!")
        else:
            print(f"\n⚠️  Found {self.results['summary']['total_broken']} broken links that need attention.")
        
        return self.results

    def save_report(self, filename="link_check_report.json"):
        """Save the results to a JSON file."""
        report_path = self.base_dir / filename
        with open(report_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n📄 Detailed report saved to: {report_path}")

    def generate_html_report(self, filename="link_check_report.html"):
        """Generate an HTML report of the link check results."""
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Link Check Report - Kristina's Academic Success Dashboard</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #2d3748; border-bottom: 3px solid #68d391; padding-bottom: 10px; }}
        h2 {{ color: #4a5568; margin-top: 30px; }}
        .summary {{ background: #f7fafc; padding: 20px; border-radius: 6px; margin: 20px 0; }}
        .summary-item {{ display: flex; justify-content: space-between; margin: 8px 0; }}
        .summary-item strong {{ color: #2d3748; }}
        .status-ok {{ color: #48bb78; font-weight: bold; }}
        .status-broken {{ color: #f56565; font-weight: bold; }}
        .link-item {{ background: #f7fafc; padding: 15px; margin: 10px 0; border-radius: 6px; border-left: 4px solid #e2e8f0; }}
        .link-item.broken {{ border-left-color: #f56565; background: #fed7d7; }}
        .link-item.ok {{ border-left-color: #48bb78; background: #c6f6d5; }}
        .link-url {{ font-family: monospace; background: #edf2f7; padding: 4px 8px; border-radius: 4px; }}
        .link-file {{ color: #718096; font-size: 0.9em; margin-top: 5px; }}
        .error-details {{ color: #e53e3e; font-size: 0.9em; margin-top: 5px; }}
        .timestamp {{ color: #718096; font-size: 0.9em; text-align: right; margin-top: 30px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔗 Link Check Report</h1>
        <p>Kristina's Academic Success Dashboard - Link Validation Results</p>
        
        <div class="summary">
            <h2>📊 Summary</h2>
            <div class="summary-item">
                <span>Total Links Checked:</span>
                <strong>{self.results['summary']['total_links']}</strong>
            </div>
            <div class="summary-item">
                <span>File Links:</span>
                <strong>{self.results['summary']['file_links']} ({self.results['summary']['broken_file_links']} broken)</strong>
            </div>
            <div class="summary-item">
                <span>External Links:</span>
                <strong>{self.results['summary']['external_links']} ({self.results['summary']['broken_external_links']} broken)</strong>
            </div>
            <div class="summary-item">
                <span>Internal Links:</span>
                <strong>{self.results['summary']['internal_links']}</strong>
            </div>
            <div class="summary-item">
                <span>Total Broken Links:</span>
                <strong class="{'status-broken' if self.results['summary']['total_broken'] > 0 else 'status-ok'}">{self.results['summary']['total_broken']}</strong>
            </div>
        </div>
"""
        
        # Add broken file links
        broken_files = [r for r in self.results['file_links'] if r['status'] == 'BROKEN']
        if broken_files:
            html_content += """
        <h2>❌ Broken File Links</h2>
"""
            for link in broken_files:
                html_content += f"""
        <div class="link-item broken">
            <div class="link-url">{link['url']}</div>
            <div class="link-file">File: {link['file']}</div>
            <div class="error-details">Resolved path: {link['resolved_path']}</div>
        </div>
"""
        
        # Add broken external links
        broken_external = [r for r in self.results['external_links'] if r['status'] == 'BROKEN']
        if broken_external:
            html_content += """
        <h2>❌ Broken External Links</h2>
"""
            for link in broken_external:
                error_msg = link.get('error', f"HTTP {link.get('status_code', 'Unknown')}")
                html_content += f"""
        <div class="link-item broken">
            <div class="link-url">{link['url']}</div>
            <div class="link-file">File: {link['file']}</div>
            <div class="error-details">Error: {error_msg}</div>
        </div>
"""
        
        # Add working links summary
        working_files = [r for r in self.results['file_links'] if r['status'] == 'OK']
        working_external = [r for r in self.results['external_links'] if r['status'] == 'OK']
        
        if working_files or working_external:
            html_content += """
        <h2>✅ Working Links</h2>
        <p>All other links are working correctly.</p>
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
    """Main function to run the link checker."""
    checker = LinkChecker()
    results = checker.run_check()
    checker.save_report()
    checker.generate_html_report()
    
    # Exit with error code if broken links found
    if results['summary']['total_broken'] > 0:
        print(f"\n⚠️  Exiting with error code due to {results['summary']['total_broken']} broken links.")
        exit(1)
    else:
        print("\n🎉 All links are working! Exiting successfully.")
        exit(0)

if __name__ == "__main__":
    main()
