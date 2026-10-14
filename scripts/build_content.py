#!/usr/bin/env python3
"""Generate the reading site and standalone LaTeX from the root manuscript."""
from pathlib import Path
import re
import shutil
import json

ROOT = Path(__file__).resolve().parents[1]
INTRO_SOURCES = (("NOTATION_STANDARD.md", "notation", "Notational conventions"),
                 ("METHODS_REFERENCE.md", "methods", "Calculus methods reference"))
MAIN_SETS = (("DIFFERENTIATION_MIXED.md", "nonlinear-scalars", "D4", "Nonlinear scalar and parameter problems"),
             ("DIFFERENTIATION_FIELDS.md", "fields-and-geometry", "D3", "Fields and geometric constraints"),
             ("INTEGRATION_MIXED.md", "parameter-integrals", "I4", "Parameter integrals and geometric accumulation"),
             ("INTEGRATION_DOMAINS.md", "oscillation-and-domains", "I3", "Oscillatory and singular integrals"))
REFERENCE_SETS = (("DIFFERENTIATION_SCALARS.md", "scalar-derivatives", "D1", "Scalar reference exercises"),
                  ("DIFFERENTIATION_RULES.md", "derivative-rules", "D2", "Composition reference exercises"),
                  ("INTEGRATION_SCALARS.md", "scalar-integrals", "I1", "Antiderivative reference exercises"),
                  ("INTEGRATION_SUBSTITUTION.md", "substitution", "I2", "Coordinate reference exercises"))
SOURCES = {"INTRODUCTION.md": "introduction"}
SOURCES.update({name: slug for name, slug, _ in INTRO_SOURCES})
SOURCES.update({name: slug for name, slug, _, _ in MAIN_SETS})
SOURCES["TRICKS_APPENDIX.md"] = "tricks"
SOURCES.update({name: slug for name, slug, _, _ in REFERENCE_SETS})
SOURCES["NOTATION_REVIEW.md"] = "references"
PROBLEM_SOURCES = tuple(item[0] for item in MAIN_SETS + REFERENCE_SETS)
CHAPTER_TITLES = {code: title for _, _, code, title in MAIN_SETS + REFERENCE_SETS}
CHAPTER_SLUGS = {code: slug for _, slug, code, _ in MAIN_SETS + REFERENCE_SETS}
REFERENCE_CODES = {item[2] for item in REFERENCE_SETS}


def problem_sections(text):
    """Require matching unique prompt, hint, and solution IDs; fail on lost content."""
    sections = re.split(r"^## (Problems|Hint ladders|Complete solutions)\s*$", text, flags=re.M)
    if len(sections) != 7:
        raise ValueError("Expected exactly Problems, Hint ladders, and Complete solutions sections")
    result = {}
    for index in (1, 3, 5):
        name, body = sections[index:index + 2]
        chunks = re.split(r"^### ([DI]\d+-\d{3})([^\n]*)\n", body, flags=re.M)
        items = {}
        for j in range(1, len(chunks), 3):
            identifier, title, content = chunks[j:j + 3]
            if identifier in items:
                raise ValueError(f"Duplicate {identifier} in {name}")
            # Do not attach the tutor entry point and editorial notes to the last solution.
            content = re.split(r"^## ", content, maxsplit=1, flags=re.M)[0].strip()
            items[identifier] = (title.strip(" —"), content)
        result[name] = items
    ids = set(result["Problems"])
    if not ids or any(set(items) != ids for items in result.values()):
        raise ValueError("Every problem needs a matching hint ladder and complete solution")
    return result


def step_style(text):
    label = re.match(r"\*\*Step \d+ — ([^:*]+)", text)
    if not label:
        return None
    words = label[1]
    if words.startswith('TRICK'):
        return 'trick-step'
    if words.startswith(('ALGEBRA', 'IDENTITY', 'APPROXIMATION')):
        return 'algebra-step'
    if 'DOMAIN' in words:
        return 'domain-step'
    if words.startswith('CHOICE'):
        return 'choice-step'
    return None


def style_algebra(text):
    chunks = re.split(r"(?=^\*\*(?:Step \d+|Result\.|(?:Recognition cue|Discussion)\.))", text, flags=re.M)
    styled = []
    for chunk in chunks:
        css_class = step_style(chunk)
        if css_class:
            chunk = f'<div class="{css_class}">\n\n' + chunk.strip() + '\n\n</div>\n'
        styled.append(chunk)
    return "\n".join(styled)


