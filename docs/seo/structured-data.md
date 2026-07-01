# Structured Data (JSON-LD)

**Purpose:** The prescriptive structured-data system for the {{BRAND_NAME}} site — which schema.org types to use, whether each is site-wide or per-page, required vs recommended properties, real Google rich-result eligibility (including deprecated features), the two-stage validation workflow, and the mistakes that get markup ignored or penalized. Pairs 1:1 with the copy-paste templates in [`../../schema/`](../../schema/).
**Status:** v1 foundation — adjustable.

---

> **On-page tags** (titles, meta, OG/Twitter) live in [`onsite-seo.md`](./onsite-seo.md). **Crawl/index rules** live in [`technical-seo.md`](./technical-seo.md). **Strategy/architecture** lives in [`seo-strategy.md`](./seo-strategy.md). This doc is the JSON-LD payload layer only.
> **Templates:** every type below links to a valid, placeholder-filled file in [`../../schema/`](../../schema/) with embedding/validation instructions in [`../../schema/README.md`](../../schema/README.md). Keep the two in sync.

---

## 0. TL;DR — structured-data rules in one screen

- [ ] **Format = JSON-LD**, `type="application/ld+json"`, server-rendered in `<head>`. Google's recommended, least-error-prone format (restated Feb 2026).
- [ ] **One entity graph.** Define `Organization`/`ProfessionalService` **once** and reference it everywhere by `@id`; don't duplicate the business block per page.
- [ ] **Most specific type wins.** An agency = `ProfessionalService` (a `LocalBusiness` subtype, which inherits from `Organization`).
- [ ] **LocalBusiness required = 2:** `name` + full `address` (`PostalAddress`). Everything else (geo, url, telephone, image, priceRange, hours) is recommended.
- [ ] **Only markup that yields a Google rich result on this site = `BreadcrumbList`.** Organization/LocalBusiness/Service/Offer feed the Knowledge Graph + AI answer engines, not a visual snippet.
- [ ] **Deprecated — do not build for rich results:** `FAQPage` (gone May 7 2026), `WebSite`/`SearchAction` sitelinks box (removed Nov 21 2024), `HowTo`.
- [ ] **No self-serving stars.** `Review`/`AggregateRating` about your own agency = ignored since 2019; fake reviews risk a manual action.
- [ ] **Only mark up what's visible on the page.** Hidden/mismatched content → structured-data manual action.
- [ ] **Validate twice:** before publish (raw code) and after every template/CMS change (live URL). Rich Results Test + Schema Markup Validator, then monitor Search Console.
- [ ] **NAP** in markup = byte-identical to Google Business Profile + site footer.

---

## 1. Type inventory — what this site uses and where

| Type | Template | Scope | Lives on | Google rich result? | Why we ship it |
| --- | --- | --- | --- | --- | --- |
| `Organization` | [`organization.jsonld`](../../schema/organization.jsonld) | **Site-wide** | Homepage (referenced everywhere by `@id`) | No (Knowledge Graph / brand panel) | Entity identity, logo, `sameAs`, contact — feeds Knowledge Graph + AI engines |
| `ProfessionalService` (LocalBusiness) | [`localbusiness.jsonld`](../../schema/localbusiness.jsonld) | **Site-wide** | Homepage + Contact | No (confirms business details) | NAP, geo, hours, area served, price range — corroborates GBP |
| `WebSite` + `SearchAction` | [`website.jsonld`](../../schema/website.jsonld) | **Site-wide** | Homepage | **No — deprecated** (sitelinks box removed Nov 21 2024) | Publisher link + site identity only; harmless, no feature |
| `Service` + `Offer` | [`service.jsonld`](../../schema/service.jsonld) | **Per-page** | Each service page | No (context / AI engines) | Describes the offering + pricing to Google & LLM answer engines |
| `FAQPage` | [`faqpage.jsonld`](../../schema/faqpage.jsonld) | **Per-page** | FAQ page | **No — deprecated** (ended May 7 2026) | Structured context only; do not expect the accordion |
| `BreadcrumbList` | [`breadcrumb.jsonld`](../../schema/breadcrumb.jsonld) | **Per-page** | Every non-home page | **Yes** ✅ | The one supported rich result here — ship it everywhere |
| `Review` / `AggregateRating` | [`review.jsonld`](../../schema/review.jsonld) | Per-page (conditional) | Only for reviews of **another** entity/supported type | No stars for self-serving | See §7 — mostly do NOT use on your own pages |
| `ImageObject` | inline (in Organization logo) | Site-wide | Logo / featured images | No (enables image display) | Gives logo/images explicit URL + dimensions |

