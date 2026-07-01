# Legal & Policy Pages — Structure System

**Purpose:** The prescriptive structure system for every legal/policy page a lead-handling AI service agency needs — Privacy Policy, Terms of Service, Cookie Policy + consent banner, Acceptable Use, SMS/messaging consent & opt-out, AI usage/disclosure, DPA note, Accessibility Statement, and Impressum — as templates, section checklists, and placeholder skeletons the owner can fill, plus footer-linking, indexing, and last-updated patterns.
**Status:** v1 foundation — adjustable.

---

> ⚠️ **NOT LEGAL ADVICE — READ THIS FIRST.** This document is a **structural/editorial template and checklist only**. It is written by a design/marketing system, not a lawyer, and it does **not** constitute legal advice, create an attorney–client relationship, or guarantee compliance with any law (GDPR, UK GDPR, CCPA/CPRA, TCPA, CAN-SPAM, ePrivacy, PIPEDA, CASL, state privacy laws, carrier/A2P 10DLC rules, or anything else). **Have a qualified attorney in your operating jurisdiction(s) draft and review every published legal page before it goes live**, and re-review whenever your data practices, tools, sub-processors, or laws change. The mustache placeholders (`{{…}}`) are deliberate blanks — do not ship a page with placeholders unresolved.

> **Values source of truth:** [`tokens/design-tokens.json`](../../tokens/design-tokens.json). Reference tokens by name (`--color-brand-600`, `--space-4`), not raw hex, in any styled component.
> **Business facts source of truth (NAP, entity, offer):** [`../00-foundations/project-brief.md`](../00-foundations/project-brief.md). Legal-page NAP **must** match site + Google Business Profile + schema exactly.

---

## 0. How to use this document

1. Pick the pages you actually need from §2 (the coverage matrix). A US-only agency and an EU-facing one need different sets.
2. For each page, work top-to-bottom through its **section checklist**, filling the **skeleton**.
3. Replace **every** `{{PLACEHOLDER}}` (see §1). Search the file for `{{` before publishing.
4. Apply the **footer-linking**, **indexing**, and **last-updated** patterns (§13–§15) to every page.
5. Send the drafts to a lawyer (§16 hand-off checklist). Publish only the reviewed version.

**Voice for legal pages:** clear, plain-language, second person where natural ("your data", "you agree"). Match brand voice (calm, direct, jargon-light) *without* softening legal meaning. Prefer short sentences and defined terms over dense clauses. Accessibility and plain-language both improve comprehension and reduce disputes.

---

## 1. Placeholders (find-and-replace before publishing)

Use these mustache placeholders verbatim so the owner can find-and-replace later. Never invent real values.

| Placeholder | Meaning | Example fill |
|---|---|---|
| `{{BRAND_NAME}}` | Public brand / trading name | Acme Lead Response |
| `{{LEGAL_ENTITY}}` | Registered legal entity (the data controller) | Acme Lead Response, LLC |
| `{{DOMAIN}}` | Primary domain | example.com |
| `{{EMAIL}}` | General contact email | hello@example.com |
| `{{PRIVACY_EMAIL}}` | Privacy / DSAR inbox (may equal `{{EMAIL}}`) | privacy@example.com |
| `{{DPO_CONTACT}}` | DPO or privacy lead (if appointed) | dpo@example.com |
| `{{PHONE}}` | Business phone (E.164 for SMS) | +1-555-0100 |
| `{{ADDRESS}}`, `{{CITY}}`, `{{REGION}}`, `{{POSTAL}}`, `{{COUNTRY}}` | Registered postal address (NAP) | 1 Main St / Austin / TX / 78701 / USA |
| `{{EFFECTIVE_DATE}}` | Date the version takes effect | 2026-07-01 |
| `{{LAST_UPDATED}}` | Date last materially changed | 2026-07-01 |
| `{{VERSION}}` | Policy version string | v1.0 |
| `{{GOVERNING_LAW}}` | Governing law / venue | State of Texas, USA |
| `{{SMS_PROVIDER}}` | A2P/SMS platform (e.g., messaging vendor) | (your SMS platform) |
| `{{HELP_KEYWORD}}` | SMS help keyword | HELP |
| `{{STOP_KEYWORD}}` | SMS opt-out keyword | STOP |
| `{{MSG_FREQUENCY}}` | Expected message frequency | up to 6 msgs/month |
| `{{SUBPROCESSOR_LIST_URL}}` | URL to live sub-processor list | example.com/subprocessors |
| `{{SOCIAL_*}}` | Social profile URLs | `{{SOCIAL_LINKEDIN}}` |

> If a placeholder has no value yet (e.g., no DPO appointed), **remove the clause**, don't ship an empty label. An empty "DPO: ____" is worse than omitting it.

---

## 2. Coverage matrix — which pages do you need?

