# Design Directions — Preview

> **Chosen direction: [01 Dispatch](./01-dispatch/index.html)** (owner decision, 2026-07-02). It has since been refined: demo button removed (no video exists), FAQ section + FAQPage JSON-LD added, per-plan pricing CTAs, icons, scroll/stat motion (reduced-motion safe), font-loading and anchor-scroll fixes. 02/03 remain as originally built, for reference.

Three genuinely distinct visual directions for the single-scroll landing page, built from the **same copy, word for word**. Open [`index.html`](./index.html) for the chooser, or open any direction directly. These are **standalone previews** — they do not use the `tokens/` brand system (the brief asked for full creative freedom), so they can be evaluated independently of the foundation on `main`.

| # | Direction | Mood | Palette | Type |
|---|---|---|---|---|
| 01 | [**Dispatch**](./01-dispatch/index.html) | Operations terminal — fast, precise, engineered | Near-black `#0B0C0E` + electric lime `#C5F82A` | Space Grotesk + JetBrains Mono |
| 02 | [**Storefront**](./02-storefront/index.html) | Warm editorial — a trusted local operator | Cream `#F6F1E7` + terracotta `#C4552F` + ink | Fraunces (serif) + Work Sans |
| 03 | [**Signal**](./03-signal/index.html) | Bold brutalist — decisive, high-contrast | Cobalt `#1F3BFF` + acid yellow `#E8FF3A` | Archivo/condensed display + Inter |

Each direction is a self-contained set: `index.html` (the full page, sections 1–11), `privacy.html`, and `terms.html` (placeholder legal pages).

## What's live vs. placeholder

- **Live (working):** the CTA funnel (every "See If Your Business Qualifies" → 4-question qualifying form → calendar/time picker → confirmation, all accessible modal dialogs), the Monthly/Yearly pricing toggle, mobile nav, and the "Watch a 90-second demo" lightbox.
- **Placeholder (swap later):** testimonials (names/quotes/logos, clearly marked), and the demo video (a 16:9 "coming soon" panel — no form).
- **Deliberately omitted:** the live AI chat demo widget (deferred by request; no placeholder left for it either).

## Notes

- Self-contained: inline CSS/JS, no build step, no external images (inline SVG only). Web fonts load from Google Fonts in the browser.
- Accessibility kept throughout: one `<h1>` per page, skip link, `:focus-visible`, labelled inputs, focus-trapped dialogs, `prefers-reduced-motion`, and WCAG-AA text contrast.
- Copy is identical across all three — only the visual design differs.
