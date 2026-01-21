/**
 * 10x Team Landing Page - React (Vite) Generator
 *
 * Generates a React project with Vite from project specifications.
 *
 * Usage: node generate-react.js <project-name>
 */

const fs = require('fs');
const path = require('path');

const projectName = process.argv[2];

if (!projectName) {
  console.error('Usage: node generate-react.js <project-name>');
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

// Create React project structure
const dirs = [
  'src',
  'src/components',
  'src/assets',
  'public'
];

dirs.forEach(dir => {
  fs.mkdirSync(path.join(buildDir, dir), { recursive: true });
});

// package.json
const packageJson = {
  "name": projectName.toLowerCase().replace(/\s+/g, '-'),
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@vitejs/plugin-react": "^4.2.0",
    "vite": "^5.0.0"
  }
};

fs.writeFileSync(path.join(buildDir, 'package.json'), JSON.stringify(packageJson, null, 2));
console.log('Created: package.json');

// vite.config.js
const viteConfig = `import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})
`;

fs.writeFileSync(path.join(buildDir, 'vite.config.js'), viteConfig);
console.log('Created: vite.config.js');

// index.html
const indexHtml = `<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="${brief.summary?.oneLiner || ''}" />
    <title>${brief.projectName || 'Landing Page'}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=${typography.fonts.heading}:wght@400;500;600;700&family=${typography.fonts.body}:wght@400;500;600&display=swap" rel="stylesheet">
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
`;

fs.writeFileSync(path.join(buildDir, 'index.html'), indexHtml);
console.log('Created: index.html');

// src/main.jsx
const mainJsx = `import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
`;

fs.writeFileSync(path.join(buildDir, 'src', 'main.jsx'), mainJsx);
console.log('Created: src/main.jsx');

// src/App.jsx
const appJsx = `import Hero from './components/Hero'
import Features from './components/Features'
import Testimonials from './components/Testimonials'
import CTA from './components/CTA'
import Footer from './components/Footer'

function App() {
  return (
    <>
      <nav className="nav">
        <div className="nav-container container">
          <a href="/" className="nav-logo">${brief.projectName || 'Brand'}</a>
          <div className="nav-menu">
            <ul className="nav-links">
              <li><a href="#features">Features</a></li>
              <li><a href="#testimonials">Testimonials</a></li>
            </ul>
            <a href="#cta" className="btn btn-primary">Get Started</a>
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
    </>
  )
}

export default App
`;

fs.writeFileSync(path.join(buildDir, 'src', 'App.jsx'), appJsx);
console.log('Created: src/App.jsx');

// src/index.css
const indexCss = `/* 10x Team Landing Page - React Styles */

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
`;

fs.writeFileSync(path.join(buildDir, 'src', 'index.css'), indexCss);
console.log('Created: src/index.css');

// Components
const heroComponent = `export default function Hero() {
  return (
    <header className="hero section">
      <div className="container">
        <div className="hero-content" style={{ textAlign: 'center', maxWidth: '800px', margin: '0 auto' }}>
          <h1 style={{ fontSize: 'var(--text-h1)', marginBottom: 'var(--space-md)' }}>
            [HEADLINE GOES HERE]
          </h1>
          <p style={{ fontSize: '1.25rem', color: 'var(--color-text-secondary)', marginBottom: 'var(--space-lg)' }}>
            [SUBHEAD GOES HERE]
          </p>
          <div style={{ display: 'flex', gap: 'var(--space-sm)', justifyContent: 'center' }}>
            <a href="#cta" className="btn btn-primary btn-lg">[PRIMARY CTA]</a>
          </div>
        </div>
      </div>
    </header>
  )
}
`;

const featuresComponent = `export default function Features() {
  const features = [
    { title: '[FEATURE 1]', description: '[FEATURE 1 DESCRIPTION]' },
    { title: '[FEATURE 2]', description: '[FEATURE 2 DESCRIPTION]' },
    { title: '[FEATURE 3]', description: '[FEATURE 3 DESCRIPTION]' },
  ]

  return (
    <section id="features" className="section" style={{ background: 'var(--color-surface)' }}>
      <div className="container">
        <div className="section-header">
          <h2 style={{ fontSize: 'var(--text-h2)' }}>[FEATURES HEADLINE]</h2>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 'var(--space-lg)' }}>
          {features.map((feature, i) => (
            <div key={i} style={{ background: 'var(--color-bg)', padding: 'var(--space-lg)', borderRadius: 'var(--radius-md)', boxShadow: 'var(--shadow-md)' }}>
              <h3 style={{ marginBottom: 'var(--space-sm)' }}>{feature.title}</h3>
              <p style={{ color: 'var(--color-text-secondary)' }}>{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
`;

const testimonialsComponent = `export default function Testimonials() {
  return (
    <section id="testimonials" className="section">
      <div className="container">
        <div className="section-header">
          <h2 style={{ fontSize: 'var(--text-h2)' }}>[TESTIMONIALS HEADLINE]</h2>
        </div>
        <blockquote style={{ maxWidth: '600px', margin: '0 auto', textAlign: 'center' }}>
          <p style={{ fontSize: '1.25rem', fontStyle: 'italic', marginBottom: 'var(--space-md)' }}>
            "[TESTIMONIAL QUOTE]"
          </p>
          <footer style={{ color: 'var(--color-text-secondary)' }}>
            <cite>[NAME]</cite>, [TITLE] at [COMPANY]
          </footer>
        </blockquote>
      </div>
    </section>
  )
}
`;

const ctaComponent = `export default function CTA() {
  return (
    <section id="cta" className="section" style={{ background: 'var(--color-primary)', color: 'white', textAlign: 'center' }}>
      <div className="container">
        <h2 style={{ fontSize: 'var(--text-h2)', marginBottom: 'var(--space-md)' }}>[CTA HEADLINE]</h2>
        <p style={{ marginBottom: 'var(--space-lg)', opacity: 0.9 }}>[CTA SUPPORTING TEXT]</p>
        <a href="#" className="btn btn-lg" style={{ background: 'white', color: 'var(--color-primary)' }}>
          [CTA BUTTON]
        </a>
      </div>
    </section>
  )
}
`;

const footerComponent = `export default function Footer() {
  return (
    <footer style={{ padding: 'var(--space-lg) 0', borderTop: '1px solid var(--color-border)' }}>
      <div className="container" style={{ textAlign: 'center', color: 'var(--color-text-secondary)' }}>
        <p>&copy; ${new Date().getFullYear()} ${brief.projectName || 'Company'}. All rights reserved.</p>
      </div>
    </footer>
  )
}
`;

fs.writeFileSync(path.join(buildDir, 'src', 'components', 'Hero.jsx'), heroComponent);
fs.writeFileSync(path.join(buildDir, 'src', 'components', 'Features.jsx'), featuresComponent);
fs.writeFileSync(path.join(buildDir, 'src', 'components', 'Testimonials.jsx'), testimonialsComponent);
fs.writeFileSync(path.join(buildDir, 'src', 'components', 'CTA.jsx'), ctaComponent);
fs.writeFileSync(path.join(buildDir, 'src', 'components', 'Footer.jsx'), footerComponent);
console.log('Created: src/components/*.jsx');

console.log('\nReact (Vite) project generated successfully!');
console.log('Next steps:');
console.log('  cd build');
console.log('  npm install');
console.log('  npm run dev');
