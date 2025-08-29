
// Progress Tracking System for Academic Success
class ProgressTracker {
    constructor() {
        this.storageKey = 'academic_progress';
        this.loadProgress();
    }
    
    loadProgress() {
        const saved = localStorage.getItem(this.storageKey);
        this.progress = saved ? JSON.parse(saved) : {
            math_chapters: {},
            english_essays: {},
            study_sessions: [],
            achievements: []
        };
    }
    
    saveProgress() {
        localStorage.setItem(this.storageKey, JSON.stringify(this.progress));
    }
    
    markChapterComplete(chapter, section) {
        if (!this.progress.math_chapters[chapter]) {
            this.progress.math_chapters[chapter] = {};
        }
        this.progress.math_chapters[chapter][section] = {
            completed: true,
            date: new Date().toISOString()
        };
        this.saveProgress();
        this.updateDisplay();
        this.checkAchievements();
    }
    
    markEssayComplete(essayType, draft) {
        if (!this.progress.english_essays[essayType]) {
            this.progress.english_essays[essayType] = {};
        }
        this.progress.english_essays[essayType][draft] = {
            completed: true,
            date: new Date().toISOString()
        };
        this.saveProgress();
        this.updateDisplay();
    }
    
    logStudySession(subject, duration, topics) {
        this.progress.study_sessions.push({
            subject,
            duration,
            topics,
            date: new Date().toISOString()
        });
        this.saveProgress();
    }
    
    checkAchievements() {
        const achievements = [];
        
        // Check math achievements
        const completedChapters = Object.keys(this.progress.math_chapters).length;
        if (completedChapters >= 3 && !this.hasAchievement('math_momentum')) {
            achievements.push({
                id: 'math_momentum',
                title: 'Math Momentum!',
                description: 'Completed 3 math chapters',
                icon: '🚀'
            });
        }
        
        // Check consistency achievements
        const recentSessions = this.progress.study_sessions.filter(session => {
            const sessionDate = new Date(session.date);
            const weekAgo = new Date();
            weekAgo.setDate(weekAgo.getDate() - 7);
            return sessionDate > weekAgo;
        });
        
        if (recentSessions.length >= 5 && !this.hasAchievement('consistent_learner')) {
            achievements.push({
                id: 'consistent_learner', 
                title: 'Consistent Learner',
                description: '5 study sessions this week',
                icon: '⭐'
            });
        }
        
        // Show new achievements
        achievements.forEach(achievement => {
            this.progress.achievements.push(achievement);
            this.showAchievementPopup(achievement);
        });
        
        if (achievements.length > 0) {
            this.saveProgress();
        }
    }
    
    hasAchievement(achievementId) {
        return this.progress.achievements.some(a => a.id === achievementId);
    }
    
    showAchievementPopup(achievement) {
        // Create achievement notification
        const popup = document.createElement('div');
        popup.className = 'fixed top-4 right-4 bg-green-500 text-white p-4 rounded-lg shadow-lg z-50 transform translate-x-full transition-transform duration-300';
        popup.innerHTML = `
            <div class="flex items-center gap-3">
                <span class="text-2xl">${achievement.icon}</span>
                <div>
                    <h4 class="font-bold">${achievement.title}</h4>
                    <p class="text-sm">${achievement.description}</p>
                </div>
            </div>
        `;
        
        document.body.appendChild(popup);
        
        // Animate in
        setTimeout(() => {
            popup.style.transform = 'translateX(0)';
        }, 100);
        
        // Auto remove
        setTimeout(() => {
            popup.style.transform = 'translateX(100%)';
            setTimeout(() => popup.remove(), 300);
        }, 4000);
    }
    
    updateDisplay() {
        // Update progress bars and completion indicators
        this.updateMathProgress();
        this.updateEnglishProgress();
        this.updateOverallProgress();
    }
    
    updateMathProgress() {
        const totalChapters = 8;
        const completedChapters = Object.keys(this.progress.math_chapters).length;
        const percentage = Math.round((completedChapters / totalChapters) * 100);
        
        const progressBar = document.getElementById('math-progress-bar');
        const progressText = document.getElementById('math-progress-text');
        
        if (progressBar && progressText) {
            progressBar.style.width = percentage + '%';
            progressText.textContent = `${completedChapters}/${totalChapters} chapters (${percentage}%)`;
        }
    }
    
    updateEnglishProgress() {
        const essayTypes = ['critical-reading', 'compare-contrast', 'cause-effect', 'argument'];
        let completedEssays = 0;
        
        essayTypes.forEach(type => {
            if (this.progress.english_essays[type] && this.progress.english_essays[type]['final']) {
                completedEssays++;
            }
        });
        
        const percentage = Math.round((completedEssays / essayTypes.length) * 100);
        
        const progressBar = document.getElementById('english-progress-bar');
        const progressText = document.getElementById('english-progress-text');
        
        if (progressBar && progressText) {
            progressBar.style.width = percentage + '%';
            progressText.textContent = `${completedEssays}/${essayTypes.length} essays (${percentage}%)`;
        }
    }
    
    updateOverallProgress() {
        const mathComplete = Object.keys(this.progress.math_chapters).length / 8;
        const englishComplete = Object.keys(this.progress.english_essays).length / 4;
        const overall = Math.round(((mathComplete + englishComplete) / 2) * 100);
        
        const overallBar = document.getElementById('overall-progress-bar');
        const overallText = document.getElementById('overall-progress-text');
        
        if (overallBar && overallText) {
            overallBar.style.width = overall + '%';
            overallText.textContent = `${overall}% Complete`;
        }
    }
    
    getWeeklyGoals() {
        // Suggest weekly goals based on progress and deadlines
        const now = new Date();
        const goals = [];
        
        // Math goals
        const mathChapters = Object.keys(this.progress.math_chapters).length;
        if (mathChapters < 4) {
            goals.push('Complete 1 math chapter this week');
        }
        
        // English goals  
        const essayCount = Object.keys(this.progress.english_essays).length;
        if (essayCount < 2) {
            goals.push('Start your next essay draft');
        }
        
        // Study consistency
        const thisWeekSessions = this.progress.study_sessions.filter(session => {
            const sessionDate = new Date(session.date);
            const weekStart = new Date(now);
            weekStart.setDate(now.getDate() - now.getDay());
            return sessionDate >= weekStart;
        });
        
        if (thisWeekSessions.length < 3) {
            goals.push('Study at least 3 times this week');
        }
        
        return goals;
    }
}

// Initialize progress tracker
const progressTracker = new ProgressTracker();

// Helper functions for chapters
function markSectionComplete(chapter, section) {
    progressTracker.markChapterComplete(chapter, section);
}

function startStudySession(subject) {
    const startTime = new Date();
    // You can extend this to track time spent
    console.log(`Started ${subject} study session at ${startTime}`);
}