**Priority order for effort (2026):** BreadcrumbList (real result) → Organization + LocalBusiness (entity/Knowledge Graph, expanded 2023→2026) → Service/Offer (AI/GEO value) → everything else last.

---

## 2. The entity graph — model the business once

**Do not paste the full business block on every page.** Define one canonical node and reference it by `@id`. This is the single most important structural decision.

```
Organization  @id=https://example.com/#organization   ← defined once (homepage)
   ▲    ▲    ▲    ▲
   │    │    │    └── ProfessionalService.parentOrganization → @id
   │    │    └─────── WebSite.publisher → @id
   │    └──────────── Service.provider → @id
   └───────────────── (any page-level node) → @id
```

- Give every reusable node a stable `@id` (a URL + fragment, e.g. `#organization`, `#website`, `#localbusiness`).
- On inner pages, **reference** the org: `"provider": { "@id": "https://example.com/#organization" }` — do not redefine it.
- Emit multiple nodes on one page with a single `"@graph": [ ... ]` array (see [`README §4`](../../schema/README.md)).

---

## 3. Organization (site-wide)

**Template:** [`organization.jsonld`](../../schema/organization.jsonld). Place on the homepage; reference by `@id` elsewhere.

**Required by Google:** none are hard-required — but ship the full recommended set for entity disambiguation.

| Property | Req/Rec | Notes |
| --- | --- | --- |
| `name` | Recommended (ship it) | Exact public brand name |
| `url` | Recommended | Canonical homepage, absolute |
| `logo` | Recommended | See §9 — crawlable, indexable, aspect ratio 0.75–2.5 |
| `sameAs` | Recommended | Array of profiles you **own** (LinkedIn, FB, IG, X, YouTube, Wikidata, GBP) |
| `contactPoint` | Recommended | `ContactPoint` with `telephone`, `contactType`, `areaServed`, `availableLanguage` |
| `address`, `email`, `telephone` | Recommended | Full `PostalAddress` object |
| `foundingDate` | Recommended | Reinforces entity |
| `vatID`, `iso6523Code`, `duns`, `leiCode`, `naics` | Recommended (behind-the-scenes) | Business identifiers that disambiguate you in the Knowledge Graph. **Omit if unknown** — never fake. |

**Rich result:** none — this feeds the Knowledge Graph / brand knowledge panel and AI answer engines. Support was expanded Nov 2023 → 2025/2026, so investment here pays off even without a visual snippet.

---

## 4. ProfessionalService / LocalBusiness (site-wide)

**Template:** [`localbusiness.jsonld`](../../schema/localbusiness.jsonld). `@type` = `ProfessionalService` — the correct `LocalBusiness` subtype for a marketing/consulting agency. Because `LocalBusiness` inherits from `Organization`, follow Organization fields **in addition** to these.

| Property | Req/Rec | Notes |
| --- | --- | --- |
| `name` | **Required** | |
| `address` | **Required** | Full `PostalAddress`: `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry`. Must be nested inside `address`, not flattened. |
| `geo` | Recommended | `GeoCoordinates` `latitude`/`longitude` |
| `url`, `telephone`, `image` | Recommended | `image` must be crawlable/indexable |
| `priceRange` | Recommended | `$`, `$$`, `$$$` |
| `openingHoursSpecification` | Recommended | Array of `OpeningHoursSpecification`. AI runs 24/7; scope human support hours honestly. |
| `areaServed` / `serviceArea` | Recommended (emerging) | Add for a business that serves beyond one storefront — an agency serving a whole country/region. |

**Rich result:** none for a generic agency — LocalBusiness feeds Google's understanding + knowledge panel and **corroborates your Google Business Profile**. Keep on-site NAP and GBP perfectly consistent; on-site markup supports GBP, it does not replace it.

---

## 5. WebSite + SearchAction (site-wide) — deprecated feature

