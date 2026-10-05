import sys, io
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"

terms = []
with pdfplumber.open(pdf_path) as pdf:
    for p_idx in [48, 49, 50]: # Pages 49, 50, 51
        tables = pdf.pages[p_idx].extract_tables()
        for t in tables:
            for row in t:
                # filter out None and empty
                non_empty = [c.strip().replace('\n', ' ') for c in row if c and c.strip()]
                if len(non_empty) >= 2:
                    t_name, t_def = non_empty[0], non_empty[1]
                    if t_name not in ['Thuật ngữ', '']:
                        terms.append((t_name, t_def))
                elif len(non_empty) == 1 and terms:
                    # continuation of previous definition
                    prev_name, prev_def = terms[-1]
                    terms[-1] = (prev_name, prev_def + " " + non_empty[0])

print(f"Total terms found: {len(terms)}")
for i, (name, d) in enumerate(terms):
    print(f"{i+1}. {name}: {d[:60]}...")
