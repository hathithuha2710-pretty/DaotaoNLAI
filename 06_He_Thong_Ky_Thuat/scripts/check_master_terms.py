import os
import sys
import re
import docx

sys.stdout.reconfigure(encoding='utf-8')

# Read master full MD
master_full_md = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md"
master_comp_md = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md"

with open(master_full_md, encoding='utf-8') as f:
    full_text = f.read()

with open(master_comp_md, encoding='utf-8') as f:
    comp_text = f.read()

# Let's check the 17 red flags from Hoi_dong_review_SP1_YCCD_AI_Lop1_5.md
# L1: items 3, 4, 9, 12, 15, 18, 20
# L2: items 10, 11, 23, 27
# L3: item 32
# L4: item 13
# L5: items 3, 13, 18, 23

# Also blacklist words:
blacklist = [
    r"\bpháp lý\b",
    r"độc quyền",
    r"kiên quyết bài trừ",
    r"kiểm thử đối kháng",
    r"nguyên lý học liên tục",
    r"thao tác thành thạo",
    r"đo lường độ tin cậy",
    r"\btất yếu\b",
    r"\bvô hiệu\b",
    # Zero deviation policy terms (wrong terms):
    r"nhắc lệnh",
    r"ảo tưởng mô hình",
    r"AI chém gió",
    r"thành kiến máy móc",
    r"clip ghép mặt",
    r"quá tải mô hình",
    r"AI sinh nội dung",
    r"đại lý AI",
    r"giấu danh tính",
    r"12 tiết tự chọn"
]

print("=== CHECKING BLACKLIST AND FORBIDDEN TERMS IN MASTER FULL MD ===")
for b in blacklist:
    matches = list(re.finditer(b, full_text, re.IGNORECASE))
    if matches:
        print(f"Found forbidden term '{b}' ({len(matches)} occurrences):")
        for m in matches:
            start = max(0, m.start() - 40)
            end = min(len(full_text), m.end() + 40)
            snippet = full_text[start:end].replace('\n', ' ')
            print(f"   ...{snippet}...")
    else:
        print(f"Clean: '{b}'")

print("\n=== CHECKING BLACKLIST AND FORBIDDEN TERMS IN MASTER COMPACT MD ===")
for b in blacklist:
    matches = list(re.finditer(b, comp_text, re.IGNORECASE))
    if matches:
        print(f"Found forbidden term '{b}' ({len(matches)} occurrences):")
        for m in matches:
            start = max(0, m.start() - 40)
            end = min(len(comp_text), m.end() + 40)
            snippet = comp_text[start:end].replace('\n', ' ')
            print(f"   ...{snippet}...")
    else:
        print(f"Clean: '{b}'")
