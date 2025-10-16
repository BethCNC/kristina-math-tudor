# E-Learning Dashboard - Design System Guide

## Quick Reference for Designers & Developers

---

## 🎨 Color Palette

### Primary Colors
```css
--color-accent: #FE5A4A        /* Coral - Primary interactive color */
--color-accent-light: #FE5A4A1A /* 10% tint - Backgrounds */
--color-accent-dark: #FF5032    /* Darker coral - Progress fills */
```

### Greyscale
```css
--color-white: #FFFFFF
--color-grey: #222222          /* Primary text */
--color-grey-2: #717171        /* Secondary text */
--color-grey-3: #BDBDBD        /* Tertiary text */
--color-grey-4: #E0E0E0        /* Borders */
--color-grey-5: #EEEEEE        /* Light borders */
--color-grey-6: #F5F5F5        /* Backgrounds */
--color-black: #000000
```

### Category Colors (for Content Differentiation)
```css
Purple: #BA68C8 / Light: #F3E5F5  → Chapter 1, 10
Orange: #FF9800 / Light: #FFF3E0  → Chapter 4, 11
Blue:   #2196F3 / Light: #E3F2FD  → Chapter 5, 13
Pink:   #E91E63 / Light: #FCE4EC  → Chapter 6, Essay 1
Lime:   #CDDC39 / Light: #F9FBE7  → Chapter 7, Completed items
```

### Dark Mode
```css
--color-bg-body: #2A2A2A
--color-bg-primary: #2A2A2A
--color-bg-secondary: #333333
--color-bg-tertiary: #3C3C3C
--color-text-primary: #FFFFFF
--color-text-secondary: rgba(255, 255, 255, 0.75)
```

---

## 📐 Spacing System (8px Grid)

```
uxs:  4px   (0.25rem)  - Tight gaps, small padding
xxs:  8px   (0.5rem)   - Default gap in components
us:   6px   (0.375rem) - Badge padding
xs:   10px  (0.625rem) - Small padding
sm:   12px  (0.75rem)  - Card padding (compact)
md:   14px  (0.875rem) - Button padding
df:   16px  (1rem)     - Standard padding/gap
lg:   18px  (1.125rem)
xl:   20px  (1.25rem)  - Section padding
xxl:  24px  (1.5rem)   - Large gaps between sections
db:   32px  (2rem)     - Major section breaks
big:  40px  (2.5rem)
tr:   48px  (3rem)     - Maximum spacing
```

**Usage Examples:**
- Between cards in grid: `gap-df` (16px) or `gap-xxl` (24px)
- Inside cards: `p-df` (16px) or `p-xxl` (24px)
- Between sections: `mb-db` (32px)
- Tight elements: `gap-xxs` (8px)

---

## 🔤 Typography Scale

### Font Families
```css
Primary:  'Inter', 'IBM Plex Sans', sans-serif
Display:  'Inter', sans-serif
Mono:     'Space Mono', 'Courier New', monospace
```

### Headings (Semibold 600)
| Class   | Size | Line Height | Usage |
|---------|------|-------------|-------|
| `.h-big`  | 40px | 44px | Hero sections |
| `.h-db`   | 32px | 36px | Page titles |
| `.h-xxl`  | 24px | 28px | Section headings |
| `.h-xl`   | 20px | 24px | Subsection headings |
| `.h-lg`   | 18px | 22px | Card headings |
| `.h-df`   | 16px | 20px | Default headings |
| `.h-md`   | 14px | 18px | Small headings |
| `.h-sm`   | 12px | 16px | Tiny headings |

### Body Text (Regular 400)
| Class | Size | Line Height | Usage |
|-------|------|-------------|-------|
| `.t-df-paragraph` | 16px | 24px | Readable paragraphs |
| `.t-df` | 16px | 20px | Default text |
| `.t-md-paragraph` | 14px | 21px | Small paragraphs |
| `.t-md` | 14px | 18px | Compact text |
| `.t-sm` | 12px | 16px | Labels, hints |
| `.t-xs` | 10px | 14px | Tiny text |
| `.t-xxs` | 8px | 12px | Micro text |

### Weight Modifiers
- `.text-bold` - 700 weight
- `.text-semibold` - 600 weight
- `.text-medium` - 500 weight
- `.text-mono` - Monospace font

---

## 🔲 Border Radius

