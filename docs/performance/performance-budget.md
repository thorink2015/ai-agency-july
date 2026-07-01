# Performance Budget

**Purpose:** The site-wide performance operating standard — the Core Web Vitals targets we hold, the hard byte/count budgets per asset class, the rendering-strategy recommendation (static-first, minimal client JS), the resource-hint and third-party-script discipline, the caching/CDN/compression baseline, and the measurement + pre-merge workflow that enforces all of it — so any developer or future Claude session ships pages that are fast for real users, not just green in a lab.
**Status:** v1 foundation — adjustable.

---

> **This is a systems/standards doc.** It defines the performance contract every page must meet. It is **not** website copy, **not** a page build, and **not** framework setup. Concrete image tactics live in [`image-optimization.md`](./image-optimization.md); font/CSS/JS/caching tactics live in [`asset-efficiency.md`](./asset-efficiency.md); this doc is the budget those two must satisfy.
>
> Reference [design tokens](../design-system/design-tokens.md) by name (`--motion-duration-base`, `--space-4`) — never raw values — except where a performance target is itself the literal (KB, ms, percentages), which is the whole point of this file.

---

## 0. TL;DR — the performance rules

- [ ] **Pass Core Web Vitals in the field (CrUX p75), not just in the lab.** All three of LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 must be "good" at the 75th percentile of real users. That is the number that affects Search and users; Lighthouse is only a diagnostic.
- [ ] **Lighthouse Performance ≥ 95** (mobile, throttled) on every template before merge.
- [ ] **Static-first rendering.** Prefer SSG (Astro, or Next in static/export mode). Ship HTML, not a framework that reconstructs HTML on the client. Hydrate only interactive islands.
- [ ] **Initial JS < 150 KB gzipped/brotli.** This is the single biggest lever for INP. Under 100 KB is the goal.
- [ ] **Total initial transfer < 1 MB** (hard target), 1.5 MB absolute ceiling. HTTP Archive median is ~2.3 MB mobile — we must be well under median.
- [ ] **The LCP element is discoverable in the initial HTML** and, if an image, marked `fetchpriority="high"` and never lazy-loaded.
- [ ] **Every image, video, embed, and ad slot reserves its space** (`width`/`height` or `aspect-ratio`). CLS regressions fail review.
- [ ] **Third-party scripts are guilty until proven innocent.** Defer them, facade them (chat widgets especially), or cut them.
- [ ] **Budgets are enforced in CI**, not by good intentions. A JS/image/weight regression fails the build before merge.

---

## 1. Core Web Vitals — the targets we hold

All three Core Web Vitals are assessed at the **75th percentile of real page loads (CrUX field data)**, segmented across mobile and desktop. A URL passes a metric only when **≥ 75% of visits** hit the "good" threshold. To "pass Core Web Vitals," **all three** must be good at p75.

| Metric | What it measures | Good | Needs improvement | Poor | Our target |
|---|---|---|---|---|---|
| **LCP** (Largest Contentful Paint) | Loading — render time of the largest in-viewport element (image, video poster, or text block) | **≤ 2.5s** | 2.5s – 4.0s | > 4.0s | **≤ 2.5s** field p75 |
| **INP** (Interaction to Next Paint) | Responsiveness — worst/near-worst interaction latency across the whole visit (input delay + processing + presentation) | **≤ 200ms** | 200ms – 500ms | > 500ms | **≤ 200ms** field p75 |
| **CLS** (Cumulative Layout Shift) | Visual stability — windowed max of unexpected layout shifts | **≤ 0.1** | 0.1 – 0.25 | > 0.25 | **≤ 0.1** field p75 |

**Diagnostic metrics we also track** (not Core Web Vitals, but they gate the ones that are):

| Metric | Good | Needs improvement | Poor | Why we care |
|---|---|---|---|---|
| **TTFB** (Time to First Byte) | **≤ 0.8s** | 0.8s – 1.8s | > 1.8s | Precedes FCP and LCP; a slow server response **directly caps** the best LCP you can achieve. |
| **FCP** (First Contentful Paint) | ≤ 1.8s | 1.8s – 3.0s | > 3.0s | First pixel of content; leading indicator for LCP. |
| **TBT** (Total Blocking Time) | < 200ms (lab) | 200ms – 600ms | > 600ms | Lighthouse's **lab proxy for INP** — Lighthouse cannot measure INP. Watch TBT to predict INP. |
| **Long task duration** | ≤ 50ms per task | — | — | Any main-thread task > 50ms blocks interaction and hurts INP. |

