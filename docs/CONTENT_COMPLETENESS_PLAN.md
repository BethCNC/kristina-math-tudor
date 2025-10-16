# Content Completeness & Accuracy Audit Plan

**Based on**: Full codebase review, STATUS.md, BUILD_NOTES.md, syllabus materials  
**Date**: October 16, 2025  
**Objective**: Ensure 100% syllabus coverage with clear due dates for all assignments

---

## 📊 Current State (From Codebase Analysis)

### MAT 143 Coverage
**Chapters with pages**: 1, 3, 4, 5, 6, 7, 8, 10, 11, 13 (10 files)  
**Required by syllabus**: 1, 4, 5, 6, 7, 10, 11, 13 (8 chapters)  
**Test mapping confirmed in code**:
- Test 1: Chapters 1 & 13 ✅
- Test 2: Chapters 4 & 5 ✅
- Test 3: Chapters 6 & 7 ✅
- Test 4: Chapters 10 & 11 ✅

**Status per STATUS.md**: "All 8 chapters covered" ✅

### ENG 111 Coverage
**Current**: 4 essay cards on `english_materials.html`  
**English resources found**: 7 markdown files with writing guides  
**Missing**: Individual essay guide pages (currently links point to pages that may not exist)

### Known from Documentation
- Per STATUS.md: Project marked "PRODUCTION READY" but noted "lesson subsections DEFERRED"
- Per BUILD_NOTES.md: Some chapters have CSS parsing issues (5, 10, 11 disabled in Vite)
- Per CLAUDE.md: Chapters 3 & 8 exist but not mentioned in official test schedule

---

## 🎯 Three-Phase Audit Plan

### Phase 1: Inventory & Verification (Start Here)

**Goal**: Document exactly what exists and what's missing

#### 1.1 Create Content Inventory
- [x] List all chapter HTML files ✅ (10 found)
- [ ] Check each chapter for:
  - Chapter overview present
  - Formulas section complete
  - Practice problems included
  - Test information shown
  - Due dates visible
- [ ] List all English resource files
- [ ] Check which essay pages exist vs which are linked
- [ ] Verify all links on main pages

#### 1.2 Verify Chapter Coverage
**Decision needed on Chapters 3 & 8**:
- CLAUDE.md says "exists from design iterations"
- Not in official test schedule
- Action: Mark as "Supplementary/Optional" or remove

**Chapters confirmed needed (8)**:
1, 4, 5, 6, 7, 10, 11, 13

#### 1.3 Extract Actual Due Dates
From course schedule and current pages:
- MAT 143: Test dates (have ranges)
- MAT 143: Hawkes deadlines (need specifics)
- ENG 111: Essay due dates (have 2 of 4)
- Weekly assignments (need pattern)

---

### Phase 2: Gap Analysis & Content Audit

**Goal**: Identify missing content and inaccuracies

#### 2.1 Audit Each MAT 143 Chapter

**Template checklist per chapter**:
- [ ] Overview paragraph exists
- [ ] "Test X Coverage" alert present with date
- [ ] All key formulas listed
- [ ] Formulas match formula_lookup.html
- [ ] Minimum 3 practice problems
- [ ] Practice solutions expandable
- [ ] Hawkes Learning link present
- [ ] Due date shown (if applicable)
- [ ] Time estimate per section (ADHD feature)
- [ ] ADHD accessibility scripts included

**Priority order** (upcoming first):
1. Chapter 6 & 7 (Test 3 is Nov 3-7 - URGENT)
2. Chapter 10 & 11 (Test 4 upcoming)
3. Chapter 1 & 13 (Test 1 passed, but for review)
4. Chapter 4 & 5 (Test 2 passed, but for review)

#### 2.2 Audit ENG 111 Content

**Check english_materials.html**:
- [ ] All 4 essays listed with status
- [ ] Due dates shown for each essay
- [ ] Links to guide pages work (or note if broken)
- [ ] Links to rubric pages work (or note if broken)

**Check english/ directory**:
- [ ] Inventory all .md and .html files
- [ ] Determine which are course resources vs external saved pages
- [ ] Identify if essay guides exist in some form
- [ ] Check if rubrics exist

#### 2.3 Calendar Completeness Check

Current calendar.html shows:
- ✅ Semester dates (Aug 18 - Dec 12)
- ✅ EVA deadline (Aug 29)
- ✅ Withdrawal deadline (Sept 26)
- ✅ 4 test date ranges
- ✅ Signature assignment weeks (12-15)
- ⚠️ Missing specific weekly Hawkes deadlines
- ⚠️ Missing lab assignment dates
- ⚠️ Missing ENG 111 quiz/discussion dates
- ⚠️ Using "Week X" instead of specific dates in some places

---

### Phase 3: Fill Gaps & Enhance

**Goal**: Create missing content and add specific dates

#### 3.1 Standardize Due Date Format

