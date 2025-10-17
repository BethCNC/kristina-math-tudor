/**
 * TIME AWARENESS SYSTEM
 * Critical for ADHD/Time Blindness: Students don't perceive time passing
 * This provides gentle, non-intrusive time reminders
 */

const TIME_CONFIG = {
    breakInterval: 25 * 60 * 1000, // 25 minutes (Pomodoro technique)
    reminderInterval: 15 * 60 * 1000, // 15 minutes
    sessionTracking: 'kristina_time_tracking',
    showTimer: false, // Set to true to show persistent timer
    enableBreakReminders: true
};

let sessionStartTime = null;
let studyTimer = null;
let reminderTimer = null;
let timerDisplay = null;

// Start tracking time
function startTimeTracking() {
    if (sessionStartTime) return; // Already tracking

    sessionStartTime = Date.now();

    // Save to localStorage in case of page refresh
    localStorage.setItem(TIME_CONFIG.sessionTracking, sessionStartTime.toString());

    // Create timer display if enabled
    if (TIME_CONFIG.showTimer) {
        createTimerDisplay();
    }

    // Set break reminder
    if (TIME_CONFIG.enableBreakReminders) {
        reminderTimer = setTimeout(showBreakReminder, TIME_CONFIG.breakInterval);
    }

    // Update timer every minute
    studyTimer = setInterval(updateTimerDisplay, 60 * 1000);
}

// Get current session time in minutes
function getSessionMinutes() {
    if (!sessionStartTime) return 0;

    const now = Date.now();
    const diff = now - sessionStartTime;
    return Math.floor(diff / (1000 * 60));
}

// Format time for display
function formatStudyTime(minutes) {
    if (minutes < 60) {
        return `${minutes}min`;
    }
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return `${hours}h ${mins}min`;
}

// Create floating timer display
function createTimerDisplay() {
    if (timerDisplay) return;

    timerDisplay = document.createElement('div');
    timerDisplay.id = 'study-timer-display';
    timerDisplay.style.cssText = `
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        background: white;
        border: 2px solid var(--primary-blue);
        border-radius: 20px;
        padding: 8px 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        z-index: 45;
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 14px;
        font-weight: 600;
        color: var(--primary-blue);
    `;

    timerDisplay.innerHTML = `
        <i data-lucide="clock" style="width: 16px; height: 16px;"></i>
        <span id="timer-text">0min</span>
    `;

    document.body.appendChild(timerDisplay);

    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    updateTimerDisplay();
}

// Update timer display
function updateTimerDisplay() {
    const timerText = document.getElementById('timer-text');
    if (timerText) {
        const minutes = getSessionMinutes();
        timerText.textContent = formatStudyTime(minutes);
    }
}

