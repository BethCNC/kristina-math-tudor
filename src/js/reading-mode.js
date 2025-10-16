/**
 * Reading Mode Controls
 * ADHD Accessibility: Adjustable font size and line spacing
 * Accommodates different reading preferences and improves comprehension
 */

class ReadingMode {
  constructor() {
    this.fontSize = 100; // Percentage
    this.lineSpacing = 1.6; // Default line-height
    this.highContrast = false;
    this.storageKey = 'kristina_reading_mode';
    this.controlsContainer = null;
    
    this.loadPreferences();
    this.init();
  }

  /**
   * Initialize reading mode controls
   */
  init() {
    this.createControls();
    this.applyPreferences();
  }

  /**
   * Load user preferences from localStorage
   */
  loadPreferences() {
    try {
      const stored = localStorage.getItem(this.storageKey);
      if (stored) {
        const prefs = JSON.parse(stored);
        this.fontSize = prefs.fontSize || 100;
        this.lineSpacing = prefs.lineSpacing || 1.6;
        this.highContrast = prefs.highContrast || false;
      }
    } catch (error) {
      console.error('Error loading reading preferences:', error);
    }
  }

  /**
   * Save preferences to localStorage
   */
  savePreferences() {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify({
        fontSize: this.fontSize,
        lineSpacing: this.lineSpacing,
        highContrast: this.highContrast
      }));
    } catch (error) {
      console.error('Error saving reading preferences:', error);
    }
  }

  /**
   * Create reading mode controls UI
   */
  createControls() {
    this.controlsContainer = document.createElement('div');
    this.controlsContainer.className = 'reading-mode-controls';
    this.controlsContainer.setAttribute('role', 'toolbar');
    this.controlsContainer.setAttribute('aria-label', 'Reading preferences');
    
    this.controlsContainer.innerHTML = `
      <button class="reading-control-toggle" aria-label="Toggle reading controls" aria-expanded="false">
        <i data-lucide="type" class="w-5 h-5"></i>
      </button>
      <div class="reading-controls-panel hidden">
        <div class="reading-control-group">
          <label class="reading-control-label">Font Size</label>
          <div class="reading-control-buttons">
            <button class="reading-control-btn" onclick="readingMode.decreaseFontSize()" aria-label="Decrease font size">
              <span class="text-lg">A-</span>
            </button>
            <span class="reading-control-value" id="font-size-value">100%</span>
            <button class="reading-control-btn" onclick="readingMode.increaseFontSize()" aria-label="Increase font size">
              <span class="text-lg">A+</span>
            </button>
          </div>
        </div>
        
        <div class="reading-control-group">
          <label class="reading-control-label">Line Spacing</label>
          <div class="reading-control-buttons">
            <button class="reading-control-btn" onclick="readingMode.decreaseLineSpacing()" aria-label="Decrease line spacing">
              <i data-lucide="minus" class="w-4 h-4"></i>
            </button>
            <span class="reading-control-value" id="line-spacing-value">1.6</span>
            <button class="reading-control-btn" onclick="readingMode.increaseLineSpacing()" aria-label="Increase line spacing">
              <i data-lucide="plus" class="w-4 h-4"></i>
            </button>
          </div>
        </div>
        
        <div class="reading-control-group">
          <label class="reading-control-label">High Contrast</label>
          <button class="reading-control-btn-full" onclick="readingMode.toggleHighContrast()" aria-pressed="${this.highContrast}">
            <i data-lucide="contrast" class="w-4 h-4"></i>
            <span id="contrast-status">${this.highContrast ? 'On' : 'Off'}</span>
          </button>
        </div>
        
        <button class="reading-control-reset" onclick="readingMode.reset()" aria-label="Reset to defaults">
          <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
          Reset
        </button>
      </div>
    `;
    
    document.body.appendChild(this.controlsContainer);
    
    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }

    // Add toggle functionality
    const toggleBtn = this.controlsContainer.querySelector('.reading-control-toggle');
    const panel = this.controlsContainer.querySelector('.reading-controls-panel');
    
    toggleBtn.addEventListener('click', () => {
      const isExpanded = toggleBtn.getAttribute('aria-expanded') === 'true';
      toggleBtn.setAttribute('aria-expanded', !isExpanded);
      panel.classList.toggle('hidden');
    });
  }

  /**
   * Apply current preferences to the page
   */
  applyPreferences() {
    document.documentElement.style.fontSize = `${this.fontSize}%`;
    document.documentElement.style.lineHeight = this.lineSpacing;
    
    if (this.highContrast) {
      document.body.classList.add('high-contrast-mode');
    } else {
      document.body.classList.remove('high-contrast-mode');
    }

    this.updateUI();
  }

  /**
   * Update control UI to reflect current values
   */
  updateUI() {
    const fontSizeEl = document.getElementById('font-size-value');
    const lineSpacingEl = document.getElementById('line-spacing-value');
    const contrastStatusEl = document.getElementById('contrast-status');
    
    if (fontSizeEl) fontSizeEl.textContent = `${this.fontSize}%`;
    if (lineSpacingEl) lineSpacingEl.textContent = this.lineSpacing.toFixed(1);
    if (contrastStatusEl) contrastStatusEl.textContent = this.highContrast ? 'On' : 'Off';
  }

  /**
   * Increase font size
   */
  increaseFontSize() {
    if (this.fontSize < 150) {
      this.fontSize += 10;
      this.applyPreferences();
      this.savePreferences();
    }
  }

  /**
   * Decrease font size
   */
  decreaseFontSize() {
    if (this.fontSize > 80) {
      this.fontSize -= 10;
      this.applyPreferences();
      this.savePreferences();
    }
  }

  /**
   * Increase line spacing
   */
  increaseLineSpacing() {
    if (this.lineSpacing < 2.5) {
      this.lineSpacing += 0.2;
      this.applyPreferences();
      this.savePreferences();
    }
  }

  /**
   * Decrease line spacing
   */
  decreaseLineSpacing() {
    if (this.lineSpacing > 1.2) {
      this.lineSpacing -= 0.2;
      this.applyPreferences();
      this.savePreferences();
    }
  }

  /**
   * Toggle high contrast mode
   */
  toggleHighContrast() {
    this.highContrast = !this.highContrast;
    this.applyPreferences();
    this.savePreferences();
    
    const btn = this.controlsContainer.querySelector('[aria-pressed]');
    if (btn) {
      btn.setAttribute('aria-pressed', this.highContrast);
    }
  }

  /**
   * Reset to default values
   */
  reset() {
    this.fontSize = 100;
    this.lineSpacing = 1.6;
    this.highContrast = false;
    this.applyPreferences();
    this.savePreferences();
  }
}

// Create global instance
const readingMode = new ReadingMode();

// Export for global use
window.readingMode = readingMode;