**Chosen format** (ADHD-friendly):
```
Due: Friday, November 15, 2025 at 11:59 PM
```

**Apply to**:
- All test date ranges → Convert to specific days
- All Hawkes assignments → Add "Due Wednesday" or specific day
- All essay deadlines → Full date with time
- Calendar entries → Specific dates not "Week X"

#### 3.2 Create Missing ENG 111 Pages

**If essay guide pages don't exist**, create:
- `english/essay-1-guide.html`
- `english/essay-1-rubric.html`
- `english/essay-2-guide.html`
- `english/essay-2-rubric.html`
- `english/essay-3-guide.html`
- `english/essay-3-rubric.html`
- `english/essay-4-guide.html`
- `english/essay-4-rubric.html`

**If writing resource pages don't exist**, create:
- `english/mla-basics.html`
- `english/in-text-citations.html`
- `english/works-cited.html`
- `english/plagiarism-guide.html`
- `english/paraphrasing.html`

#### 3.3 Enhance Chapter Pages

For chapters that need more detail:
- Add section-by-section breakdowns
- Add more practice problems
- Add real-world examples
- Add links to related formulas
- Add "Study Tips" specific to chapter

#### 3.4 Update Calendar with All Dates

**Extract from ENG 111 schedule**, add to calendar:
- Week 1: EVA Quiz + Critical Reading Discussion
- Week 2: Plagiarism Quiz + MLA Citations Quiz
- Week 3: Essay 2 Rough Draft
- Week 4: Essay 2 Peer Review
- Week 5: Essay 3 Assignment
- Week 6: Essay 3 Rough Draft
- Week 7: Essay 3 Final + Research Paper assigned
- Week 8: Research Paper Final

**For MAT 143**, determine pattern and add:
- Weekly attendance assignment day
- Hawkes Learning deadline per chapter
- Lab assignment dates (if any)

---

## 🔍 Specific Action Items

### Immediate Actions (Can Start Now)

#### Action 1: Inventory Existing Content ✅
Create `docs/CONTENT_INVENTORY.md` with:
- Complete list of all HTML pages
- Status of each (complete/incomplete)
- Which links work/broken
- What content exists in english/ directory

#### Action 2: Test All Links
Click through entire app systematically:
- Every nav link
- Every chapter card
- Every essay link
- Every external resource
- Document broken links in inventory

#### Action 3: Chapter 6 & 7 Priority Audit
Since Test 3 is Nov 3-7 (UPCOMING):
- Verify chapter-6.html has all Personal Finance content
- Verify chapter-7.html has all Measurement content
- Check formulas complete
- Verify practice problems adequate
- Add prominent "Test 3: Nov 3-7" reminder

#### Action 4: Formula Accuracy Check
Cross-reference formula_lookup.html against:
- Chapter 4 formulas
- Chapter 5 formulas
- Chapter 6 formulas (interest formulas - recently added)
- Chapter 7 formulas (conversions)
- Chapter 10 formulas (probability)
- Chapter 11 formulas (statistics)
- Chapter 13 formulas (apportionment - recently added)

---

## 📋 Deliverables

### Documents to Create
1. **CONTENT_INVENTORY.md** - What exists, what's missing
2. **GAP_ANALYSIS_REPORT.md** - Specific gaps found
3. **DUE_DATE_MASTER_LIST.md** - Every assignment with exact dates
4. **LINK_VERIFICATION_REPORT.md** - All links tested
5. **ACCURACY_VERIFICATION_REPORT.md** - Formulas checked

### Pages to Create/Update
1. Missing essay guide pages (up to 10 pages)
2. Updated chapter pages with due dates
3. Updated calendar with specific dates
4. Chapter 3 & 8 decision (keep/remove/mark optional)

---

## ✅ Success Criteria

**Audit complete when**:
- [ ] Every chapter page reviewed for accuracy
- [ ] Every formula verified against textbook/syllabus
- [ ] Every link tested (no 404s)
- [ ] Every assignment has specific due date
- [ ] Calendar matches syllabus 100%
- [ ] All gaps documented and prioritized
- [ ] Missing content created or marked as TODO

**Content complete when**:
- [ ] All 8 required MAT 143 chapters fully developed
- [ ] All 4 ENG 111 essays have guides + rubrics
- [ ] All dates specific (not "Week X")
- [ ] No broken links
- [ ] All formulas accurate
- [ ] All practice problems have solutions

---

## 🚀 Execution Strategy

Since I can proceed without additional user input (using existing course materials):

**Immediate (Today)**:
1. Create content inventory
2. Test all links
3. Audit high-priority chapters (6, 7)
4. Extract all dates from existing materials

**Next (This Week)**:
1. Fill identified gaps
2. Create missing essay pages
3. Update calendar with specific dates
4. Verify all formulas

**Final (Quality Check)**:
1. Test every link again
2. Proofread all content
3. Verify all dates
4. Create completion report

---

**Ready to begin systematic audit and gap-filling!**

