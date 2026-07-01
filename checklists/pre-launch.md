# Pre-Launch Checklist

**Purpose:** The comprehensive launch gate for {{BRAND_NAME}}'s marketing site — one pass over performance, accessibility, SEO, structured data, legal, analytics, cross-browser/device, security, and backups that MUST be green before the site (or a major release) goes live.
**Status:** v1 foundation — adjustable.

---

> **How to use:** Copy this into your release ticket. Do not launch with any **P0 (blocker)** unchecked. **P1** items should be resolved or explicitly waived by the owner with a note. Verify on the **production URL over the real network**, on **mobile first** (Google indexes mobile). Field data (CrUX) lags ~28 days, so validate performance in the lab (Lighthouse/PSI) at launch and re-check field data ~4 weeks later.

## 0. Release gate summary (fill in)

| Gate | Owner | Status | Notes |
|---|---|---|---|
| Performance (Lighthouse >= 95, budgets met) | | ☐ | |
| Accessibility (WCAG 2.2 AA, axe 0 criticals) | | ☐ | |
| SEO (titles/desc/canonical/sitemap/robots) | | ☐ | |
| Structured data (valid, no errors) | | ☐ | |
| Legal (privacy/terms/cookies/consent) | | ☐ | |
| Analytics & conversion tracking | | ☐ | |
| Cross-browser / device | | ☐ | |
| Security (HTTPS, headers, secrets) | | ☐ | |
| Backups & rollback | | ☐ | |

---

## 1. Performance — Core Web Vitals & budgets (P0)

Targets: **LCP <= 2.5s · INP <= 200ms · CLS <= 0.1 · TTFB <= 800ms · Lighthouse Performance >= 95** (p75 field for CWV; lab at launch). See [`../docs/performance/performance-budget.md`](../docs/performance/performance-budget.md).

- [ ] **P0** Lighthouse (mobile, throttled) Performance **>= 95** on all key templates (home, service, industry, pricing, contact, blog post).
- [ ] **P0** LCP element is in the initial HTML, is the hero, and has `fetchpriority="high"`; it is **never** lazy-loaded.
- [ ] **P0** CLS: every image/video/embed/ad has explicit `width`/`height` or `aspect-ratio`; fonts use `font-display: swap`/`optional`; no layout-shifting injected banners.
- [ ] **P0** INP: no long tasks blocking interaction on hero CTAs; third-party JS deferred; main-thread tasks trimmed toward `<= 50ms`.
- [ ] **P0** Budgets met: initial JS **< 150 KB gz**, hero/LCP image **< 150 KB**, total initial transfer **< 1 MB**, CSS **< 100 KB**.
- [ ] **P1** TTFB **<= 800ms** from the primary region (cache/CDN warm, HTML cacheable where possible).
- [ ] **P1** Images shipped AVIF + WebP fallback with responsive `srcset`/`sizes`; below-fold images `loading="lazy"`.
- [ ] **P1** Fonts subset + `preload`ed (critical only); `preconnect` capped at ~4–6 origins, rest `dns-prefetch`.
- [ ] **P1** Enable HTTP caching, compression (Brotli/gzip), and HTTP/2+ or HTTP/3.
- [ ] **P1** No render-blocking third-party scripts above the fold; RUM (`web-vitals`) wired to capture field INP/LCP/CLS.

## 2. Accessibility — WCAG 2.2 AA (P0)

See [`../docs/accessibility/accessibility-standards.md`](../docs/accessibility/accessibility-standards.md). Automated tools catch ~57% of issues by volume — **manual keyboard + screen-reader passes are required.**

