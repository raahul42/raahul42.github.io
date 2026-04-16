# CLAUDE.md

File guides Claude Code (claude.ai/code) for this repo.

## Project Overview

Personal portfolio on GitHub Pages. Pure HTML, CSS, vanilla JS — no build, no deps beyond CDN fonts/icons. Push to main = auto-deploy.

## Running Locally

```bash
python3 -m http.server 8765
# Visit http://localhost:8765
```

## Architecture

Single-dir static site. Three pages: `index.html` (main portfolio), `now/index.html` (now page), `privacy/index.html` (privacy tools). Base styles in `style.css`, but `retro.css` (loaded after) overrides most with ink-and-paper aesthetic. Visual/theme work: `retro.css` primary — no need to read all of `style.css` each time.

**Theme system:** Dual dark/light via CSS custom properties (`--bg`, `--accent`, etc.), toggled via JS, persisted in `localStorage`.

**Key interactive features in `index.html`:**
- Typewriter effect cycling through roles in the hero
- Scroll reveal animations
- Hamburger nav for mobile (breakpoint: 700px)
- Animated mesh background (3 floating orbs via CSS keyframes)

**Analytics:** GoatCounter (privacy-friendly, no cookies, CDN script tag).

## UI/Styling Conventions

- Keep inline text same line unless asked to break. No new lines without request.
- After UI changes, verify: z-index stacking correct, colors sufficient contrast/opacity, font sizes consistent across similar elements.
- Mobile breakpoint 700px. Use `clamp()` for fluid typography.

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