# Layout & Grid

**Purpose:** The site's layout system — container widths, responsive gutters, the 12-column grid, spacing rhythm and vertical section scale, structural specs for every common section template (hero, feature grid, logo strip, testimonial, FAQ, CTA band, footer), sticky-header behaviour, and safe-area handling — so any developer or future Claude session lays out pages consistently on top of the tokens.
**Status:** v1 foundation — adjustable.

---

> **All values here reference [design tokens](./design-tokens.md) by name** (`--container-content`, `--gutter`, `--space-24`). Do not hardcode px. Raw numbers appear only to explain the _reasoning_ behind a token.
>
> This doc is **structural** — it defines skeletons, regions, column counts, and spacing. It is **not** website copy and **not** component styling. Copy lives with content; component visuals live in the component library.

---

## 0. TL;DR — the layout rules

- [ ] **Three container widths:** `content` 1200px (default), `wide` 1440px (edge/immersive), `prose` 68ch (reading measure). Nothing wider.
- [ ] **One gutter, everywhere:** `--gutter` = `clamp(1rem, 5vw, 2rem)`. Every full-width section pads its inner container by this on the left and right.
- [ ] **12-column grid** for multi-column regions; collapse to 1 column below `md` (768px).
- [ ] **Vertical rhythm is a scale, not a guess:** section padding uses `--space-16 / 20 / 24 / 32`. Pick a tier per section weight; be consistent.
- [ ] **Sticky header** is `--z-sticky` (1100), ~64–72px tall, condenses on scroll, and every in-page anchor accounts for its height (`scroll-margin-top`).
- [ ] **Respect the notch:** add `env(safe-area-inset-*)` to fixed/edge elements and full-bleed dark sections.
- [ ] **No horizontal scroll, ever** — at any width down to 320px, at 200% zoom.

---

## 1. Containers

Three widths, each with a job. All are centred (`margin-inline: auto`) and padded by `--gutter`.

| Container | Token | Value | Use for |
|---|---|---|---|
| **Content** | `--container-content` | `1200px` | **Default.** Almost every section's inner width — hero, features, testimonials, CTA, footer. |
| **Wide** | `--container-wide` | `1440px` | Edge-to-edge/immersive layouts: full-bleed imagery, dashboards, wide logo walls. Use sparingly. |
| **Prose** | `--measure-prose` | `68ch` | Reading measure for long-form body copy (blog, legal, FAQ answers). Keeps lines 45–75ch. |

### The container pattern

A **full-bleed section** (background spans the viewport) wraps a **constrained inner container**:

```css
.section {                      /* full-bleed background */
  background: var(--bg-subtle);
}
.container {                    /* constrained, centred, gutter-padded */
  max-width: var(--container-content);
  margin-inline: auto;
  padding-inline: var(--gutter);
}
.container--wide  { max-width: var(--container-wide); }
.container--prose { max-width: var(--measure-prose); }
```

```html
<section class="section">
  <div class="container"><!-- content --></div>
</section>
```

**Rules:**
- [ ] Backgrounds (colour, image) go on the **full-bleed** element; content sits in the **constrained** child.
- [ ] Never set a fixed pixel `width` on the container — always `max-width` + `margin-inline: auto`.
- [ ] Prose blocks live _inside_ a `content` container; don't nest `content` inside `content`.

---

## 2. Gutter (responsive side padding)

One token controls all horizontal breathing room: **`--gutter` = `clamp(1rem, 5vw, 2rem)`**.

| Viewport | Resolved gutter | Why |
|---|---|---|
| 320px (min phone) | 16px (`1rem` floor) | Never crowd edges on small phones. |
| ~800px | ~40px (5vw) | Scales fluidly with the viewport. |
| ≥1280px | 32px (`2rem` cap) | Stops growing so content doesn't drift too far from edges. |

- [ ] **Always pad the inner container** with `padding-inline: var(--gutter)` — this is what stops content from touching the screen edge.
- [ ] Full-bleed backgrounds ignore the gutter (they reach the edge); their **content** respects it.
- [ ] Don't stack gutters. If a parent container already applies `--gutter`, children use `--space-*`, not another gutter.

---

## 3. The 12-column grid

Use CSS Grid with 12 columns for any multi-column region. Twelve divides cleanly into 2/3/4/6 columns.

```css
.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: var(--space-6);          /* 24px column/row gap; --space-8 for airier layouts */
}
```

### Responsive column behaviour