> **Critical facts (2026), so we don't chase myths:**
> - The **LCP "good" threshold is still 2.5s.** Several third-party blogs claim Google dropped it to 2.0s — that is false per web.dev / Search Central. Do not budget to 2.0s and panic at 2.3s.
> - **INP replaced FID** as a Core Web Vital on 2024-03-12 and remains the responsiveness metric. INP measures **all** interactions across the visit, not just the first.
> - **Lighthouse does NOT report INP.** Real INP comes only from field/RUM data. Optimizing only the lab score while ignoring CrUX is a classic mistake.
> - **CrUX is a 28-day rolling window at p75.** A fix you ship today takes ~weeks to fully reflect in Search Console / CrUX. Don't assume a fix "didn't work" because the field data hasn't moved yet — confirm in the lab and RUM first.
> - **INP is the most-failed Core Web Vital in 2026** (~43% of sites fail 200ms), almost always due to heavy JavaScript main-thread work. Ship less JS.

---

## 2. Lighthouse target and how it's scored

**Target: Performance ≥ 95** on a **mobile, throttled** run (Moto-G-class CPU 4× slowdown, slow-4G). Desktop will be higher; mobile is the gate.

Lighthouse Performance is a weighted average of five **lab** metrics:

| Metric | Weight |
|---|---|
| Total Blocking Time (TBT) | 30% |
| Largest Contentful Paint (LCP) | 25% |
| Cumulative Layout Shift (CLS) | 25% |
| First Contentful Paint (FCP) | 10% |
| Speed Index | 10% |

Bands: **0–49 red (poor), 50–89 orange (needs improvement), 90–100 green (good).** Each metric is scored on a log-normal curve, so the last few points are the hardest — a page can be "fine" at 92 and still have a real regression. Treat **95** as the floor, not the goal.

> Lighthouse is a **diagnostic tool for repeatable lab runs**. It tells you *why* something is slow. It does not tell you whether real users are having a fast experience — CrUX does that. Use both.

---

## 3. Byte & count budgets (the hard numbers)

These are **per-page, initial load, over the wire (compressed)** unless noted. Above-the-fold should account for the majority of the initial payload. Enforce in CI (§8).

