# Technical SEO

**Purpose:** The prescriptive crawlability, indexing, and page-experience rules for the {{BRAND_NAME}} site — robots.txt, XML sitemaps, canonicals, pagination, redirects, 404s, HTTPS, trailing-slash consistency, hreflang, mobile-first, page experience, and Search Console monitoring — so the right pages get crawled, indexed, and rendered correctly.
**Status:** v1 foundation — adjustable.

---

> **On-page rules** (titles, meta, headings, links, alt) live in [`onsite-seo.md`](./onsite-seo.md). **Structured data (JSON-LD)** lives in `structured-data.md`. **Strategy/architecture** lives in [`seo-strategy.md`](./seo-strategy.md). This doc is the technical/indexing layer only.
> **Templates:** [`../../public-templates/robots.txt`](../../public-templates/robots.txt) and [`../../public-templates/sitemap.xml`](../../public-templates/sitemap.xml) implement the rules below — keep them in sync with this doc.

---

## 0. TL;DR — technical rules in one screen

- [ ] **HTTPS everywhere**, HSTS, one canonical host (pick `www` or apex, 301 the other).
- [ ] **One trailing-slash style sitewide**; 301 the other form; canonicals + sitemap + internal links all use it.
- [ ] **robots.txt allows crawling**; never use `Disallow` for index control (use `noindex` on a crawlable page). Points to the sitemap. Keep < 500 KiB. **Don't block CSS/JS/images.**
- [ ] **XML sitemap(s)** list only canonical, indexable, 200 URLs with real `<lastmod>`; ≤ 50,000 URLs / 50 MB per file; use a **sitemap index** beyond that.
- [ ] **Self-referencing `rel=canonical`** (absolute, in `<head>`) on every indexable page; never canonicalize to a noindex/404/redirect; keep canonical = sitemap = internal links.
- [ ] **301** for permanent moves; fix redirect chains/loops; custom **404** returns real `404`; avoid **soft-404s**.
- [ ] **Mobile-first**: Google indexes the mobile render — full content/headings/links/schema present on mobile (indexing complete since July 2024).
- [ ] **Page experience** = tiebreaker: pass Core Web Vitals at p75, but content/E-E-A-T dominate.
- [ ] **hreflang** only if multi-language: reciprocal, valid codes, `x-default`, consistent with canonicals.
- [ ] **Monitor** in Google Search Console (coverage, sitemaps, CWV, enhancements). Field data lags ~28 days.

---

## 1. HTTPS & canonical host

- [ ] **HTTPS on every URL**; redirect all HTTP → HTTPS with **301**.
- [ ] Enable **HSTS** (`Strict-Transport-Security`) once HTTPS is stable.
- [ ] Pick **one canonical host** — `https://{{DOMAIN}}/` (apex) **or** `https://www.{{DOMAIN}}/` — and **301** the other to it. Don't serve both 200.
- [ ] All internal links, canonicals, sitemap `<loc>`, and OG `og:url` use the **chosen host + scheme** exactly.
- [ ] No mixed content (all sub-resources over HTTPS).

---

## 2. Trailing-slash consistency

Inconsistent trailing slashes create duplicate URLs and split signals. Pick one and enforce it everywhere.

- [ ] Choose **one** style sitewide: `/{{path}}/` (with slash) **or** `/{{path}}` (without). (This foundation assumes **with-slash** for directory-style pages; keep it consistent.)
- [ ] **301** the non-preferred form to the preferred (`/services` → `/services/` or vice-versa).
- [ ] Canonicals, sitemap, internal links, and redirects all use the **same** form.
- [ ] The homepage is the single exception (`https://{{DOMAIN}}/`).

---

## 3. robots.txt strategy

Implemented in [`../../public-templates/robots.txt`](../../public-templates/robots.txt).

| Rule | Detail |
| --- | --- |
| **Allow crawling by default** | `User-agent: *` / `Allow: /` |
| **Never use `Disallow` for index control** | A Disallowed URL can still be **indexed without a snippet**. To de-index, keep the page crawlable and add `noindex` (§7). |
| **Don't block render resources** | Never disallow CSS/JS/images — Google needs them to render the mobile page. |
| **Only block true crawl traps** | Infinite faceted params, cart/checkout/account, internal search — and only if they're not pages you want ranked. |
| **Point to the sitemap** | `Sitemap: https://{{DOMAIN}}/sitemap.xml` (absolute, canonical host). |
| **Size limit** | Google ignores content beyond **500 KiB**. Keep it tiny. |
| **AI crawlers** | Allowed by default (we want AI-answer visibility). Opt specific bots out only with reason. `Google-Extended` controls Gemini training, **not** Search. |

