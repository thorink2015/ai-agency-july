# Responsive Standards

**Purpose:** The mobile-first responsive contract for the whole site — the breakpoint set and what each targets, the 320px floor, fluid type/space, responsive images, touch-vs-pointer rules, a device/orientation/viewport test matrix, safe-area/notch handling, sticky elements, the mobile-nav pattern, tap-highlight, horizontal-scroll prevention, and a copy-paste testing checklist — so any developer or future Claude session ships layouts that hold from 320px to ultra-wide without regressions.
**Status:** v1 foundation — adjustable.

---

> **All values here reference [design tokens](../design-system/design-tokens.md) by name** (`--gutter`, `--space-4`, `--target-min`). Raw numbers appear only to explain the _reasoning_ behind a token, or where the platform requires a literal (media-query widths, `env()` insets — these cannot be CSS custom properties).
>
> This doc is a **systems/standards** doc. It defines the rules for how layouts adapt. It is **not** website copy, **not** a page build, and **not** component-by-component styling (that lives in the component library and [layout & grid](../design-system/layout-and-grid.md)).

---

## 0. TL;DR — the responsive rules

- [ ] **Mobile-first.** Author base styles for the smallest screen; add complexity upward with `min-width` media queries only.
- [ ] **Support 320px → ∞.** 320 CSS px is the hard floor (WCAG 1.4.10 Reflow). Nothing may require horizontal scrolling at 320px or at 400% zoom.
- [ ] **Five breakpoints, mobile-up:** `sm` 640 · `md` 768 · `lg` 1024 · `xl` 1280 · `2xl` 1536. Layout collapses to **1 column below `md` (768px)**.
- [ ] **Fluid type & space** via `clamp()` for anything that should scale continuously (h1–h3, lead, gutters). Fixed steps for everything else.
- [ ] **Touch targets ≥ 44×44 CSS px** (`--target-min`), ≥ 8px apart (`--target-spacing`). WCAG floor is 24px; we hold 44 for comfort + mobile HIG.
- [ ] **No hover-only interactions.** Anything reachable by hover must also work on tap and keyboard focus.
- [ ] **Respect the notch.** Add `env(safe-area-inset-*)` to fixed/edge/full-bleed elements.
- [ ] **No horizontal scroll, ever.** Enforce with the guardrails in §11 and test at 320/360/390px.
- [ ] **One mobile-nav pattern** (§9): accessible toggle → off-canvas panel, focus-trapped, `Esc`/backdrop closes, body scroll-locked.
- [ ] **Test the matrix** (§6) in DevTools device mode + at least one real iOS and one real Android device before launch.

---

## 1. Mobile-first principle

Author the **smallest layout first**, then progressively enhance upward. This keeps the base CSS small and fast (the payload phones download is the minimal one), and it prevents the classic bug where desktop styles leak down and get un-done by overrides.

**Rules:**

- Base (no media query) = the **320–639px** experience: single column, stacked, full-width controls.
- Enhance **up** with `min-width` only. Do **not** author `max-width` breakpoints as the primary strategy — they invert the cascade and multiply overrides.
- Each breakpoint should **add** capability (more columns, more whitespace, hover affordances), never rebuild the layout from scratch.

```css
/* ✅ Mobile-first: base is smallest, min-width adds up */
.card-grid { display: grid; gap: var(--space-4); grid-template-columns: 1fr; }
@media (min-width: 768px)  { .card-grid { grid-template-columns: repeat(2, 1fr); gap: var(--space-6); } }
@media (min-width: 1024px) { .card-grid { grid-template-columns: repeat(3, 1fr); } }

/* ❌ Desktop-first: forces you to undo things on small screens */
/* .card-grid { grid-template-columns: repeat(3,1fr); }
   @media (max-width: 1023px){ .card-grid { grid-template-columns: repeat(2,1fr); } } */
```

