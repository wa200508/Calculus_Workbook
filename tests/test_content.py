import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


content = load('build_content')
checker = load('check_site')


class ContentTests(unittest.TestCase):
    def test_manuscript_has_matching_problem_hint_solution_ids(self):
        groups = content.problem_sections((ROOT / 'PILOT_EXAMPLES.md').read_text())
        self.assertEqual(set(groups['Problems']), {'D2-001', 'I2-001'})
        for _, solution in groups['Complete solutions'].values():
            self.assertIn('CHECK', solution)

    def test_missing_solution_is_rejected(self):
        text = (ROOT / 'PILOT_EXAMPLES.md').read_text()
        head, tail = text.split('## Complete solutions', 1)
        with self.assertRaisesRegex(ValueError, 'matching'):
            content.problem_sections(head + '## Complete solutions' + tail.replace('### I2-001', '### I2-002'))

    def test_all_chapters_have_complete_problem_sets(self):
        manuscripts = {name: (ROOT / name).read_text() for name in content.PROBLEM_SOURCES}
        groups = content.collect_problems(manuscripts)
        self.assertEqual(len(groups['Problems']), 40)
        for identifier, (_, solution) in groups['Complete solutions'].items():
            self.assertIn('CHECK', solution, identifier)
            self.assertIn('SETUP', solution, identifier)
            self.assertIn('CHOICE', solution, identifier)
            hints = groups['Hint ladders'][identifier][1]
            self.assertEqual(len(content.re.findall(r'^\d+\. ', hints, flags=content.re.M)), 3, identifier)

    def test_duplicate_problem_ids_across_chapters_are_rejected(self):
        manuscripts = {name: (ROOT / name).read_text() for name in content.PROBLEM_SOURCES}
        manuscripts['DIFFERENTIATION_SCALARS.md'] = manuscripts['DIFFERENTIATION_RULES.md']
        with self.assertRaisesRegex(ValueError, 'multiple manuscripts'):
            content.collect_problems(manuscripts)

    def test_latex_preserves_absolute_value_in_table_cell(self):
        tex = content.markdown_to_tex('# Test\n\n| Meaning | Formula |\n|---|---|\n| Magnitude | $|x|$ |\n')
        self.assertIn(r'\(|x|\)', tex)
        self.assertEqual(tex.count(' & '), 2)

    def test_derivative_delimiters_and_dependencies_survive_export(self):
        expression = r'\frac{d}{dx}\left(f(x)\right)'
        self.assertIn(expression, content.markdown_to_tex('# Test\n\n$$\n' + expression + '\n$$'))

    def test_math_renderer_errors_are_detected(self):
        page = checker.Page()
        page.feed('<mjx-container><svg><g data-mml-node="merror"></g></svg></mjx-container>')
        self.assertEqual(page.math_count, 1)
        self.assertTrue(page.errors)

    def test_supporting_tricks_are_distinct_from_algebra(self):
        sample = '# Example\n\n**Step 1 — TRICK: identity.**\n\n$x=x$\n\n**Step 2 — ALGEBRA.**\n\n$x+0=x$\n'
        html = content.style_algebra(sample)
        self.assertIn('class="trick-step"', html)
        self.assertIn('class="algebra-step"', html)
        tex = content.markdown_to_tex(sample)
        self.assertIn(r'\color{TrickPurple}', tex)
        self.assertIn(r'\color{AlgebraBlue}', tex)

    def test_closed_solution_and_individual_hints_are_generated(self):
        content.build()
        page = (ROOT / 'site/problems/i2-001.md').read_text()
        self.assertIn('<details class="solution">', page)
        self.assertNotIn('<details class="solution" open', page)
        self.assertEqual(page.count('::: details Hint '), 3)
        self.assertIn('algebra-step', page)

    def test_editorial_outline_is_not_published(self):
        content.build()
        self.assertNotIn('curriculum', (ROOT / 'site/generated/book.md').read_text().lower())
        self.assertNotIn('curriculum', (ROOT / 'calculus_workbook.tex').read_text().lower())
        self.assertFalse((ROOT / 'site/generated/curriculum.md').exists())
        self.assertFalse((ROOT / 'site/public/downloads/CURRICULUM.md').exists())


if __name__ == '__main__':
    unittest.main()