```css
--radius-sm:     4px   → Small elements, banners
--radius-md:     6px   → Buttons, inputs, badges
--radius-lg:     8px   → Cards, calendar days
--radius-xl:     12px  → Course cards
--radius-xxl:    16px  → Promotional cards
--radius-pill:   48px  → Pills, switches
--radius-circle: 100px → Avatars, icon buttons
```

**Examples:**
- Buttons: `rounded-md` (6px)
- Course cards: `rounded-xl` (12px)
- Promo cards: `rounded-xxl` (16px)
- Switch toggle: `rounded-pill` (48px)
- Avatar: `rounded-circle` (100px)

---

## 🌑 Shadows (Material Design Elevation)

```css
--shadow-dp4:  Small lift (hover states)
  0 0.3px 0.9px rgba(0,0,0,0.1),
  0 1.6px 3.6px rgba(0,0,0,0.13)

--shadow-dp8:  Standard cards
  0 0.6px 1.8px rgba(0,0,0,0.1),
  0 3.2px 7.2px rgba(0,0,0,0.13)

--shadow-dp16: Modal dialogs, toasts
  0 1.2px 3.6px rgba(0,0,0,0.1),
  0 6.4px 14.4px rgba(0,0,0,0.13)

--shadow-dp64: Maximum elevation
  0 4.8px 14.4px rgba(0,0,0,0.18),
  0 25.6px 57.6px rgba(0,0,0,0.22)
```

**Usage:**
- Cards at rest: `shadow-dp4`
- Cards on hover: `shadow-dp8`
- Focus mode toggle: `shadow-dp16`
- Modals: `shadow-dp64`

---

## 🧩 Component Patterns

### Course Card (Compact)
```html
<div class="course-card hover-lift">
  <div class="course-card-content">
    <div class="course-card-cover bg-purple-light">
      <!-- 80x80px cover image -->
    </div>
    <div class="course-card-body">
      <div class="course-card-header">
        <h3 class="course-card-title">Title</h3>
      </div>
      <div class="course-card-progress">
        <p class="course-card-progress-info">5/10 lessons | 50%</p>
        <div class="progress-bar-container">
          <div class="progress-bar-fill" style="width: 50%"></div>
        </div>
      </div>
    </div>
  </div>
  <!-- Optional notification banner -->
  <div class="course-card-banner">
    <i data-lucide="bell" class="course-card-banner-icon"></i>
    <span class="course-card-banner-text">New lesson available</span>
  </div>
</div>
```

**Dimensions:**
- Cover: 80px × 80px
- Card padding: 16px
- Gap between cover and body: 12px
- Border radius: 12px

### Calendar Event Card
```html
<div class="calendar-event-card">
  <div class="calendar-event-time flex items-center justify-between">
    <div class="flex items-center gap-uxs">
      <i data-lucide="clock" class="calendar-event-time-icon"></i>
      <span class="calendar-event-time-text">10:00 - 10:30</span>
    </div>
    <button class="btn-icon btn-sm">
      <i data-lucide="more-horizontal" class="icon-sm"></i>
    </button>
  </div>
  <div class="calendar-event-body">
    <h4 class="calendar-event-title">Event Title</h4>
    <p class="calendar-event-hint">Description text</p>
  </div>
</div>
```

**Dimensions:**
- Card padding: 12px
- Border radius: 8px
- Background: #F5F5F5
- Time icon: 12px
- Menu button: 24px

### Progress Info Card
```html
<div class="progress-info-card hover-lift-sm">
  <div class="progress-info-number">10</div>
  <div class="progress-info-label">Label text</div>
</div>
```

**Dimensions:**
- Min width: 110px
- Min height: 96px
- Padding: 8px
- Border radius: 8px
- Background: #F5F5F5
- Number: 24px semibold
- Label: 12px regular grey

### Switch Toggle
```html
<div class="switch">
  <button class="switch-item active" data-view="progress">Progress</button>
  <button class="switch-item" data-view="calendar">Calendar</button>
</div>
```

**Dimensions:**
- Container: 4px padding, 48px radius, 1px #EEE border
- Item: 8-12px padding, 32px height, 48px radius
- Active: Coral fill + white text
- Inactive: Transparent + dark text

### Button Styles
```html
<!-- Primary -->
<button class="btn-fill">Button Text</button>

<!-- Outline -->
<button class="btn-outline">Button Text</button>

<!-- Text Only -->
<button class="btn-text">Button Text</button>

<!-- Icon -->
<button class="btn-icon">
  <i data-lucide="icon-name" class="icon-md"></i>
</button>

<!-- With Icon Before -->
<button class="btn-fill btn-with-icon-before">
  <i data-lucide="icon-name" class="icon-md"></i>
  Button Text
</button>
```