- [ ] **P0** axe DevTools / Lighthouse a11y: **0 critical** and 0 serious issues on every template.
- [ ] **P0** Text contrast **>= 4.5:1** (normal) / **3:1** (large); UI/graphics **>= 3:1** (1.4.11). Validate against [`../docs/accessibility/contrast-matrix.md`](../docs/accessibility/contrast-matrix.md).
- [ ] **P0** Full keyboard operability (2.1.1); no keyboard traps (2.1.2); visible focus on every interactive element (2.4.7).
- [ ] **P0** Focus is never fully hidden by sticky headers, cookie banners, or the chat widget (2.4.11 Focus Not Obscured).
- [ ] **P0** Every form control has a real programmatic `<label>` (not placeholder-only); errors are announced and not color-only (1.4.1).
- [ ] **P0** Single logical `H1` per page; headings nested without skipping levels; landmarks (`header/nav/main/footer`) present.
- [ ] **P0** All meaningful images have accurate `alt`; decorative images have `alt=""`; icon-only buttons/links have accessible names.
- [ ] **P1** Touch/click targets **>= 24×24 CSS px** (target 44×44) with **>= 8px** spacing (2.5.8).
- [ ] **P1** `prefers-reduced-motion` honored — parallax/autoplay/interaction animation disabled; carousels have pause/stop (2.2.2).
- [ ] **P1** Any drag interaction has a non-drag alternative (2.5.7); paste is NOT blocked on password/OTP fields (3.3.8).
- [ ] **P1** Screen-reader smoke test (NVDA+Firefox or VoiceOver+Safari) on nav, hero, a form, and the chat widget.
- [ ] **P1** Reflow at 320px / 400% zoom with no 2-D scroll (1.4.10); page usable with text spacing overrides (1.4.12).

## 3. SEO — technical & on-page (P0)

See [`../docs/seo/technical-seo.md`](../docs/seo/technical-seo.md) and [`../docs/seo/onsite-seo.md`](../docs/seo/onsite-seo.md).

- [ ] **P0** Unique `<title>` per page, **<= ~60 chars**, primary keyword front-loaded, brand included.
- [ ] **P0** Unique meta description per page, **<= ~155 chars**, accurate to page content.
- [ ] **P0** Self-referencing `rel=canonical` (absolute https) on every indexable page; **no conflicts** with sitemap/hreflang; never canonical to a noindex/404.
- [ ] **P0** `robots.txt` deployed at root, allows crawl of CSS/JS/images, points to the sitemap; **not** used to "hide" pages (use `noindex` meta on a crawlable page instead). See [`../public-templates/robots.txt`](../public-templates/robots.txt).
- [ ] **P0** `sitemap.xml` deployed, lists **only** canonical, 200-OK, indexable URLs with real `<lastmod>`; **<= 50,000 URLs / 50 MB** per file. See [`../public-templates/sitemap.xml`](../public-templates/sitemap.xml).
- [ ] **P0** Staging `noindex`/basic-auth **removed** from production; production is NOT accidentally blocked or `noindex`ed.
- [ ] **P0** One canonical host (e.g. `https://{{DOMAIN}}`): www vs non-www and http→https 301-redirect consistently; no mixed trailing-slash.
- [ ] **P1** OG + Twitter tags with a 1200×630 image on every page; validate the share preview. See [`../public-templates/head-meta.html`](../public-templates/head-meta.html).
- [ ] **P1** Content parity on mobile (full content, headings, links, schema render in mobile HTML).
- [ ] **P1** Descriptive internal links (no "click here"); no orphan key pages; breadcrumb present.
- [ ] **P1** 404 page is helpful and returns HTTP 404; important redirects are 301 (not 302); no redirect chains.
- [ ] **P1** Submit sitemap to Google Search Console + Bing Webmaster Tools; confirm the site is indexable in **Bing** (powers ChatGPT search).
- [ ] **P1** `llms.txt` (optional) NAP matches site/schema/GBP exactly, or is omitted. See [`../public-templates/llms.txt`](../public-templates/llms.txt).

## 4. Structured data / schema (P0)

See [`../docs/seo/structured-data.md`](../docs/seo/structured-data.md) and [`../schema/README.md`](../schema/README.md).

