/**
 * AI Appointment Agency — Tailwind theme extension
 * Mirrors tokens/design-tokens.json (single source of truth).
 *
 * Usage (tailwind.config.js):
 *   const tokens = require('./tokens/tailwind.tokens.js');
 *   module.exports = { theme: { extend: tokens } };
 *
 * Framework-agnostic: if not using Tailwind, consume tokens/tokens.css instead.
 */
module.exports = {
  colors: {
    brand: {
      50: '#EEF2FF', 100: '#E0E7FF', 200: '#C7D2FE', 300: '#A5B4FC',
      400: '#818CF8', 500: '#6366F1', 600: '#4F46E5', 700: '#4338CA',
      800: '#3730A3', 900: '#312E81',
      DEFAULT: '#4F46E5',
    },
    accent: {
      400: '#22D3EE', 500: '#06B6D4', 600: '#0891B2', 700: '#0E7490',
      DEFAULT: '#06B6D4',
    },
    ink: '#0B1120',
    neutral: {
      50: '#F8FAFC', 100: '#F1F5F9', 200: '#E2E8F0', 300: '#CBD5E1',
      400: '#94A3B8', 500: '#64748B', 600: '#475569', 700: '#334155',
      800: '#1E293B', 900: '#0F172A',
    },
    success: { DEFAULT: '#16A34A', strong: '#15803D' },
    warning: '#D97706',
    danger: '#DC2626',
    info: '#2563EB',
  },
  fontFamily: {
    display: ['Sora', 'Sora Fallback', 'system-ui', 'sans-serif'],
    body: ['Inter', 'Inter Fallback', 'system-ui', 'sans-serif'],
    mono: ['JetBrains Mono', 'ui-monospace', 'monospace'],
  },
  fontSize: {
    xs: '0.75rem', sm: '0.875rem', base: '1rem', lg: '1.125rem',
    xl: '1.25rem', '2xl': '1.5rem', '3xl': '1.875rem', '4xl': '2.25rem',
    '5xl': '3rem', '6xl': '3.75rem', '7xl': '4.5rem',
    'fluid-h1': 'clamp(2.25rem, 1.4rem + 4.25vw, 4.5rem)',
    'fluid-h2': 'clamp(1.875rem, 1.3rem + 2.9vw, 3rem)',
    'fluid-h3': 'clamp(1.5rem, 1.2rem + 1.5vw, 2.25rem)',
  },
  lineHeight: { tight: '1.1', snug: '1.25', normal: '1.5', relaxed: '1.65' },
  letterSpacing: { tighter: '-0.02em', tight: '-0.01em', normal: '0em', wide: '0.02em' },
  spacing: {
    1: '0.25rem', 2: '0.5rem', 3: '0.75rem', 4: '1rem', 5: '1.25rem',
    6: '1.5rem', 8: '2rem', 10: '2.5rem', 12: '3rem', 16: '4rem',
    20: '5rem', 24: '6rem', 32: '8rem',
  },
  borderRadius: {
    sm: '0.375rem', md: '0.5rem', lg: '0.75rem', xl: '1rem', '2xl': '1.5rem', full: '9999px',
  },
  boxShadow: {
    xs: '0 1px 2px 0 rgb(11 17 32 / 0.05)',
    sm: '0 1px 3px 0 rgb(11 17 32 / 0.08), 0 1px 2px -1px rgb(11 17 32 / 0.08)',
    md: '0 4px 6px -1px rgb(11 17 32 / 0.08), 0 2px 4px -2px rgb(11 17 32 / 0.08)',
    lg: '0 10px 15px -3px rgb(11 17 32 / 0.10), 0 4px 6px -4px rgb(11 17 32 / 0.10)',
    xl: '0 20px 25px -5px rgb(11 17 32 / 0.12), 0 8px 10px -6px rgb(11 17 32 / 0.12)',
    focus: '0 0 0 3px rgb(79 70 229 / 0.45)',
  },
  screens: { sm: '640px', md: '768px', lg: '1024px', xl: '1280px', '2xl': '1536px' },
  maxWidth: { content: '1200px', wide: '1440px', prose: '68ch' },
  zIndex: {
    dropdown: '1000', sticky: '1100', overlay: '1200',
    modal: '1300', toast: '1400', tooltip: '1500',
  },
  transitionDuration: {
    instant: '100ms', fast: '150ms', base: '200ms', slow: '300ms', slower: '500ms',
  },
  transitionTimingFunction: {
    standard: 'cubic-bezier(0.4, 0, 0.2, 1)',
    decelerate: 'cubic-bezier(0, 0, 0.2, 1)',
    accelerate: 'cubic-bezier(0.4, 0, 1, 1)',
    spring: 'cubic-bezier(0.34, 1.56, 0.64, 1)',
  },
};
