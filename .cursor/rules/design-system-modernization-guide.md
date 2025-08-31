# Design System Modernization Guide

## Project Overview

This document outlines the process for modernizing Kristina's Academic Success Dashboard by integrating the sophisticated Figma-based design system with the existing educational content.

## Current Architecture Analysis

### Existing System
- **Framework**: Vanilla HTML/CSS/JavaScript with Vite bundling
- **Styling**: Custom CSS framework with semantic design tokens
- **Content**: 8,000+ lines across 14 HTML files (MAT 143 & ENG 111 educational content)
- **AI Integration**: Python Flask backend with Anthropic Claude API
- **Deployment**: Vercel with proper security headers

### Design System Foundation
- **Location**: `/figma-tailwind-cookiecutter/`
- **Framework**: Next.js 15.3.5 + TypeScript + Tailwind CSS 4.1
- **Components**: Customized shadcn/ui with Figma-aligned tokens
- **Automation**: Scripts for Figma-to-code synchronization
- **Color System**: OKLCH color space with semantic mappings
- **Typography**: Host Grotesk + Space Mono with 12 semantic font classes

## Design System Architecture

### Color Token Structure
```css
/* Primitive Colors */
--color-amethyst-500: oklch(0.767 0.098 312.9);
--color-aquamarine-300: oklch(0.820 0.080 248.8);
--color-smokey-quartz-950: oklch(0.214 0.002 67.7);

/* Semantic Mappings */
--color-brand: var(--color-aquamarine-300);
--color-text-primary: var(--color-smokey-quartz-950);
--color-background: var(--color-red-50);
```

### Typography Scale
- `.font-display` - 60px, medium, tight tracking (hero text)
- `.font-title-large` - 64px, bold (page titles)
- `.font-title` - 48px, medium (section headers)
- `.font-title-small` - 20px, medium (card titles)
- `.font-body-large` - 18px, normal (large body text)
- `.font-body-regular` - 16px, normal (standard body text)
- `.font-button` - 14px, medium (interactive elements)
- `.font-caption` - 12px, normal (supplementary text)

### Available Components
- **Button**: 6 variants (default, destructive, outline, secondary, ghost, link)
- **Input**: Standard + compact variants with error states
- **Radix UI Primitives**: Accessible foundation components
- **Custom Components**: Hedgehog counter/stats examples

## Migration Strategy

### Phase 1: Foundation Setup (Week 1)
1. **Security Hardening** (CRITICAL)
   - Remove API key from `.env` file
   - Implement environment variable system
   - Add authentication to AI endpoints
   - Configure rate limiting

2. **Design System Integration**
   - Move `figma-tailwind-cookiecutter/src/app/globals.css` to main project
   - Update root `tailwind.config.js` to use Figma-synced tokens
   - Integrate Figma sync scripts into main build process
   - Update `components.json` to match design system setup

### Phase 2: Component Migration (Weeks 2-3)
1. **Create Next.js Foundation**
   - Set up Next.js app directory structure
   - Migrate static HTML content to Next.js pages
   - Implement layout components using design system

2. **Convert Core UI Elements**
   ```typescript
   // Old: Static HTML
   <div class="bg-background-secondary border border-border rounded-xl p-6">
     <h2 class="font-title-small">MAT 143</h2>
   </div>

   // New: React with design system
   <Card className="bg-background-secondary">
     <CardHeader>
       <CardTitle className="font-title-small">MAT 143</CardTitle>
     </CardHeader>
   </Card>
   ```

### Phase 3: Educational Content Integration (Weeks 4-5)
1. **Chapter Page Migration**
   - Convert chapter-*.html files to Next.js pages
   - Implement reusable components for mathematical content
   - Create quiz/exercise components using design system

2. **AI Tutor Interface**
   - Build React components for AI chat interface
   - Implement proper error handling and loading states
   - Use design system tokens for consistent styling

### Phase 4: Advanced Features (Week 6+)
1. **Calendar System Enhancement**
   - Migrate calendar.js to React component
   - Implement date picker using Radix UI
   - Add proper state management