**Template:** [`website.jsonld`](../../schema/website.jsonld). Homepage only.

- The **Sitelinks Search Box** this powered was **removed Nov 21 2024** and dropped from Search Console + the Rich Results Test. `SearchAction` now produces **no visual feature**.
- We still emit a minimal `WebSite` node because it carries `publisher` → `@id` (linking site ↔ organization) and site name/language, which reinforce entity signals. **Do not invest effort chasing the search box** — it's gone. If you have no site search endpoint, drop `potentialAction` entirely.

---

## 6. Service + Offer (per-page)

**Template:** [`service.jsonld`](../../schema/service.jsonld). One per service page.

| Property | Req/Rec | Notes |
| --- | --- | --- |
| `name`, `serviceType`, `description` | Recommended | Clear, benefit-led, matches on-page copy |
| `provider` | Recommended | `{ "@id": ".../#organization" }` |
| `areaServed` | Recommended | Country/region |
| `offers` / `hasOfferCatalog` | Recommended | `Offer` with `price`, `priceCurrency`, `availability`, `url`; use `UnitPriceSpecification` for monthly plans |
| `audience` | Optional | `BusinessAudience` — helps AI engines target |

**Rich result:** none — `Service`/`Offer` produce **no Google visual snippet**. Their value is context for Google and, increasingly, for **AI/LLM answer engines (GEO/AEO)** that consume Service/Offer/Organization markup directly. Keep prices accurate and **visible on the page**.

---

## 7. FAQPage (per-page) — deprecated feature

**Template:** [`faqpage.jsonld`](../../schema/faqpage.jsonld). Only on pages with a **visible** FAQ.

- **FAQ rich results ended May 7 2026** (already restricted to authoritative gov/health sites since Aug 2023). Rich Results Test support removed June 2026; Search Console API support removed Aug 2026. **Do not expect the expandable accordion.**
- We keep a valid `FAQPage` node purely as machine-readable Q&A context (useful for AI answer engines). If you ship it: every question/answer **must be visible on the page**, verbatim. If it adds maintenance with no upside for you, it's safe to drop.

---

## 8. BreadcrumbList (per-page) — the one supported rich result ✅

**Template:** [`breadcrumb.jsonld`](../../schema/breadcrumb.jsonld). Ship on **every non-home page**; it mirrors the visible breadcrumb trail.

| Property | Req/Rec | Notes |
| --- | --- | --- |
| `itemListElement` | **Required** | Array of ≥ **2** `ListItem` |
| `ListItem.position` | **Required** | Starts at **1**, increments by 1 |
| `ListItem.name` | **Required** | Visible crumb label |
| `ListItem.item` | **Required** | Absolute URL of that step (may omit on the final/current item) |

**Rich result:** **Yes** — the breadcrumb trail replaces the plain URL in the SERP. This is the highest-ROI markup on the site. Keep it in lockstep with the visible breadcrumb UI and the URL path.

---

## 9. Images / logo (ImageObject)

- Logo and **all** structured-data image URLs must be **crawlable and indexable** (not blocked by robots.txt, not `noindex`) or Google can't display them.
- Formats: **JPEG, PNG, WebP, SVG**.
- **Aspect ratio safe range: width:height between 0.75 and 2.5.** Avoid extreme (too narrow / too wide) images.
- Prefer a dedicated logo `ImageObject` with explicit `width`/`height`; supply multiple images as an array if needed.

---

## 10. Review / AggregateRating — mostly DO NOT use here ⚠️

| Rule | Detail |
| --- | --- |
| **Self-serving = ignored** | Since Sept 2019, an entity marking up reviews **about itself** on its own `Organization`/`LocalBusiness` is **ineligible** for the star feature — Google shows **0 stars**. |
| **Penalty risk** | Fabricated/aggressive self-serving reviews risk a **spam manual action**. |
| **Must be visible** | Any rating in markup must be **visible to users on the page**, or it's ineligible even where supported. |
| **Where it IS valid** | Review snippets remain valid for supported types (`Product`, `Book`, `Recipe`, `Movie`, `Event`, `Course`, `SoftwareApplication`) and for sites hosting reviews **about other businesses**. |

**Required properties (only if you legitimately use it):**