| Region | < md (768px) | md → lg | ≥ lg (1024px) |
|---|---|---|---|
| Feature cards | 1 col | 2 col | 3 (or 4) col |
| Two-column hero (text + media) | stacked, text first | stacked | 6 / 6 split |
| Testimonials | 1 col | 2 col | 3 col |
| Footer link columns | 1–2 col | 3 col | 4–5 col |

**Card grid without a full 12-col system** (simpler, auto-responsive):

```css
.card-grid {
  display: grid;
  gap: var(--space-6);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
}
```

**Rules:**
- [ ] **Gap over margins** — space grid/flex children with `gap`, never per-child margins.
- [ ] **`minmax(0, 1fr)`**, not `1fr`, so long words/overflow can't blow out a column.
- [ ] **Collapse to 1 column below `md`.** Single-column mobile is the default; add columns up.
- [ ] Keep gutters between cards ≥ `--space-6` (24px) so touch targets stay ≥8px apart.

---

## 4. Spacing rhythm & vertical section scale

Consistent vertical rhythm is what makes a page feel designed. Two scales, both from the spacing tokens.

### 4.1 Vertical section padding (top & bottom of a section)

| Tier | Token (top & bottom) | Value | Use for |
|---|---|---|---|
| **Compact** | `--space-16` | 64px | Dense sections, logo strips, sub-sections, mobile default. |
| **Standard** | `--space-20` | 80px | Most content sections at desktop. |
| **Spacious** | `--space-24` | 96px | Hero, primary feature blocks, CTA bands. |
| **Grand** | `--space-32` | 128px | Rare — big statement sections with lots of whitespace. |

**Responsive pattern** — smaller on mobile, larger on desktop:

```css
.section { padding-block: var(--space-16); }         /* mobile: 64px */
@media (min-width: 768px) {
  .section { padding-block: var(--space-24); }        /* desktop: 96px */
}
```

- [ ] Pick **one tier per section** and apply it symmetrically (equal top/bottom) unless two sections share a background (then avoid doubled padding — see below).
- [ ] **Adjacent same-background sections:** collapse the seam — don't stack `space-24` + `space-24`. Use a single divider or one section's padding.

### 4.2 Intra-section rhythm (spacing _within_ a section)

| Relationship | Token | Value |
|---|---|---|
| Eyebrow → heading | `--space-2` / `--space-3` | 8–12px |
| Heading → body/lead | `--space-4` | 16px |
| Section header → content block | `--space-10` / `--space-12` | 40–48px |
| Between stacked cards/rows (mobile) | `--space-6` | 24px |
| Grid gap | `--space-6` / `--space-8` | 24–32px |
| Inside a card (padding) | `--space-6` | 24px |

**Rule:** every vertical gap should be a spacing token. If you reach for a value not on the scale, snap to the nearest token instead.

---

## 5. Section templates (structural specs)

Each template below is a **skeleton** — regions, container, grid, spacing. No copy, no colours beyond role tokens. Compose pages from these.

### 5.1 Hero

```
┌───────────────────────────── full-bleed ─────────────────────────────┐
│  container (content) · padding-block --space-24 (mobile --space-16)   │
│  grid-12,  ≥lg: [ text col 1–6 ]        [ media col 7–12 ]            │
│  ┌ text col ─────────────────┐   ┌ media col ────────────────┐        │
│  │ eyebrow (label, --ls-wide)│   │ product shot / illustration│        │
│  │ h1  (--fluid-h1)          │   │ width/height set (no CLS)  │        │
│  │ lead (--fluid-lead)       │   │ fetchpriority=high if LCP  │        │
│  │ [Primary CTA] [Secondary] │   └───────────────────────────┘        │
│  │ trust row (logos/rating)  │                                         │
│  └───────────────────────────┘                                         │
└───────────────────────────────────────────────────────────────────────┘
```

- [ ] Container: `content`. Vertical: **Spacious** (`--space-24`), compact on mobile.
- [ ] ≥lg: two columns (6/6 via `grid-12`). < lg: stack, **text first**, media below.
- [ ] Exactly **one `<h1>`** in the hero (`--fluid-h1`, `--lh-tight`, `--font-display`).
- [ ] Media has explicit `width`/`height` (no layout shift) and is the LCP → `fetchpriority="high"`, not lazy-loaded.
- [ ] Primary CTA uses `--cta-*`, `min-height: var(--target-min)`; secondary is lower-emphasis.
- [ ] Optional trust row (logos/rating) sits under the CTAs at `--space-6`.

