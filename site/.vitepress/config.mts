import { defineConfig } from 'vitepress'

const repo = process.env.GITHUB_REPOSITORY
const owner = repo?.split('/')[0]
const name = repo?.split('/')[1]
const base = process.env.SITE_BASE ?? (name && name !== `${owner}.github.io` ? `/${name}/` : '/')
if (!base.startsWith('/') || !base.endsWith('/')) throw new Error('SITE_BASE must start and end with /')

export default defineConfig({
  title: 'Calculus Workbook',
  description: 'A worked calculus review with explicit notation, visible algebra, and help one step at a time.',
  lang: 'en-US',
  base,
  cleanUrls: false,
  srcExclude: ['public/**'],
  lastUpdated: true,
  head: [['meta', { name: 'theme-color', content: '#244a73' }]],
  markdown: { math: true },
  themeConfig: {
    siteTitle: 'Calculus Workbook · Alpha',
    nav: [
      { text: 'Read', link: '/start' },
      { text: 'Practice', link: '/practice' },
      { text: 'Notation', link: '/generated/notation' },
      { text: 'About', link: '/about' }
    ],
    sidebar: [
      { text: 'Begin here', items: [
        { text: 'How to use this book', link: '/start' },
        { text: 'Notation standard', link: '/generated/notation' },
        { text: 'Curriculum & reading routes', link: '/generated/curriculum' }
      ] },
      { text: 'Practice with full solutions', items: [
        { text: 'Problem collection', link: '/practice' },
        { text: 'D2-001 · The chain rule', link: '/problems/d2-001' },
        { text: 'I2-001 · Substitution', link: '/problems/i2-001' }
      ] },
      { text: 'Reference & project', items: [
        { text: 'Literature & notation decisions', link: '/generated/references' },
        { text: 'Complete worked examples', link: '/generated/examples' },
        { text: 'Downloads', link: '/downloads' },
        { text: 'Sharing, accuracy & contributions', link: '/about' }
      ] }
    ],
    search: { provider: 'local' },
    outline: [2, 3],
    footer: {
      message: 'Book: CC BY-SA 4.0 · Site code: MIT · Provided as-is; correctness is not guaranteed.',
      copyright: '© 2026 Calculus Workbook contributors'
    },
    ...(repo ? {
      socialLinks: [{ icon: 'github', link: `https://github.com/${repo}` }]
    } : {})
  }
})