> **Prefer intrinsic responsiveness over breakpoints where possible.** `grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr))` and `flex-wrap` adapt with zero media queries and no fixed thresholds. Reach for a breakpoint only when the content genuinely needs a different structure.

---

## 2. Breakpoints — the set and what each targets

Five `min-width` breakpoints, matching the `--breakpoint-*` tokens. These are **layout thresholds, not device names** — never assume "tablet" or "iPhone"; assume "≥ this many CSS pixels."

| Token | Value | Media query | Primarily targets | What typically changes here |
|---|---|---|---|---|
| _(base)_ | 320–639px | — (no query) | Phones, portrait | Single column, stacked nav → hamburger, full-width CTAs, edge gutters |
| `sm` | **640px** | `@media (min-width: 640px)` | Large phones landscape / small tablets | Slightly wider gutters, 2-up for small cards, side-by-side form fields |
| `md` | **768px** | `@media (min-width: 768px)` | Tablet **portrait** | **Multi-column grids turn on**, nav can go inline, hero becomes 2-col |
| `lg` | **1024px** | `@media (min-width: 1024px)` | Tablet landscape / small laptops | Full desktop nav, 3-col feature grids, sidebars, hover affordances |
| `xl` | **1280px** | `@media (min-width: 1280px)` | Desktop | Content hits `1200px` max; extra whitespace, larger display type |
| `2xl` | **1536px** | `@media (min-width: 1536px)` | Large desktop / wide monitors | Optional `wide` (1440px) container for immersive sections; caps growth |

**The one hard rule:** the multi-column → single-column collapse happens at **`md` (768px)**. Below `md`, assume one column.

**Do not** add ad-hoc breakpoints (e.g. `@media (min-width: 900px)`) to patch one component. If a component breaks between two tokens, fix it with intrinsic layout (§1) or fluid sizing (§3), not a new global threshold.

```css
/* Standard breakpoint ladder — copy verbatim */
/* base: 320–639  */
@media (min-width: 640px)  { /* sm  */ }
@media (min-width: 768px)  { /* md  */ }
@media (min-width: 1024px) { /* lg  */ }
@media (min-width: 1280px) { /* xl  */ }
@media (min-width: 1536px) { /* 2xl */ }
```

> Breakpoints are **not** exposed as CSS custom properties, because custom properties cannot be used inside a media-query condition. Keep the literal px values above as the single source; they mirror `tokens/design-tokens.json → breakpoint`.

---

## 3. The 320px floor + fluid type & space

### Minimum supported width: 320px

320 CSS px is the **hard floor** — it satisfies WCAG 2.2 **1.4.10 Reflow** (content must reflow to a 320px viewport with no two-dimensional scrolling) and covers the smallest still-common devices (e.g. iPhone SE 1st-gen, 320×568). Everything must be usable and scroll-free at 320px wide **and** at 400% browser zoom (which reflows a 1280px window down to ~320 effective px).

- Never set a `min-width` on a top-level layout wrapper that exceeds 320px.
- Never rely on a fixed pixel width for a full-width region.
- The viewport meta tag is mandatory and must **not** disable zoom:

```html
<!-- Required. Never add maximum-scale=1 or user-scalable=no — that breaks pinch-zoom (WCAG 1.4.4). -->
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
```

`viewport-fit=cover` is what makes the `env(safe-area-inset-*)` values (§7) available on notched devices.

### Fluid type via `clamp()`

Use the fluid tokens for headings and lead text so they scale **continuously** between the 320px floor and the top breakpoint — no jarring jumps at each media query. `clamp(MIN, PREFERRED, MAX)`: `MIN` protects small screens, `MAX` caps large ones, the `vw`-based `PREFERRED` interpolates between.

