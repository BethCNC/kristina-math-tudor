#!/usr/bin/env python3
"""
ENG 111 Writing Coach API Endpoint
Serverless function for Vercel deployment
"""

import os
import json
import anthropic
from datetime import datetime

def handler(request, context):
    """Vercel serverless function handler."""
    
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }
    
    if request.method == 'POST':
        try:
            # Parse request body
            body = json.loads(request.body)
            query = body.get('query', '')
            assignment_type = body.get('assignment_type', '')
            topic = body.get('topic', '')
            
            # Get API key
            api_key = os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                # Return a helpful fallback response instead of error
                return {
                    'statusCode': 200,
                    'headers': {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    },
                    'body': json.dumps({
                        "error": False,
                        "response": f"""
                        <strong>I'd love to help you with: "{query}"</strong><br><br>
                        
                        <em>💡 Since I'm not fully connected right now, here are some great resources:</em><br><br>
                        
                        <strong>📚 Quick Help:</strong><br>
                        • <a href="calendar.html" style="color: var(--color-accent-pink-dark);">Class Schedule & Assignments</a><br>
                        • <a href="index.html" style="color: var(--color-accent-pink-dark);">Back to Dashboard</a><br><br>
                        
                        <strong>✍️ Writing Help:</strong><br>
                        • Critical reading and discussion posts<br>
                        • Essay structure and organization<br>
                        • Research and citation guidance<br>
                        • Grammar and editing tips<br><br>
                        
                        <em>💡 Tip: Be specific about what assignment you're working on!</em>
                        """,
                        "timestamp": datetime.now().isoformat(),
                        "assignment_type": assignment_type,
                        "topic": topic
                    })
                }
            
            # Generate response
            response = generate_writing_coach_response(query, assignment_type, topic, api_key)
            
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps(response)
            }
            
        except Exception as e:
            # Return a helpful fallback response instead of error
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    "error": False,
                    "response": f"""
                    <strong>I'd love to help you with: "{query}"</strong><br><br>
                    
                    <em>💡 Since I'm having a technical moment, here are some writing tips:</em><br><br>
                    
                    <strong>📚 General Writing Help:</strong><br>
                    • Start with an outline to organize your thoughts<br>
                    • Write a clear thesis statement<br>
                    • Use topic sentences for each paragraph<br>
                    • Check your grammar and spelling<br><br>
                    
                    <strong>✍️ ENG 111 Focus:</strong><br>
                    • Critical reading and analysis<br>
                    • Academic discussion posts<br>
                    • Research and citation (MLA format)<br>
                    • Revision and editing strategies<br><br>
                    
                    <em>💡 Tip: Break big assignments into smaller steps!</em>
                    """,
                    "timestamp": datetime.now().isoformat(),
                    "assignment_type": assignment_type,
                    "topic": topic
                })
            }
    
    return {
        'statusCode': 405,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            "error": True,
            "message": "Method not allowed"
        })
    }

def generate_writing_coach_response(query, assignment_type, topic, api_key):
    """Generate AI writing coach response."""
    client = anthropic.Anthropic(api_key=api_key)
    
    # Course structure for ENG 111
    assignments = {
        "discussion": "Critical reading discussion posts",
        "essay": "Academic essays and analysis",
        "research": "Research papers with MLA citation",
        "analysis": "Literary or text analysis",
        "reflection": "Personal reflection writing"
    }
    
    # Build context
    context = ""
    if assignment_type and assignment_type in assignments:
        context = f"Kristina is working on: {assignments[assignment_type]}"
    if topic:
        context += f"\nSpecific topic: {topic}"
    
    # Create prompt
    prompt = f"""
You are a patient, encouraging writing coach helping Kristina with ENG 111 - Writing and Inquiry at CPCC.

{context}

Student question: {query}

Course context:
- This is an 8-week online writing course at CPCC
- Kristina has ADHD and benefits from clear, step-by-step guidance
- The course focuses on critical reading, writing, and inquiry
- She needs help with academic writing, discussion posts, and research
- Assignments include critical reading discussions, essays, and a research paper

Please provide:
1. Clear, step-by-step writing guidance
2. Simple, encouraging language appropriate for high school freshman level
3. Specific examples when possible
4. Common writing mistakes to avoid
5. Encouraging words and practical tips

Be patient, clear, and encouraging. Use simple language and provide concrete examples.
Keep responses concise but helpful (max 500 words).
Focus on building confidence and executive function skills.
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
            "assignment_type": assignment_type,
            "topic": topic
        }
        
    except Exception as e:
        return {
            "error": True,
            "message": f"AI service error: {str(e)}",
            "timestamp": datetime.now().isoformat()
        }