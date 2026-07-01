# Image Optimization

**Purpose:** The end-to-end image pipeline — which formats to serve (AVIF → WebP → fallback, SVG for vector), how to build responsive `srcset`/`sizes` recipes, how to eliminate image-driven CLS with explicit dimensions, when to lazy-load vs eager-load, how to prioritize the LCP image, per-role KB budgets, encoding settings, and the tooling to produce it all — so every image on the site is as small as it can be while looking flawless, and never becomes the reason a page misses its Core Web Vitals.
**Status:** v1 foundation — adjustable.

---

> **This is a systems/standards doc.** It defines how images are produced and delivered. The byte budgets it enforces come from [`performance-budget.md`](./performance-budget.md); responsive-image reasoning aligns with [`../responsive/responsive-standards.md`](../responsive/responsive-standards.md); art-direction/subject rules live in [imagery](../brand/imagery.md). Raw pixel/KB numbers appear here because they *are* the standard.

---

## 0. TL;DR — the image rules

- [ ] **AVIF first, WebP fallback, JPEG/PNG last.** Serve via `<picture>` (or an image CDN negotiating on the `Accept` header).
- [ ] **SVG for anything vector** — logos, icons, simple illustrations. Optimized with SVGO.
- [ ] **Always set `width` + `height`** (or CSS `aspect-ratio`) on every `<img>`/`<video>`. This is the #1 fix for image CLS.
- [ ] **Responsive raster images use `srcset` (w-descriptors) + `sizes`.** No `sizes` = the browser downloads the biggest file on every device.
- [ ] **The LCP image: eager + `fetchpriority="high"`, never `loading="lazy"`.** Exactly one high-priority image per page.
- [ ] **Below-the-fold images: `loading="lazy"` + `decoding="async"`** (+ optional `fetchpriority="low"`).
- [ ] **Generate 3–5 size variants**, cap at ~2560px, target 2× DPR (not 3×).
- [ ] **Budgets:** hero/LCP < 150 KB (200 KB ceiling), content image < 100 KB, total initial images < 500 KB.
- [ ] **Optimize at build time**, in CI — never ship a hand-exported 2 MB JPEG.

---

## 1. Format decision table

| Content type | Primary | Fallback | Notes |
|---|---|---|---|
| **Photographs / complex raster** (hero, testimonials, screenshots) | **AVIF** | WebP → JPEG | AVIF ~50% smaller than JPEG, ~20–50% smaller than WebP at matched quality; supports HDR/wide gamut. |
| **Flat graphics / UI screenshots with sharp edges** | **AVIF or WebP** | PNG | WebP/AVIF lossless beats PNG; use lossless mode for crisp UI. |
| **Logos, icons, simple illustrations, diagrams** | **SVG** | — | Vector = infinitely scalable, tiny, crisp on every DPR. See §7. |
| **Animation / short loops** | **Animated WebP** or looping muted `<video>` (`.webm`/`.mp4`) | — | Animated **WebP preferred over animated AVIF** in 2026 (AVIF encodes far slower). For anything non-trivial, use a muted autoplay `<video>` (much smaller than any animated image). Never GIF. |
| **Transparency needed** | **AVIF or WebP** (both support alpha) | PNG | Skip PNG unless a legacy target needs it. |

**Support reality (early 2026):** WebP ~96–97% global (safe as a sole modern format for most sites), AVIF ~93–95% (use with a fallback). Both are Baseline. **JPEG XL is progressive enhancement only** in 2026 — Safari ships it by default; Chrome (Feb 2026, behind a flag) and Firefox 152 (June 2026, behind a flag) are re-adding it; global support ~16% rising toward ~85–90% once Chrome enables it by default (expected H2 2026). **Do not** make JXL a primary format yet — add it as an extra `<source>` only if your CDN does it for free.

---

## 2. Encoding quality settings

