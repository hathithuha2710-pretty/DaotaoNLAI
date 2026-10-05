import re
import json

with open('03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*([1-5]\.[A-D]\d(?:\.MR\d+|\.\d+))\*\*\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|'
matches = re.findall(pattern, text)

data = {}
for stt, code, mach, yccd, intl in matches:
    g = int(code[0])
    if g not in data:
        data[g] = {'core': {}, 'mr': {}}
    target = data[g]['mr'] if '.MR' in code else data[g]['core']
    target[code] = {
        'mach': mach.strip().replace('<br>', ' ').replace('•', '').strip(),
        'yccd': yccd.strip().replace('\n', ' '),
        'intl': intl.strip().replace('\n', ' ')
    }

with open('scratch/yccd_all_grades.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Saved scratch/yccd_all_grades.json')
for g in sorted(data.keys()):
    c_count = len(data[g]['core'])
    m_count = len(data[g]['mr'])
    print(f'Lớp {g}: {c_count} core, {m_count} mr, Tổng = {c_count + m_count}')
