/**
 * 10x Team Landing Page - HTML Generator
 *
 * Generates the base HTML structure from project specifications.
 *
 * Usage: node generate-html.js <project-name>
 */

const fs = require('fs');
const path = require('path');

const projectName = process.argv[2];

if (!projectName) {
  console.error('Usage: node generate-html.js <project-name>');
  process.exit(1);
}

const projectRoot = path.join(__dirname, '..', '..', '..', '..', 'projects', projectName);

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
    brand: {
      primary: '#2563eb',
      primaryLight: '#3b82f6',
      primaryDark: '#1d4ed8'
    },
    neutral: {
      background: '#ffffff',
      surface: '#f8fafc',
      border: '#e2e8f0',
      textPrimary: '#1e293b',
      textSecondary: '#64748b'
    }
  };
}

function getDefaultTypography() {
  return {
    fonts: {
      heading: 'Inter',
      body: 'Inter'
    },
    scale: {
      h1: 'clamp(2.5rem, 5vw, 4rem)',
      h2: 'clamp(2rem, 4vw, 3rem)',
      body: '1rem'
    }
  };
}

// Generate HTML template
const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="${brief.summary?.oneLiner || ''}">

    <title>${brief.projectName || 'Landing Page'}</title>

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=${typography.fonts.heading}:wght@400;500;600;700&family=${typography.fonts.body}:wght@400;500;600&display=swap" rel="stylesheet">

    <!-- Styles -->
    <link rel="stylesheet" href="css/styles.css">

    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
</head>
<body>
    <!-- Skip Link for Accessibility -->
    <a href="#main" class="skip-link">Skip to content</a>

    <!-- Navigation -->
    <nav class="nav" role="navigation">
        <div class="nav-container container">
            <a href="/" class="nav-logo">
                <span class="logo-text">${brief.projectName || 'Brand'}</span>
            </a>

            <button class="nav-toggle" aria-label="Menu" aria-expanded="false">
                <span class="nav-toggle-icon"></span>
            </button>

            <div class="nav-menu">
                <ul class="nav-links">
                    <li><a href="#features">Features</a></li>
                    <li><a href="#testimonials">Testimonials</a></li>
                    <li><a href="#pricing">Pricing</a></li>
                </ul>
                <a href="#cta" class="btn btn-primary nav-cta">Get Started</a>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main id="main">
        <!-- Hero Section -->
        <header class="hero">
            <div class="hero-container container">
                <div class="hero-content">
                    <h1 class="hero-title">[HEADLINE GOES HERE]</h1>
                    <p class="hero-subtitle">[SUBHEAD GOES HERE]</p>
                    <div class="hero-cta">
                        <a href="#" class="btn btn-primary btn-lg">[PRIMARY CTA]</a>
                        <a href="#" class="btn btn-secondary">[SECONDARY CTA]</a>
                    </div>
                    <div class="hero-proof">
                        [SOCIAL PROOF ELEMENT]
                    </div>
                </div>
                <div class="hero-visual">
                    <img src="assets/hero-image.png" alt="Product screenshot"
                         width="600" height="400" loading="eager">
                </div>
            </div>
        </header>

        <!-- Features Section -->
        <section class="features section" id="features">
            <div class="container">
                <div class="section-header">
                    <h2>[FEATURES HEADLINE]</h2>
                    <p class="section-subtitle">[FEATURES DESCRIPTION]</p>
                </div>
                <div class="features-grid">
                    <article class="feature-card animate-on-scroll">
                        <div class="feature-icon" aria-hidden="true">
                            <!-- Icon SVG -->
                        </div>
                        <h3 class="feature-title">[FEATURE 1]</h3>
                        <p class="feature-desc">[FEATURE 1 DESCRIPTION]</p>
                    </article>
                    <article class="feature-card animate-on-scroll">
                        <div class="feature-icon" aria-hidden="true">
                            <!-- Icon SVG -->
                        </div>
                        <h3 class="feature-title">[FEATURE 2]</h3>
                        <p class="feature-desc">[FEATURE 2 DESCRIPTION]</p>
                    </article>
                    <article class="feature-card animate-on-scroll">
                        <div class="feature-icon" aria-hidden="true">
                            <!-- Icon SVG -->
                        </div>
                        <h3 class="feature-title">[FEATURE 3]</h3>
                        <p class="feature-desc">[FEATURE 3 DESCRIPTION]</p>
                    </article>
                </div>
            </div>
        </section>

        <!-- Testimonials Section -->
        <section class="testimonials section" id="testimonials">
            <div class="container">
                <div class="section-header">
                    <h2>[TESTIMONIALS HEADLINE]</h2>
                </div>
                <div class="testimonials-grid">
                    <blockquote class="testimonial-card animate-on-scroll">
                        <p class="testimonial-quote">"[TESTIMONIAL QUOTE]"</p>
                        <footer class="testimonial-author">
                            <img src="assets/avatar-1.jpg" alt="" width="48" height="48"
                                 class="testimonial-avatar" loading="lazy">
                            <div>
                                <cite class="testimonial-name">[NAME]</cite>
                                <p class="testimonial-role">[TITLE], [COMPANY]</p>
                            </div>
                        </footer>
                    </blockquote>
                </div>
            </div>
        </section>

        <!-- Final CTA Section -->
        <section class="cta-section section" id="cta">
            <div class="container">
                <div class="cta-content">
                    <h2>[CTA HEADLINE]</h2>
                    <p>[CTA SUPPORTING TEXT]</p>
                    <a href="#" class="btn btn-primary btn-lg">[CTA BUTTON]</a>
                    <p class="cta-note">[REASSURANCE TEXT]</p>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <p>&copy; ${new Date().getFullYear()} ${brief.projectName || 'Company'}. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="js/main.js" defer></script>
