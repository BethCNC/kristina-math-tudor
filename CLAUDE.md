# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Development Commands

**Local Development:**
```bash
python3 -m http.server 8000     # Start local server at http://localhost:8000
# No build step required - all pages work immediately
```

**CSS Compilation (if modifying styles):**
```bash
npm run build:css   # Compile Tailwind CSS to dist/output.css (minified)
npm run dev         # Watch and auto-compile CSS changes
```

**Production Build (Vite):**
```bash
npx vite build      # Build multi-page site to dist/ directory
npx vite preview    # Preview production build locally
```

**Python Environment Setup:**
```bash
pip install -r requirements.txt  # Install Python dependencies for API functions
# Required for API endpoints: anthropic>=0.7.0, python-dotenv>=1.0.0
```

**Common Python Scripts:**
```bash
python scripts/check_accessibility.py        # Run accessibility audit (WCAG 2.1 AA)
python scripts/check_links.py               # Check for broken links
python scripts/check_color_accessibility.py  # Verify color contrast ratios
python scripts/convert_markdown_to_html.py  # Convert course materials to HTML
```

## Project Architecture

### Core Structure
This is an academic success dashboard for MAT 143 (Quantitative Literacy) and ENG 111 (Writing & Inquiry) courses at CPCC. The application uses a multi-page static site architecture with Vite as the build tool.

**Main Application Files:**
- `index.html` - Executive function dashboard with progress tracking
- `calendar.html` - 16-week semester timeline with integrated test schedules
- `tutor.html` - AI-powered math tutoring interface
- `english_materials.html` - ENG 111 writing resources and guides
- `chapter-*.html` - Individual MAT 143 chapter study pages

### AI Tutoring System
The project includes a sophisticated AI tutoring system with multiple components:

**Backend API (Python/Vercel):**
- `api/tutor.py` - Main Vercel serverless function for math tutoring (uses claude-3-sonnet-20240229)
- `api/english_tutor.py` - English writing assistance API
- `tutor_system/mat143_tutor.py` - Comprehensive local tutoring system
- `tutor_system/enhanced_tutor.py` - Enhanced tutor with additional features

**Course Structure Integration:**
- Covers MAT 143 chapters: 1, 4, 5, 6, 7, 10, 11, 13
- Test schedule mapping: Test 1 (Ch 1,13), Test 2 (Ch 4,5), Test 3 (Ch 6,7), Test 4 (Ch 10,11)
- Hawkes Learning system integration for homework assignments

### Content Management
**Course Materials Organization:**
- `course_materials/` - Structured content including formula sheets, schedules, resources
- `public/course_materials/` - Public-facing course materials
- Formula sheets organized by unit and chapter with HTML conversion support

**English Materials:**
- Integrated research guides and writing resources from CPCC libraries
- Critical thinking and revision process materials
- Citation and plagiarism prevention resources

### Frontend Architecture
**Technology Stack:**
- Vanilla HTML/CSS/JavaScript with Tailwind CSS v3.4.1
- Radix UI components for enhanced UX (dialog, select, tabs, slot)
- Lucide icons (CDN)
- Custom retro design system with Vend Sans typography (via Google Fonts)

**Source Organization:**
- `src/styles/` - Design system CSS files (tokens-implementation.css, award-winning-design.css, main.css, adhd-friendly.css, accessibility.css)
- `src/components/` - Reusable UI components
- `src/js/` - JavaScript modules (e.g., study-planner.js)
- `src/lib/` - Utility functions
- `tokens.json` - Design token definitions (colors, spacing, typography)

**Design System:**
- WCAG 2.1 AA accessibility compliance (verified with check_accessibility.py)
- Retro color palette optimized for ADHD-friendly design
- Semantic color tokens: math (green), English (blue), warnings (red), success (green)
- High contrast minimal flat design
- Mobile-first responsive approach

