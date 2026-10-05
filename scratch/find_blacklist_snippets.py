import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_v2.0.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re
rows = text.split('\n')
for line in rows:
    for kw in ['model card', 'cây quyết định', 'decision tree', 'confusion matrix', 'few-shot', 'pháp lý']:
        if kw in line.lower():
            m = re.match(r'\|\s*\*\*(\d+)\*\*', line)
            stt = m.group(1) if m else "?"
            print(f"Keyword '{kw}' found in skill {stt}:")
            print(f"  Line snippet: {line[:200]}...")
            print("-" * 50)