| Page | Slug (recommended) | Always needed? | Triggered by |
|---|---|---|---|
| Privacy Policy | `/privacy` | **Yes** — any site collecting form/lead/analytics data | Universal. Required in practice by GDPR/CCPA/app stores/ad platforms |
| Terms of Service | `/terms` | **Yes** for a paid service/agency | Selling services, accounts, SLAs, payment |
| Cookie Policy + consent banner | `/cookies` (+ banner) | **Yes if** you use non-essential cookies/analytics/ads, or serve EU/UK/CA | ePrivacy/GDPR/UK PECR consent; CPRA opt-out |
| Acceptable Use Policy (AUP) | `/acceptable-use` | Recommended | You provide a platform/assistant clients + end-users interact with |
| SMS / Messaging Consent & Opt-Out | `/sms-terms` (+ `/messaging-consent`) | **Yes — critical** for an AI-that-texts business | TCPA/CTIA/A2P 10DLC; carrier campaign registration |
| AI Usage / Disclosure Statement | `/ai-disclosure` | **Yes — differentiator + trust** | You deploy AI assistants that talk to real people |
| DPA note / DPA | `/dpa` (or downloadable) | **Yes if** you process personal data *on behalf of* clients | GDPR Art. 28 processor terms; CCPA service-provider terms |
| Accessibility Statement | `/accessibility` | Recommended (often required for public bodies / ADA risk) | WCAG 2.2 AA commitment; EAA (EU) June 2025 |
| Impressum / Legal Notice | `/impressum` (or in footer) | **Yes if** you target Germany/Austria/EU | §5 DDG (formerly TMG); EU trader identity duties |

> **Controller vs processor — decide this first, it changes everything.** For your *own* website (leads you collect for your marketing), you are the **data controller**. For personal data you handle *inside a client's assistant on the client's behalf*, you are typically a **data processor / service provider** — that relationship is governed by the **DPA (§10)**, not your public Privacy Policy. Keep the two clearly separated.

---

## 3. Privacy Policy — `/privacy`

**Purpose:** Tell people (leads, site visitors, clients, applicants) what personal data you collect *as controller*, why, the legal basis, who you share it with, how long you keep it, and how they exercise their rights. This is the anchor legal page; most others link back to it.

### 3.1 Section checklist

- [ ] **Identity & contact of the controller** — `{{LEGAL_ENTITY}}`, `{{ADDRESS}}`, `{{PRIVACY_EMAIL}}`; DPO/privacy lead `{{DPO_CONTACT}}` if appointed; EU/UK representative if applicable (GDPR Art. 27)
- [ ] **Effective date + last-updated + version** (see §15 pattern)
- [ ] **Scope** — what this policy covers (the website + AI assistant interactions *you* control) and what it does **not** (data processed on behalf of clients → point to DPA §10)
- [ ] **What data we collect** — grouped: (a) info you give us (name, email, phone, company, message, booking details), (b) automatically collected (IP, device, cookies, usage, call/SMS metadata), (c) from third parties (ad platforms, CRMs, enrichment)
- [ ] **Special note on lead & conversation data** — chat/SMS transcripts, call recordings/transcripts, booking data captured by the AI assistant
- [ ] **Why we use it (purposes)** — respond to/qualify/book leads, provide the service, support, billing, security, analytics, marketing (with consent)
- [ ] **Legal bases** (GDPR/UK GDPR) — per purpose: consent, contract, legitimate interests (with balancing note), legal obligation. **Do not** use one blanket basis
- [ ] **AI/automated processing disclosure** — that an AI assistant may process the conversation; whether any decision is "solely automated" with legal/significant effect (GDPR Art. 22); link to AI Disclosure §9
- [ ] **Sharing & sub-processors** — categories of recipients (hosting, SMS/telephony, CRM, analytics, payment, AI model providers); link to live sub-processor list `{{SUBPROCESSOR_LIST_URL}}`
- [ ] **International transfers** — mechanism (SCCs / UK IDTA / adequacy) if data leaves EEA/UK
- [ ] **Retention** — how long, or the criteria used, per data category (transcripts, recordings, billing, marketing)
- [ ] **Your rights** — access, rectification, erasure, restriction, portability, objection, withdraw consent, complain to a supervisory authority (GDPR/UK GDPR); CCPA/CPRA: know, delete, correct, opt-out of sale/share, limit sensitive PI, non-discrimination
- [ ] **"Do we sell/share personal information?"** — explicit CCPA/CPRA statement (yes/no); if yes, provide **"Do Not Sell or Share My Personal Information"** link + Global Privacy Control (GPC) honoring note
- [ ] **How to exercise rights** — method + identity-verification note + response timelines (GDPR ~1 month; CCPA ~45 days)
- [ ] **Cookies & tracking** — short summary + link to Cookie Policy §5
- [ ] **Children** — service not directed to children under `{{age}}`; no knowing collection
- [ ] **Security** — general measures statement (no over-promising)
- [ ] **Changes to this policy** — how you notify; last-updated pattern
- [ ] **Contact** — `{{PRIVACY_EMAIL}}` + postal address

### 3.2 GDPR / UK GDPR / CCPA quick considerations

