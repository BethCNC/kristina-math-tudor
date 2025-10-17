/**
 * Deadline Urgency System
 * Dynamically calculates and applies semantic color classes based on days until deadline
 * 
 * Urgency Levels:
 * - URGENT (0-3 days): Red - immediate action required
 * - WARNING (4-7 days): Orange - this week
 * - UPCOMING (8-14 days): Blue - next 2 weeks
 * - FUTURE (14+ days): Gray - plan ahead
 * - COMPLETED (past): Green - done!
 */

function getDeadlineUrgency(deadlineDate) {
  const now = new Date();
  now.setHours(0, 0, 0, 0); // Reset to start of day for accurate comparison
  
  const deadline = new Date(deadlineDate);
  deadline.setHours(0, 0, 0, 0);
  
  const daysUntil = Math.ceil((deadline - now) / (1000 * 60 * 60 * 24));
  
  if (daysUntil < 0) return 'completed'; // Past due
  if (daysUntil <= 3) return 'urgent';    // 0-3 days
  if (daysUntil <= 7) return 'warning';   // 4-7 days
  if (daysUntil <= 14) return 'upcoming'; // 8-14 days
  return 'future';                        // 14+ days
}

function getBadgeClass(urgency) {
  return `badge-${urgency}`;
}

function getCardClass(urgency) {
  return `deadline-${urgency}`;
}

function updateDeadlineColors() {
  // Update all elements with data-deadline attribute
  document.querySelectorAll('[data-deadline]').forEach(element => {
    const deadlineDate = element.getAttribute('data-deadline');
    const urgency = getDeadlineUrgency(deadlineDate);
    
    // Update card classes
    if (element.classList.contains('card') || element.classList.contains('deadline-card')) {
      // Remove all urgency classes
      element.classList.remove('deadline-urgent', 'deadline-warning', 'deadline-upcoming', 'deadline-future', 'deadline-completed');
      // Add appropriate class
      element.classList.add(`deadline-${urgency}`);
    }
    
    // Update badge classes inside this element
    const badge = element.querySelector('.badge');
    if (badge) {
      badge.classList.remove('badge-urgent', 'badge-warning', 'badge-upcoming', 'badge-future', 'badge-completed');
      badge.classList.add(`badge-${urgency}`);
    }
    
    // Update any urgency text
    const urgencyText = element.querySelector('[data-urgency-text]');
    if (urgencyText) {
      const labels = {
        urgent: '🚨 URGENT',
        warning: '⚠️ THIS WEEK',
        upcoming: '📅 UPCOMING',
        future: '📌 FUTURE',
        completed: '✅ COMPLETED'
      };
      urgencyText.textContent = labels[urgency];
    }
  });
}

function getDaysUntilText(deadlineDate) {
  const now = new Date();
  now.setHours(0, 0, 0, 0);
  
  const deadline = new Date(deadlineDate);
  deadline.setHours(0, 0, 0, 0);
  
  const daysUntil = Math.ceil((deadline - now) / (1000 * 60 * 60 * 24));
  
  if (daysUntil < 0) return 'Past due';
  if (daysUntil === 0) return 'Today!';
  if (daysUntil === 1) return 'Tomorrow';
  if (daysUntil <= 7) return `${daysUntil} days`;
  if (daysUntil <= 14) return `${daysUntil} days`;
  
  const weeks = Math.ceil(daysUntil / 7);
  return `${weeks} week${weeks > 1 ? 's' : ''}`;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', updateDeadlineColors);

// Update every hour in case user keeps page open overnight
setInterval(updateDeadlineColors, 3600000); // 1 hour

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    getDeadlineUrgency,
    getBadgeClass,
    getCardClass,
    getDaysUntilText,
    updateDeadlineColors
  };
}

