# MAT 143 AI Tutor for Kristina 🎓

An AI-powered tutoring system specifically designed to help Kristina succeed in MAT 143 - Quantitative Literacy at CPCC.

## Quick Setup

### 1. Install Dependencies
```bash
cd /Users/bethcartrette/REPOS/kristina_math_tutor
pip3 install -r requirements.txt
```

### 2. Set Up API Key
Get an Anthropic API key from [https://console.anthropic.com/](https://console.anthropic.com/)

Then add it to your environment:
```bash
echo 'export ANTHROPIC_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

### 3. Organize Course Materials
```bash
python3 organize_files.py
```
This will automatically move MAT 143 files from Downloads into organized folders.

### 4. Run the Tutor
```bash
python3 tutor_system/mat143_tutor.py
```

## Features

### 📖 Chapter Help
- Get explanations for any chapter (1, 4, 5, 6, 7, 10, 11, 13)
- Key concepts and formulas
- Common mistakes to avoid
- Study strategies

### 📝 Homework Assistance
- Step-by-step problem solving
- Guided explanations (doesn't just give answers)
- Tips for similar problems
- Encouragement and confidence building

### 📊 Test Preparation
- **Test 1**: Chapter 1 & 13 (Thinking Mathematically, Voting Methods)
- **Test 2**: Chapter 4 & 5 (Proportions, Linear/Exponential Functions)  
- **Test 3**: Chapter 6 & 7 (Personal Finance, Conversions)
- **Test 4**: Chapter 10 & 11 (Probability, Statistics)

### 🧠 Concept Explanations
- Simple, clear explanations of mathematical concepts
- Real-world examples and applications
- Connected to course topics

### 📐 Formula Lookup
- Quick access to all course formulas
- Organized by topic (interest, conversions, statistics, etc.)
- Step-by-step usage guidance

## Course Coverage

### Chapter 1: Thinking Mathematically
- Deductive vs inductive reasoning
- Pattern recognition
- Estimation and problem solving

### Chapter 4: Proportions & Percentages
- Ratios and proportions
- Percentage calculations
- Rate problems and unit conversions

### Chapter 5: Linear & Exponential Functions
- Linear equations and modeling
- Exponential growth and decay
- Graphing and interpreting functions

### Chapter 6: Personal Finance
- Simple and compound interest
- Saving and investing strategies
- Loan calculations and budgeting
- **Key Formulas**:
  - Simple Interest: I = Prt
  - Compound Interest: A = P(1 + r/n)^(nt)
  - Continuous Compound: A = Pe^(rt)

### Chapter 7: Measurement & Conversions
- US Customary and Metric systems
- Dimensional analysis
- Temperature conversions
- **Key Conversions**:
  - 1 inch = 2.54 cm
  - 1 foot ≈ 0.305 m
  - F = 9C/5 + 32

### Chapter 10: Probability
- Basic probability concepts
- Single event probability
- Expected value calculations

### Chapter 11: Statistics
- Statistical studies and data display
- Descriptive statistics
- Normal distribution and z-scores
- **Key Formula**: z = (x - μ)/σ

### Chapter 13: Voting & Apportionment
- Election counting methods (majority, plurality, Borda count)
- Voting method flaws
- Apportionment methods (Hamilton, Jefferson, Webster)

## Usage Examples

### Getting Chapter Help
```
💭 What can I help you with? chapter 6

📖 [Detailed explanation of personal finance concepts, formulas, and examples]
```

### Homework Help
```
💭 What can I help you with? homework
Which assignment are you working on? Section 6.2 Saving and Investing
Any specific question or topic? compound interest calculation

📝 [Step-by-step guidance for compound interest problems]
```

### Test Preparation
```
💭 What can I help you with? test 3

📊 [Comprehensive study guide for Test 3 covering Chapters 6 & 7]
```

### Formula Lookup
```
💭 What can I help you with? formula interest

📐 Formulas for interest:
  • Simple Interest: I = Prt
  • Compound Interest: A = P(1 + r/n)^(nt)
  • Continuous Compound: A = Pe^(rt)
  • APY: APY = ((1 + r/n)^n - 1) × 100%
```

## Important Notes

- **Hawkes Learning**: The actual homework exercises are on the Hawkes Learning platform, not included here
- **Tests**: Use Respondus Lockdown Browser for all tests
- **Deadlines**: Check the pacing guide for all assignment due dates
- **Support**: This tutor provides guidance and explanations, not direct answers

## File Organization

```
kristina_math_tutor/
├── course_materials/
│   ├── formula_sheets/          # All formula sheets
│   ├── syllabus_and_schedule/   # Course syllabus and pacing guide
│   ├── sample_assignments/      # Example homework with solutions
│   ├── instructions/            # Hawkes Learning setup guides
│   └── miscellaneous/          # Other course materials
├── tutor_system/
│   └── mat143_tutor.py         # Main tutoring application
├── requirements.txt            # Python dependencies
├── organize_files.py          # File organization script
└── README.md                  # This guide
```

## Tips for Success

1. **Use the tutor regularly** - Don't wait until you're stuck
2. **Practice consistently** - Work through problems step-by-step
3. **Ask specific questions** - The more specific, the better help you'll get
4. **Review formulas frequently** - Use the formula lookup feature
5. **Prepare for tests early** - Start test prep at least a week before
6. **Don't just memorize** - Focus on understanding concepts

## Troubleshooting

### API Key Issues
If you get API key errors:
1. Make sure you've set the ANTHROPIC_API_KEY environment variable
2. Restart your terminal after setting the variable
3. Verify the key is correct at [https://console.anthropic.com/](https://console.anthropic.com/)

### File Organization Issues
If files aren't organizing properly:
1. Check that files are actually in your Downloads folder
2. Make sure filenames contain "MAT143" or related terms
3. Run the script with: `python3 organize_files.py`

### Installation Issues
If you have trouble installing dependencies:
1. Make sure you have Python 3.7+ installed
2. Try using `pip` instead of `pip3`
3. Consider using a virtual environment

## Support

This tutoring system is designed specifically for Kristina's MAT 143 course at CPCC. It provides patient, encouraging guidance while building mathematical confidence and understanding.

Remember: You've got this! 🌟 Math can be challenging, but with consistent practice and the right support, success is absolutely achievable.
# kristina-math-tudor
