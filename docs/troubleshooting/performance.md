# Performance Troubleshooting Playbook

**Purpose:** Symptom-driven diagnosis and repair for the {{BRAND_NAME}} site's speed problems — slow LCP, high INP, layout shift (CLS), oversized JS bundles, slow TTFB, heavy images, render-blocking resources, and third-party/chat-widget drag — each as `Symptom → Likely cause → Diagnosis → Fix → Prevention` so any developer or future Claude session can restore Core Web Vitals to "good" at the field p75.
**Status:** v1 foundation — adjustable.

---

> **This diagnoses deviations from the standard.** The targets, budgets, and build-it-right rules live in [`../performance/performance-budget.md`](../performance/performance-budget.md), [`../performance/image-optimization.md`](../performance/image-optimization.md), and [`../performance/asset-efficiency.md`](../performance/asset-efficiency.md). This file is what you open when a number goes red.
>
> Reference tokens (`--motion-duration-base`) by name; literal KB/ms/ratios are diagnostic thresholds and stay literal.

---

## 0. TL;DR — performance triage in one screen

- [ ] **Split lab vs field first.** PageSpeed Insights shows both. Field (CrUX, p75, 28-day rolling) is what Search and users experience; lab (Lighthouse) is for diagnosis. **Lighthouse cannot measure INP** — it reports TBT as a proxy. Real INP only comes from field/RUM.
- [ ] **Fix in this order of leverage:** LCP element discoverability → render-blocking → images → JS/INP → third-party → CLS reservations.
- [ ] **Change one thing, re-measure.** CrUX lags ~28 days, so validate the *lab* improvement immediately, then watch the field over weeks.
- [ ] **The LCP image is never lazy-loaded and never deferred** — it is eager + `fetchpriority="high"`.
- [ ] **Third-party scripts are guilty until proven innocent** — the chat widget is usually the biggest offender.

### Thresholds you're diagnosing against

| Metric | Good | Needs improvement | Poor |
|---|---|---|---|
| **LCP** | ≤ 2.5s | 2.5–4.0s | > 4.0s |
| **INP** | ≤ 200ms | 200–500ms | > 500ms |
| **CLS** | ≤ 0.1 | 0.1–0.25 | > 0.25 |
| **TTFB** (diagnostic) | ≤ 800ms | 800–1800ms | > 1800ms |
| **FCP** (diagnostic) | ≤ 1.8s | 1.8–3.0s | > 3.0s |
| **Long task** (main thread) | ≤ 50ms | — | > 50ms |

---

## 1. Slow LCP (Largest Contentful Paint > 2.5s)

**First step every time:** in Chrome DevTools → **Performance** panel, record a load; the LCP marker names the LCP element. In Lighthouse, "Largest Contentful Paint element" is listed under diagnostics. Identify *what* the LCP element is before touching anything.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| LCP element is an image loading late | Image not discoverable in initial HTML (injected by JS/CSS `background`), or lazy-loaded | DevTools Network: is the LCP image request started late / after JS? Lighthouse warns "Largest Contentful Paint image was lazily loaded." | Put the LCP image in the initial HTML as `<img>` with `fetchpriority="high"`, `loading="eager"` (remove any `loading="lazy"`), explicit `width`/`height`. Optionally add `<link rel="preload" as="image" imagesrcset=… imagesizes=…>` at top of `<head>`. | CI/lint rule: LCP/hero images must not carry `loading="lazy"`; require `fetchpriority="high"` on the hero. Manual check in template review. |
| LCP is a text block, still slow | Render-blocking CSS/JS or slow font delaying first paint | Lighthouse "Eliminate render-blocking resources"; Coverage panel shows unused CSS. | Inline critical CSS, defer the rest; `font-display: swap`; preload the one critical font (see §7). | Critical-CSS step in build; budget on render-blocking bytes. |
| LCP good on desktop, poor on mobile | Larger image served to mobile, or CPU-bound render on mid-tier device | PSI mobile tab; DevTools CPU throttle 4×, "Slow 4G". | Serve responsive `srcset`/`sizes` so phones get a small variant; reduce main-thread work before paint. | Test every template at 4× CPU + Slow 4G before merge. |
| TTFB is high, so LCP can never be good | Slow server/origin (see §5) — TTFB directly caps LCP | PSI field TTFB; `curl -w "%{time_starttransfer}\n" -o /dev/null -s <url>`. | Fix TTFB first (caching, CDN, static rendering) — see §5. | TTFB alert in RUM; static-first rendering. |
| LCP regressed after a content change | New hero media larger, or a new script now blocks | Compare Lighthouse traces before/after; diff the deploy. | Re-optimize the new asset; move the new script to `defer`/facade. | Lighthouse CI budget fails the PR on LCP regression. |

