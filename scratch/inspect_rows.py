import os
import re

full_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md"
old_compact_file = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md"

with open(full_file, "r", encoding="utf-8") as f:
    full_lines = f.readlines()

with open(old_compact_file, "r", encoding="utf-8") as f:
    old_lines = f.readlines()

print(f"Full file lines: {len(full_lines)}")
print(f"Old compact file lines: {len(old_lines)}")

# Parse rows from full file
full_rows = []
for line in full_lines:
    if line.startswith("| **") or line.startswith("|**"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 5:
            full_rows.append({
                "stt": parts[0],
                "code": parts[1].replace("**", ""),
                "topic": parts[2],
                "vn": parts[3],
                "intl": parts[4]
            })

print(f"Extracted {len(full_rows)} rows from full file.")

# Parse rows from old compact file
old_rows = []
for line in old_lines:
    if line.startswith("| **") or line.startswith("|**"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 4:
            old_rows.append({
                "stt": parts[0],
                "mach": parts[1],
                "topic": parts[2],
                "desc": parts[3]
            })

print(f"Extracted {len(old_rows)} rows from old compact file.")
