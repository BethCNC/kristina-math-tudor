# ADHD Features Testing Guide

**Quick checklist to verify all accessibility features are working correctly**

---

## ✅ Quick Visual Check (2 minutes)

Open the app in your browser and look for these:

### Dashboard (`index.html`)
- [ ] Headings use icons instead of emojis (📊 → icon)
- [ ] "Focus" button visible in bottom-left corner
- [ ] "Aa" reading controls button visible in top-left
- [ ] Welcome message says "Welcome Back, Kristina!" with waving hand

### Calendar Page (`calendar.html`)
- [ ] Headings use icons instead of emojis
- [ ] Filter buttons look clickable (not tiny)
- [ ] Week cards have consistent spacing

### Chapter Pages (`chapter-1.html`, etc.)
- [ ] Headings use icons instead of emojis
- [ ] Time estimates visible on each section (15 min, 20 min, etc.)
- [ ] Progress bars visible at top

---

## 🧪 Feature Testing (10 minutes)

### Test 1: Focus Mode
1. Open any chapter page
2. Look for "Focus" button in bottom-left corner
3. Click it
4. **Expected**: Navigation/footer disappear, button says "Exit"
5. Click "Exit"
6. **Expected**: Navigation/footer reappear

**✅ Pass if**: Elements hide/show correctly

---

### Test 2: Reading Mode
1. Open any page
2. Click "Aa" icon in top-left
3. Panel should open with controls
4. Click **A+** twice
5. **Expected**: Text gets larger
6. Click **Reset**
7. **Expected**: Text returns to normal size

**✅ Pass if**: Text size changes visibly

---

### Test 3: Mobile Menu (Desktop)
1. Resize browser to mobile width (< 768px)
2. Click hamburger menu (☰) in top-right
3. **Expected**: Menu slides down, overlay appears
4. Press **Escape** key
5. **Expected**: Menu closes

**✅ Pass if**: Menu opens/closes, overlay shows

---

### Test 4: Mobile Menu Focus Trap (Keyboard)
1. Resize browser to mobile width
2. Use **Tab** key to navigate to menu button
3. Press **Enter** to open menu
4. Press **Tab** repeatedly
5. **Expected**: Focus stays within menu items
6. Press **Escape**
7. **Expected**: Menu closes, focus returns to button

**✅ Pass if**: Focus doesn't leave menu while open

---

### Test 5: Progress Tracking
1. Open `chapter-1.html`
2. Click "Review Lesson" on Section 4.1
3. Watch bottom-right corner for ~2 seconds
4. **Expected**: "Progress saved" indicator appears briefly
5. Close tab
6. Reopen `index.html`
7. **Expected**: "Continue Learning" card appears on dashboard

**✅ Pass if**: Progress saves and dashboard shows resume option

---

### Test 6: Achievement System
1. Open browser console (F12)
2. Type: `progressTracker.updateSection('chapter-4', '4-1', 100)`
3. Press Enter
4. **Expected**: "Section Complete!" toast appears in top-right
5. Toast should auto-dismiss after 4 seconds

**✅ Pass if**: Toast appears and disappears

---

### Test 7: Break System
1. Open any chapter page
2. Open browser console (F12)
3. Type: `breakSystem.breakInterval = 0.1` (10% of 1 minute = 6 seconds)
4. Press Enter
5. Type: `breakSystem.startStudying()`
6. Press Enter
7. Wait 6 seconds
8. **Expected**: Break reminder appears on page

**✅ Pass if**: Break section appears after countdown

---

### Test 8: Reduced Motion
1. **macOS**: System Preferences → Accessibility → Display → Reduce motion
2. **Windows**: Settings → Ease of Access → Display → Show animations
3. Enable reduced motion in your OS
4. Hover over cards/buttons
5. **Expected**: No movement, no transforms

**✅ Pass if**: Elements don't move on hover

---

### Test 9: Touch Targets (Mobile)
1. Open on actual mobile device or device emulator
2. Try tapping all badges, buttons, filter controls
3. **Expected**: Easy to tap without missing

**✅ Pass if**: All elements tappable without precision

---

### Test 10: Keyboard Navigation
1. Use **Tab** key to navigate through `index.html`
2. **Expected**: Blue outline shows where you are
3. Press **Enter** on links
4. **Expected**: Links activate
5. Tab to "Skip to main content" at top
6. Press **Enter**
7. **Expected**: Focus jumps to main content

**✅ Pass if**: Can navigate entire page with keyboard

---

## 🎨 Visual Regression Check

### Before/After Comparison

Check these pages look correct:

- [ ] `index.html` - Dashboard has clean icons (no emojis in headings)
- [ ] `calendar.html` - Calendar entries well-spaced
- [ ] `tutor.html` - Math tutor has clean icons
- [ ] `english_materials.html` - Writing coach looks professional
- [ ] `formula_lookup.html` - Formulas say "Interest" not "Host Groteskest"
- [ ] `chapter-1.html` - Sections show time estimates

---

## 🔬 Browser Compatibility

Test in multiple browsers:

