import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

master_full_md = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md"
with open(master_full_md, encoding='utf-8') as f:
    mf_lines = f.readlines()

# Extract master rows by grade
master_rows = {g: [] for g in range(1, 6)}
current_g = None
for l in mf_lines:
    ls = l.strip()
    m = re.search(r"Lớp\s*(\d)", ls, re.IGNORECASE)
    if (ls.startswith("#") or ls.startswith("##")) and m:
        current_g = int(m.group(1))
    if ls.startswith("| **"):
        parts = [p.strip() for p in ls.split("|")[1:-1]]
        master_rows[current_g].append(parts)

# Compare each grade with individual file
base_le = "03_San_Pham_Chinh_Thuc/file lẻ"
diffs = 0

for g in range(1, 6):
    indiv_file = os.path.join(base_le, f"SP1_Khung_YCCD_AI_Lop{g}_Day_Du.md")
    with open(indiv_file, encoding='utf-8') as f:
        indiv_lines = f.readlines()
    
    indiv_rows = []
    for l in indiv_lines:
        ls = l.strip()
        if ls.startswith("| **"):
            parts = [p.strip() for p in ls.split("|")[1:-1]]
            indiv_rows.append(parts)
    
    if len(master_rows[g]) != len(indiv_rows):
        print(f"❌ Lớp {g}: Row count diff! Master={len(master_rows[g])}, Indiv={len(indiv_rows)}")
        diffs += 1
        continue
    
    # Compare each row
    for i in range(len(master_rows[g])):
        m_r = master_rows[g][i]
        i_r = indiv_rows[i]
        # Compare Code (col 1), YCCĐ (col 3)
        if m_r[1] != i_r[1]:
            print(f"❌ Lớp {g} row {i+1}: Code mismatch: Master '{m_r[1]}' vs Indiv '{i_r[1]}'")
            diffs += 1
        if m_r[3] != i_r[3]:
            print(f"⚠️ Lớp {g} row {i+1} ({m_r[1]}): YCCĐ text mismatch!")
            print(f"   Master: {m_r[3][:60]}...")
            print(f"   Indiv : {i_r[3][:60]}...")
            diffs += 1

if diffs == 0:
    print("✅ 100% ĐỒNG BỘ TUYỆT ĐỐI GIỮA FILE TỔNG THỂ VÀ TỪNG FILE LẺ!")
else:
    print(f"Tổng số điểm lệch: {diffs}")
