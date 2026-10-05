import sys, io, re
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"

# Grade definitions with page ranges and table index logic
grades_info = [
    ("LỚP 1", 14, 16),
    ("LỚP 2", 16, 18),
    ("LỚP 3", 18, 21),
    ("LỚP 4", 21, 23),
    ("LỚP 5", 23, 26),
    ("LỚP 6", 26, 29),
    ("LỚP 7", 29, 31), # ends on p31
    ("LỚP 8", 32, 34), # starts on p32
    ("LỚP 9", 34, 37),
    ("LỚP 10", 37, 39),
    ("LỚP 11", 39, 41),
    ("LỚP 12", 41, 43),
]

with pdfplumber.open(pdf_path) as pdf:
    for g_name, start_p, end_p in grades_info:
        g_num = g_name.split()[1]
        all_rows = []
        for p_idx in range(start_p - 1, end_p):
            p = pdf.pages[p_idx]
            tables = p.extract_tables()
            for t_idx, table in enumerate(tables):
                # determine if this table belongs to this grade
                # On start page: if there are 2 tables and start_p > 14 and p_idx == start_p - 1, it's table 1!
                if p_idx == start_p - 1 and len(tables) > 1 and start_p > 14:
                    if t_idx == 0:
                        continue # belongs to previous grade
                # On end page: if there are 2 tables and p_idx == end_p - 1 and end_p != 31 and end_p != 43:
                if p_idx == end_p - 1 and len(tables) > 1 and end_p != 31 and end_p != 43:
                    if t_idx > 0:
                        continue # belongs to next grade
                
                for row in table:
                    # check if row is header row
                    clean_row = [c.strip().replace('\n', ' ') if c else '' for c in row]
                    if clean_row == ['Chủ đề', 'Nội dung', 'Yêu cầu cần đạt']:
                        continue
                    if not any(clean_row):
                        continue
                    all_rows.append(clean_row)
        
        # count codes
        codes = []
        for row in all_rows:
            y_cell = row[2] if len(row) > 2 else ''
            found = re.findall(rf'\b{g_num}\.[A-D]\d*(?:\.MR\d+|\.\d+)?\b', y_cell)
            codes.extend(found)
        print(f"{g_name}: {len(all_rows)} rows, {len(codes)} YCCD codes ({len(set(codes))} unique)")
