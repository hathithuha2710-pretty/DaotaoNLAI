import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

ppct_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(ppct_file, "r", encoding="utf-8") as f:
    text = f.read()

blacklist = [
    'cây quyết định', 'decision tree', 'thẻ mô hình', 'model card',
    'ma trận nhầm lẫn', 'confusion matrix', 'few-shot', 'chain-of-thought',
    'common sense', 'foundations of ai',
    'pháp lý', 'độc quyền', 'kiên quyết bài trừ', 'kiểm thử đối kháng',
    'nguyên lý học liên tục', 'thao tác thành thạo', 'đo lường độ tin cậy'
]

print("=== 1. AUDIT BLACKLIST TRÊN PPCT MỚI ===")
found = []
for kw in blacklist:
    m = re.findall(rf'({kw})', text, re.IGNORECASE)
    if m:
        found.append((kw, len(m)))

if found:
    print(f"FAILED: Found blacklisted words in PPCT: {found}")
else:
    print("PASSED: 0 blacklist words found in new PPCT file!")

print("\n=== 2. AUDIT ĐỘ PHỦ 123 YCCĐ CHÍNH THỨC ===")
from parse_full_data import grades_data
official_codes = []
for g in range(1, 6):
    for r in grades_data[g]:
        official_codes.append(r['code'])

ppct_codes = set(re.findall(r'(\b[1-5]\.[A-D][1-5]\.(?:MR\d+|\d+)\b)', text))
missing = [c for c in official_codes if c not in ppct_codes]

print(f"Total official codes: {len(official_codes)}")
print(f"Unique codes found in PPCT: {len(ppct_codes)}")

if not missing:
    print("PASSED: Phủ kín 100% (123/123) YCCĐ của Bộ GD&ĐT trong PPCT mới!")
else:
    print(f"FAILED: Missing codes in PPCT: {missing}")

print("\n=== 3. AUDIT CƠ CẤU TIẾT HỌC 5 KHỐI LỚP ===")
# Count tables and rows
sections = re.split(r'## PHẦN [I|V|X]+: KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH AI - LỚP (\d)', text)
for i in range(1, len(sections), 2):
    g_num = int(sections[i])
    content = sections[i+1]
    
    # Core table
    core_part = content.split("### 2. Kế hoạch Giáo dục Toàn diện")[0]
    core_rows = [l for l in core_part.split('\n') if re.match(r'\|\s*\*\*\d+\*\*', l)]
    
    # 36 lessons table
    full_part = content.split("### 2. Kế hoạch Giáo dục Toàn diện")[1]
    full_rows = [l for l in full_part.split('\n') if re.match(r'\|\s*\*\*\d+\*\*', l)]
    
    print(f"Lớp {g_num}: {len(core_rows)} tiết Cốt lõi, {len(full_rows)} tiết Toàn diện")
