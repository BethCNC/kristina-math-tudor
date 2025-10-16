/**
 * E-Learning Dashboard - Mobile Bottom Navigation
 * Handles mobile bottom nav active states and navigation
 */

(function() {
  'use strict';
  
  // Determine current page
  function getCurrentPage() {
    const path = window.location.pathname;
    const page = path.split('/').pop() || 'index.html';
    
    // Map pages to nav items
    if (page === 'index.html' || page === '') return 'home';
    if (page.includes('chapter') || page === 'tutor.html') return 'courses';
    if (page === 'calendar.html') return 'calendar';
    if (page === 'formula_lookup.html' || page === 'english_materials.html') return 'resources';
    if (page === 'profile.html') return 'profile';
    
    return 'home';
  }
  
  // Set active nav item
  function setActiveNavItem() {
    const currentPage = getCurrentPage();
    const navItems = document.querySelectorAll('.nav-item-mobile');
    
    navItems.forEach(item => {
      const itemPage = item.dataset.page;
      if (itemPage === currentPage) {
        item.classList.add('active');
        item.setAttribute('aria-current', 'page');
      } else {
        item.classList.remove('active');
        item.removeAttribute('aria-current');
      }
    });
  }
  
  // Handle nav item clicks
  function handleNavClick(event) {
    const navItem = event.currentTarget;
    const href = navItem.getAttribute('href');
    
    // Let browser handle navigation normally
    // Active state will be set on page load
  }
  
  // Initialize bottom navigation
  function initBottomNav() {
    // Set active state on page load
    setActiveNavItem();
    
    // Add click handlers
    const navItems = document.querySelectorAll('.nav-item-mobile');
    navItems.forEach(item => {
      item.addEventListener('click', handleNavClick);
    });
    
    // Update active state on popstate (browser back/forward)
    window.addEventListener('popstate', setActiveNavItem);
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBottomNav);
  } else {
    initBottomNav();
  }
})();