| Asset class | Budget (compressed transfer) | Ceiling | Notes |
|---|---|---|---|
| **Total initial transfer** | **< 1 MB** | 1.5 MB | Everything the browser downloads for first meaningful paint + a bit. Median web page is ~2.3 MB mobile — be well under. |
| **Initial JavaScript** | **< 150 KB** | 180 KB | Compressed. Goal < 100 KB. Biggest INP lever. Parse/execute cost matters more than transfer — measure TBT too. |
| **CSS** | **< 60 KB** | 100 KB | Critical CSS inlined (§5); rest deferred. |
| **HTML document** | **< 50 KB** | 100 KB | Inlined critical CSS counts here — keep the inline block lean. |
| **Hero / LCP image** | **< 150 KB** | 200 KB | AVIF-first. Never lazy-loaded. See [`image-optimization.md`](./image-optimization.md). |
| **Any single content image** | **< 100 KB** | 150 KB | Below-the-fold, lazy-loaded. |
| **Total images (initial)** | **< 500 KB** | — | Sum of what loads before/at first viewport. |
| **Web fonts** | **≤ 2 preloaded** WOFF2, subset | — | See [`asset-efficiency.md`](./asset-efficiency.md#font-strategy) and [typography](../brand/typography.md). |
| **Third-party requests (initial)** | **≤ 3** | 5 | Analytics + consent + nothing else on first paint. Chat widget is facaded (§6). |

**Budget philosophy:** small, efficient files beat clever loading tricks. The fastest request is the one you never make. Before adding weight, ask "does this earn its bytes on a $150 Android phone on 4G?"

---

## 4. Rendering strategy — static-first

The core promise of this site (speed, competence, trust) is undermined by a slow page. The rendering strategy is chosen to make "fast" the default, not something we fight for.

**Recommendation, in priority order:**

1. **Static Site Generation (SSG).** Prefer **Astro** (ships zero JS by default; islands architecture is the model). **Next.js in static/`output: 'export'` mode** is an acceptable alternative if the team already knows Next. Pages are pre-rendered to HTML at build time and served from the CDN edge — this is what gets TTFB ≤ 0.8s essentially for free.
2. **Minimal client JS via islands.** Hydrate only the components that must be interactive (mobile nav toggle, form, FAQ accordion, chat facade). Everything else is static HTML. Do **not** hydrate the whole page.
3. **Avoid a client-side SPA** for a marketing site. A full React/Vue SPA reconstructs HTML the browser could have received for free, blows the JS budget, and makes INP a constant fight. There is no product app here — there is no reason to pay SPA costs.
4. **The LCP element must be in the server-rendered HTML.** No client-JS-inserted hero. The browser's preload scanner must be able to find the LCP image/text in the initial response.

| Approach | Verdict | Why |
|---|---|---|
| Astro / Eleventy (SSG + islands) | ✅ Preferred | Zero-JS baseline, opt-in hydration, tiny bundles |
| Next.js static export | ✅ Acceptable | Static output if team knows Next; watch the JS baseline |
| Next.js SSR / server components (edge) | ⚠️ Only if dynamic data demands it | Adds server + hydration cost; keep client components minimal |
| Client-side SPA (CRA/Vite SPA) | ❌ Avoid | Overkill for marketing; heavy JS, poor INP |
| WordPress + page builder | ❌ Avoid | Plugin/script bloat blows every budget |

---

## 5. Critical CSS & the render path

- **Inline the critical CSS** needed for above-the-fold rendering directly in `<head>` (keeps the HTML budget in §3 in mind — keep it lean, aim < 14 KB inlined).
- **Defer the rest** of the CSS (load non-critical stylesheets with a non-blocking pattern, e.g. `media="print"` swap or the framework's built-in critical-CSS extraction).
- **No render-blocking JS in `<head>`.** All scripts `defer` or `type="module"` (or loaded from the body end). See [`asset-efficiency.md`](./asset-efficiency.md).
- **Order in `<head>` matters:** resource hints first (§6), then critical CSS, then everything else. A `preload`/`preconnect` placed *after* render-blocking CSS is discovered too late to help.

---

## 6. Resource hints & priority (surgical, top of `<head>`)

Use these **surgically** and **at the very top of `<head>`** so the browser acts on them early.

| Hint | Use it for | Cap / rule |
|---|---|---|
| `preconnect` | Warm DNS + TCP + TLS to a **critical cross-origin** (e.g. self-hosted CDN, image CDN) | **≤ 4–6 origins.** More wastes sockets + CPU. |
| `dns-prefetch` | Non-critical cross-origins (near-zero cost — DNS only) | Everything beyond the preconnect cap. |
| `preload` | A **late-discovered critical** resource (critical font, LCP image that isn't in initial HTML markup as `<img>`) | Only truly critical. Over-preloading contends for bandwidth. Fonts need `crossorigin`. |
| `fetchpriority="high"` | The **LCP image** (exactly one) | > 1–2 high-priority images cancels the benefit. |
| `fetchpriority="low"` | Below-the-fold / non-critical early-DOM images | Frees bandwidth for the LCP image. |
| Speculation Rules API (`prerender`/`prefetch`) | Likely **next navigation** (e.g. Home → Pricing, Home → Contact) | Modern replacement for legacy `rel=prefetch`; makes cross-page LCP near-instant. Prerender conservatively (moderate eagerness) to avoid wasted work. |

```html
<!-- Top of <head>, before critical CSS -->
<link rel="preconnect" href="https://cdn.example.com" crossorigin>
<link rel="dns-prefetch" href="https://plausible.example.com">
<link rel="preload" as="font" type="font/woff2"
      href="/fonts/inter-var-subset.woff2" crossorigin>
<!-- LCP image is a real <img> in the HTML, prioritized: -->
<!-- <img src="/img/hero.avif" fetchpriority="high" width="1200" height="675" alt="…"> -->
```

**Third-party script discipline** (the #1 cause of blown budgets and bad INP):

- [ ] **Chat / booking widget → facade.** Render a lightweight placeholder (a styled button/bubble that matches the brand). Load the real widget's JS **only on interaction** (click) or on idle after LCP. Never let a chat widget block first paint or count against the LCP. This is doubly important for us — the product *is* AI chat, so the demo/marketing widget must not make the site feel slow.
- [ ] **Analytics → deferred, lightweight.** Prefer a privacy-light, small analytics script; load `defer` / after load. Never render-blocking.
- [ ] **Tag managers → avoid or budget hard.** A GTM container that injects N scripts is a budget black hole. If required, audit every tag against §3.
- [ ] **Every third party has an owner and a review date.** If nobody can say why a script is there, remove it.
- [ ] **Set explicit size on any third-party embed** (ads, iframes, video) to prevent CLS.

---

## 7. Server, CDN, caching & compression baseline

| Item | Standard |
|---|---|
| **Hosting** | Static files on a global **CDN/edge** (Cloudflare / Netlify / Vercel / equivalent). This is how TTFB ≤ 0.8s is achieved. |
| **Compression** | **Brotli** for text assets (HTML/CSS/JS/SVG/JSON), pre-compressed at build (level 11) where possible; gzip fallback. ~15–30% smaller than gzip. **Do not** re-compress already-compressed binaries (AVIF/WebP/WOFF2). |
| **Protocol** | HTTP/2 or HTTP/3. TLS 1.3. |
| **Hashed static assets** | `Cache-Control: public, max-age=31536000, immutable` (1 year) for fingerprinted JS/CSS/fonts/images. |
| **HTML** | `Cache-Control: no-cache` (or short max-age + revalidation) so deploys go live immediately. |
| **bfcache-friendly** | No `unload` handlers; cache headers that permit back/forward cache — gives instant back/forward navigations and improves aggregate LCP. |

Full detail in [`asset-efficiency.md`](./asset-efficiency.md#caching--compression).

---

## 8. Measurement workflow

Use **both** lab and field data — they answer different questions.

| Tool | Type | Use it for |
|---|---|---|
| **CrUX** (Chrome UX Report) / Search Console Core Web Vitals report | **Field** (real users, 28-day p75) | The source of truth for "are we passing?" Check monthly and after every significant release (allow ~28 days to fully reflect). |
| **PageSpeed Insights (PSI)** | Field (CrUX, top) + Lab (Lighthouse, bottom) | Quick per-URL check; shows both at once. |
| **Lighthouse / Lighthouse CI** | **Lab** (repeatable) | Diagnose *why* a page is slow; enforce the Performance ≥ 95 gate in CI. Uses TBT as the INP proxy. |
| **WebPageTest** | Lab (detailed) | Deep filmstrip/waterfall analysis, connection views, LCP-element attribution when Lighthouse isn't enough. |
| **RUM: `web-vitals` JS library** | **Field** (your own, per-load) | Capture **INP/LCP/CLS with attribution** from real users immediately — no 28-day delay, and detail CrUX doesn't give. **Required** because the lab cannot measure INP and CrUX is delayed. |

**Enforce in CI/CD:**

- [ ] **Lighthouse CI** with a `budget.json` (assertions on Performance score, LCP, TBT, CLS, and byte budgets from §3). A regression **fails the build**.
- [ ] **`bundlesize` / size-limit** on the JS and CSS bundles against §3.
- [ ] Run against **mobile throttling** — the desktop numbers are not the gate.

---

## 9. Pre-merge performance checklist

Run this on the affected template(s) before merging any PR that touches markup, styles, scripts, images, or dependencies.

- [ ] Lighthouse (mobile, throttled) **Performance ≥ 95**; LCP, TBT, CLS all green.
- [ ] **Initial JS < 150 KB** compressed (bundlesize passes). No new heavy dependency snuck in.
- [ ] **Total initial transfer < 1 MB.**
- [ ] **LCP element** is in the server HTML; if an image, `fetchpriority="high"`, correct `width`/`height`, **not** lazy-loaded, AVIF-first, < 150 KB.
- [ ] **No CLS from images/embeds/ads/fonts** — every one reserves space; test with the CLS overlay.
- [ ] **CSS ≤ 60 KB**, critical CSS inlined, rest deferred; no render-blocking `<script>` in `<head>`.
- [ ] **Fonts:** ≤ 2 preloaded WOFF2 subsets, `font-display: swap`, `crossorigin` on preloads. (See [typography](../brand/typography.md).)
- [ ] **Third-party scripts:** chat/booking widget is **facaded**; analytics deferred; ≤ 3 third-party requests on first paint.
- [ ] **Resource hints** are at the top of `<head>`, ≤ 4–6 preconnects, rest dns-prefetch.
- [ ] **Motion** respects `prefers-reduced-motion` (from tokens); no long-running JS animation on the main thread. See [motion](../design-system/motion.md).
- [ ] **Caching headers** correct: hashed assets immutable/1yr, HTML no-cache.
- [ ] **RUM** still reporting LCP/INP/CLS for this route (didn't break the beacon).
- [ ] No new long tasks > 50ms introduced (check the Performance panel / TBT delta).

---

## Related

- [`image-optimization.md`](./image-optimization.md) — image pipeline, formats, responsive `srcset`/`sizes`, LCP image handling.
- [`asset-efficiency.md`](./asset-efficiency.md) — fonts, CSS/JS minification & splitting, Brotli, caching headers, dependency discipline.
- [`../responsive/responsive-standards.md`](../responsive/responsive-standards.md) — responsive images, breakpoints, `sizes` reasoning.
- [`../brand/typography.md`](../brand/typography.md) — font families, weights, `font-display`.
- [`../design-system/motion.md`](../design-system/motion.md) — motion durations, `prefers-reduced-motion` gating.
- [`../design-system/design-tokens.md`](../design-system/design-tokens.md) — token names to consume.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — source of truth for all design values.
