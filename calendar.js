// Calendar and Pacing Guide System
class AcademicCalendar {
    constructor() {
        this.courses = {
            mat143: {
                name: 'MAT 143 - Quantitative Literacy',
                startDate: new Date('2025-08-18'),
                endDate: new Date('2025-12-12'),
                color: '#68d391', // mathGreen
                assignments: [
                    { name: 'EVA Due', date: new Date('2025-08-29'), type: 'urgent', priority: 'high' },
                    { name: 'Test 1: Ch. 1 & 13', date: new Date('2025-09-08'), endDate: new Date('2025-09-12'), type: 'test', priority: 'high' },
                    { name: 'Test 2: Ch. 4 & 5', date: new Date('2025-09-29'), endDate: new Date('2025-10-03'), type: 'test', priority: 'high' },
                    { name: 'Test 3: Ch. 6 & 7', date: new Date('2025-11-03'), endDate: new Date('2025-11-07'), type: 'test', priority: 'high' },
                    { name: 'Test 4: Ch. 10 & 11', date: new Date('2025-12-08'), endDate: new Date('2025-12-12'), type: 'test', priority: 'high' },
                    { name: 'Last Day to Withdraw', date: new Date('2025-09-26'), type: 'deadline', priority: 'medium' },
                    { name: 'Weekly Attendance', date: new Date('2025-08-25'), type: 'recurring', priority: 'medium', recurring: 'weekly' }
                ]
            },
            eng111: {
                name: 'ENG 111 - Writing & Inquiry',
                startDate: new Date('2025-08-18'),
                endDate: new Date('2025-10-10'),
                color: '#63b3ed', // englishBlue
                assignments: [
                    { name: 'EVA Syllabus Quiz', date: new Date('2025-08-25'), type: 'assignment', priority: 'high' },
                    { name: 'Critical Reading Discussion', date: new Date('2025-08-29'), type: 'discussion', priority: 'medium' },
                    { name: 'Compare/Contrast Rough Draft', date: new Date('2025-09-08'), type: 'assignment', priority: 'high' },
                    { name: 'Compare/Contrast Final Draft', date: new Date('2025-09-15'), type: 'assignment', priority: 'high' },
                    { name: 'Cause/Effect Rough Draft', date: new Date('2025-09-22'), type: 'assignment', priority: 'high' },
                    { name: 'Cause/Effect Final Draft', date: new Date('2025-09-29'), type: 'assignment', priority: 'high' },
                    { name: 'Argument Essay Rough Draft', date: new Date('2025-10-06'), type: 'assignment', priority: 'high' },
                    { name: 'Argument Essay Final Draft', date: new Date('2025-10-10'), type: 'assignment', priority: 'high' },
                    { name: 'Last Day to Withdraw', date: new Date('2025-09-08'), type: 'deadline', priority: 'medium' }
                ]
            }
        };
        
        this.currentDate = new Date();
        this.currentView = 'month';
        this.selectedFilters = ['mat143', 'eng111'];
        this.init();
    }
    
    init() {
        this.renderCalendar();
        this.setupEventListeners();
        this.updateUrgentDeadlines();
    }
    
    setupEventListeners() {
        // View switcher
        const weekBtn = document.querySelector('[data-view="week"]');
        const monthBtn = document.querySelector('[data-view="month"]');
        
        if (weekBtn) {
            weekBtn.addEventListener('click', () => this.switchView('week'));
        }
        if (monthBtn) {
            monthBtn.addEventListener('click', () => this.switchView('month'));
        }
        
        // Course filters
        document.addEventListener('change', (e) => {
            if (e.target.matches('[data-filter]')) {
                this.toggleFilter(e.target.dataset.filter);
            }
        });
    }
    
    switchView(view) {
        this.currentView = view;
        this.renderCalendar();
        
        // Update button states
        document.querySelectorAll('[data-view]').forEach(btn => {
            btn.classList.toggle('bg-coral', btn.dataset.view === view);
            btn.classList.toggle('text-white', btn.dataset.view === view);
            btn.classList.toggle('bg-white', btn.dataset.view !== view);
            btn.classList.toggle('text-navy', btn.dataset.view !== view);
        });
    }
    
    toggleFilter(courseId) {
        const index = this.selectedFilters.indexOf(courseId);
        if (index > -1) {
            this.selectedFilters.splice(index, 1);
        } else {
            this.selectedFilters.push(courseId);
        }
        this.renderCalendar();
    }
    
