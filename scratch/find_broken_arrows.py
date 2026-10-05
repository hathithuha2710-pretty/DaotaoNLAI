import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer('ightarrow', text)]
print(f"Found {len(matches)} occurrences of 'ightarrow'!")

lines = text.split('\n')
for idx, line in enumerate(lines):
    if 'ightarrow' in line:
        print(f"Line {idx+1}: {line[:60]}")
