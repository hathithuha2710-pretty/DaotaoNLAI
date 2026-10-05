import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

old_ppct_file = "03_San_Pham_Chinh_Thuc/Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_QD2422.md"

with open(old_ppct_file, "r", encoding="utf-8") as f:
    text = f.read()

# Check blacklist words in old PPCT file
blacklist = [
    'cây quyết định', 'decision tree', 'thẻ mô hình', 'model card',
    'ma trận nhầm lẫn', 'confusion matrix', 'few-shot', 'chain-of-thought',
    'common sense', 'foundations of ai',
    'pháp lý', 'độc quyền', 'kiên quyết bài trừ', 'kiểm thử đối kháng',
    'nguyên lý học liên tục', 'thao tác thành thạo', 'đo lường độ tin cậy'
]

print("=== CHECKING BLACKLIST IN OLD PPCT ===")
found = []
for kw in blacklist:
    m = re.findall(rf'({kw})', text, re.IGNORECASE)
    if m:
        found.append((kw, len(m)))

print("Blacklist found in old PPCT:", found)
