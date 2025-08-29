#!/usr/bin/env python3
"""
AI Training System for MAT 143 & ENG 111 Course Materials
This creates a knowledge base from all course materials and integrates it with the AI tutors.
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

class CourseKnowledgeExtractor:
    """Extract and organize knowledge from all course materials."""
    
    def __init__(self):
        self.knowledge_base = {
            'math': {
                'formulas': {},
                'concepts': {},
                'examples': {},
                'procedures': {}
            },
            'english': {
                'writing_process': {},
                'essay_types': {},
                'citations': {},
                'examples': {}
            },
            'metadata': {
                'last_updated': datetime.now().isoformat(),
                'sources': []
            }
        }
    
    def extract_all_course_materials(self):
        """Extract knowledge from all available course materials."""
        print("🧠 Extracting knowledge from all course materials...")
        
        # Extract from course_materials directory
        self.extract_from_directory(Path("course_materials"))
        
        # Extract from english directory
        self.extract_from_directory(Path("english"))
        
        # Extract from implemented app content
        self.extract_from_app_implementation()
        
        return self.knowledge_base
    
    def extract_from_directory(self, directory):
        """Extract knowledge from a specific directory."""
        if not directory.exists():
            return
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(('.md', '.txt', '.html')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        self.process_file_content(str(file_path), content)
                    except Exception as e:
                        print(f"⚠️ Error reading {file_path}: {e}")
    
    def extract_from_app_implementation(self):
        """Extract knowledge from implemented app chapters."""
        chapter_files = list(Path(".").glob("chapter-*.html"))
        for chapter_file in chapter_files:
            try:
                with open(chapter_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.extract_math_knowledge_from_html(str(chapter_file), content)
            except Exception as e:
                print(f"⚠️ Error reading {chapter_file}: {e}")
    
    def process_file_content(self, file_path, content):
        """Process content based on file type and location."""
        self.knowledge_base['metadata']['sources'].append(file_path)
        
        if 'english' in file_path.lower():
            self.extract_english_knowledge(file_path, content)
        else:
            self.extract_math_knowledge(file_path, content)
    
    def extract_math_knowledge(self, file_path, content):
        """Extract mathematical knowledge from content."""
        # Extract formulas
        formulas = self.extract_formulas(content)
        for formula in formulas:
            chapter = self.identify_chapter_from_path(file_path)
            if chapter not in self.knowledge_base['math']['formulas']:
                self.knowledge_base['math']['formulas'][chapter] = []
            self.knowledge_base['math']['formulas'][chapter].append(formula)
        
        # Extract concepts
        concepts = self.extract_math_concepts(content)
        for concept in concepts:
            chapter = self.identify_chapter_from_path(file_path)
            if chapter not in self.knowledge_base['math']['concepts']:
                self.knowledge_base['math']['concepts'][chapter] = []
            self.knowledge_base['math']['concepts'][chapter].append(concept)
        
        # Extract step-by-step procedures
        procedures = self.extract_procedures(content)
        for procedure in procedures:
            chapter = self.identify_chapter_from_path(file_path)
            if chapter not in self.knowledge_base['math']['procedures']:
                self.knowledge_base['math']['procedures'][chapter] = []
            self.knowledge_base['math']['procedures'][chapter].append(procedure)
    
    def extract_math_knowledge_from_html(self, file_path, content):
        """Extract mathematical knowledge from HTML chapter files."""
        chapter = self.identify_chapter_from_path(file_path)
        
        # Extract tutorial content
        tutorials = re.findall(r'Tutorial[^<]*:([^<]+)', content, re.IGNORECASE)
        
        # Extract formulas from HTML
        html_formulas = re.findall(r'<div[^>]*font-mono[^>]*>([^<]+)</div>', content, re.IGNORECASE)
        html_formulas.extend(re.findall(r'([A-Z]\w*\s*=\s*[^<>\n]+)', content))
        
        # Extract examples
        examples = re.findall(r'<strong>Example[^<]*:</strong>([^<]+)', content, re.IGNORECASE)
        
        # Store extracted knowledge
        if chapter not in self.knowledge_base['math']['formulas']:
            self.knowledge_base['math']['formulas'][chapter] = []
        self.knowledge_base['math']['formulas'][chapter].extend(html_formulas)
        
        if chapter not in self.knowledge_base['math']['examples']:
            self.knowledge_base['math']['examples'][chapter] = []
        self.knowledge_base['math']['examples'][chapter].extend(examples)
    
    def extract_english_knowledge(self, file_path, content):
        """Extract English/writing knowledge from content."""
        # Extract essay types and requirements
        essay_info = self.extract_essay_information(content)
        if essay_info:
            self.knowledge_base['english']['essay_types'].update(essay_info)
        
        # Extract writing process steps
        process_steps = self.extract_writing_process(content)
        if process_steps:
            self.knowledge_base['english']['writing_process'].update(process_steps)
        
        # Extract citation information
        citation_info = self.extract_citation_info(content)
        if citation_info:
            self.knowledge_base['english']['citations'].update(citation_info)
    
    def extract_formulas(self, content):
        """Extract mathematical formulas from text."""
        formulas = []
        
        # Various formula patterns
        patterns = [
            r'\*\*([^*]+\s*=\s*[^*]+)\*\*',  # Bold formulas
            r'^([A-Z]\w*\s*=\s*.+)$',  # Simple equations
            r'([A-Z]+\([^)]+\)\s*=\s*.+)',  # Function definitions
            r'(E\(X\)\s*=\s*.+)',  # Expected value
            r'(z\s*=\s*.+)',  # Z-scores
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content, re.MULTILINE)
            formulas.extend([m.strip() for m in matches if len(m.strip()) > 3])
        
        return list(set(formulas))
    
    def extract_math_concepts(self, content):
        """Extract key mathematical concepts."""
        concepts = []
        
        # Look for definitions and key concepts
        concept_patterns = [
            r'^\*\*([^*]+)\*\*\s*[—-]\s*(.+)$',  # Bold term — definition
            r'^([A-Z][^:]+):\s*(.+)$',  # Term: definition
            r'### ([^\\n]+)',  # Section headers
            r'## ([^\\n]+)',   # Chapter headers
        ]
        
        for pattern in concept_patterns:
            matches = re.findall(pattern, content, re.MULTILINE)
            for match in matches:
                if isinstance(match, tuple):
                    concepts.append(f"{match[0]}: {match[1]}")
                else:
                    concepts.append(match)
        
        return concepts
    
    def extract_procedures(self, content):
        """Extract step-by-step procedures."""
        procedures = []
        
        # Look for numbered steps
        step_pattern = r'((?:Step\s*\d+|^\d+\.).*?)(?=(?:Step\s*\d+|^\d+\.|$))'
        matches = re.findall(step_pattern, content, re.MULTILINE | re.DOTALL)
        
        if len(matches) >= 2:  # Only if we have multiple steps
            procedures.append(" → ".join([m.strip() for m in matches]))
        
        return procedures
    
    def extract_essay_information(self, content):
        """Extract essay requirements and information."""
        essay_info = {}
        
        # Look for essay requirements
        if 'compare' in content.lower() and 'contrast' in content.lower():
            essay_info['compare_contrast'] = self.extract_essay_details(content, 'compare/contrast')
        
        if 'argumentative' in content.lower() or 'argument' in content.lower():
            essay_info['argumentative'] = self.extract_essay_details(content, 'argumentative')
        
        return essay_info
    
    def extract_essay_details(self, content, essay_type):
        """Extract specific details for an essay type."""
        details = {'type': essay_type, 'content': content[:500]}  # First 500 chars
        return details
    
    def extract_writing_process(self, content):
        """Extract writing process information."""
        process = {}
        
        if 'revision' in content.lower() or 'editing' in content.lower():
            process['revision_editing'] = content[:300]
        
        if 'brainstorm' in content.lower():
            process['brainstorming'] = content[:300]
        
        return process
    
    def extract_citation_info(self, content):
        """Extract citation and plagiarism information."""
        citation = {}
        
        if 'mla' in content.lower() or 'citation' in content.lower():
            citation['mla_format'] = content[:400]
        
        if 'plagiarism' in content.lower():
            citation['plagiarism_prevention'] = content[:400]
        
        return citation
    
    def identify_chapter_from_path(self, file_path):
        """Identify chapter number or topic from file path."""
        # Extract chapter numbers
        chapter_match = re.search(r'chapter[\s_-]*(\d+)', file_path.lower())
        if chapter_match:
            return f"chapter_{chapter_match.group(1)}"
        
        # Extract unit numbers
        unit_match = re.search(r'unit[\s_-]*(\d+)', file_path.lower())
        if unit_match:
            return f"unit_{unit_match.group(1)}"
        
        # Extract by topic
        if 'probability' in file_path.lower():
            return 'chapter_10'
        elif 'statistics' in file_path.lower():
            return 'chapter_11'
        elif 'personal_finance' in file_path.lower() or 'finance' in file_path.lower():
            return 'chapter_6'
        elif 'voting' in file_path.lower() or 'apportionment' in file_path.lower():
            return 'chapter_13'
        
        return 'general'
    
    def save_knowledge_base(self, output_file="ai_knowledge_base.json"):
        """Save the extracted knowledge base."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge_base, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Knowledge base saved to {output_file}")
        return output_file

