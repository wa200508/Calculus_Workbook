import { defineConfig } from 'vitepress'
import { readFileSync } from 'node:fs'

const problems = JSON.parse(readFileSync(new URL('../generated/problem-index.json', import.meta.url), 'utf8')) as Array<{
  id: string, title: string, chapter: string, chapterTitle: string, link: string
}>
const chapters = [...new Set(problems.map(problem => problem.chapter))]
const chapterSidebar = chapters.map(chapter => ({
  text: `${chapter} · ${problems.find(problem => problem.chapter === chapter)!.chapterTitle}`,
  collapsed: chapter !== 'D1',
  items: [
    { text: 'Chapter guide & rules', link: `/generated/${({ D1: 'scalar-derivatives', D2: 'derivative-rules', I1: 'scalar-integrals', I2: 'substitution' } as Record<string,string>)[chapter]}` },
    ...problems.filter(problem => problem.chapter === chapter).map(problem => ({
      text: `${problem.id} · ${problem.title}`, link: problem.link
    }))
  ]
}))

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
      { text: 'Full book', link: '/generated/book' },
      { text: 'Read', link: '/start' },
      { text: 'Practice', link: '/practice' },
      { text: 'Notation', link: '/generated/notation' },
      { text: 'Tricks', link: '/generated/tricks' },
      { text: 'About', link: '/about' }
    ],
    sidebar: [
      { text: 'Begin here', items: [
        { text: 'How to use this book', link: '/start' },
        { text: 'Complete book · One page', link: '/generated/book' },
        { text: 'Notation standard', link: '/generated/notation' },
      ] },
      { text: 'Practice', items: [{ text: 'All problems', link: '/practice' }] },
      ...chapterSidebar,
      { text: 'Reference & project', items: [
        { text: 'Tricks & identities · Purple appendix', link: '/generated/tricks' },
        { text: 'Literature & notation decisions', link: '/generated/references' },
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