> **Common mistake:** using `Disallow` to hide a page from the index. It doesn't work — use `noindex` (meta or `X-Robots-Tag`) on a crawlable page instead.

---

## 4. XML sitemaps

Implemented in [`../../public-templates/sitemap.xml`](../../public-templates/sitemap.xml) (sitemap **index** template).

| Rule | Detail |
| --- | --- |
| **Include only** | Canonical, indexable, **200-OK**, self-canonical URLs. |
| **Never include** | noindex, redirected, 404/soft-404, robots-blocked, or non-canonical URLs. |
| **`<loc>`** | Absolute, HTTPS, canonical host, correct trailing-slash style. |
| **`<lastmod>`** | **Real** last-modified date (W3C/ISO 8601). Don't fake it or stamp "now" every build — Google distrusts inaccurate `lastmod`. |
| **Per-file limits** | **≤ 50,000 URLs** and **≤ 50 MB** uncompressed. |
| **Sitemap index** | Beyond one file, use an index (also ≤ 50,000 child sitemaps, ≤ 50 MB). Our template splits by section (core / services / industries / locations / blog). |
| **`<changefreq>` / `<priority>`** | Optional and largely **ignored** by Google — don't rely on them; `<lastmod>` is what matters. |
| **Small sites** | May use a single flat `<urlset>` instead of an index until a few hundred URLs. |
| **Submit** | Reference in robots.txt **and** submit in Google Search Console; keep in sync. |

> **Consistency rule:** sitemap inclusion is a **weak** canonical signal — never let the sitemap contradict `rel=canonical` or hreflang.

---

## 5. Canonical tags

- [ ] **Self-referencing `rel=canonical`** on every indexable page, absolute URL, in the **HTML `<head>`**, placed **early**.
- [ ] Duplicate/parameterized URLs (`?utm=`, `?sort=`, print, AMP-less variants) canonicalize to the **preferred clean URL**.
- [ ] **Never** canonicalize to a URL that is **noindex**, returns **404/soft-404**, or **redirects**.
- [ ] **Never** send conflicting signals: canonical, sitemap `<loc>`, internal links, and hreflang must all agree on the same URL.
- [ ] Canonical URL uses the chosen **host + scheme + trailing-slash** style.
- [ ] Redirects and `rel=canonical` are **strong** canonicalization signals; sitemap inclusion is **weak** — don't let them conflict.

---

## 6. Pagination

- [ ] Each paginated page (`/blog/page/2/`) is a **real, crawlable, self-canonical** URL — **do not** canonicalize page 2+ to page 1 (that hides deeper content).
- [ ] `rel="next"/"prev"` is no longer used by Google for indexing — rely on **normal internal links** between pages plus self-canonicals.
- [ ] Link paginated pages from the hub so they're crawlable; ensure they're not orphaned.
- [ ] If you offer a "view all" page, you *may* canonicalize paginated pages to it — only if it's reasonably sized and 200-OK.
- [ ] Filtered/sorted parameter URLs that just reorder the same set should canonicalize to the clean list (or be blocked as crawl traps if infinite).

---

## 7. Indexing control (noindex)

| Want | Do |
| --- | --- |
| Keep a page **out of the index** | `<meta name="robots" content="noindex,follow">` on a **crawlable** page (or `X-Robots-Tag: noindex` header for non-HTML). Google must be able to crawl it to see the tag — **do not** also `Disallow` it. |
| Keep out of index but pass link equity | `noindex,follow` |
| Non-HTML files (PDF etc.) | `X-Robots-Tag: noindex` HTTP header |
| Typical noindex pages | thank-you/confirmation, internal search results, staging, low-value duplicates |

> **Never** combine `Disallow` (robots.txt) with `noindex` on the same URL — the crawler can't see the `noindex`, and the URL may get indexed URL-only.

---

## 8. Redirects, 404s & error handling

