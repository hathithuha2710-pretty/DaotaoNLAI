import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

base_le = "03_San_Pham_Chinh_Thuc/file lẻ"

for g in range(1, 6):
    f_full = os.path.join(base_le, f"SP1_Khung_YCCD_AI_Lop{g}_Day_Du.md")
    f_comp = os.path.join(base_le, f"SP1_Khung_YCCD_AI_Lop{g}_Rut_Gon.md")
    with open(f_full, encoding='utf-8') as f:
        c_full = f.read()
    with open(f_comp, encoding='utf-8') as f:
        c_comp = f.read()

    full_rows = [l for l in c_full.splitlines() if l.strip().startswith("| **")]
    comp_rows = [l for l in c_comp.splitlines() if l.strip().startswith("| **")]
    print(f"Grade {g} (file lẻ): Full rows = {len(full_rows)}, Comp rows = {len(comp_rows)}")
