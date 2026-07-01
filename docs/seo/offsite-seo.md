# Off-Site & Local Authority SEO

**Purpose:** A prescriptive playbook for building off-site authority and local presence for a service/agency — Google Business Profile optimization, NAP consistency, citations & directories, compliant review generation/response, safe backlink & digital-PR tactics, social profiles/`sameAs`, brand-SERP control, and measurement — so any future session earns trust/authority signals (the dominant driver of both rankings and AI visibility) without triggering spam filters or the April 2026 review policy.
**Status:** v1 foundation — adjustable.

---

> **Scope note:** This is an authority-building systems doc, **not** page copy and **not** page building. It complements on-page ([`onsite-seo.md`](./onsite-seo.md)) and GEO ([`ai-seo-geo.md`](./ai-seo-geo.md)).
> **Why off-site dominates in 2026:** Off-site signals (brand mentions, YouTube mentions, branded search) correlate with AI visibility ~3× more strongly than backlinks (~0.664 vs ~0.218). Google's local ranking is governed by **relevance, distance, and prominence** — and prominence is built off-site (links, mentions, reviews). This is where trust is earned.

---

## 0. TL;DR — off-site authority in one screen

- [ ] **Own the entity, not just links.** NAP + `sameAs` + `LocalBusiness` schema feed Google's Knowledge Graph and AI answers. Consistency across GBP, Wikipedia/Wikidata, and social profiles determines what AI says about us. See [`ai-seo-geo.md`](./ai-seo-geo.md) §5.
- [ ] **Google Business Profile is the #1 local asset.** Verify it, pick the **most specific primary category** + only **2–3** relevant secondaries, and fill **every** field. Fully-managed profiles see ~67% more views and ~43% more website clicks.
- [ ] **NAP consistency is an entity-verification signal.** One master format everywhere; fixing inconsistencies has shown ~16% ranking lift.
- [ ] **Citations: authority > volume.** One authoritative niche citation (e.g., BBB) can carry ~10–15× the weight of a generic free directory. Stop chasing hundreds of low-value listings.
- [ ] **Reviews are policy-sensitive now.** Google's **April 2026** update **bans review gating, on-site/kiosk collection, incentives, and quotas**. Use compliant QR/link asks + reply to **>70%** of reviews.
- [ ] **Links: lead with digital PR + original data.** Rated the top white-hat tactic by ~48.6% of SEOs. Diversify so no single tactic exceeds ~30–40% of the profile.
- [ ] **Trust SpamBrain; don't reflexively disavow.** Google auto-neutralizes toxic links; ~99.9% of sites never need the disavow tool.
- [ ] **Control the brand SERP** as a distributed, AI-read trust layer — a multi-quarter program (~18-month roadmap), not a quick fix.

---

## 1. Google Business Profile (GBP) optimization checklist

GBP is the highest-leverage local asset. Google's local ranking = **relevance** (profile matches query) + **distance** (proximity) + **prominence** (how well-known, via links + reviews). We can't change distance; we maximize relevance and prominence.

### 1.1 Setup & verification

- [ ] **Claim and verify** the profile; keep the verification method current.
- [ ] Represent the business **as it appears in the real world** (signage/branding) — name must not add keywords or location it isn't branded with.
- [ ] Set the **exact business name** = our master NAP name (no keyword stuffing — a policy violation).

### 1.2 Categories (the single most influential on-profile field)

~4,046 categories exist (May 2026). ~86% of GBP views reportedly come from category/discovery searches vs brand-name searches.

- [ ] **Primary category:** the **most specific** applicable (e.g., a precise service category, not a broad umbrella).
- [ ] **Secondary categories:** add only **2–3** highly relevant ones (max is 1 primary + 9 secondary).
- [ ] **Do not** category-stuff — over-categorization triggers quality filters and can cause **suspension**.

### 1.3 Fill every field (completeness correlates with visibility)

| Field | Do | Watch out |
| --- | --- | --- |
| **Services** | List each service explicitly | Match site service names |
| **Products** | Add if applicable | Keep accurate |
| **Attributes** | Set all true attributes | Don't claim false ones |
| **Hours** | Keep current, incl. holidays | Stale hours hurt trust + ranking |
| **Booking link** | Add the book-a-call link | Point to a working URL |
| **Description** | Plain, benefit-led summary | **No links, promo language, prices, or gimmicky characters** (policy) |
| **Photos** | Real, high-quality; pro photos ~35% more clicks | No stock/misleading images |
| **Q&A** | Seed real FAQs, monitor + answer | Don't leave spam answers up |

> **Industry data:** fully-managed profiles see ~67% more views and ~43% more website clicks than basic listings.

### 1.4 GBP posts (engagement, not pack rank)

- [ ] Post ~**2–3×/week** (cited ~34% higher engagement vs monthly). Posts lift panel CTR/actions but **do not** directly move local-pack position.

