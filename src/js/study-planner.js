// Simple ADHD-Friendly Study Planner
class StudyPlanner {
    constructor() {
        this.tasks = this.loadTasks();
        this.init();
    }

    init() {
        this.createPlannerWidget();
        this.bindEvents();
        this.updateDashboard();
    }

    createPlannerWidget() {
        const widget = document.createElement('div');
        widget.id = 'study-planner-widget';
        widget.innerHTML = `
            <div class="bg-background-secondary border border-border rounded-xl p-6">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="font-title-small text-text-primary flex items-center">
                        <i data-lucide="brain-circuit" class="w-5 h-5 mr-2 text-brand"></i>
                        ADHD Study Planner
                    </h3>
                    <button id="add-task-btn" class="p-2 bg-brand text-text-inverse-primary rounded-lg hover:bg-brand-hover transition-colors">
                        <i data-lucide="plus" class="w-4 h-4"></i>
                    </button>
                </div>
                
                <!-- Quick Add Task -->
                <div id="quick-add" class="hidden mb-4">
                    <div class="flex gap-2">
                        <input id="task-input" type="text" placeholder="What do you need to study?" 
                               class="flex-1 px-3 py-2 bg-background border border-border rounded-md font-input">
                        <select id="task-subject" class="px-3 py-2 bg-background border border-border rounded-md font-input">
                            <option value="math">MAT 143</option>
                            <option value="english">ENG 111</option>
                        </select>
                        <button id="save-task-btn" class="px-4 py-2 bg-positive text-text-inverse-primary rounded-md font-button">
                            Save
                        </button>
                    </div>
                </div>
                
                <!-- Task List -->
                <div id="task-list" class="space-y-2">
                    <!-- Tasks will be dynamically added here -->
                </div>
                
                <!-- Study Session Timer -->
                <div class="mt-4 p-4 bg-background rounded-lg">
                    <div class="flex items-center justify-between">
                        <span class="font-body-small text-text-secondary">Focus Timer (Pomodoro)</span>
                        <div class="flex items-center gap-2">
                            <button id="timer-btn" class="px-3 py-1 bg-brand text-text-inverse-primary rounded font-caption">
                                25:00
                            </button>
                            <button id="break-btn" class="px-3 py-1 bg-warning text-text-inverse-primary rounded font-caption">
                                5 min break
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        // Insert into dashboard
        const dashboardSection = document.querySelector('#dashboard');
        if (dashboardSection) {
            dashboardSection.appendChild(widget);
        }
        
        // Initialize Lucide icons
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    }

    bindEvents() {
        document.addEventListener('click', (e) => {
            if (e.target.id === 'add-task-btn' || e.target.closest('#add-task-btn')) {
                this.toggleQuickAdd();
            }
            if (e.target.id === 'save-task-btn') {
                this.addTask();
            }
            if (e.target.classList.contains('task-complete-btn')) {
                this.completeTask(e.target.dataset.taskId);
            }
            if (e.target.id === 'timer-btn') {
                this.startPomodoroTimer();
            }
            if (e.target.id === 'break-btn') {
                this.startBreakTimer();
            }
        });

        document.addEventListener('keypress', (e) => {
            if (e.target.id === 'task-input' && e.key === 'Enter') {
                this.addTask();
            }
        });
    }

    toggleQuickAdd() {
        const quickAdd = document.getElementById('quick-add');
        const input = document.getElementById('task-input');
        
        if (quickAdd.classList.contains('hidden')) {
            quickAdd.classList.remove('hidden');
            input.focus();
        } else {
            quickAdd.classList.add('hidden');
            input.value = '';
        }
    }

    addTask() {
        const input = document.getElementById('task-input');
        const subject = document.getElementById('task-subject');
        const taskText = input.value.trim();
        
        if (!taskText) return;

        const task = {
            id: Date.now(),
            text: taskText,
            subject: subject.value,
            completed: false,
            created: new Date().toLocaleDateString()
        };

        this.tasks.push(task);
        this.saveTasks();
        this.renderTasks();
        
        // Clear and hide form
        input.value = '';
        this.toggleQuickAdd();
    }

    completeTask(taskId) {
        const task = this.tasks.find(t => t.id == taskId);
        if (task) {
            task.completed = true;
            this.saveTasks();
            this.renderTasks();
            this.showCompletionFeedback();
        }
    }

    renderTasks() {
        const taskList = document.getElementById('task-list');
        const incompleteTasks = this.tasks.filter(t => !t.completed);
        
        if (incompleteTasks.length === 0) {
            taskList.innerHTML = `
                <div class="text-center py-4">
                    <i data-lucide="check-circle" class="w-8 h-8 text-positive mx-auto mb-2"></i>
                    <p class="font-body-small text-text-secondary">All caught up! Great job! 🎉</p>
                </div>
            `;
        } else {
            taskList.innerHTML = incompleteTasks.map(task => `
                <div class="flex items-center justify-between p-3 bg-background rounded-lg border border-border">
                    <div class="flex items-center space-x-3">
                        <div class="w-6 h-6 rounded-full border-2 border-border bg-background flex items-center justify-center">
                            <div class="w-2 h-2 rounded-full ${task.subject === 'math' ? 'bg-positive' : 'bg-brand'}"></div>
                        </div>
                        <div>
                            <p class="font-body-small text-text-primary">${task.text}</p>
                            <p class="font-caption text-text-secondary">${task.subject === 'math' ? 'MAT 143' : 'ENG 111'} • ${task.created}</p>
                        </div>
                    </div>
                    <button class="task-complete-btn p-2 text-positive hover:bg-positive-tertiary rounded transition-colors" 
                            data-task-id="${task.id}">
                        <i data-lucide="check" class="w-4 h-4"></i>
                    </button>
                </div>
            `).join('');
        }
        
        // Reinitialize icons
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    }

    showCompletionFeedback() {
        // Simple celebration animation
        const feedback = document.createElement('div');
        feedback.className = 'fixed top-4 right-4 bg-positive text-text-inverse-primary px-4 py-2 rounded-lg font-button z-50 animate-bounce';
        feedback.innerHTML = '✅ Task completed! Nice work!';
        document.body.appendChild(feedback);
        
        setTimeout(() => {
            document.body.removeChild(feedback);
        }, 3000);
    }

    startPomodoroTimer() {
        this.startTimer(25, 'Focus time!', '#timer-btn');
    }

    startBreakTimer() {
        this.startTimer(5, 'Break time!', '#break-btn');
    }

    startTimer(minutes, message, buttonSelector) {
        const button = document.querySelector(buttonSelector);
        let timeLeft = minutes * 60;
        
        const timer = setInterval(() => {
            const mins = Math.floor(timeLeft / 60);
            const secs = timeLeft % 60;
            button.textContent = `${mins}:${secs.toString().padStart(2, '0')}`;
            
            if (timeLeft <= 0) {
                clearInterval(timer);
                button.textContent = message;
                this.showTimerComplete(message);
                setTimeout(() => {
                    button.textContent = minutes === 25 ? '25:00' : '5 min break';
                }, 2000);
            }
            timeLeft--;
        }, 1000);
    }

    showTimerComplete(message) {
        const notification = document.createElement('div');
        notification.className = 'fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-brand text-text-inverse-primary px-6 py-4 rounded-xl font-title-small z-50 shadow-lg';
        notification.innerHTML = `🎉 ${message}`;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 3000);
    }

    updateDashboard() {
        this.renderTasks();
    }

    loadTasks() {
        const saved = localStorage.getItem('kristina-study-tasks');
        return saved ? JSON.parse(saved) : [];
    }

    saveTasks() {
        localStorage.setItem('kristina-study-tasks', JSON.stringify(this.tasks));
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('dashboard')) {
        new StudyPlanner();
    }
});

export default StudyPlanner;