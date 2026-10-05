import sys, io, re
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for page_idx in range(13, 43):
        p = pdf.pages[page_idx]
        text = p.extract_text() or ''
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        grade_matches = [l for l in lines if re.match(r'^LỚP\s+\d+$', l)]
        print(f"Page {page_idx+1}: {grade_matches}")
