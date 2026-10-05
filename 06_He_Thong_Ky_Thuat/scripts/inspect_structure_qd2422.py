import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"
doc = pymupdf.open(pdf_path)
for i, page in enumerate(doc):
    text = page.get_text()
    for line in text.split('\n'):
        line_s = line.strip()
        if any(line_s.startswith(p) for p in ['I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'Phụ lục', 'PHỤ LỤC', 'LỚP ', 'BẢNG ']) or 'YÊU CẦU CẦN ĐẠT' in line_s or 'CẤP ' in line_s:
            print(f"P.{i+1}: {line_s[:100]}")
doc.close()
