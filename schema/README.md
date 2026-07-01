# Schema (JSON-LD) Templates

**Purpose:** Copy-paste JSON-LD structured-data templates for the {{BRAND_NAME}} site, plus exactly how to embed them, find-and-replace the placeholders, and validate them before and after publishing.
**Status:** v1 foundation — adjustable.

---

> **Strategy & where each type goes** lives in [`../docs/seo/structured-data.md`](../docs/seo/structured-data.md). This README is the operational how-to for the files in this folder. Read the strategy doc first to know *which* templates a given page needs.

---

## 1. What's in this folder

| File | `@type` | Scope | Put it on |
| --- | --- | --- | --- |
| [`organization.jsonld`](./organization.jsonld) | `Organization` | Site-wide | Homepage (or every page via `@id`) |
| [`localbusiness.jsonld`](./localbusiness.jsonld) | `ProfessionalService` | Site-wide | Homepage + Contact page |
| [`website.jsonld`](./website.jsonld) | `WebSite` + `SearchAction` | Site-wide | Homepage |
| [`service.jsonld`](./service.jsonld) | `Service` + `Offer` | Per-page | Each service page |
| [`faqpage.jsonld`](./faqpage.jsonld) | `FAQPage` | Per-page | FAQ page / pages with a visible FAQ |
| [`breadcrumb.jsonld`](./breadcrumb.jsonld) | `BreadcrumbList` | Per-page | Every non-home page |
| [`review.jsonld`](./review.jsonld) | `AggregateRating` + `Review` | Per-page | See ⚠️ below |

⚠️ **`review.jsonld` will NOT produce star rich results about your own agency.** Google has ignored self-serving Review/AggregateRating on an entity's own `Organization`/`LocalBusiness` since 2019, and fabricated reviews risk a manual action. It is included here only for pages that review *another* entity or a supported type. See [structured-data.md §7](../docs/seo/structured-data.md) before you ship it.

---

## 2. How to embed (in the `<head>`)

Each template is a standalone JSON-LD block. Wrap the file contents in a script tag and place it in the `<head>` (preferred) or `<body>`. **Server-render / statically include it** — do not rely on client-side injection, which is less reliable to crawl.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Your Brand"
  /* ...paste the rest of organization.jsonld here (remove this comment; JSON has no comments) ... */
}
</script>
```

**Rules:**

- [ ] `type="application/ld+json"` exactly (not `text/javascript`, not `application/json`).
- [ ] One `<script>` per top-level object, **or** combine multiple objects into a single script using a `@graph` array (see §4).
- [ ] **No JavaScript comments and no trailing commas** inside the JSON — the `/* ... */` above is illustrative only; strip it.
- [ ] Same markup must be present in the **mobile-rendered HTML** (mobile-first indexing).
- [ ] Everything you mark up must be **visible to the user on that page** (prices, ratings, FAQ answers, breadcrumb labels).

---

## 3. Find-and-replace the placeholders

Every `{{PLACEHOLDER}}` is a string you must replace before publishing. Do a global find-and-replace across all `.jsonld` files.

| Placeholder | Replace with | Example |
| --- | --- | --- |
| `{{BRAND_NAME}}` | Public brand name | `Acme AI` |
| `{{LEGAL_ENTITY}}` | Registered legal name | `Acme AI, LLC` |
| `{{DOMAIN}}` | Bare domain, no scheme/slash | `example.com` |
| `{{EMAIL}}` | Public contact email | `hello@example.com` |
| `{{PHONE}}` | E.164 phone | `+1-555-123-4567` |
| `{{ADDRESS}}` | Street address | `123 Main St, Suite 4` |
| `{{CITY}}` / `{{REGION}}` / `{{POSTAL}}` | City / state-province / ZIP | `Austin` / `TX` / `78701` |
| `{{COUNTRY}}` | ISO 3166-1 alpha-2 | `US` |
| `{{LATITUDE}}` / `{{LONGITUDE}}` | Geo coordinates (decimal) | `30.2672` / `-97.7431` |
| `{{SOCIAL_LINKEDIN}}` … `{{SOCIAL_YOUTUBE}}` | Full profile URLs you control | `https://linkedin.com/company/acme-ai` |
| `{{SETUP_PRICE}}` / `{{MONTHLY_PRICE}}` | Numeric price, no currency symbol | `1500` / `499` |
| `{{VAT_ID}}` `{{ISO6523_CODE}}` `{{DUNS}}` `{{LEI_CODE}}` `{{NAICS}}` | Business identifiers (optional) | leave out if unknown |
| `{{REVIEW_AUTHOR_1}}` / `{{REVIEW_AUTHOR_2}}` | Real reviewer names | `Jordan P.` |

**Cleanup after replacing:**

- [ ] **Delete any property you cannot fill with a real value.** Do not ship an empty string, a `{{PLACEHOLDER}}`, or a fake value. Better to omit a recommended field than to lie in it.
- [ ] Delete the optional identifier block (`vatID`, `iso6523Code`, `duns`, `leiCode`, `naics`) entirely if you have none — do not leave placeholders.
- [ ] Keep NAP (name, address, phone) **byte-for-byte identical** to your Google Business Profile and site footer.
- [ ] `sameAs` should list **only** profiles you actually own; remove the rest.

---

## 4. Combine into one `@graph` (recommended)

Rather than several script tags, emit one graph so nodes can reference each other by `@id`. This avoids duplicating the business block on every page.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    { /* organization.jsonld object (define once, site-wide) */ },
    { /* website.jsonld object */ },
    { /* localbusiness.jsonld object */ },
    { /* per-page: service.jsonld / breadcrumb.jsonld / faqpage.jsonld */ }
  ]
}
</script>
```

Inside a graph, reference the shared org node instead of repeating it:

```json
{ "@type": "Service", "provider": { "@id": "https://example.com/#organization" } }
```

---

## 5. Validate — before publishing AND after every template/CMS change

Two tools, both required:

1. **Rich Results Test** — <https://search.google.com/test/rich-results> — confirms Google *eligibility* for supported rich results (Breadcrumb here). Test the live URL after deploy and the raw code before.
2. **Schema Markup Validator** — <https://validator.schema.org/> — validates schema.org *syntax/types* even for types with no Google rich result (Organization, Service, LocalBusiness).

**Quick local JSON sanity check** (catches the #1 mistake — broken JSON):

```bash
for f in schema/*.jsonld; do python3 -c "import json,sys; json.load(open('$f'))" \
  && echo "VALID   $f" || echo "INVALID $f"; done
```

**Checklist per template:**

- [ ] JSON parses (no missing commas, unbalanced brackets, unescaped quotes, trailing commas).
- [ ] No `{{PLACEHOLDER}}` remains.
- [ ] Rich Results Test: 0 errors (warnings acceptable if the field is genuinely absent).
- [ ] Schema Markup Validator: 0 errors.
- [ ] Every value in the markup is **visible on the rendered page**.
- [ ] After publish: re-test the live URL, then watch Search Console → Enhancements / Rich results for new errors or valid-item drops.

---

## Related

- [`../docs/seo/structured-data.md`](../docs/seo/structured-data.md) — full structured-data strategy, per-type property tables, and rich-result eligibility.
- [`../docs/seo/technical-seo.md`](../docs/seo/technical-seo.md) — crawl/index rules (mobile-first, canonicals, sitemaps).
- [`../docs/seo/onsite-seo.md`](../docs/seo/onsite-seo.md) — on-page tags (titles, meta, OG/Twitter) that pair with this markup.
- [`../docs/seo/seo-strategy.md`](../docs/seo/seo-strategy.md) — site architecture and content themes.
