# Troubleshooting Playbooks

**Purpose:** The index and operating manual for the {{BRAND_NAME}} troubleshooting system — a set of symptom-driven playbooks that take a developer, marketer, or future Claude session from an observed problem (slow page, page not indexed, broken form, failed deploy) to a diagnosed cause, a concrete fix, and a prevention step, using a single consistent format across performance, SEO, accessibility, build/deploy, and forms/integrations.
**Status:** v1 foundation — adjustable.

---

> **What this is:** an incident-response layer. Each playbook is a table of `Symptom → Likely cause → Diagnosis → Fix → Prevention`. When something breaks, start here, find the symptom, work the row.
>
> **What this is NOT:** the standards themselves. The *targets* and *how to build it right the first time* live in the systems docs — [`../performance/performance-budget.md`](../performance/performance-budget.md), [`../seo/technical-seo.md`](../seo/technical-seo.md), [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md). Troubleshooting docs assume those standards exist and diagnose deviations from them.
>
> Reference [design tokens](../design-system/design-tokens.md) by name (`--color-brand-600`, `--space-4`) — never raw values — except where a diagnostic threshold is itself the literal (KB, ms, ratios), which is the whole point of these files.

---

## 0. How to use a playbook (the 5-column model)

Every playbook uses the same five columns. Read them left to right:

| Column | Question it answers | How to use it |
|---|---|---|
| **Symptom** | "What am I seeing?" | Match the observable behavior or tool output. This is your entry point — scan the Symptom column first. |
| **Likely cause** | "Why does this usually happen?" | The most common root cause(s), ordered most-likely-first. |
| **Diagnosis** | "How do I confirm it?" | The exact tool, command, DevTools panel, or check that proves the cause before you change anything. **Never fix before you diagnose.** |
| **Fix** | "What do I change?" | The concrete, prescriptive change — code, config, or setting. Copy-paste where provided. |
| **Prevention** | "How do I stop it recurring?" | The guardrail (CI check, lint rule, checklist item, monitoring alert) that catches it next time before a human does. |

**Golden rule:** reproduce → diagnose → fix one thing → re-measure → add prevention. Do not batch fixes; you will not know which one worked.

---

## 1. The playbooks

| Playbook | Use it when… | File |
|---|---|---|
| **Performance** | Pages are slow, Core Web Vitals fail, bundles are heavy, images are large, TTFB is high, the chat widget drags the page down. | [`performance.md`](./performance.md) |
| **SEO & indexing** | A page won't index, rankings dropped, canonical/duplicate warnings, sitemap/robots errors, structured-data errors in Search Console, no rich results, AI engines don't cite us. | [`seo-indexing.md`](./seo-indexing.md) |
| **Accessibility** | Contrast failures, focus is invisible/trapped, controls are unlabeled, screen readers misbehave, motion causes discomfort, form errors aren't announced. | [`accessibility.md`](./accessibility.md) |
| **Build & deploy** | Builds fail, images/fonts 404 or CORS-block, env/config is wrong, a stale deploy is cached, redirect loops, mixed-content warnings, font FOUT/FOIT, CDN problems. | [`build-deploy.md`](./build-deploy.md) |
| **Forms & integrations** | The lead form won't submit, the chat/booking widget won't load, webhook/CRM sync fails, spam floods in, SMS opt-in/delivery breaks, analytics/consent blocks scripts. | [`forms-and-integrations.md`](./forms-and-integrations.md) |

---

## 2. Triage — pick the right playbook fast

Start from what you observed, not what you assume:

| You observed… | Go to |
|---|---|
| A Lighthouse / PageSpeed / CrUX number is red | [Performance](./performance.md) |
| Google Search Console shows an error, exclusion, or drop | [SEO & indexing](./seo-indexing.md) |
| An axe/WAVE/Lighthouse a11y check fails, or keyboard/SR user reports a block | [Accessibility](./accessibility.md) |
| The site build/CI failed, or the deployed site looks broken/stale | [Build & deploy](./build-deploy.md) |
| A user action (submit, book, chat, opt-in) didn't do what it should | [Forms & integrations](./forms-and-integrations.md) |
| It's slow **and** a widget is involved | [Performance §third-party](./performance.md) first, then [Forms & integrations](./forms-and-integrations.md) |
| A page changed and now something's off | Check the last deploy first: [Build & deploy](./build-deploy.md) |

**When a symptom spans two playbooks**, start with the one that owns the *measurement* (e.g., a red CWV number → Performance), then cross-link.

---

## 3. Severity & escalation

Tag every incident so response matches impact. Lead-capture and booking break revenue directly — treat them as P1.

| Severity | Definition | Examples | Response |
|---|---|---|---|
| **P1 — critical** | Leads are being lost right now. | Lead form not submitting, booking widget down, SMS confirmations not sending, site fully down. | Drop everything. Fix or roll back within the hour. Notify {{EMAIL}}. |
| **P2 — high** | Degraded but not lost. | High INP making forms feel broken, one page deindexed, chat widget slow to load. | Same-day fix. |
| **P3 — medium** | Quality/risk issue, no immediate loss. | Contrast failure, missing structured data, non-LCP image too large. | This sprint. |
| **P4 — low** | Polish / future risk. | Minor CLS on a below-fold section, a warning (not error) in Search Console. | Backlog. |

