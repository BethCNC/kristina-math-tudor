/**
 * Achievement Toast Notification System
 * ADHD Accessibility: Provides immediate positive feedback for completions
 * Uses role="status" and aria-live="polite" for screen reader announcements
 */

class AchievementSystem {
  constructor() {
    this.container = null;
    this.init();
  }

  init() {
    // Create toast container
    this.container = document.createElement('div');
    this.container.className = 'achievement-toast-container';
    this.container.setAttribute('aria-live', 'polite');
    this.container.setAttribute('aria-atomic', 'true');
    document.body.appendChild(this.container);

    // Listen for progress events
    window.addEventListener('progressUpdated', (e) => this.handleProgressUpdate(e));
  }

  /**
   * Handle progress update events and show appropriate toast
   */
  handleProgressUpdate(event) {
    const { chapterId, sectionId, percentComplete } = event.detail;
    
    if (percentComplete === 100) {
      this.showToast({
        type: 'success',
        title: 'Section Complete!',
        message: `Great job finishing Section ${sectionId}!`,
        icon: 'check-circle',
        duration: 4000
      });
    } else if (percentComplete === 50) {
      this.showToast({
        type: 'info',
        title: 'Halfway There!',
        message: `You're making great progress on Section ${sectionId}`,
        icon: 'trending-up',
        duration: 3000
      });
    }
  }

  /**
   * Show a toast notification
   * @param {Object} options - Toast configuration
   */
  showToast({ type = 'info', title, message, icon = 'info', duration = 3000 }) {
    const toast = document.createElement('div');
    toast.className = `achievement-toast achievement-toast-${type}`;
    toast.setAttribute('role', 'status');
    
    toast.innerHTML = `
      <div class="achievement-toast-icon">
        <i data-lucide="${icon}" class="w-5 h-5"></i>
      </div>
      <div class="achievement-toast-content">
        <div class="achievement-toast-title">${title}</div>
        <div class="achievement-toast-message">${message}</div>
      </div>
      <button class="achievement-toast-close" aria-label="Close notification" onclick="this.parentElement.remove()">
        <i data-lucide="x" class="w-4 h-4"></i>
      </button>
    `;

    this.container.appendChild(toast);

    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }

    // Auto-remove after duration
    setTimeout(() => {
      toast.classList.add('hiding');
      setTimeout(() => toast.remove(), 300);
    }, duration);
  }

  /**
   * Show custom achievement
   * @param {string} achievementType - Type of achievement
   */
  showAchievement(achievementType) {
    const achievements = {
      'first-section': {
        title: 'First Steps!',
        message: 'You completed your first section!',
        icon: 'award',
        type: 'success'
      },
      'chapter-complete': {
        title: 'Chapter Mastered!',
        message: 'Excellent work completing this chapter!',
        icon: 'trophy',
        type: 'success'
      },
      'streak-3': {
        title: '3-Day Streak!',
        message: 'You\'ve studied 3 days in a row!',
        icon: 'flame',
        type: 'success'
      },
      'practice-complete': {
        title: 'Practice Makes Perfect!',
        message: 'You finished all practice problems!',
        icon: 'target',
        type: 'success'
      }
    };

    const achievement = achievements[achievementType];
    if (achievement) {
      this.showToast(achievement);
    }
  }
}

// Create global instance
const achievementSystem = new AchievementSystem();

// Export for global use
window.achievementSystem = achievementSystem;

// Helper function for manual triggers
window.showAchievement = (type) => achievementSystem.showAchievement(type);