| Regime | Must appear | Watch-out |
|---|---|---|
| **GDPR / UK GDPR** | Controller identity, legal basis **per purpose**, rights list, transfer mechanism, retention, right to lodge complaint with a supervisory authority (ICO for UK) | Blanket "we use legitimate interests" without a purpose mapping; missing Art. 27 representative for non-EU controllers targeting the EU |
| **CCPA / CPRA (California)** | Categories collected/sold/shared/disclosed, purposes, rights, "Do Not Sell or Share" + "Limit Use of Sensitive PI" links, honor GPC signal, 12-month look-back | Treating CCPA "sale/share" narrowly — ad-tech cookies often count as "sharing" |
| **Other US state laws** (e.g., VA/CO/CT/TX/UT and newer) | Similar rights + opt-outs; universal opt-out signal honoring | Assuming CCPA text covers all states verbatim |

### 3.3 Skeleton

```markdown
# Privacy Policy

**Effective:** {{EFFECTIVE_DATE}} · **Last updated:** {{LAST_UPDATED}} · **Version:** {{VERSION}}

{{LEGAL_ENTITY}} ("{{BRAND_NAME}}", "we", "us") operates {{DOMAIN}} and provides AI
appointment-setting and lead-response services. This policy explains how we handle
personal data **as a controller**. When we process personal data on behalf of a
client, our [Data Processing Addendum](/dpa) governs instead.

## 1. Who we are
{{LEGAL_ENTITY}}, {{ADDRESS}}, {{CITY}}, {{REGION}} {{POSTAL}}, {{COUNTRY}}.
Privacy contact: {{PRIVACY_EMAIL}}. [Data protection lead: {{DPO_CONTACT}}.]

## 2. What we collect
- Information you provide: …
- Collected automatically: …
- From third parties: …
- Lead & conversation data (chat/SMS/call transcripts, bookings): …

## 3. Why we use it & our legal basis
| Purpose | Data | Legal basis |
|---|---|---|
| Respond to & book leads | … | Contract / legitimate interests |
| Marketing | … | Consent |
| … | … | … |

## 4. AI & automated processing
An AI assistant may process your messages to answer, qualify, and book.
[We do / do not make solely-automated decisions with legal or similarly
significant effects.] See our [AI Disclosure](/ai-disclosure).

## 5. Sharing & sub-processors
Categories of recipients: … Current sub-processors: {{SUBPROCESSOR_LIST_URL}}.

## 6. International transfers
…mechanism (SCCs / UK IDTA / adequacy)…

## 7. Retention
| Data | Retention |
|---|---|
| Transcripts/recordings | … |
| Billing | … |

## 8. Your rights
… (GDPR/UK list) … California residents: … [Do Not Sell or Share My Personal
Information](/privacy#dnss). We honor Global Privacy Control signals.

## 9. Cookies
See our [Cookie Policy](/cookies).

## 10. Children · 11. Security · 12. Changes · 13. Contact
…
```

---

## 4. Terms of Service — `/terms`

**Purpose:** The contract governing use of your website and, at a high level, your service; caps liability, sets IP ownership, payment, and dispute terms. For B2B clients, detailed commercial terms usually live in a separate signed MSA/Order Form — the public ToS covers website use + baseline service terms.

### 4.1 Section checklist

- [ ] **Acceptance & who these terms bind** ("by using {{DOMAIN}} / the Services you agree")
- [ ] **Definitions** (Services, Client, End User, Content, Assistant)
- [ ] **The service** — high-level description (done-for-you AI setup, ongoing management, human support); relationship to signed MSA/Order Form (which controls on conflict)
- [ ] **Eligibility / accounts** — accurate info, security of credentials
- [ ] **Client obligations** — lawful lead sourcing, required consents from *their* end users (esp. SMS — see §7), compliant content
- [ ] **Acceptable use** — link to AUP §6
- [ ] **Fees, billing, taxes, renewals, cancellation, refunds**
- [ ] **Intellectual property** — your ownership of platform/IP; client's ownership of client data; feedback license
- [ ] **Third-party services** — reliance on carriers, AI providers, integrations; not liable for their outages
- [ ] **AI-specific disclaimers** — assistant outputs may be imperfect; not professional (medical/legal/financial) advice; human-in-the-loop escalation; link to AI Disclosure §9
- [ ] **Warranties & disclaimers** ("as is" to the extent permitted)
- [ ] **Limitation of liability** (cap; excluded damages)
- [ ] **Indemnification**
- [ ] **Term & termination** + effect of termination (data return/deletion → DPA)
- [ ] **Governing law & venue** — `{{GOVERNING_LAW}}`; dispute resolution / arbitration / class-waiver (jurisdiction-dependent — lawyer must confirm enforceability)
- [ ] **Changes to terms** + notice
- [ ] **Miscellaneous** (assignment, severability, entire agreement, force majeure)
- [ ] **Contact** `{{EMAIL}}`

### 4.2 Considerations

- **Consumer-protection limits:** liability caps, arbitration, and class-waivers are **not** freely enforceable everywhere (esp. EU/UK consumer contexts). Lawyer must tailor.
- **B2B vs B2C:** your buyers are SMB owners (businesses) — but keep unfair-terms rules in mind for any consumer-facing surface.
- **Cross-reference, don't duplicate:** ToS references Privacy, AUP, SMS Terms, AI Disclosure, DPA rather than restating them.

