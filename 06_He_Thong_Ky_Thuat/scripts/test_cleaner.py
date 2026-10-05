import sys, io, re
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"

def clean_cell_text(text):
    if not text:
        return ""
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if not lines:
        return ""
    
    # Reassemble wrapped lines
    items = []
    curr = []
    for l in lines:
        if l.startswith(('-', '•', '+')):
            if curr:
                items.append(" ".join(curr))
            curr = [l]
        else:
            if curr:
                curr.append(l)
            else:
                curr = [l]
    if curr:
        items.append(" ".join(curr))
        
    return "<br>".join(items).replace('|', '\\|')

with pdfplumber.open(pdf_path) as pdf:
    # Page 11 is index 10
    t = pdf.pages[10].extract_tables()[0]
    print("Header:", [clean_cell_text(c) for c in t[0]])
    print("\nRow 1 (Strand A):")
    row1 = [clean_cell_text(c) for c in t[1]]
    for col_idx, col in enumerate(row1):
        print(f"Col {col_idx}:")
        print(col)
