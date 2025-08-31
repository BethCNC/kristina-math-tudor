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
        englishMaterials: './english_materials.html'
      }
    }
  },
  server: {
    port: 3000
  }
})