### 4.3 Skeleton

```markdown
# Terms of Service

**Effective:** {{EFFECTIVE_DATE}} · **Version:** {{VERSION}}

These Terms govern your use of {{DOMAIN}} and the Services provided by
{{LEGAL_ENTITY}} ("{{BRAND_NAME}}"). If a signed Master Services Agreement or
Order Form exists, it controls where it conflicts with these Terms.

1. Acceptance   2. Definitions   3. The Services   4. Accounts & eligibility
5. Client obligations (lawful leads, required end-user consents)
6. Acceptable use → see [AUP](/acceptable-use)
7. Fees & billing   8. Intellectual property   9. Third-party services
10. AI outputs & disclaimers → see [AI Disclosure](/ai-disclosure)
11. Warranties & disclaimers   12. Limitation of liability   13. Indemnification
14. Term & termination   15. Governing law & disputes ({{GOVERNING_LAW}})
16. Changes   17. Miscellaneous   18. Contact: {{EMAIL}}
```

---

## 5. Cookie Policy + Consent Banner — `/cookies` (+ banner)

**Purpose:** Disclose the cookies/trackers you set, their purpose and lifespan, and give a **prior-consent** mechanism (EU/UK ePrivacy) and an **opt-out** mechanism (CPRA). The banner is the UI; the policy is the reference page.

### 5.1 Cookie Policy — section checklist

- [ ] **What cookies/trackers are** (plain language)
- [ ] **Categories** — Strictly Necessary, Functional/Preferences, Analytics/Performance, Marketing/Advertising
- [ ] **Cookie table** — name, provider (first/third party), purpose, category, duration
- [ ] **Legal basis** — necessary = no consent; all others = consent (EU/UK) / opt-out (CA)
- [ ] **How to manage/withdraw** — link to reopen the preference center; browser controls; GPC note
- [ ] **Changes + last-updated**
- [ ] Keep the table **in sync** with what actually loads (audit periodically)

### 5.2 Consent banner — requirements checklist

- [ ] **No non-essential cookies fire before consent** (EU/UK: prior, explicit, opt-in — pre-checked boxes are invalid)
- [ ] **"Reject All" is as easy as "Accept All"** (equal prominence, same number of clicks — regulators penalize dark patterns)
- [ ] **Granular category toggles** available (at least via "Manage preferences")
- [ ] **Persistent way to change choice later** (footer "Cookie settings" link reopens the center)
- [ ] **Records consent** (proof: timestamp, version, choices)
- [ ] **Re-prompt** when purposes/vendors change or after a defined period
- [ ] **Honor Global Privacy Control** signal for CPRA opt-out
- [ ] **Accessible:** keyboard-operable, focus-trapped, `44px` targets, meets contrast — see [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md); banner must not cause CLS (reserve space)

### 5.3 GDPR/ePrivacy vs CCPA model

| Model | Region | Mechanism | Default |
|---|---|---|---|
| **Opt-in (consent)** | EU/UK/EEA (ePrivacy + GDPR) | Block until user accepts; granular; withdrawable | Non-essential **off** by default |
| **Opt-out** | California (CPRA) + several US states | "Do Not Sell or Share" + honor GPC | May run until user opts out |

> A **geo-aware** banner (opt-in for EU/UK, opt-out notice for US) is the common approach — the lawyer confirms the trigger logic.

### 5.4 Cookie-row skeleton

```markdown
| Cookie | Provider | Purpose | Category | Duration |
|---|---|---|---|---|
| `__session` | {{BRAND_NAME}} (1st) | Keep you signed in | Strictly necessary | Session |
| `_ga` | Google (3rd) | Analytics | Analytics | 24 months |
| … | … | … | Marketing | … |
```

---

## 6. Acceptable Use Policy (AUP) — `/acceptable-use`

**Purpose:** Prohibit misuse of your assistant/platform by clients and their end users; protect you, carriers, and recipients; give you a basis to suspend abuse. Especially important because your assistant sends messages on clients' behalf.

### 6.1 Section checklist

- [ ] **Scope** — applies to clients and anyone using the Services/Assistant
- [ ] **Prohibited content** — illegal, harassing, hateful, sexual-exploitation, deceptive/fraudulent, IP-infringing
- [ ] **Prohibited messaging conduct** — spam; messaging without required consent; the **carrier-prohibited "SHAFT" categories** (Sex, Hate, Alcohol, Firearms, Tobacco/cannabis) and other A2P-restricted content; no purchased/scraped lists
- [ ] **Prohibited technical conduct** — no scraping, reverse-engineering, security circumvention, overloading, malware
- [ ] **AI-specific misuse** — no using the assistant to impersonate a human where prohibited, generate disallowed content, or evade opt-outs
- [ ] **Data/consent duties** — client must have lawful basis + consents for all contacts uploaded
- [ ] **Enforcement** — suspension/termination, cooperation with carriers/authorities
- [ ] **Reporting abuse** — `{{EMAIL}}`

### 6.2 Considerations

