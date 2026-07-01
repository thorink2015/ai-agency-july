# Memory System

**Purpose:** Define this repository as a retrieval-first "memory" for the brand/website program — how a future Claude session or teammate FINDS the right doc, TRUSTS the right source, and UPDATES memory without drift.
**Status:** v1 foundation — adjustable.

---

> **Read this first if you are new (human or model).** This repo is a knowledge base, not an app. Every decision, standard, token, and template lives here so the next session can retrieve and apply it without re-deriving it. Start at `CLAUDE.md`, follow the index, and never guess a value that a doc or token already specifies.

---

## 0. TL;DR — the three rules

- [ ] **Retrieve top-down.** Always start at [`CLAUDE.md`](../../CLAUDE.md) (root index) → jump to the doc it points at → follow that doc's `## Related` links. Do not grep blindly first.
- [ ] **One source of truth per fact.** Design values → `tokens/`. Colour/contrast → the canonical colour docs. Decisions → [`decision-log.md`](./decision-log.md). If two places disagree, the source of truth wins and the other is a bug.
- [ ] **Every change updates memory.** New decision → log an ADR. Changed standard → edit the owning doc **and** bump the affected token/version. Never leave a decision only in chat.

---

## 1. What "memory" means here

There is no database and no vector store. The memory system is **the file tree plus a disciplined retrieval + update protocol.** It works because:

| Property | How we get it |
| --- | --- |
| **Discoverable** | A single root index (`CLAUDE.md`) plus per-doc `## Related` links form a navigable graph. |
| **Authoritative** | Each fact has exactly one source of truth; everything else references it by name/path. |
| **Self-consistent** | Docs reference tokens by name (`--color-brand-600`), never raw values, so a token change propagates by reference. |
| **Auditable** | Decisions are append-only ADRs with date + status; standards changes bump a version. |
| **Retrievable by a model** | Predictable folder taxonomy, stable filenames, consistent doc headers, and concise extractable answers. |

---

## 2. Knowledge architecture (directory map)

```text
ai-agency-july/
├── CLAUDE.md                     # ROOT MEMORY / INDEX. Start here. Points at everything below.
├── README.md                     # Human-facing one-liner; defers to CLAUDE.md.
│
├── tokens/                       # ★ SOURCE OF TRUTH for all design values.
│   ├── design-tokens.json        #   Canonical values (W3C DTCG format) + $meta.version.
│   ├── tokens.css                #   CSS custom properties consumed by product code.
│   └── tailwind.tokens.js        #   Tailwind theme mapping of the same tokens.
│
├── docs/                         # All prose knowledge, grouped by domain (see §3).
│   ├── 00-foundations/           #   Why we exist: brief, brand strategy, principles.
│   ├── brand/                    #   Brand identity: colour, type, logo, imagery, icons, voice.
│   ├── design-system/            #   Applied system: tokens doc, components, layout, motion.
│   ├── accessibility/            #   WCAG standards + the contrast matrix (evidence).
│   ├── performance/              #   CWV budgets, image + asset efficiency.
│   ├── responsive/               #   Breakpoints and responsive standards.
│   ├── seo/                      #   On-site, technical, off-site, structured data, AI/GEO.
│   ├── systems/                  #   ★ Meta: how the repo itself works (THIS folder).
│   │   ├── memory-system.md      #     This file — retrieval + update protocol.
│   │   ├── decision-log.md       #     ADR-style running log of foundational decisions.
│   │   └── content-workflow.md   #     Repeatable brief→publish workflow for pages.
│   └── troubleshooting/          #   Symptom → cause → fix runbooks (added as issues recur).
│
├── schema/                       # JSON-LD templates (Organization, LocalBusiness, Service,
│   │                             #   FAQPage, Review, Breadcrumb, WebSite) + README.
│   └── *.jsonld
│
├── checklists/                   # Copy-paste acceptance checklists (a11y, SEO, perf, QA,
│                                 #   launch). Referenced by content-workflow.md.
│
├── public-templates/             # Files that ship to the site root as-is:
│   ├── robots.txt                #   crawl directives + sitemap pointer.
│   ├── sitemap.xml               #   sitemap template.
│   ├── site.webmanifest          #   PWA manifest (name, theme colour, icons).
│   ├── head-meta.html            #   copy-paste <head>: meta, OG, Twitter, hints.
│   └── llms.txt                  #   AI-crawler index / entity summary.
│
├── assets/                       # Source art: logo SVGs, image sources, exports.
└── scripts/                      # Repo tooling.
    └── verify-contrast.py        #   Re-validates colour pairings against tokens.
```

