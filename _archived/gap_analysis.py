#!/usr/bin/env python3
"""
Gap analysis to identify missing content between course materials and app implementation.
"""

import re
from pathlib import Path

def analyze_gaps():
    """Identify specific missing content."""
    gaps = {}
    
    # Check specific formula sheets that might be missing from app
    formula_sheets = {
        "Chapter_6_Formula_Sheet.md": "chapter-6.html",
        "Chapter_7_Formula_Sheet.md": "chapter-7.html", 
        "Unit_1_Formula_Sheet.md": "chapter-13.html",
        "Unit_4_Formula_Sheet.md": ["chapter-10.html", "chapter-11.html"]
    }
    
    # Read course formula sheets
    for sheet, target in formula_sheets.items():
        sheet_path = Path("course_materials/formula_sheets") / sheet
        if sheet_path.exists():
            with open(sheet_path) as f:
                sheet_content = f.read()
            
            # Extract key formulas
            formulas = extract_key_formulas(sheet_content)
            
            # Check if these formulas are in the target files
            targets = [target] if isinstance(target, str) else target
            
            for target_file in targets:
                if Path(target_file).exists():
                    with open(target_file) as f:
                        app_content = f.read()
                    
                    missing_formulas = []
                    for formula in formulas:
                        if not is_formula_in_app(formula, app_content):
                            missing_formulas.append(formula)
                    
                    if missing_formulas:
                        gaps[f"{sheet} -> {target_file}"] = missing_formulas
    
    return gaps

def extract_key_formulas(content):
    """Extract key mathematical formulas from course material."""
    formulas = []
    
    # Look for various formula patterns
    patterns = [
        r'\*\*([^*]+\s*=\s*[^*]+)\*\*',  # Bold formulas like **I = Prt**
        r'^([A-Z]\w*\s*=\s*.+)$',  # Simple formulas like I = Prt
        r'([A-Z]+\([^)]+\)\s*=\s*.+)',  # Function formulas like APY(r) = ...
        r'(E\(X\)\s*=\s*.+)',  # Expected value
        r'(z\s*=\s*.+)',  # Z-score formulas
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content, re.MULTILINE)
        formulas.extend(matches)
    
    return [f.strip() for f in formulas if len(f.strip()) > 3]

def is_formula_in_app(formula, app_content):
    """Check if a formula exists in the app content (with some flexibility)."""
    # Clean up the formula for comparison
    clean_formula = formula.replace("**", "").strip()
    
    # Check exact match
    if clean_formula in app_content:
        return True
    
    # Check for key parts of the formula
    if "=" in clean_formula:
        left_side = clean_formula.split("=")[0].strip()
        if left_side in app_content:
            return True
    
    return False

def check_chapter_completeness():
    """Check if each chapter has all required sections from course materials."""
    completeness = {}
    
    # Define expected sections for each chapter based on course materials
    expected_sections = {
        "chapter-1.html": ["1.1 Thinking Mathematically", "1.2 Estimating and Evaluating", "1.3 Problem Solving"],
        "chapter-4.html": ["4.1 Proportions", "4.2 Using Percentages", "4.3 Rates", "4.4 Dimensional Analysis"],
        "chapter-5.html": ["Linear Functions", "Linear Modeling", "Exponential Functions"],
        "chapter-6.html": ["6.1 Understanding Interest", "6.2 Saving and Investing", "6.3 Borrowing Money", "6.4 Federal Revenue", "6.5 Budgeting"],
        "chapter-7.html": ["7.4 The Metric System", "7.5 Converting between Systems"],
        "chapter-10.html": ["10.1 Introduction to Probability", "10.3 Probability of Single Events", "10.6 Expected Value"],
        "chapter-11.html": ["11.1 Statistical Studies", "11.2 Displaying Data", "11.3 Describing Data", "11.4 Normal Distribution"],
        "chapter-13.html": ["13.1 How to Determine a Winner", "13.2 Flaws in Voting Methods", "13.3 Apportionment"]
    }
    
    for chapter_file, expected in expected_sections.items():
        if Path(chapter_file).exists():
            with open(chapter_file) as f:
                content = f.read()
            
            missing_sections = []
            for section in expected:
                # Check if section is mentioned in the file (flexible matching)
                section_key = section.split()[-1].lower()  # Get the key word
                if section_key not in content.lower():
                    missing_sections.append(section)
            
            if missing_sections:
                completeness[chapter_file] = missing_sections
    
    return completeness

def generate_gap_report():
    """Generate comprehensive gap analysis report."""
    print("🔍 DETAILED GAP ANALYSIS")
    print("=" * 50)
    
    # Formula gaps
    formula_gaps = analyze_gaps()
    print(f"📊 Formula gaps found: {len(formula_gaps)}")
    
    # Chapter completeness
    missing_sections = check_chapter_completeness()
    print(f"📚 Chapters with missing sections: {len(missing_sections)}")
    
    # Generate detailed report
    report = []
    report.append("# COMPREHENSIVE GAP ANALYSIS REPORT\n")
    
    if formula_gaps:
        report.append("## ⚠️ MISSING FORMULAS\n")
        for source, formulas in formula_gaps.items():
            report.append(f"### {source}")
            for formula in formulas:
                report.append(f"- `{formula}`")
            report.append("")
    
    if missing_sections:
        report.append("## ⚠️ MISSING COURSE SECTIONS\n")
        for chapter, sections in missing_sections.items():
            report.append(f"### {chapter}")
            for section in sections:
                report.append(f"- {section}")
            report.append("")
    
    # Check for specific course materials not integrated
    report.append("## 📋 SPECIFIC MISSING INTEGRATIONS\n")
    
    # Week 1 Attendance Sample
    sample_path = Path("course_materials/sample_assignments/Week_1_Attendance_Sample.md")
    if sample_path.exists():
        with open(sample_path) as f:
            sample_content = f.read()
        
        if "Sequence Types" in sample_content:
            # Check if this content is in any chapter
            found = False
            for chapter_file in Path(".").glob("chapter-*.html"):
                with open(chapter_file) as f:
                    if "sequence" in f.read().lower():
                        found = True
                        break
            
            if not found:
                report.append("- **Week 1 Attendance Sample content** (Sequence Types, Deductive vs Inductive examples) not integrated into any chapter")
    
    # Hawkes Learning Setup
    setup_path = Path("course_materials/instructions/Hawkes_Learning_Setup.md")
    if setup_path.exists():
        # Check if this is linked from anywhere
        setup_found = False
        for html_file in Path(".").glob("*.html"):
            with open(html_file) as f:
                if "hawkes" in f.read().lower():
                    setup_found = True
                    break
        
        if not setup_found:
            report.append("- **Hawkes Learning Setup Instructions** not linked from any page")
    
    # Write report
    with open("detailed_gap_analysis.md", "w") as f:
        f.write("\n".join(report))
    
    print("📄 Detailed gap report saved to: detailed_gap_analysis.md")
    
    return formula_gaps, missing_sections

if __name__ == "__main__":
    generate_gap_report()