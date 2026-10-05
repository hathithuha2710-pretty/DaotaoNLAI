import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"
doc = pymupdf.open(pdf_path)
print(f"Total pages: {len(doc)}")
for i in range(min(5, len(doc))):
    text = doc[i].get_text()
    print(f"--- Page {i+1} (chars: {len(text)}) ---")
    print(text[:300].replace('\n', ' '))
doc.close()
