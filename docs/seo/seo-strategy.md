# SEO Strategy

**Purpose:** The overall search strategy for the {{BRAND_NAME}} marketing site — goals, keyword themes, site architecture, funnel/intent mapping, and how onsite, technical, offsite, and GEO layers fit together — so any future session builds pages that rank and convert instead of guessing.
**Status:** v1 foundation — adjustable.

---

> **Scope note:** This is a strategy/systems doc, **not** final page copy and **not** page building. Keyword *themes* below are directions, not final titles or H1s. Turn them into copy later, per page, using [`onsite-seo.md`](./onsite-seo.md).
> **Business context source of truth:** [`../00-foundations/project-brief.md`](../00-foundations/project-brief.md). This doc inherits audience, offer, and promise from there and does not redefine them.

---

## 0. TL;DR — the strategy in one screen

- [ ] We are a **local + niche service/agency**, not a SaaS or a national e-commerce brand. Strategy = **own the entity "slow lead follow-up / speed-to-lead"** for our service industries and locations.
- [ ] **Four keyword themes** (not final copy): *speed-to-lead*, *AI receptionist / answering*, *appointment setting / booking*, *lead-response automation*. Map each to a page, not a scattered blog.
- [ ] **Architecture is intent-shaped:** Home → Services → Use-cases/Industries → Pricing → About → Contact → Blog → Location pages. Every page has a single primary intent and a single primary CTA (book a call).
- [ ] **Four layers, one system:** on-page relevance ([`onsite-seo.md`](./onsite-seo.md)) + technical crawlability ([`technical-seo.md`](./technical-seo.md)) + off-site authority/brand mentions + GEO/AI-answer optimization. Content + E-E-A-T + authority dominate; Core Web Vitals is a **tiebreaker**, not a lever.
- [ ] **NAP consistency** (Name / Address / Phone) is a first-class ranking + trust signal — identical plain-text across site, schema, and Google Business Profile. See [`technical-seo.md`](./technical-seo.md).
- [ ] **Location pages are differentiated, not city-swapped clones** — local proof, reviews, service-area detail, embedded map. Doorway clones get filtered as thin.
- [ ] Success = **booked calls from organic + AI-answer citations**, not vanity rankings.

---

## 1. Goals & KPIs

SEO exists to feed the primary conversion goal from the project brief: **book a call**. Rankings are a means, not the goal.

| Priority | SEO goal | Primary KPI | Leading indicator |
| --- | --- | --- | --- |
| 1 | Booked calls from organic | Organic → booked-call conversions | Organic sessions to money pages |
| 2 | Rank for high-intent service + local queries | Positions/impressions for target themes | Coverage of themes in GSC |
| 3 | Be cited by AI answer engines (GEO) | Brand mentions/citations in AI Overviews, ChatGPT, Perplexity | Branded search volume, unlinked mentions |
| 4 | Build topical authority + E-E-A-T | Non-branded impressions growth | Indexed helpful pages, quality backlinks/mentions |

**Do / Don't**

| Do | Don't |
| --- | --- |
| Optimize money pages (services, industries, pricing, contact, locations) first | Start with a blog and hope it ranks for commercial terms |
| Measure to **booked calls**, tied back to landing page | Chase keyword rankings with no conversion path |
| Treat branded search + unlinked brand mentions as a KPI (top AI-visibility correlate) | Obsess over backlink counts alone (brand mentions correlate ~3× stronger for AI visibility) |
| Expect field-data (CrUX/GSC) changes to lag ~28 days | Expect same-day movement after a fix |

> **Myth guard:** Do **not** rely on `llms.txt` or schema to "multiply" AI citations — both are debunked (Google; Ahrefs 1,885-page test). Ship them where they add real value (see GEO), but don't budget ranking on them.

---

## 2. Keyword themes (directions, not final copy)

Four themes map to the four pillars of the promise. Each theme owns a page (or page cluster). **These are directions** — write actual titles/H1s per page in [`onsite-seo.md`](./onsite-seo.md), front-loading the primary keyword and keeping titles ≤ 60 chars.

