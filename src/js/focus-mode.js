/**
 * Focus Mode for ADHD Users
 * Strips away non-essential UI elements to support deep focus
 * Saves preference to localStorage
 */

class FocusMode {
  constructor() {
    this.isActive = false;
    this.storageKey = 'kristina_focus_mode';
    this.toggleButton = null;
    
    this.loadPreference();
    this.init();
  }

  /**
   * Initialize focus mode
   */
  init() {
    // Create toggle button
    this.createToggleButton();
    
    // Apply saved preference
    if (this.isActive) {
      this.activate();
    }
  }

  /**
   * Load user preference from localStorage
   */
  loadPreference() {
    try {
      const stored = localStorage.getItem(this.storageKey);
      this.isActive = stored === 'true';
    } catch (error) {
      console.error('Error loading focus mode preference:', error);
    }
  }

  /**
   * Save preference to localStorage
   */
  savePreference() {
    try {
      localStorage.setItem(this.storageKey, this.isActive.toString());
    } catch (error) {
      console.error('Error saving focus mode preference:', error);
    }
  }

  /**
   * Create floating toggle button
   */
  createToggleButton() {
    this.toggleButton = document.createElement('button');
    this.toggleButton.className = 'focus-mode-toggle';
    this.toggleButton.setAttribute('aria-pressed', this.isActive);
    this.toggleButton.setAttribute('aria-label', 'Toggle focus mode');
    this.toggleButton.title = 'Focus Mode: Hide distractions';
    
    this.toggleButton.innerHTML = `
      <i data-lucide="eye-off" class="w-5 h-5"></i>
      <span class="focus-mode-label">Focus</span>
    `;
    
    this.toggleButton.addEventListener('click', () => this.toggle());
    
    document.body.appendChild(this.toggleButton);
    
    // Initialize Lucide icon
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }
  }

  /**
   * Toggle focus mode on/off
   */
  toggle() {
    if (this.isActive) {
      this.deactivate();
    } else {
      this.activate();
    }
  }

  /**
   * Activate focus mode
   */
  activate() {
    this.isActive = true;
    document.body.classList.add('focus-mode-active');
    this.toggleButton.setAttribute('aria-pressed', 'true');
    this.toggleButton.querySelector('.focus-mode-label').textContent = 'Exit';
    
    this.savePreference();
    
    // Announce to screen readers
    this.announce('Focus mode activated. Non-essential elements hidden.');
  }

  /**
   * Deactivate focus mode
   */
  deactivate() {
    this.isActive = false;
    document.body.classList.remove('focus-mode-active');
    this.toggleButton.setAttribute('aria-pressed', 'false');
    this.toggleButton.querySelector('.focus-mode-label').textContent = 'Focus';
    
    this.savePreference();
    
    // Announce to screen readers
    this.announce('Focus mode deactivated. All elements visible.');
  }

  /**
   * Announce changes to screen readers
   */
  announce(message) {
    const announcement = document.createElement('div');
    announcement.setAttribute('role', 'status');
    announcement.setAttribute('aria-live', 'polite');
    announcement.className = 'sr-only';
    announcement.textContent = message;
    
    document.body.appendChild(announcement);
    
    // Remove after announcement
    setTimeout(() => announcement.remove(), 1000);
  }
}

// Create global instance
const focusMode = new FocusMode();

// Export for global use
window.focusMode = focusMode;

