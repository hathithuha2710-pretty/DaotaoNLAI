import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"

with pdfplumber.open(pdf_path) as pdf:
    # Check page 10-13 (Overview table)
    for p_idx in [9, 10, 11, 12]:
        p = pdf.pages[p_idx]
        tables = p.extract_tables()
        print(f"P.{p_idx+1}: {len(tables)} tables, text chars: {len(p.extract_text() or '')}")
        if tables:
            for t in tables:
                print("  Sample row:", [c.replace('\n', ' ')[:30] if c else '' for c in t[0]])
                if len(t) > 1:
                    print("  Row 1:", [c.replace('\n', ' ')[:30] if c else '' for c in t[1]])

    # Check page 48-50 (Glossary)
    for p_idx in [47, 48, 49, 50]:
        p = pdf.pages[p_idx]
        tables = p.extract_tables()
        print(f"Glossary P.{p_idx+1}: {len(tables)} tables, text chars: {len(p.extract_text() or '')}")
        if tables:
            for t in tables:
                print("  Sample row:", [c.replace('\n', ' ')[:30] if c else '' for c in t[0]])
                if len(t) > 1:
                    print("  Row 1:", [c.replace('\n', ' ')[:30] if c else '' for c in t[1]])