2. **Progressive Web App Features**
   - Implement service worker
   - Add offline capabilities
   - Enhance mobile experience

## File Structure After Migration

```
kristina_math_tutor/
├── app/                          # Next.js app directory
│   ├── layout.tsx               # Root layout with design system
│   ├── page.tsx                 # Dashboard (index.html content)
│   ├── calendar/page.tsx        # Calendar system
│   ├── tutor/page.tsx          # AI tutor interface
│   └── chapter-[id]/page.tsx   # Dynamic chapter pages
├── components/
│   ├── ui/                     # shadcn/ui components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── input.tsx
│   │   └── ...
│   ├── educational/            # Custom educational components
│   │   ├── chapter-card.tsx
│   │   ├── progress-indicator.tsx
│   │   ├── math-formula.tsx
│   │   └── quiz-component.tsx
│   └── layout/                 # Layout components
│       ├── header.tsx
│       ├── navigation.tsx
│       └── footer.tsx
├── lib/
│   ├── utils.ts               # Utility functions
│   ├── ai-client.ts          # AI API integration
│   └── course-data.ts        # Course content management
├── styles/
│   └── globals.css           # Design system CSS
├── public/                   # Static assets
├── api/                      # API routes (migrated Python logic)
└── scripts/                  # Figma sync scripts
    ├── sync-figma-colors.js
    └── sync-figma-fonts.js
```

## Development Workflow

### Design Token Updates
```bash
# When design changes in Figma
npm run build:colors  # Sync color tokens
npm run build:fonts   # Sync typography
npm run dev           # See changes immediately
```

### Component Development
1. **Create in Figma** - Design component with proper tokens
2. **Sync Tokens** - Run sync scripts to update CSS variables
3. **Build Component** - Create React component using shadcn patterns
4. **Document Usage** - Add to component library documentation

### Quality Assurance
- **Type Safety**: All components use TypeScript
- **Accessibility**: Radix UI primitives ensure WCAG compliance
- **Design Consistency**: Semantic tokens prevent color/typography drift
- **Performance**: Next.js optimization + proper bundling

## Critical Considerations

### Security (IMMEDIATE)
- API keys must be moved to secure environment variables
- Authentication layer required for AI endpoints
- Rate limiting essential to prevent cost overruns

### Performance
- Large project size (607MB) - optimize node_modules
- HTML files total 717KB - component-based approach will improve caching
- CDN dependencies should be self-hosted for reliability

### Maintainability
- Single source of truth for design decisions (Figma)
- Automated token synchronization reduces manual updates
- Type-safe components prevent runtime errors
- Clear separation between educational content and UI logic

## Success Metrics

### Technical
- [ ] All components use semantic design tokens
- [ ] Design changes sync automatically from Figma
- [ ] TypeScript coverage at 100%
- [ ] Lighthouse scores > 90 across all metrics

### User Experience
- [ ] Consistent visual design across all pages
- [ ] Improved mobile responsiveness
- [ ] Faster page load times
- [ ] Enhanced accessibility compliance

### Developer Experience
- [ ] Component library documentation
- [ ] Clear development workflow
- [ ] Automated testing pipeline
- [ ] Easy content updates

## Next Steps

1. **Immediate**: Address security vulnerabilities
2. **Week 1**: Set up foundation with design system integration
3. **Week 2-3**: Begin component migration starting with dashboard
4. **Week 4-5**: Migrate educational content with proper React structure
5. **Ongoing**: Iterate and improve based on usage patterns

## Resources

- [shadcn/ui Documentation](https://ui.shadcn.com/)
- [Radix UI Primitives](https://www.radix-ui.com/primitives)
- [Next.js App Router](https://nextjs.org/docs/app)
- [Tailwind CSS 4.0 Alpha](https://tailwindcss.com/blog/tailwindcss-v4-alpha)
- [Figma Design System](https://www.figma.com/community/file/1526688065982358612)

---

**This guide should be updated as the migration progresses and new requirements are identified.**