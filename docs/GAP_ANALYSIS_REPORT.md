# Content Gap Analysis Report

**Date**: October 16, 2025  
**Status**: Critical gaps identified  
**Priority**: Address P0 gaps immediately

---

## 🚨 Critical Findings

### **ALL ENG 111 Essay Pages Are Missing!**

The following pages are linked from `english_materials.html` but **DO NOT EXIST**:

**Essay Guide Pages** (0 of 8 exist):
- ❌ `english/essay-1-guide.html`
- ❌ `english/essay-1-rubric.html`
- ❌ `english/essay-2-guide.html`
- ❌ `english/essay-2-rubric.html`
- ❌ `english/essay-3-guide.html`
- ❌ `english/essay-3-rubric.html`
- ❌ `english/essay-4-guide.html`
- ❌ `english/essay-4-rubric.html`

**Writing Resource Pages** (0 of 5 exist):
- ❌ `english/mla-basics.html`
- ❌ `english/in-text-citations.html`
- ❌ `english/works-cited.html`
- ❌ `english/plagiarism-guide.html`
- ❌ `english/paraphrasing.html`

**Impact**: **13 broken links** on writing coach page - students click and get 404 errors!

---

## ⚠️ MAT 143 Gaps

### Emoji Accessibility Not Applied to Most Chapters

Only `chapter-1.html` has the new ADHD-friendly icon system:
- ❌ chapter-3.html - Still has emoji headings
- ❌ chapter-4.html - Still has emoji headings (📊, 📚, 🔢, 🎯)
- ❌ chapter-5.html - Not checked yet
- ❌ chapter-6.html - Still has emoji headings (📊, 🔢, 🎯)
- ❌ chapter-7.html - Not checked yet
- ❌ chapter-8.html - Not checked yet
- ❌ chapter-10.html - Not checked yet
- ❌ chapter-11.html - Not checked yet
- ❌ chapter-13.html - Still has emoji headings (🗳️, 📊)

### ADHD Features Not on Most Chapters

Only `chapter-1.html` has all ADHD accessibility scripts:
- ❌ chapter-3 through chapter-13 missing progress tracking
- ❌ chapter-3 through chapter-13 missing achievement system
- ❌ chapter-3 through chapter-13 missing break system
- ❌ chapter-3 through chapter-13 missing focus mode
- ❌ chapter-3 through chapter-13 missing reading mode

### Time Estimates Inconsistent

- ✅ chapter-1.html - Has clock icons with estimates (15 min, 20 min, 25 min)
- ❌ chapter-4.html - Has text "15 min" but no icon/ARIA label
- ❌ Other chapters - Not verified

---

## 📅 Due Date Gaps

### What We Have
From `index.html` and `calendar.html`:
- ✅ Chapter 7 Hawkes: "Due Wednesday, Nov 6"
- ✅ Test dates (all 4 tests have week ranges)
- ✅ Essay 3: "November 15, 2025"
- ✅ Essay 4: "December 8, 2025"
- ✅ EVA: "Friday, August 29, 2025"
- ✅ Withdrawal: "Friday, September 26, 2025"

### What's Missing
**MAT 143**:
- ❌ Chapter 1 Hawkes due date
- ❌ Chapter 4 Hawkes due date
- ❌ Chapter 5 Hawkes due date
- ❌ Chapter 6 Hawkes due date
- ❌ Chapter 10 Hawkes due date
- ❌ Chapter 11 Hawkes due date
- ❌ Chapter 13 Hawkes due date
- ❌ Lab assignment dates (unknown if labs exist)
- ❌ Weekly attendance due day
- ❌ Signature assignment specific date

**ENG 111**:
- ❌ EVA Quiz due date
- ❌ Critical Reading Discussion due date
- ❌ Plagiarism Quiz due date
- ❌ MLA Citations Quiz due date
- ❌ Essay 1 due date (marked "Completed" but no date shown)
- ❌ Essay 2 due date (marked "Completed" but no date shown)
- ❌ Essay 2 rough draft date
- ❌ Essay 2 peer review date
- ❌ Essay 3 rough draft date
- ❌ Essay 4 rough draft date

---

## 🔍 Formula Completeness Gaps

### Missing from formula_lookup.html

**Chapter 1** (Thinking Mathematically):
- May not have traditional formulas - verify

**Chapter 5** (Functions):
- ❌ Linear function formulas (y = mx + b, slope)
- ❌ Exponential growth formula (y = a(1+r)^t)
- ❌ Exponential decay formula (y = a(1-r)^t)
- ❌ Domain and range concepts

**Chapter 13** (Voting & Apportionment):
- ❌ Standard Divisor formula
- ❌ Standard Quota formula
- ❌ Modified divisor methods
- Note: Formulas were added per STATUS.md but not in formula_lookup.html?

---

## 📱 Broken Links Summary

### From english_materials.html

**Essay 3 section** links to:
- `english/essay-3-guide.html` - ❌ BROKEN (404)
- `english/essay-3-rubric.html` - ❌ BROKEN (404)

**MLA Citation Guide section** links to:
- `english/mla-basics.html` - ❌ BROKEN (404)
- `english/in-text-citations.html` - ❌ BROKEN (404)
- `english/works-cited.html` - ❌ BROKEN (404)

