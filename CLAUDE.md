# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Development Commands

**Development Server:**
```bash
npm run dev        # Start Vite dev server on port 3000
```

**Build & Deploy:**
```bash
npm run build      # Build for production using Vite
npm run preview    # Preview production build locally
```

**Python Scripts:**
```bash
python scripts/check_accessibility.py        # Run accessibility audit
python scripts/check_links.py               # Check for broken links
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
- `api/tutor.py` - Main Vercel serverless function for math tutoring
- `api/english_tutor.py` - English writing assistance API
- `tutor_system/mat143_tutor.py` - Comprehensive local tutoring system

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
- Vanilla HTML/CSS/JavaScript with Tailwind CSS v4
- Radix UI components for enhanced UX
- Lucide React icons
- Custom retro design system with Vend Sans typography

**Design System:**
- WCAG 2.1 AA accessibility compliance
- Retro color palette optimized for ADHD-friendly design
- High contrast minimal flat design
- Mobile-first responsive approach

### Build Configuration
**Vite Setup:**
- Multi-entry point configuration for all HTML pages
- PostCSS integration with Tailwind CSS
- Development server on port 3000
- Some chapter pages temporarily disabled due to CSS parsing issues

**Deployment:**
- Vercel platform with custom routing rules
- Security headers configuration
- API endpoints for AI tutoring functionality
- Static asset optimization

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

## Important Notes

- The AI tutoring requires `ANTHROPIC_API_KEY` environment variable
- Some chapter pages are temporarily disabled in the Vite config due to CSS issues
- The system includes extensive fallback responses for when AI services are unavailable
- Course content is specifically aligned with CPCC's MAT 143 and ENG 111 curricula