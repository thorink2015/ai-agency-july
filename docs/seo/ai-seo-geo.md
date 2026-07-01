# AI SEO / Generative Engine Optimization (GEO)

**Purpose:** A prescriptive playbook for earning citations and visibility in AI answer engines (Google AI Overviews/AI Mode, ChatGPT, Perplexity, Gemini) — how they pick and cite sources, the truth about `llms.txt`, how to structure extractable content, entity/NAP clarity, E-E-A-T signals, and a GEO acceptance checklist — so any future session optimizes for real 2026 signals instead of debunked hacks.
**Status:** v1 foundation — adjustable.

---

> **Scope note:** This is a systems/optimization doc, **not** page copy and **not** page building. It tells you *how* to write and structure so AI engines cite us; write the actual copy per page in [`onsite-seo.md`](./onsite-seo.md).
> **One-sentence thesis:** In 2026, GEO ≈ great SEO + off-site brand presence + genuinely extractable, well-sourced content. There is no separate "AI hack" — dedicated AI-only files and schema tricks do not move citations.

---

## 0. TL;DR — GEO in one screen

- [ ] **GEO is not separate from SEO for Google.** Google states AI Overviews/AI Mode run on core Search ranking + quality systems; there is **no special schema or file** to add. Good SEO *is* the optimization.
- [ ] **`llms.txt` does nothing for ranking or AI citations.** Google confirmed (June 15, 2026) it "won't harm nor help." No major engine uses it as an input. We ship a minimal one for humans/context only — never budget results on it.
- [ ] **Schema does NOT causally multiply citations.** Ahrefs' controlled 1,885-page test: adding schema barely moved citations on any platform. The "3.2× more citations" claims are correlation, not causation. Still add schema for *real* rich-result/entity value (see [`structured-data.md`](./structured-data.md)) — just not as an AI-citation lever.
- [ ] **Off-site brand presence beats links for AI visibility.** Brand mentions correlate ~**0.664** vs backlinks ~**0.218** (~3×); YouTube mentions correlate highest (~**0.737**). Earn unlinked mentions, digital PR, and video presence — see [`offsite-seo.md`](./offsite-seo.md).
- [ ] **Add Princeton "citation magnets."** Statistics, direct quotes from named credible sources, and inline citations lift AI visibility up to **+40%** (lower-ranked pages gain most). Aim ~**1 sourced stat per 150–200 words**.
- [ ] **Write extractable, self-contained passages** for Bing/ChatGPT/Perplexity: question-style H2/H3 that mirror real queries, one idea per 2–4 line block, answer front-loaded (100–300 word "liftable" sections). *Exception:* Google says to ignore deliberate "chunking" for its own AI features — so this is an engine-specific structure, not a Google hack.
- [ ] **Optimize per engine — overlap is near-zero.** Only ~**11%** of domains are cited by both ChatGPT and Perplexity; ~**1.4%** cited-URL overlap across four engines. Get indexed in **Bing** (powers ChatGPT search), not just Google.
- [ ] **Shift KPIs.** With ~**48%** of Google queries showing an AI Overview and ~**65–69%** zero-click, measure **citations, brand mentions, and branded/assisted demand**, not just clicks.

---

## 1. How AI answer engines pick & cite sources (2026)

AI answers are **retrieval-augmented**: the engine retrieves candidate passages/pages, then the model synthesizes an answer and cites a subset. What gets retrieved and cited differs sharply by engine.

| Engine | Retrieval / index it draws on | Notable citation behavior | What this means for us |
| --- | --- | --- | --- |
| **Google AI Overviews / AI Mode** | Core Google index + ranking/quality systems | ~17–38% of AIO citations come from the organic top 10 — **most come from outside it**; only ~1% of users click a link *inside* the AIO | Win with core SEO fundamentals + E-E-A-T; being top-10 helps but isn't required. Do **not** add AI-only files/chunking for Google. |
| **ChatGPT search (SearchGPT)** | **Bing** index; `ChatGPT-User` fetches pages live | ~87% of citations match a Bing result, but Bing top-3 predicts the actual citation only ~6.8–7.8% — indexing is necessary, rank is not sufficient. Draws ~47.9% of citations from Wikipedia | **Get and stay indexed in Bing.** Strengthen the Wikipedia/entity layer. Extractable passages help live-fetch synthesis. |
| **Perplexity** | Own near-daily-refreshed index + live web | Historically ~46.7% of citations from Reddit (down ~86% after the Oct 2025 Reddit lawsuit); rewards **freshness** heavily | Publish/refresh cornerstone content regularly; earn credible community + editorial mentions. |
| **Gemini** | Google index + Google-Extended-gated data | Follows core Google signals; entity clarity + authority dominate | Same fundamentals as Google; keep entity data consistent across the web. |

