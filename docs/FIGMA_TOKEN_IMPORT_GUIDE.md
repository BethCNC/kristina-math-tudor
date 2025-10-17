# Figma Token Import Guide

## Overview

The `tokens-new.json` file contains your **actual implemented design system** (Professional Academic Dashboard) and can be imported into Figma to keep your designs in sync with the codebase.

---

## What's Included in tokens-new.json

### ✅ Current Implementation (From CSS)

**Colors:**
- Primary Blue (#1e40af) - not coral accent
- Success Green (#059669)
- Warning Orange (#d97706)
- Danger Red (#dc2626)
- Complete deadline urgency system (5 colors)
- Course colors (Math purple, English blue)

**Typography:**
- Inter font family (primary)
- 7 font sizes (12px - 30px)
- 4 font weights (400, 500, 600, 700) ✅ includes missing weights
- 3 line heights (1.2, 1.5, 1.6)

**Spacing:**
- 10 sizes following 4px grid system ✅
- Includes space-16 (64px) that was missing from original tokens

**Shadows:**
- 4 elevation levels (sm, md, lg, xl)
- Softer Material Design style (matches current CSS)

**Components:**
- Button tokens (primary, secondary)
- Card tokens
- Badge tokens (urgent, warning, upcoming, completed)

**Accessibility:**
- 44px minimum touch target
- Focus ring specifications
- ADHD-friendly considerations

---

## How to Import into Figma

### Method 1: Using Figma Tokens Plugin (Recommended)

1. **Install Figma Tokens Plugin**
   - Open Figma
   - Go to **Plugins** → **Browse plugins in Community**
   - Search for **"Tokens Studio for Figma"** (formerly Figma Tokens)
   - Click **Install**

2. **Import tokens-new.json**
   - In Figma, open your file
   - Run the plugin: **Plugins** → **Tokens Studio**
   - Click **Settings** (gear icon)
   - Select **Import** → **From File**
   - Choose `tokens-new.json`
   - Click **Import**

3. **Apply Tokens to Styles**
   - In the plugin, go to **Themes** tab
   - Select **"Professional Academic Dashboard"**
   - Click **Create Styles from Tokens**
   - This will create Figma color styles, text styles, and effects

4. **Sync Changes**
   - When you update tokens in code, export from CSS → JSON
   - Re-import into Figma
   - Figma will update all components using those tokens

### Method 2: Manual Style Creation

If you don't want to use plugins:

1. **Create Color Styles**
   - In Figma, open **Local styles** panel
   - Click **+** next to Colors
   - Create styles matching tokens:
     - `primary/blue` → #1e40af
     - `semantic/success-green` → #059669
     - `semantic/warning-orange` → #d97706
     - `semantic/danger-red` → #dc2626
     - etc.

2. **Create Text Styles**
   - Click **+** next to Text
   - Create styles:
     - `Heading/H1` → Inter, 30px, Semibold (600), 1.2 line height
     - `Heading/H2` → Inter, 24px, Semibold (600), 1.2 line height
     - `Body/Regular` → Inter, 16px, Regular (400), 1.5 line height
     - etc.

3. **Create Effect Styles**
   - Click **+** next to Effects
   - Create shadow styles:
     - `shadow/sm` → Drop Shadow: y:1, blur:2, opacity:5%
     - `shadow/md` → Drop Shadow: y:4, blur:6, opacity:10% (add second: y:2, blur:4, 6%)
     - etc.

---

## Token Structure Explanation

### Foundation Colors
```json
{
  "colors": {
    "foundation": {
      "white": "#ffffff",
      "black": "#000000"
    }
  }
}
```
Basic colors that don't change.

### Semantic Colors
```json
{
  "colors": {
    "semantic": {
      "success-green": "#059669",
      "warning-orange": "#d97706",
      "danger-red": "#dc2626"
    }
  }
}
```
Colors with **meaning** - used for feedback and states.

### Token References
```json
{
  "text": {
    "default": {
      "value": "{colors.neutral.gray}"
    }
  }
}
```
The `{...}` syntax means this token **references** another token. When you change `colors.neutral.gray`, all references update automatically.

---

## Mapping Tokens to Figma

### Colors → Color Styles

| Token Path | Figma Style Name | Usage |
|------------|------------------|-------|
| `colors.primary.blue` | `Primary/Blue` | CTAs, links |
| `colors.semantic.success-green` | `Semantic/Success` | Completed states |
| `colors.deadline-urgency.urgent` | `Deadline/Urgent` | 0-3 day deadlines |
| `colors.course.math-purple` | `Course/Math` | MAT 143 cards |

### Typography → Text Styles

| Token Path | Figma Style Name | Usage |
|------------|------------------|-------|
| `typography.fontSizes.3xl` | `Heading/H1` | Main headings |
| `typography.fontSizes.2xl` | `Heading/H2` | Section headings |
| `typography.fontSizes.base` | `Body/Regular` | Body text |

### Spacing → Layout Grid

| Token | Figma Grid | Usage |
|-------|------------|-------|
| `spacing.4` (16px) | 16px columns | Base unit |
| `spacing.8` (32px) | 32px gutter | Component spacing |

### Shadows → Effect Styles

| Token | Figma Effect | Usage |
|-------|--------------|-------|
| `shadows.sm` | `Shadow/Small` | Subtle cards |
| `shadows.md` | `Shadow/Medium` | Interactive elements |

---

## Updating Tokens from Figma

### Export from Figma

1. Make changes in Figma
2. Open **Tokens Studio** plugin
3. Click **Export** → **Download JSON**
4. Replace `tokens-new.json` in project
5. Run CSS generation script (if you have one)
6. Commit changes to Git

### Sync Workflow

```
Figma Design → Export JSON → tokens-new.json → Generate CSS → Update site
     ↑                                                              |
     └──────────────────────────────────────────────────────────────┘
              Import updated tokens back to Figma
```

---

## Differences from Original tokens.json

### ✅ Fixed in tokens-new.json

1. **Accent color** changed from coral (#fe5a4a) to blue (#1e40af)
2. **Added font weights:** Medium (500) and Bold (700)
3. **Added space-16:** 64px spacing token
4. **Added deadline urgency system:** 5 semantic colors
5. **Shadows match current CSS:** Softer than Material Design
6. **Removed unused IBM Plex Sans** references
7. **Added component tokens:** Button, Card, Badge
8. **Added accessibility tokens:** Touch targets, focus rings
9. **Added animation tokens:** Durations, easing

### File Comparison

| Feature | tokens.json (old) | tokens-new.json | Match? |
|---------|------------------|-----------------|---------|
| Accent Color | Coral #fe5a4a | Blue #1e40af | ✅ Fixed |
| Font Weights | 2 (400, 600) | 4 (400, 500, 600, 700) | ✅ Complete |
| Spacing Scale | 13 sizes | 10 sizes (cleaner) | ✅ Simplified |
| Shadow Style | Material (strong) | Softer (current) | ✅ Matches CSS |
| Deadline Colors | ❌ None | ✅ 5 colors | ✅ Added |
| Components | ❌ None | ✅ Button, Card, Badge | ✅ Added |

---

## Best Practices

### 1. Use Token References
**Good:**
```json
{
  "button.primary.background": {
    "value": "{colors.primary.blue}"
  }
}
```

**Bad:**
```json
{
  "button.primary.background": {
    "value": "#1e40af"
  }
}
```

**Why?** If you change primary blue, all buttons update automatically.

### 2. Semantic Naming
**Good:** `colors.semantic.success-green`  
**Bad:** `colors.green`

**Why?** Semantic names explain **why** you use a color, not just what it looks like.

### 3. Keep Tokens DRY
Don't repeat values. Use references:
```json
{
  "spacing.card-padding": {
    "value": "{spacing.6}"
  }
}
```

### 4. Document Tokens
Every token should have a `description` field:
```json
{
  "value": "#1e40af",
  "type": "color",
  "description": "Primary blue for trust and stability"
}
```

---

## Troubleshooting

### Token References Not Working

**Problem:** `{colors.primary.blue}` shows as text, not the color.

**Solution:** 
1. Check token path is correct (case-sensitive)
2. Ensure referenced token exists
3. Try using full path: `{Professional Academic Dashboard.colors.primary.blue}`

### Styles Not Updating

**Problem:** Changed token but Figma styles didn't update.

**Solution:**
1. Re-run "Create Styles from Tokens" in plugin
2. Check if styles are linked to tokens
3. Delete old styles and recreate

### Import Failed

**Problem:** JSON import shows error.

**Solution:**
1. Validate JSON syntax: [jsonlint.com](https://jsonlint.com)
2. Check for missing commas or brackets
3. Ensure `type` field is correct (`color`, `fontSizes`, etc.)

---

## Validation Script

Use this to verify tokens-new.json is valid:

```javascript
const tokens = require('./tokens-new.json');

function validateTokens(obj, path = '') {
  for (const [key, value] of Object.entries(obj)) {
    // Skip metadata
    if (key.startsWith('$')) continue;
    
    // Check if it's a token (has type and value)
    if (value.type && value.value !== undefined) {
      // Validate color format
      if (value.type === 'color' && typeof value.value === 'string') {
        if (!value.value.match(/^(#[0-9a-f]{6}|rgba?\(|{.*})$/i)) {
          console.warn(`⚠️ Invalid color at ${path}${key}: ${value.value}`);
        } else {
          console.log(`✅ ${path}${key}: ${value.value}`);
        }
      }
      // Validate has description
      if (!value.description) {
        console.warn(`⚠️ Missing description at ${path}${key}`);
      }
    } else if (typeof value === 'object' && !Array.isArray(value)) {
      // Recurse into nested objects
      validateTokens(value, `${path}${key}.`);
    }
  }
}

validateTokens(tokens['Professional Academic Dashboard']);
console.log('\n✅ Token validation complete!');
```

Run with: `node validate-tokens.js`

---

## Additional Resources

- **Tokens Studio Plugin:** [tokens.studio](https://tokens.studio)
- **Design Tokens W3C Spec:** [design-tokens.github.io](https://design-tokens.github.io/community-group/)
- **Our CSS Variables:** `/src/styles/professional-academic.css`
- **Token Documentation:** `/docs/DESIGN_TOKENS_REFERENCE.md`

---

## Next Steps

1. ✅ Import `tokens-new.json` into Figma
2. ✅ Create Figma styles from tokens
3. ✅ Apply styles to existing components
4. ✅ Update components in design
5. ✅ Export updated tokens
6. ✅ Update CSS to match
7. ✅ Deploy to production

---

**Created:** November 1, 2025  
**Last Updated:** November 1, 2025  
**Version:** 1.0.0 (Professional Academic Dashboard)