def site_links(text):
    for filename, slug in SOURCES.items():
        text = text.replace(f"]({filename})", f"](/generated/{slug})")
        text = text.replace(f"]({filename}#", f"](/generated/{slug}#")
    return text


def collect_problems(content):
    combined = {name: {} for name in ("Problems", "Hint ladders", "Complete solutions")}
    for filename in PROBLEM_SOURCES:
        groups = problem_sections(content[filename])
        for name, items in groups.items():
            duplicates = combined[name].keys() & items.keys()
            if duplicates:
                raise ValueError(f"Problem IDs occur in multiple manuscripts: {sorted(duplicates)}")
            combined[name].update(items)
    return combined


def tex_escape(text):
    return re.sub(r"[&%$#_{}~^]", lambda m: {
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"
    }.get(m.group(), "\\" + m.group()), text).replace("©", r"\copyright{}")


def tex_inline(text):
    chunks = re.split(r"(\$[^$\n]+\$|\[[^\]]+\]\([^)]+\))", text)
    result = []
    for chunk in chunks:
        if chunk.startswith("$") and chunk.endswith("$"):
            result.append(r"\(" + chunk[1:-1] + r"\)")
            continue
        link = re.fullmatch(r"\[([^\]]+)\]\(([^)]+)\)", chunk)
        if link:
            label, target = link.groups()
            result.append(r"\href{" + target + "}{" + tex_escape(label) + "}" if target.startswith("https://") else tex_escape(label))
            continue
        chunk = tex_escape(chunk)
        chunk = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", chunk)
        chunk = re.sub(r"`(.*?)`", r"\\texttt{\1}", chunk)
        result.append(chunk.replace("–", "--").replace("—", "---"))
    return "".join(result)


def markdown_to_tex(text, algebra_color='AlgebraBlue'):
    lines = text.splitlines()[1:]
    output, index, in_math, list_kind, colored = [], 0, False, None, False
    box = None

    def end_list():
        nonlocal list_kind
        if list_kind:
            output.append(r"\end{" + list_kind + "}")
            list_kind = None

    def end_color():
        nonlocal colored, box
        if box:
            output.append(r"\end{" + box + "}")
            box = None
        if colored:
            output.append(r"\endgroup")
            colored = False

    while index < len(lines):
        line = lines[index]
        index += 1
        if line.strip() == "$$":
            end_list()
            output.append(r"\]" if in_math else r"\[")
            in_math = not in_math
            continue
        if in_math:
            output.append(line)
            continue
        if line.startswith("|"):
            end_list()
            rows = [line]
            while index < len(lines) and lines[index].startswith("|"):
                rows.append(lines[index]); index += 1
            cells = []
            for row in rows:
                row = re.sub(r"\$[^$]+\$", lambda m: m.group().replace("|", "PIPEPLACEHOLDER"), row)
                cell = [x.strip().replace("PIPEPLACEHOLDER", "|") for x in row.strip("|").split("|")]
                if not all(re.fullmatch(r"[-: ]+", x) for x in cell):
                    cells.append(cell)
            count = len(cells[0])
            if any(len(row) != count for row in cells):
                raise ValueError("Malformed Markdown table")
            width = .90 / count
            output.append(r"\begin{longtable}{@{}" + (r">{\raggedright\arraybackslash}p{" + f"{width:.3f}" + r"\textwidth}") * count + r"@{}}")
            for n, row in enumerate(cells):
                output.append(" & ".join(tex_inline(x) for x in row) + r" \\[5pt]")
                if n == 0:
                    output.append(r"\hline\endhead")
            output.append(r"\end{longtable}")
            continue
        heading = re.match(r"^(#{2,4}) (.*)", line)
        if heading:
            end_list(); end_color()
            level, title = heading.groups()
            if title == "Complete solutions":
                output.append(r"\clearpage")
            output.append("\\" + {2: "section", 3: "subsection", 4: "subsubsection"}[len(level)] + "{" + tex_inline(title) + "}")
            continue
        if re.match(r"\*\*(?:Step \d+|Result\.|(?:Recognition cue|Discussion)\.)", line):
            end_list(); end_color()
            kind = re.match(r"\*\*Step \d+ — (ALGEBRA|IDENTITY|APPROXIMATION|TRICK)", line)
            if kind:
                color = 'TrickPurple' if kind[1] == 'TRICK' else algebra_color
                output.append(r"\begingroup\color{" + color + "}")
                colored = True
            elif algebra_color != 'TrickPurple':
                style = step_style(line)
                if style in ('domain-step', 'choice-step'):
                    box = 'DomainStep' if style == 'domain-step' else 'ChoiceStep'
                    output.append(r"\begin{" + box + "}")
        item = re.match(r"^(- |\d+\. )(.*)", line)
        if item:
            kind = "itemize" if item[1] == "- " else "enumerate"
            if list_kind != kind:
                end_list(); output.append(r"\begin{" + kind + "}"); list_kind = kind
            output.append(r"\item " + tex_inline(item[2]))
            continue
        if line.strip():
            end_list()
        output.append(tex_inline(line))
    end_list(); end_color()
    if in_math:
        raise ValueError("Unclosed display math")
    return "\n".join(output)


