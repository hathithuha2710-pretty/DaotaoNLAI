import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_v2.0.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Find table rows starting with | **<number>** |
skill_rows = []
current_row = None

for line in lines:
    m = re.match(r'\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*([^\*]+)\*\*(.*)', line)
    if m:
        stt = int(m.group(1))
        name = m.group(2).strip()
        rest = m.group(3)
        cols = [c.strip() for c in rest.split('|')]
        skill_rows.append({
            'stt': stt,
            'name': name,
            'line': line
        })

print(f"Total matched skills: {len(skill_rows)}")
for r in skill_rows[:10]:
    print(f"{r['stt']}. {r['name']}")
