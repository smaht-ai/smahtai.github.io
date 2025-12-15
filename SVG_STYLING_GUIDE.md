# SVG Styling Guide for Blog Post Splash Images

This guide provides comprehensive styling alternatives and techniques for creating SVG splash images for blog posts. Use this reference when creating or modifying blog post splash images.

## Standard Template Structure

All blog post splash images should follow this structure:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <!-- Gradients, patterns, filters go here -->
  </defs>
  
  <!-- Background -->
  <rect width="800" height="600" fill="url(#gradientId)"/>
  
  <!-- Central Icon/Illustration (centered at x=400, y=200) -->
  <g transform="translate(400, 200)">
    <!-- Icon content here -->
  </g>
  
  <!-- Title (y=360) -->
  <text x="400" y="360" font-family="Arial, sans-serif" font-size="40" font-weight="bold"
        fill="white" text-anchor="middle">Post Title</text>
  
  <!-- Subtitle (y=400) -->
  <text x="400" y="400" font-family="Arial, sans-serif" font-size="22"
        fill="rgba(255,255,255,0.9)" text-anchor="middle">Post Subtitle</text>
</svg>
```

**Key Requirements:**
- Aspect ratio: 4:3 (800x600 viewBox)
- Icon centered at (400, 200)
- Title at y=360, font-size 40-42px, bold, white
- Subtitle at y=400, font-size 22px, rgba white 0.9 opacity

## Background Styling Alternatives

### 1. Gradient Variations

**Diagonal Gradient (Most Common)**
```svg
<linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#3B82F6;stop-opacity:1" />
  <stop offset="100%" style="stop-color:#10B981;stop-opacity:1" />
</linearGradient>
```

**Vertical Gradient**
```svg
<linearGradient id="grad" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" style="stop-color:#3B82F6"/>
  <stop offset="100%" style="stop-color:#10B981"/>
</linearGradient>
```

**Horizontal Gradient**
```svg
<linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" style="stop-color:#3B82F6"/>
  <stop offset="100%" style="stop-color:#10B981"/>
</linearGradient>
```

**Radial Gradient**
```svg
<radialGradient id="grad" cx="50%" cy="50%" r="50%">
  <stop offset="0%" style="stop-color:#3B82F6"/>
  <stop offset="100%" style="stop-color:#10B981"/>
</radialGradient>
```

**Multi-Stop Gradient (3+ Colors)**
```svg
<linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#3B82F6"/>
  <stop offset="50%" style="stop-color:#8B5CF6"/>
  <stop offset="100%" style="stop-color:#EC4899"/>
</linearGradient>
```

### 2. Pattern Backgrounds

**Dot Pattern**
```svg
<defs>
  <pattern id="dots" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
    <circle cx="20" cy="20" r="2" fill="rgba(255,255,255,0.1)"/>
  </pattern>
</defs>
<rect width="800" height="600" fill="url(#dots)"/>
```

**Grid Pattern**
```svg
<defs>
  <pattern id="grid" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  </pattern>
</defs>
<rect width="800" height="600" fill="url(#grid)"/>
```

### 3. Solid Color with Overlay
```svg
<rect width="800" height="600" fill="#1E40AF"/>
<rect width="800" height="600" fill="rgba(0,0,0,0.2)"/> <!-- Dark overlay -->
```

## Icon/Illustration Styling Alternatives

### 1. Flat Design
- Simple shapes with solid colors
- No shadows or gradients
- Bold outlines (stroke-width: 2-3)
- High contrast with background

### 2. Glassmorphism
```svg
<!-- Frosted glass effect -->
<rect x="-70" y="-60" width="140" height="160" rx="6" 
      fill="rgba(255,255,255,0.2)" stroke="white" stroke-width="3"/>
<rect x="-70" y="-60" width="140" height="160" rx="6" 
      fill="url(#glassGradient)" opacity="0.3"/>

<!-- Glass gradient definition -->
<linearGradient id="glassGradient" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" style="stop-color:rgba(255,255,255,0.4);stop-opacity:1" />
  <stop offset="100%" style="stop-color:rgba(255,255,255,0.1);stop-opacity:1" />
