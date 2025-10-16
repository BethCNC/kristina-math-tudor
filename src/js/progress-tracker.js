/**
 * Progress Tracker for ADHD Users
 * Saves and restores learning progress using localStorage
 * Prevents frustration from losing place during interrupted study sessions
 */

class ProgressTracker {
  constructor() {
    this.storageKey = 'kristina_math_progress';
    this.progress = this.loadProgress();
  }

  /**
   * Load progress from localStorage
   */
  loadProgress() {
    try {
      const stored = localStorage.getItem(this.storageKey);
      return stored ? JSON.parse(stored) : {};
    } catch (error) {
      console.error('Error loading progress:', error);
      return {};
    }
  }

  /**
   * Save progress to localStorage
   */
  saveProgress() {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(this.progress));
    } catch (error) {
      console.error('Error saving progress:', error);
    }
  }

  /**
   * Mark a section as complete
   * @param {string} chapterId - e.g., "chapter-4"
   * @param {string} sectionId - e.g., "4-1"
   * @param {number} percentComplete - 0-100
   */
  updateSection(chapterId, sectionId, percentComplete) {
    if (!this.progress[chapterId]) {
      this.progress[chapterId] = {
        sections: {},
        overallProgress: 0,
        lastAccessed: null
      };
    }

    this.progress[chapterId].sections[sectionId] = {
      percentComplete: percentComplete,
      completed: percentComplete >= 100,
      lastAccessed: new Date().toISOString()
    };

    this.progress[chapterId].lastAccessed = new Date().toISOString();
    
    // Calculate overall chapter progress
    this.calculateChapterProgress(chapterId);
    
    this.saveProgress();
    
    // Trigger custom event for UI updates
    window.dispatchEvent(new CustomEvent('progressUpdated', {
      detail: {
        chapterId,
        sectionId,
        percentComplete
      }
    }));
  }

  /**
   * Calculate overall chapter progress based on sections
   */
  calculateChapterProgress(chapterId) {
    const chapter = this.progress[chapterId];
    const sections = Object.values(chapter.sections);
    
    if (sections.length === 0) {
      chapter.overallProgress = 0;
      return;
    }

    const totalProgress = sections.reduce((sum, section) => sum + section.percentComplete, 0);
    chapter.overallProgress = Math.round(totalProgress / sections.length);
  }

  /**
   * Get progress for a specific section
   */
  getSectionProgress(chapterId, sectionId) {
    return this.progress[chapterId]?.sections[sectionId] || {
      percentComplete: 0,
      completed: false,
      lastAccessed: null
    };
  }

  /**
   * Get overall chapter progress
   */
  getChapterProgress(chapterId) {
    return this.progress[chapterId]?.overallProgress || 0;
  }

  /**
   * Get last accessed chapter for "Resume where you left off" feature
   */
  getLastAccessedChapter() {
    let lastChapter = null;
    let lastTime = null;

    Object.entries(this.progress).forEach(([chapterId, data]) => {
      if (data.lastAccessed) {
        const accessTime = new Date(data.lastAccessed);
        if (!lastTime || accessTime > lastTime) {
          lastTime = accessTime;
          lastChapter = chapterId;
        }
      }
    });

    return lastChapter;
  }

  /**
   * Get all progress data (for dashboard display)
   */
  getAllProgress() {
    return this.progress;
  }

  /**
   * Reset progress for a specific chapter or section
   */
  resetProgress(chapterId, sectionId = null) {
    if (sectionId) {
      if (this.progress[chapterId]?.sections[sectionId]) {
        delete this.progress[chapterId].sections[sectionId];
        this.calculateChapterProgress(chapterId);
      }
    } else {
      delete this.progress[chapterId];
    }
    
    this.saveProgress();
  }

  /**
   * Clear all progress (use with caution)
   */
  clearAllProgress() {
    if (confirm('Are you sure you want to clear all progress? This cannot be undone.')) {
      this.progress = {};
      this.saveProgress();
      window.location.reload();
    }
  }
}

// Create global instance
const progressTracker = new ProgressTracker();

// Auto-save progress indicator
let saveIndicator = null;

function showSaveIndicator() {
  // Create indicator if it doesn't exist
  if (!saveIndicator) {
    saveIndicator = document.createElement('div');
    saveIndicator.className = 'save-indicator';
    saveIndicator.setAttribute('role', 'status');
    saveIndicator.setAttribute('aria-live', 'polite');
    saveIndicator.innerHTML = `
      <i data-lucide="check-circle" class="w-4 h-4"></i>
      <span>Progress saved</span>
    `;
    document.body.appendChild(saveIndicator);
    
    // Initialize Lucide icon
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }
  }

  // Show indicator
  saveIndicator.classList.add('show');

  // Hide after 2 seconds
  setTimeout(() => {
    saveIndicator.classList.remove('show');
  }, 2000);
}

// Listen for progress updates
window.addEventListener('progressUpdated', () => {
  showSaveIndicator();
});

// Export for global use
window.progressTracker = progressTracker;

