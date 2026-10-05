import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"
doc = pymupdf.open(pdf_path)

with open(r"06_He_Thong_Ky_Thuat\extracted_data\qd2422_text_p1_9.txt", "w", encoding="utf-8") as f:
    for i in range(9):
        f.write(f"\n=== PAGE {i+1} ===\n")
        f.write(doc[i].get_text())

with open(r"06_He_Thong_Ky_Thuat\extracted_data\qd2422_text_p44_51.txt", "w", encoding="utf-8") as f:
    for i in range(43, len(doc)):
        f.write(f"\n=== PAGE {i+1} ===\n")
        f.write(doc[i].get_text())

print("Dumped text for p1-9 and p44-51")