**Highest-leverage LCP win:** make the LCP element discoverable in the raw HTML and give the LCP image `fetchpriority="high"`. Google's own example moved 2.6s → 1.9s this way.

---

## 2. High INP (Interaction to Next Paint > 200ms)

INP is the most commonly failed CWV in 2026 (~43% of sites fail) and almost always a **main-thread JavaScript** problem. **Lighthouse can't measure it** — you need RUM.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Field INP > 200ms, unknown interaction | Heavy JS handlers / long tasks blocking the main thread | web-vitals RUM with attribution (`onINP`) to log the target element + phase (input delay / processing / presentation). DevTools Performance: interaction track shows the long task. | Break up long tasks: `await scheduler.yield()` (fallback `setTimeout`) between chunks; debounce input handlers; move heavy work to a Web Worker or defer it. | RUM alert on INP p75 > 200ms; keep tasks ≤ 50ms — flag long tasks in CI perf trace. |
| Taps/clicks feel laggy on mobile | Too much JS parse/execute on hydration | DevTools "Total Blocking Time"; Coverage shows unused JS. | Cut/split JS; ship less; static-first, hydrate only interactive islands. | Initial JS budget < 150KB gz (target < 100KB) enforced in CI. |
| Jank when a third-party script runs | Chat/analytics/tag manager executing on the main thread | Performance panel: attribute long tasks to the third-party origin. | Facade the widget (load on interaction), defer analytics, audit tag manager (see §8). | Third-party JS allowlist + facade pattern required for chat/video embeds. |
| INP spikes on a specific component | Expensive re-render / layout thrash in a handler | Performance panel "Recalculate Style / Layout" during the interaction. | Batch DOM reads/writes; avoid forced synchronous layout; virtualize long lists. | Component perf review; avoid layout in scroll/input handlers. |
| INP fine in lab, bad in field | Lab has no real interactions; TBT proxy hid it | Confirm via RUM, not Lighthouse. | Optimize based on RUM attribution, not the lab score. | Adopt RUM; never sign off INP from Lighthouse alone. |

---

## 3. Layout shift (CLS > 0.1)

CLS is almost always **unreserved space**. DevTools → **Rendering** panel → check "Layout Shift Regions" to see shifts flash on screen; the Performance panel lists each shift with the culprit node.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Content jumps as images load | Missing `width`/`height` or `aspect-ratio` on `<img>`/`<video>`/embed | Layout Shift Regions highlights the image; Lighthouse "Image elements do not have explicit width and height." | Set explicit `width`/`height` (or CSS `aspect-ratio`); add CSS `img{height:auto;max-width:100%}`. Never `width:auto`. All `srcset` variants share one aspect ratio. | Lint: every `<img>` needs width+height; CI CLS budget ≤ 0.1. |
| Shift when web font swaps in | Fallback → webfont metrics differ (FOUT reflow) | Rendering panel shift on font load; compare fallback vs webfont metrics. | Use `size-adjust`/`ascent-override` on `@font-face` to match fallback metrics; `font-display: swap`; preload the critical font. | Font-metric override checklist; preload critical font. |
| Banner/cookie/ad pushes content down | Dynamically injected element with no reserved space | Layout Shift Regions when the element appears. | Reserve its height with a min-height placeholder; render sticky/overlay instead of inserting into flow. | Reserve space for all late-injected UI (banners, ad slots, embeds). |
| Shift on interaction (accordion, tab) | Expected shift counted because it wasn't user-initiated within 500ms | Performance panel: was it within the user-interaction window? | Ensure the shift is a direct result of user input (it's then excluded); avoid async content arriving > 500ms after click. | Design components to reserve their expanded space or animate height, not jump. |
| CLS good on desktop, bad on mobile | Ad/embed reflow only at mobile widths | PSI mobile; test at 360px width. | Reserve space per breakpoint; test narrow viewports. | Include 360px in the CLS test matrix. |

---

