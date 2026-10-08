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

    def test_closed_solution_and_individual_hints_are_generated(self):
        content.build()
        page = (ROOT / 'site/problems/i2-001.md').read_text()
        self.assertIn('<details class="solution">', page)
        self.assertNotIn('<details class="solution" open', page)
        self.assertEqual(page.count('::: details Hint '), 3)
        self.assertIn('algebra-step', page)


if __name__ == '__main__':
    unittest.main()
