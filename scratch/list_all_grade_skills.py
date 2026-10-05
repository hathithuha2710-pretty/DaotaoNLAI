import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/skills_46.json', 'r', encoding='utf-8') as f:
    skills = json.load(f)

for g_idx, g_key in enumerate(['l1', 'l2', 'l3', 'l4', 'l5'], start=1):
    print(f"\n================ SKILLS FOR GRADE {g_idx} ================")
    for s in skills:
        col = s[g_key]
        if col != '-':
            level = col.split('<br>')[0].replace('**', '').strip()
            print(f"KN {s['stt']:2d} ({s['name'][:28]}): {level}")
