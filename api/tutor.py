#!/usr/bin/env python3
"""
MAT 143 AI Tutor API Endpoint
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
            chapter = body.get('chapter', '')
            topic = body.get('topic', '')
            
            # Get API key
            api_key = os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                return {
                    'statusCode': 400,
                    'headers': {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    },
                    'body': json.dumps({
                        "error": True,
                        "message": "API key not configured"
                    })
                }
            
            # Generate response
            response = generate_tutor_response(query, chapter, topic, api_key)
            
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps(response)
            }
            
        except Exception as e:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    "error": True,
                    "message": f"Error processing request: {str(e)}"
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
