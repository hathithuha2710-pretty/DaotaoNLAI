import sys, io, re
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for page_idx in range(13, 43):
        p = pdf.pages[page_idx]
        text = p.extract_text() or ''
        
        m = re.findall(r'(LỚP\s+\d+)', text)
        tables = p.extract_tables()
        print(f"Page {page_idx+1}: detected headings={m}, tables={len(tables)}")
        for t_idx, table in enumerate(tables):
            yccd_count = 0
            for row in table:
                cell_text = " ".join([c for c in row if c])
                matches = re.findall(r'\b\d+\.[A-D]\d*(?:\.MR\d+|\.\d+)?\b', cell_text)
                yccd_count += len(matches)
            print(f"   Table {t_idx}: {len(table)} rows, {yccd_count} YCCD codes found")
