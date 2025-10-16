/**
 * Chapter Page Initialization
 * Integrates all ADHD accessibility features for chapter/learning pages
 */

document.addEventListener('DOMContentLoaded', () => {
  // Get chapter ID from page title or URL
  const chapterId = getChapterIdFromPage();
  
  if (chapterId) {
    // Track that user accessed this chapter
    const lastSection = getLastSectionFromProgress(chapterId);
    if (lastSection) {
      // Highlight or scroll to last section
      highlightLastSection(lastSection);
    }
    
    // Auto-save progress when user interacts with lessons
    trackLessonProgress(chapterId);
  }
  
  // Re-initialize Lucide icons after any dynamic content
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
});

/**
 * Extract chapter ID from current page
 */
function getChapterIdFromPage() {
  // Try to get from URL
  const path = window.location.pathname;
  const match = path.match(/chapter-(\d+)/);
  if (match) {
    return `chapter-${match[1]}`;
  }
  
  // Try to get from title
  const titleMatch = document.title.match(/Chapter (\d+)/);
  if (titleMatch) {
    return `chapter-${titleMatch[1]}`;
  }
  
  return null;
}

/**
 * Get last accessed section from progress
 */
function getLastSectionFromProgress(chapterId) {
  if (!window.progressTracker) return null;
  
  const chapterProgress = window.progressTracker.progress[chapterId];
  if (!chapterProgress) return null;
  
  // Find the section with most recent access that's not complete
  let lastSection = null;
  let lastTime = null;
  
  Object.entries(chapterProgress.sections).forEach(([sectionId, data]) => {
    if (!data.completed && data.lastAccessed) {
      const accessTime = new Date(data.lastAccessed);
      if (!lastTime || accessTime > lastTime) {
        lastTime = accessTime;
        lastSection = sectionId;
      }
    }
  });
  
  return lastSection;
}

/**
 * Highlight the last accessed section
 */
function highlightLastSection(sectionId) {
  const sectionCard = document.querySelector(`[aria-labelledby="section-${sectionId}"]`);
  if (sectionCard) {
    // Add visual highlight
    sectionCard.style.boxShadow = '0 0 0 3px var(--color-brand-default)';
    
    // Scroll into view after a brief delay
    setTimeout(() => {
      sectionCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }, 500);
  }
}

/**
 * Track lesson progress
 */
function trackLessonProgress(chapterId) {
  // Track when user clicks lesson buttons
  const lessonButtons = document.querySelectorAll('[onclick^="showLesson"]');
  lessonButtons.forEach(button => {
    button.addEventListener('click', () => {
      const sectionMatch = button.getAttribute('onclick').match(/showLesson\('(.+?)'\)/);
      if (sectionMatch && window.progressTracker) {
        const sectionId = sectionMatch[1];
        // Mark as 50% complete when viewed (arbitrary milestone)
        window.progressTracker.updateSection(chapterId, sectionId, 50);
      }
    });
  });
  
  // Track when user reveals solutions
  const solutionButtons = document.querySelectorAll('[onclick^="showSolution"]');
  solutionButtons.forEach((button, index) => {
    button.addEventListener('click', () => {
      // Could track individual practice problem completion
      console.log(`Practice problem ${index + 1} attempted`);
    });
  });
}

// Make globally available
window.chapterInit = {
  getChapterIdFromPage,
  getLastSectionFromProgress,
  highlightLastSection,
  trackLessonProgress
};

