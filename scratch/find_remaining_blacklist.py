import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

new_matrix_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(new_matrix_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    for kw in ['model card', 'foundations of ai', 'pháp lý']:
        if kw in line.lower():
            print(f"Line {idx+1} contains '{kw}':")
            print(f"  {line.strip()[:160]}")
            print("-" * 50)
