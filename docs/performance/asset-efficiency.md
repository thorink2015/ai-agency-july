# Asset Efficiency

**Purpose:** The efficiency standard for everything that isn't an image — fonts, CSS, and JavaScript — plus the delivery layer that carries them: minification, code-splitting and tree-shaking, Brotli/gzip compression, HTTP caching with immutable hashed filenames, dependency discipline, layout-shift avoidance, and prefetching. The through-line is one rule: **ship small, efficient files, and cache them aggressively.** Everything here exists to keep pages inside the budgets in [`performance-budget.md`](./performance-budget.md).
**Status:** v1 foundation — adjustable.

---

> **This is a systems/standards doc.** It sets how non-image assets are built and delivered. Byte budgets come from [`performance-budget.md`](./performance-budget.md); image handling lives in [`image-optimization.md`](./image-optimization.md); font *design* choices (families, weights) live in [typography](../brand/typography.md) — this doc covers how fonts are *loaded*. Reference [tokens](../design-system/design-tokens.md) by name; raw KB/ms numbers appear because they are the standard.

---

## 0. TL;DR — the efficiency rules

- [ ] **Small, efficient files win.** The fastest request is the one you never make; the second fastest is a tiny, cached one.
- [ ] **Self-host fonts as subsetted WOFF2.** ≤ 2 preloaded, `font-display: swap`, `crossorigin` on the preload.
- [ ] **Minify everything** (HTML/CSS/JS/SVG) and **pre-compress with Brotli** (level 11) at build; gzip fallback.
- [ ] **Tree-shake and code-split.** Ship only the JS a page uses; `import()` non-critical/interaction-triggered code.
- [ ] **Fingerprint static assets** (content hash in filename) → `Cache-Control: public, max-age=31536000, immutable`. HTML stays `no-cache`.
- [ ] **Audit every dependency.** A 40 KB library for one helper is a regression. Prefer platform features and small, focused packages.
- [ ] **Reserve space for everything** (fonts, embeds, dynamic content) so nothing shifts. See [`image-optimization.md`](./image-optimization.md#4-preventing-image-cls--always-reserve-space) for the image side.
- [ ] **Prefetch/prerender likely next navigations** with the Speculation Rules API; don't over-eagerly fetch.

---

## 1. Font strategy

Fonts are render-affecting and easy to get wrong. The families and weights are defined in [typography](../brand/typography.md); this is the **loading** contract. The site uses **Sora** (display, variable), **Inter** (body, variable), and optionally **JetBrains Mono**.

**Rules:**
- [ ] **Self-host.** Do **not** hotlink Google Fonts' CDN — self-hosting is faster (one fewer origin) and is the GDPR-safe choice (Munich ruling). If a CDN is required, use an EU-hosted compliant one (Bunny Fonts `fonts.bunny.net`, Fontsource, Coollabs).
- [ ] **WOFF2 only.** ~30% smaller than WOFF. **Do not** ship TTF/OTF/WOFF/EOT.
- [ ] **Subset** to the character set you actually use (Latin + needed punctuation). Subsetting is often the single biggest font win.
- [ ] **Variable font only when using 3+ weights/axes.** Below that, a subset **static** WOFF2 for the one or two weights is usually *smaller* — don't assume variable is always smaller. Inter/Sora across headings + body + UI generally justify variable; verify byte size.
- [ ] **`font-display: swap`** always. Text shows immediately in the fallback (~100ms block period), then swaps to the webfont. **Never** `font-display: block`/default FOIT (hides text — bad UX/SEO/a11y).
- [ ] **Preload the critical fonts only** (the weight(s) used above the fold), **≤ 2**, with **`crossorigin`** — fonts fetch in CORS mode even same-origin, and **omitting `crossorigin` causes a double fetch** (the preload is discarded).
- [ ] **Inline the critical `@font-face` + font CSS** in `<head>` for earliest discovery.
- [ ] **Match fallback metrics** to reduce swap shift: define fallbacks with `size-adjust` / `ascent-override` / `descent-override` (or use the framework's automatic fallback, e.g. `next/font`, Fontsource). The token stack already names `'Inter Fallback'` / `'Sora Fallback'` for this.

```html
<!-- In <head>, top, with crossorigin -->
<link rel="preload" as="font" type="font/woff2"
      href="/fonts/inter-var-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2"
      href="/fonts/sora-var-latin.woff2" crossorigin>
```
```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter-var-latin.woff2') format('woff2');
  font-weight: 400 700;      /* variable range */
  font-display: swap;
  font-style: normal;
}
```

---

## 2. CSS efficiency

- [ ] **Minify** (strip whitespace/comments; merge rules) in the production build.
- [ ] **Inline critical CSS** in `<head>` (above-the-fold styles, aim < 14 KB inlined); **defer the rest**. See [`performance-budget.md`](./performance-budget.md#5-critical-css--the-render-path).
- [ ] **Remove unused CSS.** Purge/tree-shake unused selectors (e.g. Tailwind's content-based purge, or PurgeCSS). Ship the CSS a page uses, not a global kitchen sink.
- [ ] **Keep specificity flat and reuse tokens** — bloated, duplicative CSS is both bigger and harder to cache-bust cleanly. Consume the [design tokens](../design-system/design-tokens.md) rather than redefining values.
- [ ] **Budget: CSS < 60 KB** compressed (100 KB ceiling), per [`performance-budget.md`](./performance-budget.md).
- [ ] Avoid `@import` in CSS (serial round-trips); bundle instead.

---

## 3. JavaScript efficiency

JS is the top cause of poor INP (~43% of sites fail 200ms, mostly from JS). Treat every kilobyte of JS as a liability.

- [ ] **Minify** and **tree-shake** (ES modules + a bundler that drops dead code). Ensure dependencies are ESM and side-effect-free (`"sideEffects": false` where true) so tree-shaking works.
- [ ] **Code-split by route/component.** Don't ship one mega-bundle; ship per-page chunks.
- [ ] **Lazy-load non-critical JS with dynamic `import()`** — load it on interaction or when idle after LCP, not up front. This is exactly how the **chat/booking widget facade** works (see [`performance-budget.md`](./performance-budget.md#6-resource-hints--priority-surgical-top-of-head)).
- [ ] **`defer` or `type="module"`** all scripts; nothing render-blocking in `<head>`.
- [ ] **Minimize hydration.** Static-first + islands (Astro) hydrate only what must be interactive. Full-page hydration is the enemy of INP.
- [ ] **Break up long tasks** (> 50ms). Yield to the main thread (`scheduler.yield()` / `setTimeout` / `isInputPending`), chunk heavy work, and keep individual tasks short so interactions stay responsive.
- [ ] **Budget: initial JS < 150 KB** compressed (goal < 100 KB). Parse/execute cost matters as much as transfer — watch **TBT** (Lighthouse's INP proxy).
- [ ] **Enforce with `bundlesize`/size-limit + Lighthouse CI** so a JS regression fails the build.

---

## 4. Reducing dependencies

Every dependency is code you didn't write, must download, parse, execute, and keep secure.

- **Question every package.** A whole date/utility library for one function is a regression — use the one function or a platform API.
- **Prefer platform features** (`fetch`, `Intl`, `URL`, `structuredClone`, CSS `:has()`/container queries, native lazy-loading, `<dialog>`, form validation) over libraries that reimplement them.
- **Prefer small, focused, ESM, tree-shakeable packages** over monoliths.
- **Check the real cost before adding** (bundlephobia-style size + whether it tree-shakes). Watch transitive dependencies.
- **Delete on sight** anything unused. Audit `package.json` and third-party scripts periodically.
- **No jQuery / no heavy UI framework for a marketing site** — the platform + a few KB of vanilla or a tiny islands runtime is enough.

---

## 5. Compression — Brotli / gzip

| Setting | Standard |
|---|---|
| **Text assets** (HTML/CSS/JS/SVG/JSON/`.map`) | **Brotli**, pre-compressed at **level 11** at build time where the host serves static `.br` files; **gzip** as fallback for clients that don't accept Brotli. Brotli is ~15–30% (up to ~25%) smaller than gzip. |
| **Dynamic responses** | Brotli level ~4–6 (11 is too slow per-request). |
| **Already-compressed binaries** (AVIF/WebP/PNG/JPEG/WOFF2/`.mp4`) | **Do not re-compress** — no gain, wasted CPU. Serve as-is. |

Serve over **HTTP/2 or HTTP/3, TLS 1.3.** Pre-compressing at build (not per-request) gives you level-11 Brotli for free on every hit.

---

## 6. Caching & HTTP headers

The rule: **fingerprint immutable assets and cache them for a year; keep HTML fresh.**

| Asset | Filename | `Cache-Control` |
|---|---|---|
| **Hashed JS/CSS/fonts/images** (content hash in name, e.g. `app.9f3a2b.js`) | fingerprinted | `public, max-age=31536000, immutable` (1 year) |
| **HTML documents** | not hashed | `no-cache` (or short `max-age` + `must-revalidate`) so deploys go live instantly |
| **`robots.txt` / `sitemap.xml` / `llms.txt`** | fixed | short `max-age` (e.g. 1 hour–1 day) |
| **Service-worker file** (if any) | fixed | `no-cache` |

Why it works: a **content hash in the filename** means the URL changes whenever the bytes change, so `immutable` + 1-year caching is safe — returning visitors and cross-page navigations pay **zero** bytes for unchanged assets, while a new deploy is picked up because the HTML (uncached) points at new hashed URLs.

**Also:**
- [ ] **bfcache-friendly:** no `unload` handlers; avoid `Cache-Control: no-store` on the document where possible — enables instant back/forward navigation.
- [ ] Set caching/compression at the **CDN/edge** (see [`performance-budget.md`](./performance-budget.md#7-server-cdn-caching--compression-baseline)).
- [ ] Add a long-cache `Vary: Accept` only where content negotiation (e.g. image CDN) requires it.

---

## 7. Avoiding layout shift (non-image sources)

Images/embeds are covered in [`image-optimization.md`](./image-optimization.md#4-preventing-image-cls--always-reserve-space). The rest:

- [ ] **Fonts:** `font-display: swap` + metric-matched fallbacks (§1) to minimize the swap reflow.
- [ ] **Reserve space for anything injected late** — banners, cookie consent, embeds, ads, "loaded" states: give the container a fixed `min-height`/`aspect-ratio` so filling it doesn't push content.
- [ ] **Never insert content above existing content** after load (except in response to a user interaction).
- [ ] **Skeletons/placeholders** must occupy the **same box** the real content will.
- [ ] **Animate only `transform`/`opacity`** (compositor-only) — animating layout properties (`width`, `top`, `margin`) causes reflow and can shift neighbors. Respect `prefers-reduced-motion` (see [motion](../design-system/motion.md)).
- [ ] Target CLS ≤ 0.1 (field p75) per [`performance-budget.md`](./performance-budget.md).

---

## 8. Prefetching & speculative loading

- **Speculation Rules API (`prerender`/`prefetch`)** is the modern way to make the *next* navigation near-instant (Home → Pricing, Home → Contact/Book). Use **moderate/conservative eagerness** so you don't prerender pages the user never visits (wasted CPU/bytes).
- **`rel="prefetch"`** for a specific known next document is acceptable where Speculation Rules aren't available.
- **Don't over-prefetch.** Speculative loading trades bandwidth for speed; on a marketing site prefetch only high-probability paths.
- **`preload`/`preconnect`/`fetchpriority`** are covered in [`performance-budget.md`](./performance-budget.md#6-resource-hints--priority-surgical-top-of-head) — keep them surgical and at the top of `<head>`.

```html
<script type="speculationrules">
{
  "prerender": [{
    "where": { "href_matches": "/pricing" },
    "eagerness": "moderate"
  }]
}
</script>
```

---

## 9. File-size budget table (by asset type)

Compressed transfer, per page, initial load. Mirrors [`performance-budget.md`](./performance-budget.md) §3 — enforce in CI.

| Asset type | Target | Ceiling |
|---|---|---|
| **HTML document** (incl. inlined critical CSS) | < 50 KB | 100 KB |
| **CSS** (total) | < 60 KB | 100 KB |
| **Initial JavaScript** | < 150 KB | 180 KB |
| **Each web font** (subset WOFF2) | < 30 KB | 50 KB |
| **Web fonts preloaded** | ≤ 2 | — |
| **Hero / LCP image** | < 150 KB | 200 KB |
| **Each content image** | < 100 KB | 150 KB |
| **Each SVG icon** | < 2 KB | 5 KB |
| **Third-party requests (initial)** | ≤ 3 | 5 |
| **Total initial transfer** | **< 1 MB** | 1.5 MB |

---

## 10. Pre-merge asset checklist

- [ ] Fonts: self-hosted **WOFF2, subset**, ≤ 2 preloaded with **`crossorigin`**, `font-display: swap`, metric-matched fallback.
- [ ] CSS minified, critical inlined + rest deferred, unused purged, **< 60 KB**.
- [ ] JS minified + **tree-shaken** + **code-split**; non-critical `import()`-deferred; all `defer`/`module`; **< 150 KB** initial; no new long tasks > 50ms.
- [ ] No unjustified new dependency; platform features preferred; transitive cost checked.
- [ ] **Brotli** (build-time, level 11) + gzip fallback; binaries not re-compressed.
- [ ] Hashed assets → `max-age=31536000, immutable`; HTML `no-cache`; bfcache not broken.
- [ ] No non-image layout shift: fonts, embeds, injected banners, skeletons all reserve space; animations use `transform`/`opacity` only.
- [ ] Prefetch/prerender only high-probability next navigations, conservatively.
- [ ] All types within the §9 budget table; **total initial < 1 MB**.

---

## Related

- [`performance-budget.md`](./performance-budget.md) — Core Web Vitals targets, budgets, rendering strategy, resource hints, CDN/compression baseline, CI enforcement.
- [`image-optimization.md`](./image-optimization.md) — image formats, responsive `srcset`/`sizes`, LCP handling, image CLS.
- [`../brand/typography.md`](../brand/typography.md) — font families, weights, and `font-display` design decisions.
- [`../design-system/motion.md`](../design-system/motion.md) — motion durations, easing, `prefers-reduced-motion` gating.
- [`../design-system/design-tokens.md`](../design-system/design-tokens.md) — token names to consume in CSS.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — source of truth for all design values.
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — the CSS custom properties to reference.
