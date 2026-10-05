import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

master_comp_md = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md"
with open(master_comp_md, encoding='utf-8') as f:
    mc_lines = f.readlines()

master_rows = {g: [] for g in range(1, 6)}
current_g = None
for l in mc_lines:
    ls = l.strip()
    m = re.search(r"Lớp\s*(\d)", ls, re.IGNORECASE)
    if (ls.startswith("#") or ls.startswith("##")) and m:
        current_g = int(m.group(1))
    if ls.startswith("| **"):
        parts = [p.strip() for p in ls.split("|")[1:-1]]
        master_rows[current_g].append(parts)

base_le = "03_San_Pham_Chinh_Thuc/file lẻ"
diffs = 0

for g in range(1, 6):
    indiv_file = os.path.join(base_le, f"SP1_Khung_YCCD_AI_Lop{g}_Rut_Gon.md")
    with open(indiv_file, encoding='utf-8') as f:
        indiv_lines = f.readlines()
    
    indiv_rows = []
    for l in indiv_lines:
        ls = l.strip()
        if ls.startswith("| **"):
            parts = [p.strip() for p in ls.split("|")[1:-1]]
            indiv_rows.append(parts)
    
    if len(master_rows[g]) != len(indiv_rows):
        print(f"❌ Lớp {g}: Compact Row count diff! Master={len(master_rows[g])}, Indiv={len(indiv_rows)}")
        diffs += 1
        continue
    
    for i in range(len(master_rows[g])):
        m_r = master_rows[g][i]
        i_r = indiv_rows[i]
        if m_r[3] != i_r[3]:
            print(f"⚠️ Lớp {g} compact row {i+1}: mismatch!")
            diffs += 1

if diffs == 0:
    print("✅ 100% ĐỒNG BỘ TUYỆT ĐỐI CẢ BẢN RÚT GỌN (COMPACT)!")
else:
    print(f"Tổng số điểm lệch bản rút gọn: {diffs}")
