#!/usr/bin/env python3
"""Check printable margins, four reference pages, and notation page boundaries."""
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

NS = '{http://www.w3.org/1999/xhtml}'


def pages(path):
    xml = subprocess.check_output(['pdftotext', '-bbox', str(path), '-'], text=True)
    # Some TeX font glyphs extract as XML-forbidden control characters.
    xml = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', xml)
    return list(ET.fromstring(xml).iter(NS + 'page'))


def check(book, sheet):
    book_pages, sheet_pages = pages(book), pages(sheet)
    if len(sheet_pages) != 4:
        raise ValueError(f'Quick reference has {len(sheet_pages)} pages; expected four')
    text_pages = subprocess.check_output(['pdftotext', '-layout', str(book), '-'], text=True).split('\f')
    embedded = [i for i, p in enumerate(text_pages) if re.match(r'Calculus quick reference\s+\d+', p.strip())]
    if len(embedded) != 4 or embedded != list(range(embedded[0], embedded[0]+4)):
        raise ValueError('The main book must contain four consecutive quick-reference pages')
    for path, pdf_pages, margin in [(book, book_pages, 66), (sheet, sheet_pages, 29)]:
        for number, page in enumerate(pdf_pages, 1):
            width, height = float(page.attrib['width']), float(page.attrib['height'])
            for word in page.iter(NS + 'word'):
                x1, y1, x2, y2 = (float(word.attrib[k]) for k in ('xMin', 'yMin', 'xMax', 'yMax'))
                page_margin = 29 if path == book and number-1 in embedded else margin
                if x1 < page_margin or x2 > width-page_margin or y1 < 15 or y2 > height-15:
                    raise ValueError(f'{path}, page {number}: text outside printable margins: {word.text!r}')
    # These pairs span the concepts most vulnerable to table/formula separation.
    for first, last in [
        ('Delimiters\n', 'Object type is'),
        ('Object typography\n', 'separate from the bracketed'),
        ('One independent scalar variable', 'constant value'),
        ('Several independent scalar variables', 'appropriate hypotheses'),
        ('Vector and matrix outputs', 'denotes transpose'),
        ('Matrix and tensor inputs', 'variation of the basis'),
        ('5. Change-of-variable notation\n', 'derivative is nonzero'),
        ('7. Labels and color conventions\n', 'stages of the calculation'),
    ]:
        matching = [p for p in text_pages if re.search(r'^' + re.escape(first.strip()) + r'\s*$', p, flags=re.M)]
        if len(matching) != 1 or last not in re.sub(r'\s+', ' ', matching[0]):
            raise ValueError(f'Notation concept split or missing: {first.strip()}')
    print(f'PDF layout: {len(book_pages)} book pages; four standalone and four embedded reference pages; margins and notation groups pass.')


if __name__ == '__main__':
    check(*(Path(p) for p in (sys.argv[1:] or ['build/calculus_workbook.pdf', 'build/calculus_quick_reference.pdf'])))
