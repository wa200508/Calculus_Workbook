import ast
import importlib.util
import math
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
        self.assertEqual(len(groups['Problems']), 92)
        counts = {'D4': 16, 'D3': 17, 'I4': 16, 'I3': 19,
                  'D1': 6, 'D2': 7, 'I1': 6, 'I2': 5}
        expected_ids = {f'{code}-{number:03d}'
                        for code, count in counts.items()
                        for number in range(1, count + 1)}
        self.assertEqual(set(groups['Problems']), expected_ids)
        for identifier, (_, solution) in groups['Complete solutions'].items():
            self.assertIn('CHECK', solution, identifier)
            self.assertIn('SETUP', solution, identifier)
            self.assertIn('CHOICE', solution, identifier)
            hints = groups['Hint ladders'][identifier][1]
            self.assertEqual(len(content.re.findall(r'^\d+\. ', hints, flags=content.re.M)), 3, identifier)

    def test_main_sets_begin_with_problems_and_reference_exercises_are_separate(self):
        main_count = reference_count = 0
        for collection, is_reference in [(content.MAIN_SETS, False), (content.REFERENCE_SETS, True)]:
            for filename, _, _, _ in collection:
                manuscript = (ROOT / filename).read_text()
                introductory_lines = manuscript.split('## Problems')[0].strip().splitlines()
                self.assertEqual(len(introductory_lines), 1, filename)
                count = len(content.problem_sections(manuscript)['Problems'])
                if is_reference:
                    reference_count += count
                else:
                    main_count += count
        self.assertEqual((main_count, reference_count), (68, 24))
        filenames = list(content.SOURCES)
        self.assertLess(filenames.index('METHODS_REFERENCE.md'), filenames.index(content.MAIN_SETS[0][0]))
        self.assertLess(filenames.index(content.MAIN_SETS[-1][0]), filenames.index('TRICKS_APPENDIX.md'))
        self.assertLess(filenames.index('TRICKS_APPENDIX.md'), filenames.index(content.REFERENCE_SETS[0][0]))

    def test_printed_problems_are_followed_by_their_own_solutions(self):
        for filename in content.PROBLEM_SOURCES:
            manuscript = (ROOT / filename).read_text()
            groups = content.problem_sections(manuscript)
            tex = content.worked_chapter_to_tex(manuscript)
            self.assertNotIn(r'\section{Problems}', tex)
            self.assertNotIn(r'\section{Complete solutions}', tex)
            self.assertNotIn(r'\section{Hint ladders}', tex)
            identifiers = list(groups['Problems'])
            for i, identifier in enumerate(identifiers):
                start = tex.index(r'\label{problem:' + identifier + '}')
                end = tex.index(r'\label{problem:' + identifiers[i+1] + '}') if i+1 < len(identifiers) else len(tex)
                block = tex[start:end]
                prompt = content.markdown_to_tex('# Statement\n\n' + groups['Problems'][identifier][1])
                solution = content.markdown_to_tex('# Solution\n\n' + groups['Complete solutions'][identifier][1])
                self.assertIn(prompt, block)
                self.assertIn(solution, block)
                self.assertLess(block.index(prompt), block.index(solution))
                self.assertIn(r'\pageref{hints:' + identifier + '}', block)
            hints = content.hints_to_tex(groups)
            for identifier in groups['Problems']:
                self.assertIn(r'\label{hints:' + identifier + '}', hints)
                self.assertIn(r'\pageref{problem:' + identifier + '}', hints)

    def test_numeric_comparisons_reject_nonfinite_values(self):
        # Load the actual comparison functions without executing each script's
        # top-level numerical suite a second time during the unit-test run.
        for filename in ('check_advanced_math.py', 'check_differentiation_expansion.py',
                         'check_integration_expansion.py',
                         'check_differentiation_expansion_2.py',
                         'check_integration_expansion_2.py'):
            path = ROOT / 'scripts' / filename
            tree = ast.parse(path.read_text(), filename=str(path))
            helpers = [node for node in tree.body
                       if isinstance(node, ast.FunctionDef) and node.name in ('near', 'between')]
            namespace = {'math': math, 'checks': 0}
            exec(compile(ast.Module(body=helpers, type_ignores=[]), str(path), 'exec'), namespace)
            prefix = () if filename == 'check_advanced_math.py' else ('regression',)
            compare = namespace['near']
            compare(*prefix, 1.0, 1.0)
            compare(*prefix, 1+2j, 1+2j)
            with self.assertRaises(AssertionError):
                compare(*prefix, 1, 2)
            for actual, expected in ((1, math.inf), (math.inf, 1),
                                     (math.nan, 1), (1, math.nan),
                                     (complex(1, math.inf), 1),
                                     (complex(1, math.nan), 1),
                                     (1, complex(1, math.inf)),
                                     (1, complex(1, math.nan))):
                with self.subTest(script=filename, actual=actual, expected=expected):
                    with self.assertRaises(AssertionError):
                        compare(*prefix, actual, expected)
            for tolerance in (math.inf, math.nan, -1):
                with self.subTest(script=filename, tolerance=tolerance):
                    with self.assertRaises(AssertionError):
                        compare(*prefix, 1, 1, tolerance)
            if 'between' in namespace:
                interval = namespace['between']
                interval('regression', 1, 0, 2)
                with self.assertRaises(AssertionError):
                    interval('regression', 3, 0, 2)
                for actual, lower, upper, slack in (
                        (math.inf, 0, math.inf, 0), (1, 0, math.inf, 0),
                        (1, -math.inf, 2, 0),
                        (math.nan, 0, 2, 0), (1, math.nan, 2, 0),
                        (1, 0, 2, math.inf), (1, 0, 2, -1), (1, 2, 0, 0)):
                    with self.subTest(interval=(actual, lower, upper, slack)):
                        with self.assertRaises(AssertionError):
                            interval('regression', actual, lower, upper, slack)

    def test_duplicate_problem_ids_across_chapters_are_rejected(self):
        manuscripts = {name: (ROOT / name).read_text() for name in content.PROBLEM_SOURCES}
        manuscripts['DIFFERENTIATION_SCALARS.md'] = manuscripts['DIFFERENTIATION_RULES.md']
        with self.assertRaisesRegex(ValueError, 'multiple manuscripts'):
            content.collect_problems(manuscripts)

    def test_latex_preserves_absolute_value_in_table_cell(self):
        tex = content.markdown_to_tex('# Test\n\n| Meaning | Formula |\n|---|---|\n| Magnitude | $|x|$ |\n')
        self.assertIn(r'\(|x|\)', tex)
        self.assertEqual(tex.count(' & '), 2)

    def test_quick_reference_is_in_the_book_before_the_problems(self):
        content.build()
        tex = (ROOT / 'calculus_workbook.tex').read_text()
        start = tex.index(r'\label{quick-reference:start}')
        end = tex.index(r'\label{quick-reference:end}')
        self.assertLess(start, end)
        self.assertLess(end, tex.index(r'\label{problem:D4-001}'))
        standalone = (ROOT / 'calculus_quick_reference.tex').read_text()
        body = standalone.split(r'\begin{document}', 1)[1].split(r'\end{document}', 1)[0]
        self.assertIn(body, tex[start:end])
        self.assertIn(r'\addcontentsline{toc}{chapter}{Calculus quick reference}', tex)

    def test_wrapped_list_items_remain_single_paragraphs(self):
        tex = content.markdown_to_tex('# Test\n\n- A long item\n  continues here.\n- Another item.\n')
        self.assertEqual(tex.count(r'\begin{itemize}'), 1)
        self.assertIn(r'\item A long item continues here.', tex)

    def test_math_in_bold_table_headers_is_preserved(self):
        tex = content.markdown_to_tex('# Test\n\n| Derivative in $x$ | Value |\n|---|---|\n| $x$ | $1$ |\n')
        self.assertIn(r'\textbf{Derivative in \(x\)}', tex)
        self.assertNotIn('**', tex)

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

    def test_method_and_domain_blocks_end_before_the_next_operation(self):
        sample = '# Example\n\n**Step 1 — CHOICE.** Method selection.\n\n**Step 2 — CALCULUS.** An operation.\n\n**Step 3 — CHECK AND DOMAIN.** Domain verification.\n\n**Recognition cue.** Conditions.\n'
        html = content.style_algebra(sample)
        self.assertIn('class="choice-step"', html)
        self.assertIn('class="domain-step"', html)
        self.assertEqual(html.count('</div>'), 2)
        tex = content.markdown_to_tex(sample)
        self.assertEqual(tex.count(r'\begin{ChoiceStep}'), 1)
        self.assertEqual(tex.count(r'\end{ChoiceStep}'), 1)
        self.assertEqual(tex.count(r'\begin{DomainStep}'), 1)
        self.assertEqual(tex.count(r'\end{DomainStep}'), 1)
        self.assertLess(tex.index(r'\end{ChoiceStep}'), tex.index('Step 2'))
        self.assertLess(tex.index(r'\end{DomainStep}'), tex.index('Recognition cue'))

    def test_editorial_outline_is_not_published(self):
        content.build()
        self.assertNotIn('curriculum', (ROOT / 'site/generated/book.md').read_text().lower())
        self.assertNotIn('curriculum', (ROOT / 'calculus_workbook.tex').read_text().lower())
        self.assertFalse((ROOT / 'site/generated/curriculum.md').exists())
        self.assertFalse((ROOT / 'site/public/downloads/CURRICULUM.md').exists())


if __name__ == '__main__':
    unittest.main()
