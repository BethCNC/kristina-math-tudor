/**
 * HAWKES LEARNING REMINDER SYSTEM
 * Critical: Hawkes is 20% of grade - students with ADHD ALWAYS forget it
 * This creates persistent, impossible-to-miss reminders
 */

const HAWKES_CONFIG = {
    dueDate: new Date('2025-11-03T23:59:59'),
    percentOfGrade: 20,
    chapters: [6, 7],
    testDate: new Date('2025-11-03'), // Same day Test 3 starts!
    url: 'https://learn.hawkeslearning.com'
};

// Check if Hawkes has been completed (stored in localStorage)
function isHawkesComplete() {
    const completion = localStorage.getItem('hawkes_ch6_complete') === 'true' &&
                      localStorage.getItem('hawkes_ch7_complete') === 'true';
    return completion;
}

// Mark chapter as complete
function markHawkesComplete(chapter) {
    localStorage.setItem(`hawkes_ch${chapter}_complete`, 'true');
    showHawkesCompleteToast(chapter);
    updateHawkesReminders();
}

// Calculate days until due
function getDaysUntilHawkes() {
    const now = new Date();
    const diff = HAWKES_CONFIG.dueDate - now;
    return Math.ceil(diff / (1000 * 60 * 60 * 24));
}

// Show completion celebration
function showHawkesCompleteToast(chapter) {
    const toast = document.createElement('div');
    toast.id = 'hawkes-complete-toast';
    toast.style.cssText = `
        position: fixed;
        top: 80px;
        right: 20px;
        background: linear-gradient(135deg, var(--success-green) 0%, #059669 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        z-index: 9999;
        max-width: 350px;
        animation: slideIn 0.3s ease;
    `;

    toast.innerHTML = `
        <div style="display: flex; align-items: start; gap: 12px;">
            <div style="flex-shrink: 0; width: 40px; height: 40px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                <i data-lucide="check-circle" style="width: 24px; height: 24px; color: var(--success-green);"></i>
            </div>
            <div>
                <h3 style="margin: 0 0 8px 0; font-size: 18px; font-weight: 700;">
                    🎉 Hawkes Chapter ${chapter} Complete!
                </h3>
                <p style="margin: 0; font-size: 14px; opacity: 0.95;">
                    ${chapter === 6 && !isHawkesComplete() ?
                        'Awesome! Now complete Chapter 7 to secure your 20%!' :
                        'You did it! That\'s 20% of your grade locked in! 💪'}
                </p>
            </div>
            <button onclick="this.parentElement.parentElement.remove()" style="background: none; border: none; color: white; cursor: pointer; font-size: 20px; padding: 0; width: 24px; height: 24px;">×</button>
        </div>
    `;

    document.body.appendChild(toast);

    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        toast.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 5000);
}