**The three things every engine rewards (in order):**

1. **Trust / authority of the source** — E-E-A-T signals AI can verify: real authors with credentials, consistent entity data across the web, original data, clear sourcing. Trust is the dominant factor.
2. **Off-site brand presence** — unlinked brand mentions, YouTube mentions, branded search. These out-correlate backlinks ~3× for AI visibility.
3. **On-page extractability + sourcing** — self-contained answers with statistics, quotes, and citations the model can lift and attribute.

> **Necessary vs sufficient:** Being indexed (Google *and* Bing) and crawlable by answer bots is **necessary**. Authority + extractable, sourced content is what makes you **cited**. Neither alone is enough.

---

## 2. AI crawler access — don't accidentally block citation eligibility

Answer engines can only cite what their **search/answer** crawlers can fetch. A common, silent failure is blocking training bots and catching the answer bots too. Verify in [`../../public-templates/robots.txt`](../../public-templates/robots.txt).

| Bot | Purpose | Default stance | Notes |
| --- | --- | --- | --- |
| `Googlebot` | Google Search + AI Overviews/AI Mode | **Allow** | Blocking = no Google visibility at all. |
| `Google-Extended` | Gemini/Vertex **training** (not Search) | Allow (our choice) | Disallowing does **not** remove Google Search/AIO eligibility. |
| `OAI-SearchBot` | ChatGPT **search** citations | **Allow** | Block this and you lose ChatGPT citation eligibility. |
| `ChatGPT-User` | Live page fetch during a ChatGPT answer | **Allow** | Needed for on-demand retrieval. |
| `GPTBot` | OpenAI **training** | Optional | Can disallow training without losing `OAI-SearchBot` search citations. |
| `PerplexityBot` | Perplexity indexing/citations | **Allow** | Block = no Perplexity citations. |
| `Claude-SearchBot` | Claude **search** citations | **Allow** | Answer-engine access. |
| `ClaudeBot` | Anthropic **training** | Optional | Training vs search are separate agents. |
| `Bingbot` | Bing index (**powers ChatGPT search**) | **Allow** | Necessary for ChatGPT visibility. |

**Do / Don't**

| Do | Don't |
| --- | --- |
| Keep search/answer bots (`OAI-SearchBot`, `PerplexityBot`, `Claude-SearchBot`, `Bingbot`, `Googlebot`) **allowed** | Blanket-`Disallow` all bots to "stop AI scraping" and silently kill citation eligibility |
| Separate **training** opt-outs (`GPTBot`, `ClaudeBot`, `Google-Extended`) from **search** access if you must opt out | Assume disallowing `Google-Extended` removes you from Google Search/AIO — it doesn't |
| Re-check robots.txt after any CMS/hosting change | Rely on robots.txt to control *indexing* (use `noindex` for that) |

---

## 3. `llms.txt` — what it is, the truth, and how we author ours

**What it is:** A proposed plain-text/Markdown file at the site root (`/llms.txt`) meant to give LLMs a curated, machine-friendly map of your most important pages and context.

**The truth (2026):**

- Adoption ~**10%** of sites (late 2025). **No major AI vendor** (Google, OpenAI, Anthropic, Meta, Mistral) uses it as a ranking or citation input.
- Google (June 15, 2026, *"Clarifying guidance on llms.txt files"*): site owners don't need machine-readable/AI text files/Markdown because **"Google Search itself doesn't use them,"** and maintaining one **"won't harm (nor help)"** visibility.

**So why ship one at all?** As a low-cost, human-and-tooling-friendly index and a place to state entity facts (NAP, what we do, canonical links). **Treat it as optional context, never a ranking lever.** Reference template: [`../../public-templates/llms.txt`](../../public-templates/llms.txt).

**How to author `llms.txt` (if we ship it):**

```markdown
# {{BRAND_NAME}}

> AI appointment-setting & lead-response agency. We deploy and manage AI
> chat/SMS/web assistants that answer, qualify, and book inbound leads in
> seconds, 24/7, with human support on call.

## Core pages
- [Services](https://example.com/services/): AI receptionist, appointment setting, lead-response automation
- [Pricing](https://example.com/pricing/): plans and how to get started
- [Industries](https://example.com/industries/): med spas, dental, home services, real estate, coaches, agencies
- [About](https://example.com/about/): team, expertise, human-support model
- [Contact](https://example.com/contact/): {{PHONE}} · {{EMAIL}} · {{ADDRESS}}

## Key facts
- Founded: {{FOUNDING_YEAR}} · Serves: {{REGION}}, {{COUNTRY}}
- NAP: {{BRAND_NAME}}, {{ADDRESS}}, {{CITY}}, {{REGION}} {{POSTAL}}, {{PHONE}}
```

