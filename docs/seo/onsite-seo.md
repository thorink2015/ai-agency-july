# On-Site (On-Page) SEO

**Purpose:** The prescriptive on-page checklist for every {{BRAND_NAME}} page — titles, meta, headings, semantic HTML, URLs, internal links, image alt, Open Graph / Twitter cards, content quality / E-E-A-T — plus a copy-paste `<head>` template and a per-page acceptance checklist any developer or marketer can apply before shipping.
**Status:** v1 foundation — adjustable.

---

> **Strategy context:** [`seo-strategy.md`](./seo-strategy.md) (themes, architecture, funnel). This doc turns those into on-page rules.
> **Technical crawl/index rules live in** [`technical-seo.md`](./technical-seo.md). **Structured data (JSON-LD)** lives in `structured-data.md`. This doc covers everything *on the page* except the schema payloads.

---

## 0. TL;DR — on-page rules in one screen

- [ ] **Title** unique per page, **≤ 60 chars / < ~600px desktop**, primary keyword in the **first 30–35 chars**, brand at the end.
- [ ] **Meta description** unique, **~150–160 chars** (front-load value in first ~120 for mobile), accurate to the page, with a soft CTA.
- [ ] **Exactly one `<h1>`** stating the page's core topic; `h2`/`h3` form a logical hierarchy with **no skipped levels**.
- [ ] **Semantic HTML5** landmarks; headings + content + links + schema all present in the **mobile HTML** (mobile-first indexing).
- [ ] **Descriptive URL:** lowercase, hyphenated, keyword-bearing, no dates/IDs/params.
- [ ] **Internal links:** descriptive anchors, hub↔spoke, ~2–5 contextual links per 1,000 words; no "click here".
- [ ] **Every meaningful `<img>` has real alt**; decorative images use `alt=""`; LCP image is eager + `fetchpriority="high"`.
- [ ] **OG + Twitter** tags on every page; image **1200×630**; `twitter:card=summary_large_image`.
- [ ] **E-E-A-T on the page:** first-hand experience, named humans, proof/stats, accurate NAP, dates.
- [ ] Page ships only after the **[§11 per-page acceptance checklist](#11-per-page-seo-acceptance-checklist)** passes.

---

## 1. Title tag

The HTML `<title>` still drives ranking even when Google rewrites the *displayed* link (Google changed ~76% of title tags in Q1 2025 — accurate, non-duplicative titles reduce rewrites).

| Rule | Value |
| --- | --- |
| Length | **~50–60 chars**, hard target **< ~600px desktop** (~480px mobile). Char count is a proxy — pixel width is the real limit. |
| Keyword position | Front-load primary keyword in the **first 30–35 chars** |
| Brand | Include `{{BRAND_NAME}}`, usually at the **end** (`… | {{BRAND_NAME}}`) |
| Local pages | Include `{{CITY}}`/`{{REGION}}` |
| Uniqueness | **Unique per page** — no duplicates, no template stuffing |
| Accuracy | Describe the page truthfully — reduces Google rewrites (brand removal is the #1 rewrite) |

**Patterns (directions, not final copy):**

| Page | Title pattern (≤ 60 chars) |
| --- | --- |
| Home | `AI Receptionist That Books Leads in Seconds | {{BRAND_NAME}}` |
| Service | `AI Appointment Setting, Done for You | {{BRAND_NAME}}` |
| Industry | `AI Lead Response for Med Spas | {{BRAND_NAME}}` |
| Location | `AI Receptionist in {{CITY}} | {{BRAND_NAME}}` |
| Pricing | `Pricing — AI Lead Response Service | {{BRAND_NAME}}` |
| Blog post | `[Specific benefit-led question or claim] | {{BRAND_NAME}}` |

**Don't:** exceed ~600px; bury the keyword after the brand; duplicate the H1 verbatim across many pages; keyword-stuff (`AI receptionist AI answering AI booking`).

---

## 2. Meta description

Not a direct ranking factor, but drives CTR. Google rewrites ~60–70% when it finds a better query match — so make it **specific to the page**.

| Rule | Value |
| --- | --- |
| Length | **~150–160 chars** (~920px) desktop; front-load the value in the **first ~110–120 chars** for mobile |
| Uniqueness | Unique per page; never reuse the same string sitewide |
| Content | Accurate summary + the benefit + a soft CTA (e.g. "Book a call") |
| Match | Reflect the actual page content and target query |

**Example (service page):**
`We set up and manage AI assistants that answer, qualify, and book your inbound leads in seconds — 24/7, with humans on call. Done for you. Book a call.` (~148 chars)

**Don't:** stuff keywords; duplicate the meta across pages; write a generic sitewide boilerplate; exceed ~160 chars (it truncates).

---

## 3. Headings & hierarchy

One page = one primary topic = one `<h1>`. Google tolerates multiple H1s, but **one clear H1 is the safe best practice** for SEO + accessibility (screen-reader navigation).

- [ ] **Exactly one `<h1>`** = the page's core topic (may echo the title's intent, not verbatim).
- [ ] `<h2>` = main sections; `<h3>` = subsections. **Never skip levels** for visual styling (style with CSS, not by picking a bigger heading tag).
- [ ] Headings are **descriptive**, keyword-relevant, human-readable — not "Section 1".
- [ ] Headings render in the **mobile HTML** (mobile-first indexing grades the mobile render).
- [ ] Use headings to structure the answer: a question-shaped `h2` followed by a concise answer wins snippets + AI citations.

```
h1  AI Appointment Setting, Done for You
├─ h2  How it works
│  ├─ h3  Answer in seconds
│  ├─ h3  Qualify the lead
│  └─ h3  Book the appointment
├─ h2  Built for your industry
├─ h2  Integrates with your tools
├─ h2  Pricing            → CTA
└─ h2  FAQ                → FAQ schema (structured-data.md)
```

---

## 4. Semantic HTML

Structure with landmarks — better for SEO parsing, accessibility, and AI extraction. (Detailed a11y rules: [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md).)

| Use | Not |
| --- | --- |
| `<header> <nav> <main> <article> <section> <aside> <footer>` | `<div>` soup for everything |
| One `<main>` per page | Multiple `<main>` |
| `<button>` for actions, `<a href>` for navigation | `<div onclick>` |
| `<nav aria-label>` for distinct nav regions | Unlabeled duplicate navs |
| Lists (`<ul>/<ol>`) for lists; `<table>` for tabular data | Faking structure with `<br>` |
| Real text for NAP, headings, key content | Text baked into images or injected only by JS |

> **Mobile-first parity:** whatever a desktop user sees — content, headings, links, structured data — must exist in the **mobile HTML**. Don't ship a stripped-down mobile layout that hides content.

---

## 5. URLs

| Rule | Example |
| --- | --- |
| Lowercase, hyphen-separated, no spaces/underscores | `/services/ai-receptionist/` |
| Keyword-bearing, short, readable | `/industries/med-spas/` |
| No dates, IDs, session params, or tracking in canonical URLs | not `/p?id=482&utm=...` |
| Match `seo-strategy.md` architecture (hub-and-spoke) | `/industries/` → `/industries/dental-clinics/` |
| **Trailing-slash style consistent sitewide** (pick one — see [`technical-seo.md`](./technical-seo.md)) | all with `/` or all without |
| Stable — don't change URLs casually; if you must, **301** the old one | see redirects in [`technical-seo.md`](./technical-seo.md) |

---

## 6. Internal linking

Internal links distribute authority and define topical relationships. (Not a Google rule, but practitioner guidance: ~**2–5 contextual links per 1,000 words**; keep total on-page links reasonable.)

- [ ] **Descriptive anchor text** that matches the target's topic — never "click here", "read more", "this page".
- [ ] **Hub ↔ spoke:** hubs link to every child; children link back to the hub and to relevant siblings (service ↔ industry matrix from [`seo-strategy.md`](./seo-strategy.md)).
- [ ] **No orphan pages** — every indexable page has ≥ 1 internal link pointing to it.
- [ ] **Point to canonical URLs** (final destination), not to redirects or non-canonical variants.
- [ ] Every page includes a **contextual link into the book-a-call path** (no dead-ends).
- [ ] **Breadcrumbs** on deep pages (pair with `BreadcrumbList` schema — see `structured-data.md`).

**Don't:** exact-match keyword-stuff every anchor; use generic anchors; bury key links behind JS-only interactions; create sitewide footers with 200 links.

---

## 7. Image alt & on-page media

Detailed image performance/format rules live in [`../performance/performance-budget.md`](../performance/performance-budget.md) and [`../brand/imagery.md`](../brand/imagery.md). On-page SEO essentials:

- [ ] **Meaningful images have descriptive `alt`** conveying content/function (not keyword-stuffed).
- [ ] **Decorative images** use `alt=""` (empty) so screen readers/crawlers skip them.
- [ ] **Explicit `width`/`height`** (or CSS `aspect-ratio`) on every image — prevents CLS.
- [ ] **LCP image** (usually the hero): **eager**-loaded, `fetchpriority="high"`, **never** `loading="lazy"`.
- [ ] Below-the-fold images: `loading="lazy"`.
- [ ] Descriptive **file names** (`ai-receptionist-demo.avif`, not `IMG_2831.jpg`).
- [ ] AVIF primary + WebP fallback with responsive `srcset`/`sizes` (see performance doc).

**Alt examples:**

| Image | Good alt |
| --- | --- |
| Screenshot of AI booking a med-spa appointment | `alt="AI assistant booking a med-spa consultation via SMS in seconds"` |
| Team photo | `alt="{{BRAND_NAME}} support team who handle escalations"` |
| Decorative background blob | `alt=""` |

---

## 8. Open Graph & Twitter (X) cards

Every page ships social meta. One 1200×630 image works across all major platforms.

| Field | Value / rule |
| --- | --- |
| `og:title` | Page title (may be slightly longer/less brand-heavy than `<title>`) |
| `og:description` | Compelling summary (can mirror meta description) |
| `og:type` | `website` (or `article` for blog posts) |
| `og:url` | The page's **canonical** absolute URL |
| `og:site_name` | `{{BRAND_NAME}}` |
| `og:image` | Absolute URL, **1200×630 (1.91:1)**, < 5 MB, with `og:image:alt` |
| `og:image:width` / `og:image:height` | `1200` / `630` |
| `og:locale` | e.g. `en_US` |
| `twitter:card` | `summary_large_image` |
| `twitter:title` / `twitter:description` / `twitter:image` | Mirror OG (image may reuse `og:image`) |
| `twitter:image:alt` | Describe the image |
| `twitter:site` / `twitter:creator` | `{{SOCIAL_X_HANDLE}}` (optional) |

Per-page OG images are encouraged; a branded default is the fallback (see [`../brand/imagery.md`](../brand/imagery.md)). Keep the safe zone clear of edges.

---

## 9. Content quality & E-E-A-T

Content relevance + E-E-A-T + authority **dominate** rankings; on-page structure makes them legible. Google rewards helpful, people-first content.

**E-E-A-T on the page (make trust crawlable):**

| Signal | How to show it on-page |
| --- | --- |
| **Experience** | First-hand specifics: real results, screenshots, before/after response times, client outcomes |
| **Expertise** | Named authors/team with roles; accurate, specific how-it-works detail; cite stats with sources |
| **Authoritativeness** | Testimonials, logos, case studies, review counts, `sameAs` profile links |
| **Trustworthiness** | Accurate plain-text **NAP**, clear pricing/next step, guarantees/SLAs, privacy/terms links, visible "humans on call" proof |

**Content rules**

- [ ] Every page has a **single clear primary intent** (from [`seo-strategy.md`](./seo-strategy.md) funnel map) and satisfies it fully.
- [ ] **Extractable answer near the top:** 1–2 sentence direct answer to the page's core question (wins snippets + AI citations).
- [ ] Use the **brand voice** (clear, direct, benefit-led, second person, short sentences, no hype) — see [`../00-foundations/brand-strategy.md`](../00-foundations/brand-strategy.md).
- [ ] **Prose measure ≤ 68ch**, body line-height ≥ 1.5, base font ≥ 16px (readability = engagement).
- [ ] **Cite stats** with a source; keep the **speed-to-lead / slow-follow-up entity framing** consistent (entity consistency is a top AI-visibility correlate).
- [ ] **Dates:** show published/updated dates on articles; keep them truthful.
- [ ] **FAQ blocks** on key pages (pair with FAQ schema — see `structured-data.md`).
- [ ] No thin/duplicate pages; no city-swap doorway clones (see [`seo-strategy.md`](./seo-strategy.md) §6).

---

## 10. Reusable `<head>` meta template

Copy-paste per page; replace `{{...}}` placeholders and the `PAGE_*` slots. Order matters: charset/viewport first, then title, then canonical, then hints/preloads (resource hints belong at the **top** of `<head>` — see [`technical-seo.md`](./technical-seo.md) / performance doc). Structured-data JSON-LD is added separately per `structured-data.md`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Title: ≤60 chars, primary keyword first 30–35, brand at end -->
  <title>PAGE_TITLE | {{BRAND_NAME}}</title>

  <!-- Meta description: ~150–160 chars, unique, accurate, soft CTA -->
  <meta name="description" content="PAGE_META_DESCRIPTION">

  <!-- Canonical: self-referencing, absolute, correct trailing-slash style -->
  <link rel="canonical" href="https://{{DOMAIN}}/PAGE_PATH/">

  <!-- Indexing (default indexable). For non-indexable pages use noindex,follow -->
  <meta name="robots" content="index,follow,max-image-preview:large">

  <!-- Resource hints (top of head, surgical: ≤4–6 preconnect origins) -->
  <link rel="preconnect" href="https://{{DOMAIN}}" crossorigin>
  <!-- <link rel="preconnect" href="https://fonts.example.com" crossorigin> -->
  <!-- Preload the LCP image + critical font (never lazy-load the LCP image) -->
  <!-- <link rel="preload" as="image" href="/img/hero.avif" fetchpriority="high"> -->
  <!-- <link rel="preload" as="font" type="font/woff2" href="/fonts/inter.woff2" crossorigin> -->

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{{BRAND_NAME}}">
  <meta property="og:title" content="PAGE_OG_TITLE">
  <meta property="og:description" content="PAGE_OG_DESCRIPTION">
  <meta property="og:url" content="https://{{DOMAIN}}/PAGE_PATH/">
  <meta property="og:image" content="https://{{DOMAIN}}/og/PAGE_OG_IMAGE.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="PAGE_OG_IMAGE_ALT">
  <meta property="og:locale" content="en_US">

  <!-- Twitter / X -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="PAGE_OG_TITLE">
  <meta name="twitter:description" content="PAGE_OG_DESCRIPTION">
  <meta name="twitter:image" content="https://{{DOMAIN}}/og/PAGE_OG_IMAGE.png">
  <meta name="twitter:image:alt" content="PAGE_OG_IMAGE_ALT">
  <!-- <meta name="twitter:site" content="{{SOCIAL_X_HANDLE}}"> -->

  <!-- Favicons / theme -->
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta name="theme-color" content="#4F46E5"><!-- --color-brand-600 -->

  <!-- hreflang (only if multi-language; must be reciprocal + x-default) -->
  <!-- <link rel="alternate" hreflang="en" href="https://{{DOMAIN}}/PAGE_PATH/"> -->
  <!-- <link rel="alternate" hreflang="x-default" href="https://{{DOMAIN}}/PAGE_PATH/"> -->

  <!-- JSON-LD structured data: add per structured-data.md (Organization/
       LocalBusiness on all pages; Service/FAQ/Breadcrumb per page type) -->
</head>
```

> The `theme-color` uses the literal brand hex because HTML `<meta>` can't read CSS tokens. It must equal `--color-brand-600` (`#4F46E5`). This is the one sanctioned raw-hex exception in this doc.

---

## 11. Per-page SEO acceptance checklist

Run before shipping **every** page. A page isn't done until all boxes are checked.

**Metadata**
- [ ] `<title>` unique, ≤ 60 chars / < ~600px, keyword in first 30–35 chars, brand at end
- [ ] `<meta name="description">` unique, ~150–160 chars, accurate, soft CTA
- [ ] Self-referencing `<link rel="canonical">` (absolute, correct trailing-slash style)
- [ ] `<meta name="robots">` correct (index vs noindex intentional)

**Structure**
- [ ] Exactly one `<h1>` = page's core topic
- [ ] Heading hierarchy logical, no skipped levels
- [ ] Semantic HTML5 landmarks; one `<main>`
- [ ] Descriptive keyword-bearing URL; no params/dates/IDs
- [ ] Full content + headings + links + schema present in **mobile HTML**

**Links & media**
- [ ] Descriptive internal-link anchors; hub↔spoke; page reachable (no orphan); links point to canonicals
- [ ] Contextual link into the book-a-call path (no dead-end)
- [ ] All meaningful images have real `alt`; decorative = `alt=""`
- [ ] Every image has explicit width/height (no CLS); LCP image eager + `fetchpriority="high"`; below-fold lazy

**Social & schema**
- [ ] OG + Twitter tags complete; image 1200×630; `twitter:card=summary_large_image`; `og:url` = canonical
- [ ] JSON-LD present per `structured-data.md` (no schema myths relied on)

**Content & E-E-A-T**
- [ ] Single clear primary intent, fully satisfied; brand voice; extractable answer near top
- [ ] E-E-A-T signals present (named humans, proof/stats-with-sources, accurate NAP, dates)
- [ ] Prose ≤ 68ch, body line-height ≥ 1.5, base ≥ 16px
- [ ] Not thin/duplicate; not a city-swap clone

---

## Related

- [`seo-strategy.md`](./seo-strategy.md) — themes, architecture, funnel/intent, how layers fit.
- [`technical-seo.md`](./technical-seo.md) — canonicals, robots, sitemaps, redirects, mobile-first, monitoring.
- [`structured-data.md`](./structured-data.md) — JSON-LD entities to add to the `<head>`.
- [`ai-seo-geo.md`](./ai-seo-geo.md) — extractable answers, entity clarity, AI-answer visibility.
- [`seo-strategy.md`](./seo-strategy.md) — SEO system overview and standards index.
- [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md) — semantic HTML, alt text, headings for a11y.
- [`../performance/performance-budget.md`](../performance/performance-budget.md) — image formats, LCP, CLS, resource hints.
- [`../brand/imagery.md`](../brand/imagery.md) — OG image export, alt-over-image guidance.
- [`../00-foundations/brand-strategy.md`](../00-foundations/brand-strategy.md) — voice for on-page copy.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — `theme-color` brand value.
