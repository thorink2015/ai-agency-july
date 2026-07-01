# SEO & Indexing Troubleshooting Playbook

**Purpose:** Symptom-driven diagnosis and repair for the {{BRAND_NAME}} site's search problems — pages not indexed, dropped rankings, canonical/duplicate issues, sitemap/robots errors, structured-data errors in Google Search Console, missing rich results, and AI engines not citing us — each as `Symptom → Likely cause → Diagnosis → Fix → Prevention` so any developer or marketer can restore crawlability, indexing, and visibility.
**Status:** v1 foundation — adjustable.

---

> **This diagnoses deviations from the standard.** The crawl/index/on-page rules live in [`../seo/technical-seo.md`](../seo/technical-seo.md), [`../seo/onsite-seo.md`](../seo/onsite-seo.md), [`../seo/structured-data.md`](../seo/structured-data.md), and [`../seo/ai-seo-geo.md`](../seo/ai-seo-geo.md). This file is what you open when Search Console flags a problem or a ranking drops.
>
> **Primary tool:** Google Search Console (GSC). Almost every diagnosis below starts with **URL Inspection** or a GSC report.
>
> **Patience rule:** indexing and CrUX changes are not instant. Re-crawl can take days; CrUX field data lags **~28 days**. Fix, request re-index, then wait before concluding it didn't work.

---

## 0. TL;DR — SEO triage in one screen

- [ ] **Start in GSC URL Inspection** for any single-page problem: it shows index status, the Google-selected canonical, crawl/render, and structured-data validity in one view.
- [ ] **Blocking ≠ deindexing.** `Disallow` in robots.txt does *not* remove a page from the index — it just stops crawling (the URL can still appear with no snippet). To remove a page, use `noindex` on a **crawlable** page.
- [ ] **Don't send conflicting signals.** Canonical, sitemap, internal links, and hreflang must all agree. Never canonicalize to a noindex/404/redirect.
- [ ] **The HTML `<title>` still drives ranking** even though Google rewrites ~76% of displayed title links.
- [ ] **Google indexes the mobile render.** If content/headings/schema/links are missing on mobile, they effectively don't exist.

### Key limits you're diagnosing against

| Thing | Limit / target |
|---|---|
| Title tag | ~50–60 chars / < ~600px desktop; keyword in first 30–35 chars |
| Meta description | ~150–160 chars desktop (~110–120 mobile); unique per page |
| XML sitemap file | ≤ 50,000 URLs / ≤ 50MB uncompressed (use a sitemap index beyond that) |
| robots.txt | ≤ 500 KiB (Google ignores beyond this) |
| OG/X card image | 1200 × 630 px (1.91:1) |
| H1 | one clear H1 per page |
| CWV (page experience) | LCP < 2.5s, INP < 200ms, CLS < 0.1 at p75 |

---

## 1. Page not indexed

Always begin with **GSC → URL Inspection → the URL**. Read the "Coverage" / "Page indexing" verdict; it names the exact reason.

