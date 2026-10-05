import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

compact_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md"

with open(compact_file, "r", encoding="utf-8") as f:
    text = f.read()

blacklist = [
    'cây quyết định', 'decision tree', 'thẻ mô hình', 'model card',
    'ma trận nhầm lẫn', 'confusion matrix', 'few-shot', 'chain-of-thought',
    'common sense', 'foundations of ai',
    'pháp lý', 'độc quyền', 'kiên quyết bài trừ', 'kiểm thử đối kháng',
    'nguyên lý học liên tục', 'thao tác thành thạo', 'đo lường độ tin cậy'
]

print("=== CHECKING BLACKLIST ON COMPACT FILE ===")
found_errors = []
for kw in blacklist:
    m = re.findall(rf'({kw})', text, re.IGNORECASE)
    if m:
        found_errors.append((kw, len(m)))

if found_errors:
    print(f"FAILED: Found blacklisted words: {found_errors}")
else:
    print("PASSED: 0 blacklist words found!")

# Check grade 3 specific
g3_part = text.split("## PHẦN III: LỚP 3")[1].split("## PHẦN IV: LỚP 4")[0]
for kw in ['tất yếu', 'vô hiệu']:
    m = re.findall(rf'({kw})', g3_part, re.IGNORECASE)
    if m:
        print(f"FAILED: Grade 3 restricted word found: {kw}")
    else:
        print(f"PASSED: Grade 3 free of '{kw}'")

# Check source mentions (UNESCO, OECD, Singapore MOE, AI4K12, Google)
print("\n=== CHECKING SOURCE NAMES IN YCCD DESCRIPTIONS ===")
source_keywords = ['UNESCO', 'OECD', 'Singapore', 'AI4K12', 'DeepMind', 'MIT Day of AI', 'Common Sense', 'UNICEF']
# Only check inside table rows
table_lines = [l for l in text.split('\n') if l.startswith('| **') or l.startswith('|**')]
source_found = []
for idx, line in enumerate(table_lines):
    # take column 5 (integrated desc)
    cols = [c.strip() for c in line.split('|')[1:-1]]
    if len(cols) >= 5:
        desc = cols[4]
        for src in source_keywords:
            if re.search(rf'\b{src}\b', desc, re.IGNORECASE):
                source_found.append((cols[1], src))

if source_found:
    print(f"FAILED: Source names found in descriptions: {source_found}")
else:
    print("PASSED: 0 source citations found in descriptions!")

# Count rows per grade
print("\n=== ROW COUNTS PER GRADE ===")
grade_sections = re.split(r'## PHẦN [I|V|X]+: LỚP (\d)', text)
counts = {}
for i in range(1, len(grade_sections), 2):
    g_num = int(grade_sections[i])
    content = grade_sections[i+1]
    rows = [l for l in content.strip().split('\n') if l.startswith('| **') or l.startswith('|**')]
    counts[g_num] = len(rows)
    print(f"Lớp {g_num}: {len(rows)} rows")

expected = {1: 21, 2: 29, 3: 32, 4: 17, 5: 24}
if counts == expected:
    print("PASSED: Row counts match expected 100% (21, 29, 32, 17, 24 = 123)!")
else:
    print(f"FAILED: Row counts mismatch: {counts} vs {expected}")