Encode to the smallest file that is visually indistinguishable at display size. Recommended starting points (tune per image, verify by eye):

| Format | Quality setting | Effort/speed | Rough cross-format equivalence |
|---|---|---|---|
| **AVIF** | quality **60–80** (65–75 typical); CQ ~23–32 on the 0–63 scale (lower = higher quality) | encoder effort/speed **~6** | AVIF q50 ≈ WebP q65 ≈ JPEG q60 |
| **WebP** | quality **75–85** (aim 80–85 for photos — the curve is inconsistent) | default | — |
| **JPEG** (fallback only) | quality **75–80**, progressive, mozjpeg | — | — |

Rules:
- **Don't ship "quality 100."** It's mostly wasted bytes with no visible gain.
- **Verify perceptually**, not by a number. Test the actual image at its real rendered size on a retina and non-retina screen.
- **Strip metadata** (EXIF/GPS/thumbnails) on export — smaller and privacy-safe.
- **Never up-scale.** A source smaller than the largest variant means you generate fewer variants, not fake big ones.

---

## 3. Responsive images — `srcset` + `sizes`

Use **`srcset` with width (`w`) descriptors + `sizes`** for any image whose rendered width varies by viewport. The browser picks the smallest file that satisfies the slot at the device's DPR.

- **`srcset`** lists each file with its intrinsic pixel width: `hero-800.avif 800w, hero-1200.avif 1200w, …`.
- **`sizes`** tells the browser the image's **rendered CSS width** at each breakpoint, *before* layout — e.g. `sizes="(max-width: 768px) 100vw, 50vw"`. **Without `sizes`, the browser assumes 100vw and downloads the largest candidate on every device.**
- Use **`x` descriptors only for fixed-size images** (density switching, e.g. an avatar): `srcset="avatar.avif 1x, avatar@2x.avif 2x"`.
- Use **`<picture>` only for art direction** (a genuinely different crop per breakpoint) **or format fallback** (§4) — not for plain resolution switching, which `srcset`/`sizes` handles alone.

**Variant generation:** create **3–5 variants stepped by file size**, not by device model. Typical widths: **640–768** (phones), **1024–1280** (tablets/small laptops), **1920 / 2560** (full-width desktop / retina). **Cap at ~2560px.** **2× DPR is enough** — don't generate 3× (negligible benefit, real bytes). **All variants must share the exact same aspect ratio** or you reintroduce CLS.

```html
<!-- Responsive content image, format fallback + width switching -->
<picture>
  <source
    type="image/avif"
    srcset="/img/case-640.avif 640w, /img/case-1024.avif 1024w, /img/case-1600.avif 1600w"
    sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 600px">
  <source
    type="image/webp"
    srcset="/img/case-640.webp 640w, /img/case-1024.webp 1024w, /img/case-1600.webp 1600w"
    sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 600px">
  <img
    src="/img/case-1024.jpg"
    srcset="/img/case-640.jpg 640w, /img/case-1024.jpg 1024w, /img/case-1600.jpg 1600w"
    sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 600px"
    width="1600" height="900"
    loading="lazy" decoding="async"
    alt="Result: response time dropped from 8 hours to 42 seconds">
</picture>
```

> Keep `sizes` accurate. If the layout says the image is 600px on desktop, don't tell the browser 100vw — you'll pull a needlessly large file. When the CSS layout changes, the `sizes` value must change with it.

---

## 4. Preventing image CLS — always reserve space

Layout shift from images is the leading cause of CLS, and it's fully preventable.

- **Set `width` and `height` attributes on every `<img>` and `<video>`.** Since 2019 the browser derives an internal `aspect-ratio` from them and reserves the box *before* the file loads.
- **Pair with responsive CSS** so the image scales without breaking the reserved ratio:

```css
img, video {
  max-width: 100%;
  height: auto;          /* scales height with width, preserving the reserved ratio */
}
```

