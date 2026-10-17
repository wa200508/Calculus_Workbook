import { defineConfig } from 'vitepress'
import { readFileSync } from 'node:fs'

const problems = JSON.parse(readFileSync(new URL('../generated/problem-index.json', import.meta.url), 'utf8')) as Array<{
  id: string, title: string, chapter: string, chapterTitle: string, chapterLink: string, reference: boolean, link: string
}>
const chapters = [...new Set(problems.map(problem => problem.chapter))]
const chapterSidebar = (reference: boolean) => chapters
  .filter(chapter => problems.find(problem => problem.chapter === chapter)!.reference === reference)
  .map(chapter => ({
    text: problems.find(problem => problem.chapter === chapter)!.chapterTitle,
    collapsed: true,
    items: [
      { text: reference ? 'Reference exercises' : 'Problem set', link: problems.find(problem => problem.chapter === chapter)!.chapterLink },
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
      { text: 'Quick reference', link: '/generated/quick-reference' },
      { text: 'Methods', link: '/generated/methods' },
      { text: 'Notation', link: '/generated/notation' },
      { text: 'Tricks', link: '/generated/tricks' },
      { text: 'About', link: '/about' }
    ],
    sidebar: [
      { text: 'Begin here', items: [
        { text: 'About the workbook', link: '/start' },
        { text: 'Complete book · One page', link: '/generated/book' },
        { text: 'Four-page quick reference', link: '/generated/quick-reference' },
        { text: 'Notation standard', link: '/generated/notation' },
        { text: 'Calculus methods reference', link: '/generated/methods' },
      ] },
      { text: 'Practice', items: [{ text: 'All problems', link: '/practice' }] },
      ...chapterSidebar(false),
      { text: 'Optional reference exercises', collapsed: true, items: [{ text: 'Reference collection', link: '/reference-exercises' }, ...chapterSidebar(true)] },
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
