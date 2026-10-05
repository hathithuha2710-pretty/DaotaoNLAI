import re
import json

with open('03_San_Pham_Chinh_Thuc/Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_v2.0.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

skill_data = []
for line in lines:
    line_s = line.strip()
    if not line_s.startswith('|'):
        continue
    cells = [c.strip() for c in line_s.split('|')]
    if len(cells) >= 9 and cells[1].replace('*', '').isdigit():
        stt = int(cells[1].replace('*', ''))
        name_cell = cells[2]
        # name and definition
        parts_name = name_cell.split('<br>')
        name = parts_name[0].replace('*', '').strip()
        definition = parts_name[1].replace('*', '').strip() if len(parts_name) > 1 else ''
        mach = cells[3].replace('`', '').strip()
        l1, l2, l3, l4, l5 = cells[4], cells[5], cells[6], cells[7], cells[8]
        skill_data.append({
            'stt': stt,
            'name': name,
            'definition': definition,
            'mach': mach,
            'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'l5': l5
        })

with open('scratch/skills_46.json', 'w', encoding='utf-8') as f:
    json.dump(skill_data, f, ensure_ascii=False, indent=2)

print('Saved scratch/skills_46.json, total skills:', len(skill_data))