</linearGradient>
```

### 3. Neumorphism (Soft 3D)
```svg
<defs>
  <filter id="shadow">
    <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
    <feOffset dx="2" dy="2" result="offsetblur"/>
    <feComponentTransfer>
      <feFuncA type="linear" slope="0.3"/>
    </feComponentTransfer>
    <feMerge>
      <feMergeNode/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
</defs>
<rect filter="url(#shadow)"/>
```

### 4. Outline/Line Art
```svg
<!-- Minimal line-based icons -->
<path fill="none" stroke="white" stroke-width="3" 
      stroke-linecap="round" stroke-linejoin="round"/>
```

### 5. Isometric/3D
```svg
<!-- 3D perspective shapes -->
<polygon points="0,0 100,50 100,150 0,100" 
         fill="rgba(255,255,255,0.3)" 
         transform="skewX(-20)"/>
```

## Text Styling Alternatives

### 1. Text Effects

**Text Shadow**
```svg
<defs>
  <filter id="textShadow">
    <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
    <feOffset dx="2" dy="2"/>
  </filter>
</defs>
<text filter="url(#textShadow)" fill="white">Title</text>
```

**Gradient Text**
```svg
<defs>
  <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:#FFFFFF"/>
    <stop offset="100%" style="stop-color:#E0E7FF"/>
  </linearGradient>
</defs>
<text fill="url(#textGrad)">Title</text>
```

**Outlined Text**
```svg
<!-- Layered for outline effect -->
<text fill="none" stroke="white" stroke-width="2" x="400" y="360">Title</text>
<text fill="white" x="400" y="360">Title</text>
```

### 2. Typography Variations

**Font Families**
```svg
<!-- Serif -->
<text font-family="Georgia, serif">Title</text>

<!-- Monospace -->
<text font-family="'Courier New', monospace">Title</text>

<!-- Bold Sans-serif -->
<text font-family="'Arial Black', sans-serif">Title</text>
```

**Text Alignment**
```svg
<text text-anchor="start" x="50">Left Aligned</text>
<text text-anchor="middle" x="400">Center Aligned (default)</text>
<text text-anchor="end" x="750">Right Aligned</text>
```

### 3. Text Layout Variations

**Stacked Text**
```svg
<text x="400" y="360" font-size="48" font-weight="bold" fill="white" text-anchor="middle">Main Title</text>
<text x="400" y="400" font-size="24" fill="rgba(255,255,255,0.9)" text-anchor="middle">Subtitle Line 1</text>
<text x="400" y="430" font-size="24" fill="rgba(255,255,255,0.9)" text-anchor="middle">Subtitle Line 2</text>
```

## Visual Effects

### 1. Decorative Elements

**Particles/Dots**
```svg
<!-- Scattered decorative elements -->
<circle cx="100" cy="150" r="3" fill="rgba(255,255,255,0.3)"/>
<circle cx="250" cy="200" r="2" fill="rgba(255,255,255,0.2)"/>
<!-- Repeat with varied positions and sizes -->
```

**Geometric Shapes**
```svg
<!-- Triangles, hexagons, etc. as decorative elements -->
<polygon points="50,50 100,100 0,100" fill="rgba(255,255,255,0.1)"/>
```

### 2. Blur Effects
```svg
<defs>
  <filter id="blur">
    <feGaussianBlur stdDeviation="5"/>
  </filter>