## 4. Large JS bundles / heavy assets

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Initial JS > 150KB gz | Shipping a full framework / unused deps / no code-split | Bundle analyzer (source-map-explorer, `@next/bundle-analyzer`); Coverage shows unused JS. | Code-split, dynamic `import()` below-fold, tree-shake, drop heavy deps (moment→date-fns, etc.), static-first render. | `bundlesize`/Lighthouse-CI JS budget fails the build. |
| A single dependency is huge | One library dominates the bundle | Analyzer flags the largest module. | Replace with a lighter alternative or import only the needed submodule. | PR check on bundle diff; approve new deps deliberately. |
| Same code loads on every page | No route-level splitting | Analyzer: shared chunk contains route-specific code. | Split per route; lazy-load non-critical features. | Route-based splitting in build config. |
| Total transfer > 1MB initial | Combined images + JS + fonts over budget | WebPageTest/DevTools "Transferred" total. | Trim the largest offenders per §1/§4/§6; enforce budgets. | `budget.json` in CI: total < 1MB target, < 1.5MB ceiling. |
| Text assets not compressed | Missing Brotli/Gzip on HTML/CSS/JS | `curl -H "Accept-Encoding: br,gzip" -I <url>` — check `content-encoding`. | Enable Brotli (level 11 static) + Gzip fallback at the CDN/server. | Compression check in deploy smoke test. |

---

## 5. Slow TTFB (Time to First Byte > 800ms)

TTFB is diagnostic, not a CWV — but it **directly caps LCP**. If TTFB is 1.5s, LCP can never be "good."

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| TTFB > 800ms on HTML | Server-side rendering per request / slow origin | `curl -w "TTFB %{time_starttransfer}s\n" -o /dev/null -s <url>`; host response-time logs. | Move to static generation (SSG) + CDN edge caching; cache HTML at the edge where possible. | Static-first rendering; TTFB alert in RUM. |
| TTFB high only far from origin | No CDN / single-region origin | Test TTFB from multiple regions (WebPageTest locations). | Put static assets and, ideally, HTML on a global CDN. | CDN required for all environments. |
| TTFB spikes under load | Origin cold starts / DB bottleneck / no cache hits | Host metrics: cache hit ratio, cold-start count, DB timing. | Increase cache TTL for static; warm functions; optimize/queries; add edge cache. | Load-test before launch; monitor cache hit ratio. |
| First request slow, rest fast | Serverless/function cold start | Compare first vs warm request TTFB. | Prefer static; if dynamic, keep functions warm / use edge runtime. | Prefer static routes; minimize dynamic endpoints. |
| TTFB fine locally, slow in prod | Missing edge cache config on the host | Check host cache headers on the HTML response. | Set correct `Cache-Control` for static HTML; enable the host's edge cache. | Cache-header check in deploy smoke test. |

---

## 6. Heavy / unoptimized images

Owning doc: [`../performance/image-optimization.md`](../performance/image-optimization.md).

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Hero image > 200KB | Legacy format (JPEG/PNG) or over-quality | DevTools Network: size + type of the LCP image. | Serve AVIF (q60–80) first, WebP (q75–85) fallback via `<picture>`; keep hero < 200KB. | Build pipeline emits AVIF+WebP; image budget in CI. |
| Same big image on all devices | No responsive `srcset`/`sizes` | Network shows the same large file on mobile. | Add `srcset` with 3–5 width variants + a real `sizes`; cap ~2560px. Without `sizes` the browser grabs the largest. | Lint: responsive images require `sizes`. |
| Below-fold images slow the page | Not lazy-loaded | Network: below-fold images fetched eagerly. | `loading="lazy" decoding="async"` on below-fold images (never the LCP one); `fetchpriority="low"` for early non-critical images. | Lazy-load default for below-fold; LCP exclusion enforced. |
| Content images > 100KB each | Unoptimized exports | Network sizes; image CDN report. | Re-encode AVIF/WebP; correct dimensions; strip metadata. | Content image budget < 100KB; total images < ~500KB. |
| SVG icons bloat HTML | Un-minified inline SVG / large illustrations inlined | View source size of inline SVGs. | Run SVGO (`removeViewBox:false`, `multipass`, floatPrecision 2 icons / 3 illustrations); inline only < ~5KB, externalize larger for caching. | SVGO in CI with committed `svgo.config.js`. |
| Font fetched twice | Missing `crossorigin` on font preload | Network shows two requests for one font. | Add `crossorigin` to `<link rel="preload" as="font">` (fonts load in CORS mode even same-origin). | Preload lint checks `crossorigin` on `as="font"`. |

---