### 5.2 Feature grid

```
container (content) · padding-block Standard
[ section header: eyebrow · h2 · lead ]      ← centred or left, max ~60ch
  --space-12
[ grid-12 → auto card grid ]
  <md: 1 col · md: 2 col · lg: 3 (or 4) col · gap --space-6
  card: icon · h3 · body · (optional link)  · padding --space-6 · radius-lg
```

- [ ] `h2` uses `--fluid-h2`. Card titles `h3` (`--text-xl`/`--fluid-h3`).
- [ ] Cards are equal-height (grid rows) — keep body copy roughly balanced.
- [ ] Card surface: `--bg`, `--radius-lg`, `--shadow-sm`/`md`, hover raises shadow (gate transition on reduced-motion).

### 5.3 Logo strip (social proof)

```
container (content or wide) · padding-block Compact (--space-16)
[ small centred label: "Trusted by…" ]  --space-6
[ logo row: flex-wrap or auto-fit grid · gap --space-8 · items centred ]
```

- [ ] Logos: uniform optical height (~24–32px), greyscale/mono for consistency, `alt` text per logo.
- [ ] Wrap gracefully (flex-wrap) — no horizontal scroll on mobile.
- [ ] Compact vertical tier; this is a supporting band, not a hero.

### 5.4 Testimonial

**Single featured:**
```
container (content, or prose for the quote) · padding-block Standard
[ large quote (--text-2xl/--fluid-h3, --lh-snug) ]
[ attribution: avatar · name · role · company ]  --space-6
```

**Grid of testimonials:**
```
container (content) · [ section header ] · --space-12
[ grid-12 → <md 1 · md 2 · lg 3 · gap --space-6 ]
  card: quote · attribution row · padding --space-6 · radius-lg
```

- [ ] Quote text stays within measure (`68ch`) even in a wide container — constrain the quote block.
- [ ] Attribution: avatar (`--radius-full`), name (`--fw-semibold`), role/company (`--text-secondary`).
- [ ] Real names/roles/results support E-E-A-T; avatars have `alt`.

### 5.5 FAQ

```
container (prose or content-narrow ~720px) · padding-block Standard
[ h2 ] · --space-10
[ accordion list ]
  item: <button> question (h3-level, --target-min) │ ▸/▾
         panel: answer in prose measure (--lh-normal)
  divider between items: --border (decorative)
```

- [ ] Use a real disclosure pattern: `<button aria-expanded>` controlling a panel (`aria-controls`), or `<details>/<summary>`.
- [ ] Question row height ≥ `--target-min` (44px); full row is the click target.
- [ ] Answers in prose measure; keep first sentence a concise, extractable answer (GEO/FAQ-schema friendly).
- [ ] Pair with FAQ JSON-LD (structured data lives in the SEO layer, not here).

### 5.6 CTA band

```
┌──────────── full-bleed (brand or dark surface) ────────────┐
│ container (content) · padding-block Spacious (--space-24)   │
│ centred: h2 (--fluid-h2) · supporting line · [Primary CTA]  │
│ optional secondary link · optional reassurance microcopy    │
└─────────────────────────────────────────────────────────────┘
```

- [ ] Background: `--cta-bg` (brand) or `.surface-dark`. If brand background, CTA button must contrast against it — use a light/inverse button, and verify contrast.
- [ ] Single dominant CTA; content centred and constrained (~`50ch` headline).
- [ ] Spacious tier; this is a conversion moment — give it room.

### 5.7 Footer

```
┌──────────── full-bleed (dark: .surface-dark) ────────────┐
│ container (content) · padding-block Standard              │
│ grid-12:                                                  │
│   [ brand col: logo · one-line pitch · NAP ]  cols 1–3    │
│   [ link col ] [ link col ] [ link col ] [ link col ]     │
│ --space-12                                                │
│ [ bottom bar: © {{LEGAL_ENTITY}} · legal links · social ] │
│ padding-bottom += env(safe-area-inset-bottom)             │
└───────────────────────────────────────────────────────────┘
```

- [ ] Columns: <md 1–2, md 3, lg 4–5. Brand/NAP block spans wider on desktop.
- [ ] NAP (name/address/phone) consistent site-wide (SEO/GEO); use placeholders `{{LEGAL_ENTITY}}`, `{{ADDRESS}}`, `{{PHONE}}`, `{{EMAIL}}`.
- [ ] Dark surface via `.surface-dark`; ensure muted footer text still meets contrast (`--text-muted-on-dark`).
- [ ] Add `env(safe-area-inset-bottom)` to bottom padding for notched devices.