> **Placeholder note:** brand/business specifics use mustache placeholders — `{{BRAND_NAME}}`, `{{DOMAIN}}`, `{{EMAIL}}`, `{{PHONE}}`, `{{ADDRESS}}`, `{{CITY}}`, `{{REGION}}`, `{{POSTAL}}`, `{{COUNTRY}}`, `{{LEGAL_ENTITY}}`, `{{SOCIAL_*}}`. Never invent real values; the owner find-and-replaces at launch.

---

## 3. The `docs/` taxonomy

Domains are folders; each folder holds one or more focused docs; each doc ends with `## Related` links to siblings. The numeric prefix on `00-foundations/` marks it as the root of the "why" — read it before the "how".

| Folder | Owns (source of truth for) | Retrieve when you need… |
| --- | --- | --- |
| `00-foundations/` | Business context, audience, offer, brand strategy, cross-cutting principles | Positioning, voice inputs, the non-negotiable principles a decision must satisfy |
| `brand/` | Colour usage, typography, logo, imagery, iconography | How the brand looks/sounds on a page |
| `design-system/` | Applied tokens, components, layout/grid, motion, interactive elements | Building or styling UI |
| `accessibility/` | WCAG 2.2 AA standards + the contrast matrix (proof) | Any contrast/keyboard/ARIA question |
| `performance/` | Core Web Vitals budgets, image + asset optimization | Deciding if an asset/bundle is within budget |
| `responsive/` | Breakpoints, fluid rules, responsive acceptance | Layout across viewports |
| `seo/` | On-site, technical, off-site, structured data, AI/GEO | Titles, meta, canonicals, JSON-LD, llms.txt |
| `systems/` | How this repo operates (memory, decisions, workflow) | Onboarding, logging a decision, shipping a page |

**Source-of-truth precedence (highest first):**

1. `tokens/design-tokens.json` — for any numeric/colour design value.
2. Canonical colour/contrast docs (`docs/brand/color-system.md`, `docs/accessibility/contrast-matrix.md`) — the only docs allowed to state raw hex + ratios.
3. `docs/systems/decision-log.md` — for *why* a standard is what it is.
4. The domain doc that owns the topic (table above).
5. Everything else references the above by name/path.

---

## 4. RETRIEVE — how to find the right answer

Follow this every time, whether you are a model or a person:

1. **Open [`CLAUDE.md`](../../CLAUDE.md).** It is the index. Match your task to a domain.
2. **Jump to the domain doc** named in the index (table in §3 maps task → folder).
3. **Follow `## Related`** at the bottom of that doc to reach adjacent facts.
4. **If it's a design value, stop at `tokens/`** — the doc will point you there; trust the token, not a number typed into prose.
5. **If it's "why did we choose X", read [`decision-log.md`](./decision-log.md)** — search the ADR title.
6. **Only then search.** If the index + related links didn't surface it, use content search (`Grep`) with a token name or exact phrase. Treat a search miss as a signal that the index needs a link.

**Retrieval do / don't**

| Do | Don't |
| --- | --- |
| Start at `CLAUDE.md`, follow links | Grep the whole repo before checking the index |
| Cite the source-of-truth path in your answer | Restate a value from memory or from a stale doc |
| Prefer token names over hex in any output | Copy raw hex into non-canonical docs or code |
| Read the doc's `## Related` for context | Answer from one doc when the topic spans folders |

---

## 5. UPDATE — how to keep memory true

Memory decays when a decision lives only in a chat. Prevent it:

