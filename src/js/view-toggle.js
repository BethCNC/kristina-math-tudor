/**
 * E-Learning Dashboard - View Toggle Component
 * Handles switching between Progress and Calendar views
 * Used on dashboard and calendar pages
 */

(function() {
  'use strict';
  
  // View toggle state management
  const ViewToggle = {
    currentView: 'progress', // default view
    
    init() {
      const toggle = document.querySelector('.switch');
      if (!toggle) return;
      
      // Get saved view preference
      this.currentView = localStorage.getItem('preferredView') || 'progress';
      
      // Set initial active state
      this.setActiveButton(this.currentView);
      this.showView(this.currentView);
      
      // Add click handlers to switch items
      const switchItems = toggle.querySelectorAll('.switch-item');
      switchItems.forEach(item => {
        item.addEventListener('click', (e) => this.handleToggle(e));
      });
    },
    
    handleToggle(event) {
      const button = event.currentTarget;
      const view = button.dataset.view;
      
      if (view && view !== this.currentView) {
        this.switchView(view);
      }
    },
    
    switchView(newView) {
      // Update state
      this.currentView = newView;
      
      // Save preference
      localStorage.setItem('preferredView', newView);
      
      // Update UI
      this.setActiveButton(newView);
      this.showView(newView);
      
      // Dispatch custom event for other components to listen
      window.dispatchEvent(new CustomEvent('viewChanged', {
        detail: { view: newView }
      }));
    },
    
    setActiveButton(view) {
      const switchItems = document.querySelectorAll('.switch-item');
      switchItems.forEach(item => {
        const itemView = item.dataset.view;
        if (itemView === view) {
          item.classList.add('active');
          item.setAttribute('aria-pressed', 'true');
        } else {
          item.classList.remove('active');
          item.setAttribute('aria-pressed', 'false');
        }
      });
    },
    
    showView(view) {
      // Hide all views
      const progressView = document.getElementById('progress-view');
      const calendarView = document.getElementById('calendar-view');
      
      if (progressView && calendarView) {
        if (view === 'progress') {
          progressView.classList.remove('hidden');
          progressView.setAttribute('aria-hidden', 'false');
          calendarView.classList.add('hidden');
          calendarView.setAttribute('aria-hidden', 'true');
        } else {
          progressView.classList.add('hidden');
          progressView.setAttribute('aria-hidden', 'true');
          calendarView.classList.remove('hidden');
          calendarView.setAttribute('aria-hidden', 'false');
        }
        
        // Smooth transition
        requestAnimationFrame(() => {
          const activeView = view === 'progress' ? progressView : calendarView;
          activeView.classList.add('fade-in');
        });
      }
    }
  };
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => ViewToggle.init());
  } else {
    ViewToggle.init();
  }
  
  // Export for external use
  window.ViewToggle = ViewToggle;
})();

