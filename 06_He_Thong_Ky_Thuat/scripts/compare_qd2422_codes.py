import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Parse QĐ 2422 to extract all Primary YCCĐs
qd_path = "06_He_Thong_Ky_Thuat/extracted_data/qd2422_full.txt"
with open(qd_path, encoding='utf-8') as f:
    lines = f.readlines()

# Let's find where each grade's YCCĐs are defined in QĐ 2422
# The codes look like: 1.A1.1, 1.A2.MR1, etc.
qd_codes = {1: [], 2: [], 3: [], 4: [], 5: []}

code_regex = re.compile(r'\b([1-5]\.[A-D][1-5]\.(?:MR\d+|\d+))\b')

for line in lines:
    matches = code_regex.findall(line)
    for m in matches:
        g = int(m[0])
        if m not in qd_codes[g]:
            qd_codes[g].append(m)

print("QĐ 2422 extracted primary codes:")
total_qd = 0
for g in range(1, 6):
    print(f"Lớp {g}: {len(qd_codes[g])} codes -> {qd_codes[g][:5]}... {qd_codes[g][-3:]}")
    total_qd += len(qd_codes[g])
print(f"Total primary codes in QĐ 2422: {total_qd}")

# 2. Extract codes from Master Full MD
master_md = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md"
with open(master_md, encoding='utf-8') as f:
    m_lines = f.readlines()

master_codes = {1: [], 2: [], 3: [], 4: [], 5: []}
current_g = None
for l in m_lines:
    ls = l.strip()
    m = re.search(r"Lớp\s*(\d)", ls, re.IGNORECASE)
    if (ls.startswith("#") or ls.startswith("##")) and m:
        current_g = int(m.group(1))
    if ls.startswith("| **"):
        parts = [p.strip() for p in ls.split("|")[1:-1]]
        code_raw = parts[1].replace("*", "")
        master_codes[current_g].append(code_raw)

print("\nMaster Full MD extracted codes:")
total_master = 0
for g in range(1, 6):
    print(f"Lớp {g}: {len(master_codes[g])} codes")
    total_master += len(master_codes[g])
print(f"Total in Master Full MD: {total_master}")

# Compare one-by-one
all_matched = True
for g in range(1, 6):
    qd_set = set(qd_codes[g])
    ms_set = set(master_codes[g])
    diff_missing = qd_set - ms_set
    diff_extra = ms_set - qd_set
    if diff_missing:
        print(f"❌ Lớp {g} MISSING in Master: {diff_missing}")
        all_matched = False
    if diff_extra:
        print(f"❌ Lớp {g} EXTRA in Master: {diff_extra}")
        all_matched = False
    if not diff_missing and not diff_extra:
        # Check order
        if qd_codes[g] == master_codes[g]:
            print(f"✅ Lớp {g}: Khớp 100% cả tập hợp và thứ tự ({len(master_codes[g])}/{len(qd_codes[g])})")
        else:
            print(f"⚠️ Lớp {g}: Khớp 100% tập hợp nhưng thứ tự có khác biệt chút ít")

if all_matched:
    print("\n🎉 HOÀN TOÀN TRÙNG KHỚP 100% VỚI DANH MỤC PHÁP LÝ QĐ 2422!")
