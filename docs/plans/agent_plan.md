# Agent Implementation Plan for Kristina’s Academic Dashboard

This plan outlines the high‑level steps for building the new academic dashboard.  Use it as a guide when running Cursor’s Plan Mode and background agents.  Each step should be broken into smaller subtasks as needed during planning and execution.

## 1. Explore and Gather Course Information

- **Inspect existing course pages**: Read through all `chapter-*.html` files, `english_materials.html`, `calendar_study_system.html`, and any syllabus or pacing documents.
- **Extract key details**:
  - Course start and end dates.
  - Weekly pacing: which chapters/essays are covered each week.
  - Assignment names, due dates, test dates, labs, attendance requirements, and the signature assignment.
  - Important deadlines: EVA (attendance verification) deadline, withdrawal deadline, and final exam.
- **Document missing content**: Note any formulas, sections, or topics not currently covered (e.g., APY, present/future value, standard divisor/quota, expected value).

## 2. Remove Legacy Code and Consolidate

- Delete or ignore files in the `_archived/` directory and any prototype pages that are no longer relevant.
- Remove duplicate implementations of calendars or templates; keep the most complete version as a reference.
- Consolidate duplicated CSS and JavaScript into a single, organised structure under `src/styles/` and `src/scripts/`.

## 3. Define Information Architecture

- **Dashboard/Home**: Provide an overview of both courses, including progress bars, upcoming deadlines, and quick links to current assignments.
- **Calendar**: Create a 16‑week interactive calendar with filters by course and urgency (urgent/soon/completed).  Ensure accurate dates for tests, assignments, and labs.
- **Math Tutor**: For each chapter:
  - Write a concise overview.
  - Create formula sheets with definitions and examples.
  - Implement practice problems with solutions.
  - Integrate AI explanations via the Anthropic API.
- **Writing Coach**: For each essay assignment:
  - Include the prompt, rubric, and requirements.
  - Provide writing strategies, revision checklists, and citation guides.
  - Track due dates and submission statuses.
- **Resource Center**: Collate formula lookups, writing resources, external links (Hawkes Learning, Brightspace), and study strategies.

## 4. Build the Design System

- Implement a retro/modern minimal palette using the colour tokens defined in `tokens.json` and the rules file.  Define semantic colours (math green, English blue, warning red, success green).
- Use Vend Sans as the primary font with defined weights (400–900) and ensure high contrast ratios.
- Build reusable components (cards, buttons, forms, navigation bars) with consistent padding, rounded corners, and focus states.
- Store global styles and Tailwind configuration in `src/styles/design-system.css` and extend the Tailwind config accordingly.

## 5. Develop Core Pages

- **index.html**: Dashboard that aggregates progress, deadlines, and quick actions.
- **calendar.html**: Interactive calendar.  Populate it with data extracted in Step 1.  Implement filters and colour coding.
- **tutor.html**: Front‑end for the math tutor.  Provide chapter navigation, formula sheets, practice problems, and an input for AI assistance.
- **english_materials.html**: Writing coach page.  List essay assignments, rubrics, and resources.
- **chapter-*.html**: For each chapter:
  - Section headings corresponding to topics (e.g., proportions, functions, finance).
  - Key formulas with examples.
  - Step‑by‑step problem breakdowns.
  - Practice questions and answers.

## 6. Integrate the AI Tutor

- Write a Python function under `api/` that calls the Anthropic Claude API.  Use the `anthropic` package.
- Define endpoints (e.g., `/api/tutor`) that accept user questions and return model responses.
- Handle missing API keys or errors gracefully by returning fallback study resources.
- Expose the API to the front‑end using `fetch` or a simple `axios` call from the tutor interface.

## 7. Populate Missing Formulas and Sections

- For Chapter 6: Add **APY** and **present/future value** formulas with explanations and examples.
- For Chapter 13: Add **standard divisor** and **standard quota** formulas.
- For Chapters 10 and 11: Add **expected value** definitions and examples.
- Add new lesson pages for topics missing from the original materials (e.g., 1.1 Thinking Mathematically, 1.2 Estimating & Evaluating, 6.2 Saving & Investing, 6.4 Federal Revenue, 10.3 Probability of Single Events, 11.1 Statistical Studies).

## 8. Implement the Writing Coach

- For each essay in ENG 111:
  - Provide the assignment prompt and rubric.
  - Outline the stages of the writing process (brainstorming, drafting, revision).
  - Offer citation tips and links to research resources.
  - Include a checklist to track essay progress (draft due, peer review, final submission).

## 9. Testing and Validation

- Run `python test_system.py` (or create your own tests) to verify that formula lookups, schedule generation, and AI endpoints behave correctly.
- Manually open each page and ensure links, navigation, and interactive elements work as expected.
- Use accessibility tools (e.g., axe-core, Lighthouse) to validate contrast ratios and keyboard navigation.
- Optimise performance to achieve page load times under two seconds.

## 10. Deployment & Review

- Deploy the site to Vercel or Netlify.  Ensure environment variables (e.g., `ANTHROPIC_API_KEY`) are set.
- Perform a final review of the deployed site to confirm that content, dates, and interactions are accurate.
- Merge the feature branch created by the background agent into the main branch once the site meets all success criteria.

## 🚧 Future Improvements

- Implement user authentication if Kristina needs personal notes or saved progress.
- Add analytics to monitor which features she uses most and refine the dashboard based on feedback.
- Build scripts to automatically update deadlines when new semesters or syllabi are released.