#!/usr/bin/env python3
"""
MAT 143 AI Tutor API Endpoint
Serverless function for Vercel deployment
"""

import os
import json
from http.server import BaseHTTPRequestHandler
from datetime import datetime

try:
    import anthropic
except ImportError:
    anthropic = None

class handler(BaseHTTPRequestHandler):
    """Vercel serverless function handler."""
    
    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_POST(self):
        """Handle POST requests."""
        try:
            # Parse request body
            content_length = int(self.headers.get('Content-Length', 0))
            body_data = self.rfile.read(content_length)
            body = json.loads(body_data.decode('utf-8'))
            
            query = body.get('query', '')
            chapter = body.get('chapter', '')
            topic = body.get('topic', '')
            
            # Get API key
            api_key = os.getenv('ANTHROPIC_API_KEY')
            if not api_key or not anthropic:
                # Return a helpful fallback response instead of error
                chapter_info = ""
                if chapter:
                    chapter_topics = {
                        "1": "problem solving, patterns, deductive & inductive reasoning",
                        "4": "proportions, cross-multiplication, percentages, unit rates",
                        "5": "linear functions (y=mx+b), exponential functions (y=ab^x)",
                        "6": "simple interest (I=Prt), compound interest, APY, loans, present value",
                        "7": "metric conversions, temperature formulas, dimensional analysis",
                        "10": "probability calculations, expected value E(X), odds, independent events",
                        "11": "mean, median, mode, standard deviation, z-scores, normal distribution",
                        "13": "voting methods (plurality, Borda, IRV), apportionment (standard divisor & quota)"
                    }
                    topic_hint = chapter_topics.get(chapter, "")
                    if topic_hint:
                        chapter_info = f"<br><br><strong>Chapter {chapter} covers:</strong> {topic_hint}"
                
                response_data = {
                    "error": False,
                    "response": f"""
                    <strong>Question: "{query}"</strong>{chapter_info}<br><br>
                    
                    <div style="background-color: #fff6d8; border-left: 4px solid #fed23b; padding: 12px; border-radius: 4px;">
                    <strong>💡 AI Tutor Setup Needed</strong><br>
                    The AI tutor endpoint needs an ANTHROPIC_API_KEY environment variable to be configured.
                    </div><br>
                    
                    <strong>📚 In the meantime, try these resources:</strong><br>
                    • <a href="formula_lookup.html" style="color: #399d3c; font-weight: 500;">Formula Lookup</a> - Quick reference for all formulas<br>
                    • <a href="chapter-{chapter}.html" style="color: #399d3c; font-weight: 500;">Chapter {chapter} Page</a> - Detailed explanations & examples<br>
                    • <a href="https://learn.hawkeslearning.com/" target="_blank" style="color: #399d3c; font-weight: 500;">Hawkes Learning</a> - Interactive practice problems<br><br>
                    
                    <strong>🎯 Study Tips:</strong><br>
                    • Review the chapter page for step-by-step examples<br>
                    • Practice similar problems in Hawkes Learning<br>
                    • Check the formula sheet for quick reference<br>
                    • Reach out to your instructor during office hours
                    """,
                    "timestamp": datetime.now().isoformat(),
                    "chapter": chapter,
                    "topic": topic,
                    "fallback": True
                }
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode('utf-8'))
                return
            
            # Generate response
            response = generate_tutor_response(query, chapter, topic, api_key)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            # Return a helpful fallback response instead of error
            response_data = {
                "error": False,
                "response": f"""
                <strong>Question: "{query}"</strong><br><br>
                
                <div style="background-color: #fec6c0; border-left: 4px solid #fd5441; padding: 12px; border-radius: 4px;">
                <strong>⚠️ Temporary Service Issue</strong><br>
                The AI tutor is experiencing a temporary issue. Don't worry - here are alternative resources!
                </div><br>
                
                <strong>📚 Alternative Resources:</strong><br>
                • <a href="formula_lookup.html" style="color: #399d3c; font-weight: 500;">Formula Lookup</a> - Quick reference for all formulas<br>
                • <a href="tutor.html" style="color: #399d3c; font-weight: 500;">Chapter Pages</a> - Detailed explanations & examples<br>
                • <a href="https://learn.hawkeslearning.com/" target="_blank" style="color: #399d3c; font-weight: 500;">Hawkes Learning</a> - Interactive practice & video tutorials<br><br>
                
                <strong>🎯 Study Strategy:</strong><br>
                1. Review the relevant chapter page for formulas and examples<br>
                2. Try practice problems in Hawkes Learning<br>
                3. Use the formula lookup for quick reference<br>
                4. If still stuck, reach out during office hours
                """,
                "timestamp": datetime.now().isoformat(),
                "chapter": chapter,
                "topic": topic,
                "fallback": True
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
    
    def do_GET(self):
        """Handle GET requests."""
        self.send_response(405)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({
            "error": True,
            "message": "Method not allowed. Use POST to /api/tutor"
        }).encode('utf-8'))

def generate_tutor_response(query, chapter, topic, api_key):
    """Generate AI tutor response."""
    client = anthropic.Anthropic(api_key=api_key)
    
    # Course structure
    chapters = {
        1: "Thinking Mathematically, Estimating, Problem Solving",
        4: "Proportions, Percentages, and Ratios",
        5: "Linear and Exponential Functions",
        6: "Personal Finance (Interest, Saving, Borrowing)",
        7: "Measurement and Conversions",
        10: "Probability and Expected Value",
        11: "Statistics and Data Analysis",
        13: "Voting Methods and Apportionment"
    }
    
    # Build context
    context = ""
    if chapter and chapter in chapters:
        context = f"Kristina is working on Chapter {chapter}: {chapters[chapter]}"
    if topic:
        context += f"\nSpecific topic: {topic}"
    
    # Create prompt
    prompt = f"""
You are a patient, encouraging math tutor helping Kristina with MAT 143 - Quantitative Literacy at CPCC.

{context}

Student question: {query}

Course context:
- This is an online course at CPCC
- Kristina has struggled with math before and needs extra encouragement
- She uses Hawkes Learning for homework assignments
- The course covers practical, real-world applications of math

Please provide:
1. A clear, step-by-step explanation
2. Simple, encouraging language
3. Real-world examples when possible
4. Common mistakes to avoid
5. Encouraging words and study tips

Be patient, clear, and encouraging. Use simple language and provide concrete examples.
Keep responses concise but thorough (max 500 words).
"""
    
    try:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return {
            "error": False,
            "response": response.content[0].text,
            "timestamp": datetime.now().isoformat(),
            "chapter": chapter,
            "topic": topic
        }
        
    except Exception as e:
        return {
            "error": True,
            "message": f"AI service error: {str(e)}",
            "timestamp": datetime.now().isoformat()
        }
