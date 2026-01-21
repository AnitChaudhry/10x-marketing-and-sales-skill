/**
 * 10x Team Landing Page - Astro Generator
 *
 * Generates an Astro project from project specifications.
 *
 * Usage: node generate-astro.js <project-name>
 */

const fs = require('fs');
const path = require('path');

const projectName = process.argv[2];

if (!projectName) {
  console.error('Usage: node generate-astro.js <project-name>');
  process.exit(1);
}

const projectRoot = path.join(__dirname, '..', '..', '..', '..', 'projects', projectName);
const buildDir = path.join(projectRoot, 'build');

// Check if required files exist
const briefPath = path.join(projectRoot, 'requirements', 'brief.json');
const colorsPath = path.join(projectRoot, 'design', 'colors.json');
const typographyPath = path.join(projectRoot, 'design', 'typography.json');

if (!fs.existsSync(briefPath)) {
  console.error('Error: requirements/brief.json not found. Run discovery phase first.');
  process.exit(1);
}

// Load specifications
const brief = JSON.parse(fs.readFileSync(briefPath, 'utf8'));
const colors = fs.existsSync(colorsPath) ? JSON.parse(fs.readFileSync(colorsPath, 'utf8')) : getDefaultColors();
const typography = fs.existsSync(typographyPath) ? JSON.parse(fs.readFileSync(typographyPath, 'utf8')) : getDefaultTypography();

function getDefaultColors() {
  return {
    brand: { primary: '#2563eb', primaryLight: '#3b82f6', primaryDark: '#1d4ed8' },
    neutral: { background: '#ffffff', surface: '#f8fafc', border: '#e2e8f0', textPrimary: '#1e293b', textSecondary: '#64748b' }
  };
}

function getDefaultTypography() {
  return {
    fonts: { heading: 'Inter', body: 'Inter' },
    scale: { h1: 'clamp(2.5rem, 5vw, 4rem)', h2: 'clamp(2rem, 4vw, 3rem)', body: '1rem' }
  };
}

// Create Astro project structure
const dirs = [
  'src/pages',
  'src/layouts',
  'src/components',
  'src/styles',
  'public'
];

dirs.forEach(dir => {
  fs.mkdirSync(path.join(buildDir, dir), { recursive: true });
});

// package.json
const packageJson = {
  "name": projectName.toLowerCase().replace(/\s+/g, '-'),
  "type": "module",
  "version": "1.0.0",
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^4.0.0"
  }
};

fs.writeFileSync(path.join(buildDir, 'package.json'), JSON.stringify(packageJson, null, 2));
console.log('Created: package.json');

// astro.config.mjs
const astroConfig = `import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://example.com',
});
`;

fs.writeFileSync(path.join(buildDir, 'astro.config.mjs'), astroConfig);
console.log('Created: astro.config.mjs');

// tsconfig.json
const tsConfig = {
  "extends": "astro/tsconfigs/strict"
};

fs.writeFileSync(path.join(buildDir, 'tsconfig.json'), JSON.stringify(tsConfig, null, 2));
console.log('Created: tsconfig.json');

