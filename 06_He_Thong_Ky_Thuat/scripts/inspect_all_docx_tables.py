import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import docx

docx_path = r"06_He_Thong_Ky_Thuat\extracted_data\Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.docx"
doc = docx.Document(docx_path)

for i, table in enumerate(doc.tables):
    first_row = [c.text.strip().replace('\n', ' ')[:30] for c in table.rows[0].cells]
    # check for unique cells in first row
    seen = []
    for c in first_row:
        if not seen or c != seen[-1]:
            seen.append(c)
    print(f"Table {i+1}: {len(table.rows)} rows x {len(table.columns)} cols | Header: {seen}")