**Roll back first, diagnose second** for P1. A working previous deploy beats a perfect diagnosis. See [`build-deploy.md` §rollback](./build-deploy.md).

---

## 4. Shared diagnostic toolkit

The tools referenced across all playbooks. Install/bookmark these once.

| Tool | Use for | Where |
|---|---|---|
| **Chrome DevTools** (Performance, Network, Lighthouse, Rendering panels) | Local lab diagnosis of perf, CLS, render-blocking, requests. | Built into Chrome. |
| **PageSpeed Insights** | Field (CrUX) + lab (Lighthouse) in one view. | `pagespeed.web.dev` |
| **web-vitals JS library / RUM** | Real INP/LCP/CLS attribution from actual users (lab can't measure INP). | Self-hosted on the site. |
| **Google Search Console (GSC)** | Indexing, coverage, sitemaps, CWV field data, structured-data/rich-result status. | `search.google.com/search-console` |
| **URL Inspection (GSC)** | Live-test a single URL's index status, canonical, render, and structured data. | Inside GSC. |
| **Rich Results Test / Schema Markup Validator** | Validate JSON-LD and eligibility. | `search.google.com/test/rich-results` |
| **axe DevTools / WAVE / Lighthouse a11y** | Automated accessibility scans (catch ~57% of issues; rest need manual + AT). | Browser extensions. |
| **Screen readers** | Manual a11y verification. | NVDA + Firefox/Chrome; VoiceOver + Safari; JAWS. |
| **curl -I / -sS -D -** | Inspect status codes, redirects, headers (cache, CORS, security). | CLI. |
| **CDN / host dashboard & logs** | Deploy status, cache state, edge errors, TTFB. | Your host (Netlify/Vercel/Cloudflare/etc.). |
| **CRM / webhook logs & a request-bin** | Verify integration payloads actually arrive. | CRM dashboard + `webhook.site` for isolation. |

---

## 5. How to add a new playbook or row

Keep the system consistent so it stays scannable under pressure.

### Add a **row** to an existing playbook
- [ ] Confirm it's a genuinely new symptom (search the file first; don't duplicate).
- [ ] Write the **Symptom** as an *observable* ("INP > 200ms in the field"), not a cause.
- [ ] Order **Likely cause** most-common-first.
- [ ] Make **Diagnosis** a *provable* step (a command, panel, or check with an expected result).
- [ ] Make **Fix** prescriptive — numbers, snippets, exact settings. No "optimize it."
- [ ] Make **Prevention** an enforceable guardrail (CI/lint/checklist/alert), not advice.
- [ ] Cross-link to the owning systems doc.

### Add a **new playbook file**
- [ ] Name it `<domain>.md` in `docs/troubleshooting/`.
- [ ] Follow the doc conventions: `# Title`, one-line `**Purpose:**`, `**Status:** v1 foundation — adjustable.`, horizontal rule, and a `## Related` section at the end.
- [ ] Open with a **TL;DR / fast-triage** section, then symptom tables grouped by area.
- [ ] Add it to **§1 The playbooks** and **§2 Triage** tables in this README.
- [ ] Link it from the relevant systems doc so people find it from both directions.

### Playbook row skeleton (copy this)

```markdown
| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| <observable behavior / tool output> | <root cause, most likely first> | <exact tool/command/check + expected result> | <concrete change, snippet, or setting> | <CI check / lint rule / checklist / alert> |
```

---

## 6. Incident log (lightweight)

For anything P1–P2, capture a one-line record so patterns surface over time. A simple append-only list in the repo or issue tracker is enough.

| Field | Example |
|---|---|
| Date | 2026-07-01 |
| Severity | P1 |
| Symptom | Lead form returned 500 on submit |
| Root cause | Webhook endpoint URL changed in CRM, not updated in env |
| Fix | Updated `CRM_WEBHOOK_URL`, redeployed |
| Prevention added | Synthetic form-submit check every 15 min → alert |

If the same root cause appears twice, the prevention step failed — strengthen it (move it into CI or monitoring).

---

## Related

- [`performance.md`](./performance.md) — slow LCP, high INP, CLS, bundles, TTFB, images, render-blocking, widgets.
- [`seo-indexing.md`](./seo-indexing.md) — indexing, rankings, canonicals, sitemaps/robots, structured data, AI citation.
- [`accessibility.md`](./accessibility.md) — contrast, focus, keyboard, labels, screen readers, motion, form errors.
- [`build-deploy.md`](./build-deploy.md) — build failures, asset 404/CORS, env, cache/stale, redirects, mixed content, fonts, CDN.
- [`forms-and-integrations.md`](./forms-and-integrations.md) — form submit, widgets, webhooks/CRM, spam, SMS opt-in/delivery, consent/analytics.
- [`../performance/performance-budget.md`](../performance/performance-budget.md) — the performance standard these playbooks defend.
- [`../seo/technical-seo.md`](../seo/technical-seo.md) — the crawl/index standard.
- [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md) — the WCAG 2.2 AA standard.
- [`../design-system/design-tokens.md`](../design-system/design-tokens.md) — token names referenced in fixes.