### Build Configuration
**Vite Setup (vite.config.js):**
- Multi-entry point configuration for HTML pages in root directory
- Active entry points: index, calendar, tutor, formulaLookup, englishMaterials, chapter-1, chapter-4, chapter-6, chapter-7, chapter-13
- Temporarily disabled: chapter-5, chapter-10, chapter-11 (CSS parsing issues - need investigation)
- PostCSS integration with @tailwindcss/postcss and autoprefixer via postcss.config.js
- Development server configured for port 3000 (run with `npx vite`)
- Build output to `dist/` directory
- Note: npm scripts only handle Tailwind CSS compilation, not Vite server

**Deployment (Vercel):**
- Platform: Vercel serverless functions for API endpoints
- Configuration: `vercel.json` includes security headers (no buildCommand/devCommand needed)
- Security headers: X-Content-Type-Options, X-Frame-Options, X-XSS-Protection, Referrer-Policy
- Python runtime for serverless functions in `api/` directory
- API endpoints auto-deployed from `api/*.py` files (e.g., `/api/tutor`, `/api/english_tutor`)
- Static HTML/CSS/JS files served directly from root (no build output needed for deployment)
- `requirements.txt` installed automatically via `installCommand` in vercel.json

### Key Scripts & Automation
The `scripts/` directory contains numerous Python utilities for:
- Accessibility testing and fixes
- Link checking and repair
- Content conversion (Markdown to HTML)
- Color accessibility verification
- HTML structure validation

### Session Management & Personalization
The tutoring system is specifically designed for "Kristina" with:
- Personalized encouragement and patience
- Math anxiety awareness and support
- Connection to specific CPCC course requirements
- Executive function support features

## Development Guidelines

**Tech Stack Restrictions:**
- Use vanilla HTML/CSS/JavaScript only - do NOT introduce heavy frameworks (React, Vue, etc.)
- Styling must use Tailwind CSS v3.4.1 with the custom design system in `src/styles/` and `tokens.json`
- Backend/API functions must be Python-based in the `api/` directory for Vercel serverless deployment
- Icons: Lucide (CDN); Fonts: Vend Sans (Google Fonts)

**Code Quality Standards:**
- Write semantic HTML with proper heading hierarchy and ARIA labels
- Design mobile-first and maintain WCAG 2.1 AA compliance
- Break content into digestible sections for ADHD-friendly design
- Keep design minimal - avoid unnecessary animations or visual clutter
- Use consistent padding, spacing, and component styles from design system

**Content Scope:**
- Base all work on official MAT 143 and ENG 111 syllabi
- Focus on academic success and executive function support features
- Do NOT add features unrelated to academics (social sharing, gamification, etc.)
- The `_archived/` directory contains outdated code - do not reference it
- Core sections: Dashboard (progress tracking), Calendar (16-week timeline), Math Tutor (chapter pages), Writing Coach (essay guides), Resource Center (formula lookup)

## Important Notes

**Environment & Configuration:**
- AI tutoring requires `ANTHROPIC_API_KEY` environment variable (set in Vercel project settings)
- API uses Anthropic's Claude model (claude-3-sonnet-20240229 in api/tutor.py)
- Fallback responses are implemented when API key is missing or services unavailable - gracefully degrades with helpful resource links
- API functions handle CORS for cross-origin requests from the frontend
- For local API testing, use Vercel CLI: `vercel dev` (requires Vercel account and project link)

**Known Issues:**
- Chapter pages 5, 10, 11 temporarily disabled in Vite config due to CSS parsing issues
- Various `-broken`, `-old`, `-new` HTML files exist from design iterations

**Course Alignment:**
- Content specifically aligned with CPCC's MAT 143 and ENG 111 curricula
- Semester dates: Aug 18 - Dec 12, 2025
- Test schedule: Test 1 (Ch 1,13), Test 2 (Ch 4,5), Test 3 (Ch 6,7), Test 4 (Ch 10,11)