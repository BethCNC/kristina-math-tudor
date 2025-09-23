#!/usr/bin/env python3
"""
Integrate ALL course materials into the AI tutor system.
This script reads all course materials and creates a comprehensive knowledge base.
"""

import json
import os
from pathlib import Path
import re

def extract_content_from_file(file_path):
    """Extract meaningful content from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove HTML tags if it's an HTML file
        if file_path.suffix == '.html':
            content = re.sub(r'<[^>]+>', '', content)
        
        # Clean up whitespace
        content = re.sub(r'\s+', ' ', content).strip()
        
        return content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def build_comprehensive_knowledge_base():
    """Build a comprehensive knowledge base from all course materials."""
    
    course_materials_dir = Path("course_materials")
    knowledge_base = {
        "math": {
            "formulas": {},
            "concepts": {},
            "examples": {},
            "study_guides": {},
            "schedules": {},
            "assignments": {}
        },
        "english": {
            "writing_guides": {},
            "essay_requirements": {},
            "citation_guides": {}
        }
    }
    
    if not course_materials_dir.exists():
        print("❌ course_materials directory not found!")
        return knowledge_base
    
    # Process all files in course_materials
    for file_path in course_materials_dir.rglob("*"):
        if file_path.is_file() and file_path.suffix in ['.html', '.md']:
            content = extract_content_from_file(file_path)
            if not content:
                continue
            
            # Categorize content based on file path and content
            relative_path = file_path.relative_to(course_materials_dir)
            path_parts = str(relative_path).split('/')
            
            # Determine category
            if 'formula' in str(file_path).lower():
                if 'chapter_6' in str(file_path):
                    knowledge_base["math"]["formulas"]["chapter_6"] = content
                elif 'chapter_7' in str(file_path):
                    knowledge_base["math"]["formulas"]["chapter_7"] = content
                elif 'unit_4' in str(file_path):
                    knowledge_base["math"]["formulas"]["unit_4"] = content
                elif 'unit_1' in str(file_path):
                    knowledge_base["math"]["formulas"]["unit_1"] = content
                else:
                    knowledge_base["math"]["formulas"]["general"] = content
            
            elif 'schedule' in str(file_path).lower():
                knowledge_base["math"]["schedules"]["fall_2025"] = content
            
            elif 'guide' in str(file_path).lower():
                if 'all_sections' in str(file_path):
                    knowledge_base["math"]["study_guides"]["complete_guide"] = content
                else:
                    knowledge_base["math"]["study_guides"]["general"] = content
            
            elif 'hawkes' in str(file_path).lower():
                knowledge_base["math"]["assignments"]["hawkes_setup"] = content
            
            elif 'resources' in str(file_path).lower():
                knowledge_base["math"]["concepts"]["chapter_resources"] = content
            
            elif 'sample' in str(file_path).lower():
                knowledge_base["math"]["assignments"]["sample_assignments"] = content
            
            else:
                # General content
                if 'math' in str(file_path).lower() or 'mat' in str(file_path).lower():
                    knowledge_base["math"]["concepts"]["general"] = content
                else:
                    knowledge_base["english"]["writing_guides"]["general"] = content
    
    return knowledge_base

def create_enhanced_knowledge_base():
    """Create an enhanced knowledge base with all course materials."""
    print("🔍 Building comprehensive knowledge base from course materials...")
    
    knowledge_base = build_comprehensive_knowledge_base()
    
    # Add specific course information
    knowledge_base["course_info"] = {
        "mat143": {
            "title": "MAT 143 - Quantitative Literacy",
            "chapters": {
                1: "Thinking Mathematically, Estimating, Problem Solving",
                4: "Proportions, Percentages, and Ratios", 
                5: "Linear and Exponential Functions",
                6: "Personal Finance (Interest, Saving, Borrowing)",
                7: "Measurement and Conversions",
                10: "Probability and Expected Value",
                11: "Statistics and Data Analysis",
                13: "Voting Methods and Apportionment"
            },
            "test_schedule": {
                "Test 1": "Week 4 (Sept 8-12) - Chapters 1 & 13",
                "Test 2": "Week 7 (Sept 29-Oct 3) - Chapters 4 & 5",
                "Test 3": "Week 11 (Nov 3-7) - Chapters 6 & 7", 
                "Test 4": "Week 16 (Dec 8-12) - Chapters 10 & 11"
            },
            "important_dates": {
                "semester_start": "August 18, 2025",
                "semester_end": "December 12, 2025",
                "census_date": "August 29, 2025",
                "last_withdraw": "September 26, 2025"
            }
        },
        "eng111": {
            "title": "ENG 111 - Writing and Inquiry",
            "current_assignments": {
                "cause_effect_essay": "Due September 22, 2025"
            }
        }
    }
    
    # Save the enhanced knowledge base
    output_path = Path("ai_knowledge_base_comprehensive.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Comprehensive knowledge base saved to {output_path}")
    print(f"📊 Total sections: {sum(len(section) for section in knowledge_base['math'].values())}")
    
    return knowledge_base

if __name__ == "__main__":
    create_enhanced_knowledge_base()