- **Never use `width: auto`** on a responsive image — it overrides the reserved-space calculation and reintroduces shift.
- **All `srcset` variants must share the same aspect ratio.** Mixed ratios = shift when a different variant loads.
- For a purely CSS-sized slot, use `aspect-ratio` on the container instead of/alongside attributes.
- **`background-image` reserves nothing** — for any meaningful/LCP image use a real `<img>`/`<picture>`, not a CSS background.

See [`performance-budget.md`](./performance-budget.md) §1 (CLS ≤ 0.1) and [`../responsive/responsive-standards.md`](../responsive/responsive-standards.md).

---

## 5. Loading priority — LCP vs the rest

The single highest-leverage LCP win: **the LCP image is eager and prioritized; everything below the fold is deferred.**

| Image role | `loading` | `fetchpriority` | `decoding` | Other |
|---|---|---|---|---|
| **LCP image** (hero, above-the-fold headline image) | **eager** (omit `loading` / `loading="eager"`) | **`high`** | `async` | Must be a real `<img>` in the initial HTML. Optional matching `<link rel="preload">` if late-discovered. **Never** `loading="lazy"`. |
| **Above-the-fold, non-LCP** | eager | — (or `low` to yield bandwidth to LCP) | `async` | Don't lazy-load anything in the first viewport. |
| **Below-the-fold** | **`lazy`** | `low` (optional) | `async` | The default for most content images. |

```html
<!-- LCP hero image: eager, high priority, dimensions set, NOT lazy -->
<img
  src="/img/hero-1200.avif"
  srcset="/img/hero-800.avif 800w, /img/hero-1200.avif 1200w, /img/hero-2000.avif 2000w"
  sizes="100vw"
  width="1200" height="675"
  fetchpriority="high"
  decoding="async"
  alt="AI assistant booking an appointment in a live chat, 42-second response">
```

Rules & pitfalls:
- **Exactly one `fetchpriority="high"` image per page** (the LCP one). Marking several cancels the benefit.
- **Lazy-loading the LCP/above-the-fold image adds ~500ms+** and triggers a Lighthouse warning — the most common image mistake. Don't.
- Google's measured example: `fetchpriority="high"` on the hero took LCP **2.6s → 1.9s** (~0.7s, ~27%).
- Chrome pre-fetches lazy images ~**1250–2500px before** the viewport, so they're usually ready on scroll — safe to lazy-load anything genuinely below the fold.
- Use **`fetchpriority="low"`** on non-critical early-DOM images (e.g. a logo strip) so bandwidth flows to the LCP image first.

---

## 6. Per-role KB budgets

Aligned with [`performance-budget.md`](./performance-budget.md) §3. Budgets are **compressed transfer size at the delivered variant**, not the source.

| Image role | Target | Ceiling |
|---|---|---|
| **Hero / LCP image** | **< 150 KB** | 200 KB |
| **Content / section image** | **< 100 KB** | 150 KB |
| **Thumbnail / avatar / logo strip item** | **< 30 KB** | 50 KB |
| **Icon (SVG)** | **< 2 KB** | 5 KB |
| **Total images, initial viewport** | **< 500 KB** | — |

If a hero can't hit 200 KB as a photo, the fix is usually: a tighter crop, a simpler image, a slightly lower AVIF quality, a smaller max variant, or replacing a photo with an SVG/illustration — **not** raising the budget.

---

## 7. SVG discipline

SVG is the format for logos, icons, and simple illustrations — tiny, crisp at every DPR, stylable with CSS.

- **Optimize with SVGO in CI** using a committed `svgo.config.js`, not ad-hoc.
  - `removeViewBox: false` (keeping `viewBox` is what makes it scale)
  - `multipass: true`
  - `floatPrecision: 2` for icons, `3` for detailed illustrations
