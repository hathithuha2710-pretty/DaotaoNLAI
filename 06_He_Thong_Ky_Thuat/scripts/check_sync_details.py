import os
import sys
import re
import docx

sys.stdout.reconfigure(encoding='utf-8')

# Compare Compact MD codes
compact_md = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md"
with open(compact_md, encoding='utf-8') as f:
    c_lines = f.readlines()

comp_codes = {1: [], 2: [], 3: [], 4: [], 5: []}
current_g = None
for l in c_lines:
    ls = l.strip()
    m = re.search(r"Lớp\s*(\d)", ls, re.IGNORECASE)
    if (ls.startswith("#") or ls.startswith("##")) and m:
        current_g = int(m.group(1))
    if ls.startswith("| **"):
        parts = [p.strip() for p in ls.split("|")[1:-1]]
        # In compact MD, what column is the code?
        # Let's inspect parts: parts[0] is STT, parts[1] is Strand, parts[2] is Topic, parts[3] is YCCĐ & Outcome?
        # Let's see how code is stored in compact MD
        comp_codes[current_g].append(parts)

print("Compact MD row count by grade:")
for g in range(1, 6):
    print(f"Lớp {g}: {len(comp_codes[g])} rows")

# Let's print first row of compact MD for L1
if comp_codes[1]:
    print("\nSample Compact MD row Lớp 1:", comp_codes[1][0])

# Check individual files in file lẻ vs Master
print("\n=== CHECKING INDIVIDUAL FILES VS MASTER ===")
base_le = "03_San_Pham_Chinh_Thuc/file lẻ"
master_full_md = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md"

with open(master_full_md, encoding='utf-8') as f:
    mf_text = f.read()

for g in range(1, 6):
    f_indiv = os.path.join(base_le, f"SP1_Khung_YCCD_AI_Lop{g}_Day_Du.md")
    with open(f_indiv, encoding='utf-8') as f:
        indiv_text = f.read()
    
    indiv_rows = [l.strip() for l in indiv_text.splitlines() if l.strip().startswith("| **")]
    print(f"Grade {g}: Individual full MD rows = {len(indiv_rows)}")
