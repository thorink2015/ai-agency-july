# Logo & Usage

**Purpose:** The logo system spec for {{BRAND_NAME}} — variants, clear space, minimum sizes, placement, misuse rules, and the full favicon/app-icon/OG-image export matrix — plus a concrete creation brief, because **no logo exists yet**. When a logo is designed, it must conform to this doc.
**Status:** v1 foundation — adjustable.

---

## Status: no logo exists yet

There is no logo file in [`assets/brand/`](../../assets/brand/) at time of writing. Until one is created:

- Use the **wordmark placeholder**: `{{BRAND_NAME}}` set in **Sora SemiBold (600)**, letter-spacing `-0.01em`, in `--color-neutral-ink` on light / `--color-neutral-0` on dark.
- Do not commission or ship a logo that violates the [creation brief](#logo-creation-brief) or the [construction rules](#construction-rules-apply-to-every-variant) below.
- Once real files land in `assets/brand/`, update the [Status](#status-no-logo-exists-yet) line and check off the [delivery checklist](#delivery-checklist).

---

## Logo anatomy

The logo system has three parts. Not every variant uses all three.

| Part | What it is | Notes |
|---|---|---|
| **Symbol / mark** | Standalone glyph (icon) | Must read at 16px. Used for favicon, app icon, avatar. |
| **Wordmark** | `{{BRAND_NAME}}` as styled type | Sora-based; may be used without the symbol. |
| **Lockup** | Symbol + wordmark locked together | The primary logo. Fixed spacing between symbol and wordmark. |

---

## Variants

Every variant ships in the [export matrix](#file-format--export-matrix). Filenames follow the [naming convention](#file-naming-convention).

| Variant | When to use | Foreground | Background |
|---|---|---|---|
| **Primary (full colour)** | Default. Light backgrounds. | Brand indigo `--color-brand-600` symbol + ink `--color-neutral-ink` wordmark | Light (`--color-neutral-0/50`) |
| **Reversed (on dark)** | Dark sections, footers, dark hero | White `--color-neutral-0` (symbol may keep brand indigo if it holds ≥3:1 on the dark bg) | Dark (`--color-neutral-ink`, `#0B1120`) |
| **Mono — dark** | 1-colour contexts on light (print, fax, embroidery, single-ink) | Solid `--color-neutral-ink` | Light |
| **Mono — light** | 1-colour contexts on dark | Solid `--color-neutral-0` | Dark |
| **Symbol only** | Favicon, app icon, avatar, tight spaces | Per above | Per above |
| **Wordmark only** | Where symbol is redundant or too small to help | Per above | Per above |

**Colour rules (inherit from [`color-system.md`](./color-system.md)):**

- The symbol may use brand indigo `--color-brand-600`; accent teal `--color-accent-500` is allowed only as a **secondary/decorative** element within the symbol, never as the sole foreground on a dark bg where it must carry meaning.
- **Never** place the logo where its foreground drops below **3:1** against the background (WCAG 1.4.11 for graphical objects).
- Full-colour logo on photography: only over a solid, calm area or a scrim; otherwise use mono/reversed.

---

## Construction rules (apply to every variant)

- **Grid:** design the symbol on a **24px icon grid** to match [`iconography.md`](./iconography.md). Keystroke weight `1.5px–2px` optical at base; rounded joins/caps — "rounded-but-crisp."
- **Geometry:** align to the brand's rounded-but-crisp language. Corner radii should echo `--radius` steps, not arbitrary curves.
- **Optical balance:** the symbol should sit visually centered, not mathematically centered. Trim the SVG viewBox to the true bounds, then add clear space as padding — never bake padding into the artwork.
- **One weight of truth:** the wordmark is **Sora SemiBold (600)** by default. Convert to outlines in delivered SVGs so it renders without the font installed.

---

## Clear space

Clear space = the minimum breathing room around the logo. **No other element (text, edge, image, button) may enter it.**

- **Clear space = the cap height (`X`) of the wordmark**, applied on all four sides.
- For the **symbol only**, `X` = **25% of the symbol's width**.

```
   ┌───────────────────────────────┐
   │            ↕ X                 │   X = cap height of the wordmark
   │   ┌───────────────────────┐    │
   │ X │   [symbol]  BRANDNAME  │ X  │   (for symbol-only: X = 25% of symbol width)
   │   └───────────────────────┘    │
   │            ↕ X                 │
   └───────────────────────────────┘
```

More clear space is always fine; less is never allowed.

---

## Minimum sizes

Below these sizes the logo loses legibility. Do not go smaller.

| Variant | Min width (digital) | Min width (print) |
|---|---|---|
| **Full lockup** | **120px** | 25mm |
| **Wordmark only** | **90px** | 20mm |
| **Symbol only** | **24px** (favicon exception: 16px, see below) | 8mm |

- The **16px favicon** is the only place the symbol may render below 24px — it must be a **hand-tuned, simplified** version (see [favicon guidance](#favicon-strategy)).
- If a needed placement is smaller than the minimum, switch to the **symbol only** rather than shrinking the lockup.

---

## Placement

| Context | Placement | Size guidance |
|---|---|---|
| **Site header** | Top-left, vertically centered in the nav | Lockup ~28–36px tall; tappable target ≥44px (link padding) |
| **Footer** | Top-left of footer block or centered above legal | Reversed/mono on the dark footer |
| **Favicon / tab** | Browser-controlled | Symbol only (see matrix) |
| **OG / social share** | Composed into the 1200×630 card, not floating full-bleed | See [OG image](#og--social-share-image) |
| **Email signature** | Left-aligned, lockup | ≥120px wide, link to `{{DOMAIN}}` |
| **Avatars (social)** | Symbol only, centered with padding | Provide a padded square export |

- Default alignment is **left**. Center only in symmetrical layouts (footer, splash, avatar).
- Keep the logo on a calm surface. Never on a busy photo without a scrim.

---

## Misuse — do not

Every rule below has caused a real brand to look broken. Enforce them.

| # | Don't | Why |
|---|---|---|
| 1 | Stretch, squash, or change proportions | Distorts the mark |
| 2 | Rotate or skew | Breaks the horizontal reading |
| 3 | Recolour outside the approved variants | Off-brand, often fails contrast |
| 4 | Put white text/logo on `accent-500` teal | Fails contrast (2.43:1) — see colour doc |
| 5 | Add drop shadows, glows, bevels, gradients (unless in the approved artwork) | Cheapens the premium feel |
| 6 | Place on a low-contrast or busy background (<3:1) | Illegible; WCAG fail |
| 7 | Re-typeset the wordmark in another font | It's not the wordmark anymore |
| 8 | Alter spacing between symbol and wordmark | Breaks the lockup |
| 9 | Add taglines/effects inside the clear space | Crowds the mark |
| 10 | Use a low-res raster where an SVG should be used | Blurry, unprofessional |
| 11 | Reconstruct the logo from parts (DIY lockup) | Use the official lockup file |
| 12 | Outline, add keylines, or "sticker" the logo | Off-brand |

---

## File format & export matrix

All source and exports live in [`assets/brand/`](../../assets/brand/). **SVG is the master for every logo variant**; rasters are exports for fixed-size targets.

### Logo variants (vector master + raster fallback)

| Asset | Format(s) | Notes |
|---|---|---|
| Primary lockup | SVG (master) + PNG @1x/@2x | PNG only where SVG can't be used |
| Reversed lockup | SVG + PNG @1x/@2x | For dark backgrounds |
| Mono dark / mono light | SVG each | 1-colour contexts |
| Symbol only | SVG + PNG @1x/@2x | Basis for favicon/app icons |
| Wordmark only | SVG | Type outlined |

**SVG hygiene:** run through SVGO; strip metadata/editor cruft; keep a meaningful `viewBox`; include `<title>` for accessibility; avoid embedded rasters; ensure single-path where practical.

### Favicon set

| File | Size(s) | Format | Notes |
|---|---|---|---|
| `favicon.ico` | **16, 32, 48** (multi-res) | ICO | Legacy + browser tabs; bundle all three sizes in one `.ico` |
| `favicon.svg` | scalable | SVG | Modern browsers; `<link rel="icon" type="image/svg+xml">`; supports dark-mode via `prefers-color-scheme` inside the SVG |
| `apple-touch-icon.png` | **180×180** | PNG | iOS home screen; **no transparency** (opaque background); ~40px safe padding |

### Android / PWA maskable icons

| File | Size | Format | Notes |
|---|---|---|---|
| `icon-192.png` | **192×192** | PNG | `purpose: "maskable"` in the web manifest |
| `icon-512.png` | **512×512** | PNG | `purpose: "maskable"`; also used as splash source |

**Maskable safe zone:** keep all critical artwork within the **central 80%** (≈40px inset on 512, per Android's maskable spec / minimum safe radius). Fill the full canvas with a brand background colour — no transparency — so the OS mask can crop to any shape without clipping the symbol.

Reference in `manifest.webmanifest`:

```json
{
  "icons": [
    { "src": "/assets/brand/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable" },
    { "src": "/assets/brand/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" },
    { "src": "/assets/brand/icon-192-any.png", "sizes": "192x192", "type": "image/png", "purpose": "any" }
  ],
  "theme_color": "#4F46E5",
  "background_color": "#0B1120"
}
```

> `theme_color` = brand indigo `#4F46E5` (`--color-brand-600`). `background_color` = ink `#0B1120` (`--color-neutral-ink`). Ship an `any`-purpose 192 too, so non-maskable contexts don't get over-cropped.

### `<head>` wiring (copy-paste)

```html
<link rel="icon" href="/assets/brand/favicon.ico" sizes="16x16 32x32 48x48">
<link rel="icon" type="image/svg+xml" href="/assets/brand/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/brand/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#4F46E5">
```

### OG / social share image

| File | Size | Format | Notes |
|---|---|---|---|
| `og-default.png` (or `.jpg`) | **1200×630** | PNG or JPG | Default Open Graph + Twitter card; keep under performance budget |

- **Safe area:** keep logo and key text within the central **1140×580**; platforms crop edges.
- Composition: reversed/mono logo on `--color-neutral-ink`, or primary logo on `--color-neutral-50`, with a short benefit line in Sora. High contrast, no tiny text.
- Per-page OG images are encouraged; this is the fallback. See [`../seo/`](../seo/) for meta wiring (`og:image`, `twitter:image`, dimensions).

```html
<meta property="og:image" content="https://example.com/assets/brand/og-default.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
```

---

## File naming convention

All lowercase, hyphen-separated, `{brand}-{part}-{variant}[-{modifier}]@{scale}.{ext}`. Use `logo` as `{brand}` prefix (swap to real brand slug on find-and-replace).

| Pattern | Example |
|---|---|
| Lockup, primary | `logo-lockup-primary.svg` |
| Lockup, reversed | `logo-lockup-reversed.svg` |
| Lockup, PNG @2x | `logo-lockup-primary@2x.png` |
| Mono dark / light | `logo-lockup-mono-dark.svg`, `logo-lockup-mono-light.svg` |
| Symbol | `logo-symbol-primary.svg` |
| Wordmark | `logo-wordmark-ink.svg` |
| Favicon | `favicon.ico`, `favicon.svg` |
| Apple touch | `apple-touch-icon.png` |
| Maskable | `icon-192.png`, `icon-512.png`, `icon-192-any.png` |
| OG | `og-default.png` |

**Rules:** no spaces, no capitals, no version numbers in filenames (use git). `@2x`/`@3x` suffix only for raster density variants. SVG needs no scale suffix.

---

## Where assets live

```
assets/brand/
├── logo-lockup-primary.svg        # master, full colour
├── logo-lockup-reversed.svg       # for dark
├── logo-lockup-mono-dark.svg
├── logo-lockup-mono-light.svg
├── logo-symbol-primary.svg
├── logo-wordmark-ink.svg
├── logo-lockup-primary@2x.png     # raster fallback
├── favicon.ico                    # 16/32/48 multi-res
├── favicon.svg
├── apple-touch-icon.png           # 180
├── icon-192.png                   # maskable
├── icon-512.png                   # maskable
├── icon-192-any.png               # any-purpose
└── og-default.png                 # 1200×630
```

Keep editable source (e.g. `.fig`, `.ai`) out of the web bundle — store in the design source repo/folder, not `assets/brand/`. Only export-ready files ship.

---

## Logo creation brief

Hand this to a designer (or generate against it). The mark must feel **modern-tech with warmth**, matching the brand personality: trustworthy, fast, competent, human+AI, premium-but-approachable, calm confidence.

### Concept direction

- **Idea space:** speed-to-lead and "the conversation that gets answered." Motifs worth exploring: a **chat/speech bubble** fused with a **spark/bolt (speed)**, a **checkmark/booked slot**, a forward-motion arrow, or an abstract "signal answered" glyph. Avoid literal robots, brains, and generic chat-bubble clip-art.
- **Human + AI:** hint at both — e.g. a bubble that also reads as a person/presence — without being cute or gimmicky.
- **Tone:** confident and calm, not loud. It should look at home next to premium SaaS/agency brands, not a hype startup.

### Construction requirements

- [ ] Symbol designed on a **24px grid**, optically balanced, legible at **16px**.
- [ ] Rounded-but-crisp geometry; corner radii echo `--radius` steps; stroke `1.5–2px` optical.
- [ ] Works in **1 colour** (mono) before any colour is added — test mono first.
- [ ] Wordmark in **Sora SemiBold (600)**, tracking `-0.01em`, outlined in delivered SVGs.
- [ ] Passes **≥3:1** contrast in every approved placement (primary, reversed, mono).
- [ ] No gradient/shadow/bevel dependence — must survive as flat vector.

### Palette for the mark

- Primary symbol colour: brand indigo `--color-brand-600` `#4F46E5`.
- Optional secondary/decorative: accent teal `--color-accent-500` `#06B6D4` (never the sole meaning-bearing colour on dark).
- Neutrals: ink `#0B1120`, white `#FFFFFF`.
- No colours outside the token palette.

### Deliverables (the designer must return)

- [ ] Lockup: primary, reversed, mono-dark, mono-light — as **SVG**.
- [ ] Symbol-only and wordmark-only — as **SVG**.
- [ ] Correctly exported favicon set (ICO 16/32/48, SVG), apple-touch 180, maskable 192/512 (+ any-192), OG 1200×630.
- [ ] A one-page usage sheet confirming clear space and min sizes from this doc.
- [ ] Editable source file (kept out of `assets/brand/`).

---

## Delivery checklist

- [ ] All SVGs optimized (SVGO), `viewBox` present, `<title>` set, type outlined.
- [ ] Every variant validated ≥3:1 against its intended background (log in `docs/accessibility/contrast-matrix.md`).
- [ ] Favicon `.ico` contains 16/32/48; `favicon.svg` present and dark-mode aware.
- [ ] `apple-touch-icon.png` is 180×180, opaque, padded.
- [ ] Maskable 192/512 keep artwork in the central 80% safe zone; opaque background.
- [ ] `og-default.png` is exactly 1200×630, key content in the 1140×580 safe area, under budget.
- [ ] `<head>` and `manifest.webmanifest` wired per snippets above.
- [ ] Files named per convention and placed in `assets/brand/`.
- [ ] [Status](#status-no-logo-exists-yet) line updated once real files land.

---

## Favicon strategy

- The generic favicon derives from the **symbol only**, never the full lockup (illegible when tiny).
- At **16px**, hand-tune: thicken strokes, drop fine detail, increase internal contrast. Do not just downscale the 512 export.
- Prefer `favicon.svg` for modern browsers; keep `favicon.ico` (16/32/48) for legacy and Windows tiles.
- Test on **both** light and dark browser chrome; if the symbol vanishes on one, give `favicon.svg` a `prefers-color-scheme` swap.

---

## Related

- [`brand-guidelines.md`](./brand-guidelines.md) — master brand overview & index.
- [`color-system.md`](./color-system.md) — canonical colour, contrast, ≥3:1 rules for graphical objects.
- [`iconography.md`](./iconography.md) — 24px grid, stroke weight the symbol must match.
- [`typography.md`](./typography.md) — Sora specs for the wordmark.
- [`../seo/`](../seo/) — OG/Twitter meta wiring and image references.
- [`../../assets/brand/`](../../assets/brand/) — where the exported logo & icon files live.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — colour & radius values referenced here.
