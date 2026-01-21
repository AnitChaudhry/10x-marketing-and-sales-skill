# SEO & Meta Tags Checklist

> **Used by**: Launch Agent
> **When**: Configuring SEO before deployment

---

## Primary Meta Tags

```html
<head>
  <!-- Character encoding -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Primary Meta Tags -->
  <title>{Value Prop} | {Brand Name}</title>
  <meta name="title" content="{Value Prop} | {Brand Name}">
  <meta name="description" content="{150-160 character description}">
  <meta name="keywords" content="{relevant, keywords, comma, separated}">
  <meta name="robots" content="index, follow">
  <meta name="language" content="English">
  <meta name="author" content="{Brand Name}">

  <!-- Canonical URL -->
  <link rel="canonical" href="{full-url}">
</head>
```

---

## Title Tag Guidelines

**Format**: `{Value Proposition} | {Brand Name}`

**Rules**:
- 50-60 characters maximum
- Include primary keyword
- Be compelling, not just descriptive
- Unique for each page

**Examples**:
```
✅ Track Time & Bill Clients Instantly | TimeTracker
✅ Free Marketing Masterclass + Templates | GrowthLab
❌ Home | My Company (too vague)
❌ The Best Project Management Software... (too long)
```

---

## Meta Description Guidelines

**Rules**:
- 150-160 characters
- Summarize the value proposition
- Include a call to action
- Use action words

**Examples**:
```
✅ "Join 10,000+ freelancers who track time and invoice clients in one click.
    Start your free trial today—no credit card required."

❌ "We are a company that makes software for tracking time."
```

---

## Open Graph (Facebook/LinkedIn)

```html
<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="{full-url}">
<meta property="og:title" content="{Compelling social title}">
<meta property="og:description" content="{Social-optimized description}">
<meta property="og:image" content="{og-image-url}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="{Brand Name}">
```

### OG Image Requirements
- Size: 1200 x 630 pixels
- Format: PNG or JPG
- File size: Under 1MB
- Include: Logo, headline, visual element

---

## Twitter Cards

```html
<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="{full-url}">
<meta name="twitter:title" content="{Twitter title - 70 chars max}">
<meta name="twitter:description" content="{Twitter description - 200 chars max}">
<meta name="twitter:image" content="{twitter-image-url}">
```

---

## Structured Data (JSON-LD)

### Organization Schema
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{Brand Name}",
  "url": "{Website URL}",
  "logo": "{Logo URL}",
  "description": "{Business description}",
  "sameAs": [
    "{Facebook URL}",
    "{Twitter URL}",
    "{LinkedIn URL}"
  ]
}
</script>
```

### Product Schema (if applicable)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{Product Name}",
  "description": "{Product description}",
  "brand": {
    "@type": "Brand",
    "name": "{Brand Name}"
  },
  "offers": {
    "@type": "Offer",
    "priceCurrency": "USD",
    "price": "{price}",
    "availability": "https://schema.org/InStock"
  }
}
</script>
```

### FAQ Schema (if FAQ section exists)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{Question 1}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{Answer 1}"
      }
    }
  ]
}
</script>
```

---

## Additional Files

### robots.txt
```
User-agent: *
Allow: /

Sitemap: {url}/sitemap.xml
```

### sitemap.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{full-url}</loc>
    <lastmod>{YYYY-MM-DD}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

---

## Performance SEO

- [ ] Page loads in under 3 seconds
- [ ] Images optimized and properly sized
- [ ] Fonts preloaded
- [ ] Critical CSS inlined (optional)
- [ ] JavaScript deferred
- [ ] Lazy loading for below-fold images

```html
<!-- Preload fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Lazy load images -->
<img src="image.jpg" loading="lazy" alt="Description">

<!-- Defer JavaScript -->
<script src="main.js" defer></script>
```

---

## SEO Checklist

### Before Launch
- [ ] Title tag set (50-60 chars)
- [ ] Meta description set (150-160 chars)
- [ ] Canonical URL configured
- [ ] OG tags configured
- [ ] Twitter cards configured
- [ ] OG image created (1200x630)
- [ ] Structured data added
- [ ] robots.txt created
- [ ] sitemap.xml created
- [ ] All images have alt text
- [ ] URLs are clean and descriptive
- [ ] Page loads under 3 seconds

### After Launch
- [ ] Submit to Google Search Console
- [ ] Submit sitemap
- [ ] Test social sharing (paste URL in Twitter/Facebook)
- [ ] Verify structured data (Google Rich Results Test)
- [ ] Monitor Core Web Vitals
