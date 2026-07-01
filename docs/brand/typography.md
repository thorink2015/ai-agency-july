# Typography

**Purpose:** The complete type system — font families, scale, weights, line-heights, letter-spacing, heading hierarchy, responsive behavior, and the self-hosting/performance rules that keep type fast and CLS-free — so any page or component renders text on-brand, legible, and WCAG 2.2 AA compliant.
**Status:** v1 foundation — adjustable.

---

## TL;DR (extractable answer)

- **Display / headings:** Sora (variable). **Body / UI:** Inter (variable). **Code / technical accents:** JetBrains Mono.
- **Base size 16px** (`--text-base`), never smaller for body. **Body line-height ≥ 1.5** (WCAG 1.4.12).
- **One `<h1>` per page. Never skip heading levels.** Style is decoupled from level — use classes, not tag choice, to size text.
- **Prose measure caps at 68ch** (`--measure-prose`) for readability (45–75ch target).
- **Self-host** subsetted **WOFF2** via Fontsource (GDPR-compliant, no Google Fonts CDN). **`font-display: swap`**, **preload 1–2 critical fonts**, and ship **`@font-face` `size-adjust` / metric overrides** to eliminate font-swap CLS.
- Ship **only the weights you use** (400/500/600/700). Variable font pays off at **3+ weights**; below that a single subset static WOFF2 can be smaller.

All values below are consumed from [`../../tokens/tokens.css`](../../tokens/tokens.css) (source: [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json)). Reference tokens **by name** (`--text-lg`, `--lh-normal`), not raw px/rem.

---

## 1. Font families

| Role | Family | Token | Style axis used | Use for |
|------|--------|-------|-----------------|---------|
| Display | **Sora** (variable) | `--font-display` | weight 400–700 | h1–h3, eyebrows, big stat numbers, wordmark. Geometric, modern-tech, confident. |
| Body / UI | **Inter** (variable) | `--font-body` | weight 400–700 | body copy, UI labels, buttons, forms, nav, h4–h6, captions. Best-in-class screen legibility. |
| Mono | **JetBrains Mono** | `--font-mono` | weight 400–600 | code snippets, API keys, technical accents, tabular counters. Optional — load only on pages that use it. |

**Full stacks (from tokens — do not retype):**

```css
--font-display: 'Sora', 'Sora Fallback', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
--font-body:    'Inter', 'Inter Fallback', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
--font-mono:    'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
```

- `'* Fallback'` entries are **local metric-matched fallback faces** (see §8) — they are the CLS-prevention layer, not a real installed font.
- Rule of thumb: **Sora ≠ body.** Sora is for headlines and short display strings; long text in Sora reads slower. Body is always Inter.

### Do / Don't — families

| Do | Don't |
|----|-------|
| Use Sora for h1–h3 and hero display strings. | Set paragraphs or long lists in Sora. |
| Use Inter for everything readable and interactive. | Introduce a 4th typeface "for variety." |
| Load JetBrains Mono only where code appears. | Ship mono globally when one page uses it. |
| Rely on the fallback stack while webfonts load. | Leave text invisible during load (FOIT). |

---

## 2. Type scale (px / rem + intended use)

Modular scale on a **16px base**. Consume via `--text-*`. Sizes below `base` are for metadata/labels only — **never** body paragraphs.

| Token | rem | px | Font | Weight | Line-height | Intended use |
|-------|-----|----|----|-------|-------------|--------------|
| `--text-xs` | 0.75 | 12 | Inter | 500 | 1.5 | Legal, timestamps, badge text. Min size on the site. |
| `--text-sm` | 0.875 | 14 | Inter | 400–500 | 1.5 | Captions, helper text, table cells, secondary UI. |
| `--text-base` | 1 | 16 | Inter | 400 | 1.5 (`--lh-normal`) | **Default body.** Never smaller. |
| `--text-lg` | 1.125 | 18 | Inter | 400 | 1.5–1.65 | Lead-in body, comfortable long-form, large UI. |
| `--text-xl` | 1.25 | 20 | Inter/Sora | 500–600 | 1.4 | Sub-lead, card titles, h5–h6. |
| `--text-2xl` | 1.5 | 24 | Sora | 600 | 1.25 (`--lh-snug`) | h4, small section titles, pull quotes. |
| `--text-3xl` | 1.875 | 30 | Sora | 600–700 | 1.25 | h3 (fixed), stat numbers. |
| `--text-4xl` | 2.25 | 36 | Sora | 700 | 1.1–1.25 | h2 (small end), sub-hero. |
| `--text-5xl` | 3 | 48 | Sora | 700 | 1.1 (`--lh-tight`) | h1 (small end), h2 (large end). |
| `--text-6xl` | 3.75 | 60 | Sora | 700 | 1.1 | Large hero h1. |
| `--text-7xl` | 4.5 | 72 | Sora | 700 | 1.1 | Max hero display (h1 clamp ceiling). |

