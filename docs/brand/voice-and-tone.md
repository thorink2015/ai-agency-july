# Voice & Copy System

**Purpose:** The execution-level rules for writing every word on the site — microcopy, CTAs, errors, labels, terminology, and mechanics — so copy is consistent, accessible, and unmistakably {{BRAND_NAME}}. This doc *operationalizes* the voice summary in [brand-strategy.md §3](../00-foundations/brand-strategy.md); read that first for the strategy, this for the how.
**Status:** v1 foundation — adjustable.

---

## 1. Voice in one line

**Clear, direct, benefit-led, jargon-light, reassuring. Second person. Short sentences. Confidence without hype.**

We sound like a competent, calm expert who respects the reader's time — not a hype-machine and not a robot. When in doubt, **say the plain thing and lead with the payoff.**

## 2. Tone by context

Voice is constant; tone flexes. Match the reader's emotional state.

| Context | Reader is… | Tone | Example |
| --- | --- | --- | --- |
| Hero / value prop | Skimming, skeptical | Confident, outcome-first | "Never miss a lead." |
| How-it-works / features | Evaluating | Plain, explanatory, calm | "We connect it to your CRM and calendar, then run it for you." |
| Pricing / commitment | Cautious | Transparent, low-pressure | "No setup fee. Cancel anytime." |
| Forms / labels | Task-focused | Minimal, guiding | "Work email" · "We'll only use this to send your demo link." |
| Errors / support | Frustrated | Warm, accountable, human | "That didn't go through. Check the number and try again." |
| Success / confirmation | Relieved | Brief, affirming | "You're booked. Check your inbox for the details." |
| Social proof | Comparing | Specific, let numbers talk | "Booked 43% more calls in the first month." |

## 3. Mechanics (house style)

| Rule | Standard |
| --- | --- |
| **Person** | Second person ("you/your"). We = "we", never "the company" or "{{BRAND_NAME}} Inc." in body copy. |
| **Sentence length** | Prefer < 20 words. Break long sentences. One idea per sentence. |
| **Reading level** | Aim Grade 6–8 (plain English). Test long-form with a readability check. |
| **Capitalization** | **Sentence case** for headings, buttons, and labels ("Book a demo", not "Book A Demo"). Reserve Title Case for proper nouns. |
| **Punctuation** | Oxford comma. One space after periods. No multiple `!!!`. Max one exclamation per screen. |
| **Numbers** | Numerals for 0–9 and up ("3 steps", "seconds", "24/7"). Always pair a claim-number with a source. |
| **Dates/times** | "1 Jul 2026" or "July 1, 2026" — pick one per locale and stay consistent. 12-hour with am/pm for times. |
| **Contractions** | Yes — they're warmer ("you'll", "we'll", "it's"). |
| **Abbreviations** | Spell out on first use ("speed-to-lead (STL)"). Avoid internal jargon entirely in public copy. |
| **Emphasis** | Bold for scannable keywords. Never ALL-CAPS for emphasis (accessibility + shouting). No underlines except links. |
| **Oxford/US vs UK spelling** | Pick one per `{{DOMAIN}}` locale; default US English unless the owner says otherwise. |

## 4. Words we use / avoid

| Say this | Not this |
| --- | --- |
| answer, respond, book, qualify, follow up | leverage, utilize, facilitate |
| set up / run it for you | onboard synergies, operationalize |
| works with your tools | seamless omnichannel integration |
| fast, in seconds, 24/7 | blazing-fast, lightning-quick, next-gen |
| real person / human on call | fully autonomous, no humans needed |
| your leads, your calendar | our valued customers, end-users |
| clear, simple | frictionless, turnkey, robust |

**Banned words (public copy):** revolutionary, cutting-edge, game-changer, synergy, paradigm, disrupt, world-class, best-in-class (unbacked), unprecedented. **Banned punctuation:** `!!!`, ALL-CAPS words, ⚡/🔥-style emoji in headlines.

## 5. Microcopy patterns

### CTAs (buttons & links)
- **Start with a verb, name the value:** "Book a demo", "Get a lead-response plan", "See how it works", "Talk to a human".
- **One primary CTA per view** (see [interactive-elements.md](../design-system/interactive-elements.md)). Secondary CTAs are lower-emphasis and complementary ("See pricing").
- **Buttons perform actions; links navigate.** Don't style a nav link as a button unless it triggers the primary action.
- **Avoid dead ends:** "Submit", "Click here", "Learn more" (unspecific). Prefer "Book my demo", "Read the setup guide".
- **Link text is meaningful out of context** (WCAG 2.4.4 / screen readers): the linked words describe the destination.