def worked_chapter_to_tex(text):
    """Keep each statement and its solution together in the printed edition."""
    groups = problem_sections(text)
    output = []
    for number, (identifier, (title, prompt)) in enumerate(groups['Problems'].items()):
        if number:
            output.append(r'\clearpage')
        output.extend([
            r'\section{' + tex_inline(identifier + ' — ' + title) + '}',
            r'\label{problem:' + identifier + '}',
            r'\markright{' + identifier + '}',
            r'{\small Hints: page~\pageref{hints:' + identifier + r'}.}\par\medskip',
            markdown_to_tex('# Statement\n\n' + prompt),
            r'\subsection*{Worked solution}',
            markdown_to_tex('# Solution\n\n' + groups['Complete solutions'][identifier][1]),
        ])
    # Chapter bibliographies belong after the calculations, not inside the last solution.
    references = re.search(r'^## Application references\s*\n(.*)', text, flags=re.M | re.S)
    if references:
        output.append(markdown_to_tex('# References\n\n## Application references\n\n' + references[1]))
    return '\n'.join(output)


def hints_to_tex(problems):
    output = [r'\chapter{Hints}', r'\markright{}',
              'The hints provide progressively more of an approach. Each problem reference gives the page on which its statement and complete worked solution begin.']
    for identifier, (title, _) in problems['Problems'].items():
        output.extend([
            r'\subsection*{' + tex_inline(identifier + ' — ' + title) + '}',
            r'\label{hints:' + identifier + '}',
            r'Problem and worked solution: page~\pageref{problem:' + identifier + '}.',
            markdown_to_tex('# Hints\n\n' + problems['Hint ladders'][identifier][1]),
        ])
    return '\n'.join(output)


