/**
 * SESSION CONTINUITY SYSTEM
 * Critical for ADHD: Students forget where they were, what they were doing
 * This creates a "resume where you left off" system
 */

const SESSION_CONFIG = {
    storageKey: 'kristina_study_session',
    idleTimeout: 10 * 60 * 1000, // 10 minutes = considered "left"
    chapters: [1, 4, 5, 6, 7, 10, 11, 13],
    essays: [1, 2, 3, 4]
};

// Track current study session
function updateStudySession(type, id, title, url, progress = 0) {
    const session = {
        type: type, // 'chapter' or 'essay'
        id: id, // chapter number or essay number
        title: title,
        url: url,
        progress: progress, // 0-100
        lastActive: Date.now(),
        startTime: Date.now()
    };

    localStorage.setItem(SESSION_CONFIG.storageKey, JSON.stringify(session));
}

// Get active session (if not too old)
function getActiveSession() {
    const sessionData = localStorage.getItem(SESSION_CONFIG.storageKey);
    if (!sessionData) return null;

    const session = JSON.parse(sessionData);
    const now = Date.now();
    const timeSinceActive = now - session.lastActive;

    // If more than idle timeout, consider it stale
    if (timeSinceActive > SESSION_CONFIG.idleTimeout) {
        return null;
    }

    return session;
}

// Clear session (when student completes the work)
function clearStudySession() {
    localStorage.removeItem(SESSION_CONFIG.storageKey);
    const card = document.getElementById('resume-study-card');
    if (card) {
        card.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => card.remove(), 300);
    }
}

// Calculate time spent (in minutes)
function getTimeSpent(startTime) {
    const now = Date.now();
    const diffMs = now - startTime;
    return Math.floor(diffMs / (1000 * 60));
}

// Format time spent
function formatTimeSpent(minutes) {
    if (minutes < 1) return 'just now';
    if (minutes < 60) return `${minutes} minute${minutes === 1 ? '' : 's'} ago`;
    const hours = Math.floor(minutes / 60);
    return `${hours} hour${hours === 1 ? '' : 's'} ago`;
}

// Create "Resume Study" card on dashboard
function createResumeStudyCard() {
    const session = getActiveSession();
    if (!session) return;

    // Don't show on the page they're already on
    const currentPage = window.location.pathname.split('/').pop();
    if (currentPage === session.url.split('/').pop()) return;

    const timeSince = Date.now() - session.lastActive;
    const minutes = Math.floor(timeSince / (1000 * 60));
    const timeText = formatTimeSpent(minutes);

    const card = document.createElement('div');
    card.id = 'resume-study-card';
    card.className = 'card';
    card.style.cssText = `
        border-left: 4px solid var(--primary-blue);
        background: linear-gradient(135deg, var(--primary-blue-light) 0%, var(--white) 100%);
        margin-bottom: var(--space-8);
        animation: slideIn 0.3s ease;
    `;

    const progressBarWidth = session.progress || 0;
    const icon = session.type === 'chapter' ? 'book-open' : 'pen-tool';
    const typeLabel = session.type === 'chapter' ? 'Chapter' : 'Essay';

    card.innerHTML = `
        <div class="card-body">
            <div style="display: flex; align-items: start; justify-content: space-between; margin-bottom: var(--space-4);">
                <div style="display: flex; align-items: center; gap: var(--space-4);">
                    <div style="width: 48px; height: 48px; background-color: var(--primary-blue); border-radius: var(--radius-lg); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                        <i data-lucide="${icon}" style="width: 24px; height: 24px; color: var(--white);"></i>
                    </div>
                    <div>
                        <div style="display: flex; align-items: center; gap: var(--space-2); margin-bottom: var(--space-1);">
                            <span style="font-size: var(--font-size-xs); font-weight: 600; color: var(--primary-blue); text-transform: uppercase; letter-spacing: 0.5px;">RESUME STUDYING</span>
                            <span style="font-size: var(--font-size-xs); color: var(--neutral-gray-light);">• ${timeText}</span>
                        </div>
                        <h3 style="margin: 0; color: var(--neutral-gray); font-size: var(--font-size-lg);">
                            ${session.title}
                        </h3>
                        ${progressBarWidth > 0 ? `
                            <div style="margin-top: var(--space-2);">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-1);">
                                    <span style="font-size: var(--font-size-xs); color: var(--neutral-gray-light);">Progress</span>
                                    <span style="font-size: var(--font-size-xs); font-weight: 600; color: var(--primary-blue);">${progressBarWidth}%</span>
                                </div>
                                <div class="progress-bar" style="width: 200px;">
                                    <div class="progress-fill" style="width: ${progressBarWidth}%;"></div>
                                </div>
                            </div>
                        ` : ''}
                    </div>
                </div>
                <button onclick="clearResumeCard()" style="background: none; border: none; color: var(--neutral-gray-light); cursor: pointer; font-size: 20px; padding: 0; width: 24px; height: 24px;" aria-label="Dismiss">×</button>
            </div>
            <div style="display: flex; gap: var(--space-3);">
                <a href="${session.url}" class="btn btn-primary" style="flex: 1;">
                    <i data-lucide="play-circle" style="width: 16px; height: 16px;"></i>
                    Continue Studying
                </a>
                <button onclick="clearStudySessionGlobal()" class="btn btn-secondary">
                    Start Fresh
                </button>
            </div>
        </div>
    `;

    // Insert after welcome section on dashboard
    const welcomeSection = document.querySelector('main .mb-8');
    if (welcomeSection && welcomeSection.nextSibling) {
        welcomeSection.parentNode.insertBefore(card, welcomeSection.nextSibling);
    } else if (welcomeSection) {
        welcomeSection.parentNode.appendChild(card);
    } else {
        // Fallback: insert at start of main
        const main = document.querySelector('main');
        if (main && main.firstChild) {
            main.insertBefore(card, main.firstChild);
        }
    }

    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