- Single `Review`: `itemReviewed`, `reviewRating` (with `ratingValue`), `author` (`Person`/`Organization` with `name`). `datePublished` recommended.
- `AggregateRating`: `ratingValue` **plus** at least one of `ratingCount` or `reviewCount`. `bestRating` (default 5) / `worstRating` (default 1) recommended.

The included [`review.jsonld`](../../schema/review.jsonld) is a **reference structure**. For social proof about your own agency, display testimonials as **visible on-page content** and rely on your **Google Business Profile** for review stars — not self-serving on-site markup.

---

## 11. Deprecated / removed features — quick reference

| Feature | Status | Date |
| --- | --- | --- |
| FAQ rich result | Removed | May 7 2026 (RRT support gone June 2026; SC API Aug 2026) |
| Sitelinks Search Box (`WebSite`/`SearchAction`) | Removed | Nov 21 2024 |
| Self-serving Review stars (LocalBusiness/Organization) | Not displayed | since Sept 2019 |
| HowTo rich result | Removed | 2023 |

**Structured-data manual action** only removes **rich-result eligibility** — it does **not** change ranking; the page still appears in normal Search. But fix it fast: it signals a guidelines violation.

---

## 12. Validation workflow — two stages, two tools

Validate **before publishing** (raw code) **and after every template/CMS change** (live URL).

| Stage | Tool | Checks |
| --- | --- | --- |
| Syntax (local) | `python3 -c "import json; json.load(open(f))"` | JSON parses at all — catches the #1 mistake |
| Eligibility | [Rich Results Test](https://search.google.com/test/rich-results) | Google rich-result eligibility (Breadcrumb here) |
| Schema correctness | [Schema Markup Validator](https://validator.schema.org/) | schema.org types/props for non-rich types (Org, Service, LocalBusiness) |
| Ongoing | Google Search Console → Enhancements / Rich results | New errors, valid-item drops, "Unparsable structured data" |

**Ship checklist per page:**

- [ ] JSON parses locally (loop in [`README §5`](../../schema/README.md)).
- [ ] No `{{PLACEHOLDER}}` remains; no empty-string or fake values.
- [ ] Correct, most-specific `@type`; `PostalAddress` nested inside `address`.
- [ ] All required props present (see per-type tables).
- [ ] Every marked-up value is **visible on the rendered page** (prices, ratings, FAQ answers, crumbs).
- [ ] Markup present in **mobile** HTML.
- [ ] Rich Results Test + Schema Markup Validator = 0 errors.
- [ ] After deploy: re-test the live URL; watch Search Console for 28 days.

---

## 13. Common mistakes → what actually happens

| Mistake | Result |
| --- | --- |
| Self-serving Review/AggregateRating on your own Org/LocalBusiness | Stars **ignored**; fake reviews risk a **spam manual action** |
| Marking up content **not visible** on the page (hidden/mismatched) | **Structured-data manual action** → loses rich-result eligibility |
| Aggregate rating in markup users can't see | Rating **ineligible** |
| Expecting a rich result from Service/Offer or plain LocalBusiness | None appear — only Breadcrumb (+ Product/Review on supported types) yield visual results |
| Still building for FAQPage / HowTo / Sitelinks Search Box | Wasted effort — all deprecated |
| JSON errors (missing commas, unescaped quotes, unbalanced brackets, `PostalAddress` not nested in `address`) | "**Unparsable structured data**" — item dropped |
| Omitting required props (no full `PostalAddress`; `ListItem` missing position/name/item; `AggregateRating` missing ratingValue or a count) | Item **ineligible** |
| Non-crawlable / extreme-aspect-ratio logo/image | Google **can't display** the image |
| Duplicating the full business block on every page instead of `@id` references | Bloat + drift; NAP inconsistencies |

---

## Related

- [`../../schema/README.md`](../../schema/README.md) — how to embed, replace placeholders, and validate the templates.
- [`../../schema/`](../../schema/) — the seven JSON-LD template files this doc governs.
- [`./onsite-seo.md`](./onsite-seo.md) — on-page tags (titles, meta, OG/Twitter) that pair with this markup.
- [`./technical-seo.md`](./technical-seo.md) — crawl/index rules (mobile-first, canonicals, sitemaps, GSC).
- [`./seo-strategy.md`](./seo-strategy.md) — site architecture, content themes, and funnel.
