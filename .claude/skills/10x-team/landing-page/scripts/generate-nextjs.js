/**
 * 10x Team Landing Page - Next.js Generator
 *
 * Generates a Next.js (App Router) project from project specifications.
 *
 * Usage: node generate-nextjs.js <project-name>
 */

const fs = require('fs');
const path = require('path');

const projectName = process.argv[2];

if (!projectName) {
  console.error('Usage: node generate-nextjs.js <project-name>');
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

// Create Next.js project structure
const dirs = [
  'app',
  'components',
  'public'
];

dirs.forEach(dir => {
  fs.mkdirSync(path.join(buildDir, dir), { recursive: true });
});

// package.json
const packageJson = {
  "name": projectName.toLowerCase().replace(/\s+/g, '-'),
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "eslint": "^8.0.0",
    "eslint-config-next": "^14.0.0"
  }
};

fs.writeFileSync(path.join(buildDir, 'package.json'), JSON.stringify(packageJson, null, 2));
console.log('Created: package.json');

// next.config.js
const nextConfig = `/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = nextConfig
`;

fs.writeFileSync(path.join(buildDir, 'next.config.js'), nextConfig);
console.log('Created: next.config.js');

// app/layout.js
const layoutJs = `import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: '${brief.projectName || 'Landing Page'}',
  description: '${brief.summary?.oneLiner || ''}',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
`;

fs.writeFileSync(path.join(buildDir, 'app', 'layout.js'), layoutJs);
console.log('Created: app/layout.js');

// app/globals.css
const globalsCss = `/* 10x Team Landing Page - Next.js Styles */

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
.hero { text-align: center; }
.hero-content { max-width: 800px; margin: 0 auto; }
.hero h1 { font-size: var(--text-h1); margin-bottom: var(--space-md); }
.hero-subtitle { font-size: 1.25rem; color: var(--color-text-secondary); margin-bottom: var(--space-lg); }

/* Features */
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

.feature-card h3 { margin-bottom: var(--space-sm); }
.feature-card p { color: var(--color-text-secondary); }

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

.testimonial cite { color: var(--color-text-secondary); }

/* CTA Section */
.cta-section {
  background: var(--color-primary);
  color: white;
  text-align: center;
}

.cta-section h2 { font-size: var(--text-h2); margin-bottom: var(--space-md); }
.cta-section p { margin-bottom: var(--space-lg); opacity: 0.9; }
.cta-section .btn { background: white; color: var(--color-primary); }

/* Footer */
.footer {
  padding: var(--space-lg) 0;
  border-top: 1px solid var(--color-border);
  text-align: center;
  color: var(--color-text-secondary);
}
`;

fs.writeFileSync(path.join(buildDir, 'app', 'globals.css'), globalsCss);
console.log('Created: app/globals.css');

// app/page.js
const pageJs = `import Hero from '../components/Hero'
import Features from '../components/Features'
import Testimonials from '../components/Testimonials'
import CTA from '../components/CTA'
import Footer from '../components/Footer'

export default function Home() {
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
`;

fs.writeFileSync(path.join(buildDir, 'app', 'page.js'), pageJs);
console.log('Created: app/page.js');

// Components
const heroComponent = `export default function Hero() {
  return (
    <header className="hero section">
      <div className="container">
        <div className="hero-content">
          <h1>[HEADLINE GOES HERE]</h1>
          <p className="hero-subtitle">[SUBHEAD GOES HERE]</p>
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
        <div className="features-grid">
          {features.map((feature, i) => (
            <div key={i} className="feature-card">
              <h3>{feature.title}</h3>
              <p>{feature.description}</p>
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
        <div className="testimonial">
          <blockquote>"[TESTIMONIAL QUOTE]"</blockquote>
          <cite>[NAME], [TITLE] at [COMPANY]</cite>
        </div>
      </div>
    </section>
  )
}
`;

const ctaComponent = `export default function CTA() {
  return (
    <section id="cta" className="cta-section section">
      <div className="container">
        <h2>[CTA HEADLINE]</h2>
        <p>[CTA SUPPORTING TEXT]</p>
        <a href="#" className="btn btn-lg">[CTA BUTTON]</a>
      </div>
    </section>
  )
}
`;

const footerComponent = `export default function Footer() {
  return (
    <footer className="footer">
      <div className="container">
        <p>&copy; ${new Date().getFullYear()} ${brief.projectName || 'Company'}. All rights reserved.</p>
      </div>
    </footer>
  )
}
`;

fs.writeFileSync(path.join(buildDir, 'components', 'Hero.jsx'), heroComponent);
fs.writeFileSync(path.join(buildDir, 'components', 'Features.jsx'), featuresComponent);
fs.writeFileSync(path.join(buildDir, 'components', 'Testimonials.jsx'), testimonialsComponent);
fs.writeFileSync(path.join(buildDir, 'components', 'CTA.jsx'), ctaComponent);
fs.writeFileSync(path.join(buildDir, 'components', 'Footer.jsx'), footerComponent);
console.log('Created: components/*.jsx');

console.log('\nNext.js project generated successfully!');
console.log('Next steps:');
console.log('  cd build');
console.log('  npm install');
console.log('  npm run dev');