---

## 6. Sticky header behaviour

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);              /* 1100 */
  min-height: 4rem;                      /* 64px; ≤72px */
  padding-inline: var(--gutter);
  padding-top: env(safe-area-inset-top); /* notch */
  background: var(--bg);
  transition: box-shadow var(--duration-fast) var(--ease-standard),
              min-height var(--duration-fast) var(--ease-standard);
}
.site-header[data-scrolled="true"] {     /* toggled past ~8px scroll */
  min-height: 3.5rem;                    /* condense to 56px */
  box-shadow: var(--shadow-sm);          /* lift off content */
  background: color-mix(in srgb, var(--bg) 92%, transparent);
  backdrop-filter: saturate(1.1) blur(8px);
}
```

- [ ] Height **64–72px** at rest; condenses to ~56px once scrolled (JS toggles `data-scrolled`, or use a scroll-driven approach).
- [ ] `z-index: var(--z-sticky)` — below overlays/modals, above page content.
- [ ] Add a subtle shadow only **after** scroll so it's flush at the top.
- [ ] **Anchor offset:** any in-page target needs `scroll-margin-top` ≥ header height so it isn't hidden under the sticky bar:

```css
:where(h2, h3, [id]) { scroll-margin-top: 5rem; }
```

- [ ] Mobile nav: hamburger → panel/drawer at `--z-overlay`; trap focus, close on Esc, restore focus to the trigger.
- [ ] The whole condense/shadow transition is decorative → it self-disables under the global reduced-motion reset in `tokens.css`.

---

## 7. Safe-area / notch handling

Modern phones have rounded corners, notches, and home indicators. Full-bleed and fixed elements must respect the safe area.

- [ ] **Viewport meta** must enable safe-area insets:
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  ```
- [ ] **Sticky header:** `padding-top: env(safe-area-inset-top)`.
- [ ] **Footer / bottom-fixed bars:** `padding-bottom: env(safe-area-inset-bottom)`.
- [ ] **Full-bleed side content** in landscape (notch on the side): combine gutter with insets:
  ```css
  padding-inline: max(var(--gutter), env(safe-area-inset-left), env(safe-area-inset-right));
  ```
- [ ] Fixed CTAs / cookie bars / mobile action bars: include the relevant inset so the home indicator never overlaps a control.
- [ ] Test on a device/emulator with `viewport-fit=cover`; without it, `env()` insets resolve to 0.

---

## 8. Layout QA checklist

- [ ] No horizontal scrollbar at any width from **320px up**, and at **200% zoom** (WCAG 1.4.10 reflow).
- [ ] All sections use a **container** (`content`/`wide`/`prose`) + `--gutter`; nothing touches the viewport edge unintentionally.
- [ ] Multi-column regions **collapse to 1 column** below `md`.
- [ ] Vertical section padding uses a **single tier** from §4.1; no arbitrary values.
- [ ] All intra-section gaps are **spacing tokens** (§4.2); grid uses `gap`, not per-child margins.
- [ ] Grid columns use `minmax(0, 1fr)` — no overflow blow-out.
- [ ] Sticky header: correct `z-index`, condense behaviour, and anchors have `scroll-margin-top`.
- [ ] Safe-area insets applied to header, footer, and any fixed elements; `viewport-fit=cover` set.
- [ ] Images have explicit `width`/`height` → **CLS < 0.1**; LCP media not lazy-loaded.
- [ ] Prose blocks constrained to `68ch`; no line exceeds ~75ch.
- [ ] Touch targets ≥ `--target-min` (44px) with ≥ `--target-spacing` (8px) between them.

---

## Related

- [`design-tokens.md`](./design-tokens.md) — the container, spacing, breakpoint, z-index, and motion tokens this layout uses.
- [`../brand/typography.md`](../brand/typography.md) — heading scale, prose measure, and fluid type applied in these templates.
- [`../brand/color-system.md`](../brand/color-system.md) — surface/background/CTA colour roles and contrast rules.
- [`../00-foundations/principles.md`](../00-foundations/principles.md) — whitespace, hierarchy, and motion principles behind these choices.
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — `--container-*`, `--gutter`, `--space-*`, `--z-*` custom properties.
- [`../../tokens/tailwind.tokens.js`](../../tokens/tailwind.tokens.js) — `maxWidth`, `spacing`, `screens`, `zIndex` for utility-based layout.