def build():
    content = {name: (ROOT / name).read_text() for name in SOURCES}
    problems = collect_problems(content)
    for directory in ("site/generated", "site/problems", "site/public/downloads", "site/public/licenses"):
        (ROOT / directory).mkdir(parents=True, exist_ok=True)
    for obsolete in ('site/generated/curriculum.md', 'site/generated/examples.md',
                     'site/public/downloads/CURRICULUM.md', 'site/public/downloads/PILOT_EXAMPLES.md'):
        (ROOT / obsolete).unlink(missing_ok=True)
    for name, slug in SOURCES.items():
        notice = '> **Alpha development.** Content is CC BY-SA 4.0, provided as-is without a guarantee of correctness.\n\n'
        if name == 'INTRODUCTION.md':
            notice = ''  # The site shell already displays the alpha notice.
        text = site_links(content[name])
        first, rest = text.split("\n", 1)
        styled = style_algebra(rest)
        if slug == 'tricks':
            styled = '<div class="tricks-appendix">\n\n' + styled + '\n\n</div>\n'
        (ROOT / "site/generated" / f"{slug}.md").write_text(first + "\n\n" + notice + styled)
        shutil.copyfile(ROOT / name, ROOT / "site/public/downloads" / name)
    index = []
    for identifier, (title, prompt) in problems["Problems"].items():
        hints = problems["Hint ladders"][identifier][1]
        hint_list = re.findall(r"^\d+\. (.*)$", hints, flags=re.M)
        if not hint_list:
            raise ValueError(f"No hints for {identifier}")
        solution = problems["Complete solutions"][identifier][1]
        chapter = identifier.split('-')[0]
        index.append({'id': identifier, 'title': title, 'chapter': chapter,
                      'chapterTitle': CHAPTER_TITLES[chapter], 'chapterLink': '/generated/' + CHAPTER_SLUGS[chapter], 'reference': chapter in REFERENCE_CODES, 'link': f'/problems/{identifier.lower()}'})
        page = f'# {identifier} — {title}\n\n<p class="problem-meta">{chapter} · Alpha development · Full solution and check · CC BY-SA 4.0</p>\n\n## Your problem\n\n{prompt}\n\n## Hints\n\n'
        for number, hint in enumerate(hint_list, 1):
            page += f'::: details Hint {number}\n\n{hint}\n\n:::\n\n'
        page += '## Complete solution\n\n<details class="solution"><summary>Open the complete worked solution</summary>\n\n' + style_algebra(solution) + '\n\n</details>\n\n'
        page += f'## Ask a tutor\n\n“Help me with {identifier}. I am stuck at step __. Use the notation standard, show all function inputs, and give me one next step at a time.”\n\n[Read the notation standard](/generated/notation) · [Choose another problem](/practice)\n'
        (ROOT / "site/problems" / f"{identifier.lower()}.md").write_text(site_links(page))
    (ROOT / 'site/generated/problem-index.json').write_text(json.dumps(index, indent=2) + '\n')
    for reference, target in ((False, 'practice-table.inc'), (True, 'reference-table.inc')):
        table = '| Problem | Set | Help available |\n|---|---|---|\n'
        for item in index:
            if item['reference'] == reference:
                table += f"| [{item['id']} — {item['title']}]({item['link']}) | {item['chapter']} | Three hints, full solution, and check |\n"
        (ROOT / 'site/generated' / target).write_text(table)
    for source, target in (("LICENSE", "MIT.txt"), ("LICENSES/CC-BY-SA-4.0.txt", "CC-BY-SA-4.0.txt")):
        shutil.copyfile(ROOT / source, ROOT / "site/public/licenses" / target)
    preamble = (ROOT / "scripts/book-preamble.tex").read_text()
    manuscript = preamble.replace("% WORKBOOK_INTRODUCTION", markdown_to_tex(content["INTRODUCTION.md"]))
    for filename, _, title in INTRO_SOURCES:
        manuscript += "\n\\chapter{" + title + "}\n" + markdown_to_tex(content[filename]) + "\n"
    for filename, _, _, title in MAIN_SETS:
        manuscript += "\n\\chapter{" + title + "}\n\\markright{}\n" + worked_chapter_to_tex(content[filename]) + "\n"
    manuscript += "\n\\appendix\n\\chapter{Tricks and identities}\n\\markright{}\n\\begingroup\\color{TrickPurple}\n"
    manuscript += markdown_to_tex(content["TRICKS_APPENDIX.md"], algebra_color='TrickPurple') + '\n\\endgroup\n'
    for filename, _, code, title in REFERENCE_SETS:
        manuscript += "\n\\chapter{" + code + ": " + title + "}\n\\markright{}\n" + worked_chapter_to_tex(content[filename]) + "\n"
    manuscript += "\n" + hints_to_tex(problems) + "\n"
    manuscript += "\n\\chapter{Literature review and notation decisions}\n\\markright{}\n" + markdown_to_tex(content["NOTATION_REVIEW.md"]) + "\n\\end{document}\n"
    (ROOT / "calculus_workbook.tex").write_text(manuscript)
    shutil.copyfile(ROOT / "calculus_workbook.tex", ROOT / "site/public/downloads/calculus_workbook.tex")
    combined = '# Calculus: A Worked Review\n\nCC BY-SA 4.0 · Provided as-is; correctness is not guaranteed.\n\n'
    combined += "\n\n---\n\n".join(content.values())
    (ROOT / "site/public/downloads/calculus-workbook.md").write_text(combined)
    book = '---\noutline: 2\n---\n\n# Calculus: A Worked Review\n\n'
    book += '> **Alpha development.** This is the current manuscript, including all solutions. Content is CC BY-SA 4.0 and provided as-is.\n\n'
    version = json.loads((ROOT / 'package.json').read_text())['version']
    book += f'[Download the alpha PDF](https://github.com/wa200508/Calculus_Workbook/releases/tag/v{version}) · [Practice with hidden solutions](/practice)\n\n'
    for filename, slug in SOURCES.items():
        chapter = re.sub(r'^(#{1,5}) ', r'\1# ', content[filename], flags=re.M)
        chapter = style_algebra(site_links(chapter))
        if slug == 'tricks':
            chapter = '<div class="tricks-appendix">\n\n' + chapter + '\n\n</div>\n'
        book += '\n\n' + chapter
    (ROOT / 'site/generated/book.md').write_text(book)
    print(f"Generated {len(SOURCES)} reading pages, {len(index)} practice pages, downloads, and LaTeX.")


if __name__ == "__main__":
    build()
