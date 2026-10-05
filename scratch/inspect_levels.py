import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/skills_46.json', 'r', encoding='utf-8') as f:
    skills = json.load(f)

check_ids = [3, 9, 11, 12, 17, 26, 32, 33, 34, 35, 36, 37, 38, 39, 45]
for s in skills:
    stt = s['stt']
    if stt in check_ids:
        print(f"KN {stt}: {s['name']}")
        for l in ['l1', 'l2', 'l3', 'l4', 'l5']:
            fl = s[l].split('<br>')[0].replace('**', '').strip() if s[l] != '-' else '-'
            print(f"   {l}: {fl}")