| Case | Rule |
| --- | --- |
| **Permanent move** | **301** (permanent). Update internal links to point at the final URL, not the redirect. |
| **Temporary** | 302/307 only when truly temporary. |
| **Chains/loops** | Eliminate redirect chains (A→B→C) — collapse to A→C. No loops. |
| **404 (Not Found)** | Custom, on-brand 404 page that returns a real **HTTP 404** status, with search + links back to money pages. |
| **410 (Gone)** | Use for intentionally removed content you won't restore. |
| **Soft-404** | Avoid: a "not found" page that returns **200**. Return the correct status code. |
| **Redirect on move** | When changing a URL/slug, 301 the old → new; keep old out of the sitemap. |
| **Don't redirect** | Many-to-one bulk redirects to the homepage (Google may treat as soft-404) — map to the closest relevant page. |

---

## 9. hreflang (only if multi-language / multi-region)

Skip entirely for a single-language site. If used:

- [ ] Valid codes: **ISO 639-1** language + optional **ISO 3166-1 Alpha-2** region (`en`, `en-GB`, `es-AR`).
- [ ] **Reciprocal**: every alternate references every other alternate **and itself**.
- [ ] Include an **`x-default`** fallback.
- [ ] Each `hreflang` target is a **canonical, indexable, 200** URL — never a redirect or noindex.
- [ ] Keep hreflang consistent with `rel=canonical` and the sitemap (no conflicts).
- [ ] Implement in `<head>` `<link rel="alternate">` (or XML sitemap / HTTP header) — one method, applied consistently.

---

## 10. Structured data pointer

Structured data (JSON-LD) is the machine-readable entity layer. **Full payloads and rules live in `structured-data.md`** — do not duplicate them here. Technical requirements this doc enforces:

- [ ] JSON-LD present in the rendered **mobile HTML** (mobile-first grading).
- [ ] `Organization` / `LocalBusiness` (specific subtype, e.g. `ProfessionalService`, with `sameAs`) sitewide; `Service`, `FAQPage`, `BreadcrumbList` per page type.
- [ ] **NAP in schema matches** the plain-text NAP on-site **and** Google Business Profile / Bing Places / Apple Maps exactly — Google/Gemini cross-check schema against GBP (see [`seo-strategy.md`](./seo-strategy.md) §6).
- [ ] Schema URLs (`url`, `sameAs`, `@id`) use the canonical host/scheme.
- [ ] Validate with Rich Results Test + Search Console "Enhancements".

See **[`structured-data.md`](./structured-data.md)**.

---

## 11. Mobile-first & page experience

**Mobile-first indexing is complete (July 2024).** Google indexes and ranks using the **mobile** render — even for desktop searchers.

- [ ] **Responsive design**, single template — mobile HTML contains **full** content, headings, links, images, and structured data (no stripped-down mobile).
- [ ] Content/heading **parity** between mobile and desktop.
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- [ ] Tap targets ≥ **44×44 CSS px**, ≥ 8px spacing (see [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md)).
- [ ] No horizontal scroll; no interstitials that block content on mobile.

**Page experience = tiebreaker, not a lever.** Core Web Vitals reward good pages **alongside** relevance and helpful content; excellent CWV can't rescue weak content, but poor CWV can cap gains. Optimize CWV in the context of helpful, people-first content.

**Core Web Vitals thresholds (field, p75 — full detail in [`../performance/performance-budget.md`](../performance/performance-budget.md)):**

| Metric | Good | Needs improvement | Poor |
| --- | --- | --- | --- |
| **LCP** (loading) | **≤ 2.5 s** | 2.5–4.0 s | > 4.0 s |
| **INP** (responsiveness) | **≤ 200 ms** | 200–500 ms | > 500 ms |
| **CLS** (visual stability) | **≤ 0.1** | 0.1–0.25 | > 0.25 |
| **TTFB** (diagnostic, not a CWV) | ≤ 800 ms | 800–1800 ms | > 1800 ms |

A URL passes only if **all three** CWV are "good" at the **75th percentile** of real-user (CrUX) data. **INP is the most-failed CWV in 2026** — prioritize main-thread/JS optimization.

> **Myth guard:** LCP "good" is **2.5 s** (not 2.0 s) per Google's docs; INP is a real but **secondary** input, **not** a "primary ranking signal." Ignore 2026 blogs claiming otherwise — they're not in Google's documentation.

---

