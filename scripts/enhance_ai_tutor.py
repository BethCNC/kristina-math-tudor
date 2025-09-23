#!/usr/bin/env python3
"""
Enhanced AI Tutor with Comprehensive Notes and Tutorials
This script enhances the AI tutor with detailed notes, tutorials, and study features.
"""

import json
import os
from pathlib import Path
import re

def create_enhanced_knowledge_base():
    """Create an enhanced knowledge base with comprehensive notes and tutorials."""
    
    # Load existing comprehensive knowledge base
    try:
        with open('ai_knowledge_base_comprehensive.json', 'r', encoding='utf-8') as f:
            knowledge_base = json.load(f)
    except FileNotFoundError:
        knowledge_base = {"math": {}, "english": {}, "course_info": {}}
    
    # Enhanced math section with detailed notes and tutorials
    enhanced_math = {
        "formulas": knowledge_base.get("math", {}).get("formulas", {}),
        "concepts": knowledge_base.get("math", {}).get("concepts", {}),
        "examples": knowledge_base.get("math", {}).get("examples", {}),
        "study_guides": knowledge_base.get("math", {}).get("study_guides", {}),
        "schedules": knowledge_base.get("math", {}).get("schedules", {}),
        "assignments": knowledge_base.get("math", {}).get("assignments", {}),
        
        # NEW: Comprehensive notes and tutorials
        "detailed_notes": {
            "chapter_1": {
                "title": "Thinking Mathematically",
                "sections": {
                    "1.1": {
                        "title": "Thinking Mathematically",
                        "key_concepts": [
                            "Deductive Reasoning: Drawing conclusions from general principles",
                            "Inductive Reasoning: Making predictions based on patterns",
                            "Mathematical thinking vs everyday thinking"
                        ],
                        "detailed_explanations": {
                            "deductive_reasoning": {
                                "definition": "Drawing conclusions from general principles. If premises are true, conclusion must be true.",
                                "examples": [
                                    "All birds have feathers. A robin is a bird. Therefore, robins have feathers.",
                                    "All triangles have 3 sides. This is a triangle. Therefore, it has 3 sides."
                                ],
                                "keywords": ["all", "every", "always", "never", "must", "necessarily"]
                            },
                            "inductive_reasoning": {
                                "definition": "Making predictions based on patterns and observations. Conclusion is probable, not certain.",
                                "examples": [
                                    "I've seen 10 swans and they're all white. Therefore, all swans are white.",
                                    "The sun has risen every day. Therefore, it will rise tomorrow."
                                ],
                                "keywords": ["probably", "likely", "tends to", "usually", "often"]
                            }
                        },
                        "practice_problems": [
                            {
                                "question": "Taylor plays football and has caught 24 out of 56 targets so far this season. So, he is expected to catch 6 out of 14 targets in tonight's game.",
                                "answer": "Inductive reasoning - making a prediction based on past performance",
                                "explanation": "This is inductive because it's making a prediction about future performance based on past data."
                            }
                        ],
                        "study_tips": [
                            "Look for keywords to identify reasoning type",
                            "Practice with real-world examples",
                            "Remember: deductive = certain, inductive = probable"
                        ]
                    },
                    "1.2": {
                        "title": "Estimating and Evaluating",
                        "key_concepts": [
                            "Estimation strategies for quick approximations",
                            "Evaluating reasonableness of answers",
                            "Order of magnitude thinking"
                        ],
                        "detailed_explanations": {
                            "estimation_strategies": {
                                "rounding": "Round numbers to make calculations easier",
                                "benchmark_numbers": "Use 10, 100, 1000 for comparisons",
                                "breaking_down": "Break complex problems into simpler parts"
                            },
                            "evaluating_answers": {
                                "reasonableness_check": "Does the answer make sense in context?",
                                "unit_consistency": "Do the units match what's expected?",
                                "magnitude_check": "Is the answer the right size?"
                            }
                        },
                        "practice_problems": [
                            {
                                "question": "Estimate: 47 × 23",
                                "answer": "About 1,000 (50 × 20 = 1,000)",
                                "explanation": "Round 47 to 50 and 23 to 20 for easier calculation."
                            }
                        ]
                    },
                    "1.3": {
                        "title": "Problem Solving: Processes and Techniques",
                        "key_concepts": [
                            "Polya's 4-step problem solving process",
                            "Working backwards, making tables, finding patterns",
                            "Organizing information effectively"
                        ],
                        "detailed_explanations": {
                            "polya_steps": {
                                "step_1": {
                                    "title": "Understand the Problem",
                                    "questions": ["What are you solving for?", "What information do you have?", "What are you trying to find?"]
                                },
                                "step_2": {
                                    "title": "Devise a Plan",
                                    "questions": ["What method will you use?", "What formulas or strategies apply?", "How can you break it into steps?"]
                                },
                                "step_3": {
                                    "title": "Carry Out the Plan",
                                    "description": "Do the math step by step. Show your work clearly. Don't skip steps."
                                },
                                "step_4": {
                                    "title": "Look Back",
                                    "questions": ["Does the answer make sense?", "Did you answer the question asked?", "Can you check your work?"]
                                }
                            }
                        }
                    }
                }
            },
            "chapter_4": {
                "title": "Proportions, Percentages, and Ratios",
                "sections": {
                    "4.1": {
                        "title": "Proportions, Percentages, and Ratios",
                        "key_concepts": [
                            "Ratios: Comparing two quantities (3:4 or 3/4)",
                            "Proportions: Two equal ratios (a/b = c/d)",
                            "Cross-multiplication: If a/b = c/d, then ad = bc",
                            "Percentages: Parts per hundred"
                        ],
                        "detailed_explanations": {
                            "ratios": {
                                "definition": "A comparison of two quantities",
                                "examples": ["3:4", "3/4", "3 to 4"],
                                "simplifying": "Always reduce to lowest terms"
                            },
                            "proportions": {
                                "definition": "Two equal ratios",
                                "cross_multiplication": "If a/b = c/d, then ad = bc",
                                "solving_steps": [
                                    "Set up the proportion",
                                    "Cross multiply",
                                    "Solve for the unknown",
                                    "Check your answer"
                                ]
                            }
                        },
                        "practice_problems": [
                            {
                                "question": "Solve for x: 3/4 = x/12",
                                "solution": "x = 9",
                                "steps": [
                                    "Cross multiply: 3 × 12 = 4 × x",
                                    "36 = 4x",
                                    "Divide by 4: x = 9",
                                    "Check: 3/4 = 9/12 ✓"
                                ]
                            }
                        ]
                    }
                }
            }
        },
        
        # NEW: Interactive tutorials
        "interactive_tutorials": {
            "step_by_step_solver": {
                "description": "Interactive step-by-step problem solver",
                "features": [
                    "Guided problem solving",
                    "Hint system",
                    "Common mistake alerts",
                    "Progress tracking"
                ]
            },
            "concept_explainer": {
                "description": "Detailed concept explanations with examples",
                "features": [
                    "Visual representations",
                    "Real-world applications",
                    "Multiple examples",
                    "Practice problems"
                ]
            }
        },
        
        # NEW: Study session tracking
        "study_sessions": {
            "session_tracking": {
                "description": "Track study sessions and progress",
                "features": [
                    "Time spent on each topic",
                    "Topics mastered",
                    "Areas needing review",
                    "Study streak tracking"
                ]
            },
            "progress_analytics": {
                "description": "Analytics on learning progress",
                "features": [
                    "Mastery levels by topic",
                    "Time investment analysis",
                    "Weakness identification",
                    "Study recommendations"
                ]
            }
        }
    }
    
    # Enhanced English section
    enhanced_english = {
        "writing_guides": knowledge_base.get("english", {}).get("writing_guides", {}),
        "essay_requirements": knowledge_base.get("english", {}).get("essay_requirements", {}),
        "citation_guides": knowledge_base.get("english", {}).get("citation_guides", {}),
        
        # NEW: Enhanced writing support
        "detailed_writing_guides": {
            "essay_types": {
                "cause_effect": {
                    "structure": "Introduction → Causes → Effects → Conclusion",
                    "key_elements": ["Clear thesis", "Logical organization", "Evidence", "Analysis"],
                    "common_mistakes": ["Confusing correlation with causation", "Oversimplifying complex issues"]
                },
                "argumentative": {
                    "structure": "Introduction → Arguments → Counterarguments → Conclusion",
                    "key_elements": ["Strong thesis", "Evidence", "Logical reasoning", "Rebuttal"],
                    "common_mistakes": ["Logical fallacies", "Weak evidence", "Ignoring counterarguments"]
                }
            },
            "writing_process": {
                "prewriting": ["Brainstorming", "Outlining", "Research"],
                "drafting": ["First draft", "Focus on content"],
                "revising": ["Big picture changes", "Organization", "Clarity"],
                "editing": ["Grammar", "Spelling", "Punctuation"]
            }
        },
        
        # NEW: Interactive writing tools
        "interactive_tools": {
            "thesis_generator": {
                "description": "Help create strong thesis statements",
                "features": ["Template guidance", "Strength checker", "Examples"]
            },
            "outline_builder": {
                "description": "Interactive essay outline builder",
                "features": ["Structure templates", "Content organization", "Progress tracking"]
            }
        }
    }
    
    # Create enhanced knowledge base
    enhanced_knowledge_base = {
        "math": enhanced_math,
        "english": enhanced_english,
        "course_info": knowledge_base.get("course_info", {}),
        
        # NEW: Global features
        "global_features": {
            "note_taking": {
                "description": "Comprehensive note-taking system",
                "features": [
                    "Save personal notes",
                    "Highlight important concepts",
                    "Create study cards",
                    "Organize by topic"
                ]
            },
            "ai_tutoring": {
                "description": "Enhanced AI tutoring capabilities",
                "features": [
                    "Personalized explanations",
                    "Adaptive difficulty",
                    "Progress tracking",
                    "Encouragement system"
                ]
            },
            "study_planning": {
                "description": "Intelligent study planning",
                "features": [
                    "Schedule optimization",
                    "Topic prioritization",
                    "Review reminders",
                    "Goal tracking"
                ]
            }
        }
    }
    
    # Save enhanced knowledge base
    with open('ai_knowledge_base_enhanced.json', 'w', encoding='utf-8') as f:
        json.dump(enhanced_knowledge_base, f, indent=2, ensure_ascii=False)
    
    print("✅ Enhanced knowledge base created with comprehensive notes and tutorials!")
    return enhanced_knowledge_base

if __name__ == "__main__":
    create_enhanced_knowledge_base()
