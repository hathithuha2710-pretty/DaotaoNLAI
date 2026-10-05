import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'## PHẦN [IVXLC]+\.\s+KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH AI - LỚP (\d)', text)
for i in range(1, len(parts), 2):
    g = int(parts[i])
    content = parts[i+1]
    tables = content.split('### ')
    for t in tables[1:]:
        title = t.split('\n')[0].strip()
        rows = [l for l in t.split('\n') if re.match(r'\|\s*\*\*\d+\*\*', l)]
        tiet_list = []
        for r in rows:
            cols = [c.strip() for c in r.split('|')]
            tiet_list.append(cols[1].replace('**', ''))
        print(f"Lớp {g} - {title[:35]}: {len(tiet_list)} rows -> {tiet_list}")
