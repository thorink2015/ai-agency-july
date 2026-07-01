# Content Publish Checklist

**Purpose:** The editorial gate for {{BRAND_NAME}} content (blog posts, guides, case studies, resource pages) — everything to verify for editorial quality, GEO/SEO, schema, and accessibility **before** hitting publish, so content earns rankings and AI citations instead of drifting.
**Status:** v1 foundation — adjustable.

---

> **How to use:** Run per article before publishing. Content quality, E-E-A-T, and originality dominate — GEO/SEO structure only amplifies genuinely helpful content. AI answer engines reward extractable, well-sourced, up-to-date content; **quality beats volume** (8–12 strong pieces/month outperform 50+ thin ones). See [`../docs/seo/ai-seo-geo.md`](../docs/seo/ai-seo-geo.md) and [`../docs/systems/content-workflow.md`](../docs/systems/content-workflow.md).

## 1. Editorial quality (P0)

- [ ] One clear reader + one search intent; the piece actually answers it.
- [ ] Original, first-hand value: our own data, examples, screenshots, or POV — not a rewrite of page-1 results.
- [ ] Brand voice: clear, direct, benefit-led, second person, short sentences, jargon-light, confident-not-hypey.
- [ ] Proofread: spelling/grammar clean, no placeholder/lorem text, no broken {{PLACEHOLDER}} left in body copy.
- [ ] Accurate and current: claims true as of the publish date; no outdated stats or dead product references.
- [ ] Clear CTA relevant to the topic (book a call / related service) without turning the piece into an ad.

## 2. E-E-A-T & trust signals (P0)

- [ ] Named author byline with real credentials/experience; links to an author/about page.
- [ ] `datePublished` (and `dateModified` on updates) shown to readers and in schema.
- [ ] External claims cite **credible, primary** sources with links; internal claims link to our relevant pages.
- [ ] Consistent Organization/entity info; NAP (if present) matches site/schema/GBP exactly.

## 3. GEO / AI-answer optimization

See [`../docs/seo/ai-seo-geo.md`](../docs/seo/ai-seo-geo.md). Structure content to be **extractable and liftable** by AI engines (helps Bing/ChatGPT/Perplexity; harmless for Google, which runs on core ranking).

- [ ] Question-style `H2`/`H3` headings that mirror how users actually phrase queries.
- [ ] Key answer **front-loaded**: each section opens with a self-contained 2–4 line answer that stands alone if lifted.
- [ ] "Citation magnets" present: ~**1 specific statistic/figure per 150–200 words**, each attributed to a named source.
- [ ] At least one direct quotation or cited primary source where it strengthens authority.
- [ ] Sections are self-contained ~100–300-word passages (single idea each) for passage-level retrieval.
- [ ] Do NOT rely on `llms.txt`, schema, or "chunking hacks" for citations — no major engine uses them as inputs; earned quality and brand mentions do.
- [ ] Off-site amplification planned (digital PR, YouTube mention, social) — brand mentions correlate with AI visibility ~3× more than backlinks.

## 4. On-page SEO

See [`../docs/seo/onsite-seo.md`](../docs/seo/onsite-seo.md).

- [ ] `<title>` <= ~60 chars, primary keyword front-loaded; unique, non-duplicative.
- [ ] Meta description <= ~155 chars, unique, compelling, accurate to the content.
- [ ] Clean keyword-relevant slug; self-referencing `rel=canonical`; not a near-duplicate of an existing URL.
- [ ] Single `H1`; logical heading hierarchy (no skipped levels).
- [ ] 2–5 descriptive contextual internal links per ~1,000 words (no "click here"); link to money/service pages where relevant.
- [ ] Primary keyword + natural synonyms used; **no keyword stuffing**.
- [ ] Added to `sitemap.xml` with real `<lastmod>`; internal links from relevant existing pages point in.

## 5. Media & accessibility (P0)

See [`../docs/accessibility/accessibility-standards.md`](../docs/accessibility/accessibility-standards.md) and [`../docs/performance/image-optimization.md`](../docs/performance/image-optimization.md).

- [ ] Every image has accurate `alt` (decorative = `alt=""`); descriptive filenames.
- [ ] Images AVIF/WebP, compressed to budget (content < 100 KB), explicit `width`/`height` (no CLS); below-fold `loading="lazy"`.
- [ ] Embeds/videos have titles/captions; no autoplay-with-sound; motion respects `prefers-reduced-motion`.
- [ ] Contrast >= 4.5:1 for any custom-colored text/callouts; meaning not by color alone.
- [ ] Readable measure (~68ch), body line-height >= 1.5, real heading structure for screen-reader navigation.

## 6. Social & schema

- [ ] OG + Twitter tags set for the article; `summary_large_image` with a 1200×630 image + alt; share preview checked.
- [ ] `Article`/`BlogPosting` JSON-LD with headline, author, `datePublished`, `dateModified`, image, publisher.
- [ ] `FAQPage` schema only if a **visible** FAQ block exists; `BreadcrumbList` present. Validates with **0 errors** (Rich Results Test).

## 7. Final pre-publish

- [ ] Preview on mobile + desktop; all links resolve (200); no console errors.
- [ ] Reviewed/approved per [`../docs/systems/content-workflow.md`](../docs/systems/content-workflow.md).
- [ ] Post-publish: request indexing (GSC), confirm Bing can crawl it, and schedule a freshness review (cornerstone content updated regularly).

---

## Related

- [`pre-launch.md`](./pre-launch.md)
- [`new-page.md`](./new-page.md)
- [`quality-gates.md`](./quality-gates.md)
- [`../docs/seo/ai-seo-geo.md`](../docs/seo/ai-seo-geo.md)
- [`../docs/seo/onsite-seo.md`](../docs/seo/onsite-seo.md)
- [`../docs/systems/content-workflow.md`](../docs/systems/content-workflow.md)
- [`../docs/accessibility/accessibility-standards.md`](../docs/accessibility/accessibility-standards.md)