- Align AUP prohibitions with **carrier/CTIA A2P rules** (SHAFT + prohibited-message list) and **TCPA** so a client's misuse doesn't expose you.
- Cross-link from ToS (§4) and SMS Terms (§7).

---

## 7. SMS / Messaging Consent & Opt-Out — `/sms-terms` (+ `/messaging-consent`) — **CRITICAL**

**Purpose:** For an AI-that-texts business this is the highest-risk area. You need (a) **program disclosure terms** and (b) a **consent capture + opt-out** system that satisfies **TCPA**, **CTIA messaging guidelines**, and **A2P 10DLC** carrier registration. Non-compliance risks statutory damages **and** number/campaign blocking by carriers.

> **Two hats again:** Usually the **client** is the sender who must obtain end-user consent; you provide the compliant plumbing and terms. Make the client's consent obligations explicit (in ToS §4 + AUP §6). Where you send on your own behalf (your marketing texts), you are the sender and must comply directly.

### 7.1 Consent capture — required elements (opt-in UI)

- [ ] **Clear opt-in** at point of collection (checkbox/keyword), describing the program
- [ ] **Program/brand name** identified in the consent text
- [ ] **Purpose** of messages (e.g., appointment reminders, lead follow-up)
- [ ] **Message frequency** disclosure — `{{MSG_FREQUENCY}}`
- [ ] **"Msg & data rates may apply"**
- [ ] **Opt-out instructions** — "Reply `{{STOP_KEYWORD}}` to cancel"
- [ ] **Help instructions** — "Reply `{{HELP_KEYWORD}}` for help"
- [ ] **Links to** SMS Terms + Privacy Policy adjacent to the opt-in
- [ ] **Consent is not a condition of purchase** (where marketing consent)
- [ ] **No pre-checked boxes**; consent logged (who/when/what text/IP)
- [ ] **Separate consent** for marketing vs transactional where required
- [ ] **Consent not shared/sold** for third-party marketing (carrier requirement; must be stated in privacy/terms and honored)

### 7.2 SMS Terms page — section checklist

- [ ] **Program description** + sender identity `{{BRAND_NAME}}` / `{{LEGAL_ENTITY}}`
- [ ] **Message types** (transactional vs promotional)
- [ ] **Frequency** `{{MSG_FREQUENCY}}`
- [ ] **Cost** — "Msg & data rates may apply"
- [ ] **Opt-out** — reply `{{STOP_KEYWORD}}` (also CANCEL/END/QUIT/UNSUBSCRIBE); effect (you stop) + confirmation message
- [ ] **Help** — reply `{{HELP_KEYWORD}}`; support `{{PHONE}}` / `{{EMAIL}}`
- [ ] **Supported carriers** disclaimer ("carriers not liable for delayed/undelivered messages")
- [ ] **Privacy** — link to Privacy Policy; statement that opt-in data isn't sold/shared for others' marketing
- [ ] **Changes** + last-updated
- [ ] **AI note** — messages may be sent/handled by an automated assistant (link AI Disclosure §9)

### 7.3 Opt-out handling — system requirements

- [ ] `{{STOP_KEYWORD}}` (and synonyms) processed **automatically and immediately**; send one confirmation, then stop
- [ ] `{{HELP_KEYWORD}}` returns program + contact info automatically
- [ ] Opt-outs are **honored across the program** and logged
- [ ] AI assistant must **not** attempt to re-engage or override an opt-out
- [ ] Re-consent required before messaging an opted-out contact again

### 7.4 A2P 10DLC / TCPA / CTIA awareness

| Item | What to know (awareness — confirm with counsel/provider) |
|---|---|
| **A2P 10DLC** | US application-to-person messaging over 10-digit long codes requires **Brand + Campaign registration** with carriers via your `{{SMS_PROVIDER}}`. Unregistered traffic is filtered/blocked. Sample messages, opt-in flow, and use-case are reviewed. |
| **TCPA** | Federal law governing automated/marketing calls & texts; requires prior express (and, for marketing, prior express *written*) consent; statutory damages per violation. Maintain consent records + honor opt-outs. |
| **CTIA guidelines** | Industry messaging principles: consent, SHAFT prohibitions, opt-out keywords, no consent-sharing. |
| **SHAFT** | Sex, Hate, Alcohol, Firearms, Tobacco content is carrier-restricted/prohibited (see AUP §6). |
| **Consent-sharing rule** | Carrier rules require that opt-in consent **not** be sold/shared with third parties for marketing — state and honor this. |

> Register campaigns through `{{SMS_PROVIDER}}` **before** launch. Keep your published SMS Terms consistent with the sample opt-in/messages you register.

### 7.5 Consent-language skeleton (opt-in microcopy)

```text
By checking this box, you agree to receive appointment and follow-up text
messages from {{BRAND_NAME}} at the number provided, sent by an automated
system. Consent is not a condition of purchase. {{MSG_FREQUENCY}}.
Msg & data rates may apply. Reply {{STOP_KEYWORD}} to cancel, {{HELP_KEYWORD}}
for help. See [SMS Terms](/sms-terms) and [Privacy Policy](/privacy).
```

---

