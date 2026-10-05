import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md', 'r', encoding='utf-8') as f:
    old_full = f.read()

with open('03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md', 'r', encoding='utf-8') as f:
    new_full = f.read()

def parse_md_table(text):
    rows = {}
    for line in text.split('\n'):
        if line.startswith('| **') or line.startswith('|**'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 5:
                code = parts[1].replace('**', '').strip()
                rows[code] = {
                    'stt': parts[0].replace('**', ''),
                    'code': code,
                    'topic': parts[2],
                    'vn': parts[3],
                    'intl': parts[4]
                }
    return rows

old_data = parse_md_table(old_full)
new_data = parse_md_table(new_full)

print(f"Total old codes: {len(old_data)}, Total new codes: {len(new_data)}")

diff_count = 0
for code, nd in new_data.items():
    if code in old_data:
        od = old_data[code]
        if od['intl'] != nd['intl'] or od['vn'] != nd['vn']:
            diff_count += 1
            print(f"[{code}]")
            if od['vn'] != nd['vn']:
                print(f"  VN Diff:")
                print(f"    OLD: {od['vn']}")
                print(f"    NEW: {nd['vn']}")
            if od['intl'] != nd['intl']:
                print(f"  INTL Diff:")
                print(f"    OLD: {od['intl']}")
                print(f"    NEW: {nd['intl']}")
            print("-" * 60)

print(f"Total differences found across 123 YCCĐ: {diff_count}")
