import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_QD2422.md', 'r', encoding='utf-8') as f:
    text = f.read()

part2 = text.split('## PHẦN III')[1].split('## PHẦN IV')[0]
full2 = part2.split('### 2. Kế hoạch Giáo dục Toàn diện')[1]

# Normalize ightarrow
full2 = re.sub(r'\s*\$\s*[\r\n]+\s*ightarrow\$\s*', ' -> ', full2)

for l in full2.split('\n'):
    m = re.match(r'\|\s*\*\*(\d+)\*\*', l)
    if m:
        tiet = m.group(1)
        mr_matches = re.findall(r'\b2\.[A-D][1-5]\.MR\d+\b', l)
        core_matches = re.findall(r'\b2\.[A-D][1-5]\.\d+\b', l)
        print(f"Tiết {tiet}: Core={core_matches}, MR={mr_matches}")
