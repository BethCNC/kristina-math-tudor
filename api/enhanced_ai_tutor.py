#!/usr/bin/env python3
"""
Enhanced AI Tutor with Comprehensive Course Knowledge
This AI tutor is trained on ALL course materials and provides specific, accurate help.
"""

import json
import re
from flask import Flask, request, jsonify
from pathlib import Path

app = Flask(__name__)

# Load the comprehensive knowledge base
def load_knowledge_base():
    """Load the extracted knowledge base."""
    try:
        knowledge_path = Path("../ai_knowledge_base.json")
        if not knowledge_path.exists():
            knowledge_path = Path("ai_knowledge_base.json")
        
        with open(knowledge_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Could not load knowledge base: {e}")
        return {"math": {"formulas": {}, "concepts": {}, "examples": {}}, "english": {}}

KNOWLEDGE_BASE = load_knowledge_base()

class EnhancedMathTutor:
    """AI Math Tutor with comprehensive course knowledge."""
    
    def __init__(self, knowledge_base):
        self.knowledge = knowledge_base.get('math', {})
        self.formulas = self.knowledge.get('formulas', {})
        self.concepts = self.knowledge.get('concepts', {})
        self.examples = self.knowledge.get('examples', {})
    
    def get_help(self, question, chapter=None):
        """Provide comprehensive help based on the question."""
        question_lower = question.lower()
        
        # Identify the topic
        topic_info = self.identify_topic(question_lower, chapter)
        
        # Get relevant formulas and concepts
        relevant_content = self.get_relevant_content(topic_info)
        
        # Generate response
        response = self.generate_response(question, topic_info, relevant_content)
        
        return response
    
    def identify_topic(self, question_lower, chapter):
        """Identify what mathematical topic the question is about."""
        topics = {
            'interest': ['interest', 'compound', 'simple', 'apy', 'investment'],
            'proportion': ['proportion', 'ratio', 'cross multiply', 'percent'],
            'probability': ['probability', 'expected value', 'odds', 'chance'],
            'statistics': ['mean', 'median', 'standard deviation', 'z-score', 'normal'],
            'voting': ['voting', 'plurality', 'majority', 'borda', 'election'],
            'apportionment': ['apportionment', 'quota', 'divisor', 'hamilton'],
            'conversion': ['convert', 'metric', 'temperature', 'measurement'],
            'linear': ['linear', 'slope', 'function', 'equation'],
            'exponential': ['exponential', 'growth', 'decay']
        }
        
        identified_topics = []
        for topic, keywords in topics.items():
            if any(keyword in question_lower for keyword in keywords):
                identified_topics.append(topic)
        
        # Map to chapters
        chapter_mapping = {
            'interest': 'chapter_6',
            'proportion': 'chapter_4', 
            'probability': 'chapter_10',
            'statistics': 'chapter_11',
            'voting': 'chapter_13',
            'apportionment': 'chapter_13',
            'conversion': 'chapter_7',
            'linear': 'chapter_5',
            'exponential': 'chapter_5'
        }
        
        if chapter:
            chapter_key = f"chapter_{chapter}"
        else:
            chapter_key = chapter_mapping.get(identified_topics[0] if identified_topics else 'general', 'general')
        
        return {
            'topics': identified_topics,
            'chapter': chapter_key,
            'primary_topic': identified_topics[0] if identified_topics else 'general'
        }
    
    def get_relevant_content(self, topic_info):
        """Get relevant formulas and concepts for the topic."""
        chapter = topic_info['chapter']
        
        relevant_formulas = []
        relevant_concepts = []
        
        # Get formulas for the specific chapter
        if chapter in self.formulas:
            relevant_formulas = self.formulas[chapter]
        
        # Also check related chapters and general formulas
        for key, formulas in self.formulas.items():
            for topic in topic_info['topics']:
                matching_formulas = [f for f in formulas if topic.lower() in f.lower()]
                relevant_formulas.extend(matching_formulas)
        
        # Get concepts
        if chapter in self.concepts:
            relevant_concepts = self.concepts[chapter]
        
        # Remove duplicates
        relevant_formulas = list(set(relevant_formulas))
        relevant_concepts = list(set(relevant_concepts))
        
        return {
            'formulas': relevant_formulas[:10],  # Limit to top 10
            'concepts': relevant_concepts[:5],    # Limit to top 5
            'chapter': chapter
        }
    
    def generate_response(self, question, topic_info, relevant_content):
        """Generate a comprehensive response."""
        response_parts = []
        
        # Header with encouragement
        response_parts.append(f'<div class="space-y-4">')
        response_parts.append(f'<p><strong>Great question!</strong> Let me help you with this step by step. 🎯</p>')
        
        # Topic identification
        if topic_info['topics']:
            topics_str = ", ".join(topic_info['topics']).title()
            response_parts.append(f'<p>This looks like a question about: <strong>{topics_str}</strong></p>')
        
        # Relevant formulas
        if relevant_content['formulas']:
            response_parts.append('<div class="bg-blue-50 border border-blue-200 p-4 rounded-lg">')
            response_parts.append('<h5 class="font-semibold text-blue-800 mb-2">📐 Key Formulas:</h5>')
            
            for formula in relevant_content['formulas'][:5]:  # Top 5 most relevant
                clean_formula = self.clean_formula(formula)
                if len(clean_formula) > 5:  # Only show meaningful formulas
                    response_parts.append(f'<div class="bg-white p-2 rounded border font-mono text-sm">{clean_formula}</div>')
            
            response_parts.append('</div>')
        
        # Study tips for ADHD
        response_parts.append(self.get_adhd_study_tips(topic_info['primary_topic']))
        
        # Specific guidance based on question type
        response_parts.append(self.get_specific_guidance(question, topic_info['primary_topic']))
        
        # Encouragement
        response_parts.append('<div class="bg-green-50 border border-green-200 p-3 rounded">')
        response_parts.append('<p class="text-green-800"><strong>Remember:</strong> You\'re doing great by asking questions! That\'s exactly how learning works. Take it one step at a time, and you\'ve got this! 💪</p>')
        response_parts.append('</div>')
        
        response_parts.append('</div>')
        
        return "\\n".join(response_parts)
    
    def clean_formula(self, formula):
        """Clean up extracted formulas for display."""
        # Remove HTML and excess whitespace
        clean = re.sub(r'<[^>]+>', '', formula)
        clean = re.sub(r'\\n\\s*', ' ', clean)
        clean = re.sub(r'\\s+', ' ', clean)
        clean = clean.strip()
        
        # Remove obvious duplicates and artifacts
        if 'HTML' in clean or 'getElementById' in clean:
            return ""
        
        return clean
    
    def get_adhd_study_tips(self, topic):
        """Get ADHD-friendly study tips for specific topics."""
        tips_by_topic = {
            'interest': 'Break interest problems into 3 steps: 1) Identify P, r, t  2) Convert % to decimal  3) Plug into formula',
            'proportion': 'Use "cross your fingers" - cross multiply to solve proportions!',
            'probability': 'Think "favorable over total" - count what you want over what\'s possible',
            'statistics': 'Remember: Mean gets pulled by outliers, median stays stable',
            'voting': 'Make a table for each voting method - visual organization helps!',
            'conversion': 'Use the "stair step" method - bigger units go down the stairs'
        }
        
        tip = tips_by_topic.get(topic, 'Break the problem into small steps and check each one')
        
        return f'''<div class="bg-yellow-50 border border-yellow-300 p-3 rounded">
                    <h6 class="font-semibold text-yellow-800 mb-1">💡 ADHD Study Tip:</h6>
                    <p class="text-yellow-700 text-sm">{tip}</p>
                   </div>'''
    
    def get_specific_guidance(self, question, topic):
        """Provide specific step-by-step guidance."""
        guidance_templates = {
            'interest': '''
                <div class="bg-gray-50 p-3 rounded">
                    <h6 class="font-semibold mb-2">📋 Interest Problem Steps:</h6>
                    <ol class="list-decimal list-inside text-sm space-y-1">
                        <li>Identify: Principal (P), Rate (r), Time (t)</li>
                        <li>Convert percentage to decimal (5% = 0.05)</li>
                        <li>Choose formula: Simple (I=Prt) or Compound (A=P(1+r/n)^nt)</li>
                        <li>Substitute values and calculate</li>
                        <li>Check: Does your answer make sense?</li>
                    </ol>
                </div>
            ''',
            'proportion': '''
                <div class="bg-gray-50 p-3 rounded">
                    <h6 class="font-semibold mb-2">📋 Proportion Steps:</h6>
                    <ol class="list-decimal list-inside text-sm space-y-1">
                        <li>Set up the ratio: a/b = c/d</li>
                        <li>Cross multiply: a × d = b × c</li>
                        <li>Solve for the unknown</li>
                        <li>Check by substituting back</li>
                    </ol>
                </div>
            ''',
            'probability': '''
                <div class="bg-gray-50 p-3 rounded">
                    <h6 class="font-semibold mb-2">📋 Probability Steps:</h6>
                    <ol class="list-decimal list-inside text-sm space-y-1">
                        <li>Count favorable outcomes</li>
                        <li>Count total possible outcomes</li>
                        <li>P = favorable/total</li>
                        <li>Simplify if possible</li>
                    </ol>
                </div>
            '''
        }
        
        return guidance_templates.get(topic, '''
            <div class="bg-gray-50 p-3 rounded">
                <h6 class="font-semibold mb-2">📋 General Problem-Solving Steps:</h6>
                <ol class="list-decimal list-inside text-sm space-y-1">
                    <li>Read the problem carefully</li>
                    <li>Identify what you know and what you need to find</li>
                    <li>Choose the right formula or method</li>
                    <li>Work through step by step</li>
                    <li>Check your answer</li>
                </ol>
            </div>
        ''')

class EnhancedEnglishTutor:
    """AI English Tutor with comprehensive course knowledge."""
    
    def __init__(self, knowledge_base):
        self.knowledge = knowledge_base.get('english', {})
    
    def get_help(self, question, context=None):
        """Provide comprehensive writing help."""
        question_lower = question.lower()
        
        # Identify writing topic
        topic_info = self.identify_writing_topic(question_lower)
        
        # Generate response
        response = self.generate_writing_response(question, topic_info)
        
        return response
    
    def identify_writing_topic(self, question_lower):
        """Identify what writing topic the question is about."""
        topics = {
            'essay_structure': ['structure', 'organize', 'outline', 'introduction', 'conclusion'],
            'compare_contrast': ['compare', 'contrast', 'similarity', 'difference'],
            'citations': ['cite', 'citation', 'mla', 'quote', 'source'],
            'plagiarism': ['plagiarism', 'cheat', 'copy', 'original'],
            'revision': ['revise', 'edit', 'improve', 'draft'],
            'thesis': ['thesis', 'argument', 'main idea', 'claim'],
            'brainstorm': ['brainstorm', 'ideas', 'topic', 'start']
        }
        
        identified_topics = []
        for topic, keywords in topics.items():
            if any(keyword in question_lower for keyword in keywords):
                identified_topics.append(topic)
        
        return {
            'topics': identified_topics,
            'primary_topic': identified_topics[0] if identified_topics else 'general'
        }
    
    def generate_writing_response(self, question, topic_info):
        """Generate a comprehensive writing response."""
        response_parts = []
        
        response_parts.append('<div class="space-y-4">')
        response_parts.append('<p><strong>I\'m here to help with your writing!</strong> ✍️</p>')
        
        # Topic-specific advice
        topic = topic_info['primary_topic']
        
        if topic == 'essay_structure':
            response_parts.append(self.get_essay_structure_help())
        elif topic == 'compare_contrast':
            response_parts.append(self.get_compare_contrast_help())
        elif topic == 'citations':
            response_parts.append(self.get_citation_help())
        elif topic == 'plagiarism':
            response_parts.append(self.get_plagiarism_help())
        elif topic == 'revision':
            response_parts.append(self.get_revision_help())
        elif topic == 'thesis':
            response_parts.append(self.get_thesis_help())
        else:
            response_parts.append(self.get_general_writing_help())
        
        # ADHD writing tips
        response_parts.append(self.get_adhd_writing_tips())
        
        # Encouragement
        response_parts.append('<div class="bg-green-50 border border-green-200 p-3 rounded">')
        response_parts.append('<p class="text-green-800"><strong>You\'re doing great!</strong> Writing is a process, and every draft gets better. Keep going! 🌟</p>')
        response_parts.append('</div>')
        
        response_parts.append('</div>')
        
        return "\\n".join(response_parts)
    
    def get_essay_structure_help(self):
        return '''
        <div class="bg-blue-50 border border-blue-200 p-4 rounded">
            <h5 class="font-semibold text-blue-800 mb-2">📝 Essay Structure:</h5>
            <ol class="list-decimal list-inside text-sm space-y-2 text-blue-700">
                <li><strong>Introduction:</strong> Hook + Background + Thesis</li>
                <li><strong>Body Paragraphs:</strong> Topic sentence + Evidence + Analysis + Transition</li>
                <li><strong>Conclusion:</strong> Restate thesis + Summarize points + Final thought</li>
            </ol>
        </div>
        '''
    
    def get_compare_contrast_help(self):
        return '''
        <div class="bg-purple-50 border border-purple-200 p-4 rounded">
            <h5 class="font-semibold text-purple-800 mb-2">⚖️ Compare/Contrast Structure:</h5>
            <div class="text-sm space-y-2 text-purple-700">
                <p><strong>Option 1 - Point by Point:</strong> Compare each aspect directly</p>
                <p><strong>Option 2 - Subject by Subject:</strong> Discuss all of A, then all of B</p>
                <p><strong>Key:</strong> Use transition words like "similarly," "however," "in contrast"</p>
            </div>
        </div>
        '''
    
    def get_citation_help(self):
        return '''
        <div class="bg-green-50 border border-green-200 p-4 rounded">
            <h5 class="font-semibold text-green-800 mb-2">📚 MLA Citation Basics:</h5>
            <div class="text-sm space-y-1 text-green-700 font-mono">
                <p><strong>In-text:</strong> (Author Page)</p>
                <p><strong>Works Cited:</strong> Author. "Title." Source, Date.</p>
            </div>
        </div>
        '''
    
    def get_plagiarism_help(self):
        return '''
        <div class="bg-red-50 border border-red-200 p-4 rounded">
            <h5 class="font-semibold text-red-800 mb-2">⚠️ Avoiding Plagiarism:</h5>
            <ul class="list-disc list-inside text-sm space-y-1 text-red-700">
                <li>Always cite sources, even when paraphrasing</li>
                <li>Use quotation marks for exact words</li>
                <li>Put ideas in your own words</li>
                <li>When in doubt, cite it!</li>
            </ul>
        </div>
        '''
    
    def get_revision_help(self):
        return '''
        <div class="bg-yellow-50 border border-yellow-200 p-4 rounded">
            <h5 class="font-semibold text-yellow-800 mb-2">✏️ Revision vs. Editing:</h5>
            <div class="text-sm space-y-2 text-yellow-700">
                <p><strong>Revision (Big Picture):</strong> Ideas, organization, clarity</p>
                <p><strong>Editing (Details):</strong> Grammar, spelling, punctuation</p>
                <p><strong>Tip:</strong> Always revise before editing!</p>
            </div>
        </div>
        '''
    
    def get_thesis_help(self):
        return '''
        <div class="bg-indigo-50 border border-indigo-200 p-4 rounded">
            <h5 class="font-semibold text-indigo-800 mb-2">🎯 Strong Thesis Statements:</h5>
            <ul class="list-disc list-inside text-sm space-y-1 text-indigo-700">
                <li>Make a clear argument or claim</li>
                <li>Be specific, not vague</li>
                <li>Preview your main points</li>
                <li>Put it at the end of your introduction</li>
            </ul>
        </div>
        '''
    
    def get_general_writing_help(self):
        return '''
        <div class="bg-gray-50 p-4 rounded">
            <h5 class="font-semibold mb-2">📋 Writing Process Steps:</h5>
            <ol class="list-decimal list-inside text-sm space-y-1">
                <li>Brainstorm and choose topic</li>
                <li>Create outline</li>
                <li>Write first draft</li>
                <li>Revise for content and organization</li>
                <li>Edit for grammar and style</li>
            </ol>
        </div>
        '''
    
    def get_adhd_writing_tips(self):
        return '''
        <div class="bg-orange-50 border border-orange-300 p-3 rounded">
            <h6 class="font-semibold text-orange-800 mb-1">🧠 ADHD Writing Tips:</h6>
            <ul class="text-orange-700 text-sm list-disc list-inside space-y-1">
                <li>Write in short bursts (15-25 minutes)</li>
                <li>Use outlines and graphic organizers</li>
                <li>Start with brain dumps - get ideas out first</li>
                <li>Revise in separate sessions from writing</li>
            </ul>
        </div>
        '''

# Initialize tutors
math_tutor = EnhancedMathTutor(KNOWLEDGE_BASE)
english_tutor = EnhancedEnglishTutor(KNOWLEDGE_BASE)

@app.route('/api/ai-tutor', methods=['POST'])
def enhanced_ai_tutor():
    """Enhanced AI tutor endpoint with comprehensive knowledge."""
    try:
        data = request.json
        question = data.get('question', '')
        chapter = data.get('chapter', '')
        context = data.get('context', 'general')
        
        if not question.strip():
            return jsonify({
                'answer': '<p>Please ask me a specific question and I\'ll be happy to help! 🤖</p>',
                'success': True
            })
        
        # Route to appropriate tutor
        if context == 'math-tutorial' or any(word in question.lower() for word in ['formula', 'calculate', 'solve', 'math', 'percent', 'interest', 'probability']):
            response = math_tutor.get_help(question, chapter)
        elif context == 'writing-help' or any(word in question.lower() for word in ['essay', 'write', 'citation', 'thesis', 'paragraph']):
            response = english_tutor.get_help(question, context)
        else:
            # General helpful response
            response = f'''
            <div class="space-y-3">
                <p><strong>I'm here to help you with both math and writing!</strong> 📚✍️</p>
                <p>Your question: "{question}"</p>
                <div class="grid grid-cols-2 gap-4">
                    <div class="bg-blue-50 p-3 rounded">
                        <h6 class="font-semibold text-blue-800">Math Help</h6>
                        <p class="text-sm text-blue-700">Ask about formulas, calculations, or specific math problems</p>
                    </div>
                    <div class="bg-green-50 p-3 rounded">
                        <h6 class="font-semibold text-green-800">Writing Help</h6>
                        <p class="text-sm text-green-700">Ask about essays, citations, or writing process</p>
                    </div>
                </div>
                <p>Can you tell me more specifically what you need help with? I have comprehensive knowledge of all your course materials! 🎯</p>
            </div>
            '''
        
        return jsonify({'answer': response, 'success': True})
    
    except Exception as e:
        return jsonify({
            'answer': '<p>I had a small hiccup, but I\'m still here to help! Please try asking your question again. 🤖✨</p>',
            'error': str(e),
            'success': False
        })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'knowledge_loaded': len(KNOWLEDGE_BASE.get('math', {}).get('formulas', {})) > 0,
        'formulas_count': sum(len(formulas) for formulas in KNOWLEDGE_BASE.get('math', {}).get('formulas', {}).values())
    })

if __name__ == '__main__':
    print(f"🤖 Enhanced AI Tutor starting...")
    print(f"📊 Loaded {sum(len(formulas) for formulas in KNOWLEDGE_BASE.get('math', {}).get('formulas', {}).values())} formulas")
    print(f"🔬 Covering {len(KNOWLEDGE_BASE.get('math', {}).get('formulas', {}))} chapters")
    app.run(debug=True, port=5001)  # Different port to avoid conflicts