| Symptom (GSC status) | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| "Excluded by 'noindex' tag" | A `noindex` meta/header on a page you want indexed | URL Inspection → "Indexing allowed? No: 'noindex' detected"; `curl -sI <url>` for `x-robots-tag`, view-source for `<meta name="robots" content="noindex">`. | Remove the `noindex`; keep the page crawlable; Request Indexing. | Template check: only intentional pages carry `noindex`; staging noindex never ships to prod. |
| "Blocked by robots.txt" | `Disallow` rule stops crawling | URL Inspection shows blocked; test in robots.txt Tester; view `/{robots.txt}`. | Remove/narrow the `Disallow`; use `noindex` (not robots block) for index control. | robots.txt in review; never block pages you want indexed or CSS/JS. |
| "Crawled – currently not indexed" | Thin/duplicate/low-value content; Google chose not to index | Compare against similar indexed pages; check word count, uniqueness, internal links. | Improve depth, uniqueness, and internal linking; differentiate template pages (see §2/§thin). | Content quality bar; no template-clone location pages. |
| "Discovered – currently not indexed" | Crawl budget / low priority; not yet fetched | URL Inspection: last crawl "N/A" or old. | Add internal links from strong pages; include in sitemap with accurate `<lastmod>`; Request Indexing. | Strong internal linking + sitemap hygiene. |
| "Duplicate, Google chose different canonical" | Google picked another URL as canonical | URL Inspection: "User-declared canonical" vs "Google-selected canonical" differ. | Strengthen signals: self-canonical, unique content, consistent internal links to the preferred URL. | Self-referencing canonical on all indexable pages. |
| "Soft 404" | Page returns 200 but looks empty/error-like | URL Inspection; check the rendered content. | Add real content or return a proper 404/410; fix empty states. | No 200-status empty pages; custom 404 returns real 404. |
| "Page with redirect" | The URL 301/302s elsewhere | `curl -sI <url>` shows 3xx. | Submit the destination URL, not the redirected one, in the sitemap. | Sitemap lists only final 200 canonical URLs. |
| Not submitted at all | Page missing from sitemap and unlinked | Search the sitemap; check internal links. | Add to sitemap; link internally from relevant pages. | Sitemap generated from the route manifest at build. |

---

## 2. Dropped rankings

Rankings drop for algorithm, technical, content, or competitive reasons. Isolate *when* and *how much* first.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Sudden site-wide drop on a specific date | Google core/algorithm update, or an accidental site-wide technical change | GSC Performance: pin the date; cross-reference known update dates; check for a bad deploy on that date. | If a deploy: revert the SEO regression (accidental noindex, robots block, broken canonical/redirect). If an update: improve helpful-content/E-E-A-T, don't chase tactics. | Deploy diff review for SEO-affecting changes; monitor GSC clicks weekly. |
| Gradual decline over weeks | Content staleness, lost backlinks, or rising competition | GSC Performance trend; backlink tool; SERP comparison vs competitors. | Refresh content, rebuild/earn links, deepen the page vs competitors. | Content refresh cadence; backlink monitoring. |
| One page dropped, rest fine | On-page regression, cannibalization, or lost internal links | URL Inspection + GSC page-level Performance; check for two pages targeting the same query. | Fix the page (title/content/links); consolidate cannibalizing pages with canonical/redirect. | Keyword-to-URL map to prevent cannibalization. |
| Drop after a redesign/migration | Broken redirects, changed URLs, lost content/links | Crawl old vs new URLs; check 301 map; compare on-page elements. | Restore 1:1 301s; re-add missing content/headings/schema/links. | Migration checklist with 301 map + parity audit. |
| Impressions steady, clicks down | Title/description rewritten or SERP feature took the click | GSC Performance CTR by query; inspect the live SERP. | Improve title/meta relevance to reduce Google rewrites; target the SERP feature (FAQ, etc.). | Unique, accurate titles/descriptions per page. |
| Rankings fine, traffic down | CWV/page-experience or seasonality | GSC CWV report; compare year-over-year. | Fix failing CWV (see [`performance.md`](./performance.md)); account for seasonality. | CWV monitoring; page-experience as a tiebreaker. |

---

