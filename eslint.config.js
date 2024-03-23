import antfu from '@antfu/eslint-config'

export default antfu(
  {
    typescript: true,
    vue: true,
    unocss: true,
    toml: false,
    markdown: false,
  },
)
