import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import AlphaNotice from './AlphaNotice.vue'
import './custom.css'
export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, {
    'doc-before': () => h(AlphaNotice),
    'home-hero-info-before': () => h(AlphaNotice)
  })
}
