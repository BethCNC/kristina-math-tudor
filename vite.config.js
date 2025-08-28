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
        reference: './reference.html',
        calendarStudy: './calendar_study_system.html',
        studyHelper: './web_study_helper.html'
      }
    }
  },
  server: {
    port: 3000
  }
})