    getVisibleAssignments() {
        let assignments = [];
        
        Object.keys(this.courses).forEach(courseId => {
            if (this.selectedFilters.includes(courseId)) {
                const course = this.courses[courseId];
                course.assignments.forEach(assignment => {
                    assignments.push({
                        ...assignment,
                        courseId,
                        courseName: course.name,
                        courseColor: course.color
                    });
                });
            }
        });
        
        return assignments.sort((a, b) => new Date(a.date) - new Date(b.date));
    }
    
    renderCalendar() {
        const container = document.getElementById('calendar-container');
        if (!container) return;
        
        if (this.currentView === 'month') {
            this.renderMonthView(container);
        } else {
            this.renderWeekView(container);
        }
    }
    
    renderMonthView(container) {
        const year = this.currentDate.getFullYear();
        const month = this.currentDate.getMonth();
        const firstDay = new Date(year, month, 1);
        const lastDay = new Date(year, month + 1, 0);
        const daysInMonth = lastDay.getDate();
        const startingDayOfWeek = firstDay.getDay();
        
        let html = `
            <div class="flex items-center justify-between mb-6">
                <button onclick="calendar.previousMonth()" class="p-2 hover:bg-gray-100 rounded">
                    <i data-lucide="chevron-left" class="w-5 h-5"></i>
                </button>
                <h3 class="text-xl font-semibold text-navy">
                    ${firstDay.toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}
                </h3>
                <button onclick="calendar.nextMonth()" class="p-2 hover:bg-gray-100 rounded">
                    <i data-lucide="chevron-right" class="w-5 h-5"></i>
                </button>
            </div>
            
            <div class="mb-4 flex flex-wrap gap-2">
                <label class="flex items-center space-x-2 text-sm">
                    <input type="checkbox" data-filter="mat143" ${this.selectedFilters.includes('mat143') ? 'checked' : ''} class="rounded">
                    <span class="w-3 h-3 bg-green-400 rounded-full"></span>
                    <span>MAT 143</span>
                </label>
                <label class="flex items-center space-x-2 text-sm">
                    <input type="checkbox" data-filter="eng111" ${this.selectedFilters.includes('eng111') ? 'checked' : ''} class="rounded">
                    <span class="w-3 h-3 bg-blue-400 rounded-full"></span>
                    <span>ENG 111</span>
                </label>
            </div>
            
            <div class="grid grid-cols-7 gap-1 mb-2">
                ${['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].map(day => 
                    `<div class="p-2 text-center text-sm font-medium text-dusty">${day}</div>`
                ).join('')}
            </div>
            
            <div class="grid grid-cols-7 gap-1">
        `;
        
        // Empty cells for days before month starts
        for (let i = 0; i < startingDayOfWeek; i++) {
            html += '<div class="h-24 bg-gray-50 border border-gray-100"></div>';
        }
        
        // Days of the month
        for (let day = 1; day <= daysInMonth; day++) {
            const currentDay = new Date(year, month, day);
            const dayAssignments = this.getAssignmentsForDate(currentDay);
            const isToday = this.isToday(currentDay);
            const isWeekend = currentDay.getDay() === 0 || currentDay.getDay() === 6;
            
            html += `
                <div class="h-24 border border-gray-100 p-1 ${isToday ? 'bg-coral/10 border-coral' : isWeekend ? 'bg-gray-50' : 'bg-white'} overflow-hidden">
                    <div class="text-sm font-medium text-navy mb-1">${day}</div>
                    <div class="space-y-1">
                        ${dayAssignments.slice(0, 2).map(assignment => 
                            `<div class="text-xs px-1 py-0.5 rounded truncate" style="background-color: ${assignment.courseColor}20; color: ${assignment.courseColor}">
                                ${assignment.name}
                            </div>`
                        ).join('')}
                        ${dayAssignments.length > 2 ? `<div class="text-xs text-dusty">+${dayAssignments.length - 2} more</div>` : ''}
                    </div>
                </div>
            `;
        }
        
        html += '</div>';
        container.innerHTML = html;
        
        // Reinitialize Lucide icons
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    }
    