### 1.5 Local Services Ads (optional paid layer)

- [ ] Consider **Google Local Services Ads** (now the **"Google Verified"** badge, post-Oct 2025) for pay-per-lead visibility **above** the organic map pack. Benchmark home-services cost/lead ~**$53** (typical $25–$130+; HVAC ~$45–80, plumbing ~$35–65, electrical ~$40–75, roofing ~$55–90).

---

## 2. NAP consistency (an entity signal, not just directory hygiene)

Google's 2026 local algorithm uses **AI entity verification, Knowledge Graph data, and multi-source consistency checks**. Inconsistent NAP weakens the entity and what AI Overviews/ChatGPT/Perplexity say about us.

- [ ] **Define one master NAP format** and use it **verbatim** everywhere. Store it in [`../00-foundations/project-brief.md`](../00-foundations/project-brief.md) as the source of truth.

```
{{BRAND_NAME}}
{{ADDRESS}}
{{CITY}}, {{REGION}} {{POSTAL}}
{{COUNTRY}}
{{PHONE}}   ·   {{EMAIL}}
```

- [ ] Match this **exactly** in: site footer + Contact (plain crawlable text), `LocalBusiness`/`Organization` schema, `llms.txt`, GBP, Bing Places, Apple Maps, and every citation.
- [ ] **Consistency rules:** identical abbreviations (St. vs Street), suite format, phone format, and legal vs trade name. Pick one and never vary it.
- [ ] Fixing NAP inconsistencies has shown ~**16% ranking lift** — audit and correct before chasing new citations.

> **Cross-reference:** on-site NAP + `LocalBusiness`/`Organization` schema **corroborates** GBP and the Knowledge Graph. Never put NAP only in an image or JS. Schema details in [`structured-data.md`](./structured-data.md); entity/NAP for AI in [`ai-seo-geo.md`](./ai-seo-geo.md).

---

## 3. Citations & directories (authority > volume)

A "citation" is any web mention of our NAP. In 2026, **quality beats quantity** — authoritative niche/industry citations carry ~**10–15×** the ranking weight of generic free directories, and low-value volume has **diminishing returns**.

**Priority order:**

1. **Core mapping/data** — Google Business Profile, Bing Places, Apple Business Connect (feed the big entity graphs).
2. **Authoritative/industry** — BBB, relevant industry associations, Chamber of Commerce, high-authority niche directories for our verticals (med spa, dental, home services, real estate, coaching, agency directories).
3. **Trusted general** — a small set of reputable general directories (e.g., Yelp where relevant to the vertical).
4. **Data aggregators** — where they feed downstream listings in our market.

**Do / Don't**

| Do | Don't |
| --- | --- |
| Prioritize a **short list** of authoritative, relevant citations | Blast NAP to hundreds of free directories |
| Keep every citation's NAP **identical** to master | Let format drift across listings |
| Audit existing citations and **fix/merge** duplicates | Create duplicate GBPs or listings |
| Choose citations relevant to our **industry + area** | Chase volume for its own sake (diminishing returns) |

---

## 4. Reviews — generation & response (2026 policy-compliant)

Reviews drive **prominence** (a Google local factor) and buyer trust. But Google's **April 2026** review policy is strict and enforces **retroactively**.

### 4.1 What's now BANNED (April 2026 update)

Google added **pre-publication screening** (rolled out April 16–17, 2026), **location-proximity filters**, and **account-history verification** (testing began March 2026). Prohibited:

| Banned tactic | Why it's out |
| --- | --- |
| **Review gating** (screening for happy customers before asking) | Prohibited; can strip reviews retroactively |
| **On-site/kiosk/tablet collection** (shared device on premises) | Proximity filters flag/remove these |
| **Incentives** — discounts, gifts, loyalty points, refunds for reviews | Prohibited |
| **Mandated content** — requiring an employee's name or specific wording | Prohibited |
| **Review quotas** for staff | Prohibited |

> Enforcement can apply **retroactively** to already-posted non-compliant reviews. Audit and stop any of the above immediately.

### 4.2 Compliant review generation

