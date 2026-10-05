import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

full_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md"
old_compact_file = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md"

with open(full_file, "r", encoding="utf-8") as f:
    full_lines = [l for l in f if l.startswith("| **") or l.startswith("|**")]

with open(old_compact_file, "r", encoding="utf-8") as f:
    old_lines = [l for l in f if l.startswith("| **") or l.startswith("|**")]

for i in range(5):
    f_parts = [p.strip() for p in full_lines[i].split("|")[1:-1]]
    o_parts = [p.strip() for p in old_lines[i].split("|")[1:-1]]
    print(f"--- Row {i+1} ({f_parts[1].replace('**', '')}) ---")
    print(f"VN (Full): {f_parts[3]}")
    print(f"INTL (Full): {f_parts[4][:120]}...")
    print(f"Old Compact: {o_parts[3]}")
    print()
