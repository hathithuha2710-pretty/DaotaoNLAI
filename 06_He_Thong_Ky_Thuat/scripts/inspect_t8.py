import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import docx

docx_path = r"06_He_Thong_Ky_Thuat\extracted_data\Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.docx"
doc = docx.Document(docx_path)

# Let's inspect Table 8 (Lớp 3)
t8 = doc.tables[7]
print(f"Table 8 has {len(t8.rows)} rows and {len(t8.columns)} columns")
for r_idx, row in enumerate(t8.rows[:10]):
    row_vals = [c.text.strip().replace('\n', ' ')[:40] for c in row.cells]
    print(f"  Row {r_idx}: {row_vals}")