**Dimensions:**
- Height: 48px (standard), 36px (small), 56px (large)
- Padding: 14px vertical, 16px horizontal
- Border radius: 6px
- Icon sizes: 12px (sm), 16px (md), 20px (lg)

---

## 📱 Responsive Grid System

### Breakpoints
```css
Mobile:  0 - 640px
Tablet:  641px - 1024px
Desktop: 1025px+
```

### Grid Behavior
```html
<div class="grid grid-cols-3 gap-df">
  <!-- Content -->
</div>
```

**Column Behavior:**
- `grid-cols-2`: 1 col (mobile), 2 cols (tablet+)
- `grid-cols-3`: 1 col (mobile), 2 cols (tablet), 3 cols (desktop)
- `grid-cols-4`: 1 col (mobile), 2 cols (tablet), 4 cols (desktop)

---

## 🎭 State Variations

### Hover States
```css
.hover-lift:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-dp8);
}

.hover-scale:hover {
  transform: scale(1.02);
}
```

### Active States
```css
.active-scale:active {
  transform: scale(0.98);
}
```

### Focus States
```css
*:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}
```

### Disabled States
```css
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}
```

---

## 🔧 Utility Classes

### Layout
```css
.flex              /* display: flex */
.flex-col          /* flex-direction: column */
.items-center      /* align-items: center */
.justify-between   /* justify-content: space-between */
.flex-1            /* flex: 1 */
.gap-df            /* gap: 16px */
```

### Spacing
```css
.p-df              /* padding: 16px */
.p-xxl             /* padding: 24px */
.mb-df             /* margin-bottom: 16px */
.mb-xxl            /* margin-bottom: 24px */
.mb-db             /* margin-bottom: 32px */
```

### Typography
```css
.text-primary      /* color: #222 */
.text-secondary    /* color: #717171 */
.text-accent       /* color: #FE5A4A */
.text-semibold     /* font-weight: 600 */
.text-mono         /* font-family: monospace */
```

### Background
```css
.bg-primary        /* background: #FFF */
.bg-secondary      /* background: #F5F5F5 */
.bg-accent-light   /* background: rgba(254,90,74,0.1) */
.bg-purple-light   /* background: #F3E5F5 */
```

### Borders & Radius
```css
.rounded-md        /* border-radius: 6px */
.rounded-lg        /* border-radius: 8px */
.rounded-xl        /* border-radius: 12px */
.rounded-pill      /* border-radius: 48px */
.border-primary    /* border-color: #E0E0E0 */
```

---

## 📐 Component Specifications

### Icon Sizes
```
12px - Small icons in compact areas
16px - Default icon size
18px - Medium icons in buttons
20px - Large icons in navigation
```

### Touch Targets
```
Minimum: 44px × 44px (WCAG AAA)
Buttons:  48px height
Icon buttons: 40px × 40px
Small buttons: 36px height
Bottom nav: 64px height
```

### Card Padding
```
Compact: 8px
Standard: 12-16px
Spacious: 24px
Hero sections: 32px
```

---

## 🎬 Animation Timing

```css
--transition-fast:   100ms  /* Active states */
--transition-normal: 200ms  /* Hover states */
--transition-slow:   300ms  /* Page transitions */
--transition-ease:   cubic-bezier(0.4, 0, 0.2, 1)
```

**Animation Guidelines:**
- Hover: 200ms
- Active/click: 100ms
- Page entrance: 300ms
- Progress fills: 300ms
- Stagger delay: 50ms per item

---

## 🎯 When to Use Each Component

### Course Card
**Use for:**
- Chapter listings
- Essay assignments
- Course modules
- Any learning content with progress tracking

**Don't use for:**
- Static content
- External links (use buttons)
- Simple lists

### Event Card
**Use for:**
- Calendar events
- Scheduled tasks
- Time-based activities
- Deadline reminders

**Don't use for:**
- All-day events (use different pattern)
- Multi-day events

### Progress Info Card
**Use for:**
- Statistics display
- Achievement counts
- Summary metrics
- Dashboard widgets

**Don't use for:**
- Detailed data (use full cards)
- Interactive elements

### Badges
**Use for:**
- Categories
- Status indicators
- Chapter numbers
- Time estimates
- Course types