- [ ] **P0** `Organization` + `WebSite` JSON-LD on the homepage; `LocalBusiness` (specific subtype, not generic) with NAP that **matches** the site, `llms.txt`, and Google Business Profile.
- [ ] **P0** JSON-LD validates with **0 errors** in the [Schema.org validator](https://validator.schema.org/) and Google [Rich Results Test](https://search.google.com/test/rich-results).
- [ ] **P1** `Service` schema on service pages; `BreadcrumbList` on nested pages; `FAQPage` only where visible FAQ content exists.
- [ ] **P1** `sameAs` links to real, live social/GBP profiles; no schema for content not on the page.

## 5. Legal & compliance (P0)

See [`../docs/legal/legal-pages.md`](../docs/legal/legal-pages.md).

- [ ] **P0** Privacy Policy, Terms of Service, and Cookie Policy published, linked in the footer, and current.
- [ ] **P0** Cookie/consent banner present where required; **non-essential scripts (analytics/ads/chat) do not fire before consent**; banner does not obscure focus (2.4.11).
- [ ] **P0** Contact/booking forms disclose data use and link to the privacy policy; consent captured for SMS/marketing where applicable (e.g. TCPA/opt-in).
- [ ] **P1** Business identity in the footer: {{LEGAL_ENTITY}}, {{ADDRESS}}, {{EMAIL}}, {{PHONE}} (consistent NAP).
- [ ] **P1** Copyright year, and any required disclosures/accessibility statement, present.
- [ ] **P1** `/.well-known/security.txt` deployed with a **future** `Expires`. See [`../public-templates/security.txt`](../public-templates/security.txt).

## 6. Analytics & conversion tracking (P1)

- [ ] **P1** Analytics installed once (no duplicate tags), respects consent, and excludes internal/staging traffic.
- [ ] **P1** Primary conversions tracked as events: **book-a-call / form submit / phone-tap / chat-open**; test each fires exactly once.
- [ ] **P1** Phone (`tel:`) and email (`mailto:`) links and the chat widget verified working on mobile.
- [ ] **P1** Google Search Console + Bing verified; UTM conventions documented; goal/conversion values set.

## 7. Cross-browser & device (P1)

- [ ] **P1** Latest Chrome, Safari (macOS + iOS), Firefox, and Edge — layout, forms, and chat widget all work.
- [ ] **P1** Real iOS Safari + Android Chrome pass (not just emulators): tap targets, sticky header, safe-area insets, no horizontal scroll.
- [ ] **P1** Breakpoints 320 / 375 / 768 / 1024 / 1280 / 1536 render cleanly (see tokens `--breakpoint-*`).
- [ ] **P1** Dark mode / forced-colors (Windows High Contrast) does not break contrast or hide content.

## 8. Security (P0)

See §5 for `security.txt`.

- [ ] **P0** HTTPS everywhere; valid, non-expiring-soon TLS cert; HTTP→HTTPS 301; HSTS enabled.
- [ ] **P0** No secrets/API keys/`.env`/source maps exposed in the client bundle or repo; `.git` not web-accessible.
- [ ] **P0** No mixed content; forms submit over HTTPS to a trusted endpoint with spam/abuse protection.
- [ ] **P1** Security headers set: `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Strict-Transport-Security`, `Permissions-Policy`.
- [ ] **P1** Dependencies patched (no known critical CVEs); admin/CMS behind auth; rate-limiting on form/chat endpoints.

## 9. Backups & rollback (P0)

- [ ] **P0** A known-good backup (code + content/DB + DNS/config) exists and a **rollback path is tested**.
- [ ] **P0** DNS TTL lowered before cutover; registrar/host access confirmed; someone owns the launch window.
- [ ] **P1** Uptime + error monitoring and an SSL-expiry alert are active post-launch.
- [ ] **P1** Post-launch watch scheduled: re-check CrUX field CWV, GSC coverage, and analytics ~28 days after go-live.

---

## Related

- [`new-page.md`](./new-page.md)
- [`content-publish.md`](./content-publish.md)
- [`quality-gates.md`](./quality-gates.md)
- [`../docs/performance/performance-budget.md`](../docs/performance/performance-budget.md)
- [`../docs/accessibility/accessibility-standards.md`](../docs/accessibility/accessibility-standards.md)
- [`../docs/seo/technical-seo.md`](../docs/seo/technical-seo.md)
- [`../docs/seo/structured-data.md`](../docs/seo/structured-data.md)
- [`../docs/legal/legal-pages.md`](../docs/legal/legal-pages.md)
- [`../public-templates/head-meta.html`](../public-templates/head-meta.html)
