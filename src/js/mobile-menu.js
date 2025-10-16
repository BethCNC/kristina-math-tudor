/**
 * Mobile Menu with Focus Trap Management
 * ADHD Accessibility: Prevents keyboard users from getting lost in navigation
 */

class MobileMenu {
  constructor() {
    this.menuButton = document.getElementById('mobile-menu-button');
    this.menu = document.getElementById('mobile-menu');
    this.body = document.body;
    this.isOpen = false;
    this.focusableElements = [];
    this.firstFocusable = null;
    this.lastFocusable = null;
    
    if (this.menuButton && this.menu) {
      this.init();
    }
  }

  init() {
    // Toggle menu on button click
    this.menuButton.addEventListener('click', () => this.toggle());
    
    // Close menu on escape key
    document.addEventListener('keydown', (e) => this.handleEscape(e));
    
    // Close menu when clicking outside
    document.addEventListener('click', (e) => this.handleClickOutside(e));
  }

  toggle() {
    if (this.isOpen) {
      this.close();
    } else {
      this.open();
    }
  }

  open() {
    this.isOpen = true;
    this.menuButton.setAttribute('aria-expanded', 'true');
    this.menu.classList.remove('hidden');
    this.body.classList.add('menu-open');
    
    // Set up focus trap
    this.updateFocusableElements();
    
    // Focus first menu item
    if (this.firstFocusable) {
      this.firstFocusable.focus();
    }
    
    // Add focus trap listeners
    this.menu.addEventListener('keydown', (e) => this.trapFocus(e));
  }

  close() {
    this.isOpen = false;
    this.menuButton.setAttribute('aria-expanded', 'false');
    this.menu.classList.add('hidden');
    this.body.classList.remove('menu-open');
    
    // Return focus to menu button
    this.menuButton.focus();
  }

  updateFocusableElements() {
    // Find all focusable elements within the menu
    this.focusableElements = Array.from(
      this.menu.querySelectorAll(
        'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
      )
    );
    
    this.firstFocusable = this.focusableElements[0];
    this.lastFocusable = this.focusableElements[this.focusableElements.length - 1];
  }

  trapFocus(e) {
    if (e.key !== 'Tab') return;
    
    // Shift + Tab (backwards)
    if (e.shiftKey) {
      if (document.activeElement === this.firstFocusable) {
        e.preventDefault();
        this.lastFocusable.focus();
      }
    }
    // Tab (forwards)
    else {
      if (document.activeElement === this.lastFocusable) {
        e.preventDefault();
        this.firstFocusable.focus();
      }
    }
  }

  handleEscape(e) {
    if (e.key === 'Escape' && this.isOpen) {
      this.close();
    }
  }

  handleClickOutside(e) {
    if (this.isOpen && 
        !this.menu.contains(e.target) && 
        !this.menuButton.contains(e.target)) {
      this.close();
    }
  }
}

// Initialize mobile menu when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new MobileMenu();
});

