/**
 * 10x Team Landing Page - Unified Project Generator
 *
 * Generates a complete landing page project based on tech stack selection.
 *
 * Usage: node generate-project.js <project-name> [tech-stack]
 *
 * Tech stacks: html (default), react, nextjs, astro, vue
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const projectName = process.argv[2];
const techStack = process.argv[3] || 'html';

if (!projectName) {
  console.error('Usage: node generate-project.js <project-name> [tech-stack]');
  console.error('');
  console.error('Tech stacks:');
  console.error('  html    - Static HTML/CSS/JS (default)');
  console.error('  react   - React with Vite');
  console.error('  nextjs  - Next.js (App Router)');
  console.error('  astro   - Astro');
  console.error('  vue     - Vue 3 with Vite');
  process.exit(1);
}

const projectRoot = path.join(__dirname, '..', '..', '..', '..', 'projects', projectName);
const prefsPath = path.join(__dirname, '..', '..', '..', '..', 'user-preferences', `${projectName}.json`);

// Validate project exists
if (!fs.existsSync(projectRoot)) {
  console.error(`Error: Project "${projectName}" not found.`);
  console.error(`Expected location: ${projectRoot}`);
  console.error('');
  console.error('Run init-project.js first to create the project structure.');
  process.exit(1);
}

// Validate brief.json exists
const briefPath = path.join(projectRoot, 'requirements', 'brief.json');
if (!fs.existsSync(briefPath)) {
  console.error('Error: requirements/brief.json not found.');
  console.error('Run the Discovery phase first to generate the brief.');
  process.exit(1);
}

// Map tech stack to generator script
const generators = {
  'html': 'generate-html.js',
  'react': 'generate-react.js',
  'nextjs': 'generate-nextjs.js',
  'astro': 'generate-astro.js',
  'vue': 'generate-vue.js'
};

const validStacks = Object.keys(generators);

if (!validStacks.includes(techStack)) {
  console.error(`Error: Invalid tech stack "${techStack}".`);
  console.error(`Valid options: ${validStacks.join(', ')}`);
  process.exit(1);
}

const generatorScript = path.join(__dirname, generators[techStack]);

console.log(`\n=== 10x Team Landing Page Generator ===\n`);
console.log(`Project: ${projectName}`);
console.log(`Tech Stack: ${techStack}`);
console.log(`Generator: ${generators[techStack]}`);
console.log('');

// Run the appropriate generator
try {
  execSync(`node "${generatorScript}" "${projectName}"`, {
    stdio: 'inherit',
    cwd: __dirname
  });

  // Update project status
  const statusPath = path.join(projectRoot, 'status.json');
  if (fs.existsSync(statusPath)) {
    const status = JSON.parse(fs.readFileSync(statusPath, 'utf8'));
    status.techStack = techStack;
    status.phases.build = {
      status: 'completed',
      startedAt: new Date().toISOString(),
      completedAt: new Date().toISOString(),
      techStack: techStack
    };
    fs.writeFileSync(statusPath, JSON.stringify(status, null, 2));
  }

  console.log('\n=== Generation Complete ===\n');
  console.log(`Output: ${path.join(projectRoot, 'build')}`);
  console.log('');
  console.log('To run locally:');

  if (techStack === 'html') {
    console.log('  Open build/index.html in your browser');
    console.log('  Or use a local server:');
    console.log('    npx serve build');
  } else {
    console.log(`  cd projects/${projectName}/build`);
    console.log('  npm install');
    console.log('  npm run dev');
  }

  console.log('');

} catch (error) {
  console.error('Error running generator:', error.message);
  process.exit(1);
}
