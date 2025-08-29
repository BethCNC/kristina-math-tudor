
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configure OpenAI (you'll need to add your API key)
# openai.api_key = os.getenv('OPENAI_API_KEY')

MATH_TUTOR_PROMPT = """
You are a patient, encouraging math tutor specializing in MAT 143 (Quantitative Literacy).
Your student has ADHD and struggles with executive function, so:

1. Break down complex problems into small steps
2. Use encouraging, non-judgmental language
3. Provide multiple examples
4. Connect concepts to real-world applications
5. Offer memory aids and organizational tips

Current chapter context: {chapter}
Student question: {question}

Provide a clear, step-by-step explanation that builds confidence.
"""

ENGLISH_TUTOR_PROMPT = """
You are a supportive writing coach for ENG 111 (Writing & Inquiry).
Your student has ADHD and needs extra structure and encouragement.

Focus on:
1. Breaking writing tasks into manageable chunks
2. Providing clear organizational strategies
3. Offering specific, actionable feedback
4. Building confidence in their writing abilities
5. Connecting writing to their interests and experiences

Student question: {question}
Writing context: {context}

Provide helpful, encouraging guidance that builds writing confidence.
"""

@app.route('/api/ai-tutor', methods=['POST'])
def ai_tutor():
    try:
        data = request.json
        question = data.get('question', '')
        chapter = data.get('chapter', '')
        context = data.get('context', 'general')
        
        if context == 'math-tutorial':
            prompt = MATH_TUTOR_PROMPT.format(chapter=f"Chapter {chapter}", question=question)
        else:
            prompt = ENGLISH_TUTOR_PROMPT.format(question=question, context=context)
        
        # For now, return a helpful response
        # In production, you'd use OpenAI API here
        response = generate_tutor_response(question, chapter, context)
        
        return jsonify({'answer': response, 'success': True})
    
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

def generate_tutor_response(question, chapter, context):
    """Generate helpful tutor responses (placeholder for AI integration)"""
    
    # Math responses
    if context == 'math-tutorial':
        if 'proportion' in question.lower():
            return """
            <div class="space-y-3">
                <p><strong>Great question about proportions!</strong> Let me break this down step by step:</p>
                <div class="bg-blue-50 p-3 rounded">
                    <h6 class="font-semibold">Step 1: Set up the proportion</h6>
                    <p>A proportion is two equal ratios: a/b = c/d</p>
                </div>
                <div class="bg-blue-50 p-3 rounded">
                    <h6 class="font-semibold">Step 2: Cross multiply</h6>
                    <p>If a/b = c/d, then a × d = b × c</p>
                </div>
                <div class="bg-green-50 p-3 rounded">
                    <h6 class="font-semibold">Memory tip for ADHD:</h6>
                    <p>Think "Cross your fingers for luck" - cross multiply to solve!</p>
                </div>
                <p>Would you like me to work through a specific example with you?</p>
            </div>
            """
    
    # Default encouraging response
    return f"""
    <div class="space-y-3">
        <p><strong>I'm here to help you succeed!</strong> 📚</p>
        <p>That's a great question about {f"Chapter {chapter}" if chapter else "your coursework"}. 
        Let me think through this with you step by step.</p>
        <div class="bg-yellow-50 p-3 rounded">
            <p><strong>Remember:</strong> Every question you ask shows you're actively learning. 
            That's exactly what successful students do!</p>
        </div>
        <p>Can you tell me more specifically what part is confusing you? 
        The more details you give me, the better I can help! 🤖✨</p>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True, port=5000)
