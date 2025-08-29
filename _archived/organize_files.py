#!/usr/bin/env python3
"""
File Organization Script for MAT 143 Course Materials
Moves files from Downloads folder to organized course structure
"""

import os
import shutil
from pathlib import Path

def organize_course_files():
    """Organize course files from Downloads into proper structure."""
    
    downloads_dir = Path.home() / "Downloads"
    base_dir = Path(__file__).parent / "course_materials"
    
    print("🗂️  Organizing MAT 143 course materials...")
    
    # File mapping based on typical naming patterns
    file_mappings = {
        # Formula sheets
        "formula_sheets": [
            "formula sheet", "formulas", "unit 1 formula", "unit 4 formula", 
            "chapter 6 formula", "chapter 7 formula", "mat143 unit"
        ],
        
        # Syllabus and schedule
        "syllabus_and_schedule": [
            "syllabus", "pacing guide", "schedule", "semester", "fall 2025"
        ],
        
        # Sample assignments
        "sample_assignments": [
            "attendance week", "solutions", "assignment", "homework"
        ],
        
        # Instructions
        "instructions": [
            "beginning of semester", "hawkes learning", "instructions", "students"
        ]
    }
    
    # Create subdirectories if they don't exist
    for subdir in file_mappings.keys():
        (base_dir / subdir).mkdir(parents=True, exist_ok=True)
    
    # Look for MAT 143 related files in Downloads
    mat143_files = []
    for file_path in downloads_dir.glob("*"):
        if file_path.is_file():
            filename_lower = file_path.name.lower()
            if any(term in filename_lower for term in ["mat143", "mat 143", "quantitative literacy"]):
                mat143_files.append(file_path)
    
    print(f"Found {len(mat143_files)} MAT 143 related files in Downloads")
    
    # Organize files
    organized_count = 0
    for file_path in mat143_files:
        filename_lower = file_path.name.lower()
        moved = False
        
        for category, keywords in file_mappings.items():
            if any(keyword in filename_lower for keyword in keywords):
                destination = base_dir / category / file_path.name
                
                # Avoid overwriting existing files
                counter = 1
                original_dest = destination
                while destination.exists():
                    stem = original_dest.stem
                    suffix = original_dest.suffix
                    destination = original_dest.parent / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                try:
                    shutil.copy2(file_path, destination)
                    print(f"  ✅ Moved {file_path.name} → {category}/")
                    organized_count += 1
                    moved = True
                    break
                except Exception as e:
                    print(f"  ❌ Error moving {file_path.name}: {e}")
        
        if not moved:
            # Put unmatched files in a general folder
            misc_dir = base_dir / "miscellaneous"
            misc_dir.mkdir(exist_ok=True)
            destination = misc_dir / file_path.name
            
            try:
                shutil.copy2(file_path, destination)
                print(f"  📄 Moved {file_path.name} → miscellaneous/")
                organized_count += 1
            except Exception as e:
                print(f"  ❌ Error moving {file_path.name}: {e}")
    
    print(f"\n🎉 Successfully organized {organized_count} files!")
    print(f"Files are now organized in: {base_dir}")
    
    # List organized structure
    print("\n📁 Current organization:")
    for item in base_dir.rglob("*"):
        if item.is_file():
            relative_path = item.relative_to(base_dir)
            print(f"  📄 {relative_path}")


if __name__ == "__main__":
    organize_course_files()
