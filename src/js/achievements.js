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
   * @param {Object} replacements - Values to replace in messages (e.g., {chapter: 6})
   */
  showAchievement(achievementType, replacements = {}) {
    const achievements = {
      'first-section': {
        title: '🎯 First Steps!',
        message: 'You completed your first section! You\'re off to a great start!',
        icon: 'award',
        type: 'success',
        confetti: true
      },
      'chapter-complete': {
        title: '🎉 Chapter Mastered!',
        message: 'Excellent work! One step closer to acing Test {testNum}!',
        icon: 'trophy',
        type: 'success',
        confetti: true
      },
      'chapter-50-percent': {
        title: '⭐ Halfway There!',
        message: 'You\'re crushing it! Keep going!',
        icon: 'trending-up',
        type: 'info',
        confetti: false
      },
      'streak-3': {
        title: '🔥 3-Day Streak!',
        message: 'You\'ve studied 3 days in a row! Consistency is 🔑!',
        icon: 'flame',
        type: 'success',
        confetti: true
      },
      'streak-7': {
        title: '⚡ 7-Day Streak!',
        message: 'A full week! You\'re unstoppable!',
        icon: 'zap',
        type: 'success',
        confetti: true
      },
      'practice-complete': {
        title: '💪 Practice Complete!',
        message: 'You finished all practice problems! The formulas are clicking!',
        icon: 'target',
        type: 'success',
        confetti: false
      },
      'hawkes-ch-complete': {
        title: '✅ Hawkes Chapter Done!',
        message: 'That\'s {percent}% of your grade secured! Keep going!',
        icon: 'check-circle',
        type: 'success',
        confetti: true
      },
      'hawkes-all-complete': {
        title: '🏆 ALL HAWKES COMPLETE!',
        message: '20% of your grade is LOCKED IN! You\'re killing it!',
        icon: 'trophy',
        type: 'success',
        confetti: true,
        duration: 6000
      },
      'essay-started': {
        title: '✍️ Essay Started!',
        message: 'Getting started is huge - you\'ve got this!',
        icon: 'pen-tool',
        type: 'info',
        confetti: false
      },
      'essay-submitted': {
        title: '🚀 Essay Submitted!',
        message: 'Another essay down! You\'re unstoppable!',
        icon: 'send',
        type: 'success',
        confetti: true
      },
      'test-prep-ready': {
        title: '🎯 Test Prep Complete!',
        message: 'All chapters for Test {testNum} reviewed - you\'re ready!',
        icon: 'check-circle',
        type: 'success',
        confetti: true,
        duration: 6000
      },
      'study-25min': {
        title: '⏱️ 25 Minutes of Focus!',
        message: 'Solid study session! Your brain is leveling up!',
        icon: 'clock',
        type: 'info',
        confetti: false
      },
      'study-1hour': {
        title: '💪 1 Hour of Study!',
        message: 'Wow! That\'s dedication! Take a well-earned break!',
        icon: 'award',
        type: 'success',
        confetti: true
      }
    };

    const achievement = achievements[achievementType];
    if (achievement) {
      // Replace placeholders in message
      let message = achievement.message;
      Object.keys(replacements).forEach(key => {
        message = message.replace(`{${key}}`, replacements[key]);
      });

      this.showToast({
        ...achievement,
        message: message
      });

      // Show confetti for major achievements
      if (achievement.confetti) {
        this.showConfetti();
      }

      // Save to achievement history
      this.saveToHistory(achievementType, message);
    }
  }

  /**
   * Show confetti animation
   */
  showConfetti() {
    const colors = ['#2563eb', '#059669', '#d97706', '#dc2626', '#7c3aed'];
    const confettiCount = 30;

    for (let i = 0; i < confettiCount; i++) {
      const confetti = document.createElement('div');
      confetti.style.cssText = `
        position: fixed;
        top: 80px;
        right: ${180 + Math.random() * 100}px;
        width: 10px;
        height: 10px;
        background: ${colors[Math.floor(Math.random() * colors.length)]};
        opacity: 0.8;
        z-index: 10000;
        border-radius: 50%;
        pointer-events: none;
      `;

      // Add confetti animation
      confetti.animate([
        { transform: 'translateY(0) rotate(0deg)', opacity: 0.8 },
        { transform: `translateY(100vh) rotate(${360 + Math.random() * 360}deg)`, opacity: 0 }
      ], {
        duration: 2000 + Math.random() * 1000,
        easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
      });

      document.body.appendChild(confetti);

      setTimeout(() => confetti.remove(), 3000);
    }
  }

  /**
   * Save achievement to history
   */
  saveToHistory(type, message) {
    const history = JSON.parse(localStorage.getItem('kristina_achievement_history') || '[]');

    history.push({
      type: type,
      message: message,
      timestamp: Date.now(),
      date: new Date().toISOString()
    });

    // Keep last 50 achievements
    if (history.length > 50) {
      history.shift();
    }

    localStorage.setItem('kristina_achievement_history', JSON.stringify(history));
  }

  /**
   * Get total achievement count
   */
  getAchievementCount() {
    const history = JSON.parse(localStorage.getItem('kristina_achievement_history') || '[]');
    return history.length;
  }
}

// Create global instance
const achievementSystem = new AchievementSystem();

// Export for global use
window.achievementSystem = achievementSystem;

// Helper function for manual triggers
window.showAchievement = (type) => achievementSystem.showAchievement(type);