**Rules for our `llms.txt`:** use absolute `https://{{DOMAIN}}` URLs; keep NAP **identical** to site/schema/GBP (§5); no keyword stuffing; keep it short and current; do **not** disallow it in robots.txt. If maintaining it ever slips, delete it rather than let it go stale.

---

## 4. Content structure for extractability (the part that actually helps)

AI retrieval for Bing/ChatGPT/Perplexity often operates at **passage/chunk level** — ~100–300 word sections that semantically match a query. Make every key section a complete, liftable answer.

> **Google caveat:** Google explicitly says to **ignore deliberate "chunking"** for its own AI features — for Google, this structure is just good writing, not a required tactic. The techniques below help Bing/ChatGPT/Perplexity and never hurt Google, so apply them site-wide as *quality*, not as a Google hack.

### 4.1 The extractable-passage pattern

| Element | Rule | Example |
| --- | --- | --- |
| **Question-style heading** | H2/H3 phrased as the real user query | `## How fast should you respond to a new lead?` |
| **Front-loaded answer** | First 1–2 sentences answer it completely, standalone | "Respond within 5 minutes. Leads contacted in the first 5 minutes are far more likely to convert than those contacted an hour later." |
| **Single idea per block** | 2–4 lines, one concept, self-contained | No "as mentioned above" — each block stands alone |
| **Passage size** | Keep self-contained sections ~100–300 words | A model can lift the whole section as one answer |
| **Definitions** | Define key terms in a sentence AI can quote | "Speed-to-lead is the elapsed time between a lead arriving and your first response." |

### 4.2 Citation magnets (Princeton GEO — up to +40% visibility)

The Princeton GEO study (KDD 2024, GEO-bench, 10,000 queries) found the highest-impact tactics were **Statistics Addition, Quotation Addition, and Cite Sources** — up to **+40%** visibility, with a measured **+115%** relative lift for a 5th-ranked page that added citations. **Lower-ranked pages gain the most.**

- [ ] **Statistics:** ~**1 specific stat/percentage/figure per 150–200 words**, each with source attribution.
- [ ] **Quotations:** direct quotes from **named, credible** sources (studies, recognized experts) — not anonymous filler.
- [ ] **Cite sources:** inline citation/link to the **primary** source of each stat or claim.
- [ ] **Tables:** use tables for comparisons, specs, and stat sets — highly extractable and quotable.
- [ ] **FAQ blocks:** cluster real questions with concise upfront answers (see §4.3).

**Do / Don't**

