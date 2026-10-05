import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_QD2422.md', 'r', encoding='utf-8') as f:
    text = f.read()

part2 = text.split('## PHẦN III')[1].split('## PHẦN IV')[0]
full2 = part2.split('### 2. Kế hoạch Giáo dục Toàn diện')[1]

for l in full2.split('\n'):
    if re.match(r'\|\s*\*\*\d+\*\*', l):
        cols = [c.strip() for c in l.split('|')]
        tiet = cols[1].replace('**', '')
        ten = cols[2].replace('**', '')
        code = cols[6].replace('**', '')
        if 'MR' in code:
            print(f"Tiết {tiet}: {ten} -> {code}")