| Token | Value | Use for |
|---|---|---|
| `--fluid-h1` | `clamp(2.25rem, 1.4rem + 4.25vw, 4.5rem)` | Page/hero H1 |
| `--fluid-h2` | `clamp(1.875rem, 1.3rem + 2.9vw, 3rem)` | Section H2 |
| `--fluid-h3` | `clamp(1.5rem, 1.2rem + 1.5vw, 2.25rem)` | Subsection H3 |
| `--fluid-lead` | `clamp(1.125rem, 1.05rem + 0.4vw, 1.375rem)` | Hero/intro lead paragraph |

```css
h1 { font-size: var(--fluid-h1); line-height: var(--line-height-tight); }
.lead { font-size: var(--fluid-lead); line-height: var(--line-height-normal); }
```

**Body copy stays fixed at `--font-size-base` (16px).** Never fluid-scale body text — it hurts the reading measure and can dip below 16px on small screens. Keep body `line-height ≥ 1.5` (`--line-height-normal`) everywhere, and cap reading width at `--measure-prose` (68ch).

> **Accessibility rule for `clamp()`:** always express `MIN`/`MAX` in `rem`, never `px`, so text still honours the user's browser font-size and can resize to 200% (WCAG 1.4.4). The `vw` term alone would ignore zoom; `clamp` with rem bounds fixes that.

### Fluid space

- Page side padding uses `--gutter` = `clamp(1rem, 5vw, 2rem)` — tighter on phones, roomier on desktop, one variable everywhere.
- For section rhythm, prefer the fixed step scale (`--space-16 / 20 / 24 / 32`) chosen per breakpoint; reserve fluid space for gutters and hero padding where continuous scaling reads better.

---

## 4. Responsive images

Images are the biggest CLS and payload risk on mobile. Every content/hero image must ship responsive sources, explicit dimensions, and correct loading priority. (Full format/budget rules live in the imagery + performance docs; this is the responsive contract.)

**Non-negotiables:**

- [ ] **Always set `width` + `height`** (or CSS `aspect-ratio`) so the browser reserves space → zero layout shift (CLS).
- [ ] **`srcset` + `sizes`** so each viewport downloads an appropriately sized file — never a 2000px hero on a 360px phone.
- [ ] **AVIF first, WebP fallback**, via `<picture>`.
- [ ] **LCP image (hero): `fetchpriority="high"`, `loading="eager"`, and preload it.** Never lazy-load the LCP image.
- [ ] **Below-the-fold images: `loading="lazy"` + `decoding="async"`.**
- [ ] Hero/LCP image budget **< 200 KB**; content images **< 100 KB**.

```html
<!-- Hero / LCP image: eager, high priority, never lazy -->
<picture>
  <source type="image/avif" srcset="/img/hero-640.avif 640w, /img/hero-1024.avif 1024w, /img/hero-1600.avif 1600w" sizes="(min-width: 1024px) 50vw, 100vw">
  <source type="image/webp" srcset="/img/hero-640.webp 640w, /img/hero-1024.webp 1024w, /img/hero-1600.webp 1600w" sizes="(min-width: 1024px) 50vw, 100vw">
  <img src="/img/hero-1024.webp" width="1600" height="900" alt="Descriptive alt text"
       fetchpriority="high" loading="eager" decoding="async">
</picture>

<!-- Below-the-fold image: lazy -->
<img src="/img/feature.webp" srcset="/img/feature-480.webp 480w, /img/feature-960.webp 960w"
     sizes="(min-width: 768px) 33vw, 100vw" width="960" height="720" alt="…"
     loading="lazy" decoding="async">
```

**`sizes` is the part people get wrong.** It tells the browser the image's *rendered* width at each breakpoint so it can pick the right `srcset` entry **before** layout. Match it to how the image actually renders (e.g. full-width on mobile, one-third column on `md+`). A wrong `sizes` silently ships oversized images.

Make decorative/background images responsive too, and always give `<img>` a `max-width: 100%; height: auto;` base so nothing overflows its container (a common horizontal-scroll cause — see §11).

```css
img, svg, video, canvas { max-width: 100%; height: auto; display: block; }
```

---

## 5. Touch vs pointer