> Prefer the **fluid clamp tokens** (§4) for h1–h3 instead of picking a fixed step, so headings scale smoothly across viewports.

---

## 3. Weights

Ship exactly these four; every extra weight is bytes on the LCP path.

| Name | Token | Value | Use |
|------|-------|-------|-----|
| Regular | `--fw-regular` | 400 | Body copy, long-form, default. |
| Medium | `--fw-medium` | 500 | UI labels, nav, emphasized inline text, small captions. |
| Semibold | `--fw-semibold` | 600 | h3–h6, buttons, card titles, eyebrows. |
| Bold | `--fw-bold` | 700 | h1–h2, big stats, strong display emphasis. |

- **Emphasis in body** = `<strong>` at 600 or 700; **do not** go below 400 or use faux-bold (`font-weight` the browser synthesizes) — always a real shipped weight.
- **Never** use weight < 400 for text (thin faces fail contrast perception and legibility).
- Do not synthesize italics/bold. If you need italic Inter, ship the italic axis; otherwise avoid italics for UI.

---

## 4. Fluid heading clamps

Headings h1–h3 (and the lead paragraph) use `clamp()` so they scale with the viewport between a mobile floor and a desktop ceiling — no media-query stepping, no overflow. Consume the tokens; don't hand-write clamps.

| Token | Value | Floor → ceiling | Applies to |
|-------|-------|-----------------|------------|
| `--fluid-h1` | `clamp(2.25rem, 1.4rem + 4.25vw, 4.5rem)` | 36px → 72px | Page `<h1>` / hero title |
| `--fluid-h2` | `clamp(1.875rem, 1.3rem + 2.9vw, 3rem)` | 30px → 48px | Section `<h2>` |
| `--fluid-h3` | `clamp(1.5rem, 1.2rem + 1.5vw, 2.25rem)` | 24px → 36px | Sub-section `<h3>` |
| `--fluid-lead` | `clamp(1.125rem, 1.05rem + 0.4vw, 1.375rem)` | 18px → 22px | Lead paragraph under h1/h2 |

- h4–h6 use **fixed** steps (`--text-2xl` / `--text-xl` / `--text-lg`) — fluid scaling below h3 adds no value.
- The `vw` term guarantees the floor is hit at ~360px and the ceiling at ~1536px (`--breakpoint-2xl`). Do not exceed the ceiling; giant type past 72px hurts readability and the LCP measurement.

---

## 5. Line-heights & letter-spacing

**Line-height** — larger text gets tighter leading; body stays airy.

| Token | Value | Use |
|-------|-------|-----|
| `--lh-tight` | 1.1 | Display h1/h2 (5xl+). |
| `--lh-snug` | 1.25 | h3–h4, card titles. |
| `--lh-normal` | **1.5** | **Body — WCAG floor. Never below 1.5 for paragraphs.** |
| `--lh-relaxed` | 1.65 | Long-form articles, dense prose blocks. |

**Letter-spacing** — nudge, don't shout. Body stays at 0.

| Token | Value | Use |
|-------|-------|-----|
| `--ls-tighter` | -0.02em | Large display (5xl–7xl) only. |
| `--ls-tight` | -0.01em | h3–h4, 2xl–4xl headings. |
| `--ls-normal` | 0 | **All body, UI, and text ≤ 20px.** |
| `--ls-wide` | 0.02em | Uppercase eyebrows/labels/overlines only. |

- Negative tracking on **body** hurts legibility — reserve it for headings ≥ 24px.
- Uppercase runs (eyebrows) **must** get `--ls-wide` or they read cramped.

---

## 6. Prose measure (line length)

- Cap running text at **`--measure-prose` = 68ch** (target range 45–75ch). Beyond ~75ch the eye loses the next line's start.
- Apply on the text container, not the page: `max-width: var(--measure-prose);`.
- Full-width layouts (cards grids, heroes) are exempt — the 68ch cap is for **paragraph flow**, not layout.

```css
.prose { max-width: var(--measure-prose); }
.prose p + p { margin-block-start: var(--space-4); } /* paragraph rhythm */
```

---

## 7. Heading hierarchy rules

Semantic level and visual size are **separate concerns**. Choose the tag for document structure; choose a size class for looks.