## 12. Rendering & crawlability

- [ ] Critical content and links are in the **initial HTML** (SSR/SSG) — don't depend on client-side JS for primary content, headings, links, or schema.
- [ ] LCP element is **discoverable in the initial HTML**; LCP image not lazy-loaded.
- [ ] Links use real `<a href>` (crawlable) — not JS-only click handlers.
- [ ] No crawl budget waste: avoid infinite parameter spaces, session-ID URLs, and duplicate faceted URLs (canonical or block traps).
- [ ] Use **bfcache-friendly** patterns (no `unload` handlers) for instant back/forward.

---

## 13. Monitoring (Google Search Console)

| Report | Watch for | Cadence |
| --- | --- | --- |
| **Pages / Coverage** | Indexed vs excluded; "Discovered/Crawled – not indexed"; noindex/canonical anomalies | Weekly |
| **Sitemaps** | Submitted vs indexed; errors; ensure only canonical URLs listed | On publish + monthly |
| **Core Web Vitals** | Mobile + desktop groups; URLs failing at p75 (esp. INP) | Monthly |
| **Enhancements** | Structured-data validity (Breadcrumb/FAQ/LocalBusiness) | On publish + monthly |
| **Performance (Search)** | Queries, CTR, position — improve titles/meta/content where CTR/position lags | Weekly |
| **Removals / Manual actions / Security** | Any manual action or security issue | On alert |
| **URL Inspection** | Live-test indexability + mobile render of any new/changed page | Per launch |

Also: submit sitemap; verify the correct **domain property**; connect Bing Webmaster Tools. **Field data (CrUX/GSC) lags ~28 days** — don't expect same-day movement after a fix; verify fixes with lab tools (Lighthouse) + URL Inspection immediately, then confirm in field data weeks later.

---

## 14. Technical acceptance checklist

Run at site launch and when adding page types:

- [ ] HTTPS enforced; HTTP→HTTPS 301; single canonical host; other host 301'd
- [ ] One trailing-slash style; non-preferred form 301'd; consistent in canonicals/sitemap/links
- [ ] robots.txt allows crawl, doesn't block CSS/JS/images, points to sitemap, < 500 KiB
- [ ] Sitemap(s): only canonical/indexable/200 URLs, real `<lastmod>`, ≤ 50k/50MB, index if needed, submitted in GSC
- [ ] Self-referencing canonical on all indexable pages; no conflicts with sitemap/hreflang; never to noindex/404/redirect
- [ ] Pagination pages self-canonical and crawlable (not canonicalized to page 1)
- [ ] noindex used (not Disallow) for out-of-index pages; noindex pages remain crawlable
- [ ] 301 for moves; no chains/loops; custom 404 returns 404; no soft-404s
- [ ] hreflang (if used) reciprocal, valid codes, x-default, consistent with canonicals
- [ ] JSON-LD present in mobile HTML; NAP matches site + GBP; validated (see `structured-data.md`)
- [ ] Mobile-first parity: full content/headings/links/schema in mobile render; responsive; viewport meta
- [ ] Core Web Vitals pass at p75 (LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1); TTFB ≤ 0.8s
- [ ] Critical content/links/LCP element in initial HTML (SSR/SSG); real `<a href>` links
- [ ] GSC + Bing verified; sitemap submitted; CWV/coverage/enhancements monitored

---

## Related

- [`onsite-seo.md`](./onsite-seo.md) — titles, meta, headings, canonical/robots meta, internal links, `<head>` template.
- [`seo-strategy.md`](./seo-strategy.md) — architecture, keyword themes, NAP/local strategy, how layers fit.
- [`structured-data.md`](./structured-data.md) — JSON-LD entity payloads referenced in §10.
- [`ai-seo-geo.md`](./ai-seo-geo.md) — GEO / AI-answer visibility, llms.txt.
- [`seo-strategy.md`](./seo-strategy.md) — SEO system overview and standards index.
- [`../performance/performance-budget.md`](../performance/performance-budget.md) — Core Web Vitals detail, budgets, resource hints.
- [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md) — mobile tap targets, viewport, semantic parity.
- [`../../public-templates/robots.txt`](../../public-templates/robots.txt) — robots directives implementing §3.
- [`../../public-templates/sitemap.xml`](../../public-templates/sitemap.xml) — sitemap index implementing §4.
