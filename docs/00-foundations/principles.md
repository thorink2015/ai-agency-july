# Principles

**Purpose:** The design + engineering principles every page, component, and content decision must uphold — a short, checkable rulebook that turns brand values and quality standards into day-to-day defaults.
**Status:** v1 foundation — adjustable.

---

## How to use this

Each principle is a **name + why + a concrete implication**. When a decision is ambiguous, resolve it in the direction these principles point. If you break one, write down why. All numeric targets trace back to [Project Brief §8](./project-brief.md) and the systems docs.

---

### 1. Speed is a feature

The product is speed-to-lead; the site must feel as fast as the promise. A slow site contradicts the pitch.
**Implication:** Meet Core Web Vitals in the field — **LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1**, TTFB ≤ 0.8s, Lighthouse ≥ 95. Budgets: initial JS < 150 KB gz, LCP image < 150 KB, total initial transfer < 1 MB. `fetchpriority="high"` on the LCP image; preload critical fonts.

### 2. Accessible by default

WCAG 2.2 AA is the floor, not a retrofit. Accessibility is part of "premium-but-approachable."
**Implication:** Ship only WCAG-validated token pairings (see `tokens/design-tokens.json`). Every interactive element: visible `:focus-visible` ring (`--color-brand-600`, 3:1), name/role/state, keyboard operable. Touch targets **44px** with **8px** min spacing. Never white text on `--color-accent-500` (2.43:1 — fails).

### 3. Mobile-first

Google indexes the mobile version; most buyers arrive on phones. Design up from the small screen, not down from desktop.
**Implication:** Author base styles for narrow viewports; layer enhancements at breakpoints (sm 640 / md 768 / lg 1024 / xl 1280). Full content, headings, links, and schema must be present in the mobile HTML — no stripped-down mobile layout.

### 4. Content-first

Layout serves the message and the conversion, not the reverse. Structure content before styling it.
**Implication:** One clear `<h1>` per page; logical `h2/h3` hierarchy (never skip levels for looks). Prose measure ≤ 68ch, body line-height ≥ 1.5. Front-load the answer in each section so a single block is self-contained and skimmable.

### 5. Tokens over hardcoding

`tokens/design-tokens.json` is the single source of truth. Hardcoded values drift and break consistency and a11y guarantees.
**Implication:** Reference tokens by name (`--color-brand-600`, `--space-4`, `--radius-lg`), never raw hex/px in components. New value needed? Add a token, don't inline. The only files that may cite raw hex are the canonical colour/contrast docs.

### 6. Progressive enhancement

Core content and the primary CTA must work without JavaScript; JS enriches, it doesn't gate.
**Implication:** Server-render meaningful HTML. "Book a call" is a real link/form that works JS-off. Interactivity (chat widget, animations) layers on top and degrades gracefully.

### 7. Measure, don't guess

Opinions lose to data. We instrument the funnel and the field, then decide.
**Implication:** Track field CWV (CrUX/RUM), conversion to booked call, demo requests, branded search, and AI-answer citations. Ship changes as measurable hypotheses; use Search Console generative-AI reports and per-platform AI-visibility trackers. Shift KPIs toward citations/branded demand as clicks decline.

### 8. Motion with intent

Motion should feel responsive, not decorative, and never harm users who don't want it.
**Implication:** Durations 100–500ms, `ease-standard cubic-bezier(0.4,0,0.2,1)`. Gate **all** non-essential motion behind `@media (prefers-reduced-motion: no-preference)` with opacity/instant fallbacks. No motion that causes CLS.

### 9. Trust over hype

Every claim earns its place with proof; hype erodes the calm-confidence brand.
**Implication:** Pair each promise with a proof point (stat, testimonial, demo, guarantee). Use **one specific, cited figure per ~150–200 words**. Real author bylines and consistent NAP everywhere. No unbacked superlatives, no "revolutionary."

### 10. SEO & GEO are fundamentals, not add-ons

Good SEO *is* the AI-answer optimization. Google confirms AI Overviews/AI Mode run on core ranking; no special files or "AI-only" hacks are needed.
**Implication:** Titles ≤ 60 chars (keyword in first ~30), meta ≤ 155 chars, single H1, canonical, OG/Twitter cards, sitemap, robots.txt, JSON-LD. Earn off-site brand mentions (the ~3x stronger AI-visibility signal vs backlinks). **Don't** ship an `llms.txt` expecting ranking benefit or rely on schema to "multiply" citations — both are debunked (Google; Ahrefs 1,885-page test).

### 11. Consistency is the system

Reuse beats reinvention. One button, one card, one spacing rhythm — defined once.
**Implication:** Build from the token scale and shared components. Section rhythm on the `--space-*` scale (e.g. `--space-32`). Content max-width 1200px, gutter `clamp(1rem, 5vw, 2rem)`. If two things look almost the same, make them the same.

### 12. Ship images the right way

Images are the biggest CLS and payload risk; treat them as a budget line.
**Implication:** AVIF primary + WebP fallback, responsive `srcset`/`sizes`, **explicit `width`/`height`** (no CLS), lazy-load below the fold, `fetchpriority="high"` for the LCP image. Optimize SVG icons/logo. Subset fonts, `font-display: swap`, preload critical faces.

---

## Quick self-check (pre-merge)

- [ ] Meets CWV budgets (LCP/INP/CLS, JS/image/transfer)
- [ ] WCAG 2.2 AA: contrast, focus-visible, keyboard, 44px targets
- [ ] Mobile HTML has full content, headings, links, schema
- [ ] One H1; logical heading order; measure ≤ 68ch
- [ ] No hardcoded colours/spacing — tokens only
- [ ] Primary CTA works with JS disabled
- [ ] Non-essential motion gated behind `prefers-reduced-motion`
- [ ] Every claim has a nearby proof; ~1 cited stat / 150–200 words
- [ ] SEO essentials present; no `llms.txt`/schema myths relied on
- [ ] Images: AVIF+WebP, dimensions set, LCP prioritized

## Related

- [Project Brief](./project-brief.md)
- [Brand Strategy](./brand-strategy.md)
- [Design Tokens (JSON)](../../tokens/design-tokens.json)
- [Design System](../design-system/README.md)
- [Accessibility Standards](../accessibility/accessibility-standards.md)
- [Performance Budgets](../performance/performance-budget.md)
- [SEO System](../seo/seo-strategy.md)
- [AI / GEO SEO](../seo/ai-seo-geo.md)
- [Responsive Strategy](../responsive/responsive-standards.md)
