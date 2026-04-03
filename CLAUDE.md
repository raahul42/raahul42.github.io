# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio site hosted on GitHub Pages. Pure HTML, CSS, and vanilla JS — no build step, no dependencies beyond CDN-loaded fonts and icons. Changes pushed to main deploy automatically.

## Running Locally

```bash
python3 -m http.server 8765
# Visit http://localhost:8765
```

## Architecture

Single-directory static site. Three pages: `index.html` (main portfolio), `now/index.html` (what I'm doing now), `privacy/index.html` (privacy tools stack). Base styling lives in `style.css`, but `retro.css` (loaded after) overrides most of it with the ink-and-paper aesthetic. When working on visual/theme changes, `retro.css` is the primary file — there's no need to read all of `style.css` each time.

**Theme system:** Dual dark/light mode using CSS custom properties (`--bg`, `--accent`, etc.), toggled via JS and persisted in `localStorage`.

**Key interactive features in `index.html`:**
- Typewriter effect cycling through roles in the hero
- Scroll reveal animations
- Hamburger nav for mobile (breakpoint: 700px)
- Animated mesh background (3 floating orbs via CSS keyframes)

**Analytics:** GoatCounter (privacy-friendly, no cookies, loaded via CDN script tag).

## UI/Styling Conventions

- Keep inline text on the same line unless explicitly asked to break it. Do not move text to new lines without being asked.
- After making UI changes, verify: z-index stacking is correct, colors have sufficient contrast/opacity, font sizes are consistent across similar elements.
- Mobile breakpoint is 700px. Use `clamp()` for fluid typography.

## Code Structure

| File/Folder | Contents |
|---|---|
| `index.html` | Main portfolio page with all sections and embedded JS |
| `style.css` | Base styles, layout, and dark-mode defaults — largely overridden by `retro.css` |
| `retro.css` | Ink-and-paper theme overrides; primary file for any visual/UI changes |
| `now/index.html` | "Now" page (reading, watching, fascinations) |
| `privacy/index.html` | Privacy tools stack page |
| `images/` | Static image assets |
| `.claude/` | Claude Code launch config (runs python3 HTTP server on port 8765) |
