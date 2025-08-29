#!/usr/bin/env python3
"""
MAT 143 Tutor System Test Script
Verifies all components are working correctly
"""

import os
import sys
from pathlib import Path
import json

def test_file_structure():
    """Test that all required files exist."""
    print("🔍 Testing file structure...")
    
    required_files = [
        "index.html",
        "tutor.html", 
        "reference.html",
        "calendar_study_system.html",
        "web_study_helper.html",
        "calendar.html",
        "tutor_system/mat143_tutor.py",
        "tutor_system/enhanced_tutor.py",
        "course_materials/formula_sheets/All_Sections_Guide.md",
        "requirements.txt",
        "package.json",
        "vite.config.js",
        "tokens.json",
        "setup.sh",
        "organize_files.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
        else:
            print(f"  ✅ {file_path}")
    
    if missing_files:
        print(f"  ❌ Missing files: {missing_files}")
        return False
    
    print("  ✅ All required files present")
    return True

def test_python_dependencies():
    """Test Python dependencies."""
    print("\n🐍 Testing Python dependencies...")
    
    try:
        import anthropic
        print("  ✅ anthropic package available")
    except ImportError:
        print("  ❌ anthropic package not found")
        return False
    
    try:
        import pathlib
        print("  ✅ pathlib package available")
    except ImportError:
        print("  ❌ pathlib package not found")
        return False
    
    return True

def test_api_key():
    """Test if API key is configured."""
    print("\n🔑 Testing API key configuration...")
    
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if api_key:
        print("  ✅ ANTHROPIC_API_KEY is set")
        return True
    else:
        print("  ⚠️  ANTHROPIC_API_KEY not set (required for AI features)")
        print("  💡 Run: export ANTHROPIC_API_KEY='your_key_here'")
        return False

def test_course_materials():
    """Test course materials organization."""
    print("\n📚 Testing course materials...")
    
    materials_dir = Path("course_materials")
    if not materials_dir.exists():
        print("  ❌ course_materials directory not found")
        return False
    
    subdirs = ["formula_sheets", "instructions", "resources", "sample_assignments", "syllabus_and_schedule"]
    for subdir in subdirs:
        subdir_path = materials_dir / subdir
        if subdir_path.exists():
            print(f"  ✅ {subdir}/")
        else:
            print(f"  ⚠️  {subdir}/ not found")
    
    # Check for formula sheets
    formula_dir = materials_dir / "formula_sheets"
    if formula_dir.exists():
        formula_files = list(formula_dir.glob("*.md"))
        print(f"  ✅ Found {len(formula_files)} formula sheet files")
    
    return True

def test_design_tokens():
    """Test design tokens file."""
    print("\n🎨 Testing design tokens...")
    
    try:
        with open("tokens.json", "r") as f:
            tokens = json.load(f)
        
        required_sections = ["colors", "typography", "spacing", "borderRadius", "shadows"]
        for section in required_sections:
            if section in tokens:
                print(f"  ✅ {section} section present")
            else:
                print(f"  ❌ {section} section missing")
                return False
        
        print("  ✅ Design tokens file is valid")
        return True
    except Exception as e:
        print(f"  ❌ Error reading tokens.json: {e}")
        return False

def test_html_files():
    """Test HTML files for basic structure."""
    print("\n🌐 Testing HTML files...")
    
    html_files = [
        "index.html",
        "tutor.html",
        "reference.html",
        "calendar_study_system.html",
        "web_study_helper.html"
    ]
    
    for html_file in html_files:
        try:
            with open(html_file, "r") as f:
                content = f.read()
                if "<!DOCTYPE html>" in content and "<title>" in content:
                    print(f"  ✅ {html_file} - Valid HTML structure")
                else:
                    print(f"  ❌ {html_file} - Invalid HTML structure")
        except Exception as e:
            print(f"  ❌ {html_file} - Error reading file: {e}")
    
    return True

def test_vite_config():
    """Test Vite configuration."""
    print("\n⚙️  Testing Vite configuration...")
    
    try:
        with open("vite.config.js", "r") as f:
            content = f.read()
            if "defineConfig" in content and "input" in content:
                print("  ✅ vite.config.js is valid")
                return True
            else:
                print("  ❌ vite.config.js is invalid")
                return False
    except Exception as e:
        print(f"  ❌ Error reading vite.config.js: {e}")
        return False

def test_package_json():
    """Test package.json."""
    print("\n📦 Testing package.json...")
    
    try:
        with open("package.json", "r") as f:
            package = json.load(f)
        
        required_fields = ["name", "version", "scripts", "devDependencies"]
        for field in required_fields:
            if field in package:
                print(f"  ✅ {field} field present")
            else:
                print(f"  ❌ {field} field missing")
                return False
        
        print("  ✅ package.json is valid")
        return True
    except Exception as e:
        print(f"  ❌ Error reading package.json: {e}")
        return False

def run_all_tests():
    """Run all tests and provide summary."""
    print("🧪 MAT 143 Tutor System Test Suite")
    print("=" * 50)
    
    tests = [
        ("File Structure", test_file_structure),
        ("Python Dependencies", test_python_dependencies),
        ("API Key", test_api_key),
        ("Course Materials", test_course_materials),
        ("Design Tokens", test_design_tokens),
        ("HTML Files", test_html_files),
        ("Vite Config", test_vite_config),
        ("Package.json", test_package_json)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"  ❌ {test_name} test failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results Summary")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your system is ready to use.")
        print("\n🚀 Next steps:")
        print("1. Set your ANTHROPIC_API_KEY if not already done")
        print("2. Run 'npm run dev' to start development server")
        print("3. Open index.html in your browser")
        print("4. Or run 'python3 tutor_system/enhanced_tutor.py' for AI features")
    else:
        print("⚠️  Some tests failed. Please fix the issues above before proceeding.")
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
