/**
 * ADHD Break System
 * Provides periodic rest stops to reduce attention fatigue
 * Tracks study time and suggests breaks at appropriate intervals
 */

class BreakSystem {
  constructor(options = {}) {
    this.breakInterval = options.breakInterval || 15; // minutes
    this.breakDuration = options.breakDuration || 5; // minutes
    this.studyStartTime = null;
    this.breakTimer = null;
    this.isOnBreak = false;
    this.storageKey = 'kristina_break_settings';
    
    this.loadSettings();
  }

  /**
   * Load user break preferences
   */
  loadSettings() {
    try {
      const stored = localStorage.getItem(this.storageKey);
      if (stored) {
        const settings = JSON.parse(stored);
        this.breakInterval = settings.breakInterval || 15;
        this.breakDuration = settings.breakDuration || 5;
      }
    } catch (error) {
      console.error('Error loading break settings:', error);
    }
  }

  /**
   * Save user break preferences
   */
  saveSettings() {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify({
        breakInterval: this.breakInterval,
        breakDuration: this.breakDuration
      }));
    } catch (error) {
      console.error('Error saving break settings:', error);
    }
  }

  /**
   * Start tracking study time
   */
  startStudying() {
    if (this.studyStartTime) return; // Already studying
    
    this.studyStartTime = Date.now();
    this.scheduleBreak();
  }

  /**
   * Schedule the next break reminder
   */
  scheduleBreak() {
    if (this.breakTimer) {
      clearTimeout(this.breakTimer);
    }

    this.breakTimer = setTimeout(() => {
      this.suggestBreak();
    }, this.breakInterval * 60 * 1000);
  }

  /**
   * Show break suggestion
   */
  suggestBreak() {
    const breakSection = this.createBreakSection();
    
    // Find a good place to insert the break (after current section)
    const main = document.querySelector('main');
    if (main) {
      const currentSection = main.querySelector('section:last-of-type');
      if (currentSection) {
        currentSection.insertAdjacentElement('afterend', breakSection);
        
        // Scroll to break
        breakSection.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    this.isOnBreak = true;
  }

  /**
   * Create break section HTML element
   */
  createBreakSection() {
    const section = document.createElement('section');
    section.className = 'adhd-break-section';
    section.setAttribute('aria-label', 'Take a study break');
    
    section.innerHTML = `
      <div class="adhd-break-card">
        <div class="adhd-break-icon" aria-hidden="true">
          <i data-lucide="coffee" class="w-8 h-8"></i>
        </div>
        <div class="adhd-break-content">
          <h3 class="adhd-break-title">Time for a Quick Break!</h3>
          <p class="adhd-break-message">
            You've been studying for ${this.breakInterval} minutes. Taking short breaks helps with focus and retention.
          </p>
          <div class="adhd-break-suggestions">
            <p class="text-sm font-medium mb-2">Quick break ideas (${this.breakDuration} min):</p>
            <ul class="text-sm space-y-1">
              <li>• Stretch and walk around</li>
              <li>• Get water or a healthy snack</li>
              <li>• Look away from screen (20-20-20 rule)</li>
              <li>• Deep breathing exercises</li>
            </ul>
          </div>
        </div>
        <div class="adhd-break-actions">
          <button class="adhd-button adhd-button-primary" onclick="breakSystem.continueStudying(this)">
            <i data-lucide="play" class="w-4 h-4" aria-hidden="true"></i>
            Continue Learning
          </button>
          <button class="adhd-button adhd-button-secondary" onclick="breakSystem.startBreakTimer(this)">
            <i data-lucide="timer" class="w-4 h-4" aria-hidden="true"></i>
            Start ${this.breakDuration}-min Break
          </button>
        </div>
      </div>
    `;

    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }

    return section;
  }

  /**
   * Continue studying after declining break
   */
  continueStudying(button) {
    const breakSection = button.closest('.adhd-break-section');
    if (breakSection) {
      breakSection.remove();
    }
    
    this.isOnBreak = false;
    this.scheduleBreak(); // Schedule next break
  }

  /**
   * Start break timer
   */
  startBreakTimer(button) {
    const actionsDiv = button.closest('.adhd-break-actions');
    
    actionsDiv.innerHTML = `
      <div class="break-timer">
        <i data-lucide="timer" class="w-5 h-5 animate-pulse"></i>
        <span class="break-timer-text">Break time: <span id="break-countdown">${this.breakDuration}:00</span></span>
      </div>
      <button class="adhd-button adhd-button-primary" onclick="breakSystem.endBreak(this)">
        <i data-lucide="play" class="w-4 h-4" aria-hidden="true"></i>
        End Break Early
      </button>
    `;

    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }

    // Start countdown
    this.countdown(this.breakDuration * 60);
  }

  /**
   * Countdown timer for break
   */
  countdown(seconds) {
    const countdownEl = document.getElementById('break-countdown');
    if (!countdownEl) return;

    const interval = setInterval(() => {
      seconds--;
      const mins = Math.floor(seconds / 60);
      const secs = seconds % 60;
      countdownEl.textContent = `${mins}:${secs.toString().padStart(2, '0')}`;

      if (seconds <= 0) {
        clearInterval(interval);
        this.endBreak();
      }
    }, 1000);
  }

  /**
   * End break and resume studying
   */
  endBreak(button = null) {
    const breakSection = button ? button.closest('.adhd-break-section') : document.querySelector('.adhd-break-section');
    
    if (breakSection) {
      // Show completion message
      const message = document.createElement('div');
      message.className = 'adhd-break-complete';
      message.innerHTML = `
        <i data-lucide="check-circle" class="w-5 h-5 text-positive"></i>
        <span>Break complete! Ready to continue?</span>
      `;
      
      breakSection.querySelector('.adhd-break-card').appendChild(message);
      
      // Remove after 2 seconds
      setTimeout(() => {
        breakSection.remove();
      }, 2000);
    }

    this.isOnBreak = false;
    this.studyStartTime = Date.now(); // Reset study timer
    this.scheduleBreak();
  }

  /**
   * Update break interval (user preference)
   */
  setBreakInterval(minutes) {
    this.breakInterval = minutes;
    this.saveSettings();
    
    if (this.studyStartTime && !this.isOnBreak) {
      this.scheduleBreak();
    }
  }
}

// Create global instance
const breakSystem = new BreakSystem();

// Auto-start when page loads
document.addEventListener('DOMContentLoaded', () => {
  // Only start on chapter/content pages
  if (document.querySelector('main[id="main-content"]')) {
    breakSystem.startStudying();
  }
});

// Export for global use
window.breakSystem = breakSystem;