| Rule | Requirement |
|------|-------------|
| One H1 | Exactly **one `<h1>` per page** (the page's main subject). |
| No skips | Never jump h2 → h4. Descend one level at a time; you may climb back up freely. |
| Order = meaning | Heading order reflects the outline, not the visual order on screen. |
| Style ≠ level | Need big text that isn't the page title? Use an `<h2>`/`<p>` with a display **class**, not a misused `<h1>`. |
| No empty headings | Every heading has a text accessible name; never use a heading purely for spacing. |

**Default mapping (visual):**

| Tag | Size token | Family / weight | Tracking |
|-----|-----------|-----------------|----------|
| `h1` | `--fluid-h1` | Sora 700 | `--ls-tighter` |
| `h2` | `--fluid-h2` | Sora 700 | `--ls-tight` |
| `h3` | `--fluid-h3` | Sora 600 | `--ls-tight` |
| `h4` | `--text-2xl` | Sora 600 | `--ls-tight` |
| `h5` | `--text-xl` | Inter 600 | `--ls-normal` |
| `h6` | `--text-lg` | Inter 600 | `--ls-normal` (uppercase → `--ls-wide`) |
| Eyebrow | `--text-sm` | Inter 600, uppercase | `--ls-wide` |
| Lead | `--fluid-lead` | Inter 400 | `--ls-normal` |
| Body | `--text-base` | Inter 400, `--lh-normal` | `--ls-normal` |

```css
h1 { font: 700 var(--fluid-h1)/var(--lh-tight) var(--font-display); letter-spacing: var(--ls-tighter); }
h2 { font: 700 var(--fluid-h2)/var(--lh-tight) var(--font-display); letter-spacing: var(--ls-tight); }
h3 { font: 600 var(--fluid-h3)/var(--lh-snug)  var(--font-display); letter-spacing: var(--ls-tight); }
body { font: 400 var(--text-base)/var(--lh-normal) var(--font-body); color: var(--text); }
.text-balance  { text-wrap: balance; }  /* headings: even line breaks */
.text-pretty   { text-wrap: pretty; }   /* paragraphs: no orphans */
```

- Use `text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs — both are progressive enhancements, safe to apply.

---

## 8. CRITICAL — font performance & loading

Fonts are on the LCP critical path. Get this wrong and you eat FOIT, layout shift, or a GDPR problem. Follow every rule.

### 8.1 Rules (non-negotiable)

- [ ] **Self-host** all fonts. Do **not** hotlink Google Fonts' CDN (Munich GDPR ruling). Install via **Fontsource**; EU-compliant CDN alternatives if ever needed: Bunny Fonts, Coollabs.
- [ ] Ship **WOFF2 only**. No TTF/OTF/WOFF/EOT. WOFF2 is ~30% smaller than WOFF and ~99% supported.
- [ ] **Subset** to the ranges you actually render (Latin at minimum; add `latin-ext` only if used). Subsetting is the biggest single win.
- [ ] **`font-display: swap`** on every `@font-face` — fallback shows in ~100ms, then swaps. Never `block`/FOIT.
- [ ] **Preload the 1–2 critical fonts** only (the weights visible above the fold: typically Inter 400 body + Sora 700 h1). Preloading everything creates contention.
- [ ] Preload links **must** carry `crossorigin` — fonts load in CORS mode even same-origin; omitting it double-fetches.
- [ ] Provide **`size-adjust` + metric overrides** (`ascent/descent/line-gap-override`) on the fallback `@font-face` so the fallback occupies the same box as the webfont → **zero swap CLS**.
- [ ] **Limit weights/axes.** Ship 400/500/600/700 only. Variable font wins at **3+ weights**; for a lone weight, a subset static WOFF2 can be smaller — measure.
- [ ] Inline the critical `@font-face` + font CSS in `<head>` for earliest discovery.
- [ ] Serve fonts **Brotli-precompressed** with `Cache-Control: max-age=31536000, immutable` (hashed filenames). Don't double-compress the already-compressed WOFF2 payload.

### 8.2 Preload snippet (`<head>`)

Preload **only** the above-the-fold weights. Order: preload → inline `@font-face` → styles.

```html
<!-- Critical body + hero heading weight only. crossorigin is REQUIRED. -->
<link rel="preload" href="/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/sora-latin-700-normal.woff2"  as="font" type="font/woff2" crossorigin>
```

> If you ship the variable font, preload the single variable WOFF2 per family instead of per-weight, and cover the visible weight range with one file.

### 8.3 `@font-face` — variable, subsetted, swap

```css
/* Inter — variable, Latin subset, weight axis 100–900 (we only *use* 400–700) */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400 700;          /* declare only the range you use */
  font-display: swap;
  src: url('/fonts/inter-latin-variable.woff2') format('woff2-variations');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+2000-206F, U+2074,
                 U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

/* Sora — variable, Latin subset, display use */
@font-face {
  font-family: 'Sora';
  font-style: normal;
  font-weight: 400 700;
  font-display: swap;
  src: url('/fonts/sora-latin-variable.woff2') format('woff2-variations');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+2000-206F, U+2074,
                 U+20AC, U+2122, U+2212, U+2215, U+FEFF, U+FFFD;
}
```

### 8.4 CLS-killing fallback faces (metric overrides)

Define a metric-matched **fallback** `@font-face` per family so the system font used during `swap` occupies the exact same space. This is what the `'* Fallback'` entries in the token stacks point to. Tune numbers with [Fontaine](https://github.com/unjs/fontaine) or the Malte Ubl generator; the values below are production starting points.

```css
/* Inter fallback → Arial-metric-matched, no CLS on swap */
@font-face {
  font-family: 'Inter Fallback';
  src: local('Arial');
  ascent-override: 90.44%;
  descent-override: 22.52%;
  line-gap-override: 0%;
  size-adjust: 107.4%;
}

/* Sora fallback → Arial-metric-matched */
@font-face {
  font-family: 'Sora Fallback';
  src: local('Arial');
  ascent-override: 96%;
  descent-override: 30%;
  line-gap-override: 0%;
  size-adjust: 103%;
}
```

> Re-generate these overrides whenever the subset or primary font changes. Wrong metrics reintroduce the CLS you were preventing.

### 8.5 Fallback stack (what shows before webfonts land)

Ordered per family. The `system-ui` chain renders instantly and closely resembles the target.

| Family | Fallback chain |
|--------|----------------|
| Sora | `'Sora Fallback', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif` |
| Inter | `'Inter Fallback', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif` |
| Mono | `ui-monospace, SFMono-Regular, Menlo, monospace` |

### 8.6 Budget & targets

| Metric | Target |
|--------|--------|
| Fonts on the critical (preloaded) path | **1–2 files** |
| Format | WOFF2 only |
| Per-family subset size (Latin, variable) | aim ≤ 30–40KB each |
| `font-display` | `swap` (never `block`) |
| Font-swap CLS contribution | **0** (metric overrides) |
| Cache-Control (hashed fonts) | `max-age=31536000, immutable` |

---

## 9. Responsive type behavior

| Concern | Rule |
|---------|------|
| Scaling | h1–h3 + lead scale via `clamp()` tokens (§4). No per-breakpoint font sizes. |
| Body size | Stays `--text-base` (16px) at every breakpoint — never shrink body on mobile. |
| Zoom / resize | Text must survive **200% zoom** (WCAG 1.4.4) and reflow to a **320px** viewport (1.4.10) without horizontal scroll. Because base is `rem`, zoom scales everything. |
| User text-spacing | No clipping when users force 1.5× line-height, 2× paragraph spacing, 0.12em letter, 0.16em word (WCAG 1.4.12). Don't set fixed heights on text containers. |
| Measure | 68ch cap holds at all widths; on wide screens the container centers, it doesn't stretch. |
| Mono | Use `font-variant-numeric: tabular-nums` for counters/stats so digits don't jitter. |

---

## 10. Accessibility checklist (type-specific, WCAG 2.2 AA)

- [ ] Body text ≥ 16px and line-height ≥ 1.5.
- [ ] Text contrast ≥ **4.5:1** normal, ≥ **3:1** large (≥24px regular or ≥18.66px bold). See [`color-system.md`](./color-system.md).
- [ ] No text as images (except the logo wordmark).
- [ ] Exactly one `<h1>`; no skipped heading levels; no empty/spacer headings.
- [ ] Survives 200% zoom and 320px reflow with no clipping or horizontal scroll.
- [ ] Real font weights only — no synthesized bold/italic; nothing below weight 400.
- [ ] `font-display: swap` everywhere (no FOIT hiding text).
- [ ] Meaning never conveyed by weight/size/color alone.

---

## Related

- [`brand-guidelines.md`](./brand-guidelines.md) — master brand overview & index.
- [`color-system.md`](./color-system.md) — canonical colour & text-contrast rules.
- [`logo-and-usage.md`](./logo-and-usage.md) — Sora specs for the wordmark.
- [`voice-and-tone.md`](./voice-and-tone.md) — how the words themselves should read.
- [`iconography.md`](./iconography.md) — icon grid & stroke, paired with type.
- [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — validated text/background pairings.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — source of truth for all type values.
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — the `--font-*`, `--text-*`, `--lh-*`, `--ls-*` custom properties to consume.