</defs>
<circle filter="url(#blur)"/>
```

## Color Scheme Alternatives

### 1. Monochromatic
```svg
<!-- Single color with variations -->
<stop offset="0%" style="stop-color:#3B82F6"/>   <!-- Blue -->
<stop offset="100%" style="stop-color:#1E40AF"/> <!-- Darker blue -->
```

### 2. Complementary Colors
```svg
<!-- Opposite on color wheel -->
<stop offset="0%" style="stop-color:#3B82F6"/>  <!-- Blue -->
<stop offset="100%" style="stop-color:#F59E0B"/> <!-- Orange -->
```

### 3. Analogous Colors
```svg
<!-- Adjacent on color wheel -->
<stop offset="0%" style="stop-color:#3B82F6"/>   <!-- Blue -->
<stop offset="50%" style="stop-color:#8B5CF6"/>  <!-- Purple -->
<stop offset="100%" style="stop-color:#EC4899"/> <!-- Pink -->
```

### 4. Dark Mode Style
```svg
<!-- Dark background with light text -->
<rect width="800" height="600" fill="#1F2937"/> <!-- Dark gray -->
<text fill="#F9FAFB"/> <!-- Light text -->
```

## Popular Color Combinations

**Blue to Green** (Tech/Modern)
```svg
<stop offset="0%" style="stop-color:#3B82F6"/>
<stop offset="100%" style="stop-color:#10B981"/>
```

**Purple to Pink** (Creative/Design)
```svg
<stop offset="0%" style="stop-color:#8B5CF6"/>
<stop offset="100%" style="stop-color:#EC4899"/>
```

**Orange to Red** (Energy/Action)
```svg
<stop offset="0%" style="stop-color:#F59E0B"/>
<stop offset="100%" style="stop-color:#EF4444"/>
```

**Teal to Blue** (Professional)
```svg
<stop offset="0%" style="stop-color:#14B8A6"/>
<stop offset="100%" style="stop-color:#3B82F6"/>
```

## Layout Alternatives

### 1. Asymmetric Layout
```svg
<!-- Icon on left, text on right -->
<g transform="translate(200, 200)">Icon</g>
<text x="500" y="300">Title</text>
```

### 2. Split Layout
```svg
<!-- Two-tone background split -->
<rect x="0" y="0" width="400" height="600" fill="#3B82F6"/>
<rect x="400" y="0" width="400" height="600" fill="#10B981"/>
```

### 3. Full Bleed Icon
```svg
<!-- Icon extends to edges -->
<g transform="translate(400, 300)">
  <!-- Larger icon that goes to edges -->
</g>
```

## Style Combinations

### Minimalist
- **Background**: Solid color or subtle gradient
- **Icon**: Simple line art, no fills
- **Text**: Clean sans-serif, no effects

### Bold
- **Background**: High contrast gradient
- **Icon**: Geometric shapes, bold outlines
- **Text**: Outlined or with shadow, large size

### Elegant
- **Background**: Soft gradient (purple/pink)
- **Icon**: Glassmorphism effect
- **Text**: Serif font, gradient fill

### Modern
- **Background**: Multi-stop gradient
- **Icon**: Flat design with transparency
- **Text**: Sans-serif, clean

### Vintage
- **Background**: Warm colors (orange/brown)
- **Icon**: Textured patterns
- **Text**: Serif font, subtle shadow

## Best Practices

1. **Contrast**: Ensure text is always readable (white text on dark gradients works best)
2. **Simplicity**: Keep icons recognizable and simple (200px wide/tall max)
3. **Consistency**: Use similar styling across related blog posts
4. **Brand Colors**: Use brand colors when appropriate
5. **File Size**: Keep SVG optimized (remove unnecessary attributes)
6. **Accessibility**: Use semantic structure with `<g>` tags for grouping

## File Organization

- Blog splash images: `/assets/images/blog/*.svg`
- Use descriptive filenames: `topic-name.svg`
- Follow kebab-case naming convention

## Quick Reference Template

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#COLOR1;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#COLOR2;stop-opacity:1" />
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="800" height="600" fill="url(#grad)"/>

  <!-- Central Icon/Illustration -->
  <g transform="translate(400, 200)">
    <!-- Your icon/illustration here -->
    <!-- Keep it around 200px wide/tall, centered -->
  </g>

  <!-- Title -->
  <text x="400" y="360" font-family="Arial, sans-serif" font-size="40" font-weight="bold"
        fill="white" text-anchor="middle">Post Title</text>

  <!-- Subtitle -->
  <text x="400" y="400" font-family="Arial, sans-serif" font-size="22"
        fill="rgba(255,255,255,0.9)" text-anchor="middle">Post Subtitle or Description</text>
</svg>
```