### Chrome/Edge (Chromium)
- [ ] All features work
- [ ] Icons render correctly
- [ ] Progress saves
- [ ] localStorage accessible

### Firefox
- [ ] All features work
- [ ] Icons render correctly
- [ ] Progress saves
- [ ] localStorage accessible

### Safari (macOS/iOS)
- [ ] All features work
- [ ] Icons render correctly
- [ ] Progress saves
- [ ] localStorage accessible

---

## 📱 Device Testing

### Desktop
- [ ] All features accessible
- [ ] Layout looks good
- [ ] No horizontal scroll
- [ ] Focus mode works

### Tablet (iPad, Android)
- [ ] Touch targets adequate
- [ ] Menu works correctly
- [ ] Landscape and portrait orientations
- [ ] Reading mode controls accessible

### Mobile (iPhone, Android)
- [ ] Touch targets easy to tap
- [ ] Text readable without zoom
- [ ] Formulas don't overflow
- [ ] Mobile menu works
- [ ] Focus/Reading controls don't overlap

---

## ♿ Screen Reader Testing

### VoiceOver (macOS/iOS)
1. Enable VoiceOver (Cmd + F5)
2. Navigate through pages
3. **Check**:
   - [ ] Headings announced correctly (no emoji noise)
   - [ ] Icons marked as decorative (aria-hidden)
   - [ ] Buttons have clear labels
   - [ ] Progress updates announced
   - [ ] Achievement toasts announced

### NVDA (Windows)
1. Start NVDA
2. Navigate through pages
3. **Check**: Same as above

**✅ Pass if**: Navigation is clear, no confusing announcements

---

## 🐛 Common Issues & Fixes

### Issue: "Progress saved" doesn't appear
**Fix**: Check browser console for errors, verify localStorage not blocked

### Issue: Scripts not loading
**Fix**: Check file paths, ensure files exist in `src/js/` directory

### Issue: Icons show as empty boxes
**Fix**: Check internet connection (Lucide loads from CDN)

### Issue: Styles not applying
**Fix**: Hard refresh (Cmd/Ctrl + Shift + R)

### Issue: Focus mode doesn't hide elements
**Fix**: Check if body has class `focus-mode-active`, verify CSS loaded

---

## 📊 Performance Check

### Load Time
- [ ] Pages load in < 2 seconds
- [ ] No flash of unstyled content
- [ ] Icons load quickly

### Responsiveness
- [ ] Buttons respond immediately
- [ ] No lag when clicking
- [ ] Smooth animations (if motion allowed)

### Memory Usage
- [ ] No memory leaks after extended use
- [ ] localStorage doesn't grow excessively
- [ ] Console shows no errors

---

## ✅ Acceptance Criteria

All features pass if:

1. ✅ No JavaScript errors in console
2. ✅ All interactive elements have 44×44px minimum size
3. ✅ Keyboard navigation works throughout
4. ✅ Screen readers don't announce decorative elements
5. ✅ Progress saves and restores correctly
6. ✅ Break system triggers after interval
7. ✅ Achievement toasts appear on completions
8. ✅ Focus mode hides/shows elements correctly
9. ✅ Reading mode adjusts text correctly
10. ✅ No typos or duplicate classes in formula_lookup.html

---

## 🎓 User Acceptance Testing

### Ask Kristina (or ADHD students):

1. **Is the app less overwhelming now?**
   - Focus mode helpful?
   - Break reminders appreciated?

2. **Do the features help or hinder?**
   - Too many notifications?
   - Progress tracking useful?
   - Time estimates accurate?

3. **What's still difficult?**
   - Any confusing elements?
   - Missing features?
   - Suggestions for improvement?

---

## 📝 Testing Log Template

Use this to track your testing:

```
Date: __________
Tester: __________
Browser: __________
Device: __________

Feature Tests:
[ ] Focus Mode: Pass / Fail / Notes: ________________
[ ] Reading Mode: Pass / Fail / Notes: ________________
[ ] Progress Tracking: Pass / Fail / Notes: ________________
[ ] Break System: Pass / Fail / Notes: ________________
[ ] Achievement Toasts: Pass / Fail / Notes: ________________
[ ] Mobile Menu: Pass / Fail / Notes: ________________
[ ] Touch Targets: Pass / Fail / Notes: ________________
[ ] Keyboard Navigation: Pass / Fail / Notes: ________________
[ ] Screen Reader: Pass / Fail / Notes: ________________
[ ] Reduced Motion: Pass / Fail / Notes: ________________

Overall: Pass / Fail
Issues Found: ________________________________
Recommendations: ________________________________
```

---

## 🚀 Quick Production Checklist

Before deploying:

- [ ] All HTML pages have emoji fixes
- [ ] All pages load necessary scripts
- [ ] CSS file includes all new components
- [ ] No console errors on any page
- [ ] Test on real mobile device
- [ ] Test with screen reader
- [ ] Test keyboard navigation
- [ ] Verify localStorage works
- [ ] Check all time estimates accurate
- [ ] Proofread all user-facing text

---

**Happy Testing!** 🎉

*If all tests pass, the ADHD accessibility implementation is complete and ready for use!*