## 3. Canonical / duplicate issues

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Google ignores your canonical | Weak/conflicting signals or canonical to a poor target | URL Inspection: declared vs selected canonical. | Make canonical absolute, in `<head>`, self-referencing on the preferred URL; align sitemap + internal links + hreflang. | Canonical = sitemap = internal links, enforced in template. |
| Duplicate content across URL variants | `www`/apex, `http`/`https`, trailing-slash, or params all resolve 200 | `curl -sI` each variant — do they 301 to one canonical host/form? | 301 all variants to one canonical host + one trailing-slash style; self-canonical. | One canonical host + one slash style; 301 the rest. |
| Params create infinite duplicates | Tracking/filter params generate crawlable duplicate URLs | GSC coverage shows many param URLs. | Canonicalize params to the clean URL; avoid linking param URLs internally. | Clean internal links; canonical strips params. |
| Canonical points to noindex/404/redirect | Misconfigured canonical target | Follow the canonical URL's status with `curl -sI`. | Point canonical only to an indexable, 200, self-canonical page. | Lint canonical targets in CI (must be 200 + indexable). |
| Pagination duplicates | Paginated pages canonicalizing to page 1 | Inspect page-2+ canonicals. | Self-canonical each paginated page (don't canonical all to page 1); ensure unique content. | Pagination pattern documented and templated. |

---

## 4. Sitemap & robots.txt errors

| Symptom (GSC) | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| "Sitemap could not be read" / fetch error | Wrong path, non-200, or malformed XML | GSC Sitemaps report; fetch the sitemap URL directly; validate XML. | Serve valid XML at the referenced path, 200 status; fix encoding/syntax. | Sitemap validated in CI; smoke test fetches it post-deploy. |
| "Sitemap contains URLs blocked by robots.txt" | Sitemap lists disallowed URLs | GSC flags the URLs; cross-check robots.txt. | Remove blocked URLs from the sitemap or unblock them (whichever is intended). | Sitemap generated only from crawlable, canonical routes. |
| Sitemap includes noindex/404/redirect URLs | Auto-generation not filtering | GSC "Sitemap" coverage; spot-check statuses. | Include only canonical, indexable, 200 URLs with real `<lastmod>`. | Build-time filter: 200 + indexable + canonical only. |
| Sitemap too large | > 50,000 URLs or > 50MB | Count URLs / file size. | Split into multiple sitemaps under a sitemap index (index also ≤ 50k / 50MB). | Auto-split at 50k URLs. |
| robots.txt not respected | File > 500 KiB, wrong location, or non-200 | Fetch `/{robots.txt}`; check size and status. | Keep < 500 KiB at the root, 200 status; reference the sitemap. | robots.txt size/status in smoke test. |
| robots.txt blocks CSS/JS/images | Over-broad `Disallow` breaks rendering | GSC URL Inspection "Screenshot" looks unstyled. | Allow crawling of CSS/JS/image assets. | Never disallow rendering assets. |

---

## 5. Structured-data errors in Search Console

Validate with the **Rich Results Test** and **Schema Markup Validator**; monitor in **GSC → Enhancements**. Owning doc: [`../seo/structured-data.md`](../seo/structured-data.md).

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| GSC "Invalid" items in an Enhancement report | Missing required property or wrong type | Rich Results Test on the URL — it lists the missing/invalid field. | Add the required property; use the correct schema type; re-validate; Validate Fix in GSC. | JSON-LD validated in CI against the target type. |
| "Non-critical issues"/warnings | Recommended (not required) properties missing | Rich Results Test warnings section. | Add recommended fields where they add value; warnings don't block eligibility but improve it. | Include recommended fields in the schema template. |
| Schema present but not detected | JSON-LD injected by JS Google didn't render, or syntax error | URL Inspection → "View crawled page" / rendered HTML; validate JSON syntax. | Put JSON-LD in the server-rendered HTML; fix JSON syntax (trailing commas, quotes). | Server-render JSON-LD; lint JSON. |
| Wrong entity / mismatched data | Schema says one thing, page/GBP says another | Compare schema NAP/values to on-page + Google Business Profile. | Make schema match visible content and GBP exactly (NAP consistency). | Single source for NAP feeding schema, page, and GBP. |
| Multiple conflicting blocks | Two schema blocks describe the same entity differently | Validator shows duplicates/conflicts. | Consolidate into one accurate block per entity. | One canonical schema block per entity/page type. |

---

## 6. Missing rich results

Passing validation makes you *eligible*, not *guaranteed*. Google decides display.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Valid schema, no rich result shown | Eligible but Google chose not to display, or quality threshold | Rich Results Test says "eligible"; check the live SERP. | Ensure content genuinely matches the schema; improve page quality; be patient (display is Google's call). | Only mark up content that's actually on the page. |
| FAQ/HowTo rich result disappeared | Google reduced eligibility for that type / policy change | GSC Enhancements trend drop with no code change. | Keep valid markup; don't rely on any single rich-result type; diversify SERP presence. | Don't build strategy on one volatile rich-result type. |
| Breadcrumb/logo/sitelinks missing | Missing/incorrect `BreadcrumbList`/`Organization` markup | Rich Results Test for those types. | Add correct `BreadcrumbList` and `Organization` (with `logo`) schema. | Include breadcrumb + organization schema sitewide. |
| Review stars gone | Self-serving/ineligible review markup or policy | Validator + Google's review-snippet policy. | Only mark up genuine, policy-compliant reviews on eligible content. | Follow review-snippet policy; no self-created ratings. |
| Marked up but wrong page type | Schema type doesn't match Google's supported features | Rich Results Test "no eligible items detected." | Use a supported type (`LocalBusiness` subtype, `FAQPage`, etc.) that Google renders. | Use documented, supported schema types only. |

---

## 7. AI engines not citing us (AI Overviews / generative search / LLMs)

Owning doc: [`../seo/ai-seo-geo.md`](../seo/ai-seo-geo.md). Optimize for *extractability* and *entity clarity*.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Not cited in AI Overviews / answers | Content isn't concisely extractable or lacks entity/E-E-A-T clarity | Read the page as a machine: is there a direct, quotable answer near the top? Are entities named? | Add concise, self-contained answers under clear H2/H3 questions; state entities plainly; include cited stats and consistent NAP. | Question-led headings + concise-answer pattern in content templates. |
| AI cites competitors instead | They have clearer answers, stronger authority, or better structure | Compare their cited passages to yours. | Provide a better, more direct answer with E-E-A-T signals (author, credentials, sources). | E-E-A-T signals (author bio, sources) on key pages. |
| Missing FAQ/answer schema | No `FAQPage` / structured Q&A for the assistant to parse | Rich Results Test; check for FAQ schema. | Add `FAQPage` schema mirroring on-page Q&A. | FAQ schema on FAQ/service pages. |
| Wrong facts about the business surfaced | Inconsistent NAP/entity across web + schema + GBP | Compare website, schema, GBP, directories. | Make NAP identical everywhere; use specific `LocalBusiness` subtype + `sameAs` to profiles. | Single NAP source; `sameAs` links to verified profiles. |
| AI can't access the content | Content JS-rendered / gated / blocked to bots | Fetch as plain text (`curl`); check robots/user-agent rules. | Server-render key content as crawlable text; don't block legitimate AI crawlers you want citing you. | Server-rendered, plain-text-extractable key content. |
| Provide an `llms.txt` | No machine-readable guide for LLMs | Check for `/{llms.txt}`. | Publish an `llms.txt` summarizing the business, key pages, and canonical facts. | `llms.txt` maintained alongside sitemap. |

---

## 8. Post-fix verification checklist

- [ ] Re-ran **GSC URL Inspection** and used **Request Indexing** / **Validate Fix** where relevant.
- [ ] Confirmed canonical, sitemap, internal links, and hreflang all **agree**.
- [ ] Confirmed the page is **crawlable** (not accidentally robots-blocked) before relying on `noindex`/canonical.
- [ ] Verified structured data with the **Rich Results Test** (eligible, no errors).
- [ ] Checked the fix on the **mobile render** (what Google indexes).
- [ ] Logged that **re-crawl takes days and CrUX ~28 days** — don't conclude failure prematurely.

---

## Related

- [`README.md`](./README.md) — playbook index, triage, and severity model.
- [`../seo/technical-seo.md`](../seo/technical-seo.md) — robots, sitemaps, canonicals, redirects, mobile-first.
- [`../seo/onsite-seo.md`](../seo/onsite-seo.md) — titles, meta, headings, links, alt text.
- [`../seo/structured-data.md`](../seo/structured-data.md) — JSON-LD types and templates.
- [`../seo/ai-seo-geo.md`](../seo/ai-seo-geo.md) — llms.txt, extractable answers, entity/E-E-A-T for AI engines.
- [`../seo/seo-strategy.md`](../seo/seo-strategy.md) — architecture and keyword-to-URL mapping.
- [`performance.md`](./performance.md) — CWV/page-experience diagnosis (a Search signal).
- [`build-deploy.md`](./build-deploy.md) — redirects, canonical host, and migration mechanics.
