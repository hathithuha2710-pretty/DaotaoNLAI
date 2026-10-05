import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for p_idx in [47, 48, 49, 50]: # Pages 48, 49, 50, 51
        p = pdf.pages[p_idx]
        print(f"=== Page {p_idx+1} ===")
        tables = p.extract_tables()
        print(f"Tables: {len(tables)}")
        for t in tables:
            print(f"  Rows: {len(t)}")
            for row in t[:4]:
                print("   ", [c.replace('\n', ' ')[:40] if c else '' for c in row])