// Create persistent floating reminder (smaller, less obtrusive than Next Due widget)
function createHawkesFloatingReminder() {
    // Don't show if already complete
    if (isHawkesComplete()) {
        return;
    }

    const days = getDaysUntilHawkes();

    // Don't show if more than 14 days away
    if (days > 14) {
        return;
    }

    // Determine urgency
    let urgencyColor, urgencyBg, urgencyText;
    if (days <= 0) {
        urgencyColor = '#b91c1c'; // Dark red
        urgencyBg = '#fef2f2';
        urgencyText = 'OVERDUE!';
    } else if (days <= 3) {
        urgencyColor = '#dc2626'; // Red
        urgencyBg = '#fef2f2';
        urgencyText = days === 1 ? 'DUE TOMORROW!' : `${days} DAYS LEFT!`;
    } else if (days <= 7) {
        urgencyColor = '#d97706'; // Orange
        urgencyBg = '#fef3c7';
        urgencyText = `${days} days left`;
    } else {
        urgencyColor = '#2563eb'; // Blue
        urgencyBg = '#dbeafe';
        urgencyText = `${days} days left`;
    }

    const reminder = document.createElement('div');
    reminder.id = 'hawkes-floating-reminder';
    reminder.style.cssText = `
        position: fixed;
        bottom: 20px;
        left: 20px;
        background: ${urgencyBg};
        border-left: 4px solid ${urgencyColor};
        padding: 16px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 50;
        max-width: 300px;
        animation: pulse 2s infinite;
    `;

    reminder.innerHTML = `
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <i data-lucide="alert-circle" style="width: 20px; height: 20px; color: ${urgencyColor};"></i>
                    <span style="font-weight: 700; color: ${urgencyColor}; font-size: 14px;">HAWKES DUE ${urgencyText}</span>
                </div>
                <button onclick="dismissHawkesReminder()" style="background: none; border: none; color: ${urgencyColor}; cursor: pointer; font-size: 18px; padding: 0; width: 20px; height: 20px;">×</button>
            </div>
            <p style="margin: 0; font-size: 13px; color: #374151;">
                20% of your grade! Complete Ch 6 & 7 before Nov 3
            </p>
            <div style="display: flex; gap: 8px; margin-top: 4px;">
                <button onclick="window.open('${HAWKES_CONFIG.url}', '_blank')" class="btn btn-sm" style="flex: 1; background: ${urgencyColor}; color: white; padding: 8px 12px; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 12px;">
                    Go to Hawkes
                </button>
                <button onclick="markHawkesChapterComplete(6)" class="btn btn-sm" style="background: white; border: 1px solid ${urgencyColor}; color: ${urgencyColor}; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 12px;">
                    Ch 6 ✓
                </button>
                <button onclick="markHawkesChapterComplete(7)" class="btn btn-sm" style="background: white; border: 1px solid ${urgencyColor}; color: ${urgencyColor}; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 12px;">
                    Ch 7 ✓
                </button>
            </div>
        </div>
    `;

    // Add CSS animation for pulse
    if (!document.querySelector('#hawkes-pulse-animation')) {
        const style = document.createElement('style');
        style.id = 'hawkes-pulse-animation';
        style.textContent = `
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.02); }
            }
            @keyframes slideIn {
                from { transform: translateX(400px); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            @keyframes slideOut {
                from { transform: translateX(0); opacity: 1; }
                to { transform: translateX(400px); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
    }

    document.body.appendChild(reminder);

    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

// Dismiss reminder temporarily (1 hour)
function dismissHawkesReminder() {
    const reminder = document.getElementById('hawkes-floating-reminder');
    if (reminder) {
        reminder.remove();
    }

    // Set dismissal timestamp
    localStorage.setItem('hawkes_reminder_dismissed', Date.now());
}

// Check if reminder was recently dismissed
function wasRecentlyDismissed() {
    const dismissed = localStorage.getItem('hawkes_reminder_dismissed');
    if (!dismissed) return false;

    const dismissedTime = parseInt(dismissed);
    const now = Date.now();
    const oneHour = 60 * 60 * 1000;

    return (now - dismissedTime) < oneHour;
}

// Update all Hawkes reminders on page
function updateHawkesReminders() {
    const reminder = document.getElementById('hawkes-floating-reminder');
    if (reminder) {
        reminder.remove();
    }

    if (!wasRecentlyDismissed()) {
        createHawkesFloatingReminder();
    }
}

// Mark chapter complete (called from button)
function markHawkesChapterComplete(chapter) {
    markHawkesComplete(chapter);
}

// Global function for dismiss button
window.dismissHawkesReminder = dismissHawkesReminder;
window.markHawkesChapterComplete = markHawkesChapterComplete;

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        if (!wasRecentlyDismissed()) {
            createHawkesFloatingReminder();
        }
    });
} else {
    if (!wasRecentlyDismissed()) {
        createHawkesFloatingReminder();
    }
}

// Update reminder every 5 minutes (in case day count changes)
setInterval(updateHawkesReminders, 5 * 60 * 1000);
