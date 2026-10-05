import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"
with pdfplumber.open(pdf_path) as pdf:
    print(f"Total pages: {len(pdf.pages)}")
    for i in range(13, 20): # Grade 1, 2, 3 pages
        tables = pdf.pages[i].extract_tables()
        print(f"Page {i+1}: found {len(tables)} tables")
        if tables:
            for t in tables:
                print(f"  Table rows: {len(t)}, cols: {len(t[0]) if t else 0}")
                for row in t[:3]:
                    clean_row = [c.replace('\n', ' ')[:40] if c else '' for c in row]
                    print("    ", clean_row)
