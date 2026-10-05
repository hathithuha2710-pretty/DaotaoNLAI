import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

folder = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi"
expected_files = [
    "SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md",
    "SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.docx",
    "SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md",
    "SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.docx",
    "SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.md",
    "SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.docx",
    "SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.xlsx"
]

print("=== 1. TỔNG KIỂM TRA FILE TRONG THƯ MỤC SẢN PHẨM MỚI ===")
all_exist = True
for f in expected_files:
    fpath = os.path.join(folder, f)
    if os.path.exists(fpath):
        size_kb = os.path.getsize(fpath) / 1024
        print(f"  [OK] {f} ({size_kb:.1f} KB)")
    else:
        print(f"  [FAIL] Missing file: {f}")
        all_exist = False

blacklist = [
    'cây quyết định', 'decision tree', 'thẻ mô hình', 'model card',
    'ma trận nhầm lẫn', 'confusion matrix', 'few-shot', 'chain-of-thought',
    'common sense', 'foundations of ai',
    'pháp lý', 'độc quyền', 'kiên quyết bài trừ', 'kiểm thử đối kháng',
    'nguyên lý học liên tục', 'thao tác thành thạo', 'đo lường độ tin cậy'
]

print("\n=== 2. KIỂM ĐỊNH BLACKLIST TRÊN CẢ 3 FILE MARKDOWN ===")
md_files = [
    "SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md",
    "SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md",
    "SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.md"
]

all_clean = True
for mf in md_files:
    with open(os.path.join(folder, mf), 'r', encoding='utf-8') as s:
        text = s.read()
    found = []
    for kw in blacklist:
        m = re.findall(rf'({kw})', text, re.IGNORECASE)
        if m:
            found.append((kw, len(m)))
    if found:
        print(f"  [FAIL] {mf} chứa từ cấm: {found}")
        all_clean = False
    else:
        print(f"  [PASS] {mf}: SẠCH 100% BLACKLIST (0 từ cấm)!")

print("\n=== 3. KIỂM ĐỊNH ĐỘ PHỦ YCCĐ BỘ GD&ĐT (123 YCCĐ) TRÊN SP2 MỚI ===")
with open(os.path.join(folder, "SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.md"), "r", encoding="utf-8") as s:
    sp2_text = s.read()

from parse_full_data import grades_data
official_codes = []
for g in range(1, 6):
    for r in grades_data[g]:
        official_codes.append(r['code'])

sp2_codes = set(re.findall(r'(\b[1-5]\.[A-D][1-5]\.(?:MR\d+|\d+)\b)', sp2_text))
missing = [c for c in official_codes if c not in sp2_codes]

if not missing:
    print(f"  [PASS] SP2 Ma Trận phủ kín 100% ({len(official_codes)}/{len(official_codes)}) YCCĐ chuẩn quốc gia!")
else:
    print(f"  [FAIL] SP2 thiếu các mã: {missing}")
