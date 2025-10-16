/**
 * AI Math Tutor Frontend Integration
 * Connects the tutor form to the /api/tutor endpoint
 */

class MathTutor {
    constructor() {
        this.form = document.getElementById('tutor-form');
        this.questionInput = document.getElementById('question-input');
        this.chapterSelect = document.getElementById('chapter-select');
        this.responseArea = document.getElementById('tutor-response');
        this.loadingArea = document.getElementById('tutor-loading');
        this.responseContent = document.getElementById('response-content');
        
        this.init();
    }

    init() {
        if (this.form) {
            this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        }
    }

    async handleSubmit(event) {
        event.preventDefault();
        
        const question = this.questionInput.value.trim();
        const chapter = this.chapterSelect.value;
        
        if (!question) {
            this.showError('Please enter a question.');
            return;
        }

        // Show loading state
        this.showLoading();

        try {
            const response = await this.askTutor(question, chapter);
            this.displayResponse(response);
        } catch (error) {
            this.showError('Unable to connect to the tutor. Please try again later or check the resources below.');
        }
    }

    async askTutor(query, chapter = '') {
        const response = await fetch('/api/tutor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                query: query,
                chapter: chapter,
                topic: ''
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }

    showLoading() {
        this.responseArea?.classList.add('hidden');
        this.loadingArea?.classList.remove('hidden');
    }

    displayResponse(data) {
        this.loadingArea?.classList.add('hidden');
        
        if (this.responseContent) {
            // Check if this is a fallback response
            if (data.fallback) {
                this.responseContent.innerHTML = `
                    <div class="alert alert-warning">
                        <i data-lucide="info" class="w-5 h-5"></i>
                        <div>
                            ${data.response}
                        </div>
                    </div>
                `;
            } else {
                // Format the AI response with proper styling
                this.responseContent.innerHTML = this.formatResponse(data.response);
            }
            
            // Re-initialize Lucide icons for any new icons in the response
            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
        }
        
        this.responseArea?.classList.remove('hidden');
        
        // Scroll to response
        this.responseArea?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    formatResponse(text) {
        // Convert markdown-style formatting to HTML
        let formatted = text
            .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.+?)\*/g, '<em>$1</em>')
            .replace(/`(.+?)`/g, '<code class="font-mono bg-smokey-quartz-100 dark:bg-smokey-quartz-800 px-1 py-0.5 rounded text-sm">$1</code>')
            .replace(/\n\n/g, '</p><p class="mb-4">')
            .replace(/\n/g, '<br>');

        return `<div class="prose prose-sm max-w-none dark:prose-invert"><p class="mb-4">${formatted}</p></div>`;
    }

    showError(message) {
        this.loadingArea?.classList.add('hidden');
        
        if (this.responseContent) {
            this.responseContent.innerHTML = `
                <div class="alert alert-danger">
                    <i data-lucide="alert-circle" class="w-5 h-5"></i>
                    <div>
                        <strong>Error</strong>
                        <p class="text-sm mt-1">${message}</p>
                        <div class="mt-3 space-y-2">
                            <p class="text-sm font-medium">Alternative resources:</p>
                            <ul class="text-sm list-disc list-inside ml-2">
                                <li><a href="/formula_lookup.html" class="text-ruby-700 dark:text-ruby-300 hover:underline">Formula Lookup</a></li>
                                <li><a href="https://learn.hawkeslearning.com/" target="_blank" class="text-ruby-700 dark:text-ruby-300 hover:underline">Hawkes Learning</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            `;
            
            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
        }
        
        this.responseArea?.classList.remove('hidden');
    }
}

// Initialize tutor when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new MathTutor();
});