| # | Theme | Intent | Owns (primary page) | Modifiers to work in |
| --- | --- | --- | --- | --- |
| 1 | **Speed-to-lead** | Problem-aware, commercial | Home + "speed-to-lead" pillar | *respond to leads in seconds, lead response time, first-responder wins, missed lead recovery* |
| 2 | **AI receptionist / answering** | Solution-aware, commercial | Service: AI assistant / receptionist | *AI receptionist, AI answering service, 24/7 AI chat/SMS, virtual front desk* |
| 3 | **Appointment setting / booking** | Solution-aware, commercial | Service: appointment setting | *AI appointment setting, auto-book appointments, calendar booking bot, no-show reduction* |
| 4 | **Lead-response automation** | Solution/vendor-aware | Service: lead-response automation | *automated lead follow-up, lead nurture automation, CRM lead response, inbound lead automation* |

**Modifier layers** (combine with themes to generate long-tail, per page — never in one stuffed page):

- **Industry modifiers:** med spa, dental/clinic, HVAC/plumbing/roofing (home services), real estate, coaches, agencies.
- **Local modifiers:** {{CITY}}, {{REGION}}, "near me", service-area names.
- **Buyer-language modifiers:** "done for you", "managed", "with human support", "for [industry]", "vs [manual/other]".

**Intent classes we target (and how we serve each):**

| Intent | Example query shape | Page type that wins |
| --- | --- | --- |
| Commercial-investigation | "best AI appointment setting for med spas" | Industry use-case page |
| Transactional/hire | "AI receptionist service {{CITY}}" | Location page / service page |
| Problem-aware | "how to respond to leads faster" | Blog pillar → CTA to service |
| Comparison | "AI receptionist vs answering service" | Comparison/blog page → service |
| Branded | "{{BRAND_NAME}} pricing / reviews" | Pricing / About / testimonials |

> **Anti-cannibalization rule:** one theme = one primary page. If two pages could rank for the same query, merge them or make one clearly the target (internal links + canonical intent). Don't publish three near-identical "AI receptionist" pages.

---

## 3. Site & page architecture

Flat, shallow, intent-shaped. Aim for **≤ 3 clicks** from home to any money page. Every page inherits from a single primary intent and funnels to **book a call**.

```
/                         Home ......................... speed-to-lead promise + all paths
├── /services/            Services hub ................. overview + links to each service
│   ├── /services/ai-receptionist/        Theme 2
│   ├── /services/appointment-setting/    Theme 3
│   └── /services/lead-response-automation/ Theme 4
├── /industries/          Use-cases hub ................ overview + links to each industry
│   ├── /industries/med-spas/
│   ├── /industries/dental-clinics/
│   ├── /industries/home-services/
│   ├── /industries/real-estate/
│   ├── /industries/coaches/
│   └── /industries/agencies/            (white-label/partner)
├── /pricing/             Pricing ...................... plans + book-a-call CTA
├── /about/              About ........................ E-E-A-T: team, story, proof, humans
├── /contact/            Contact ...................... NAP, form, book-a-call, map
├── /blog/               Blog hub ..................... pillars + supporting posts
│   ├── /blog/[pillar]/                   speed-to-lead pillar, etc.
│   └── /blog/[post]/
└── /locations/          Locations hub (if multi-area)
    ├── /locations/{{city}}/              differentiated local pages
    └── ...
```

**Architecture rules**

| Rule | Why |
| --- | --- |
| Hub-and-spoke: a hub page links to every child; children link back up and laterally | Distributes authority; helps crawl + topical clustering |
| Descriptive, lowercase, hyphenated URLs; keyword in slug; no dates/IDs | Readability + relevance; stable canonicals |
| One primary intent + one primary CTA per page | No dead-ends; every page feeds book-a-call |
| Services vs Industries are a **matrix**, not duplication | Service = *what we do*; Industry = *who it's for*. Cross-link, don't clone |
| Location pages only if we genuinely serve/differentiate the area | City-swap clones = doorway/thin risk (see §6) |
| Breadcrumbs on all deep pages (with `BreadcrumbList` schema — see `structured-data.md`) | Crawl clarity + SERP breadcrumbs |

**Services × Industries matrix (how to avoid duplication):** each *service* page describes the mechanism; each *industry* page describes the outcome for that buyer and links to the relevant services. If you need "AI receptionist for med spas," make it a section on the **industry** page linking to the **service** page — not a third standalone page.

---

