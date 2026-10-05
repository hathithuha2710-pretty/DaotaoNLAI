import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

from parse_full_data import grades_data

old_compact_file = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md"

with open(old_compact_file, "r", encoding="utf-8") as f:
    text = f.read()

# Split into grades in old compact file
old_sections = re.split(r'## PHẦN [I|V|X]+: LỚP (\d)', text)
old_grades_data = {}
for i in range(1, len(old_sections), 2):
    g_num = int(old_sections[i])
    content = old_sections[i+1]
    rows = []
    lines = content.strip().split('\n')
    for line in lines:
        if line.startswith('| **') or line.startswith('|**'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 4:
                rows.append({
                    "stt": parts[0].replace('**', ''),
                    "mach": parts[1].replace('**', ''),
                    "subtopic": parts[2],
                    "desc": parts[3]
                })
    old_grades_data[g_num] = rows

print("Old compact rows parsed:")
for g, rows in old_grades_data.items():
    print(f"Lớp {g}: {len(rows)} YCCĐ")

# Check if old desc contains full VN requirement keywords
for g in range(1, 6):
    new_rows = grades_data[g]
    old_rows = old_grades_data[g]
    print(f"\n=== LỚP {g} SAMPLE COMPARISON (First 3) ===")
    for idx in range(min(3, len(new_rows))):
        nr = new_rows[idx]
        od = old_rows[idx]
        print(f"[{nr['code']}]")
        print(f"  VN QĐ2422:   {nr['vn']}")
        print(f"  Old Compact: {od['desc']}")
