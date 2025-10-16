# Deployment Guide - Kristina's Academic Dashboard

## Quick Start (5 Minutes to Deploy)

### 1. Install Dependencies
```bash
npm install
```

### 2. Build Tailwind CSS
```bash
npm run build
# Or for development with auto-rebuild:
npm run dev
```

### 3. Set Up Environment Variable
Create a `.env` file (never commit this):
```bash
ANTHROPIC_API_KEY=your_api_key_from_anthropic_console
```

Get your API key from: https://console.anthropic.com/

### 4. Deploy to Vercel (Recommended)

#### Option A: GitHub Integration (Easiest)
1. Push your code to GitHub
2. Go to https://vercel.com
3. Click "New Project"
4. Import your repository
5. Add environment variable:
   - Key: `ANTHROPIC_API_KEY`
   - Value: Your API key from step 3
6. Click "Deploy"

Vercel will automatically:
- Detect the serverless function in `/api/tutor.py`
- Build your Tailwind CSS
- Deploy to a global CDN
- Provide HTTPS

#### Option B: Vercel CLI
```bash
npm install -g vercel
vercel login
vercel

# Add environment variable
vercel env add ANTHROPIC_API_KEY
```

### 5. Test the Deployment
1. Visit your deployed URL
2. Navigate to "AI Math Tutor"
3. Ask a question (e.g., "How do I calculate compound interest?")
4. Verify the AI responds (not fallback message)

---

## Alternative Deployment Options

### Netlify
1. Connect your GitHub repository
2. Build command: `npm run build`
3. Publish directory: `./`
4. Add environment variable in Netlify UI:
   - `ANTHROPIC_API_KEY`
5. Deploy

**Note:** You'll need to configure Netlify Functions for the `/api/tutor` endpoint.

### Local Development Server
```bash
# Terminal 1: Build CSS
npm run dev

# Terminal 2: Serve files
python3 -m http.server 8000
# Or use: npx serve .

# Visit: http://localhost:8000
```

**Note:** AI tutor won't work locally without API proxy setup.

---

## File Structure
```
kristina_math_tutor/
├── index.html                  # Dashboard (entry point)
├── calendar.html               # 16-week semester calendar
├── tutor.html                  # AI math tutor interface
├── english_materials.html      # Writing coach
├── chapter-*.html              # Individual chapter pages
├── api/
│   └── tutor.py               # Serverless AI tutor endpoint
├── src/
│   ├── js/
│   │   └── tutor.js           # Frontend tutor integration
│   └── styles/
│       ├── globals.css        # Global styles entry point
│       └── design-system.css  # Component library
├── tailwind.config.js         # Tailwind configuration
├── package.json               # Node dependencies
└── requirements.txt           # Python dependencies
```

---

## Environment Variables

### Required
- `ANTHROPIC_API_KEY` - Your Anthropic API key for AI tutor functionality

### Optional
- `ANTHROPIC_MODEL` - Claude model version (default: claude-3-sonnet-20240229)

---

## Updating Content

### Changing Semester Dates
Edit `calendar.html` and update:
- Semester start/end dates
- EVA deadline
- Withdrawal deadline
- Test dates (Weeks 4, 7, 11, 16)

### Adding New Formulas
1. Navigate to the appropriate chapter HTML file
2. Add a new `.formula-card` div in the formulas section
3. Follow the existing pattern:
```html
<div class="formula-card">
    <h3 class="text-xl font-semibold mb-3 text-emerald-900 dark:text-emerald-100">
        Formula Name
    </h3>
    <p class="formula">Formula Here</p>
    <p class="text-sm mt-2">Description...</p>
    <div class="example">
        <strong>Example:</strong> Worked example...
    </div>
</div>
```

### Updating Progress Tracking
Edit `index.html`:
- Find the progress bars in the "Course Progress" section
- Update `style="width: XX%"` attribute
- Update `aria-valuenow="XX"` for accessibility

---

## Troubleshooting

### AI Tutor Shows Fallback Message
**Cause:** ANTHROPIC_API_KEY not set or invalid  
**Fix:**
1. Check environment variable is set in hosting platform
2. Verify API key is valid at https://console.anthropic.com/
3. Redeploy after setting variable

### Styles Not Loading
**Cause:** Tailwind CSS not compiled  
**Fix:**
```bash
npm run build
# Or for development:
npm run dev
```

### Mobile Menu Not Working
**Cause:** JavaScript not loading  
**Fix:**
- Check browser console for errors
- Verify Lucide CDN is accessible
- Ensure mobile-menu-button ID exists in HTML

---

## Browser Support

### Tested & Supported
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile Safari (iOS 14+)
- ✅ Chrome Mobile (Android 10+)

### Known Issues
- None at this time

---

## Accessibility Statement

This dashboard is designed to meet WCAG 2.1 Level AA standards:
- ✅ Color contrast ratios of 4.5:1 for normal text
- ✅ Keyboard navigable interface
- ✅ Screen reader compatible
- ✅ Mobile responsive (320px minimum width)
- ✅ Focus indicators on all interactive elements
- ✅ Semantic HTML with proper landmarks

For accessibility concerns, refer to `docs/accessibility_validation.md`

---

## Support & Maintenance

### Semester Updates
Before each new semester:
1. Update dates in `calendar.html`
2. Update current week number in `index.html`
3. Reset progress bars to 0%
4. Archive previous semester data if needed

### Content Updates
- Formula additions: Edit chapter HTML files
- New chapters: Create new `chapter-X.html` following existing template
- Essay updates: Edit `english_materials.html`

---

## Performance Optimization

### Current Optimizations
- ✅ Tailwind CSS purges unused styles
- ✅ Minimal JavaScript (vanilla, no frameworks)
- ✅ CDN-hosted fonts and icons
- ✅ Semantic HTML for fast parsing

### Future Optimizations (Optional)
- [ ] Image optimization (if images added)
- [ ] Service worker for offline support
- [ ] Progressive Web App (PWA) manifest
- [ ] Font subsetting for faster loads

---

## Security Considerations

### API Key Security
- ✅ API key stored as environment variable (not in code)
- ✅ Never committed to git (.env in .gitignore)
- ✅ CORS headers configured for security
- ✅ Graceful fallback prevents key exposure

### Best Practices
- Always use HTTPS in production (Vercel provides free SSL)
- Keep dependencies updated (`npm audit`, `pip list --outdated`)
- Monitor API usage to avoid unexpected charges

---

**Questions?** Check the full documentation in `/docs/` or refer to the implementation summary.

**Ready to Deploy!** 🚀