// Show break reminder
function showBreakReminder() {
    const minutes = getSessionMinutes();

    const reminder = document.createElement('div');
    reminder.id = 'break-reminder-toast';
    reminder.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, var(--success-green) 0%, #059669 100%);
        color: white;
        padding: 32px;
        border-radius: 16px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        z-index: 9999;
        max-width: 400px;
        text-align: center;
        animation: bounceIn 0.5s ease;
    `;

    reminder.innerHTML = `
        <div style="width: 64px; height: 64px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px auto;">
            <i data-lucide="coffee" style="width: 32px; height: 32px; color: var(--success-green);"></i>
        </div>
        <h2 style="margin: 0 0 12px 0; font-size: 24px; font-weight: 700;">
            Great Work! Time for a Break 🎉
        </h2>
        <p style="margin: 0 0 20px 0; font-size: 16px; opacity: 0.95;">
            You've been studying for ${formatStudyTime(minutes)}. Your brain needs a rest!
        </p>
        <div style="background: rgba(255,255,255,0.2); padding: 12px; border-radius: 8px; margin-bottom: 20px; font-size: 14px;">
            <strong>Break tips:</strong> Stand up, stretch, get water, look at something far away (20-20-20 rule)
        </div>
        <div style="display: flex; gap: 12px;">
            <button onclick="dismissBreakReminder()" class="btn" style="flex: 1; background: white; color: var(--success-green); border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: 700; font-size: 16px;">
                5 Min Break
            </button>
            <button onclick="continueStudying()" class="btn" style="flex: 1; background: rgba(255,255,255,0.2); color: white; border: 2px solid white; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: 700; font-size: 16px;">
                Keep Going
            </button>
        </div>
        <button onclick="dismissBreakReminder()" style="position: absolute; top: 12px; right: 12px; background: rgba(255,255,255,0.2); border: none; color: white; cursor: pointer; font-size: 24px; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">×</button>
    `;

    // Add backdrop
    const backdrop = document.createElement('div');
    backdrop.id = 'break-reminder-backdrop';
    backdrop.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.5);
        z-index: 9998;
        animation: fadeIn 0.3s ease;
    `;

    // Add animations
    if (!document.querySelector('#break-animations')) {
        const style = document.createElement('style');
        style.id = 'break-animations';
        style.textContent = `
            @keyframes bounceIn {
                from {
                    transform: translate(-50%, -50%) scale(0.5);
                    opacity: 0;
                }
                60% {
                    transform: translate(-50%, -50%) scale(1.1);
                }
                to {
                    transform: translate(-50%, -50%) scale(1);
                    opacity: 1;
                }
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes fadeOut {
                from { opacity: 1; }
                to { opacity: 0; }
            }
        `;
        document.head.appendChild(style);
    }

    document.body.appendChild(backdrop);
    document.body.appendChild(reminder);

    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

// Dismiss break reminder and take 5 min break
function dismissBreakReminder() {
    const reminder = document.getElementById('break-reminder-toast');
    const backdrop = document.getElementById('break-reminder-backdrop');

    if (reminder) {
        reminder.style.animation = 'fadeOut 0.3s ease';
        setTimeout(() => reminder.remove(), 300);
    }

    if (backdrop) {
        backdrop.style.animation = 'fadeOut 0.3s ease';
        setTimeout(() => backdrop.remove(), 300);
    }

    // Show break timer
    startBreakTimer(5);

    // Schedule next break reminder for 25 minutes from now
    reminderTimer = setTimeout(showBreakReminder, TIME_CONFIG.breakInterval);
}

// Continue studying without break
function continueStudying() {
    const reminder = document.getElementById('break-reminder-toast');
    const backdrop = document.getElementById('break-reminder-backdrop');

    if (reminder) {
        reminder.style.animation = 'fadeOut 0.3s ease';
        setTimeout(() => reminder.remove(), 300);
    }

    if (backdrop) {
        backdrop.style.animation = 'fadeOut 0.3s ease';
        setTimeout(() => backdrop.remove(), 300);
    }

    // Schedule next reminder for 15 minutes (shorter since they skipped)
    reminderTimer = setTimeout(showBreakReminder, TIME_CONFIG.reminderInterval);

    // Show encouragement
    showQuickToast('💪 Keep it up! Remember to stay hydrated!', 3000);
}

// Start break countdown timer
function startBreakTimer(minutes) {
    let secondsRemaining = minutes * 60;

    const breakTimer = document.createElement('div');
    breakTimer.id = 'break-countdown-timer';
    breakTimer.style.cssText = `
        position: fixed;
        top: 80px;
        right: 20px;
        background: linear-gradient(135deg, var(--success-green) 0%, #059669 100%);
        color: white;
        padding: 16px 20px;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        z-index: 50;
        display: flex;
        align-items: center;
        gap: 12px;
        font-weight: 600;
        animation: slideIn 0.3s ease;
    `;

    breakTimer.innerHTML = `
        <i data-lucide="coffee" style="width: 20px; height: 20px;"></i>
        <div>
            <div style="font-size: 12px; opacity: 0.9;">Break Time</div>
            <div id="break-countdown" style="font-size: 20px;">${minutes}:00</div>
        </div>
        <button onclick="endBreakEarly()" style="background: rgba(255,255,255,0.2); border: none; color: white; cursor: pointer; padding: 4px 8px; border-radius: 4px; font-size: 12px;">End Break</button>
    `;

    document.body.appendChild(breakTimer);

    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // Countdown
    const interval = setInterval(() => {
        secondsRemaining--;

        const mins = Math.floor(secondsRemaining / 60);
        const secs = secondsRemaining % 60;
        const display = `${mins}:${secs.toString().padStart(2, '0')}`;

        const countdown = document.getElementById('break-countdown');
        if (countdown) {
            countdown.textContent = display;
        }

        if (secondsRemaining <= 0) {
            clearInterval(interval);
            endBreak();
        }
    }, 1000);

    // Store interval ID for early end
    window.currentBreakInterval = interval;
}

// End break early
function endBreakEarly() {
    if (window.currentBreakInterval) {
        clearInterval(window.currentBreakInterval);
    }
    endBreak();
}

// End break
function endBreak() {
    const timer = document.getElementById('break-countdown-timer');
    if (timer) {
        timer.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => timer.remove(), 300);
    }

    showQuickToast('✨ Break complete! Let\'s get back to it!', 3000);
}