## 4. Funnel & conversion-intent mapping

Map every page to a funnel stage so content depth and CTA match intent. Primary CTA is always **book a call**; secondary CTAs feed it.

| Funnel stage | Visitor mindset | Page types | Content job | Primary CTA | Secondary CTA |
| --- | --- | --- | --- | --- | --- |
| **TOFU** (problem-aware) | "I'm losing leads / responding too slow" | Blog pillars, speed-to-lead content, Home top | Frame the problem, cite stats, teach | Book a call | Get the speed-to-lead playbook (email) |
| **MOFU** (solution-aware) | "What solves this? Is AI right?" | Service pages, industry use-cases, comparisons | Show the mechanism, proof, integrations, human backup | Book a call / Get a demo | Watch 2-min demo, ROI calculator |
| **BOFU** (vendor-aware) | "Is {{BRAND_NAME}} the right vendor?" | Pricing, About, testimonials, contact, location | De-risk: proof, humans, SLAs, guarantees, local trust | Book a call | Try a live chat, request pricing |

**Intent → content depth rules**

- BOFU/commercial pages: concise, proof-dense, extractable one-line answers near the top (good for humans and AI Overviews), clear pricing/next-step. Don't bury the CTA.
- TOFU/blog: genuinely helpful, first-hand (E-E-A-T), cites stats, ends with a contextual CTA into the matching MOFU page — never a dead-end.
- Every page answers "**what do you want me to do next?**" above the fold and again at the end.

> **Extractable-answer pattern (serves SEO + GEO):** open key pages with a 1–2 sentence direct answer to the page's core question (e.g. "An AI receptionist answers, qualifies, and books your inbound leads in seconds, 24/7."). This wins featured snippets and AI-answer citations. See [`onsite-seo.md`](./onsite-seo.md) content section.

---

## 5. How the layers fit together

SEO here is **four layers, one system**. No single layer wins alone; content + authority dominate, technical is table-stakes, CWV is a tiebreaker.

| Layer | Owns | Doc | One-line role |
| --- | --- | --- | --- |
| **On-page / on-site** | Relevance, structure, metadata, internal links, E-E-A-T on the page | [`onsite-seo.md`](./onsite-seo.md) | Tell Google & readers *exactly* what each page is about and why to trust it |
| **Technical** | Crawlability, indexing, canonicals, sitemaps, redirects, mobile-first, page experience | [`technical-seo.md`](./technical-seo.md) | Make sure the right pages get crawled, indexed, and rendered correctly |
| **Structured data** | Machine-readable entities: LocalBusiness/Service/FAQ/Breadcrumb | `structured-data.md` (see [`../seo/`](../seo/)) | Make entities + NAP + FAQs machine-readable for Search & AI |
| **Off-site** | Authority, brand mentions, citations, GBP, reviews | (off-site playbook) | Earn trust/authority signals; brand mentions ≈ 3× backlinks for AI visibility |
| **GEO / AI-SEO** | Answer-engine visibility, extractable answers, entity clarity | [`ai-seo-geo.md`](./ai-seo-geo.md) | Get cited in AI Overviews / ChatGPT / Perplexity |

**Priority order when time is limited:** (1) content relevance + E-E-A-T on money pages → (2) technical crawl/index correctness → (3) structured data + NAP consistency → (4) off-site brand mentions + reviews → (5) GEO extractability → (6) Core Web Vitals polish (tiebreaker). Poor CWV can *cap* gains; excellent CWV can't *rescue* weak content.

**Dependency chain (what blocks what):**

```
Technical (crawl/index/render OK)  ── enables ──▶  On-page relevance can be seen
On-page + Structured data          ── enables ──▶  Entity clarity + rich results
Entity clarity + Off-site mentions ── enables ──▶  Authority + AI-answer citations
All of the above + CWV tiebreaker  ── enables ──▶  Competitive rankings → booked calls
```

---

## 6. Local SEO strategy (service-area/agency)

Because our buyers search locally and by industry, local signals matter.