**When you make a decision** (chose a tool, a threshold, a pattern):
- [ ] Append an ADR to [`decision-log.md`](./decision-log.md) (`ADR-NNNN`, today's date, status `Accepted`, context/decision/consequences).
- [ ] Link the ADR from the doc that the decision affects.

**When a standard changes** (a threshold moves, a rule flips):
- [ ] Edit the **owning** doc (single source of truth — §3 precedence).
- [ ] Update every doc that referenced it *by name* only if the name changed (values propagate by reference, so usually nothing else changes).
- [ ] If the change touches design values, edit `tokens/design-tokens.json` **and bump `$meta.version`** (see §6), then regenerate `tokens.css` / `tailwind.tokens.js` and re-run `scripts/verify-contrast.py`.
- [ ] Log an ADR recording the change and superseding the old one if applicable.

**When you add a doc:**
- [ ] Put it in the correct domain folder (§3).
- [ ] Use the standard header + `## Related` footer (§7).
- [ ] Add a link to it from `CLAUDE.md` and from at least one sibling's `## Related`.

**When a fact is wrong:** fix the source of truth, not the copy. If you find a raw value copied into prose, replace it with the token name.

---

## 6. Versioning tokens & docs

| Artifact | Version signal | Bump when |
| --- | --- | --- |
| Design tokens | `tokens/design-tokens.json` → `$meta.version` (semver) | **PATCH:** comment/typo fix. **MINOR:** add a token or non-breaking value refinement. **MAJOR:** remove/rename a token or change a value that breaks existing pairings. |
| A doc | `**Status:**` line + git history | Any substantive change; keep the status line honest (e.g. `v1 foundation — adjustable` → `v2 — palette revised 2026-…`). |
| Contrast validation | `$meta.lastValidated` + `contrastValidated` | Any colour value change — re-run `scripts/verify-contrast.py` and update the date. |

**Rule:** a MAJOR/MINOR token bump **must** be accompanied by an ADR. A doc edit that changes a threshold **must** update the number in exactly one place.

---

## 7. Conventions (so retrieval stays predictable)

**Filenames:** lowercase, hyphenated, `.md`; descriptive and stable (`color-system.md`, not `colors2.md`). Folders are domain names; only foundations carries a numeric prefix.

**Every markdown doc:**
```md
# <Title>

**Purpose:** <one line — what this doc is for and who retrieves it>
**Status:** v1 foundation — adjustable.

---

<body: prescriptive, numbered, tables + checklists + snippets>

---

## Related
- [`sibling.md`](./sibling.md) — one-line why to open it.
```

**In-doc style:** prescriptive over descriptive; numbers and thresholds over adjectives; do/don't tables; task-list checklists; reference values by **token name** (`--space-4`, `--color-brand-600`) — raw hex only in the canonical colour/contrast docs.

**ADR IDs:** `ADR-0001`, `ADR-0002`, … monotonically increasing, never reused, never renumbered.

---

## 8. Quickstart — "how to use this repo"

**A future Claude session, starting cold:**
1. Read [`CLAUDE.md`](../../CLAUDE.md) fully — it is the map.
2. Read [`docs/00-foundations/project-brief.md`](../00-foundations/project-brief.md) and [`principles.md`](../00-foundations/principles.md) for the "why" and the non-negotiables.
3. Skim [`decision-log.md`](./decision-log.md) so you don't re-litigate settled choices.
4. Keep `tokens/design-tokens.json` open — it settles every value dispute.
5. To build a page, follow [`content-workflow.md`](./content-workflow.md) end to end.

**A teammate (marketer/dev), shipping something:**
1. Find the domain in §3 → open the owning doc → follow `## Related`.
2. Consume values from `tokens/`, never hardcode.
3. Run the relevant checklist in `checklists/` before publish.
4. If you decided anything non-obvious, log an ADR.

---

## Related

- [`decision-log.md`](./decision-log.md) — ADR-style record of every foundational decision.
- [`content-workflow.md`](./content-workflow.md) — the brief→publish workflow that consumes this memory.
- [`../00-foundations/project-brief.md`](../00-foundations/project-brief.md) — business, audience, offer.
- [`../00-foundations/principles.md`](../00-foundations/principles.md) — the checkable rulebook.
- [`../brand/color-system.md`](../brand/color-system.md) — canonical colour source of truth.
- [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — contrast evidence.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — the design value source of truth.
- [`../../CLAUDE.md`](../../CLAUDE.md) — the root index this system revolves around.