</body>
</html>`;

// Write HTML file
const htmlPath = path.join(projectRoot, 'build', 'index.html');
fs.writeFileSync(htmlPath, html);
console.log(`Generated: ${htmlPath}`);

// Generate base CSS
const css = `/* 10x Team Landing Page - Generated Styles */

:root {
    /* Colors */
    --color-primary: ${colors.brand?.primary || '#2563eb'};
    --color-primary-light: ${colors.brand?.primaryLight || '#3b82f6'};
    --color-primary-dark: ${colors.brand?.primaryDark || '#1d4ed8'};

    --color-bg: ${colors.neutral?.background || '#ffffff'};
    --color-surface: ${colors.neutral?.surface || '#f8fafc'};
    --color-border: ${colors.neutral?.border || '#e2e8f0'};
    --color-text: ${colors.neutral?.textPrimary || '#1e293b'};
    --color-text-secondary: ${colors.neutral?.textSecondary || '#64748b'};

    /* Typography */
    --font-heading: '${typography.fonts?.heading || 'Inter'}', sans-serif;
    --font-body: '${typography.fonts?.body || 'Inter'}', sans-serif;

    --text-h1: ${typography.scale?.h1 || 'clamp(2.5rem, 5vw, 4rem)'};
    --text-h2: ${typography.scale?.h2 || 'clamp(2rem, 4vw, 3rem)'};
    --text-body: ${typography.scale?.body || '1rem'};

    /* Spacing */
    --space-xs: 0.5rem;
    --space-sm: 1rem;
    --space-md: 1.5rem;
    --space-lg: 2rem;
    --space-xl: 3rem;
    --space-2xl: 5rem;

    /* Layout */
    --max-width: 1200px;

    /* Effects */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 16px;
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
    --transition-fast: 150ms ease;
    --transition-base: 300ms ease;
}

/* Reset */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: var(--font-body);
    font-size: var(--text-body);
    line-height: 1.6;
    color: var(--color-text);
    background-color: var(--color-bg);
}

/* Container */
.container {
    width: 100%;
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 0 var(--space-md);
}

/* Section */
.section {
    padding: var(--space-2xl) 0;
}

.section-header {
    text-align: center;
    max-width: 700px;
    margin: 0 auto var(--space-xl);
}

/* Buttons */
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

.btn-secondary {
    background: transparent;
    color: var(--color-primary);
    border: 2px solid var(--color-primary);
}

.btn-lg {
    padding: var(--space-md) var(--space-xl);
    font-size: 1.125rem;
}

/* Skip Link */
.skip-link {
    position: absolute;
    top: -100%;
    left: var(--space-sm);
    padding: var(--space-sm);
    background: var(--color-primary);
    color: white;
    z-index: 100;
}

.skip-link:focus {
    top: var(--space-sm);
}

/* TODO: Add remaining styles from build-agent.md */
`;

const cssPath = path.join(projectRoot, 'build', 'css', 'styles.css');
fs.writeFileSync(cssPath, css);
console.log(`Generated: ${cssPath}`);

// Generate base JS
const js = `// 10x Team Landing Page - Generated JavaScript

// Mobile Navigation
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('.nav-menu');

navToggle?.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('active');
    navToggle.setAttribute('aria-expanded', isOpen);
});

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            navMenu?.classList.remove('active');
        }
    });
});

// Scroll Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.animate-on-scroll').forEach(el => {
    observer.observe(el);
});

console.log('10x Team Landing Page loaded');
`;

const jsPath = path.join(projectRoot, 'build', 'js', 'main.js');
fs.writeFileSync(jsPath, js);
console.log(`Generated: ${jsPath}`);

console.log('\\nBase files generated successfully!');
console.log('Next: Run copywriting and design phases to fill in content.');
