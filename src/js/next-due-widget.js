/**
 * Next Due Widget - ADHD Support Feature
 * Shows upcoming deadlines on every page
 * Critical for students who struggle with time management
 */

// Deadline data - UPDATE THIS AS SEMESTER PROGRESSES
const deadlines = [
    {
        title: 'Test 3',
        course: 'MAT 143',
        description: 'Chapters 6 & 7',
        dueDate: new Date('2025-11-03'),
        endDate: new Date('2025-11-07'),
        link: 'chapter-6.html',
        type: 'test',
        urgency: 'critical' // critical, high, medium, low
    },
    {
        title: 'Essay 3',
        course: 'ENG 111',
        description: 'Analytical Essay',
        dueDate: new Date('2025-11-15T23:59:59'),
        link: 'english/essay-3-guide.html',
        type: 'essay',
        urgency: 'high'
    },
    {
        title: 'Hawkes Ch 6 & 7',
        course: 'MAT 143',
        description: 'Complete before Test 3',
        dueDate: new Date('2025-11-03'),
        link: 'https://learn.hawkeslearning.com',
        type: 'homework',
        urgency: 'critical',
        external: true
    },
    {
        title: 'Test 4',
        course: 'MAT 143',
        description: 'Chapters 10 & 11',
        dueDate: new Date('2025-12-08'),
        endDate: new Date('2025-12-12'),
        link: 'chapter-10.html',
        type: 'test',
        urgency: 'medium'
    },
    {
        title: 'Essay 4',
        course: 'ENG 111',
        description: 'Research Paper',
        dueDate: new Date('2025-12-08T23:59:59'),
        link: 'english/essay-4-guide.html',
        type: 'essay',
        urgency: 'medium'
    }
];

// Calculate days until deadline
function getDaysUntil(date) {
    const now = new Date();
    const diff = date - now;
    const days = Math.ceil(diff / (1000 * 60 * 60 * 24));
    return days;
}

// Get urgency class based on days remaining
function getUrgencyClass(days) {
    if (days < 0) return 'overdue';
    if (days <= 3) return 'critical';
    if (days <= 7) return 'high';
    if (days <= 14) return 'medium';
    return 'low';
}

// Format date range for tests
function formatDateRange(startDate, endDate) {
    const options = { month: 'short', day: 'numeric' };
    if (endDate) {
        return `${startDate.toLocaleDateString('en-US', options)} - ${endDate.toLocaleDateString('en-US', options)}`;
    }
    return startDate.toLocaleDateString('en-US', options);
}

// Create widget HTML
function createNextDueWidget() {
    const now = new Date();
    
    // Filter upcoming deadlines (not past) and sort by date
    const upcoming = deadlines
        .filter(d => d.dueDate > now || (d.endDate && d.endDate > now))
        .sort((a, b) => a.dueDate - b.dueDate)
        .slice(0, 3); // Show next 3 deadlines

    if (upcoming.length === 0) {
        return ''; // No upcoming deadlines
    }

    let widgetHTML = `
        <div id="next-due-widget" class="next-due-widget" role="complementary" aria-label="Upcoming deadlines">
            <div class="next-due-header">
                <div class="flex items-center gap-2">
                    <i data-lucide="clock" style="width: 16px; height: 16px;"></i>
                    <h3 style="margin: 0; font-size: var(--font-size-sm); font-weight: 600;">NEXT DUE</h3>
                </div>
                <button id="toggle-widget" class="btn-icon" aria-label="Toggle deadline widget">
                    <i data-lucide="chevron-down" style="width: 16px; height: 16px;"></i>
                </button>
            </div>
            <div id="widget-content" class="next-due-content">
    `;

    upcoming.forEach((deadline, index) => {
        const days = getDaysUntil(deadline.dueDate);
        const urgency = getUrgencyClass(days);
        const dateDisplay = deadline.endDate 
            ? formatDateRange(deadline.dueDate, deadline.endDate)
            : formatDateRange(deadline.dueDate);
        
        const urgencyColor = {
            'critical': 'var(--danger-red)',
            'high': 'var(--warning-orange)',
            'medium': 'var(--primary-blue)',
            'low': 'var(--neutral-gray-light)'
        }[urgency];

        const urgencyBg = {
            'critical': '#fef2f2',
            'high': '#fef3c7',
            'medium': '#f0f9ff',
            'low': '#f9fafb'
        }[urgency];

        const daysText = days === 0 ? 'TODAY' : 
                        days === 1 ? 'Tomorrow' : 
                        days < 0 ? 'OVERDUE' :
                        `${days} days`;

        widgetHTML += `
            <div class="deadline-item ${urgency}" style="background-color: ${urgencyBg}; border-left-color: ${urgencyColor};">
                <div style="display: flex; justify-content: between; align-items: start; margin-bottom: var(--space-2);">
                    <div style="flex: 1;">
                        <p style="margin: 0; font-size: var(--font-size-xs); color: var(--neutral-gray-light); font-weight: 600;">${deadline.course}</p>
                        <p style="margin: 0; font-size: var(--font-size-sm); font-weight: 600; color: ${urgencyColor};">${deadline.title}</p>
                    </div>
                    <span class="days-badge" style="background-color: ${urgencyColor}; color: var(--white);">${daysText}</span>
                </div>
                <p style="margin: 0 0 var(--space-2) 0; font-size: var(--font-size-xs); color: var(--neutral-gray-light);">${deadline.description}</p>
                <p style="margin: 0 0 var(--space-3) 0; font-size: var(--font-size-xs); font-weight: 600;">${dateDisplay}</p>
                <a href="${deadline.link}" class="btn btn-sm btn-primary w-full" ${deadline.external ? 'target="_blank" rel="noopener"' : ''}>
                    ${deadline.type === 'test' ? 'Prepare' : deadline.type === 'essay' ? 'Start Writing' : 'Complete'}
                </a>
            </div>
        `;
    });

    widgetHTML += `
            </div>
            <div class="next-due-footer">
                <a href="deadlines.html" class="btn btn-sm btn-secondary w-full">View All Deadlines</a>
            </div>
        </div>
    `;

    return widgetHTML;
}

// Initialize widget
function initNextDueWidget() {
    // Create widget element
    const widgetHTML = createNextDueWidget();
    if (!widgetHTML) return; // No deadlines to show

    // Insert widget into page
    const widgetContainer = document.createElement('div');
    widgetContainer.innerHTML = widgetHTML;
    document.body.appendChild(widgetContainer.firstElementChild);

    // Initialize Lucide icons in widget
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // Toggle widget collapse
    const toggleBtn = document.getElementById('toggle-widget');
    const content = document.getElementById('widget-content');
    const widget = document.getElementById('next-due-widget');
    
    if (toggleBtn && content) {
        toggleBtn.addEventListener('click', () => {
            const isCollapsed = content.style.display === 'none';
            content.style.display = isCollapsed ? 'block' : 'none';
            widget.classList.toggle('collapsed', !isCollapsed);
            
            const icon = toggleBtn.querySelector('[data-lucide]');
            if (icon) {
                icon.setAttribute('data-lucide', isCollapsed ? 'chevron-down' : 'chevron-up');
                lucide.createIcons();
            }
        });
    }
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initNextDueWidget);
} else {
    initNextDueWidget();
}

