# Design System

**Purpose:** The landing index for the applied design system — how {{BRAND_NAME}}'s tokens become real, accessible, on-brand UI. Start here to build or style anything.
**Status:** v1 foundation — adjustable.

---

The design system turns the [design tokens](../../tokens/design-tokens.json) (the *values*) into the *rules and components* you build pages from. It sits between the **brand** docs (identity: colour, type, voice) and the eventual page markup. Every value referenced here is consumed by name from the tokens — never hardcoded.

## Documents

| Doc | Owns (source of truth for) | Open when you need to… |
| --- | --- | --- |
| [`design-tokens.md`](./design-tokens.md) | The token architecture (primitive → semantic/role), how to consume them in CSS/Tailwind, and the change/governance process | Understand or extend the token system |
| [`layout-and-grid.md`](./layout-and-grid.md) | Containers (1200/1440/68ch), the responsive gutter, the 12-column grid, vertical rhythm, and section templates | Lay out a page or section |
| [`components.md`](./components.md) | The component contracts — Button, Link, Input, Card, Accordion, Nav, Modal, etc. — with states, tokens, a11y, and minimal HTML | Build or style a UI component |
| [`interactive-elements.md`](./interactive-elements.md) | CTA hierarchy, forms & validation UX, conversion elements (book-a-call/chat), and interaction feedback | Place a CTA, design a form, or wire the primary conversion flow |
| [`motion.md`](./motion.md) | Motion tokens (durations/easings), standard animation patterns, performance rules, and mandatory reduced-motion handling | Animate anything |

## How to use it

1. **Values come from tokens.** Import [`tokens/tokens.css`](../../tokens/tokens.css) (CSS custom properties) or [`tokens/tailwind.tokens.js`](../../tokens/tailwind.tokens.js). Reference by name (`--color-brand-600`, `--space-4`) — see [`design-tokens.md`](./design-tokens.md).
2. **Colour is governed.** Allowed pairings are fixed by [`../brand/color-system.md`](../brand/color-system.md) and proven in [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md). Use role tokens (`--cta-bg`, `--text`, `--focus-ring`) and you can't ship a failing pairing.
3. **Accessibility is built in, not bolted on.** Every component spec lists its keyboard/ARIA/target-size requirements against [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md) (WCAG 2.2 AA).
4. **Stay in budget.** Interactive/animated pieces must respect the [performance budget](../performance/performance-budget.md) and reduced-motion.
5. **Compose, then ship.** Follow [`../systems/content-workflow.md`](../systems/content-workflow.md) and the [new-page checklist](../../checklists/new-page.md).

## Guardrails

- **Tokens over hardcoding** (ADR-0010). No raw hex/px in components.
- **One primary CTA per view** (see [`interactive-elements.md`](./interactive-elements.md)).
- **44px touch targets, visible focus, reduced-motion** — non-negotiable (ADR-0004).
- **Sentence-case UI copy** per [`../brand/voice-and-tone.md`](../brand/voice-and-tone.md).

---

## Related

- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — the value source of truth.
- [`../brand/color-system.md`](../brand/color-system.md) — allowed colour usage.
- [`../brand/typography.md`](../brand/typography.md) — type scale and font loading.
- [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md) — the a11y bar every component meets.
- [`../responsive/responsive-standards.md`](../responsive/responsive-standards.md) — breakpoints and responsive rules.
- [`../systems/content-workflow.md`](../systems/content-workflow.md) — how components become shipped pages.