Phones and tablets are **touch** (coarse pointer, no true hover); laptops/desktops are **mouse** (fine pointer, hover). Many devices are both (touch laptop, tablet + trackpad). Design for touch by default and treat hover as an enhancement.

### Target size & spacing

- **Comfortable target: 44×44 CSS px** (`--target-min`) for every interactive element — buttons, links-as-buttons, nav items, form controls, icon buttons.
- **WCAG 2.2 floor (2.5.8, AA) is 24×24 CSS px**, or a spacing exception (a 24px-diameter circle centred on each target must not intersect a neighbour's). We hold **44** because it also satisfies mobile HIG and the AAA 2.5.5 target.
- **≥ 8px** (`--target-spacing`) between adjacent targets so fingers don't hit the wrong one.
- Inline text links inside a sentence are exempt from the size rule, but stack list/nav links with enough vertical padding to reach 44px.

```css
.btn, .nav__link, .icon-btn {
  min-height: var(--target-min);   /* 44px */
  min-width:  var(--target-min);
  /* pad small labels/icons out to the full target box */
  display: inline-flex; align-items: center; justify-content: center;
}
```

### Detect capability, don't guess by width

Use interaction media queries, not viewport width, to decide whether hover/fine-pointer affordances are safe:

```css
/* Only attach hover styles where hover truly exists */
@media (hover: hover) and (pointer: fine) {
  .card:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); }
}
/* Coarse pointer (touch): make targets bigger, skip hover reveals */
@media (pointer: coarse) {
  .icon-btn { min-height: var(--target-min); min-width: var(--target-min); }
}
```

### Hover-only pitfalls (do not ship these)

| Pitfall | Why it breaks on touch | Fix |
|---|---|---|
| Dropdown/menu that opens only on `:hover` | Touch users can't hover; menu never opens | Open on **tap/click** (toggle) and keyboard focus; use `:focus-within` too |
| Content revealed only on hover (tooltips, "hover to see price") | Invisible on touch and to keyboard users | Make content always visible, or reveal on tap/focus |
| Critical action shown only on row hover (e.g. "Delete" appears on hover) | Unreachable on touch | Always render the control, or provide a persistent affordance |
| Hover-triggered animation as the only feedback | No feedback on tap | Provide an active/pressed state for `:active` and touch |

**Also:** never rely on precise drag as the only way to do something. WCAG 2.2 **2.5.7 Dragging Movements (AA)** requires a single-pointer, non-drag alternative for any drag interaction (sliders need tap-to-position or +/− buttons; sortable lists need "move up/down").

---

## 6. Device / orientation / viewport test matrix

Test **layout thresholds and real devices**, not a checklist of phone model names. The viewport sizes below are representative anchors — hit each band, then verify the two orientations and the extremes.

### Viewport size anchors (CSS px, portrait width)

| Band | Test widths | Represents | Must verify |
|---|---|---|---|
| **Floor** | **320**, 360 | Smallest phones (SE), reflow floor | No h-scroll; all text/targets usable; nav → hamburger |
| **Common phone** | 375, **390**, 414, 430 | iPhone 12–15 / Pro Max, most Androids | Base layout, single column, sticky header + safe area |
| **Large phone / small tablet** | 640, 700 | `sm` band | 2-up small cards; forms side-by-side |
| **Tablet portrait** | **768**, 820 | iPad portrait, `md` | Multi-column turns on; nav decision point |
| **Tablet landscape / laptop** | **1024**, 1180, 1280 | iPad landscape, laptops, `lg`/`xl` | Desktop nav, 3-col grids, hover affordances |
| **Desktop** | 1440, **1536**, 1920 | Monitors, `2xl` | Content caps at 1200px; no over-stretch; whitespace holds |

### Orientation

| Orientation | Check |
|---|---|
| **Portrait** (default) | Everything above. Sticky header + bottom safe area. |
| **Landscape phone** (e.g. 844×390) | Short viewport height: hero doesn't push content off-screen; modals/sheets scroll internally; on-screen keyboard doesn't cover the focused input; `100dvh` used instead of `100vh` (§8). |
| **Landscape ↔ portrait rotate** | No layout lock; content reflows; no lost scroll position or trapped modal. |

### Test surfaces

- [ ] **Chrome/Edge DevTools device mode** — sweep the responsive ruler slowly from **320 → 1920**, watching for overflow, overlap, and clipped text. Toggle a device preset (iPhone SE, iPhone 14 Pro, iPad, Pixel) and rotate each.
- [ ] **DevTools throttling** — set "Mobile" CPU (4–6× slowdown) + "Slow 4G" to feel real phone performance and INP.
- [ ] **DevTools rendering** — enable **"Emulate CSS `prefers-reduced-motion`"** and check reduced-motion fallbacks.
- [ ] **Real iOS device (Safari)** — the only reliable check for the notch/home-indicator safe areas, `100dvh`/dynamic toolbar behaviour, tap-highlight, momentum scroll, and iOS input-zoom (see §11). Emulators do **not** reproduce these faithfully.
- [ ] **Real Android device (Chrome)** — check the URL-bar collapse resizing the viewport, back-gesture edges, and font rendering.
- [ ] **Keyboard-only pass at 320px and 400% zoom** — tab through everything; confirm visible focus and no obscured focus (§9, §7).

> **DevTools device mode is necessary but not sufficient.** It cannot reproduce safe areas, dynamic browser chrome, touch-callout, momentum scrolling, or iOS input-zoom. Always finish on at least one real iPhone and one real Android before launch.

---

## 7. Safe areas / notch

Notches, rounded corners, and the home indicator carve out zones where content can be clipped or untappable. With `viewport-fit=cover` (§3) set, the browser exposes four `env()` insets. Apply them to anything that touches a screen edge.

```css
:root {
  /* fall back to 0 on non-notched devices */
  --safe-top:    env(safe-area-inset-top, 0px);
  --safe-right:  env(safe-area-inset-right, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left:   env(safe-area-inset-left, 0px);
}

/* Fixed header: keep it clear of the notch */
.site-header {
  padding-top: max(var(--space-3), var(--safe-top));
  padding-inline: max(var(--gutter), var(--safe-left), var(--safe-right));
}

/* Fixed bottom bar / mobile CTA: clear the home indicator */
.mobile-cta-bar {
  padding-bottom: max(var(--space-3), var(--safe-bottom));
}

/* Full-bleed dark section that runs edge-to-edge in landscape */
.section--bleed {
  padding-inline: max(var(--gutter), var(--safe-left), var(--safe-right));
}
```

**Apply safe-area insets to:** the sticky/fixed header, any fixed bottom bar or mobile CTA, off-canvas nav panels, full-screen modals/sheets, and any full-bleed edge-to-edge section (especially in landscape, where left/right insets are non-zero).

Use `max()` so the inset never *reduces* your normal padding — it only pushes content further in when a notch demands it.

---

## 8. Sticky & fixed elements

Sticky headers, floating CTAs, and chat widgets are useful but cause three recurring responsive bugs: they eat vertical space on short landscape viewports, they cover anchored content, and they can obscure the keyboard-focused element (a WCAG 2.2 failure).

**Rules:**

- **Sticky header** sits at `--z-sticky` (1100), ~64–72px tall, and every in-page anchor target must carry `scroll-margin-top` equal to header height so jumps don't hide the heading behind it:

  ```css
  :target, [id] { scroll-margin-top: calc(72px + var(--safe-top)); }
  ```

- **Use `dvh`, not `vh`, for full-height regions.** Mobile browser chrome (URL bar) grows/shrinks; `100vh` overshoots and causes clipping/jump. `100dvh` tracks the *dynamic* viewport. Provide a `vh` fallback for old engines:

  ```css
  .hero--full { min-height: 100vh; min-height: 100dvh; }
  ```

- **Focus must never be obscured (WCAG 2.2 — 2.4.11 Focus Not Obscured, AA).** A sticky header, cookie banner, or chat widget must not fully cover a focused input/link when tabbing. Fix with `scroll-margin-top` (above) and by keeping overlays from overlapping the focus scroll position.
- **Auto-updating/moving sticky content** (tickers, auto-advancing banners lasting > 5s) needs a pause/stop control (WCAG 2.2.2).
- The **live-chat / AI-assistant launcher** is fixed bottom-right; give it `--z-sticky`-band z-index, keep it clear of the bottom safe area, and ensure it does not overlap primary CTAs or the mobile nav toggle at 320px.

---

## 9. Mobile navigation pattern

One canonical pattern site-wide. Below `md` (768px) the primary nav collapses to a hamburger toggle that opens an off-canvas panel.

**Anatomy:**

1. **Toggle button** — a real `<button>` (44×44 target), with `aria-expanded` and `aria-controls` pointing at the panel, and an accessible name ("Open menu" / "Close menu"). Not a bare `<div>`.
2. **Panel** — off-canvas (slide from right/top) or full-screen overlay, above the header in z-order.
3. **Backdrop** — dim scrim; clicking it closes the menu.

**Behaviour requirements:**

- [ ] Opens on tap **and** is fully keyboard operable.
- [ ] **Focus moves into the panel** on open; **focus is trapped** inside while open; on close, focus **returns to the toggle**.
- [ ] **`Esc` closes** it; clicking the backdrop closes it.
- [ ] **Body scroll is locked** while open (prevent background scroll), and restored on close.
- [ ] Nav links are stacked, each ≥ 44px tall, ≥ 8px apart.
- [ ] The panel respects safe-area insets (§7) top and bottom.
- [ ] `aria-expanded` toggles `true`/`false` on the button; the panel is `hidden`/`inert` when closed so it's out of the tab order.

```html
<button class="nav-toggle" aria-expanded="false" aria-controls="mobile-nav">
  <span class="sr-only">Menu</span>
  <svg aria-hidden="true" focusable="false"><!-- icon --></svg>
</button>

<nav id="mobile-nav" class="mobile-nav" aria-label="Primary" hidden>
  <ul>
    <li><a href="/how-it-works">How it works</a></li>
    <li><a href="/pricing">Pricing</a></li>
    <li><a class="btn btn--primary" href="/book">Book a demo</a></li>
  </ul>
</nav>
```

```css
@media (min-width: 768px) {
  .nav-toggle { display: none; }        /* inline desktop nav takes over at md+ */
  .mobile-nav { /* becomes the inline nav */ }
}
```

Animate the panel with a transform (cheap, 60fps) and gate it behind `prefers-reduced-motion` — reduced-motion users get an instant/opacity-only open.

---

## 10. Tap highlight & touch feedback

- **iOS/Android show a default grey tap flash** (`-webkit-tap-highlight-color`). Replace it with an intentional, on-brand feedback instead of leaving the default or removing feedback entirely:

  ```css
  html { -webkit-tap-highlight-color: transparent; } /* kill the default flash */
  /* …then provide a real pressed state so users still get feedback */
  .btn:active { transform: scale(0.98); background: var(--cta-bg-hover); }
  ```

- **Do not remove tap feedback without replacing it.** Users need confirmation the tap registered. Provide `:active` (touch) and `:focus-visible` (keyboard) states.
- **`touch-action`** — set `touch-action: manipulation` on tappable controls to remove the ~300ms double-tap-zoom delay and keep taps snappy:

  ```css
  .btn, .nav__link, a { touch-action: manipulation; }
  ```

- **`user-select: none`** on button labels/icons so a long-press-drag doesn't select text instead of pressing — but never on body copy or anything users may want to copy.
- **Callout menu:** `-webkit-touch-callout: none` on custom controls stops the iOS long-press context menu on links/images used as buttons. Leave it on for real content links.

---

## 11. Preventing horizontal scroll

Unintended horizontal overflow (the "content wider than the viewport" bug) is the single most common mobile defect. It's almost always one oversized child pushing the page wide. Prevent it structurally, then verify.

**Structural guardrails:**

- [ ] Media never overflows: `img, svg, video, canvas, iframe { max-width: 100%; }` (see §4).
- [ ] Never set a fixed `width` in px on a full-width block; use `%`, `fr`, `minmax()`, or `max-width`.
- [ ] Account for padding/border with `box-sizing: border-box` globally (`*, *::before, *::after { box-sizing: border-box; }`).
- [ ] Watch `100vw`: it **includes the scrollbar width** on desktop and can exceed the content box → overflow. Prefer `100%` or `100dvw`; if you must use `vw`, subtract the scrollbar.
- [ ] Long unbreakable strings (URLs, emails, tokens) need `overflow-wrap: anywhere` / `word-break: break-word` so they don't force width.
- [ ] Negative margins, absolute-positioned decoration, and off-canvas panels must not spill: clip with `overflow-x: clip` on their **container**, not on `<body>` globally (a global `overflow-x: hidden` masks the bug and breaks `position: sticky`).
- [ ] Grids/flex rows that could exceed the viewport use `min-width: 0` on flex/grid children (default `min-width: auto` refuses to shrink and causes overflow).
- [ ] Tables: wrap wide tables in a scroll container (`overflow-x: auto`) rather than letting the page scroll.

```css
*, *::before, *::after { box-sizing: border-box; }
img, svg, video, canvas, iframe { max-width: 100%; height: auto; }
.flex-child, .grid-child { min-width: 0; }              /* allow shrink */
.long-text { overflow-wrap: anywhere; }
.table-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; }
```

**iOS input-zoom note:** iOS Safari auto-zooms the page when you focus an input whose font-size is **< 16px**, which then leaves the page scrolled/zoomed. Keep all form inputs at **≥ 16px** (`--font-size-base`) to prevent it.

**Debugging overflow:** in DevTools console, `document.querySelectorAll('*').forEach(el=>{ if(el.scrollWidth>document.documentElement.clientWidth) console.log(el); })` — logs every element wider than the viewport. Or temporarily add `* { outline: 1px solid red; }` and find what crosses the right edge at 320px.

---

## 12. Do / Don't

| ✅ Do | ❌ Don't |
|---|---|
| Author base styles mobile-first; enhance up with `min-width` | Write desktop-first and undo it with `max-width` overrides |
| Support 320px and 400% zoom with zero horizontal scroll | Set a `min-width` > 320px on a layout wrapper |
| Use the five token breakpoints (640/768/1024/1280/1536) | Invent ad-hoc breakpoints (900, 1100) to patch one component |
| Prefer intrinsic layout (`auto-fit minmax`, `flex-wrap`) | Reach for a media query when the content could just wrap |
| Fluid type via `clamp()` with **rem** min/max bounds | Use `vw`-only sizing (ignores zoom → fails WCAG 1.4.4) |
| Keep body text fixed at 16px, `line-height ≥ 1.5` | Fluid-scale body copy or drop inputs below 16px |
| Make targets 44×44 with ≥ 8px spacing | Ship 24px icon buttons packed together |
| Gate hover behind `@media (hover:hover)`; provide tap+focus equivalents | Put menus, tooltips, or actions behind hover-only |
| Provide a non-drag alternative for sliders/reordering (2.5.7) | Require precise drag as the only way to do something |
| Set `width`+`height` (or `aspect-ratio`) on every image | Ship images without dimensions (CLS) |
| Give `srcset`+`sizes`; AVIF→WebP; LCP image eager+`fetchpriority=high` | Serve one giant image to every viewport, or lazy-load the LCP image |
| Add `env(safe-area-inset-*)` via `max()` to fixed/edge elements | Ignore the notch and clip content behind it |
| Use `100dvh` for full-height regions | Use `100vh` (overshoots with mobile browser chrome) |
| Keep `scroll-margin-top` on anchors so focus/jumps clear the sticky header (2.4.11) | Let a sticky header / cookie banner / chat widget cover the focused element |
| One accessible mobile-nav pattern: toggle, focus-trap, `Esc`, scroll-lock | Hamburger that's a `<div>`, no focus trap, background scrolls |
| Replace the tap-highlight with an intentional `:active` state; `touch-action: manipulation` | Strip tap feedback entirely, leaving no confirmation |
| Test the full matrix + real iOS & Android before launch | Trust DevTools device mode alone (no safe areas, no input-zoom) |
| Set `box-sizing: border-box` and `min-width:0` on flex/grid children | Hide overflow with global `body { overflow-x: hidden }` and call it fixed |

---

## 13. Pre-launch responsive testing checklist

**Widths & reflow**
- [ ] Sweep DevTools ruler 320 → 1920; no horizontal scroll, no overlap, no clipped text at any width.
- [ ] Usable at **320px** and at **400% zoom** (WCAG 1.4.10 Reflow).
- [ ] No element wider than the viewport (run the overflow-finder snippet from §11).
- [ ] Text resizes to **200%** without loss (WCAG 1.4.4); inputs are ≥ 16px (no iOS input-zoom).

**Breakpoints**
- [ ] Layout collapses to 1 column below `md` (768px); grids come back correctly at md/lg.
- [ ] Only the five token breakpoints are used — no stray thresholds.

**Touch & pointer**
- [ ] All targets ≥ 44×44 with ≥ 8px spacing; verified on a real touch device.
- [ ] No hover-only menus/tooltips/actions; hover styles gated behind `@media (hover:hover)`.
- [ ] Any drag interaction has a non-drag alternative (2.5.7).

**Images**
- [ ] Every image has `width`+`height`/`aspect-ratio` (CLS = 0 from images).
- [ ] `srcset`+`sizes` correct; hero is eager + `fetchpriority="high"`, below-fold is lazy.

**Orientation & viewport**
- [ ] Portrait and landscape both pass, including short landscape phone (844×390).
- [ ] `100dvh` used for full-height regions; no jump on URL-bar collapse.
- [ ] Rotate mid-page: reflows cleanly, no trapped modal, scroll position sane.

**Safe areas & sticky**
- [ ] `viewport-fit=cover` set; `env(safe-area-inset-*)` applied to header, bottom bar, off-canvas, full-bleed sections — verified on a **real notched iPhone**.
- [ ] Sticky header clears anchors (`scroll-margin-top`); focus never obscured by header/banner/chat (2.4.11).

**Mobile nav**
- [ ] Toggle is a real button with `aria-expanded`/`aria-controls`; opens on tap and keyboard.
- [ ] Focus enters panel, is trapped, returns to toggle on close; `Esc` and backdrop close; body scroll locked.

**Feedback & motion**
- [ ] Intentional `:active`/`:focus-visible` states; `touch-action: manipulation` on controls.
- [ ] `prefers-reduced-motion` fallbacks verified (DevTools rendering emulation).

**Real devices**
- [ ] Passed on ≥ 1 real iPhone (Safari) and ≥ 1 real Android (Chrome).
- [ ] Checked with mobile CPU + Slow-4G throttling.

---

## Related

- [Layout & Grid](../design-system/layout-and-grid.md) — containers, 12-col grid, gutters, sticky header, section templates.
- [Design Tokens](../design-system/design-tokens.md) — the `--breakpoint-*`, `--gutter`, `--space-*`, `--fluid-*`, `--target-*` variables referenced here.
- [Motion](../design-system/motion.md) — durations, easings, and the `prefers-reduced-motion` contract.
- [Typography](../brand/typography.md) — type scale, fluid headings, reading measure.
- [Imagery](../brand/imagery.md) — image formats, art direction, and asset production specs.
