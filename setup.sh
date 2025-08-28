#!/bin/bash
# MAT 143 Tutor Setup Script

echo "🎓 Setting up MAT 143 Tutor for Kristina..."
echo "==========================================="

# Check if we're in the right directory
if [ ! -d "course_materials" ]; then
    echo "❌ Please run this script from the kristina_math_tutor directory"
    exit 1
fi

echo ""
echo "1. 📁 Organizing course materials..."
python3 organize_files.py

echo ""
echo "2. 🐍 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo ""
echo "3. 📦 Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "4. 🔑 Setting up API key..."
echo "Please visit https://console.anthropic.com/ to get your API key"
echo "Then run: export ANTHROPIC_API_KEY='your_key_here'"
echo ""

echo "5. 🌐 Opening web-based study helper..."
if command -v open >/dev/null 2>&1; then
    open web_study_helper.html
elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open web_study_helper.html
else
    echo "Please open web_study_helper.html in your browser"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Usage Options:"
echo "1. 🌐 Web Helper: Open web_study_helper.html (no API key needed)"
echo "2. 🤖 AI Tutor: Run 'python3 tutor_system/mat143_tutor.py' (requires API key)"
echo ""
echo "The web helper provides formulas, study guides, and tips."
echo "The AI tutor provides interactive help and personalized assistance."
echo ""
echo "Good luck with your studies, Kristina! You've got this! 🌟"