// Show quick toast notification
function showQuickToast(message, duration = 3000) {
    const toast = document.createElement('div');
    toast.style.cssText = `
        position: fixed;
        bottom: 80px;
        left: 50%;
        transform: translateX(-50%);
        background: var(--neutral-gray);
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 9999;
        font-size: 14px;
        font-weight: 500;
        animation: slideUp 0.3s ease;
    `;

    toast.textContent = message;

    // Add slide up animation
    if (!document.querySelector('#toast-animations')) {
        const style = document.createElement('style');
        style.id = 'toast-animations';
        style.textContent = `
            @keyframes slideUp {
                from {
                    transform: translateX(-50%) translateY(20px);
                    opacity: 0;
                }
                to {
                    transform: translateX(-50%) translateY(0);
                    opacity: 1;
                }
            }
        `;
        document.head.appendChild(style);
    }

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, duration);
}

// Stop tracking time
function stopTimeTracking() {
    if (sessionStartTime) {
        const minutes = getSessionMinutes();

        // Save to study history
        saveStudySession(minutes);

        sessionStartTime = null;
        localStorage.removeItem(TIME_CONFIG.sessionTracking);

        if (studyTimer) {
            clearInterval(studyTimer);
            studyTimer = null;
        }

        if (reminderTimer) {
            clearTimeout(reminderTimer);
            reminderTimer = null;
        }

        if (timerDisplay) {
            timerDisplay.remove();
            timerDisplay = null;
        }
    }
}

// Save study session to history
function saveStudySession(minutes) {
    const history = JSON.parse(localStorage.getItem('kristina_study_history') || '[]');

    history.push({
        date: new Date().toISOString(),
        minutes: minutes,
        page: window.location.pathname.split('/').pop()
    });

    // Keep last 30 sessions
    if (history.length > 30) {
        history.shift();
    }

    localStorage.setItem('kristina_study_history', JSON.stringify(history));
}

// Check if returning from previous session
function checkPreviousSession() {
    const savedStart = localStorage.getItem(TIME_CONFIG.sessionTracking);
    if (savedStart) {
        const savedTime = parseInt(savedStart);
        const now = Date.now();
        const diff = now - savedTime;

        // If less than 2 hours, resume session
        if (diff < 2 * 60 * 60 * 1000) {
            sessionStartTime = savedTime;
            if (TIME_CONFIG.showTimer) {
                createTimerDisplay();
            }
            if (TIME_CONFIG.enableBreakReminders) {
                reminderTimer = setTimeout(showBreakReminder, TIME_CONFIG.breakInterval);
            }
            studyTimer = setInterval(updateTimerDisplay, 60 * 1000);
        } else {
            // Session too old, clear it
            localStorage.removeItem(TIME_CONFIG.sessionTracking);
        }
    }
}

// Global functions
window.dismissBreakReminder = dismissBreakReminder;
window.continueStudying = continueStudying;
window.endBreakEarly = endBreakEarly;

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        // Check for previous session
        checkPreviousSession();

        // Start tracking if on chapter/essay page
        const currentPage = window.location.pathname.split('/').pop();
        if (currentPage.match(/chapter-\d+\.html/) || currentPage.match(/essay-\d+-guide\.html/)) {
            if (!sessionStartTime) {
                startTimeTracking();
            }
        }

        // Stop tracking when leaving page
        window.addEventListener('beforeunload', () => {
            if (sessionStartTime) {
                const minutes = getSessionMinutes();
                saveStudySession(minutes);
            }
        });
    });
} else {
    checkPreviousSession();

    const currentPage = window.location.pathname.split('/').pop();
    if (currentPage.match(/chapter-\d+\.html/) || currentPage.match(/essay-\d+-guide\.html/)) {
        if (!sessionStartTime) {
            startTimeTracking();
        }
    }

    window.addEventListener('beforeunload', () => {
        if (sessionStartTime) {
            const minutes = getSessionMinutes();
            saveStudySession(minutes);
        }
    });
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        startTimeTracking,
        stopTimeTracking,
        getSessionMinutes
    };
}