**Avoiding Plagiarism section** links to:
- `english/plagiarism-guide.html` - ❌ BROKEN (404)
- `english/paraphrasing.html` - ❌ BROKEN (404)

**Total broken links from english_materials.html**: 7 links

### Potential Issues (Need Testing)
- Chapter navigation links from tutor.html (need to verify all work)
- Formula lookup navigation links
- Calendar event links
- Course materials links

---

## 🎯 Priority Classification

### P0 - CRITICAL (Fix Immediately)
1. **Create missing essay guide pages** (7 pages)
   - Essay 3 & 4 are current/upcoming - URGENT
   - Students clicking links get 404 errors
   - Impact: Blocks student work on current assignments

2. **Audit Chapters 6 & 7**
   - Test 3 is Nov 3-7 (less than 3 weeks!)
   - Must be complete and accurate
   - Need to add due dates if missing

3. **Fix broken links on english_materials.html**
   - Either create pages or update links
   - Current state damages credibility

### P1 - HIGH (This Week)
1. **Add ADHD features to all chapters**
   - Only chapter-1 has full features
   - 9 chapters missing progress tracking, achievements, breaks

2. **Fix emoji accessibility on remaining chapters**
   - 9 chapters still have emoji headings
   - Inconsistent with updated pages

3. **Add specific due dates throughout**
   - Hawkes deadlines on chapter pages
   - Calendar specific dates
   - Essay draft deadlines

4. **Verify formula accuracy**
   - Cross-check against known-good sources
   - Add missing Chapter 5 & 13 formulas to lookup

### P2 - MEDIUM (Next Week)
1. **Chapters 3 & 8 decision**
   - Investigate if covered
   - Remove or mark as supplementary

2. **Create remaining essay resources**
   - MLA guide pages
   - Plagiarism guide pages

3. **Enhance chapter content**
   - More practice problems
   - Video links
   - Study tips

### P3 - LOW (Future)
1. Detailed lesson subsections (noted as deferred in STATUS.md)
2. Additional practice problems
3. Flashcard system
4. Study guides per test

---

## 📊 Gap Summary Statistics

| Category | Exists | Missing | % Complete |
|----------|--------|---------|------------|
| **MAT 143 Chapters** | 10 | 0 | 100% (but 2 unconfirmed) |
| **Chapter Content** | Varies | TBD after audit | ~70% estimated |
| **ENG 111 Essay Guides** | 0 | 8 | 0% ⚠️ |
| **ENG 111 Resource Pages** | 0 | 5 | 0% ⚠️ |
| **Formula Lookup Sections** | 5 chapters | 3 chapters | 63% |
| **Specific Due Dates** | ~10 | ~25+ | ~30% |
| **ADHD Features Applied** | 4 pages | 9 chapter pages | ~30% |
| **Emoji Accessibility** | 5 pages | 9 chapter pages | ~35% |

---

## 🔧 Recommended Action Plan

### Immediate (Today - 4 hours)

1. **Create Essay 3 & 4 Pages** (P0 - URGENT)
   - essay-3-guide.html
   - essay-3-rubric.html
   - essay-4-guide.html
   - essay-4-rubric.html
   - Use ENG 111 course schedule for requirements
   - Include clear due dates

2. **Audit Chapters 6 & 7** (P0 - Test Nov 3-7)
   - Verify all formulas present
   - Check practice problems adequate
   - Confirm test date prominently shown
   - Fix emojis
   - Add ADHD scripts

3. **Test All Links** (P0)
   - Systematically click every link
   - Document broken links
   - Fix or create placeholder pages

### This Week (12 hours)

4. **Apply ADHD Features to All Chapters** (P1)
   - Copy script includes from chapter-1.html
   - Add to chapters 3-13
   - Verify all features work

5. **Fix Emojis on All Chapters** (P1)
   - Replace with Lucide icons
   - Make aria-hidden
   - Match chapter-1 style

6. **Create Essay 1 & 2 Pages** (P1)
   - essay-1-guide.html + rubric
   - essay-2-guide.html + rubric
   - For completeness/review

7. **Add Specific Due Dates** (P1)
   - Extract from syllabi
   - Add to chapter pages
   - Update calendar

### Next Week (8 hours)

8. **Create Writing Resource Pages** (P2)
   - Convert existing .md files to HTML
   - Create mla-basics.html
   - Create plagiarism-guide.html
   - Use existing content from english/ directory

9. **Verify Formula Accuracy** (P1)
   - Check each formula against source
   - Add Chapter 5 & 13 formulas
   - Cross-reference chapter pages

10. **Chapters 3 & 8 Resolution** (P2)
    - Research if covered
    - Remove or repurpose
    - Update navigation

---

## ✅ Completion Criteria

**Audit complete when**:
- [ ] Every chapter reviewed and documented
- [ ] Every link tested
- [ ] Every gap catalogued
- [ ] Priorities assigned

**Content complete when**:
- [ ] All essay pages created
- [ ] All broken links fixed
- [ ] All chapters have ADHD features
- [ ] All chapters have proper icons
- [ ] All dates specific and accurate
- [ ] No 404 errors anywhere

---

**Status**: Analysis complete, ready to execute fixes  
**Next**: Begin creating missing essay pages

