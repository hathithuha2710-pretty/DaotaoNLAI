import sys, io, re
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"

with pdfplumber.open(pdf_path) as pdf:
    # Page 14 is index 13 (Lớp 1)
    p = pdf.pages[13]
    tables = p.extract_tables()
    for row in tables[0]:
        print([c.replace('\n', ' ') if c else '' for c in row])
