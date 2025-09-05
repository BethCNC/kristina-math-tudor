#!/usr/bin/env python3
"""
Update HTML Links to Point to New HTML Files Instead of Markdown
Updates all references from .md files to .html files.
"""

import os
import re
from pathlib import Path

class MarkdownLinkUpdater:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.updates_applied = []
        
    def find_html_files(self):
        """Find all HTML files that need updating."""
        html_files = []
        for pattern in ['*.html', '**/*.html']:
            html_files.extend(self.base_dir.glob(pattern))
        
        # Exclude dist, node_modules, and report files
        return [f for f in html_files if f.is_file() and not any(part in str(f) for part in ['dist', 'node_modules', 'accessibility_report', 'link_check_report', 'color_accessibility_report']) and f.name not in ['accessibility_report.html', 'link_check_report.html', 'color_accessibility_report.html']]
    
    def update_markdown_links(self, content, file_path):
        """Update markdown file links to HTML file links."""
        updates = 0
        
        # Find all markdown file references
        markdown_links = re.findall(r'href="([^"]*\.md)"', content)
        
        for md_link in markdown_links:
            # Convert .md to .html
            html_link = md_link.replace('.md', '.html')
            
            # Update the link in content
            content = content.replace(f'href="{md_link}"', f'href="{html_link}"')
            updates += 1
            self.updates_applied.append(f"Updated {md_link} to {html_link} in {file_path.name}")
        
        return content, updates
    
    def update_file(self, file_path):
        """Update markdown links in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            total_updates = 0
            
            # Apply updates
            content, updates = self.update_markdown_links(content, file_path)
            total_updates += updates
            
            # Write back if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Updated {total_updates} markdown links in {file_path.name}")
                return total_updates
            else:
                print(f"ℹ️  No markdown links to update in {file_path.name}")
                return 0
                
        except Exception as e:
            print(f"❌ Error updating {file_path.name}: {e}")
            return 0
    
    def run(self):
        """Run the markdown link updater on all HTML files."""
        print("🔧 Starting markdown link updates...")
        print("=" * 60)
        
        html_files = self.find_html_files()
        print(f"📄 Found {len(html_files)} HTML files to check")
        
        total_updates = 0
        files_updated = 0
        
        for file_path in html_files:
            updates = self.update_file(file_path)
            total_updates += updates
            if updates > 0:
                files_updated += 1
        
        print("=" * 60)
        print(f"🎉 MARKDOWN LINK UPDATES COMPLETE")
        print(f"📊 Files processed: {len(html_files)}")
        print(f"🔧 Files updated: {files_updated}")
        print(f"✅ Total updates applied: {total_updates}")
        
        if self.updates_applied:
            print("\n📋 Updates applied:")
            for update in self.updates_applied[:15]:  # Show first 15
                print(f"  • {update}")
            if len(self.updates_applied) > 15:
                print(f"  ... and {len(self.updates_applied) - 15} more")
        
        return total_updates

if __name__ == "__main__":
    updater = MarkdownLinkUpdater()
    updater.run()