### Forms
- **Labels:** always visible, above the field, sentence case, plain ("Work email", not "E-mail Address*"). Never placeholder-as-label.
- **Help text:** one short line, states *why* or *what format* ("So we can text your booking confirmations.").
- **Required/optional:** mark the *optional* ones if most are required, or vice-versa — whichever is fewer. Don't rely on `*` alone; add text.
- **Errors:** specific, human, and actionable — say what's wrong and how to fix it. Announce them accessibly (see [accessibility-standards.md](../accessibility/accessibility-standards.md)).

| Situation | Copy |
| --- | --- |
| Empty required field | "Add your work email so we can send the demo link." |
| Invalid format | "That email doesn't look right — check for a typo." |
| Server/unknown error | "Something went wrong on our end. Try again, or email {{EMAIL}}." |
| Success | "You're booked. We've emailed the details to {email}." |
| Loading | "Booking your call…" (not "Please wait") |

### SMS/consent microcopy (this business texts leads)
- Consent must be explicit and plain: "By sharing your number, you agree to receive appointment texts from {{BRAND_NAME}}. Reply STOP to opt out. Msg & data rates may apply."
- Keep this consistent with [legal-pages.md](../legal/legal-pages.md) (SMS/A2P consent) — never soften it into a hidden pre-checked box.

## 6. Voice by page type (quick specs)

| Page | Job of the copy | Voice notes |
| --- | --- | --- |
| Home / hero | Land the promise + one proof + primary CTA | Punchy, outcome-first, one idea |
| Services | Explain the offer plainly, tie each to a pillar | Calm, concrete, benefit → how |
| Use-cases / industries | Mirror the reader's world back to them | "your clinic", "your leads" — specific |
| Pricing | Remove risk, be transparent | Low-pressure, no dark patterns |
| About | Earn trust: real people, real expertise (E-E-A-T) | Warm, credible, first-person "we" |
| FAQ | Answer the real objection in the first sentence | Extractable, self-contained answers (also feeds GEO — see [ai-seo-geo.md](../seo/ai-seo-geo.md)) |
| Legal | Accurate, readable, no fake friendliness | Plain, precise (see [legal-pages.md](../legal/legal-pages.md)) |

## 7. Accessibility & SEO of copy

- **Front-load the answer.** Start sections with a self-contained sentence that states the point — helps skimmers, screen-reader users, and AI answer engines lift it as a citation.
- **Descriptive headings** in a logical order (one H1, no skipped levels) — headings are the copy skeleton, not styling.
- **Alt text voice:** describe the *meaning/function* of an image in plain words; decorative images get empty alt. See [imagery.md](./imagery.md).
- **Meta copy:** titles ≤ 60 chars, meta descriptions ≤ 155 chars, benefit-led — see [onsite-seo.md](../seo/onsite-seo.md).
- **Don't keyword-stuff.** Write for the reader; the SEO follows the clarity.

## 8. Copy QA checklist (before publish)

- [ ] Leads with the benefit; the payoff isn't buried.
- [ ] Second person, short sentences, sentence case.
- [ ] No banned words / no hype / ≤ 1 exclamation per screen.
- [ ] Every claim has a proof point or cited number nearby.
- [ ] One primary CTA; CTA + link text are meaningful out of context.
- [ ] Form labels visible; error/success/loading copy present and human.
- [ ] SMS/consent language matches legal, if applicable.
- [ ] Headings form a logical outline; first sentence of each section is liftable.
- [ ] Reading level ~Grade 6–8; jargon removed.
- [ ] Placeholders ({{BRAND_NAME}}, {{DOMAIN}}, {{EMAIL}}, {{PHONE}}) still intact where real values aren't set.

---

## Related

- [`../00-foundations/brand-strategy.md`](../00-foundations/brand-strategy.md) — positioning, voice strategy, messaging pillars, naming, taglines.
- [`brand-guidelines.md`](./brand-guidelines.md) — brand overview that indexes this doc.
- [`../design-system/interactive-elements.md`](../design-system/interactive-elements.md) — CTA hierarchy and form UX this copy fills.
- [`../seo/onsite-seo.md`](../seo/onsite-seo.md) — titles, meta, on-page copy standards.
- [`../seo/ai-seo-geo.md`](../seo/ai-seo-geo.md) — extractable-answer writing for AI engines.
- [`../legal/legal-pages.md`](../legal/legal-pages.md) — consent and legal copy structures.
