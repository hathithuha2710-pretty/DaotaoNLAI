import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import docx

docx_path = r"06_He_Thong_Ky_Thuat\extracted_data\Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.docx"
doc = docx.Document(docx_path)

for i in range(40):
    p = doc.paragraphs[i]
    runs = p.runs
    is_bold = any(r.bold for r in runs)
    style = p.style.name if p.style else 'None'
    print(f"P{i:02d} [{style}] [bold={is_bold}]: {p.text.strip()[:70]}")
