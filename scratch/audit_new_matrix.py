import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

new_matrix_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(new_matrix_file, "r", encoding="utf-8") as f:
    text = f.read()

blacklist = [
    'cây quyết định', 'decision tree', 'thẻ mô hình', 'model card',
    'ma trận nhầm lẫn', 'confusion matrix', 'few-shot', 'chain-of-thought',
    'common sense', 'foundations of ai',
    'pháp lý', 'độc quyền', 'kiên quyết bài trừ', 'kiểm thử đối kháng',
    'nguyên lý học liên tục', 'thao tác thành thạo', 'đo lường độ tin cậy'
]

print("=== 1. AUDIT BLACKLIST TRÊN MA TRẬN MỚI ===")
found = []
for kw in blacklist:
    m = re.findall(rf'({kw})', text, re.IGNORECASE)
    if m:
        found.append((kw, len(m)))

if found:
    print(f"FAILED: Found blacklisted words: {found}")
else:
    print("PASSED: 0 blacklist words found in new SP2 matrix!")

print("\n=== 2. AUDIT ĐỘ PHỦ 123 YCCĐ CHÍNH THỨC ===")
from parse_full_data import grades_data
official_codes = []
for g in range(1, 6):
    for r in grades_data[g]:
        official_codes.append(r['code'])

matrix_codes = re.findall(r'(\b[1-5]\.[A-D][1-5]\.(?:MR\d+|\d+)\b)', text)
matrix_unique = set(matrix_codes)

missing = [c for c in official_codes if c not in matrix_unique]
print(f"Total official codes: {len(official_codes)}")
print(f"Unique official codes in matrix: {len(matrix_unique)}")

if not missing:
    print("PASSED: Phủ kín 100% (123/123) YCCĐ của Bộ GD&ĐT!")
else:
    print(f"FAILED: Missing codes: {missing}")

extra = [c for c in matrix_unique if c not in set(official_codes)]
if not extra:
    print("PASSED: 0 mã ngoài khung (100% khớp chuẩn QĐ 2422)!")
else:
    print(f"FAILED: Extra codes found: {extra}")
