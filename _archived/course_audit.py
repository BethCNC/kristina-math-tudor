#!/usr/bin/env python3
"""
Comprehensive audit tool to verify ALL course materials are integrated into the app.
This script compares course_materials/ content with actual app implementation.
"""

import os
import re
from pathlib import Path

def read_file_content(file_path):
    """Safely read file content with proper encoding handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                return f.read()
        except:
            return f"[ERROR: Could not read file {file_path}]"
    except:
        return f"[ERROR: File not found {file_path}]"

def extract_topics_from_course_materials():
    """Extract all topics, formulas, and concepts from course_materials/"""
    materials = {}
    
    # Check course_materials directory
    course_materials_dir = Path("course_materials")
    if not course_materials_dir.exists():
        print("⚠️ course_materials directory not found!")
        return materials
    
    # Scan all files in course_materials
    for root, dirs, files in os.walk(course_materials_dir):
        for file in files:
            if file.endswith(('.md', '.txt')):
                file_path = Path(root) / file
                content = read_file_content(file_path)
                materials[str(file_path)] = {
                    'content': content,
                    'topics': extract_topics_from_text(content),
                    'formulas': extract_formulas_from_text(content)
                }
    
    return materials

def extract_topics_from_text(content):
    """Extract topics, sections, and key concepts from text."""
    topics = []
    
    # Extract headers (markdown format)
    headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
    topics.extend(headers)
    
    # Extract numbered sections
    sections = re.findall(r'^\d+\.\d+\s+(.+)$', content, re.MULTILINE)
    topics.extend(sections)
    
    # Extract bullet points with key concepts
    bullets = re.findall(r'^\*\s+(.+)$', content, re.MULTILINE)
    topics.extend([b for b in bullets if len(b) > 10])  # Filter short bullets
    
    return list(set(topics))  # Remove duplicates

def extract_formulas_from_text(content):
    """Extract mathematical formulas from text."""
    formulas = []
    
    # Look for formula patterns
    formula_patterns = [
        r'[A-Z]\s*=\s*[^\\n]+',  # Basic formula like P = rt
        r'\*\*[^*]+\*\*',  # Bold formulas
        r'`[^`]+`',  # Code-formatted formulas
        r'^\s*[\w\s]+:\s*[A-Z].*=.*$'  # Formula descriptions
    ]
    
    for pattern in formula_patterns:
        matches = re.findall(pattern, content, re.MULTILINE)
        formulas.extend(matches)
    
    return list(set(formulas))

def check_app_implementation():
    """Check what's actually implemented in the app."""
    app_content = {}
    
    # Check all HTML files
    html_files = list(Path(".").glob("*.html"))
    for html_file in html_files:
        content = read_file_content(html_file)
        app_content[str(html_file)] = {
            'content': content,
            'topics': extract_topics_from_html(content),
            'formulas': extract_formulas_from_html(content)
        }
    
    return app_content

def extract_topics_from_html(content):
    """Extract topics and concepts from HTML content."""
    topics = []
    
    # Extract text from headers
    headers = re.findall(r'<h[1-6][^>]*>([^<]+)</h[1-6]>', content, re.IGNORECASE)
    topics.extend(headers)
    
    # Extract tutorial titles
    tutorials = re.findall(r'Tutorial[^<]*:([^<]+)', content, re.IGNORECASE)
    topics.extend(tutorials)
    
    # Extract section titles
    sections = re.findall(r'<span[^>]*>([^<]+)</span>', content)
    topics.extend([s.strip() for s in sections if len(s.strip()) > 5])
    
    return list(set(topics))

def extract_formulas_from_html(content):
    """Extract formulas from HTML content."""
    formulas = []
    
    # Extract formulas from code blocks
    code_blocks = re.findall(r'<code[^>]*>([^<]+)</code>', content, re.IGNORECASE)
    formulas.extend(code_blocks)
    
    # Extract from font-mono classes (likely formulas)
    mono_text = re.findall(r'font-mono[^>]*>([^<]+)<', content)
    formulas.extend(mono_text)
    
    # Extract mathematical expressions
    math_expressions = re.findall(r'[A-Z]\s*=\s*[^<>\n]+', content)
    formulas.extend(math_expressions)
    
    return list(set(formulas))

def generate_audit_report():
    """Generate comprehensive audit report."""
    print("🔍 MAT 143 & ENG 111 Course Materials Audit")
    print("=" * 50)
    
    # Get course materials
    print("📚 Scanning course_materials directory...")
    course_materials = extract_topics_from_course_materials()
    
    # Get app implementation
    print("🖥️ Scanning app implementation...")
    app_content = check_app_implementation()
    
    # Generate report
    report = []
    report.append("# Course Materials vs App Implementation Audit\n")
    
    report.append("## Course Materials Found:\n")
    for file_path, data in course_materials.items():
        report.append(f"### {file_path}")
        report.append(f"**Topics ({len(data['topics'])}):** {', '.join(data['topics'][:10])}{'...' if len(data['topics']) > 10 else ''}")
        report.append(f"**Formulas ({len(data['formulas'])}):** {', '.join(data['formulas'][:5])}{'...' if len(data['formulas']) > 5 else ''}")
        report.append("")
    
    report.append("## App Implementation Found:\n")
    for file_path, data in app_content.items():
        if 'chapter-' in file_path or 'english' in file_path:
            report.append(f"### {file_path}")
            report.append(f"**Topics ({len(data['topics'])}):** {', '.join(data['topics'][:10])}{'...' if len(data['topics']) > 10 else ''}")
            report.append(f"**Formulas ({len(data['formulas'])}):** {', '.join(data['formulas'][:5])}{'...' if len(data['formulas']) > 5 else ''}")
            report.append("")
    
    # Write report
    with open("course_audit_report.md", "w") as f:
        f.write("\n".join(report))
    
    print(f"📊 Found {len(course_materials)} course material files")
    print(f"📱 Found {len([f for f in app_content.keys() if 'chapter-' in f or 'english' in f])} app content files")
    print("📄 Detailed report saved to: course_audit_report.md")
    
    return course_materials, app_content

if __name__ == "__main__":
    generate_audit_report()