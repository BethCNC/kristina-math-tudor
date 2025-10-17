# UI Semantic Color & Calendar Enhancement Plan

## Current Problems

1. **Inconsistent deadline urgency colors** across pages
2. **Calendar exists but isn't interactive** - no filtering, no full 16-week view
3. **Semantic meaning unclear** - when to use red vs orange vs blue
4. **No visual deadline system** that works universally

## Solution: Universal Semantic Color System

### Color Definitions (Already in CSS)
```css
--danger-red: #dc2626;       /* 0-3 days (URGENT) */
--warning-orange: #d97706;   /* 4-7 days (THIS WEEK) */
--primary-blue: #1e40af;     /* 8-14 days (UPCOMING) */
--success-green: #059669;    /* Completed */
--neutral-gray-light: #6b7280; /* Future (14+ days) */
```

### Deadline Urgency Classes to Add

```css
/* Deadline Cards with Semantic Colors */
.deadline-urgent {
  border-left: 4px solid var(--danger-red);
  background: linear-gradient(135deg, #fef2f2 0%, var(--white) 100%);
}

.deadline-warning {
  border-left: 4px solid var(--warning-orange);
  background: linear-gradient(135deg, #fff7ed 0%, var(--white) 100%);
}

.deadline-upcoming {
  border-left: 4px solid var(--primary-blue);
  background: linear-gradient(135deg, #f0f9ff 0%, var(--white) 100%);
}

.deadline-completed {
  border-left: 4px solid var(--success-green);
  background: linear-gradient(135deg, #ecfdf5 0%, var(--white) 100%);
  opacity: 0.6;
}

.deadline-future {
  border-left: 4px solid var(--neutral-gray-light);
  background: var(--white);
}
```

### Badge Color Classes

```css
.badge-urgent {
  background-color: var(--danger-red);
  color: var(--white);
}

.badge-warning {
  background-color: var(--warning-orange);
  color: var(--white);
}

.badge-upcoming {
  background-color: var(--primary-blue);
  color: var(--white);
}

.badge-completed {
  background-color: var(--success-green);
  color: var(--white);
}

.badge-future {
  background-color: var(--neutral-gray-light);
  color: var(--white);
}
```

## Calendar Enhancements Needed

### 1. Full 16-Week Calendar Grid (Aug 18 - Dec 12)

**Current:** Only shows November 2025
**Needed:** Show all 16 weeks with all deadlines

### 2. Calendar Filtering System

Add filter buttons:
- **All Deadlines** (default)
- **MAT 143 Only**
- **ENG 111 Only**
- **Tests Only**
- **Essays Only**
- **Hawkes Learning**
- **Attendance**

### 3. Calendar Legend

Add visual legend:
```html
<div class="flex gap-4 mb-6">
  <div class="flex items-center gap-2">
    <div style="width: 12px; height: 12px; background: var(--danger-red); border-radius: 50%;"></div>
    <span>Urgent (0-3 days)</span>
  </div>
  <div class="flex items-center gap-2">
    <div style="width: 12px; height: 12px; background: var(--warning-orange); border-radius: 50%;"></div>
    <span>This Week (4-7 days)</span>
  </div>
  <div class="flex items-center gap-2">
    <div style="width: 12px; height: 12px; background: var(--primary-blue); border-radius: 50%;"></div>
    <span>Upcoming (8-14 days)</span>
  </div>
  <div class="flex items-center gap-2">
    <div style="width: 12px; height: 12px; background: var(--success-green); border-radius: 50%;"></div>
    <span>Completed</span>
  </div>
</div>
```

### 4. Dynamic Urgency Updates (JavaScript)

Calculate days until deadline and apply appropriate class:

```javascript
function getDeadlineUrgency(deadlineDate) {
  const now = new Date();
  const deadline = new Date(deadlineDate);
  const daysUntil = Math.ceil((deadline - now) / (1000 * 60 * 60 * 24));
  
  if (daysUntil < 0) return 'completed'; // Past due
  if (daysUntil <= 3) return 'urgent';    // 0-3 days
  if (daysUntil <= 7) return 'warning';   // 4-7 days
  if (daysUntil <= 14) return 'upcoming'; // 8-14 days
  return 'future';                        // 14+ days
}

function updateDeadlineColors() {
  document.querySelectorAll('[data-deadline]').forEach(element => {
    const deadlineDate = element.getAttribute('data-deadline');
    const urgency = getDeadlineUrgency(deadlineDate);
    
    // Remove all urgency classes
    element.classList.remove('deadline-urgent', 'deadline-warning', 'deadline-upcoming', 'deadline-future', 'deadline-completed');
    
    // Add appropriate class
    element.classList.add(`deadline-${urgency}`);
  });
}

// Run on page load and every hour
updateDeadlineColors();
setInterval(updateDeadlineColors, 3600000);
```

## Implementation Plan

### Phase 1: Add Semantic Color Classes to CSS (15 min)
- Add deadline urgency classes
- Add badge urgency classes
- Verify color contrast for WCAG compliance

### Phase 2: Update Next Due Widget (15 min)
- Apply semantic colors to widget items
- Show urgency indicators
- Update badge colors dynamically

### Phase 3: Enhance Calendar Page (1 hour)
- Create full 16-week view
- Add filtering system
- Add interactive legend
- Implement dynamic urgency coloring with JavaScript

### Phase 4: Apply Semantic System Site-Wide (30 min)
- Update `index.html` deadline cards
- Update `deadlines.html` master tracker
- Update chapter pages with Hawkes alerts
- Ensure consistency across all 20+ pages

### Phase 5: Testing (30 min)
- Test urgency updates at different dates
- Test calendar filtering
- Verify mobile responsiveness
- Check color accessibility

## All Deadlines with Semantic Colors

### URGENT (0-3 days) - RED
- Hawkes Learning: Nov 3 (TEST 3 DEPENDENCY!)
- Test 3: Nov 3-7

### WARNING (4-7 days) - ORANGE
- Essay 3: Nov 15

### UPCOMING (8-14 days) - BLUE
- Attendance Week 13: Nov 18-22
- Attendance Week 14: Nov 25-29

### FUTURE (14+ days) - GRAY
- Final Exams: Dec 8-12
- Signature Assignment: Dec 8

## Success Criteria
- [ ] Semantic color system added to CSS
- [ ] Calendar shows full 16 weeks
- [ ] Calendar has working filters
- [ ] Deadline urgency updates dynamically
- [ ] Colors consistent across all pages
- [ ] Next Due Widget uses semantic colors
- [ ] Mobile-friendly and accessible
- [ ] Deployed to Vercel

## Estimated Time: 2.5 hours total

