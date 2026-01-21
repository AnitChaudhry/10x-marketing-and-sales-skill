/**
 * 10x Team Landing Page - Project Lister
 *
 * Lists all landing page projects and their status.
 *
 * Usage: node list-projects.js
 */

const fs = require('fs');
const path = require('path');

const projectsRoot = path.join(__dirname, '..', '..', '..', '..', 'projects');

if (!fs.existsSync(projectsRoot)) {
  console.log('No projects folder found. Run /landing-page new to create your first project.');
  process.exit(0);
}

const projects = fs.readdirSync(projectsRoot, { withFileTypes: true })
  .filter(dirent => dirent.isDirectory())
  .map(dirent => {
    const statusPath = path.join(projectsRoot, dirent.name, 'status.json');
    let status = { overallStatus: 'unknown', currentPhase: 'unknown' };

    if (fs.existsSync(statusPath)) {
      try {
        status = JSON.parse(fs.readFileSync(statusPath, 'utf8'));
      } catch (e) {
        // Keep default status
      }
    }

    return {
      name: dirent.name,
      status: status.overallStatus || 'unknown',
      phase: status.currentPhase || 'unknown',
      createdAt: status.createdAt || 'unknown'
    };
  });

if (projects.length === 0) {
  console.log('No projects found. Run /landing-page new to create your first project.');
  process.exit(0);
}

console.log('\\n10x Team Landing Page Projects\\n');
console.log('=' .repeat(60));
console.log('');

projects.forEach((project, index) => {
  const statusIcon = project.status === 'complete' ? '✅' :
                     project.status === 'in_progress' ? '🔄' : '⏸️';

  console.log(`${index + 1}. ${project.name}`);
  console.log(`   Status: ${statusIcon} ${project.status}`);
  console.log(`   Current Phase: ${project.phase}`);
  console.log(`   Created: ${project.createdAt}`);
  console.log('');
});

console.log('=' .repeat(60));
console.log(`\\nTotal: ${projects.length} project(s)`);
console.log('\\nTo resume a project: /landing-page resume <project-name>');
