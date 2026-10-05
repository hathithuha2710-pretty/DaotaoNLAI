import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import docx
from docx.text.paragraph import Paragraph
from docx.table import Table

docx_path = r"06_He_Thong_Ky_Thuat\extracted_data\Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.docx"
doc = docx.Document(docx_path)

body = doc.element.body
elements = []
for child in body:
    if child.tag.endswith('p'):
        p = Paragraph(child, doc)
        elements.append(('p', p.text.strip()))
    elif child.tag.endswith('tbl'):
        t = Table(child, doc)
        elements.append(('tbl', len(t.rows), len(t.columns)))

print(f"Total elements in order: {len(elements)}")
for i, el in enumerate(elements[:40]):
    if el[0] == 'p':
        if el[1]:
            print(f"[{i}] P: {el[1][:80]}")
    else:
        print(f"[{i}] TABLE: {el[1]} rows x {el[2]} cols")
