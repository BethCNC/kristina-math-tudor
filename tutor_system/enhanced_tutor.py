#!/usr/bin/env python3
"""
Enhanced MAT 143 AI Tutor System with Calendar Integration
Includes detailed pacing guide and timeline management
"""

import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import anthropic
from pathlib import Path

class MAT143TutorWithCalendar:
    def __init__(self, api_key: str = None):
        """Initialize the MAT 143 Tutor with course knowledge and calendar."""
        if api_key:
            self.client = anthropic.Anthropic(api_key=api_key)
        else:
            self.client = None
        
        self.course_materials = {}
        self.session_history = []
        self.load_course_materials()
        
        # Complete course structure with all sections from pacing guide
        self.chapters = {
            1: {
                "title": "Thinking Mathematically, Estimating, Problem Solving",
                "sections": {
                    "1.1": "Thinking Mathematically",
                    "1.2": "Estimating and Evaluating", 
                    "1.3": "Problem Solving: Processes and Techniques"
                }
            },
            4: {
                "title": "Proportions, Percentages, and Ratios",
                "sections": {
                    "4.1": "Proportions, Percentages, and Ratios",
                    "4.2": "Using Percentages",
                    "4.3": "Rates, Unit Rates, and Rates of Change",
                    "4.4": "Using Rates for Dimensional Analysis"
                }
            },
            5: {
                "title": "Linear and Exponential Functions",
                "sections": {
                    "5.1": "Linear Equations and Functions",
                    "5.2": "Linear Modeling", 
                    "5.7": "Exponential Functions"
                }
            },
            6: {
                "title": "Personal Finance (Interest, Saving, Borrowing)",
                "sections": {
                    "6.1": "Understanding Interest",
                    "6.2": "Saving and Investing",
                    "6.3": "Borrowing Money",
                    "6.4": "Federal Revenue",
                    "6.5": "Budgeting"
                }
            },
            7: {
                "title": "Measurement and Conversions", 
                "sections": {
                    "7.4": "The Metric System - Dimensional Analysis",
                    "7.5": "Converting Between Metric and US Customary Systems"
                }
            },
            10: {
                "title": "Probability and Expected Value",
                "sections": {
                    "10.1": "Introduction to Probability",
                    "10.2": "Counting Outcomes", 
                    "10.3": "Probability of Single Events",
                    "10.4": "Addition and Multiplication Rules of Probability",
                    "10.6": "Expected Value"
                }
            },
            11: {
                "title": "Statistics and Data Analysis",
                "sections": {
                    "11.1": "Statistical Studies",
                    "11.2": "Displaying Data", 
                    "11.3": "Describing and Analyzing Data",
                    "11.4": "Empirical Rule and Z-scores"
                }
            },
            13: {
                "title": "Voting Methods and Apportionment",
                "sections": {
                    "13.1": "How to Determine a Winner",
                    "13.2": "Flaws in Voting Methods",
                    "13.3": "Apportionment"
                }
            }
        }
        
        # Detailed semester schedule based on pacing guide
        self.semester_schedule = self.create_semester_schedule()
        
        # Test schedule with specific dates
        self.test_schedule = {
            "Test 1": {
                "chapters": [1, 13],
                "week": 4,
                "dates": "September 8-12, 2025",
                "topics": ["Mathematical reasoning", "Voting methods", "Apportionment"]
            },
            "Test 2": {
                "chapters": [4, 5], 
                "week": 7,
                "dates": "September 29 - October 3, 2025",
                "topics": ["Proportions", "Percentages", "Linear functions", "Exponential functions"]
            },
            "Test 3": {
                "chapters": [6, 7],
                "week": 11, 
                "dates": "November 3-7, 2025",
                "topics": ["Interest calculations", "Conversions", "Personal finance"]
            },
            "Test 4": {
                "chapters": [10, 11],
                "week": 16,
                "dates": "December 8-12, 2025", 
                "topics": ["Probability", "Statistics", "Z-scores"]
            }
        }

    def create_semester_schedule(self):
        """Create detailed semester schedule with all assignments and due dates."""
        
        # Base date: semester starts August 18, 2025
        semester_start = datetime(2025, 8, 18)
        
        schedule = {}
        
        # Week 1: August 18-22
        schedule["Week 1"] = {
            "dates": "August 18-22, 2025",
            "sections": ["1.1", "1.2"],
            "assignments": {
                "BrightSpace": [
                    {"name": "Syllabus Review", "due": "Friday 8/22 11:59 PM"},
                    {"name": "EVA (Enrollment Verification Activity)", "due": "Friday 8/29 11:59 PM"}, 
                    {"name": "Attendance Week 1", "due": "Friday 8/22 11:59 PM"}
                ],
                "Hawkes": [
                    {"name": "Section 1.1 Thinking Mathematically", "due": "Sunday 8/24 11:59 PM"},
                    {"name": "Section 1.2 Estimating and Evaluating", "due": "Sunday 8/24 11:59 PM"}
                ]
            },
            "focus": "Getting started, mathematical reasoning, estimation"
        }
        
        # Week 2: August 25-29
        schedule["Week 2"] = {
            "dates": "August 25-29, 2025", 
            "sections": ["1.3", "13.1"],
            "assignments": {
                "BrightSpace": [
                    {"name": "Attendance Week 2", "due": "Friday 8/29 11:59 PM"},
                    {"name": "Lab #1 (Chapter 1)", "due": "Friday 8/29 11:59 PM"},
                    {"name": "EVA FINAL DEADLINE", "due": "Friday 8/29 11:59 PM"}
                ],
                "Hawkes": [
                    {"name": "Section 1.3 Problem Solving", "due": "Sunday 8/31 11:59 PM"},
                    {"name": "Section 13.1 How to Determine a Winner", "due": "Sunday 8/31 11:59 PM"}
                ]
            },
            "focus": "Problem solving strategies, voting methods introduction"
        }
        
        # Week 3: September 1-5
        schedule["Week 3"] = {
            "dates": "September 1-5, 2025",
            "sections": ["13.2", "13.3"], 
            "assignments": {
                "BrightSpace": [
                    {"name": "Attendance Week 3", "due": "Friday 9/5 11:59 PM"},
                    {"name": "Lab #2 (Chapter 13)", "due": "Friday 9/5 11:59 PM"}
                ],
                "Hawkes": [
                    {"name": "Section 13.2 Flaws in Voting Methods", "due": "Sunday 9/7 11:59 PM"},
                    {"name": "Section 13.3 Apportionment", "due": "Sunday 9/7 11:59 PM"}
                ]
            },
            "focus": "Voting method flaws, apportionment methods"
        }
        
        # Week 4: September 8-12 (TEST 1)
        schedule["Week 4"] = {
            "dates": "September 8-12, 2025",
            "sections": ["Review", "Test 1"],
            "assignments": {
                "BrightSpace": [
                    {"name": "Attendance Week 4", "due": "Friday 9/12 11:59 PM"},
                    {"name": "TEST 1 (Chapters 1 & 13)", "due": "During week - check email"}
                ],
                "Hawkes": [
                    {"name": "TEST 1 in Hawkes", "due": "During week - check email"}
                ]
            },
            "focus": "Test 1: Mathematical thinking and voting methods"
        }
        
        # Week 5: September 15-19
        schedule["Week 5"] = {
            "dates": "September 15-19, 2025",
            "sections": ["4.1", "4.2", "4.3"],
            "assignments": {
                "BrightSpace": [
                    {"name": "Attendance Week 5", "due": "Friday 9/19 11:59 PM"},
                    {"name": "Lab #3 (Chapter 4)", "due": "Friday 9/19 11:59 PM"}
                ],
                "Hawkes": [
                    {"name": "Section 4.1 Proportions, Percentages, & Ratios", "due": "Sunday 9/21 11:59 PM"},
                    {"name": "Section 4.2 Using Percentages", "due": "Sunday 9/21 11:59 PM"},
                    {"name": "Section 4.3 Rates, Unit Rates, & Rates of Changes", "due": "Sunday 9/21 11:59 PM"}
                ]
            },
            "focus": "Proportions, percentages, rates"
        }
        
        # Week 6: September 22-26  
        schedule["Week 6"] = {
            "dates": "September 22-26, 2025",
            "sections": ["5.1", "5.2", "5.7"],
            "assignments": {
                "BrightSpace": [
                    {"name": "Attendance Week 6", "due": "Friday 9/26 11:59 PM"},
                    {"name": "Lab #4 (Chapter 5)", "due": "Friday 9/26 11:59 PM"}
                ],
                "Hawkes": [
                    {"name": "Section 5.1 Linear Equations & Functions", "due": "Sunday 9/28 11:59 PM"},
                    {"name": "Section 5.2 Linear Modeling", "due": "Sunday 9/28 11:59 PM"}, 
                    {"name": "Section 5.7 Exponential Functions", "due": "Sunday 9/28 11:59 PM"}
                ]
            },
            "focus": "Linear and exponential functions",
            "important": "LAST DAY TO WITHDRAW: Friday 9/26/2025"
        }
        
        # Continue with remaining weeks...
        # Week 7: Test 2, Week 8: Chapter 7, etc.
        
        return schedule

    def get_current_week_info(self):
        """Get information about the current week in the semester."""
        today = datetime.now()
        semester_start = datetime(2025, 8, 18)
        
        if today < semester_start:
            return {
                "status": "not_started",
                "message": f"Semester starts on {semester_start.strftime('%B %d, %Y')}",
                "days_until": (semester_start - today).days
            }
        
        # Calculate which week we're in
        days_since_start = (today - semester_start).days
        week_number = (days_since_start // 7) + 1
        
        if week_number <= 16:
            week_key = f"Week {week_number}"
            if week_key in self.semester_schedule:
                return {
                    "status": "in_progress", 
                    "week": week_number,
                    "info": self.semester_schedule[week_key]
                }
        
        return {
            "status": "completed",
            "message": "Semester has ended. Great job!"
        }

    def get_upcoming_assignments(self, days_ahead=7):
        """Get assignments due in the next specified number of days."""
        upcoming = []
        today = datetime.now()
        
        for week_key, week_info in self.semester_schedule.items():
            for assignment_type, assignments in week_info.get("assignments", {}).items():
                for assignment in assignments:
                    # Parse due date (simplified - in real implementation would need proper date parsing)
                    if "due" in assignment:
                        upcoming.append({
                            "week": week_key,
                            "type": assignment_type, 
                            "name": assignment["name"],
                            "due": assignment["due"],
                            "sections": week_info.get("sections", [])
                        })
        
        return upcoming

    def get_test_preparation_guide(self, test_number: int) -> str:
        """Get detailed test preparation guide with timeline."""
        if test_number not in [1, 2, 3, 4]:
            return "Please specify Test 1, 2, 3, or 4."
            
        test_key = f"Test {test_number}"
        test_info = self.test_schedule[test_key]
        
        guide = f"""
# 📊 Test {test_number} Preparation Guide

## Test Information
- **Chapters Covered:** {', '.join([str(c) for c in test_info['chapters']])}
- **Test Dates:** {test_info['dates']}
- **Week:** {test_info['week']}

## Key Topics to Master
"""
        
        for topic in test_info['topics']:
            guide += f"- {topic}\n"
            
        guide += f"""
## Chapter Breakdown
"""
        
        for chapter_num in test_info['chapters']:
            chapter = self.chapters[chapter_num]
            guide += f"\n### Chapter {chapter_num}: {chapter['title']}\n"
            for section_num, section_title in chapter['sections'].items():
                guide += f"- **{section_num}:** {section_title}\n"
        
        guide += f"""
## 📅 Study Timeline (Start 1 Week Before)

### 7 Days Before Test
- [ ] Review all formula sheets for covered chapters
- [ ] Complete practice problems from Hawkes Learning
- [ ] Identify weak areas that need extra attention

### 5 Days Before Test  
- [ ] Focus study time on identified weak areas
- [ ] Practice step-by-step problem solving
- [ ] Review common mistakes and how to avoid them

### 3 Days Before Test
- [ ] Take practice quiz covering all topics
- [ ] Review any remaining problem areas
- [ ] Organize formula sheets and notes

### 1 Day Before Test
- [ ] Light review of formulas (don't cram!)
- [ ] Get good sleep and proper nutrition
- [ ] Test Respondus Lockdown Browser setup

### Test Day
- [ ] Arrive early or log in early for online test
- [ ] Read questions carefully
- [ ] Show all work clearly
- [ ] Check units in final answers
- [ ] Stay calm and confident!

## 💡 Test-Taking Strategies
1. **Read each problem twice** before starting
2. **Identify what you're solving for** first
3. **Write down given information** clearly
4. **Choose the right formula** for the problem
5. **Check if your answer makes sense** in context
"""
        
        return guide

    def interactive_session(self):
        """Enhanced interactive tutoring session with calendar features."""
        print("🎓 Welcome to your Enhanced MAT 143 Tutor! 🎓")
        print("Hi Kristina! I'm here to help you succeed in Quantitative Literacy.")
        
        # Show current week info
        week_info = self.get_current_week_info()
        if week_info["status"] == "in_progress":
            current_week = week_info["info"]
            print(f"\n📅 Current Week: {week_info['week']} ({current_week['dates']})")
            print(f"📚 Sections this week: {', '.join(current_week['sections'])}")
            print(f"🎯 Focus: {current_week['focus']}")
        
        print("\nWhat would you like help with today?")
        print("Commands:")
        print("  'calendar' - See current week and upcoming assignments") 
        print("  'chapter X' - Get help with chapter X")
        print("  'section X.Y' - Get help with specific section")
        print("  'homework' - Get homework help")
        print("  'test X' - Prepare for test X") 
        print("  'explain [concept]' - Understand a concept")
        print("  'formula [topic]' - Look up formulas")
        print("  'schedule' - See full semester timeline")
        print("  'quit' - Exit")
        print("\n" + "="*50)
        
        while True:
            try:
                user_input = input("\n💭 What can I help you with? ").strip().lower()
                
                if user_input == 'quit' or user_input == 'exit':
                    print("Good luck with your studies, Kristina! You've got this! 🌟")
                    break
                
                elif user_input == 'calendar':
                    self.show_calendar_info()
                    
                elif user_input == 'schedule':
                    self.show_semester_schedule()
                
                elif user_input.startswith('section'):
                    try:
                        section = user_input.split()[1]
                        print(f"\n📖 {self.get_section_help(section)}")
                    except IndexError:
                        print("Please specify a section (e.g., 'section 6.2')")
                
                elif user_input.startswith('chapter'):
                    try:
                        chapter_num = int(user_input.split()[1])
                        print(f"\n📖 {self.get_chapter_help(chapter_num)}")
                    except (IndexError, ValueError):
                        print("Please specify a chapter number (e.g., 'chapter 6')")
                
                # ... rest of the interactive commands
                
            except KeyboardInterrupt:
                print("\n\nGood luck with your studies, Kristina! You've got this! 🌟")
                break
            except Exception as e:
                print(f"Oops, something went wrong: {e}")

    def show_calendar_info(self):
        """Display current week information and upcoming assignments."""
        week_info = self.get_current_week_info()
        
        if week_info["status"] == "not_started":
            print(f"\n📅 {week_info['message']}")
            print(f"⏳ Days until semester starts: {week_info['days_until']}")
            return
        
        if week_info["status"] == "completed":
            print(f"\n🎉 {week_info['message']}")
            return
            
        current_week = week_info["info"]
        print(f"\n📅 Week {week_info['week']}: {current_week['dates']}")
        print(f"📚 Sections: {', '.join(current_week['sections'])}")
        print(f"🎯 Focus: {current_week['focus']}")
        
        if "important" in current_week:
            print(f"⚠️  IMPORTANT: {current_week['important']}")
        
        print(f"\n📋 This Week's Assignments:")
        for assignment_type, assignments in current_week["assignments"].items():
            print(f"\n  {assignment_type}:")
            for assignment in assignments:
                print(f"    • {assignment['name']} - Due: {assignment['due']}")

    def show_semester_schedule(self):
        """Display the complete semester schedule."""
        print("\n📅 MAT 143 Fall 2025 Complete Schedule")
        print("="*50)
        
        for week_key, week_info in self.semester_schedule.items():
            print(f"\n{week_key}: {week_info['dates']}")
            print(f"  📚 Sections: {', '.join(week_info['sections'])}")
            print(f"  🎯 {week_info['focus']}")
            
            if "important" in week_info:
                print(f"  ⚠️  {week_info['important']}")

    def get_section_help(self, section: str) -> str:
        """Get help for a specific section (e.g., '6.2')."""
        # Find which chapter this section belongs to
        chapter_num = int(section.split('.')[0])
        
        if chapter_num not in self.chapters:
            return f"Section {section} is not part of the MAT 143 curriculum."
        
        chapter = self.chapters[chapter_num]
        if section not in chapter['sections']:
            return f"Section {section} not found in Chapter {chapter_num}."
            
        section_title = chapter['sections'][section]
        
        return f"Section {section}: {section_title}\n\n" + self.get_chapter_help(chapter_num)

    def get_chapter_help(self, chapter: int, topic: str = "") -> str:
        """Get help for a specific chapter."""
        if chapter not in self.chapters:
            return f"Chapter {chapter} is not part of the MAT 143 curriculum."
        
        chapter_info = self.chapters[chapter]
        
        # Build response with section information
        response = f"Chapter {chapter}: {chapter_info['title']}\n\n"
        response += "Sections covered:\n"
        
        for section_num, section_title in chapter_info['sections'].items():
            response += f"• {section_num}: {section_title}\n"
        
        # Add specific help based on chapter
        if chapter == 1:
            response += self.get_chapter_1_help()
        elif chapter == 4:
            response += self.get_chapter_4_help()
        elif chapter == 5:
            response += self.get_chapter_5_help()
        elif chapter == 6:
            response += self.get_chapter_6_help()
        elif chapter == 7:
            response += self.get_chapter_7_help()
        elif chapter == 10:
            response += self.get_chapter_10_help()
        elif chapter == 11:
            response += self.get_chapter_11_help()
        elif chapter == 13:
            response += self.get_chapter_13_help()
        
        return response

    # Helper methods for each chapter
    def get_chapter_1_help(self):
        return """
🧠 Key Concepts:
• Deductive Reasoning: Drawing conclusions from general principles
• Inductive Reasoning: Making generalizations from specific observations
• Pattern Recognition: Finding consistent rules in sequences
• Problem Solving: Organized approach to finding solutions

💡 Study Tips:
• Practice identifying sequence patterns (arithmetic, geometric, neither)
• Learn to distinguish between deductive and inductive reasoning
• Use estimation to check if answers are reasonable
"""

    def get_chapter_4_help(self):
        return """
📊 Key Concepts:
• Proportions: Equal ratios (a/b = c/d)
• Cross-multiplication: If a/b = c/d, then ad = bc
• Percentages: Parts per hundred
• Unit rates: Rates with denominator of 1

💡 Study Tips:
• Set up proportions carefully - make sure units match
• Convert percentages to decimals for calculations
• Practice percentage increase/decrease problems
• Use dimensional analysis for unit conversions
"""

    def get_chapter_5_help(self):
        return """
📈 Key Concepts:
• Linear functions: Constant rate of change (straight line)
• Exponential functions: Constant percent change (curved)
• Slope: Rate of change in linear functions
• Growth/decay factors in exponential functions

💡 Study Tips:
• Linear: y = mx + b (m is slope, b is y-intercept)
• Exponential: y = a(b)^x (b > 1 is growth, 0 < b < 1 is decay)
• Look for constant differences (linear) vs constant ratios (exponential)
"""

    def get_chapter_6_help(self):
        return """
💰 Key Concepts:
• Simple Interest: I = Prt
• Compound Interest: A = P(1 + r/n)^(nt)
• APY: Actual yearly return including compounding
• Present/Future Value calculations

💡 Study Tips:
• Memorize the interest formulas - they're used frequently
• Remember: r must be in decimal form (5% = 0.05)
• n = compounding frequency (monthly = 12, quarterly = 4)
• Use financial calculator functions when allowed
"""

    def get_chapter_7_help(self):
        return """
📏 Key Concepts:
• Metric prefixes: kilo-, centi-, milli-, etc.
• Conversion factors: 1 inch = 2.54 cm, etc.
• Dimensional analysis: Using unit fractions to convert
• Temperature: C = 5(F-32)/9, F = 9C/5 + 32

💡 Study Tips:
• Memorize key conversions (especially 1 inch = 2.54 cm)
• Set up conversions so units cancel properly
• Always include units in your work
• Double-check that final units match what's asked for
"""

    def get_chapter_10_help(self):
        return """
🎲 Key Concepts:
• Basic probability: P(event) = favorable/total outcomes
• Expected value: Average result over many trials
• Probability rules: 0 ≤ P ≤ 1, sum of all outcomes = 1
• Tree diagrams for complex probability

💡 Study Tips:
• List all possible outcomes systematically
• Use fractions, then convert to decimals if needed
• Expected value = Σ(outcome × probability)
• Check that probabilities sum to 1
"""

    def get_chapter_11_help(self):
        return """
📊 Key Concepts:
• Statistical studies: observational vs experimental
• Data displays: histograms, box plots, scatter plots
• Measures of center: mean, median, mode
• Z-scores: z = (x - μ)/σ

💡 Study Tips:
• Z-scores tell you how many standard deviations from mean
• Empirical rule: 68% within 1 std dev, 95% within 2, 99.7% within 3
• Positive z-score = above average, negative = below average
• Practice reading and interpreting graphs
"""

    def get_chapter_13_help(self):
        return """
🗳️ Key Concepts:
• Voting methods: majority, plurality, Borda count, etc.
• Fairness criteria: majority, Condorcet, monotonicity, etc.
• Apportionment: Hamilton, Jefferson, Webster methods
• Standard divisor and quota calculations

💡 Study Tips:
• Learn the steps for each apportionment method
• Understand why different methods can give different results
• Practice calculating standard divisors and quotas
• Know the fairness criteria and which methods violate them
"""


def main():
    """Main function to run the enhanced tutor."""
    print("Setting up your Enhanced MAT 143 tutor with calendar...")
    
    # Try to get API key, but don't require it for calendar features
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Note: No API key found. Calendar and study features will work,")
        print("but AI-powered explanations will be limited.")
        print("Get an API key from: https://console.anthropic.com/")
    
    tutor = MAT143TutorWithCalendar(api_key)
    tutor.interactive_session()


if __name__ == "__main__":
    main()
