# 🎓 MAT 143 AI Tutor System - Modern Minimal Design

A comprehensive AI-powered tutoring system designed to help Kristina succeed in MAT 143 - Quantitative Literacy at CPCC. Features a modern minimal design with M sans font and black/white emphasis.

## 🌐 **Live Production Site**
**https://kristina-math-tudor-mg41ka3f9-beths-projects-87b71e8b.vercel.app**

## 🎯 **What's Included**

### ✅ **Complete Chapter Coverage**
All 8 course chapters with detailed section breakdowns:
- **Chapter 1**: Thinking Mathematically (3 sections)
- **Chapter 4**: Proportions & Percentages (4 sections)  
- **Chapter 5**: Linear & Exponential Functions (3 sections)
- **Chapter 6**: Personal Finance (5 sections)
- **Chapter 7**: Measurement & Conversions (2 sections)
- **Chapter 10**: Probability (3 sections)
- **Chapter 11**: Statistics (4 sections)
- **Chapter 13**: Voting & Apportionment (3 sections)

### 🎨 **Modern Minimal Design System**
- **M Sans Font**: Rubik font family for clean, modern typography
- **Black & White Emphasis**: Primary color palette with #30302f and #f2f2f2
- **Accent Colors**: Soft pastels (#c3dde9, #e4e67b, #e5ccd0, #eb7754)
- **Clean Layout**: Minimal borders, ample whitespace, modern aesthetics

### 📅 **Interactive Calendar System** 
- **Week-by-week schedule** with all 16 weeks mapped out
- **Real assignment due dates** from the pacing guide
- **Current week highlighting** and progress tracking
- **Test countdown timers** for all 4 tests
- **Important deadline alerts** (EVA, withdrawal date, etc.)

### 🤖 **Three Study Systems**

## 🚀 **Quick Start Options**

### **Option 1: Web-Based System** (⭐ RECOMMENDED)
```bash
# Open the main site
open https://kristina-math-tudor-mg41ka3f9-beths-projects-87b71e8b.vercel.app

# Or open locally
open index.html
```

**Features:**
- Modern minimal design interface
- AI tutor with production API
- Reference guide with formulas
- Interactive calendar system
- Study helper tools

### **Option 2: Calendar Study System**
```bash
open calendar_study_system.html
```
**Perfect for:**
- Seeing exactly what's due when
- Tracking semester progress  
- Test preparation timelines
- Daily/weekly study planning

### **Option 3: Enhanced AI Tutor** (Local)
```bash
cd /Users/bethcartrette/REPOS/kristina_math_tutor
source venv/bin/activate
python tutor_system/enhanced_tutor.py
```
**Perfect for:**
- Interactive Q&A with calendar integration
- Personalized homework help
- Step-by-step explanations
- Concept clarification

## 🛠️ **Setup Instructions**

### 1. **Environment Setup**
```bash
cd /Users/bethcartrette/REPOS/kristina_math_tutor

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. **API Key Setup** (Optional - for local AI features)
Get an Anthropic API key from [https://console.anthropic.com/](https://console.anthropic.com/)

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

### 3. **Organize Course Materials**
```bash
python organize_files.py
```
This automatically moves MAT 143 files from Downloads into organized folders.

### 4. **Production Deployment** (Already Done!)
The system is deployed on Vercel with:
- ✅ Global CDN for fast loading
- ✅ Automatic HTTPS security
- ✅ AI API endpoint for tutoring
- ✅ Modern minimal design
- ✅ Mobile-responsive interface

## 📋 **Complete File Structure**

```
kristina_math_tutor/
├── 🌐 index.html                    # Main landing page (modern minimal)
├── 🤖 tutor.html                    # AI tutor interface
├── 📚 reference.html                # Formula reference guide
├── 📅 calendar_study_system.html    # Interactive calendar
├── 🛠️ web_study_helper.html         # Study helper
├── 📅 calendar.html                 # Calendar page
├── 🎨 tokens.json                   # Design system tokens
├── ⚙️ vercel.json                   # Production configuration
├── 📦 package.json                  # Node.js dependencies
├── ⚡ vite.config.js                # Build configuration
├── 🤖 tutor_system/
│   ├── enhanced_tutor.py            # Calendar-integrated AI tutor
│   └── mat143_tutor.py              # Original AI tutor
├── 🔌 api/
│   └── tutor.py                     # Production API endpoint
├── 📚 course_materials/
│   ├── formula_sheets/
│   │   ├── All_Sections_Guide.md    # Complete section guide
│   │   ├── Unit_1_Formula_Sheet.md  # Voting & apportionment
│   │   ├── Chapter_6_Formula_Sheet.md # Personal finance
│   │   ├── Chapter_7_Formula_Sheet.md # Conversions
│   │   └── Unit_4_Formula_Sheet.md  # Statistics
│   ├── sample_assignments/
│   ├── syllabus_and_schedule/
│   ├── instructions/
│   └── resources/
├── 📋 requirements.txt              # Python dependencies
├── 🛠️ setup.sh                      # Automated setup script
├── 🧪 test_system.py                # System verification
├── 📖 README.md                     # This guide
├── 📋 PRODUCTION_CHECKLIST.md       # Deployment guide
└── .gitignore                       # Version control exclusions
```

## 🎨 **Design System**

### **Color Palette**
- **Primary**: Black (#30302f) to White (#f2f2f2) gradient
- **Accent Blue**: #c3dde9 (soft, calming)
- **Accent Yellow**: #e4e67b (warm, encouraging)
- **Accent Pink**: #e5ccd0 (gentle, supportive)
- **Accent Orange**: #eb7754 (energetic, motivating)

### **Typography**
- **Primary Font**: Rubik (M sans font family)
- **Weights**: 400 (normal), 500 (medium), 600 (semibold), 700 (bold), 800 (extrabold), 900 (black)
- **Uppercase Headings**: Modern, clean aesthetic
- **Letter Spacing**: 0.05em for enhanced readability

### **Layout Principles**
- **Minimal Borders**: 1px solid with subtle colors
- **Ample Whitespace**: Generous padding and margins
- **Clean Buttons**: Uppercase text with border transitions
- **Consistent Spacing**: 4pt grid system (16px increments)

## 📅 **Calendar Features**

### **Week-by-Week Breakdown**
- **16 weeks** fully mapped with real dates
- **Every assignment** with actual due dates from pacing guide
- **Current week highlighting** shows exactly where you are
- **Test weeks** specially marked with countdown timers

### **Test Schedule**
- **Test 1**: Sept 8-12 (Chapters 1 & 13)
- **Test 2**: Sept 29-Oct 3 (Chapters 4 & 5)  
- **Test 3**: Nov 3-7 (Chapters 6 & 7)
- **Test 4**: Dec 8-12 (Chapters 10 & 11)

### **Important Deadlines**
- **EVA Deadline**: August 29, 2025
- **Withdrawal Date**: September 26, 2025
- **Signature Assignment**: November 21, 2025
- **Final Exam**: December 15-19, 2025

## 🎯 **Usage Examples**

### **Getting Chapter Help**
```
💭 What can I help you with? chapter 6

📖 [Detailed explanation of personal finance concepts, formulas, and examples]
```

### **Homework Help**
```
💭 What can I help you with? homework
Which assignment are you working on? Section 6.2 Saving and Investing
Any specific question or topic? compound interest calculation

📝 [Step-by-step guidance for compound interest problems]
```

### **Test Preparation**
```
💭 What can I help you with? test 3

📊 [Comprehensive study guide for Test 3 covering Chapters 6 & 7]
```

### **Formula Lookup**
```
💭 What can I help you with? formula interest

📐 Formulas for interest:
  • Simple Interest: I = Prt
  • Compound Interest: A = P(1 + r/n)^(nt)
  • Continuous Compound: A = Pe^(rt)
  • APY: APY = ((1 + r/n)^n - 1) × 100%
```

## 💡 **Pro Tips for Success**

### **Hawkes Learning Mastery**
- Don't rush - work until you see "Congratulations! You've Mastered this lesson"
- Use hints when stuck, but focus on understanding why
- Complete assignments throughout the week, not just Sunday

### **Test Strategy** 
- Use Respondus Lockdown Browser - test setup early
- Review formula sheets the night before (don't cram)
- Read each problem carefully and show all work
- Check that final answers make sense and have correct units

### **Time Management**
- Use the calendar system to plan ahead
- Don't procrastinate on major assignments
- Start Signature Assignment early (it's worth 5% of grade)
- Remember: Last day to withdraw is September 26, 2025

### **Getting Help**
- Use AI tutor for step-by-step problem explanations
- Ask specific questions rather than general "help with math"
- Email instructor early if you're struggling
- Form study groups with classmates

## 🔧 **Development & Deployment**

### **Local Development**
```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

### **Production Deployment**
```bash
# Deploy to Vercel
vercel --prod

# Check deployment status
vercel ls
```

### **System Testing**
```bash
# Run comprehensive system test
python test_system.py
```

## 🆘 **Troubleshooting**

### **API Key Issues**
If you get API key errors:
1. Make sure you've set the ANTHROPIC_API_KEY environment variable
2. Restart your terminal after setting the variable
3. Verify the key is correct at [https://console.anthropic.com/](https://console.anthropic.com/)

### **File Organization Issues**
If files aren't organizing properly:
1. Check that files are actually in your Downloads folder
2. Make sure filenames contain "MAT143" or related terms
3. Run the script with: `python organize_files.py`

### **Installation Issues**
If you have trouble installing dependencies:
1. Make sure you have Python 3.7+ installed
2. Use the virtual environment: `source venv/bin/activate`
3. Try using `pip` instead of `pip3`

### **Production Issues**
If the live site has problems:
1. Check Vercel dashboard for deployment status
2. Verify environment variables are set correctly
3. Check API endpoint logs for errors

## 🌟 **Success Mindset**

**Remember:**
- You've successfully organized all the tools needed for success
- Every expert was once a beginner  
- Progress over perfection - celebrate small wins
- This system adapts to your learning style and pace
- You have support built in for when things get challenging

**The goal isn't just to pass MAT 143 - it's to build confidence and skills that will serve you in life and future courses.**

## 📊 **Success Metrics & Goals**

### **Short-term (Weekly)**
- ✅ Complete all BrightSpace attendance assignments
- ✅ Achieve "mastery" status in Hawkes Learning
- ✅ Submit lab assignments on time

### **Medium-term (Test Prep)**
- ✅ Start test preparation 1 week before each test
- ✅ Score 70% or higher on all tests (C or better)
- ✅ Complete Signature Assignment by November 21

### **Long-term (Semester)**
- ✅ Pass MAT 143 with overall grade of C (70%) or better
- ✅ Build confidence in mathematical reasoning
- ✅ Develop quantitative literacy skills for life

## 🎉 **You're All Set!**

This system contains:
- ✅ Complete chapter and section coverage
- ✅ Interactive calendar with real dates  
- ✅ AI tutoring capabilities
- ✅ Formula sheets and study guides
- ✅ Test preparation timelines
- ✅ Assignment tracking
- ✅ Progress monitoring
- ✅ Modern minimal design system
- ✅ Production deployment on Vercel

**Everything Kristina needs to succeed in MAT 143 is now organized and ready to use! 🌟**

Start with the web-based system to get oriented, then use the other tools as needed. Success in MAT 143 is absolutely achievable with consistent effort and the right support system.

**You've got this, Kristina! 💪**

---

## 📝 **Version History**

- **v2.0.0**: Modern minimal design system with M sans font
- **v1.5.0**: Production deployment on Vercel with API integration
- **v1.0.0**: Complete tutoring system with calendar integration
