import { defineConfig } from 'vite'

export default defineConfig({
  root: '.',
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: {
        main: './index.html',
        calendar: './calendar.html',
        tutor: './tutor.html',
        formulaLookup: './formula_lookup.html',
        englishMaterials: './english_materials.html',
        chapter1: './chapter-1.html',
        chapter4: './chapter-4.html',
        chapter6: './chapter-6.html',
        chapter7: './chapter-7.html',
        chapter13: './chapter-13.html'
        // Temporarily disabled due to CSS parsing issues
        // chapter5: './chapter-5.html',
        // chapter10: './chapter-10.html',
        // chapter11: './chapter-11.html'
      }
    }
  },
  css: {
    postcss: './postcss.config.js'
  },
  server: {
    port: 3000
  }
})
