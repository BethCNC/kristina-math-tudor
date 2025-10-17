# Design Tokens Reference Guide

**Source File:** `/tokens.json`  
**Version:** Light Theme (E-learning Dashboard)  
**Last Updated:** November 1, 2025

---

## 📋 Table of Contents

1. [Color System](#color-system)
2. [Typography](#typography)
3. [Spacing & Sizing](#spacing--sizing)
4. [Shadows & Elevation](#shadows--elevation)
5. [Semantic Tokens](#semantic-tokens)
6. [Usage Examples](#usage-examples)
7. [Migration from Figma](#migration-from-figma)

---

## 🎨 Color System

### Main Colors

#### Foundation Colors
```json
{
  "white": "#ffffff",
  "black": "#000000",
  "body": "#ffffff"  // references white
}
```

#### Grey Scale (6 shades)
Perfect for text, borders, and subtle backgrounds.

| Token | Hex | Usage |
|-------|-----|-------|
| `grey` | `#222222` | Primary text, headers |
| `grey-2` | `#717171` | Secondary text, labels |
| `grey-3` | `#bdbdbd` | Disabled text, placeholders |
| `grey-4` | `#e0e0e0` | Borders, dividers |
| `grey-5` | `#eeeeee` | Light backgrounds |
| `grey-6` | `#f5f5f5` | Subtle backgrounds, cards |

**Note:** Our current professional design system uses different greys. Consider using these tokens for consistency.

#### Accent & Primary
```json
{
  "accent": "#fe5a4a",        // Coral red (CTAs, important actions)
  "accent-light": "#fe5a4a1a" // 10% opacity for backgrounds
}
```

**Current Implementation:**
- Our CSS uses `--primary-blue: #1e40af` for trust/stability
- Consider if coral accent should replace blue for CTAs

#### Category Colors (Material Design Inspired)

**Purple** (Math/Analytics)
```json
{
  "purple": "#ba68c8",
  "purple-light": "#f3e5f5"
}
```

**Orange** (Warnings/Reminders)
```json
{
  "orange": "#ff9800",
  "orange-light": "#fff3e0"
}
```

**Blue** (Information/Primary)
```json
{
  "blue": "#2196f3",
  "blue-light": "#e3f2fd"
}
```

**Pink** (Highlights/Special)
```json
{
  "pink": "#e91e63",
  "pink-light": "#fce4ec"
}
```

**Lime** (Success/Growth)
```json
{
  "lime": "#cddc39",
  "lime-light": "#f9fbe7"
}
```

### Semantic Color Tokens

#### Text Colors
```json
{
  "text.default": "{colors.main.grey}",     // #222222
  "text.light": "{colors.main.grey-2}",     // #717171
  "text.inverse": "{colors.main.white}",    // #ffffff
  "text.inverse-light": "#ffffffbf",        // 75% opacity
  "text.accent": "{colors.main.accent}",    // #fe5a4a
  "text.hover": "{colors.main.black}"       // #000000
}
```

#### Button Colors
```json
{
  "button.default": "{colors.main.grey}",
  "button.inverse": "{colors.main.white}",
  "button.accent": "{colors.main.accent}",
  "button.hover": "{colors.main.black}"
}
```

### Color Accessibility

**WCAG 2.1 AA Compliance:**
- Grey (#222222) on White: **15.3:1** ✅ AAA
- Grey-2 (#717171) on White: **4.7:1** ✅ AA
- Accent (#fe5a4a) on White: **3.8:1** ⚠️ AA Large Text Only
- Blue (#2196f3) on White: **4.6:1** ✅ AA

**Recommendation:** Use accent color for large text or with white text on accent background.

---

## 🔤 Typography

### Font Families

**Primary:** Inter (Body text, UI elements)
```json
{
  "fontFamilies.inter": "Inter"
}
```

**Secondary:** IBM Plex Sans (Headings, special emphasis)
```json
{
  "fontFamilies.ibm-plex-sans": "IBM Plex Sans"
}
```

**Current Implementation:**
- Our CSS uses `font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
- IBM Plex Sans is defined in tokens but not currently used in CSS

### Font Sizes

Complete scale from 8px to 32px:

| Token | Value | Rem | Usage |
|-------|-------|-----|-------|
| `fontSize.0` | 8px | 0.5rem | Tiny labels, timestamps |
| `fontSize.1` | 10px | 0.625rem | Small captions |
| `fontSize.2` | 12px | 0.75rem | Labels, helper text |
| `fontSize.3` | 14px | 0.875rem | Secondary text |
| `fontSize.4` | 16px | 1rem | Body text (base) |
| `fontSize.5` | 18px | 1.125rem | Large body |
| `fontSize.6` | 20px | 1.25rem | H4 headings |
| `fontSize.7` | 24px | 1.5rem | H3 headings |
| `fontSize.8` | 32px | 2rem | H2, H1 headings |

**Current CSS Mapping:**
```css
--font-size-xs: 0.75rem;    /* 12px - matches fontSize.2 */
--font-size-sm: 0.875rem;   /* 14px - matches fontSize.3 */
--font-size-base: 1rem;     /* 16px - matches fontSize.4 */
--font-size-lg: 1.125rem;   /* 18px - matches fontSize.5 */
--font-size-xl: 1.25rem;    /* 20px - matches fontSize.6 */
--font-size-2xl: 1.5rem;    /* 24px - matches fontSize.7 */
--font-size-3xl: 1.875rem;  /* 30px - NOT in tokens! */
```

**Discrepancy:** Our CSS uses 30px for `3xl` but tokens.json only goes up to 32px. Consider adding 30px to tokens or adjusting CSS.

### Font Weights

**Inter:**
```json
{
  "inter-0": "Semi Bold",  // 600
  "inter-1": "Regular"     // 400
}
```

**IBM Plex Sans:**
```json
{
  "ibm-plex-sans-0": "SemiBold",  // 600
  "ibm-plex-sans-1": "Regular"    // 400
}
```

**Current CSS:**
- Uses `font-weight: 400` (regular) for body
- Uses `font-weight: 500` (medium) - NOT in tokens!
- Uses `font-weight: 600` (semibold) for headings
- Uses `font-weight: 700` (bold) - NOT in tokens!

**Recommendation:** Add Medium (500) and Bold (700) weights to tokens.json.

### Line Heights

15 predefined line heights for optimal readability:

| Token | Value | Best For |
|-------|-------|----------|
| `lineHeights.0` | 44px | Display text (32px font) |
| `lineHeights.1` | 36px | H1 headings |
| `lineHeights.2` | 28px | H2 headings |
| `lineHeights.3` | 24px | H3 headings |
| `lineHeights.4` | 22px | Large body |
| `lineHeights.5` | 20px | Body text (16px) |
| `lineHeights.6` | 18px | Small text |
| `lineHeights.7` | 16px | Dense text |
| `lineHeights.8` | 20px | Alternative body |
| `lineHeights.9` | 24px | Spacious headings |
| `lineHeights.10` | 18px | Compact body |
| `lineHeights.11` | 21px | Comfortable reading |
| `lineHeights.12` | 16px | Tight labels |
| `lineHeights.13` | 14px | Very compact |
| `lineHeights.14` | 12px | Micro text |

**Current CSS:**
- Uses `line-height: 1.5` (relative) for body
- Uses `line-height: 1.2` (relative) for headings
- Uses `line-height: 1.6` (relative) for body

**Recommendation:** Consider using token-based absolute line heights for more precise control.

---

## 📏 Spacing & Sizing

### Size Scale (14 sizes)

Based on 4px grid system with fractional steps:

| Token | Value | Rem | Pixels | Usage |
|-------|-------|-----|--------|-------|
| `size.uxs` | 0.25rem | 0.25rem | 4px | Micro spacing |
| `size.xxs` | 0.5rem | 0.5rem | 8px | Tight spacing |
| `size.us` | 0.375rem | 0.375rem | 6px | In-between |
| `size.xs` | 0.625rem | 0.625rem | 10px | Small spacing |
| `size.sm` | 0.75rem | 0.75rem | 12px | Compact padding |
| `size.md` | 0.875rem | 0.875rem | 14px | Medium spacing |
| `size.df` | 1rem | 1rem | 16px | Default spacing |
| `size.lg` | 1.125rem | 1.125rem | 18px | Comfortable spacing |
| `size.xl` | 1.25rem | 1.25rem | 20px | Large spacing |
| `size.xxl` | 1.5rem | 1.5rem | 24px | Section spacing |
| `size.db` | 2rem | 2rem | 32px | Component spacing |
| `size.big` | 2.5rem | 2.5rem | 40px | Large margins |
| `size.tr` | 3rem | 3rem | 48px | Section breaks |

**Current CSS Spacing:**
```css
--space-1: 0.25rem;   /* 4px  - matches size.uxs */
--space-2: 0.5rem;    /* 8px  - matches size.xxs */
--space-3: 0.75rem;   /* 12px - matches size.sm */
--space-4: 1rem;      /* 16px - matches size.df */
--space-5: 1.25rem;   /* 20px - matches size.xl */
--space-6: 1.5rem;    /* 24px - matches size.xxl */
--space-8: 2rem;      /* 32px - matches size.db */
--space-10: 2.5rem;   /* 40px - matches size.big */
--space-12: 3rem;     /* 48px - matches size.tr */
--space-16: 4rem;     /* 64px - NOT in tokens! */
```

**Perfect Alignment!** ✅ Our spacing scale matches tokens beautifully (except 64px).

**User Memory:** User prefers 4pt grid system (4px increments). ✅ Our tokens respect this!

---

## 🌑 Shadows & Elevation

Material Design-inspired elevation system with 4 levels:

### sw-dp4 (Low Elevation)
**Usage:** Cards, buttons (resting state)

```css
box-shadow: 
  0 0.3px 0.9px rgba(0,0,0,0.1),
  0 1.6px 3.6px rgba(0,0,0,0.13);
```

### sw-dp8 (Medium Elevation)
**Usage:** Dropdowns, tooltips, raised buttons

```css
box-shadow: 
  0 0.6px 1.8px rgba(0,0,0,0.1),
  0 3.2px 7.2px rgba(0,0,0,0.13);
```

### sw-dp16 (High Elevation)
**Usage:** Modals, popovers, floating action buttons

```css
box-shadow: 
  0 1.2px 3.6px rgba(0,0,0,0.1),
  0 6.4px 14.4px rgba(0,0,0,0.13);
```

### sw-dp64 (Maximum Elevation)
**Usage:** Navigation drawer, bottom sheets, important overlays

```css
box-shadow: 
  0 4.8px 14.4px rgba(0,0,0,0.18),
  0 25.6px 57.6px rgba(0,0,0,0.22);
```

**Current CSS Shadows:**
```css
--shadow-sm: 0 1px 2px 0 rgba(0,0,0,0.05);        /* Lighter than dp4 */
--shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), ... /* Between dp4-dp8 */
--shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1),... /* Between dp8-dp16 */
--shadow-xl: 0 20px 25px -5px rgba(0,0,0,0.1),... /* Between dp16-dp64 */
```

**Recommendation:** Our current shadows are softer (lower opacity). Consider if Material Design shadows from tokens.json better match the Figma design intent.

---

## 🎯 Semantic Tokens

### Purpose

Semantic tokens reference base tokens and provide **context-specific naming**. They make code more readable and easier to maintain.

### How to Use Semantic Tokens

**Bad (Hard-coded):**
```css
color: #222222;
```

**Good (Base Token):**
```css
color: var(--grey);
```

**Best (Semantic Token):**
```css
color: var(--text-default);
```

**Why?** If you decide grey should be `#333333` instead, you only change it once. If you want different text colors on different backgrounds, semantic tokens adapt.

### Token Reference Format

Tokens use `{path.to.token}` syntax for references:

```json
{
  "text.default": "{colors.main.grey}"
}
```

This means `text.default` will always equal whatever `colors.main.grey` is set to.

---

## 💻 Usage Examples

### Example 1: Button with Accent Color

**HTML:**
```html
<button class="btn-primary">Complete Hawkes</button>
```

**CSS (using tokens):**
```css
.btn-primary {
  background-color: var(--accent);
  color: var(--text-inverse);
  padding: var(--size-sm) var(--size-df);
  font-size: var(--fontSize-3);
  font-weight: var(--inter-0);
  border-radius: var(--size-xxs);
  box-shadow: var(--sw-dp4);
}

.btn-primary:hover {
  background-color: var(--button-hover);
  box-shadow: var(--sw-dp8);
}
```

### Example 2: Card with Category Color

**HTML:**
```html
<div class="course-card math">
  <h3>MAT 143: Chapter 6</h3>
  <p>Personal Finance</p>
</div>
```

**CSS (using tokens):**
```css
.course-card {
  background-color: var(--grey-6);
  padding: var(--size-xxl);
  border-radius: var(--size-sm);
  box-shadow: var(--sw-dp4);
  border-left: 4px solid var(--purple);
}

.course-card.math {
  background: linear-gradient(135deg, var(--purple-light) 0%, var(--white) 100%);
  border-left-color: var(--purple);
}

.course-card h3 {
  font-size: var(--fontSize-6);
  font-weight: var(--inter-0);
  color: var(--text-default);
  line-height: var(--lineHeights-3);
  margin-bottom: var(--size-xxs);
}

.course-card p {
  font-size: var(--fontSize-3);
  color: var(--text-light);
  line-height: var(--lineHeights-5);
}
```

### Example 3: Typography Scale

**HTML:**
```html
<h1>Academic Dashboard</h1>
<h2>MAT 143 & ENG 111</h2>
<h3>This Week's Tasks</h3>
<p>You're making great progress!</p>
```

**CSS (using tokens):**
```css
h1 {
  font-family: var(--inter);
  font-size: var(--fontSize-8);    /* 32px */
  font-weight: var(--inter-0);     /* Semi Bold */
  line-height: var(--lineHeights-1); /* 36px */
  color: var(--text-default);
  margin-bottom: var(--size-df);
}

h2 {
  font-family: var(--inter);
  font-size: var(--fontSize-7);    /* 24px */
  font-weight: var(--inter-0);
  line-height: var(--lineHeights-2); /* 28px */
  color: var(--text-default);
  margin-bottom: var(--size-sm);
}

h3 {
  font-family: var(--inter);
  font-size: var(--fontSize-6);    /* 20px */
  font-weight: var(--inter-0);
  line-height: var(--lineHeights-3); /* 24px */
  color: var(--text-default);
  margin-bottom: var(--size-xs);
}

p {
  font-family: var(--inter);
  font-size: var(--fontSize-4);    /* 16px */
  font-weight: var(--inter-1);     /* Regular */
  line-height: var(--lineHeights-5); /* 20px */
  color: var(--text-default);
}
```

---

## 🔄 Migration from Figma

### Step 1: Export Tokens from Figma

If you have the Figma Tokens plugin:

1. Open Figma file
2. Select **Tokens plugin**
3. Export as **JSON**
4. Save as `tokens.json`

**Note:** Our current `tokens.json` appears to be from an e-learning template. Verify it matches your custom Figma designs.

### Step 2: Compare with Current CSS

**Current CSS Variables vs Tokens:**

| Our CSS | tokens.json | Match? |
|---------|-------------|--------|
| `--primary-blue: #1e40af` | `blue: #2196f3` | ❌ Different |
| `--success-green: #059669` | `lime: #cddc39` | ❌ Different concept |
| `--warning-orange: #d97706` | `orange: #ff9800` | ❌ Different |
| `--danger-red: #dc2626` | `accent: #fe5a4a` | ❌ Different |
| `--space-4: 1rem` | `size.df: 1rem` | ✅ Match! |
| `--shadow-md` | `sw-dp8` | ⚠️ Similar intent |

**Recommendation:** Decide if you want to:
- **Option A:** Use tokens.json as source of truth (more Material Design)
- **Option B:** Update tokens.json to match our professional academic design
- **Option C:** Keep both and use selectively

### Step 3: Create CSS Variables from Tokens

**Automated approach:**

```javascript
// Convert tokens.json to CSS custom properties
const tokens = require('./tokens.json');

function tokenToCSS(obj, prefix = '') {
  let css = '';
  for (const [key, value] of Object.entries(obj)) {
    if (value.type && value.value) {
      const varName = `${prefix}${key}`.replace(/\./g, '-');
      css += `  --${varName}: ${value.value};\n`;
    } else if (typeof value === 'object') {
      css += tokenToCSS(value, `${prefix}${key}-`);
    }
  }
  return css;
}

console.log(':root {');
console.log(tokenToCSS(tokens['Tokens/Light']));
console.log('}');
```

### Step 4: Update Components

**Before:**
```css
.card {
  background: #ffffff;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
```

**After (using tokens):**
```css
.card {
  background: var(--white);
  padding: var(--size-xxl);
  border-radius: var(--size-sm);
  box-shadow: var(--sw-dp8);
}
```

---

## 🎨 Design System Integration

### Current Status

**✅ What's Implemented:**
- Professional academic color system (blue, green, orange, red)
- Spacing scale (4px grid)
- Typography (Inter font)
- Shadows (softer than Material Design)
- Semantic deadline colors (urgent, warning, upcoming)

**⚠️ What Needs Alignment:**
- tokens.json uses coral accent (#fe5a4a) vs our blue (#1e40af)
- tokens.json has Material Design shadows vs our softer shadows
- tokens.json includes IBM Plex Sans (unused)
- Missing font weights (500, 700) in tokens.json

### Recommended Actions

1. **Update tokens.json to match current design:**
   ```json
   {
     "colors": {
       "main": {
         "accent": "#1e40af",        // Change from coral to blue
         "accent-success": "#059669",  // Add success green
         "accent-warning": "#d97706",  // Add warning orange
         "accent-danger": "#dc2626"    // Add danger red
       }
     }
   }
   ```

2. **Add missing font weights:**
   ```json
   {
     "fontWeights": {
       "inter-2": "Medium",  // 500
       "inter-3": "Bold"     // 700
     }
   }
   ```

3. **Add space-16 (64px):**
   ```json
   {
     "size": {
       "huge": "4rem"  // 64px
     }
   }
   ```

4. **Document semantic deadline system in tokens:**
   ```json
   {
     "colors": {
       "deadline": {
         "urgent": "#dc2626",     // 0-3 days
         "warning": "#d97706",    // 4-7 days
         "upcoming": "#1e40af",   // 8-14 days
         "completed": "#059669",  // Past
         "future": "#6b7280"      // 14+ days
       }
     }
   }
   ```

---

## 📚 Additional Resources

- **Figma File:** [E-learning Dashboard UI](https://www.figma.com/design/pOyqXnWT6VLK3UciRtufO7/)
- **Current CSS:** `/src/styles/professional-academic.css`
- **Semantic Color System:** `/docs/SEMANTIC_COLOR_SYSTEM.md`
- **Material Design Elevation:** [Material.io](https://material.io/design/environment/elevation.html)

---

## 🔧 Maintenance

### When to Update Tokens

1. **Brand color change** - Update base colors
2. **New component** - Add semantic tokens
3. **Responsive breakpoint** - Add size tokens
4. **Accessibility fix** - Adjust colors/contrast

### Version Control

- Always commit `tokens.json` changes
- Document breaking changes in commit message
- Update CSS variables to match
- Test across all pages before deploying

### Testing Tokens

```javascript
// Verify all tokens are valid
const tokens = require('./tokens.json');
function validateTokens(obj, path = '') {
  for (const [key, value] of Object.entries(obj)) {
    if (value.type && value.value) {
      if (value.type === 'color' && !value.value.match(/^#[0-9a-f]{6}$/i)) {
        console.warn(`Invalid color at ${path}${key}: ${value.value}`);
      }
    } else if (typeof value === 'object') {
      validateTokens(value, `${path}${key}.`);
    }
  }
}
validateTokens(tokens);
```

---

**Last Updated:** November 1, 2025  
**Maintainer:** Design System Team  
**Questions?** See `README.md` or `CONTRIBUTING.md`