// src/styles/global.css
const globalCss = `/* 10x Team Landing Page - Astro Styles */

:root {
  --color-primary: ${colors.brand?.primary || '#2563eb'};
  --color-primary-light: ${colors.brand?.primaryLight || '#3b82f6'};
  --color-primary-dark: ${colors.brand?.primaryDark || '#1d4ed8'};
  --color-bg: ${colors.neutral?.background || '#ffffff'};
  --color-surface: ${colors.neutral?.surface || '#f8fafc'};
  --color-border: ${colors.neutral?.border || '#e2e8f0'};
  --color-text: ${colors.neutral?.textPrimary || '#1e293b'};
  --color-text-secondary: ${colors.neutral?.textSecondary || '#64748b'};
  --font-heading: '${typography.fonts?.heading || 'Inter'}', sans-serif;
  --font-body: '${typography.fonts?.body || 'Inter'}', sans-serif;
  --text-h1: ${typography.scale?.h1 || 'clamp(2.5rem, 5vw, 4rem)'};
  --text-h2: ${typography.scale?.h2 || 'clamp(2rem, 4vw, 3rem)'};
  --text-body: ${typography.scale?.body || '1rem'};
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 1.5rem;
  --space-lg: 2rem;
  --space-xl: 3rem;
  --space-2xl: 5rem;
  --max-width: 1200px;
  --radius-md: 8px;
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
  --transition-fast: 150ms ease;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html { scroll-behavior: smooth; }

body {
  font-family: var(--font-body);
  font-size: var(--text-body);
  line-height: 1.6;
  color: var(--color-text);
  background-color: var(--color-bg);
}

.container {
  width: 100%;
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--space-md);
}

.section {
  padding: var(--space-2xl) 0;
}

.section-header {
  text-align: center;
  max-width: 700px;
  margin: 0 auto var(--space-xl);
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-sm) var(--space-lg);
  font-family: var(--font-body);
  font-weight: 600;
  border: none;
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--transition-fast);
  text-decoration: none;
}

.btn-primary {
  background: var(--color-primary);
  color: white;
}

.btn-primary:hover {
  background: var(--color-primary-dark);
  transform: translateY(-2px);
}

.btn-lg {
  padding: var(--space-md) var(--space-xl);
  font-size: 1.125rem;
}

/* Navigation */
.nav {
  position: sticky;
  top: 0;
  background: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
  z-index: 100;
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 4rem;
}

.nav-logo {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 1.25rem;
  color: var(--color-text);
  text-decoration: none;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: var(--space-lg);
}

.nav-links {
  display: flex;
  list-style: none;
  gap: var(--space-lg);
}

.nav-links a {
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color var(--transition-fast);
}

.nav-links a:hover {
  color: var(--color-primary);
}

/* Hero */
.hero {
  text-align: center;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero h1 {
  font-size: var(--text-h1);
  margin-bottom: var(--space-md);
}

.hero-subtitle {
  font-size: 1.25rem;
  color: var(--color-text-secondary);
  margin-bottom: var(--space-lg);
}

.hero-cta {
  display: flex;
  gap: var(--space-sm);
  justify-content: center;
}

/* Features */
.features {
  background: var(--color-surface);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--space-lg);
}

.feature-card {
  background: var(--color-bg);
  padding: var(--space-lg);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
}

.feature-card h3 {
  margin-bottom: var(--space-sm);
}

.feature-card p {
  color: var(--color-text-secondary);
}

/* Testimonials */
.testimonial {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

.testimonial blockquote {
  font-size: 1.25rem;
  font-style: italic;
  margin-bottom: var(--space-md);
}

.testimonial cite {
  color: var(--color-text-secondary);
}

/* CTA Section */
.cta-section {
  background: var(--color-primary);
  color: white;
  text-align: center;
}

.cta-section h2 {
  font-size: var(--text-h2);
  margin-bottom: var(--space-md);
}

.cta-section p {
  margin-bottom: var(--space-lg);
  opacity: 0.9;
}

.cta-section .btn {
  background: white;
  color: var(--color-primary);
}

/* Footer */
.footer {
  padding: var(--space-lg) 0;
  border-top: 1px solid var(--color-border);
  text-align: center;
  color: var(--color-text-secondary);
}
`;

fs.writeFileSync(path.join(buildDir, 'src', 'styles', 'global.css'), globalCss);
console.log('Created: src/styles/global.css');

// src/layouts/Layout.astro
const layoutAstro = `---
interface Props {
  title: string;
  description?: string;
}

const { title, description = '' } = Astro.props;
---

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={description} />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=${typography.fonts.heading}:wght@400;500;600;700&family=${typography.fonts.body}:wght@400;500;600&display=swap" rel="stylesheet">
    <title>{title}</title>
  </head>
  <body>
    <slot />
  </body>
</html>

<style is:global>
  @import '../styles/global.css';
</style>
`;

fs.writeFileSync(path.join(buildDir, 'src', 'layouts', 'Layout.astro'), layoutAstro);
console.log('Created: src/layouts/Layout.astro');