## 7. Render-blocking resources

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| FCP/LCP delayed by CSS | Large blocking stylesheet in `<head>` | Lighthouse "Eliminate render-blocking resources"; Coverage shows unused CSS. | Inline critical CSS, load the rest with a non-blocking pattern; purge unused CSS. | Critical-CSS build step; CSS budget < 100KB. |
| FCP delayed by a `<script>` in head | Synchronous script blocking parse | Network waterfall: script blocks before first paint. | Add `defer` (or `async` if independent); move non-critical JS to end/idle. | Lint: no blocking `<script>` in `<head>` without defer/async. |
| Resource hints not helping | `preconnect`/`preload` placed after blocking CSS/JS, discovered too late | Check `<head>` order — hints must be at the very top. | Move `preconnect`/`preload` to the top of `<head>`, before stylesheets. | Head-order lint / template review. |
| Too many preconnects | 10+ `preconnect` origins wasting sockets/CPU | Count `preconnect` links. | Cap at ~4–6 critical origins; demote the rest to `dns-prefetch`. | Preconnect cap enforced in review. |
| Slow next-page navigation | No speculative loading | Field LCP high on internal navigations. | Adopt Speculation Rules API (`prerender`/`prefetch`) for likely next pages; use bfcache-friendly patterns (no `unload` handlers). | Speculation rules for primary nav paths; audit for `unload` handlers. |

---

## 8. Third-party / chat-widget slowness

The AI chat/booking widget is core to the product **and** the most likely performance offender. Load it without wrecking CWV.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Chat widget adds seconds to load | Widget script loads eagerly on every page, blocking main thread | Performance panel: long tasks attributed to the widget origin; Network: widget JS in the critical path. | **Facade pattern:** render a lightweight fake button; load the real widget only on click/hover or after `requestIdleCallback`. Load `async`/`defer`. | Facade required for chat/booking embeds; widget excluded from critical path. |
| INP spikes when widget initializes | Heavy widget hydration on the main thread | Attribute the long task to the widget in RUM/Performance. | Delay init until idle or first interaction; sandbox in an iframe if the vendor supports it. | Init-on-interaction pattern; measure INP with widget present. |
| Analytics/tag manager slows everything | Tag manager loading many tags synchronously | Performance panel: GTM/analytics long tasks; Network count. | Load analytics `async`, defer non-essential tags, prune the tag container, respect consent gating (see [`forms-and-integrations.md`](./forms-and-integrations.md)). | Tag audit; consent-gated + deferred loading. |
| CLS when widget button appears | Widget injects a floating button with no reserved space | Layout Shift Regions when widget mounts. | Position `fixed`/overlay so it doesn't reflow content; reserve space if inline. | Overlay-only widget placement. |
| Third-party is slow and you can't fix it | Vendor server latency out of your control | Network timing on the third-party request. | Facade + lazy so it never blocks first load; set a timeout/fallback; consider a lighter vendor. | Budget third-party weight; review vendor perf before adopting. |
| Multiple third parties compound | Chat + booking + analytics + pixels all eager | Count third-party requests and bytes in DevTools. | Prioritize: only the widget the user needs on that page; facade the rest. | Per-page third-party allowlist. |

---

## 9. Post-fix verification checklist

- [ ] Reproduced the symptom and identified **one** root cause before changing code.
- [ ] Re-ran **Lighthouse (mobile, throttled)** — target ≥ 95, and the specific lab metric improved.
- [ ] For INP, validated against **RUM/field**, not Lighthouse (which can't measure it).
- [ ] Confirmed no regression in the other CWV (fixing LCP shouldn't add CLS, etc.).
- [ ] Added or confirmed the **prevention guardrail** (CI budget / lint / RUM alert).
- [ ] Noted that **field CrUX data lags ~28 days** — the win won't show in Search Console immediately.

---

## Related

- [`README.md`](./README.md) — playbook index, triage, and severity model.
- [`../performance/performance-budget.md`](../performance/performance-budget.md) — the CWV targets and byte budgets this playbook defends.
- [`../performance/image-optimization.md`](../performance/image-optimization.md) — image format/responsive/lazy tactics.
- [`../performance/asset-efficiency.md`](../performance/asset-efficiency.md) — font/CSS/JS/caching/compression tactics.
- [`seo-indexing.md`](./seo-indexing.md) — CWV as a Search page-experience signal.
- [`forms-and-integrations.md`](./forms-and-integrations.md) — chat/booking widget and analytics loading.
- [`build-deploy.md`](./build-deploy.md) — CDN, caching, and compression at the deploy layer.
