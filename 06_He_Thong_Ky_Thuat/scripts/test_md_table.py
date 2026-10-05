import sys, io, re
sys.stdout.reconfigure(encoding='utf-8')
import docx
from docx.text.paragraph import Paragraph
from docx.table import Table

docx_path = r"06_He_Thong_Ky_Thuat\extracted_data\Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.docx"
doc = docx.Document(docx_path)

def clean_cell_text(text):
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    cleaned = "<br>".join(lines)
    cleaned = cleaned.replace('|', '\\|')
    return cleaned

def table_to_markdown(table):
    md_lines = []
    # Get max cols
    num_cols = max(len(row.cells) for row in table.rows)
    if num_cols == 0:
        return ""
    
    # Process rows
    rows_data = []
    for row in table.rows:
        row_cells = [clean_cell_text(cell.text) for cell in row.cells]
        rows_data.append(row_cells)
    
    if not rows_data:
        return ""
    
    # Header row
    header = rows_data[0]
    md_lines.append("| " + " | ".join(header) + " |")
    md_lines.append("| " + " | ".join(["---"] * len(header)) + " |")
    
    for row in rows_data[1:]:
        # ensure matching column count
        while len(row) < len(header):
            row.append("")
        row = row[:len(header)]
        md_lines.append("| " + " | ".join(row) + " |")
    
    return "\n".join(md_lines)

# Test first 2 tables
table_count = 0
for child in doc.element.body:
    if child.tag.endswith('tbl'):
        t = Table(child, doc)
        table_count += 1
        print(f"\n--- TABLE {table_count} ({len(t.rows)} rows x {len(t.columns)} cols) ---")
        md = table_to_markdown(t)
        print(md[:500])
        if table_count >= 2:
            break