// src/pages/index.astro
const indexAstro = `---
import Layout from '../layouts/Layout.astro';
import Hero from '../components/Hero.astro';
import Features from '../components/Features.astro';
import Testimonials from '../components/Testimonials.astro';
import CTA from '../components/CTA.astro';
import Footer from '../components/Footer.astro';
---

<Layout title="${brief.projectName || 'Landing Page'}" description="${brief.summary?.oneLiner || ''}">
  <nav class="nav">
    <div class="nav-container container">
      <a href="/" class="nav-logo">${brief.projectName || 'Brand'}</a>
      <div class="nav-menu">
        <ul class="nav-links">
          <li><a href="#features">Features</a></li>
          <li><a href="#testimonials">Testimonials</a></li>
        </ul>
        <a href="#cta" class="btn btn-primary">Get Started</a>
      </div>
    </div>
  </nav>

  <main>
    <Hero />
    <Features />
    <Testimonials />
    <CTA />
  </main>

  <Footer />
</Layout>
`;

fs.writeFileSync(path.join(buildDir, 'src', 'pages', 'index.astro'), indexAstro);
console.log('Created: src/pages/index.astro');

// Components
const heroAstro = `---
// Hero Component
---

<header class="hero section">
  <div class="container">
    <div class="hero-content">
      <h1>[HEADLINE GOES HERE]</h1>
      <p class="hero-subtitle">[SUBHEAD GOES HERE]</p>
      <div class="hero-cta">
        <a href="#cta" class="btn btn-primary btn-lg">[PRIMARY CTA]</a>
      </div>
    </div>
  </div>
</header>
`;

const featuresAstro = `---
// Features Component
const features = [
  { title: '[FEATURE 1]', description: '[FEATURE 1 DESCRIPTION]' },
  { title: '[FEATURE 2]', description: '[FEATURE 2 DESCRIPTION]' },
  { title: '[FEATURE 3]', description: '[FEATURE 3 DESCRIPTION]' },
];
---

<section id="features" class="features section">
  <div class="container">
    <div class="section-header">
      <h2>[FEATURES HEADLINE]</h2>
    </div>
    <div class="features-grid">
      {features.map((feature) => (
        <div class="feature-card">
          <h3>{feature.title}</h3>
          <p>{feature.description}</p>
        </div>
      ))}
    </div>
  </div>
</section>
`;

const testimonialsAstro = `---
// Testimonials Component
---

<section id="testimonials" class="section">
  <div class="container">
    <div class="section-header">
      <h2>[TESTIMONIALS HEADLINE]</h2>
    </div>
    <div class="testimonial">
      <blockquote>"[TESTIMONIAL QUOTE]"</blockquote>
      <cite>[NAME], [TITLE] at [COMPANY]</cite>
    </div>
  </div>
</section>
`;

const ctaAstro = `---
// CTA Component
---

<section id="cta" class="cta-section section">
  <div class="container">
    <h2>[CTA HEADLINE]</h2>
    <p>[CTA SUPPORTING TEXT]</p>
    <a href="#" class="btn btn-lg">[CTA BUTTON]</a>
  </div>
</section>
`;

const footerAstro = `---
// Footer Component
const year = new Date().getFullYear();
---

<footer class="footer">
  <div class="container">
    <p>&copy; {year} ${brief.projectName || 'Company'}. All rights reserved.</p>
  </div>
</footer>
`;

fs.writeFileSync(path.join(buildDir, 'src', 'components', 'Hero.astro'), heroAstro);
fs.writeFileSync(path.join(buildDir, 'src', 'components', 'Features.astro'), featuresAstro);
fs.writeFileSync(path.join(buildDir, 'src', 'components', 'Testimonials.astro'), testimonialsAstro);
fs.writeFileSync(path.join(buildDir, 'src', 'components', 'CTA.astro'), ctaAstro);
fs.writeFileSync(path.join(buildDir, 'src', 'components', 'Footer.astro'), footerAstro);
console.log('Created: src/components/*.astro');

console.log('\nAstro project generated successfully!');
console.log('Next steps:');
console.log('  cd build');
console.log('  npm install');
console.log('  npm run dev');
