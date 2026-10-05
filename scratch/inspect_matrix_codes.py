import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_v2.0.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all YCCD codes mentioned in the matrix
found_codes = re.findall(r'(\b[1-5]\.[A-D][1-5]\.(?:MR\d+|\d+)\b)', text)
found_unique = sorted(list(set(found_codes)))
print(f"Total YCCD code mentions: {len(found_codes)}")
print(f"Unique YCCD codes found: {len(found_unique)}")

# Compare with our official 123 codes
from parse_full_data import grades_data
official_codes = []
for g in range(1, 6):
    for r in grades_data[g]:
        official_codes.append(r['code'])

print(f"Official codes: {len(official_codes)}")
missing = [c for c in official_codes if c not in found_unique]
print(f"Missing official codes in v2.0 matrix: {len(missing)} -> {missing}")

extra = [c for c in found_unique if c not in official_codes]
print(f"Extra codes in v2.0 matrix: {len(extra)} -> {extra}")