## 8. AI Usage / Disclosure Statement — `/ai-disclosure`

**Purpose:** Tell end users, plainly, that they may be interacting with an AI assistant; what it does; its limits; when a human steps in; and how their conversation data is used. This is both a **trust differentiator** and increasingly a **transparency obligation** (EU AI Act transparency duties; some US state chatbot-disclosure laws).

### 8.1 Section checklist

- [ ] **Plain disclosure** — "You may be chatting/texting with an AI assistant"
- [ ] **What it does** — answers questions, qualifies, books appointments 24/7
- [ ] **Human-in-the-loop** — when/how a human takes over; how to reach a human
- [ ] **Limitations** — may be inaccurate; not professional (medical/legal/financial) advice; verify important details
- [ ] **Data use** — conversations may be processed/stored/used to operate & improve the service; whether used to train models (state clearly; link Privacy §3)
- [ ] **No fully-automated significant decisions** (or disclose + provide human-review path per GDPR Art. 22)
- [ ] **Accuracy & feedback** — how to report a bad response
- [ ] **Recording note** — if calls/chats are recorded, say so (and get consent where required — two-party consent states)
- [ ] **Last-updated**

### 8.2 Considerations

| Regime | Consideration |
|---|---|
| **EU AI Act** | Transparency duty: users must be informed they're interacting with an AI system unless obvious. AI-generated content disclosure. |
| **US state bot laws** | Some states require disclosure that a bot is being used in certain commercial/persuasion contexts. |
| **Call recording** | Two-party/all-party consent states require consent to record calls; disclose at start of call. |
| **GDPR Art. 22** | Solely-automated decisions with legal/significant effect need a lawful basis + human-review right. |

### 8.3 Skeleton

```markdown
# How we use AI

**Last updated:** {{LAST_UPDATED}}

When you message or call {{BRAND_NAME}}, an AI assistant may respond to answer
questions, qualify your enquiry, and book appointments — 24/7. A human is
available and will step in for anything the assistant can't handle; ask to
speak to a person at any time.

**Limitations.** The assistant can be wrong and does not provide medical, legal,
or financial advice. Please confirm important details with our team.

**Your conversation data.** We process and store conversations to run and improve
the Service. [We do / do not use your conversations to train AI models.] See our
[Privacy Policy](/privacy). Calls may be recorded where permitted; you'll be told
at the start.
```

---

## 9. DPA note / Data Processing Addendum — `/dpa`

**Purpose:** When you process personal data **on behalf of a client** (their leads/contacts inside their assistant), GDPR Art. 28 (and CCPA service-provider terms) require a written processor agreement. The public page can be a **note + downloadable DPA** clients execute.

### 9.1 Section checklist (Art. 28 processor terms)

- [ ] **Roles** — client = controller, `{{LEGAL_ENTITY}}` = processor
- [ ] **Subject matter, duration, nature & purpose** of processing
- [ ] **Types of personal data + categories of data subjects**
- [ ] **Process only on documented instructions** from the controller
- [ ] **Confidentiality** of personnel
- [ ] **Security measures** (Art. 32) — technical & organizational measures
- [ ] **Sub-processors** — authorization, flow-down terms, notice of changes; link `{{SUBPROCESSOR_LIST_URL}}`
- [ ] **Assist controller** with data-subject requests & DPIAs
- [ ] **Breach notification** — notify controller without undue delay
- [ ] **Deletion/return** of data at end of service
- [ ] **Audit & information rights**
- [ ] **International transfers** — SCCs / UK IDTA
- [ ] **CCPA "service provider" language** — no selling; use limited to the business purpose
- [ ] **Signature/execution mechanism**

### 9.2 Public-page skeleton

```markdown
# Data Processing Addendum (DPA)

Where {{LEGAL_ENTITY}} processes personal data on behalf of a client, this DPA
forms part of our agreement and reflects GDPR Article 28 and applicable US
service-provider requirements.

- Roles: Client = controller · {{BRAND_NAME}} = processor
- Sub-processors: {{SUBPROCESSOR_LIST_URL}}
- Request/execute a signed DPA: {{PRIVACY_EMAIL}}

[Download DPA (PDF)]  ·  See [Privacy Policy](/privacy).
```

---

## 10. Accessibility Statement — `/accessibility`

**Purpose:** State your accessibility commitment, target conformance, known limitations, and a contact for accessibility issues. Reduces ADA/EAA risk and signals quality.

### 10.1 Section checklist

- [ ] **Commitment** to accessibility
- [ ] **Conformance target** — WCAG 2.2 **Level AA** (per our standards)
- [ ] **Measures taken** (design system, testing, training)
- [ ] **Known limitations** (honest list + remediation timeline)
- [ ] **Feedback mechanism** — accessible contact `{{EMAIL}}` / `{{PHONE}}`, expected response time
- [ ] **Compatibility** — browsers/AT tested
- [ ] **Assessment approach** (self-eval / third-party audit)
- [ ] **Date** + last-updated

> Source of truth for our actual conformance targets: [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md). Don't contradict it.

### 10.2 Skeleton

