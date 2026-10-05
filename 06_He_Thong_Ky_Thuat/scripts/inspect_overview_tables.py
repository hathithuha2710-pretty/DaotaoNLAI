import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for p_idx in [9, 10, 11, 12]:
        p = pdf.pages[p_idx]
        print(f"=== P.{p_idx+1} ===")
        tables = p.extract_tables()
        for t_idx, t in enumerate(tables):
            print(f"Table {t_idx}: {len(t)} rows x {len(t[0]) if t else 0} cols")
            for r in t[:3]:
                print(" ", [c.strip().replace('\n', ' ')[:30] if c else '' for c in r])
