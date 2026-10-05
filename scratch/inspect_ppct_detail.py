import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

ppct_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(ppct_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'pháp lý' in line.lower():
        print(f"Line {idx+1} contains 'pháp lý': {line.strip()[:160]}")

# Check sections
text = "".join(lines)
parts = re.split(r'## PHẦN [I|V|X]+\. KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH AI - LỚP (\d)', text)
print(f"Total parts split: {len(parts)}")

for i in range(1, len(parts), 2):
    g_num = int(parts[i])
    content = parts[i+1]
    
    # Split into 12 Core and 36 Full
    subsections = content.split("### 2. Kế hoạch Giáo dục Toàn diện")
    core_part = subsections[0]
    full_part = subsections[1] if len(subsections) > 1 else ""
    
    core_rows = [l for l in core_part.split('\n') if re.match(r'\|\s*\*\*\d+\*\*', l)]
    full_rows = [l for l in full_part.split('\n') if re.match(r'\|\s*\*\*\d+\*\*', l)]
    
    print(f"Lớp {g_num}: {len(core_rows)} tiết Cốt lõi, {len(full_rows)} tiết Toàn diện")