def create_ai_tutor_prompts(knowledge_base):
    """Create specialized AI tutor prompts based on the knowledge base."""
    
    # Math tutor prompt
    math_prompt = f"""You are an expert MAT 143 tutor with comprehensive knowledge of all course materials. 

COURSE KNOWLEDGE BASE:
{json.dumps(knowledge_base['math'], indent=2)}

Your role:
- Help students understand mathematical concepts from MAT 143
- Provide step-by-step solutions using the exact formulas and procedures from the course
- Use ADHD-friendly explanations with clear, simple language
- Give practical examples and real-world applications
- Always reference the specific formulas and concepts from the knowledge base above

When answering:
1. Identify which chapter/topic the question relates to
2. Use the exact formulas and procedures from the knowledge base
3. Break down solutions into clear steps
4. Provide memory tricks and study tips when helpful
5. Encourage the student and acknowledge their efforts

Be encouraging, patient, and thorough in your explanations."""
    
    # English tutor prompt
    english_prompt = f"""You are an expert ENG 111 writing coach with comprehensive knowledge of all course materials.

COURSE KNOWLEDGE BASE:
{json.dumps(knowledge_base['english'], indent=2)}

Your role:
- Help students with all aspects of academic writing
- Guide students through the complete writing process
- Provide feedback on essays and writing assignments
- Help with MLA citations and avoiding plagiarism
- Support students with ADHD in organizing their writing

When helping:
1. Identify which type of writing or assignment they need help with
2. Use the writing process steps from the knowledge base
3. Provide specific, actionable feedback
4. Help break down complex tasks into manageable steps
5. Offer encouragement and positive reinforcement

Be supportive, constructive, and specific in your guidance."""
    
    return math_prompt, english_prompt