```markdown
# Accessibility Statement

**Last updated:** {{LAST_UPDATED}}

{{BRAND_NAME}} is committed to making {{DOMAIN}} accessible. We aim to conform to
**WCAG 2.2 Level AA**.

**Measures:** design system with validated contrast, keyboard support, semantic
HTML, and periodic testing.
**Known limitations:** … (with target fix dates).
**Feedback:** email {{EMAIL}} or call {{PHONE}}; we aim to respond within {{n}}
business days.
```

---

## 11. Impressum / Legal Notice — `/impressum`

**Purpose:** Germany/Austria (and broadly EU) require a legal-identity disclosure ("Impressum") for commercial sites — under German **§5 DDG** (which replaced the TMG). Skip only if you have zero DE/AT/EU exposure; when in doubt, include it.

### 11.1 Section checklist

- [ ] **Provider name** — `{{LEGAL_ENTITY}}`
- [ ] **Full postal address** — `{{ADDRESS}}`, `{{CITY}}`, `{{REGION}}` `{{POSTAL}}`, `{{COUNTRY}}` (no P.O. box)
- [ ] **Contact** — `{{EMAIL}}`, `{{PHONE}}`
- [ ] **Represented by** (managing director / authorized rep), where a company
- [ ] **Register + number** (commercial register / equivalent), if applicable
- [ ] **VAT/tax ID**, if applicable
- [ ] **Responsible for content** (name/address) where required
- [ ] **Regulator/professional body**, if a regulated profession
- [ ] **EU ODR platform** link, if selling to EU consumers online

### 11.2 Skeleton

```markdown
# Impressum / Legal Notice

**{{LEGAL_ENTITY}}**
{{ADDRESS}}, {{CITY}}, {{REGION}} {{POSTAL}}, {{COUNTRY}}
Email: {{EMAIL}} · Phone: {{PHONE}}

Represented by: {{name}}
[Register: {{register + number}}] · [VAT ID: {{vat}}]
Responsible for content: {{name, address}}
```

---

## 12. Cross-page consistency rules

- [ ] **NAP identical** on every legal page and matching site + Google Business Profile + schema (`../seo/technical-seo.md`).
- [ ] **Entity name** consistent: use `{{LEGAL_ENTITY}}` for legal identity, `{{BRAND_NAME}}` for the brand voice.
- [ ] **Dates in ISO 8601** (`YYYY-MM-DD`) and consistent across pages.
- [ ] **Cross-links** resolve: Privacy ↔ Cookies ↔ SMS ↔ AI Disclosure ↔ DPA ↔ ToS ↔ AUP.
- [ ] **No contradictions** (e.g., retention period in Privacy vs DPA; "we don't sell data" vs a tracking pixel that shares data).
- [ ] **One version/effective-date system** (§15) applied everywhere.

---

## 13. Footer linking & information architecture

**Footer link group ("Legal"):** Privacy Policy · Terms of Service · Cookie Policy · Cookie Settings (reopens preference center) · SMS Terms · AI Disclosure · Acceptable Use · Accessibility · DPA · Impressum (if applicable) · "Do Not Sell or Share My Personal Information" (CA).

Linking rules:

- [ ] Real, crawlable `<a href>` links in the footer of **every** page (not JS-only).
- [ ] **"Cookie Settings"** and **"Do Not Sell or Share"** are actionable controls, not just informational pages.
- [ ] Descriptive anchor text (not "click here") — good for SEO + accessibility (see [`../seo/onsite-seo.md`](../seo/onsite-seo.md)).
- [ ] Keep the footer link count reasonable; group under a "Legal" heading.
- [ ] Link the relevant policy **contextually** at the point of collection (lead form → Privacy + SMS Terms next to the submit/opt-in).
- [ ] Legal pages themselves cross-link via each page's own **Related/See-also** block.

Footer skeleton:

```html
<nav aria-label="Legal">
  <h2>Legal</h2>
  <ul>
    <li><a href="/privacy">Privacy Policy</a></li>
    <li><a href="/terms">Terms of Service</a></li>
    <li><a href="/cookies">Cookie Policy</a></li>
    <li><button type="button" data-open-cookie-settings>Cookie Settings</button></li>
    <li><a href="/sms-terms">SMS Terms</a></li>
    <li><a href="/ai-disclosure">AI Disclosure</a></li>
    <li><a href="/acceptable-use">Acceptable Use</a></li>
    <li><a href="/accessibility">Accessibility</a></li>
    <li><a href="/dpa">Data Processing (DPA)</a></li>
    <!-- If EU/DE exposure: --><li><a href="/impressum">Impressum</a></li>
    <!-- If CA sale/share: --><li><a href="/privacy#dnss">Do Not Sell or Share My Personal Information</a></li>
  </ul>
</nav>
```

---

## 14. Indexing guidance (`noindex`?) & SEO handling

