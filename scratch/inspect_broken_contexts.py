import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'ightarrow' in line:
        print(f"--- Line {i+1} ---")
        for j in range(max(0, i-2), min(len(lines), i+3)):
            print(f"{j+1}: {lines[j].rstrip()}")
