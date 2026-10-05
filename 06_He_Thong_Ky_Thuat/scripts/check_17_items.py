import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

master_full_md = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md"
with open(master_full_md, encoding='utf-8') as f:
    lines = f.readlines()

current_grade = None
grade_rows = {1: [], 2: [], 3: [], 4: [], 5: []}

for line in lines:
    line_s = line.strip()
    m = re.search(r"Lớp\s*(\d)", line_s, re.IGNORECASE)
    if (line_s.startswith("#") or line_s.startswith("##")) and m:
        current_grade = int(m.group(1))
    if line_s.startswith("| **"):
        parts = [p.strip() for p in line_s.split("|")[1:-1]]
        grade_rows[current_grade].append(parts)

items_to_check = {
    1: [3, 4, 9, 12, 15, 18, 20],
    2: [10, 11, 23, 27],
    3: [32],
    4: [13],
    5: [3, 13, 18, 23]
}

print("=== CHECKING THE 17 AUDIT ITEMS IN MASTER FULL MD ===")
for g, items in items_to_check.items():
    print(f"\n--- GRADE {g} ---")
    rows = grade_rows[g]
    for idx in items:
        # idx is 1-based STT
        row = rows[idx-1]
        stt = row[0]
        code = row[1]
        topic = row[2]
        yccd = row[3]
        inter = row[4]
        print(f"STT {stt} | Code: {code}")
        print(f"  YCCĐ: {yccd}")
        print(f"  Tham chiếu QT: {inter}\n")