| Page | Index? | Rationale |
|---|---|---|
| Privacy Policy | **Index** | Trust/E-E-A-T signal; users & AI answer engines look for it; keep crawlable |
| Terms of Service | **Index** | Same; commonly indexed |
| Cookie Policy | Index | Fine to index |
| SMS Terms | **Index** | Carriers/registration reviewers and users need to find it via URL |
| AI Disclosure | **Index** | Transparency + differentiator; good for GEO/AI-answer trust |
| Acceptable Use | Index | Fine to index |
| Accessibility | **Index** | Signals quality; sometimes required to be reachable |
| DPA (public note) | Index (note) / `noindex` (raw PDF fine either way) | Index the human page |
| Impressum | Index | Required to be reachable; index it |
| Duplicate/gated legal variants, print versions, `?preview=` | **`noindex`** | Avoid duplicate/thin indexing |

Rules:

- [ ] Do **not** `Disallow` legal pages in robots.txt to hide them — blocked pages can still be indexed without a snippet. Use a `noindex` **meta robots** / `X-Robots-Tag` on a **crawlable** page instead (see [`../seo/technical-seo.md`](../seo/technical-seo.md)).
- [ ] Self-referencing `rel=canonical` on each indexable legal page, early in `<head>`.
- [ ] Don't canonicalize to a `noindex`/404 page; keep canonical/sitemap consistent.
- [ ] Title ≤ ~60 chars (front-load): e.g., `Privacy Policy | {{BRAND_NAME}}`.
- [ ] Meta description ~150–160 chars, unique per page.
- [ ] Single `<h1>` per page; logical `h2`/`h3` for sections.
- [ ] Include indexable legal pages in the XML sitemap (exclude `noindex` ones).
- [ ] Structured data optional; NAP in these pages must match `LocalBusiness`/`Organization` schema.

`<head>` snippet:

```html
<title>Privacy Policy | {{BRAND_NAME}}</title>
<meta name="description" content="How {{BRAND_NAME}} collects, uses, and protects your data, and the privacy rights you can exercise.">
<link rel="canonical" href="https://{{DOMAIN}}/privacy">
<!-- Indexable by default. For duplicate/print variants only: -->
<!-- <meta name="robots" content="noindex,follow"> -->
```

---

## 15. Last-updated / versioning pattern

Apply this identical block near the top of **every** legal page:

```markdown
**Effective:** {{EFFECTIVE_DATE}} · **Last updated:** {{LAST_UPDATED}} · **Version:** {{VERSION}}
```

- [ ] Use **ISO 8601** dates (`2026-07-01`).
- [ ] **Effective** = when the version takes force; **Last updated** = last material change. They can differ (advance-notice period).
- [ ] Bump `{{VERSION}}` (`v1.0` → `v1.1`) on every change; keep a short **change log** (date + summary) at the bottom of the page or in a `/legal/changelog`.
- [ ] For **material** changes, notify users in advance where required (email/banner/in-product), especially for ToS, Privacy, SMS Terms.
- [ ] Keep an internal archive of superseded versions (defensible record).
- [ ] Emit a machine-readable `dateModified` in page metadata if you use `WebPage` schema.

Change-log skeleton:

```markdown
## Change log
| Date | Version | Summary |
|---|---|---|
| {{LAST_UPDATED}} | {{VERSION}} | Initial publication. |
```

---

## 16. Lawyer hand-off checklist (do before publishing)

- [ ] Every `{{PLACEHOLDER}}` resolved (search the repo for `{{`).
- [ ] Controller/processor split confirmed (Privacy vs DPA scope).
- [ ] Legal bases mapped per purpose (GDPR/UK GDPR).
- [ ] CCPA/CPRA (+ other US state) rights, "sell/share" determination, and GPC honoring confirmed.
- [ ] SMS opt-in language + STOP/HELP flow matches what's registered in A2P 10DLC via `{{SMS_PROVIDER}}`; TCPA consent records in place.
- [ ] AI disclosure + call-recording consent reviewed for your operating states/countries.
- [ ] Liability caps, arbitration/class-waiver, and governing law reviewed for enforceability in `{{GOVERNING_LAW}}`.
- [ ] Sub-processor list is live, accurate, and linked.
- [ ] Impressum details verified (if EU/DE exposure).
- [ ] Accessibility statement doesn't over-claim vs actual conformance.
- [ ] **A qualified attorney has reviewed and approved every page.**

> **Reminder:** This document is a structural template and checklist, **not legal counsel**. Publishing is a legal decision — get sign-off.

---

## Related

- [`../00-foundations/project-brief.md`](../00-foundations/project-brief.md) — business, audience, offer, NAP source of truth for placeholders.
- [`../00-foundations/brand-strategy.md`](../00-foundations/brand-strategy.md) — voice/tone to keep legal copy on-brand without softening meaning.
- [`../seo/technical-seo.md`](../seo/technical-seo.md) — canonical, robots meta vs robots.txt, `noindex`, sitemap, NAP/schema consistency.
- [`../seo/onsite-seo.md`](../seo/onsite-seo.md) — titles/meta length, single H1, descriptive anchors, `<head>` template.
- [`../seo/ai-seo-geo.md`](../seo/ai-seo-geo.md) — extractable answers, E-E-A-T, entity/NAP consistency for AI answers.
- [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md) — WCAG 2.2 AA target for the consent banner and pages.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — tokens for styling the consent banner/preference center.
