import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md', 'r', encoding='utf-8') as f:
    text = f.read()

roman_map = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V'}
official_core = {}
official_mr = {}

for g in range(1, 6):
    r = roman_map[g]
    part = text.split(f'## PHẦN {r}: LỚP {g}')[1]
    if g < 5:
        next_r = roman_map[g+1]
        part = part.split(f'## PHẦN {next_r}: LỚP {g+1}')[0]
    
    # Extract codes from table or text: format like **1.A1.1** or `1.A1.1`
    codes = sorted(list(set(re.findall(rf'\b{g}\.[A-D][1-5]\.(?:MR\d+|\d+)\b', part))))
    core = [c for c in codes if 'MR' not in c]
    mr = [c for c in codes if 'MR' in c]
    official_core[g] = core
    official_mr[g] = mr
    print(f"LỚP {g}: Tổng {len(codes)} ({len(core)} Cốt lõi, {len(mr)} Mở rộng)")
    print(f"  Core ({len(core)}): {core}")
    print(f"  MR   ({len(mr)}): {mr}")
