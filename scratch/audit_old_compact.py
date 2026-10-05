import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

old_compact_file = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md"

with open(old_compact_file, "r", encoding="utf-8") as f:
    text = f.read()

blacklist = [
    'cây quyết định', 'decision tree', 'thẻ mô hình', 'model card',
    'ma trận nhầm lẫn', 'confusion matrix', 'few-shot', 'chain-of-thought',
    'common sense', 'foundations of ai',
    'pháp lý', 'độc quyền', 'kiên quyết bài trừ', 'kiểm thử đối kháng',
    'nguyên lý học liên tục', 'thao tác thành thạo', 'đo lường độ tin cậy'
]

found = []
for kw in blacklist:
    m = re.findall(rf'({kw})', text, re.IGNORECASE)
    if m:
        found.append((kw, len(m)))

print("Blacklist in old compact file:", found)

# Check grade 3 for 'tất yếu', 'vô hiệu'
g3_part = text.split("## PHẦN III: LỚP 3")[1].split("## PHẦN IV: LỚP 4")[0]
for kw in ['tất yếu', 'vô hiệu']:
    m = re.findall(rf'({kw})', g3_part, re.IGNORECASE)
    if m:
        print(f"Grade 3 restricted word found: {kw} ({len(m)})")
