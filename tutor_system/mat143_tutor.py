#!/usr/bin/env python3
"""
MAT 143 AI Tutor System for Kristina
A personalized tutoring assistant for MAT 143 - Quantitative Literacy

This system provides:
- Chapter-specific help
- Formula assistance
- Step-by-step problem solving
- Homework guidance
- Test preparation
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional
import anthropic
from pathlib import Path

class MAT143Tutor:
    def __init__(self, api_key: str):
        """Initialize the MAT 143 Tutor with course knowledge."""
        self.client = anthropic.Anthropic(api_key=api_key)
        self.course_materials = {}
        self.session_history = []
        self.load_course_materials()
        
        # Course structure based on provided materials
        self.chapters = {
            1: "Thinking Mathematically, Estimating, Problem Solving",
            4: "Proportions, Percentages, and Ratios",
            5: "Linear and Exponential Functions", 
            6: "Personal Finance (Interest, Saving, Borrowing)",
            7: "Measurement and Conversions",
            10: "Probability and Expected Value",
            11: "Statistics and Data Analysis",
            13: "Voting Methods and Apportionment"
        }
        
        # Test schedule
        self.test_schedule = {
            "Test 1": ["Chapter 1", "Chapter 13"],
            "Test 2": ["Chapter 4", "Chapter 5"], 
            "Test 3": ["Chapter 6", "Chapter 7"],
            "Test 4": ["Chapter 10", "Chapter 11"]
        }

    def load_course_materials(self):
        """Load all course materials from the course_materials directory."""
        materials_dir = Path(__file__).parent.parent / "course_materials"
        
        if materials_dir.exists():
            for file_path in materials_dir.rglob("*"):
                if file_path.is_file():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            self.course_materials[str(file_path)] = content
                    except Exception as e:
                        print(f"Could not load {file_path}: {e}")

    def get_chapter_help(self, chapter: int, topic: str = "") -> str:
        """Get help for a specific chapter and topic."""
        if chapter not in self.chapters:
            return f"Chapter {chapter} is not part of the MAT 143 curriculum."
        
        chapter_info = self.chapters[chapter]
        
        prompt = f"""
You are a patient, encouraging math tutor helping Kristina with MAT 143 - Quantitative Literacy.

Kristina is working on Chapter {chapter}: {chapter_info}

{f"Specific topic: {topic}" if topic else ""}

Course context:
- This is an online course at CPCC
- Kristina has struggled with math before and needs extra encouragement
- She uses Hawkes Learning for homework assignments
- The course covers practical, real-world applications of math

Please provide:
1. A brief overview of the chapter concepts
2. Key formulas or methods (if applicable)
3. Common mistakes to avoid
4. Step-by-step approach to typical problems
5. Encouraging words and study tips

Be patient, clear, and encouraging. Use simple language and provide concrete examples.
"""
        
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"I'm having trouble connecting right now. Error: {e}"

    def help_with_homework(self, assignment: str, specific_question: str = "") -> str:
        """Provide homework help for specific assignments."""
        prompt = f"""
You are helping Kristina with her MAT 143 homework assignment: {assignment}

{f"Specific question: {specific_question}" if specific_question else ""}

Kristina needs:
- Step-by-step explanations
- Clear reasoning for each step
- Tips for similar problems
- Encouragement and confidence building

Important: Don't just give the answer. Help her understand the process so she can solve similar problems independently.

Course topics covered:
- Chapter 1: Mathematical thinking, estimation, problem solving
- Chapter 4: Proportions, percentages, ratios  
- Chapter 5: Linear and exponential functions
- Chapter 6: Interest, saving, borrowing, budgeting
- Chapter 7: Metric system and conversions
- Chapter 10: Probability and expected value
- Chapter 11: Statistics and data analysis
- Chapter 13: Voting methods and apportionment

Be encouraging and patient. Kristina has struggled with math before but is determined to succeed.
"""
        
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1200,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"I'm having trouble connecting right now. Error: {e}"

    def test_prep_help(self, test_number: int) -> str:
        """Provide test preparation guidance."""
        if f"Test {test_number}" not in self.test_schedule:
            return "Please specify Test 1, 2, 3, or 4."
        
        test_chapters = self.test_schedule[f"Test {test_number}"]
        
        prompt = f"""
Help Kristina prepare for Test {test_number} in MAT 143.

This test covers: {', '.join(test_chapters)}

Provide:
1. Key concepts to review for each chapter
2. Important formulas to memorize
3. Types of problems likely to appear
4. Study strategies and tips
5. Practice problem suggestions
6. Time management advice for the test
7. Encouraging words to build confidence

Remember: 
- Kristina uses the Respondus Lockdown Browser for tests
- Tests are taken both in BrightSpace and Hawkes Learning
- She has struggled with math before and needs encouragement
- Focus on practical, step-by-step approaches

Be supportive and help build her confidence while ensuring she's well-prepared.
"""
        
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1200,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"I'm having trouble connecting right now. Error: {e}"

    def explain_concept(self, concept: str) -> str:
        """Explain a specific mathematical concept in simple terms."""
        prompt = f"""
Explain the concept of "{concept}" to Kristina, who is taking MAT 143 - Quantitative Literacy.

Guidelines:
- Use simple, clear language
- Provide real-world examples
- Break complex ideas into smaller steps
- Be encouraging and supportive
- Connect to course topics when possible
- Include practical applications

