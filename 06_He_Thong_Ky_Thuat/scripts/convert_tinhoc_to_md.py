import sys, io, re
sys.stdout.reconfigure(encoding='utf-8')
import docx
from docx.text.paragraph import Paragraph
from docx.table import Table

docx_path = r"06_He_Thong_Ky_Thuat\extracted_data\Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.docx"
out_md_path = r"04_Hoc_Lieu_Va_Tham_Khao\SGK Tin học\Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.md"
out_md_legal = r"01_Van_Ban_Phap_Ly\Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.md"

doc = docx.Document(docx_path)

def clean_cell_text(text):
    if not text:
        return ""
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if not lines:
        return ""
    
    items = []
    curr = []
    for l in lines:
        if l.startswith(('-', '•', '+', '*')) or re.match(r'^\d+[\.\)]\s+', l):
            if curr:
                items.append(" ".join(curr))
            curr = [l]
        else:
            if curr:
                curr.append(l)
            else:
                curr = [l]
    if curr:
        items.append(" ".join(curr))
        
    return "<br>".join(items).replace('|', '\\|')

def table_to_markdown(table):
    md_lines = []
    rows_data = []
    max_cols = 0
    for row in table.rows:
        row_cells = [clean_cell_text(cell.text) for cell in row.cells]
        max_cols = max(max_cols, len(row_cells))
        rows_data.append(row_cells)
    
    if not rows_data or max_cols == 0:
        return ""
    
    header = rows_data[0]
    while len(header) < max_cols:
        header.append("")
    
    md_lines.append("| " + " | ".join(header) + " |")
    md_lines.append("| " + " | ".join(["---"] * len(header)) + " |")
    
    for row in rows_data[1:]:
        while len(row) < len(header):
            row.append("")
        row = row[:len(header)]
        if len(set(row)) == 1 and row[0] != "":
            val = f"**{row[0]}**"
            row = [val] * len(row)
        md_lines.append("| " + " | ".join(row) + " |")
    
    return "\n" + "\n".join(md_lines) + "\n"

body = doc.element.body
output_blocks = []

for child in body:
    if child.tag.endswith('p'):
        p = Paragraph(child, doc)
        text = p.text.strip()
        if not text:
            continue
        
        is_bold = any(r.bold for r in p.runs if r.text.strip())
        
        if text.startswith(('I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.')):
            output_blocks.append(f"\n## {text}\n")
        elif text.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')) and is_bold and len(text) < 120:
            output_blocks.append(f"\n### {text}\n")
        elif text.startswith(('a)', 'b)', 'c)', 'd)', 'e)', 'g)', 'h)')) and is_bold and len(text) < 120:
            output_blocks.append(f"\n#### {text}\n")
        elif text in ['LỚP 3', 'LỚP 4', 'LỚP 5', 'LỚP 6', 'LỚP 7', 'LỚP 8', 'LỚP 9', 'LỚP 10', 'LỚP 11', 'LỚP 12']:
            output_blocks.append(f"\n### {text}\n")
        elif text.startswith('CHƯƠNG TRÌNH GIÁO DỤC PHỔ THÔNG'):
            output_blocks.append(f"# {text}")
        elif text == 'MÔN TIN HỌC':
            output_blocks.append(f"# {text}\n")
        elif text.startswith('(Ban hành kèm theo'):
            output_blocks.append(f"*{text}*\n\n---")
        elif text == 'MỤC LỤC':
            output_blocks.append(f"\n## {text}\n")
        else:
            if text.startswith(('-', '+', '•', '* ')):
                output_blocks.append(f"- {text.lstrip('-+•* ')}")
            else:
                if is_bold and len(text) < 100:
                    output_blocks.append(f"\n**{text}**\n")
                else:
                    output_blocks.append(f"{text}\n")
    elif child.tag.endswith('tbl'):
        t = Table(child, doc)
        tbl_md = table_to_markdown(t)
        if tbl_md:
            output_blocks.append(tbl_md)

final_md = "\n".join(output_blocks)
final_md = re.sub(r'\n{3,}', '\n\n', final_md)

with open(out_md_path, 'w', encoding='utf-8') as f:
    f.write(final_md)

with open(out_md_legal, 'w', encoding='utf-8') as f:
    f.write(final_md)

print(f"Updated {out_md_path} and {out_md_legal} cleanly!")