| Do | Don't |
| --- | --- |
| Cite a **primary** source and the year for every stat | Cite a stat with no source (models won't trust/lift it) |
| Front-load the answer, then explain | Bury the answer under 300 words of preamble |
| One idea per short block; each self-contained | Write long "as we saw above" chains that don't stand alone |
| Add stats/quotes only where genuinely relevant | Sprinkle fake or unsourced numbers to game it (spam risk) |

### 4.3 FAQ schema — status and honest guidance

`FAQPage` **rich results are gone** (Google stopped showing them May 7, 2026; tooling support removed mid-2026). **Do not add `FAQPage` schema expecting a Google rich result.**

**But keep the FAQ *content pattern*** — question-led H2/H3 + concise upfront answers is exactly the extractable structure AI engines reward. So:

- [ ] Write real FAQ **content** (questions users actually ask) with 2–4 line front-loaded answers.
- [ ] Do **not** rely on `FAQPage` markup for a visual snippet; it no longer renders. (See [`structured-data.md`](./structured-data.md) for what schema still earns rich results.)
- [ ] Keep answers visible on the page (never markup-only, never hidden).

---

## 5. Entity clarity & consistent NAP

AI engines build an **entity** understanding of your brand from many sources (site, GBP, Wikipedia/Wikidata, review sites, social). Contradictions weaken the entity and what AI says about you.

- [ ] **One master NAP format** — identical Name / Address / Phone in plain crawlable text on Contact + footer, in `LocalBusiness`/`Organization` schema, in GBP, and in `llms.txt`. Google cross-checks schema against GBP.
- [ ] **`sameAs`** on Organization schema pointing to verified profiles you control (LinkedIn, Facebook, Instagram, X, YouTube, Wikipedia/Wikidata, Crunchbase, GBP) — reinforces entity identity for the Knowledge Graph and AI summaries. (See [`structured-data.md`](./structured-data.md).)
- [ ] **Consistent business description** across the web — same core promise and category language everywhere ("AI appointment-setting & lead-response agency").
- [ ] **Entity presence off-site** — a clean, complete brand SERP + Knowledge Panel acts as a distributed trust layer AI reads (RAG source). See [`offsite-seo.md`](./offsite-seo.md).

> **Why it matters for GEO specifically:** ChatGPT draws ~47.9% of citations from Wikipedia; entity data on Wikipedia/Wikidata and consistent NAP directly shape brand summaries in AI answers.

---

## 6. E-E-A-T & author/expertise signals AI can verify

Trust is the dominant citation factor. Make expertise **machine-verifiable**, not just asserted.

| Signal | Do this | Why |
| --- | --- | --- |
| **Real bylines** | Name real authors with credentials + a bio; link an author page | AI and raters can verify who is speaking |
| **First-hand experience** | Show real deployments, screenshots, results, "we did X" | "Experience" is the first E in E-E-A-T |
| **Original data** | Publish first-party stats (our own response-time/booking data) | Original research is a strong citation magnet |
| **Consistent Organization identity** | Same name/logo/description across web, Wikidata, review sites | Entity disambiguation → trust |
| **Clear sourcing** | Cite primary sources for external claims | Verifiable = quotable |
| **Named human backup** | State the human-support model + who's accountable | Reinforces our differentiator + trust |

**Do / Don't**

| Do | Don't |
| --- | --- |
| Attribute content to a real, credentialed person | Publish faceless "admin" content on YMYL-adjacent topics |
| Cite primary sources and link them | Cite "studies show" with no reference |
| Build genuine authority (mentions, PR, reviews) | Treat E-E-A-T as an on-page "score" you toggle |

---

## 7. What to do vs myths (the GEO myth guard)

| Myth / mistake | Reality (2026) | What to do instead |
| --- | --- | --- |
| "Publish `llms.txt` to rank / get cited" | No engine uses it as input; Google says it "won't harm nor help" | Ship a minimal one for context only; expect **zero** ranking effect |
| "Schema multiplies AI citations 2.5–3.2×" | Ahrefs' 1,885-page controlled test: citations barely moved; the 3× is correlation | Add schema for real rich-result/entity value, **not** as an AI lever |
| "GEO is a separate discipline with AI-only hacks" | Google's AI features run on core ranking; same fundamentals apply | Do great SEO + off-site brand + extractable sourcing |
| "Deliberately chunk/rewrite content for machines" | Google says **ignore** chunking for its AI features (helps Bing/ChatGPT/Perplexity though) | Write naturally extractable content as *quality*, engine-aware |
| "Publish 50+ posts/month to win citations" | 50+/month showed **no** advantage over 8–12 high-quality posts | Fewer, deeper, better-sourced pieces |
| "Backlinks are the main AI-visibility driver" | Brand mentions correlate ~3× stronger (0.664 vs 0.218) | Earn mentions, digital PR, YouTube presence |
| "Farm mentions/links to fake signals" | Spam systems catch it; doesn't move real citations | Earn credible, editorial mentions |
| "Keyword-stuff for the model" | Models handle synonyms/meaning; stuffing hurts extractability | Write clearly for one idea per block |
| "FAQ schema gets a rich snippet" | `FAQPage` rich results ended May 7, 2026 | Keep FAQ *content*; drop reliance on the markup |

---

## 8. Per-engine quick-reference

| Engine | Get indexed / crawlable | Highest-leverage move | Measure |
| --- | --- | --- | --- |
| **Google AIO / AI Mode** | `Googlebot` allowed; strong core SEO | E-E-A-T + fundamentals on money pages | GSC generative-AI impression reports |
| **ChatGPT search** | **Bing indexed** + `OAI-SearchBot`/`ChatGPT-User` allowed | Bing presence + Wikipedia/entity layer + extractable passages | Manual citation checks / AI-visibility trackers |
| **Perplexity** | `PerplexityBot` allowed | **Freshness** + credible community/editorial mentions | Manual checks; watch recency |
| **Gemini** | `Googlebot` allowed (Google-Extended per goals) | Same as Google + consistent entity data | GSC + manual checks |

> **Overlap reminder:** ~11% domain overlap (ChatGPT↔Perplexity), ~1.4% URL overlap across four engines. Treat each as a **separate channel** with separate measurement.

---

## 9. Measurement — shift KPIs from clicks to citations

Clicks are structurally declining: ~**48%** of Google queries show an AI Overview (up ~58% YoY), ~**65–69%** of searches are zero-click, and position-1 CTR drops ~**37.5%** when an AIO is present. But being **cited** in an AIO lifts CTR ~**+35%** vs not cited. So measure presence, not just clicks.

| KPI | Source | Cadence | Note |
| --- | --- | --- | --- |
| AI Overview impressions/clicks | GSC generative-AI performance reports | Weekly | New Search Console reports (2026) |
| AI-answer citations (per engine) | Manual checks + AI-visibility trackers | Monthly | Track ChatGPT/Perplexity/Gemini separately |
| Brand mentions (linked + unlinked) | Brand monitoring | Monthly | Top AI-visibility correlate |
| Branded search volume | GSC + keyword tools | Monthly | Leading demand indicator |
| Bing indexation | Bing Webmaster Tools | Monthly | Necessary for ChatGPT |
| Assisted/branded booked calls | Analytics + booking tool | Weekly | The real business KPI |

---

## 10. GEO acceptance checklist

Before treating a page/site as "GEO-ready":

- [ ] Indexed in **both** Google and **Bing**; verified in GSC + Bing Webmaster Tools.
- [ ] robots.txt allows search/answer bots (`Googlebot`, `OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `Claude-SearchBot`, `Bingbot`); training opt-outs (if any) don't block them.
- [ ] Key sections use **question-style headings** mirroring real queries, with **front-loaded** answers.
- [ ] Content is built from **self-contained 100–300 word passages**, one idea per 2–4 line block.
- [ ] ~**1 sourced statistic per 150–200 words**; every stat has a **primary source** + year.
- [ ] At least one **direct quote** from a named credible source where relevant.
- [ ] Comparisons/specs presented as **tables**; FAQ *content* present (no reliance on `FAQPage` rich results).
- [ ] **NAP identical** across site, `Organization`/`LocalBusiness` schema, GBP, and `llms.txt`.
- [ ] `sameAs` links to verified profiles; entity description consistent across the web.
- [ ] Real **author byline + credentials**; first-hand experience and original data present.
- [ ] Off-site plan active (mentions, digital PR, YouTube, reviews) — see [`offsite-seo.md`](./offsite-seo.md).
- [ ] **No reliance on debunked myths:** `llms.txt`/schema "multiplying" citations; AI-only chunking as a Google hack; volume over quality; `FAQPage` rich snippets.
- [ ] KPIs shifted to **citations + mentions + branded/assisted demand**, tracked per engine.

---

## Sources

- Google — *Optimizing for Generative AI Features on Google Search*: `developers.google.com/search/docs/fundamentals/ai-optimization-guide`
- Google Search Central Blog (May 2026) — *A new resource for optimizing for generative AI*
- Google Search Central Blog (June 2026) — *Search Generative AI performance reports in Search Console*
- Google — *Creating Helpful, Reliable, People-First Content (E-E-A-T)*
- Search Engine Land — *Google says llms.txt files won't harm or help your search rankings*
- Ahrefs — *We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved.*
- Ahrefs — *AI brand visibility correlations* (75,000-brand study)
- Princeton/Georgia Tech/IIT Delhi — *GEO: Generative Engine Optimization* (KDD 2024)
- Seer Interactive — SearchGPT/Bing citation analysis; OpenAI — *Introducing ChatGPT search*

---

## Related

- [`seo-strategy.md`](./seo-strategy.md) — overall search strategy; where GEO fits in the four-layer system.
- [`onsite-seo.md`](./onsite-seo.md) — on-page copy, extractable-answer pattern, E-E-A-T on the page.
- [`technical-seo.md`](./technical-seo.md) — indexing, crawlability, robots.txt strategy, mobile-first.
- [`offsite-seo.md`](./offsite-seo.md) — off-site authority, brand mentions, GBP, reviews (top AI-visibility correlate).
- [`structured-data.md`](./structured-data.md) — JSON-LD entities, `Organization`/`sameAs`, what still earns rich results.
- [`../00-foundations/project-brief.md`](../00-foundations/project-brief.md) — business, audience, offer, promise (entity source of truth).
- [`../../public-templates/robots.txt`](../../public-templates/robots.txt) — crawl directives incl. AI/answer bots.
- [`../../public-templates/llms.txt`](../../public-templates/llms.txt) — optional AI-context file template.