Course context: MAT 143 focuses on practical math for everyday life, including:
- Problem solving and estimation
- Proportions and percentages
- Linear and exponential relationships
- Personal finance
- Measurement and conversions
- Basic probability and statistics
- Voting and apportionment

Make the explanation accessible and relevant to someone who has struggled with math but is determined to learn.
"""
        
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"I'm having trouble connecting right now. Error: {e}"

    def formula_lookup(self, topic: str) -> str:
        """Look up formulas for specific topics."""
        formulas = {
            "interest": {
                "Simple Interest": "I = Prt",
                "Compound Interest": "A = P(1 + r/n)^(nt)",
                "Continuous Compound": "A = Pe^(rt)",
                "APY": "APY = ((1 + r/n)^n - 1) × 100%"
            },
            "conversions": {
                "Temperature F to C": "C = 5(F-32)/9",
                "Temperature C to F": "F = 9C/5 + 32",
                "Length": "1 inch = 2.54 cm, 1 ft ≈ 0.305 m, 1 yard ≈ 0.914 m, 1 mile ≈ 1.61 km"
            },
            "statistics": {
                "Z-score": "z = (data - mean) / standard deviation",
                "Population z-score": "z = (x - μ) / σ",
                "Sample z-score": "z = (x - x̄) / s"
            },
            "probability": {
                "Basic Probability": "P(event) = favorable outcomes / total outcomes",
                "Expected Value": "E(X) = Σ(x × P(x))"
            },
            "apportionment": {
                "Standard Divisor": "SD = total population / total items to apportion",
                "Standard Quota": "SQ = subgroup population / standard divisor"
            }
        }
        
        topic_lower = topic.lower()
        result = f"Formulas for {topic}:\n\n"
        
        found = False
        for category, formula_dict in formulas.items():
            if topic_lower in category or any(topic_lower in formula.lower() for formula in formula_dict.keys()):
                found = True
                result += f"{category.upper()}:\n"
                for name, formula in formula_dict.items():
                    result += f"  • {name}: {formula}\n"
                result += "\n"
        
        if not found:
            result = f"I don't have specific formulas for '{topic}' in my database. Try asking about: interest, conversions, statistics, probability, or apportionment."
        
        return result

    def interactive_session(self):
        """Start an interactive tutoring session."""
        print("🎓 Welcome to your MAT 143 Tutor! 🎓")
        print("Hi Kristina! I'm here to help you succeed in Quantitative Literacy.")
        print("\nWhat would you like help with today?")
        print("Commands:")
        print("  'chapter X' - Get help with chapter X")
        print("  'homework' - Get homework help")
        print("  'test X' - Prepare for test X")
        print("  'explain [concept]' - Understand a concept")
        print("  'formula [topic]' - Look up formulas")
        print("  'quit' - Exit")
        print("\n" + "="*50)
        
        while True:
            try:
                user_input = input("\n💭 What can I help you with? ").strip().lower()
                
                if user_input == 'quit' or user_input == 'exit':
                    print("Good luck with your studies, Kristina! You've got this! 🌟")
                    break
                
                elif user_input.startswith('chapter'):
                    try:
                        chapter_num = int(user_input.split()[1])
                        print(f"\n📖 {self.get_chapter_help(chapter_num)}")
                    except (IndexError, ValueError):
                        print("Please specify a chapter number (e.g., 'chapter 6')")
                
                elif user_input.startswith('homework'):
                    assignment = input("Which assignment are you working on? ")
                    question = input("Any specific question or topic? (optional) ")
                    print(f"\n📝 {self.help_with_homework(assignment, question)}")
                
                elif user_input.startswith('test'):
                    try:
                        test_num = int(user_input.split()[1])
                        print(f"\n📊 {self.test_prep_help(test_num)}")
                    except (IndexError, ValueError):
                        print("Please specify a test number (e.g., 'test 2')")
                
                elif user_input.startswith('explain'):
                    concept = ' '.join(user_input.split()[1:])
                    if concept:
                        print(f"\n🧠 {self.explain_concept(concept)}")
                    else:
                        concept = input("What concept would you like me to explain? ")
                        print(f"\n🧠 {self.explain_concept(concept)}")
                
                elif user_input.startswith('formula'):
                    topic = ' '.join(user_input.split()[1:])
                    if topic:
                        print(f"\n📐 {self.formula_lookup(topic)}")
                    else:
                        topic = input("What topic do you need formulas for? ")
                        print(f"\n📐 {self.formula_lookup(topic)}")
                
                else:
                    print("I'm not sure what you need help with. Try one of these commands:")
                    print("  'chapter X', 'homework', 'test X', 'explain [concept]', 'formula [topic]'")
                    
            except KeyboardInterrupt:
                print("\n\nGood luck with your studies, Kristina! You've got this! 🌟")
                break
            except Exception as e:
                print(f"Oops, something went wrong: {e}")


def main():
    """Main function to run the tutor."""
    print("Setting up your MAT 143 tutor...")
    
    # You'll need to set your Anthropic API key as an environment variable
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("Please set your ANTHROPIC_API_KEY environment variable.")
        print("You can get an API key from: https://console.anthropic.com/")
        return
    
    tutor = MAT143Tutor(api_key)
    tutor.interactive_session()


if __name__ == "__main__":
    main()
