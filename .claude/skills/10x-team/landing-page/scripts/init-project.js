/**
 * 10x Team Landing Page - Project Initializer
 *
 * Creates the folder structure for a new landing page project.
 *
 * Usage: node init-project.js <project-name> [tech-stack]
 *
 * Tech stacks: html (default), react, nextjs, astro, vue
 */

const fs = require('fs');
const path = require('path');

const projectName = process.argv[2];
const techStack = process.argv[3] || 'html';

if (!projectName) {
  console.error('Usage: node init-project.js <project-name> [tech-stack]');
  console.error('');
  console.error('Tech stacks:');
  console.error('  html    - Static HTML/CSS/JS (default)');
  console.error('  react   - React with Vite');
  console.error('  nextjs  - Next.js (App Router)');
  console.error('  astro   - Astro');
  console.error('  vue     - Vue 3 with Vite');
  process.exit(1);
}

const validStacks = ['html', 'react', 'nextjs', 'astro', 'vue'];
if (!validStacks.includes(techStack)) {
  console.error(`Error: Invalid tech stack "${techStack}".`);
  console.error(`Valid options: ${validStacks.join(', ')}`);
  process.exit(1);
}

const projectRoot = path.join(__dirname, '..', '..', '..', '..', 'projects', projectName);

const folders = [
  'requirements',
  'copy',
  'design',
  'build',
  'testing',
  'launch'
];

// Create project folders
console.log(`\n=== Initializing Project: ${projectName} ===\n`);
console.log(`Tech Stack: ${techStack}`);
console.log('');

folders.forEach(folder => {
  const folderPath = path.join(projectRoot, folder);
  fs.mkdirSync(folderPath, { recursive: true });
  console.log(`Created: ${folder}/`);
});

// Create initial status.json
const status = {
  projectName: projectName,
  techStack: techStack,
  createdAt: new Date().toISOString(),
  currentPhase: 'discovery',
  phases: {
    discovery: { status: 'pending', startedAt: null, completedAt: null },
    copywriting: { status: 'pending', startedAt: null, completedAt: null },
    design: { status: 'pending', startedAt: null, completedAt: null },
    build: { status: 'pending', startedAt: null, completedAt: null, techStack: techStack },
    qa: { status: 'pending', startedAt: null, completedAt: null },
    launch: { status: 'pending', startedAt: null, completedAt: null }
  },
  revisions: [],
  overallStatus: 'in_progress'
};

fs.writeFileSync(
  path.join(projectRoot, 'status.json'),
  JSON.stringify(status, null, 2)
);

// Create user-preferences folder if it doesn't exist
const prefsDir = path.join(__dirname, '..', '..', '..', '..', 'user-preferences');
if (!fs.existsSync(prefsDir)) {
  fs.mkdirSync(prefsDir, { recursive: true });
}

console.log('');
console.log(`=== Project "${projectName}" initialized successfully! ===`);
console.log('');
console.log(`Location: ${projectRoot}`);
console.log(`Tech Stack: ${techStack}`);
console.log('');
console.log('Next steps:');
console.log('  1. Run the Discovery phase to gather requirements');
console.log('  2. Run the Copywriting phase to create content');
console.log('  3. Run the Design phase to define visuals');
console.log(`  4. Run generate-project.js ${projectName} ${techStack} to build`);
console.log('');