- **Inline tiny SVGs** (< ~5 KB, ideally < 1 KB icons) directly in markup to save a request and allow `currentColor` theming.
- **Externalize larger/complex SVGs** as `<img src="…svg">` so the browser can cache them across pages.
- **Strip editor cruft** (Illustrator/Figma metadata, hidden layers, comments, default fills).
- **Never** embed a raster inside an SVG to "make it responsive" — that just hides a big PNG.
- Set `width`/`height` (or a sized container) on inline icons so they don't reflow.

```js
// svgo.config.js
export default {
  multipass: true,
  floatPrecision: 2,
  plugins: [
    { name: 'preset-default', params: { overrides: { removeViewBox: false } } },
    'removeDimensions', // keep viewBox, drop width/height so CSS controls size
  ],
};
```

---

## 8. Tooling

Produce all variants and formats **automatically at build time / in CI** — no manual exports.

| Tool | Use |
|---|---|
| **sharp** (Node) | Programmatic resize + AVIF/WebP/JPEG encode in build scripts; the engine behind most frameworks' image pipelines. Fastest for batch. |
| **Framework image components** | Astro `<Image>` / `astro:assets`, Next `<Image>`, `@11ty/eleventy-img` — generate `srcset`, formats, dimensions, and lazy attrs for you. **Prefer these** so you don't hand-maintain markup. |
| **Squoosh** (app or CLI) | One-off manual encodes + eyeballing AVIF/WebP quality trade-offs. |
| **`avifenc` / `cwebp`** (CLI) | Scripted encodes with precise quality/effort control. |
| **SVGO** | SVG optimization (§7), wired into CI. |
| **Image CDN** (Cloudinary / imgix / Cloudflare Images / Netlify Image CDN) | On-the-fly resize + `Accept`-header format negotiation (auto AVIF/WebP). Good when the image set is large or user-generated. |

**CI enforcement:**
- [ ] Build fails if any delivered image exceeds its role budget (§6).
- [ ] Build fails if an `<img>` lacks `width`/`height` (or `aspect-ratio`).
- [ ] Lint that no above-the-fold/LCP image has `loading="lazy"`, and no page has > 1 `fetchpriority="high"` image.

---

## 9. Pre-merge image checklist

- [ ] Every raster image served **AVIF-first** with a WebP (and JPEG/PNG) fallback via `<picture>` or CDN negotiation.
- [ ] Every `<img>`/`<video>` has **`width` + `height`** (or `aspect-ratio`); `img { height: auto; max-width: 100% }` in place.
- [ ] Responsive images use **`srcset` (w) + accurate `sizes`**; 3–5 variants; all same aspect ratio; capped ~2560px.
- [ ] **LCP image:** in initial HTML, `fetchpriority="high"`, eager, `decoding="async"`, **not** lazy, within 150/200 KB.
- [ ] Below-the-fold images: **`loading="lazy"` + `decoding="async"`**.
- [ ] Exactly **one** `fetchpriority="high"` image on the page.
- [ ] All images within their **role budgets** (§6); total initial images < 500 KB.
- [ ] SVGs run through **SVGO**; icons inlined, larger illustrations externalized.
- [ ] Metadata stripped; no "quality 100"; no oversized source shipped.
- [ ] Alt text present and meaningful (empty `alt=""` only for purely decorative images).

---

## Related

- [`performance-budget.md`](./performance-budget.md) — Core Web Vitals targets and the byte budgets these images must satisfy.
- [`asset-efficiency.md`](./asset-efficiency.md) — fonts, CSS/JS, Brotli, caching that images ride alongside.
- [`../responsive/responsive-standards.md`](../responsive/responsive-standards.md) — breakpoints and responsive-image reasoning behind `sizes`.
- [`../brand/imagery.md`](../brand/imagery.md) — subject matter, treatment, and art-direction rules for photography.
- [`../brand/iconography.md`](../brand/iconography.md) — icon grid, stroke, and SVG production specs.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — breakpoints and radii referenced by image containers.