def main():
    """Main function to extract knowledge and create AI training materials."""
    print("🚀 Starting AI Training System for Course Materials")
    print("=" * 60)
    
    # Extract all knowledge
    extractor = CourseKnowledgeExtractor()
    knowledge_base = extractor.extract_all_course_materials()
    
    # Save knowledge base
    knowledge_file = extractor.save_knowledge_base()
    
    # Create AI prompts
    math_prompt, english_prompt = create_ai_tutor_prompts(knowledge_base)
    
    # Save prompts
    with open("ai_math_tutor_prompt.txt", "w") as f:
        f.write(math_prompt)
    
    with open("ai_english_tutor_prompt.txt", "w") as f:
        f.write(english_prompt)
    
    # Statistics
    total_formulas = sum(len(formulas) for formulas in knowledge_base['math']['formulas'].values())
    total_concepts = sum(len(concepts) for concepts in knowledge_base['math']['concepts'].values())
    total_sources = len(knowledge_base['metadata']['sources'])
    
    print(f"📊 Extraction Complete!")
    print(f"   • {total_sources} source files processed")
    print(f"   • {total_formulas} mathematical formulas extracted")
    print(f"   • {total_concepts} concepts identified")
    print(f"   • {len(knowledge_base['english']['essay_types'])} essay types documented")
    print(f"📄 AI tutor prompts saved to:")
    print(f"   • ai_math_tutor_prompt.txt")
    print(f"   • ai_english_tutor_prompt.txt")
    print(f"💾 Full knowledge base saved to: {knowledge_file}")
    
    return knowledge_base, math_prompt, english_prompt

if __name__ == "__main__":
    main()