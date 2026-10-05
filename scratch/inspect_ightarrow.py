import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any \r\n with \n
text = text.replace('\r\n', '\n').replace('\r', '\n')

# Check where ightarrow appears
lines = text.split('\n')
for idx, line in enumerate(lines):
    if 'ightarrow' in line:
        print(f"L{idx+1}: {line}")
