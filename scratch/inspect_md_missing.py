import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect Lớp 1 table 2 (36 lessons) around lesson 14, 15, 16, 17
lines = text.split('\n')
for i, line in enumerate(lines):
    if 'LỚP 1' in line:
        print(f"Lớp 1 at line {i}")
    if '| **14** |' in line or '| **15** |' in line or '| **16** |' in line or '| **17** |' in line:
        print(f"Line {i}: {line[:70]}")
    if '| **3** |' in line and 'LỚP 2' in lines[max(0, i-50):i]:
        pass