- [ ] **NAP consistency** — identical Name / Address / Phone in plain crawlable text on Contact + footer, in `LocalBusiness` schema, and in Google Business Profile / Bing Places / Apple Maps. Google cross-checks schema against GBP. Never put NAP only in an image or JS. (Details: [`technical-seo.md`](./technical-seo.md).)
- [ ] **Specific `LocalBusiness` subtype** where it fits (`ProfessionalService`), with `sameAs` to profiles, rather than generic `LocalBusiness`. (See `structured-data.md`.)
- [ ] **Google Business Profile** claimed, categorized, with real reviews, photos, and services — a top local ranking + trust asset.
- [ ] **Differentiated location pages** (see rule below), only where we truly serve the area.

**Location-page differentiation rule (avoid doorway/thin filtering):**

| Include (real, per-area) | Avoid (clone signals) |
| --- | --- |
| Local reviews/testimonials, project/results photos | Only the city name swapped in a template |
| Specific service-area detail (neighborhoods, coverage) | Copy-pasted boilerplate with `{{CITY}}` find-replaced |
| Embedded map + local NAP | No unique local proof or content |
| Industry proof relevant to that area | Auto-generated pages for cities we don't serve |

Thin/near-duplicate city pages are increasingly filtered as doorway content — build fewer, genuinely local pages.

---

## 7. Measurement & iteration

| What | Tool | Cadence | Note |
| --- | --- | --- | --- |
| Coverage, queries, positions, index status | Google Search Console | Weekly | Field data lags ~28 days; don't panic on short windows |
| Core Web Vitals (field) | GSC CWV report + CrUX/RUM | Monthly | p75 mobile + desktop; 28-day rolling |
| Booked calls by landing page | Analytics + booking tool | Weekly | The real KPI — tie organic to bookings |
| Branded search + unlinked mentions | GSC + brand monitoring | Monthly | Leading indicator of authority + AI visibility |
| AI-answer citations | Manual/monitoring across AI engines | Monthly | GEO KPI (see [`ai-seo-geo.md`](./ai-seo-geo.md)) |

**Iteration loop:** ship money pages → verify indexing (Technical) → check queries/CTR in GSC → improve titles/meta/content where CTR or position lags → earn mentions/reviews → re-check after the 28-day field window.

---

## 8. Strategy acceptance checklist

Before treating the site's SEO foundation as "done":

- [ ] Every keyword theme (§2) maps to exactly one primary page — no cannibalization.
- [ ] Architecture (§3) is flat (≤ 3 clicks to money pages), hub-and-spoke, descriptive URLs.
- [ ] Every page has one primary intent + one primary CTA (book a call); no dead-ends.
- [ ] Funnel mapping (§4) done: each page tagged TOFU/MOFU/BOFU with matching depth + CTA.
- [ ] Money pages open with an extractable one-line answer.
- [ ] NAP is consistent across site, schema, and GBP (§6).
- [ ] Location pages (if any) are genuinely differentiated, not city-swap clones.
- [ ] On-page ([`onsite-seo.md`](./onsite-seo.md)) and technical ([`technical-seo.md`](./technical-seo.md)) checklists pass per page.
- [ ] Structured data planned (`structured-data.md`); GEO extractability planned ([`ai-seo-geo.md`](./ai-seo-geo.md)).
- [ ] No reliance on debunked myths (llms.txt/schema "multiplying" citations; LCP "2.0s"; INP "primary signal").

---

## Related

- [`onsite-seo.md`](./onsite-seo.md) — on-page checklist, meta template, E-E-A-T, per-page acceptance.
- [`technical-seo.md`](./technical-seo.md) — crawlability, sitemaps, canonicals, redirects, mobile-first, monitoring.
- [`ai-seo-geo.md`](./ai-seo-geo.md) — GEO / AI-answer-engine optimization.
- [`offsite-seo.md`](./offsite-seo.md) — Google Business Profile, citations, reviews, authority.
- [`structured-data.md`](./structured-data.md) — JSON-LD entities: LocalBusiness/Service/FAQ/Breadcrumb.
- [`../00-foundations/project-brief.md`](../00-foundations/project-brief.md) — business, audience, offer, conversion goals.
- [`../performance/performance-budget.md`](../performance/performance-budget.md) — Core Web Vitals budgets referenced here.
- [`../../public-templates/robots.txt`](../../public-templates/robots.txt) — crawl directives + sitemap pointer.
- [`../../public-templates/sitemap.xml`](../../public-templates/sitemap.xml) — sitemap index template.