- [ ] Use the **official GBP review link / QR code** on receipts, invoices, and follow-up **email/SMS** (off-premise, customer's own device).
- [ ] Ask **everyone** (universal request), not just happy customers (no gating).
- [ ] Aim for a **steady, natural cadence** over ~90 days — a burst-then-silence pattern underperforms. ~73% of consumers trust only reviews from the **last 30 days**, so keep velocity **year-round**.
- [ ] Never incentivize, script, or quota reviews.

### 4.3 Respond to every review (fully compliant + a strong "actively managed" signal)

- [ ] **Reply rate target: >70%.** Profiles replying to >70% reportedly win ~2.1× more leads than those replying to <30%.
- [ ] **Reply fast** — within ~1 hour is tied to ~34% higher CTR vs >24h.
- [ ] **Positive:** thank + reinforce the specific outcome (books more calls, faster follow-up).
- [ ] **Negative:** stay calm, acknowledge, offer to resolve offline, keep the human-support tone. Never argue or reveal private details.

### 4.4 Review schema — the honest pointer

- [ ] **Do NOT** add self-serving `Review`/`AggregateRating` (star) markup to our **own** `LocalBusiness`/`Organization` schema — Google has **not** shown self-serving review stars since Sept 2019; it's ignored, and fabricated reviews risk a **spam manual action**. Rely on **GBP** for star display in Maps/local pack. Full rules in [`structured-data.md`](./structured-data.md).

### 4.5 Review benchmarks

| Metric | Target | Note |
| --- | --- | --- |
| Reviews for local-pack competitiveness | **10+** min, **50+** competitive | 50+ reportedly wins ~4.4× more clicks than <5 |
| Reply rate | **>70%** | ~2.1× more leads vs <30% |
| Reply speed | **~1 hour** | ~34% higher CTR vs >24h |
| Recency | **steady, last 30 days** | ~73% trust only last-month reviews |

---

## 5. Safe backlinks & digital PR (avoid spam/penalties)

Links still help authority at the top end (>32,000 referring domains ≈ ~3.5× more likely to be AI-cited), but **brand mentions correlate ~3× stronger than backlinks** for AI visibility. Earn links the safe way; earn **mentions** even more.

### 5.1 White-hat tactics (in priority order)

| Tactic | Why | Note |
| --- | --- | --- |
| **Digital PR + original data study** | Rated top white-hat tactic by ~48.6% of SEOs | Pitch data-driven stories (our own response-time/booking data) |
| **Expert commentary** (HARO / Qwoted / Featured.com) | Earns editorial links **and** E-E-A-T | Named, credentialed responses |
| **Broken-link building** | ~17% success rate | Relevant resource pages only |
| **Genuine partnerships / integrations** | Natural, relevant links | Integration/partner pages of tools we support |
| **Unlinked brand mentions → relationships** | Feed AI visibility + PR | Even *unlinked* mentions correlate strongly |

### 5.2 Diversification & safety rules

- [ ] **No single tactic > ~30–40%** of the link profile — diversify.
- [ ] Keep **anchor text natural** (branded/URL/natural phrases; avoid exact-match commercial anchors at scale).
- [ ] Prioritize **relevance + authority** over raw count.
- [ ] Earn **YouTube mentions** (titles/transcripts/descriptions) — the **strongest** 2026 AI-visibility correlate (~0.737).

### 5.3 What NOT to do (spam-policy violations)

| Don't | Consequence |
| --- | --- |
| Buy links / use PBNs | Spam policy violation; caught in real time |
| Mass low-quality paid guest posts | Devalued/penalized |
| **Site reputation abuse** (renting a host site's authority) | Explicit policy violation (Nov 2024 update) |
| Farm inauthentic mentions/links | Doesn't move real signals; spam risk |

### 5.4 Disavow — almost never

- [ ] **Do NOT reflexively disavow.** Google's **SpamBrain** auto-neutralizes manipulative links; ~**99.9%** of sites never need the tool. Reserve disavow **only** for an active/imminent **manual action** for unnatural links. (Tool still active as of March 2026, but treat as last resort.)

---

## 6. Social profiles & `sameAs`

Social profiles are entity + NAP corroboration and `sameAs` targets that strengthen Knowledge Graph disambiguation and AI brand summaries.

- [ ] Claim official profiles: LinkedIn, Facebook, Instagram, X, **YouTube** (highest AI-visibility correlate), plus any vertical-relevant network.
- [ ] Use **identical NAP + description** on each (see §2).
- [ ] Add each verified profile to `Organization` **`sameAs`** in schema, using full canonical URLs — only profiles we actually control. Placeholders: `{{SOCIAL_LINKEDIN}}`, `{{SOCIAL_FACEBOOK}}`, `{{SOCIAL_INSTAGRAM}}`, `{{SOCIAL_X}}`, `{{SOCIAL_YOUTUBE}}`. (Markup in [`structured-data.md`](./structured-data.md).)
- [ ] Include Wikipedia/Wikidata and Crunchbase in `sameAs` **if** we genuinely have entries — do not fabricate.

---

## 7. Brand SERP control (the distributed trust layer)

The brand SERP (what appears when someone searches "{{BRAND_NAME}}") is a **distributed, AI-read trust layer / RAG source**, not a single page. Owning it is a **multi-quarter program (~18-month roadmap, ~9 controllable elements)**.

- [ ] **Knowledge Panel** — earn a complete panel via consistent entity data (Organization schema, GBP, Wikidata, `sameAs`).
- [ ] **Own page-1 results** — homepage, About, GBP, key social profiles, positive third-party mentions.
- [ ] **Sitelinks** — clean site architecture + strong internal linking (see [`seo-strategy.md`](./seo-strategy.md)).
- [ ] **Reviews surface** — GBP rating visible; positive third-party review presence.
- [ ] **Suppress/outrank** any stale or negative result with better-optimized owned assets over time.
- [ ] Keep **all entity data consistent** — the panel and AI brand summaries read from the same well.

---

## 8. Measurement

| What | Tool | Cadence | Note |
| --- | --- | --- | --- |
| GBP views, searches, actions, calls | GBP Insights / Performance | Monthly | Category/discovery vs direct split |
| Local-pack + local rankings | Rank tracker (geo-gridded) | Monthly | Distance affects results |
| Reviews: count, rating, recency, reply rate | GBP + review tools | Weekly | Reply rate **>70%**, recency last 30 days |
| Citations: coverage + NAP accuracy | Citation audit tool | Quarterly | Fix inconsistencies (authority-first) |
| Backlinks + referring domains | Backlink tool | Monthly | Watch tactic diversification (<30–40% each) |
| **Brand mentions** (linked + unlinked) | Brand monitoring | Monthly | Top AI-visibility correlate |
| Branded search volume | GSC + keyword tools | Monthly | Leading demand/authority indicator |
| Brand SERP state | Manual review | Quarterly | Panel completeness, page-1 ownership |
| Local-search → booked calls | Analytics + booking tool | Weekly | The real KPI (~33% local-search conversion in 2026) |

---

## 9. Off-site acceptance checklist

Before treating off-site/local as "done":

- [ ] **GBP** verified; **most specific primary category** + only 2–3 secondaries; **every field** filled; description has **no links/promo/prices**.
- [ ] GBP posts cadence ~2–3×/week set up (engagement, not pack rank).
- [ ] **NAP master format** defined and **identical** across site, schema, `llms.txt`, GBP, Bing Places, Apple, and all citations.
- [ ] Citations = a **short authoritative** list (BBB/industry/local), NAP-consistent; duplicates fixed.
- [ ] Review workflow is **policy-compliant** (no gating/kiosk/incentives/quotas); official link/QR on invoices + follow-up email/SMS; universal ask; steady velocity.
- [ ] **Reply rate >70%**, fast replies; positive + negative handled with the human-support tone.
- [ ] **No self-serving `Review`/`AggregateRating`** markup on our own `LocalBusiness`/`Organization` schema.
- [ ] Backlink plan leads with **digital PR + original data + expert commentary**; no tactic >30–40%; natural anchors.
- [ ] **No spam tactics** (bought links/PBNs/site-reputation-abuse); **no reflexive disavow**.
- [ ] Social profiles claimed with consistent NAP; verified profiles in `sameAs`.
- [ ] **Brand SERP** program underway (Knowledge Panel + page-1 ownership + reviews surface).
- [ ] Measurement wired to **booked calls, brand mentions, and branded search** — not vanity metrics.

---

## Sources

- Google Business Profile Help — *Tips to improve your local ranking* (`support.google.com/business/answer/7091`)
- Google Business Profile Help — *Guidelines for representing your business* (`answer/3038177`)
- Google Business Profile Help — *Prohibited & restricted content* (`answer/7400114`); *Policy overview* (`answer/13762416`)
- Google Search Central — *Spam Policies for Google Web Search*; *Updating our site reputation abuse policy* (Nov 2024)
- Google Maps UGC Policy (April 2026 review update) — via Birdeye / Mainstreethost / Three Chapter Media
- Ahrefs — *AI brand visibility correlations* (75,000-brand study; mentions ~0.664 vs links ~0.218)
- BuzzStream / Blue Tree Digital / SEOEngico (2026) — digital-PR effectiveness; GetMeLinks / GSQI — disavow/SpamBrain

---

## Related

- [`seo-strategy.md`](./seo-strategy.md) — overall search strategy; where off-site authority fits in the four-layer system.
- [`ai-seo-geo.md`](./ai-seo-geo.md) — GEO / AI-answer optimization; entity + NAP for AI, brand mentions as top correlate.
- [`onsite-seo.md`](./onsite-seo.md) — on-page relevance, E-E-A-T on the page.
- [`technical-seo.md`](./technical-seo.md) — crawlability, indexing, NAP in crawlable text, mobile-first.
- [`structured-data.md`](./structured-data.md) — `LocalBusiness`/`Organization`/`sameAs` markup; why self-serving review stars don't show.
- [`../00-foundations/project-brief.md`](../00-foundations/project-brief.md) — business, audience, NAP source of truth.
- [`../../public-templates/robots.txt`](../../public-templates/robots.txt) — crawl directives + sitemap pointer.