// Auto-track when student is on a chapter page
function autoTrackChapterPage() {
    const currentPage = window.location.pathname.split('/').pop();

    // Match chapter-X.html pattern
    const chapterMatch = currentPage.match(/chapter-(\d+)\.html/);
    if (chapterMatch) {
        const chapterNum = parseInt(chapterMatch[1]);
        const chapterTitles = {
            1: 'Chapter 1: Thinking Mathematically',
            4: 'Chapter 4: Proportions & Percentages',
            5: 'Chapter 5: Linear & Exponential Functions',
            6: 'Chapter 6: Personal Finance',
            7: 'Chapter 7: Measurement & Conversions',
            10: 'Chapter 10: Probability',
            11: 'Chapter 11: Statistics',
            13: 'Chapter 13: Voting & Apportionment'
        };

        if (chapterTitles[chapterNum]) {
            updateStudySession('chapter', chapterNum, chapterTitles[chapterNum], currentPage, 0);
        }
    }

    // Match essay-X-guide.html pattern
    const essayMatch = currentPage.match(/essay-(\d+)-guide\.html/);
    if (essayMatch) {
        const essayNum = parseInt(essayMatch[1]);
        const essayTitles = {
            1: 'Essay 1: Narrative Essay',
            2: 'Essay 2: Reflection Essay',
            3: 'Essay 3: Analytical Essay',
            4: 'Essay 4: Research Paper'
        };

        if (essayTitles[essayNum]) {
            updateStudySession('essay', essayNum, essayTitles[essayNum], currentPage, 0);
        }
    }
}

// Update session on page activity (scroll, click)
function updateSessionActivity() {
    const session = getActiveSession();
    if (session) {
        session.lastActive = Date.now();
        localStorage.setItem(SESSION_CONFIG.storageKey, JSON.stringify(session));
    }
}

// Global functions for buttons
window.clearStudySessionGlobal = clearStudySession;
window.clearResumeCard = clearStudySession;

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        // Auto-track if on chapter/essay page
        autoTrackChapterPage();

        // Show resume card if on dashboard
        const currentPage = window.location.pathname.split('/').pop();
        if (currentPage === 'index.html' || currentPage === '') {
            createResumeStudyCard();
        }

        // Update activity on interaction
        document.addEventListener('scroll', updateSessionActivity, { passive: true });
        document.addEventListener('click', updateSessionActivity);
    });
} else {
    autoTrackChapterPage();

    const currentPage = window.location.pathname.split('/').pop();
    if (currentPage === 'index.html' || currentPage === '') {
        createResumeStudyCard();
    }

    document.addEventListener('scroll', updateSessionActivity, { passive: true });
    document.addEventListener('click', updateSessionActivity);
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        updateStudySession,
        getActiveSession,
        clearStudySession
    };
}
