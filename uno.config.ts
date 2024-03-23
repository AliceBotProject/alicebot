import { defineConfig, presetIcons, presetUno } from 'unocss'

export default defineConfig({
  shortcuts: {
    'i-mdi-python': 'i-mdi-language-python', // 防止和 VitePress 内置样式冲突
  },
  theme: {
    colors: {
      vp: {
        neutral: 'var(--vp-c-neutral)',
        bg: {
          1: 'var(--vp-c-bg)',
          alt: 'var(--vp-c-bg-alt)',
          elv: 'var(--vp-c-bg-elv)',
          soft: 'var(--vp-c-bg-soft)',
        },
        border: 'var(--vp-c-border)',
        divider: 'var(--vp-c-divider)',
        gutter: 'var(--vp-c-gutter)',
        text: {
          1: 'var(--vp-c-text-1)',
          2: 'var(--vp-c-text-2)',
          3: 'var(--vp-c-text-3)',
        },
        default: {
          1: 'var(--vp-c-default-1)',
          2: 'var(--vp-c-default-2)',
          3: 'var(--vp-c-default-3)',
          soft: 'var(--vp-c-default-soft)',
        },
        brand: {
          1: 'var(--vp-c-brand-1)',
          2: 'var(--vp-c-brand-2)',
          3: 'var(--vp-c-brand-3)',
          soft: 'var(--vp-c-brand-soft)',
        },
      },
    },
  },
  presets: [
    presetUno(),
    presetIcons(),
  ],
})
