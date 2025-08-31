# 🚀 MAT 143 Tutor Deployment Guide

Complete guide for deploying and using the MAT 143 AI tutoring system.

## 📋 Quick Start Options

### Option 1: Web-Based (Recommended for Production)
```bash
# Start the development server
npm run dev

# Or build for production
npm run build
npm run preview
```

### Option 2: Python AI Tutor (Full Features)
```bash
# Install dependencies
pip3 install -r requirements.txt

# Set up API key
export ANTHROPIC_API_KEY="your_key_here"

# Run the enhanced tutor
python3 tutor_system/enhanced_tutor.py
```

### Option 3: Static HTML Files (No Setup Required)
Simply open any of these files in your browser:
- `index.html` - Landing page
- `tutor.html` - Web-based tutor interface
- `reference.html` - Formula and concept reference
- `calendar_study_system.html` - Interactive calendar
- `web_study_helper.html` - Study helper

## 🌐 Production Deployment

### Vercel Deployment (Recommended)

1. **Connect to Vercel:**
   ```bash
   # Install Vercel CLI
   npm i -g vercel
   
   # Deploy
   vercel
   ```

2. **Environment Variables:**
   - Add `ANTHROPIC_API_KEY` in Vercel dashboard
   - Set to your Anthropic API key

3. **Custom Domain (Optional):**
   - Add custom domain in Vercel dashboard
   - Configure DNS settings

### Netlify Deployment

1. **Connect to Netlify:**
   ```bash
   # Install Netlify CLI
   npm install -g netlify-cli
   
   # Deploy
   netlify deploy
   ```

2. **Environment Variables:**
   - Add `ANTHROPIC_API_KEY` in Netlify dashboard

### GitHub Pages

1. **Build the project:**
   ```bash
   npm run build
   ```

2. **Deploy to GitHub Pages:**
   - Push to GitHub repository
   - Enable GitHub Pages in repository settings
   - Set source to `/docs` or `/gh-pages` branch

## 🔧 Local Development

### Prerequisites
- Node.js 16+ 
- Python 3.7+
- Anthropic API key

### Setup Steps

1. **Clone and Install:**
   ```bash
   cd /Users/bethcartrette/REPOS/kristina_math_tutor
   npm install
   pip3 install -r requirements.txt
   ```

2. **Environment Setup:**
   ```bash
   # Add to ~/.zshrc or ~/.bashrc
   export ANTHROPIC_API_KEY="your_api_key_here"
   source ~/.zshrc
   ```

3. **Organize Course Materials:**
   ```bash
   python3 organize_files.py
   ```

### Development Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run Python tutor
python3 tutor_system/enhanced_tutor.py

# Run basic tutor
python3 tutor_system/mat143_tutor.py
```

## 📱 Usage Scenarios

### For Students (Kristina)

**Daily Study Routine:**
1. Open `calendar_study_system.html` to see what's due
2. Use `reference.html` for quick formula lookups
3. Use `tutor.html` for interactive help
4. Run Python tutor for detailed explanations

**Test Preparation:**
1. Check test dates in calendar system
2. Review relevant formulas in reference
3. Practice with AI tutor
4. Use study strategies from reference guide

### For Instructors

**Course Management:**
1. Update course materials in `course_materials/`
2. Modify calendar dates in `calendar_study_system.html`
3. Add new formulas to `reference.html`
4. Update AI tutor prompts in Python files

## 🔐 Security Considerations

### API Key Management
- Never commit API keys to version control
- Use environment variables in production
- Rotate keys regularly
- Monitor API usage

### Data Privacy
- No personal data is stored
- All interactions are temporary
- Course materials are local only

## 🛠️ Customization

### Adding New Content

**New Formulas:**
1. Add to `reference.html` in the formulas section
2. Update `course_materials/formula_sheets/`
3. Add to AI tutor knowledge base

**New Chapters:**
1. Update chapter structure in Python tutors
2. Add to calendar system
3. Create new formula sheets
4. Update navigation in HTML files

**Styling Changes:**
1. Modify CSS variables in HTML files
2. Update `tokens.json` for design system
3. Rebuild with `npm run build`

### AI Tutor Customization

**Prompt Engineering:**
- Edit prompts in `tutor_system/enhanced_tutor.py`
- Adjust tone and style for different audiences
- Add specific examples and explanations

**Knowledge Base:**
- Add new course materials to `course_materials/`
- Update chapter definitions
- Modify test schedules

## 📊 Analytics & Monitoring

### Usage Tracking
```javascript
// Add to HTML files for basic analytics
const trackEngagement = (action) => {
  console.log(`User engagement: ${action}`, {
    timestamp: new Date().toISOString(),
    page: window.location.pathname
  });
};
```

### Performance Monitoring
- Monitor API response times
- Track user engagement patterns
- Monitor error rates

## 🐛 Troubleshooting

### Common Issues

**API Key Errors:**
```bash
# Check if key is set
echo $ANTHROPIC_API_KEY

# Re-set the key
export ANTHROPIC_API_KEY="your_key_here"
```

**Python Dependencies:**
```bash
# Reinstall dependencies
pip3 install -r requirements.txt --force-reinstall

# Check Python version
python3 --version
```

**Build Issues:**
```bash
# Clear cache and rebuild
rm -rf node_modules package-lock.json
npm install
npm run build
```

**File Organization:**
```bash
# Re-run organization script
python3 organize_files.py

# Check file permissions
ls -la course_materials/
```

### Getting Help

1. **Check the logs:**
   - Browser console for web issues
   - Terminal output for Python issues

2. **Verify setup:**
   - Run `setup.sh` to check configuration
   - Test each component individually

3. **Common solutions:**
   - Restart development server
   - Clear browser cache
   - Reinstall dependencies

## 📈 Performance Optimization

### Web Performance
- Images are optimized and inline
- CSS is minified in production
- JavaScript is bundled efficiently
- Static assets are cached

### AI Performance
- Responses are cached where possible
- API calls are optimized
- Error handling prevents crashes

## 🔄 Updates & Maintenance

### Regular Maintenance
- Update dependencies monthly
- Monitor API usage and costs
- Backup course materials
- Test all components

### Version Control
```bash
# Commit changes
git add .
git commit -m "Update: [description]"
git push

# Create releases
git tag v1.0.0
git push origin v1.0.0
```

## 🎯 Success Metrics

### Student Success
- Test scores improvement
- Assignment completion rates
- Time spent studying
- Confidence levels

### System Performance
- API response times
- User engagement
- Error rates
- Usage patterns

## 📞 Support

### For Technical Issues
- Check this deployment guide
- Review error logs
- Test in different environments

### For Content Updates
- Modify course materials directly
- Update AI prompts
- Adjust calendar dates

### For New Features
- Extend HTML interfaces
- Add new Python functions
- Update design system

---

## 🎉 Deployment Checklist

- [ ] Environment variables set
- [ ] Dependencies installed
- [ ] Course materials organized
- [ ] API key configured
- [ ] All HTML files working
- [ ] Python tutors functional
- [ ] Calendar system updated
- [ ] Reference materials complete
- [ ] Styling consistent
- [ ] Mobile responsive
- [ ] Performance optimized
- [ ] Error handling in place
- [ ] Documentation updated

**You're ready to deploy! 🚀**

The MAT 143 tutor system is now complete and ready for production use. Choose the deployment method that best fits your needs and get started helping Kristina succeed in math!
