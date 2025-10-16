/**
 * Calendar Deadline Urgency System
 * ADHD Accessibility: Visual color coding based on deadline proximity
 * Improves time awareness and reduces deadline anxiety
 */

class CalendarUrgency {
  constructor() {
    this.today = new Date();
    this.init();
  }

  /**
   * Initialize urgency system
   */
  init() {
    document.addEventListener('DOMContentLoaded', () => {
      this.updateAllDeadlines();
    });
  }

  /**
   * Calculate days until a deadline
   * @param {string} dateString - Date in format "YYYY-MM-DD" or "Month Day, Year"
   */
  daysUntil(dateString) {
    const deadline = new Date(dateString);
    const diffTime = deadline - this.today;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays;
  }

  /**
   * Get urgency level based on days until deadline
   * @param {number} days - Days until deadline
   */
  getUrgencyLevel(days) {
    if (days < 0) return 'overdue';
    if (days <= 2) return 'critical';  // < 48 hours
    if (days <= 7) return 'soon';      // 2-7 days
    if (days <= 14) return 'upcoming'; // 1-2 weeks
    return 'future';                   // > 2 weeks
  }

  /**
   * Apply urgency styling to a deadline element
   * @param {HTMLElement} element - Element to style
   * @param {number} days - Days until deadline
   */
  applyUrgencyStyle(element, days) {
    const urgency = this.getUrgencyLevel(days);
    
    // Remove existing urgency classes
    element.classList.remove('deadline-overdue', 'deadline-critical', 'deadline-soon', 'deadline-upcoming', 'deadline-future');
    
    // Add appropriate class
    element.classList.add(`deadline-${urgency}`);
    
    // Update badge if present
    const badge = element.querySelector('.badge');
    if (badge && urgency === 'critical') {
      badge.classList.remove('badge-warning', 'badge-neutral', 'badge-success');
      badge.classList.add('badge-danger');
      badge.textContent = 'Urgent';
    } else if (badge && urgency === 'soon') {
      badge.classList.remove('badge-danger', 'badge-neutral', 'badge-success');
      badge.classList.add('badge-warning');
      badge.textContent = 'Upcoming';
    }
    
    // Add countdown if critical
    if (urgency === 'critical' || urgency === 'soon') {
      this.addCountdown(element, days);
    }
  }

  /**
   * Add countdown indicator to urgent deadlines
   */
  addCountdown(element, days) {
    const existing = element.querySelector('.deadline-countdown');
    if (existing) return; // Already has countdown
    
    const countdown = document.createElement('div');
    countdown.className = 'deadline-countdown';
    countdown.setAttribute('aria-label', `${days} days remaining`);
    
    let countdownText = '';
    let countdownClass = '';
    
    if (days === 0) {
      countdownText = 'Due Today!';
      countdownClass = 'pulse-urgent';
    } else if (days === 1) {
      countdownText = 'Due Tomorrow';
      countdownClass = 'pulse-urgent';
    } else {
      countdownText = `${days} days left`;
      countdownClass = days <= 2 ? 'pulse-urgent' : '';
    }
    
    countdown.innerHTML = `
      <i data-lucide="clock" class="w-4 h-4 ${countdownClass}" aria-hidden="true"></i>
      <span class="font-semibold">${countdownText}</span>
    `;
    
    // Find appropriate place to insert
    const header = element.querySelector('.flex.items-start.justify-between');
    if (header) {
      const wrapper = document.createElement('div');
      wrapper.className = 'mt-2';
      wrapper.appendChild(countdown);
      header.insertAdjacentElement('afterend', wrapper);
    }
    
    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }
  }

  /**
   * Update all deadline cards on the calendar page
   */
  updateAllDeadlines() {
    // This would need actual deadline dates from the calendar
    // For now, we'll set up the structure
    
    const deadlineCards = document.querySelectorAll('[data-deadline]');
    deadlineCards.forEach(card => {
      const deadlineDate = card.getAttribute('data-deadline');
      if (deadlineDate) {
        const days = this.daysUntil(deadlineDate);
        this.applyUrgencyStyle(card, days);
      }
    });

    // Auto-update every hour
    setInterval(() => {
      this.today = new Date();
      this.updateAllDeadlines();
    }, 3600000); // 1 hour
  }

  /**
   * Get urgency color for a deadline
   * @param {number} days - Days until deadline
   */
  getUrgencyColor(days) {
    const urgency = this.getUrgencyLevel(days);
    const colors = {
      'overdue': 'var(--color-ruby-500)',
      'critical': 'var(--color-ruby-500)',
      'soon': 'var(--color-carnelian-500)',
      'upcoming': 'var(--color-emerald-500)',
      'future': 'var(--color-neutral-tertiary)'
    };
    return colors[urgency];
  }
}

// Create global instance
const calendarUrgency = new CalendarUrgency();

// Export for global use
window.calendarUrgency = calendarUrgency;