    renderWeekView(container) {
        const startOfWeek = this.getStartOfWeek(this.currentDate);
        const days = [];
        
        for (let i = 0; i < 7; i++) {
            const day = new Date(startOfWeek);
            day.setDate(startOfWeek.getDate() + i);
            days.push(day);
        }
        
        let html = `
            <div class="flex items-center justify-between mb-6">
                <button onclick="calendar.previousWeek()" class="p-2 hover:bg-gray-100 rounded">
                    <i data-lucide="chevron-left" class="w-5 h-5"></i>
                </button>
                <h3 class="text-xl font-semibold text-navy">
                    Week of ${startOfWeek.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}
                </h3>
                <button onclick="calendar.nextWeek()" class="p-2 hover:bg-gray-100 rounded">
                    <i data-lucide="chevron-right" class="w-5 h-5"></i>
                </button>
            </div>
            
            <div class="grid grid-cols-7 gap-2">
                ${days.map(day => {
                    const dayAssignments = this.getAssignmentsForDate(day);
                    const isToday = this.isToday(day);
                    
                    return `
                        <div class="bg-white border border-dusty/10 rounded-lg p-3 min-h-[200px] ${isToday ? 'ring-2 ring-coral/50' : ''}">
                            <div class="font-medium text-navy mb-3">
                                ${day.toLocaleDateString('en-US', { weekday: 'short', day: 'numeric' })}
                            </div>
                            <div class="space-y-2">
                                ${dayAssignments.map(assignment => 
                                    `<div class="text-xs p-2 rounded" style="background-color: ${assignment.courseColor}20; color: ${assignment.courseColor}">
                                        <div class="font-medium">${assignment.name}</div>
                                        <div class="text-xs opacity-75">${assignment.courseName.split(' - ')[0]}</div>
                                    </div>`
                                ).join('')}
                            </div>
                        </div>
                    `;
                }).join('')}
            </div>
        `;
        
        container.innerHTML = html;
        
        // Reinitialize Lucide icons
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    }
    
    getAssignmentsForDate(date) {
        const assignments = this.getVisibleAssignments();
        return assignments.filter(assignment => {
            const assignmentDate = new Date(assignment.date);
            return this.isSameDay(assignmentDate, date);
        });
    }
    
    getStartOfWeek(date) {
        const d = new Date(date);
        const day = d.getDay();
        const diff = d.getDate() - day;
        return new Date(d.setDate(diff));
    }
    
    isSameDay(date1, date2) {
        return date1.getFullYear() === date2.getFullYear() &&
               date1.getMonth() === date2.getMonth() &&
               date1.getDate() === date2.getDate();
    }
    
    isToday(date) {
        return this.isSameDay(date, new Date());
    }
    
    previousMonth() {
        this.currentDate.setMonth(this.currentDate.getMonth() - 1);
        this.renderCalendar();
    }
    
    nextMonth() {
        this.currentDate.setMonth(this.currentDate.getMonth() + 1);
        this.renderCalendar();
    }
    
    previousWeek() {
        this.currentDate.setDate(this.currentDate.getDate() - 7);
        this.renderCalendar();
    }
    
    nextWeek() {
        this.currentDate.setDate(this.currentDate.getDate() + 7);
        this.renderCalendar();
    }
    
    updateUrgentDeadlines() {
        const urgentContainer = document.getElementById('urgent-deadlines');
        if (!urgentContainer) return;
        
        const today = new Date();
        const twoDaysFromNow = new Date(today.getTime() + (2 * 24 * 60 * 60 * 1000));
        
        const assignments = this.getVisibleAssignments();
        const urgentDeadlines = assignments.filter(assignment => {
            const assignmentDate = new Date(assignment.date);
            return assignmentDate <= twoDaysFromNow && assignmentDate >= today;
        });
        
        if (urgentDeadlines.length === 0) {
            urgentContainer.innerHTML = '<p class="text-dusty text-sm">No urgent deadlines in the next 48 hours.</p>';
        } else {
            urgentContainer.innerHTML = urgentDeadlines.map(deadline => {
                const courseColor = deadline.courseId === 'mat143' ? '#68d391' : '#63b3ed';
                const courseBg = deadline.courseId === 'mat143' ? 'bg-green-100' : 'bg-blue-100';
                const courseText = deadline.courseId === 'mat143' ? 'text-green-700' : 'text-blue-700';
                return `
                    <div class="flex items-center justify-between py-2">
                        <span class="font-medium text-navy">${deadline.name}</span>
                        <span class="text-xs px-2 py-1 rounded ${courseBg} ${courseText}">
                            ${new Date(deadline.date).toLocaleDateString()}
                        </span>
                    </div>
                `;
            }).join('');
        }
    }
}

// Initialize calendar when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.calendar = new AcademicCalendar();
});