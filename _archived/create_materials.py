#!/usr/bin/env python3
"""
Course Materials Organizer for MAT 143
Extracts and organizes the provided course materials
"""

import os
from pathlib import Path

def create_course_materials():
    """Create organized course materials from the provided documents."""
    
    base_dir = Path("/Users/bethcartrette/REPOS/kristina_math_tutor/course_materials")
    
    print("📁 Creating organized course materials...")
    
    # Formula sheets content
    formula_sheets = {
        "Unit_1_Formula_Sheet.md": """# MAT 143 Unit 1 Formula Sheet

## Election Counting Methods

**Majority Rule Decision** — The winner must have more than 50% of the votes to win.

**Plurality** — The candidate with the most votes wins. No majority required.

**Borda Count** — Voting results are organized in a preference table and each ranking is assigned a specific number of points based on how many candidates are in the election. The candidate with the most ranking points is declared the winner.

**Plurality with Elimination** — A series of runoff elections where the candidate with the least amount of first-place votes is removed from the ballot each round. A winner is declared when a candidate has a majority of the first place votes.

**Pairwise Comparison** — Every candidate is compared head to head with other candidates. In each pair of comparisons, the candidate with the greater number of higher rankings is given a point. The candidate with the most points after all head-to head comparisons are made is the winner. The number of pairwise match-ups is n(n-1)/2.

## Apportionment

**Standard Divisor (SD)** — The average number of members of the population that will account for one apportioned item.
SD = total population in a group / total number of items to be apportioned
*Round the standard divisor to 4 decimal places*

**Standard Quota (SQ)** — represents the number of items that will be apportioned to each subgroup
SQ = population of the subgroup / Standard divisor

### Hamilton Method of Apportionment
1. Calculate the standard divisor
2. Calculate the standard quota for each subgroup
3. Calculate the lower quota for each subgroup (Round down)
4. Assign each subgroup the number of resources based on its lower quota
5. Assign any remaining resources based on the fractional remainder of the standard quota, in order from largest to smallest

### Jefferson Method of Apportionment
1. Calculate the Standard divisor
2. Calculate the standard quota for each subgroup
3. Calculate the lower quota (round down)
4. Assign each subgroup the number of resources based on its lower quota
5. If there are remaining resources to be distributed, chose a modified divisor by trial and error until the sum of the lower quotas equals the number of resources to be apportioned

### Webster's Method
1. Calculate the standard divisor
2. Calculate the standard quota for each subgroup. Round each quota to the nearest integer
3. Assign each subgroup the number of resources based on the rounded quota (Round like normal)
4. If there are remaining resources to be distributed, chose a modified divisor by trial and error until the sum of the rounded quotas equals the number of resources to be apportioned
""",

        "Chapter_6_Formula_Sheet.md": """# MAT 143 Chapter 6 Formula Sheet - Personal Finance

## Simple Interest Formula
**I = Prt**
- I = Interest earned
- P = Principal (starting amount)
- r = annual interest rate (as decimal)
- t = time in years

## Compound Interest
**A = P(1 + r/n)^(nt)**
- A = Final amount
- P = Principal
- r = annual interest rate (as decimal)
- n = number of compounding periods per year
- t = time in years

### Compounding Frequencies:
- Annually: n = 1
- Semiannually: n = 2  
- Quarterly: n = 4
- Monthly: n = 12
- Weekly: n = 52
- Daily: n = 365

## Continuous Compound Interest Formula
**A = Pe^(rt)**

## Annual Percentage Yield (APY)
**APY = ((1 + r/n)^n - 1) × 100%**

## Present Value
**PV = A / (1 + r/n)^(nt)**

## Annuity Formula for Future Value
**FV = PMT × [((1 + r/n)^(nt) - 1) / (r/n)]**

## Annuity Formula for Payment Amounts
**PMT = FV × [r/n / ((1 + r/n)^(nt) - 1)]**

## Regular Payment Formula for Fixed Installment Loans
**PMT = (P × r/n) / (1 - (1 + r/n)^(-nt))**

## Maximum Purchase Price Formula
**maximum purchase price = PMT × [(1 - (1 + r/n)^(-nt)) / (r/n)]**

## Number of Fixed Payments Required to Pay Off Credit Card Debt
**R = -log(1 - (r/n)(A/PMT)) / log(1 + r/n)**
""",

        "Chapter_7_Formula_Sheet.md": """# MAT 143 Chapter 7 Formula Sheet - Conversions

## US Customary System

### Units of Length
- 12 inches (in.) = 1 foot (ft)
- 36 inches (in.) = 1 yard (yd)
- 3 feet (ft) = 1 yard (yd)
- 5280 Feet (ft) = 1 mile (mi)

### Units of Mass
- 16 ounces (oz) = 1 pound (lb)
- 2000 pounds = 1 ton (T)

### Units of Capacity
- 8 fluid ounces (fl oz) = 1 cup (c)
- 2 cups = 1 pint (pt) = 16 fl. oz
- 2 pints = 1 quart (qt)
- 4 quarts = 1 gallon

### Units of Time
- 60 seconds (sec) = 1 minute (min)
- 60 minutes = 1 hour (hr)
- 24 hours = 1 day
- 7 days = 1 week

## Metric System Prefixes
- Kilo- (1000)
- Hecto- (100) 
- Deka- (10)
- Base Unit (1)
- Deci- (0.1)
- Centi- (0.01)
- Milli- (0.001)

## Common US to Metric Conversions

### Length
- **1 inch = 2.54 cm**
- **1 ft ≈ 0.305 m**
- **1 yard ≈ 0.914 m**
- **1 mile ≈ 1.61 km**

### Area
- 1 in² ≈ 6.45 cm²
- 1 ft² ≈ 0.093 m²
- 1 yd² ≈ 0.836 m²
- 1 mi² ≈ 2.6 km²
- 1 acre ≈ 0.405 ha

### Volume
- 1 tsp ≈ 5 mL
- 1 tbsp ≈ 15 mL
- 1 cup ≈ 0.24 L
- 1 pint ≈ 0.47 L
- 1 qt ≈ 0.946 L
- 1 gal ≈ 3.785 L

### Mass
- 1 oz ≈ 28.35 g
- 1 lb ≈ 0.454 kg

## Temperature Formulas
- **F = (9C/5) + 32**
- **C = 5(F-32)/9**
""",

        "Unit_4_Formula_Sheet.md": """# MAT 143 Unit 4 Formula Sheet - Statistics

## Z-Score Formula
**z = (data - mean) / standard deviation**

### For Populations:
**z = (x - μ) / σ**
- x = data value
- μ = population mean
- σ = population standard deviation

### For Samples:
**z = (x - x̄) / s**
- x = data value
- x̄ = sample mean
- s = sample standard deviation

## Empirical Rule (68-95-99.7 Rule)
For normally distributed data:
- 68% of data falls within 1 standard deviation of the mean
- 95% of data falls within 2 standard deviations of the mean
- 99.7% of data falls within 3 standard deviations of the mean

## Probability
**P(event) = favorable outcomes / total outcomes**

**Expected Value: E(X) = Σ(x × P(x))**
"""
    }
    
    # Create formula sheets
    formula_dir = base_dir / "formula_sheets"
    formula_dir.mkdir(parents=True, exist_ok=True)
    
    for filename, content in formula_sheets.items():
        with open(formula_dir / filename, 'w') as f:
            f.write(content)
    
    # Sample assignments content
    sample_assignments = {
        "Week_1_Attendance_Sample.md": """# MAT 143 Week 1 Attendance Assignment Sample

## Question Types You Can Expect:

### Deductive vs Inductive Reasoning
**Example:** Taylor plays football and has caught 24 out of 56 targets so far this season. So, he is expected to catch 6 out of 14 targets in tonight's game.
**Answer:** Inductive (making a prediction based on past performance)

### Pattern Recognition
**Example:** Given the sequence: 288, 144, 72, 36, ...
- **Pattern:** To find the next number, divide the previous number by 2
- **Next terms:** 18, 9
- **Type:** Geometric sequence

### Sequence Types
- **Arithmetic:** Constant difference between terms (add same number each time)
- **Geometric:** Constant ratio between terms (multiply/divide by same number each time)
- **Neither:** Pattern that doesn't fit arithmetic or geometric rules

## Study Tips:
1. Look for what's being added, subtracted, multiplied, or divided
2. Check if the pattern is consistent throughout the sequence  
3. Write out your reasoning in complete sentences
4. Always identify the sequence type (arithmetic, geometric, or neither)
"""
    }
    
    # Create sample assignments
    assignments_dir = base_dir / "sample_assignments"
    assignments_dir.mkdir(parents=True, exist_ok=True)
    
    for filename, content in sample_assignments.items():
        with open(assignments_dir / filename, 'w') as f:
            f.write(content)
    
    # Course schedule and syllabus
    syllabus_content = {
        "Course_Schedule_Fall_2025.md": """# MAT 143 Course Schedule - Fall 2025

## Important Dates
- **Semester Start:** August 18, 2025
- **Semester End:** December 12, 2025  
- **Census Date (EVA Due):** August 29, 2025
- **Last Day to Withdraw:** September 26, 2025

## Test Schedule
- **Test 1:** Week 4 (Sept 8-12) - Chapters 1 & 13
- **Test 2:** Week 7 (Sept 29-Oct 3) - Chapters 4 & 5
- **Test 3:** Week 11 (Nov 3-7) - Chapters 6 & 7
- **Test 4:** Week 16 (Dec 8-12) - Chapters 10 & 11

## Chapter Coverage by Week
1. **Weeks 1-2:** Chapter 1 (Thinking Mathematically) & Chapter 13 (Voting/Apportionment)
2. **Weeks 5-6:** Chapter 4 (Proportions) & Chapter 5 (Functions)
3. **Weeks 8-10:** Chapter 7 (Conversions) & Chapter 6 (Personal Finance)
4. **Weeks 12-15:** Chapter 10 (Probability) & Chapter 11 (Statistics)

## Assignment Types & Weights
- **Tests:** 60%
- **Homework (Hawkes Learning):** 20%
- **Lab Assignments:** 10%
- **Signature Assignment:** 5%
- **Weekly Attendance:** 5%

## Key Requirements
- Complete EVA (Enrollment Verification Activity) by census date
- Use Respondus Lockdown Browser for all tests
- Achieve "mastery" in Hawkes Learning assignments (must see congratulations message)
- Submit weekly attendance assignments in BrightSpace
"""
    }
    
    # Create syllabus materials
    syllabus_dir = base_dir / "syllabus_and_schedule"
    syllabus_dir.mkdir(parents=True, exist_ok=True)
    
    for filename, content in syllabus_content.items():
        with open(syllabus_dir / filename, 'w') as f:
            f.write(content)
    
    # Instructions content
    instructions_content = {
        "Hawkes_Learning_Setup.md": """# Setting Up Hawkes Learning for MAT 143

## IMPORTANT: Complete EVA First!
The Hawkes Learning button will NOT appear on your Brightspace page until the EVA (Enrollment Verification Activity) is completed.

## Setup Steps:
1. Log into your Brightspace account
2. Click on your MAT 143 course
3. Click on Content
4. Click on the Hawkes Learning button (6th item on left-hand side)
5. Click on the first assignment: Lesson 1.1
6. You should now be in Hawkes Learning

## For Homework Success:
- Complete problems until you see: "Congratulations! You've Mastered this lesson"
- You get either 100% (mastery) or 0% (not mastered) - no partial credit
- Use hints when stuck, but focus on understanding
- Return to Hawkes Learning tab in Brightspace for all assignments

## Need Help?
- No access code needed - it's included in your tuition
- If you have issues, contact your instructor immediately
- For MAT 043 students: Follow separate instructions from your MAT 043 instructor
"""
    }
    
    # Create instructions
    instructions_dir = base_dir / "instructions"
    instructions_dir.mkdir(parents=True, exist_ok=True)
    
    for filename, content in instructions_content.items():
        with open(instructions_dir / filename, 'w') as f:
            f.write(content)
    
    # Chapter resources
    resources_content = {
        "Chapter_Resources.md": """# MAT 143 Chapter Resources

## Google Drive Folders (from course materials)

### Chapter 1 & 13
- Chapter 1: https://drive.google.com/drive/folders/1yEsb6TUSC72mb6PU8P3Oy2eztxYo-eqb
- Chapter 13: https://drive.google.com/drive/folders/1yOKSgy3mr3X7oR1LpzBtp7mpk9pzVuIg

### Chapter 4 & 5
- Chapter 4: https://drive.google.com/drive/folders/18ATn37hsHGv6X09NP1FeEvtSJ7owBjzv
- Chapter 5: https://drive.google.com/drive/folders/19DpXl6jGlVsVU5XeoZCSGDzkBipyJDsK

### Chapter 6 & 7
- Chapter 6: https://drive.google.com/drive/folders/18_REPow9vLpTEAWCJEDIKqgHbPix3vBx
- Chapter 7: https://drive.google.com/drive/folders/1EQ4JvXkaMcVQg5YvEt7twpY4j_FjCvL9

### Chapter 10 & 11  
- Chapter 10: https://drive.google.com/drive/folders/1X1oVeQMy4vZY0tkr5GdtFS9UE20F2MhW
- Chapter 11: https://drive.google.com/drive/folders/1hKIdhMi4LlINf0CxPOvpWEpEnt911tUv

## Hawkes Learning Video Topics

### Chapter 1: Thinking Mathematically
- 1.1 Thinking Mathematically
- 1.2 Estimating and Evaluating  
- 1.3 Problem Solving: Processes and Techniques

### Chapter 4: Proportions & Percentages
- 4.1 Proportions, Percentages, and Ratios
- 4.2 Using Percentages
- 4.3 Rates, Unit Rates, and Rates of Change
- 4.4 Using Rates for Dimensional Analysis

### Chapter 5: Linear & Exponential Functions
- Note: Hawkes Learning does not have videos for Chapter 5

### Chapter 6: Personal Finance
- 6.1 Understanding Interest
- 6.2 Saving and Investing
- 6.3 Borrowing Money
- 6.4 Federal Revenue
- 6.5 Budgeting

### Chapter 7: Measurement & Conversions
- 7.4 The Metric System
- 7.5 Converting between the US Customary System and the Metric System

### Chapter 10: Probability
- 10.1 Introduction to Probability
- 10.2 Counting Outcomes
- 10.3 Probability of Single Events
- 10.4 Addition and Multiplication Rules of Probability
- 10.6 Expected Value

### Chapter 11: Statistics  
- 11.1 Statistical Studies
- 11.2 Displaying Data
- 11.3 Describing and Analyzing Data
- 11.4 The Normal Distribution

### Chapter 13: Voting & Apportionment
- 13.1 How to Determine a Winner
- 13.2 Flaws in Voting Methods
- 13.3 Apportionment
"""
    }
    
    # Create resources
    resources_dir = base_dir / "resources"
    resources_dir.mkdir(parents=True, exist_ok=True)
    
    for filename, content in resources_content.items():
        with open(resources_dir / filename, 'w') as f:
            f.write(content)
    
    print(f"✅ Created organized course materials in {base_dir}")
    
    # List what was created
    print("\n📁 Course materials organized:")
    for item in base_dir.rglob("*"):
        if item.is_file():
            relative_path = item.relative_to(base_dir)
            print(f"  📄 {relative_path}")

if __name__ == "__main__":
    create_course_materials()