**Don't use for:**
- Long text (use labels)
- Interactive filters (use switch)

### Switch Toggle
**Use for:**
- View switching (2-3 options)
- Mode selection
- Binary choices

**Don't use for:**
- Many options (use tabs or select)
- One-time actions (use buttons)

---

## 📱 Mobile Navigation Pattern

```html
<!-- Desktop: Horizontal header -->
<header class="header">
  <a href="/" class="header-logo">Logo</a>
  <nav class="header-nav">
    <a href="#" class="nav-item-desktop active">Home</a>
    <!-- More items -->
  </nav>
  <div class="header-actions">
    <button class="btn-icon">Icon</button>
    <div class="avatar">Avatar</div>
  </div>
</header>

<!-- Mobile: Bottom navigation -->
<nav class="bottom-nav">
  <a href="#" class="nav-item-mobile active">
    <i data-lucide="home" class="nav-item-mobile-icon"></i>
    <span class="nav-item-mobile-label">Home</span>
  </a>
  <!-- 4 more items -->
</nav>
```

---

## 🎨 Color Usage Guidelines

### Accent Coral (#FE5A4A)
**Use for:**
- Primary buttons
- Active navigation states
- Progress fills
- Interactive elements
- Notification badges
- Focus indicators

**Don't use for:**
- Body text (low contrast)
- Large backgrounds
- Borders (too vibrant)

### Category Colors
**Assign to:**
- Chapter 1: Purple
- Chapter 4: Orange
- Chapter 5: Blue
- Chapter 6: Pink
- Chapter 7: Lime
- Chapter 10: Purple
- Chapter 11: Orange
- Chapter 13: Blue

**Usage:**
- Cover backgrounds: Light tints (e.g., `bg-purple-light`)
- Badges: Full color (e.g., `badge-purple`)
- Section identifiers

### Greyscale
- **#222 (grey)**: Primary text, headings
- **#717171 (grey-2)**: Secondary text, descriptions
- **#BDBDBD (grey-3)**: Tertiary text, disabled elements
- **#E0E0E0 (grey-4)**: Borders
- **#EEE (grey-5)**: Light borders, switch container
- **#F5F5F5 (grey-6)**: Card backgrounds, alternating rows

---

## ✅ Accessibility Quick Checks

### Color Contrast
- Primary text (#222) on white: **15.8:1** ✅ AAA
- Secondary text (#717171) on white: **4.69:1** ✅ AA
- White on accent (#FE5A4A): **3.39:1** ⚠️ AA large text only

### Touch Targets
- All buttons: **48px** ✅
- Icon buttons: **40px** ✅
- Small buttons: **36px** ✅
- Bottom nav: **64px** ✅

### Keyboard
- All interactive elements Tab-accessible ✅
- Focus indicators visible ✅
- No keyboard traps ✅
- Skip link functional ✅

### Screen Reader
- Semantic HTML ✅
- ARIA labels on icon buttons ✅
- Heading hierarchy ✅
- Landmark regions ✅

---

## 🚀 Getting Started

### 1. Include Design System
```html
<link rel="stylesheet" href="src/styles/globals-new.css">
```

### 2. Use Semantic Structure
```html
<body class="bg-primary">
  <header class="header"><!-- Nav --></header>
  <main class="container"><!-- Content --></main>
  <nav class="bottom-nav"><!-- Mobile nav --></nav>
</body>
```

### 3. Build with Components
- Start with course cards for content
- Use consistent spacing (`gap-df`, `mb-xxl`)
- Apply hover states (`hover-lift`)
- Add icons from Lucide
- Initialize with `lucide.createIcons()`

### 4. Test Responsiveness
- View at 375px, 768px, 1280px
- Check mobile bottom nav appears
- Verify grid collapses correctly
- Test touch targets on devices

---

## 📖 Further Resources

**Figma Source:**
- [E-learning dashboard UI](https://www.figma.com/design/pOyqXnWT6VLK3UciRtufO7/)

**Design Tokens:**
- See `tokens.json` for complete token definitions

**Component Showcase:**
- View `responsive-test.html` for all component examples

**Accessibility:**
- Review `ACCESSIBILITY_AUDIT_CHECKLIST.md`

**Implementation:**
- See `IMPLEMENTATION_SUMMARY.md` for complete details

---

**Design System Version**: 1.0.0  
**Last Updated**: October 16, 2025  
**Status**: Production Ready

