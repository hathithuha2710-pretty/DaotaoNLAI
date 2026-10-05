import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_v2.0.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract skill names
skill_pattern = re.findall(r'\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*([^\*]+)\*\*', text)
print(f"Total skills extracted: {len(skill_pattern)}")
for stt, name in skill_pattern:
    print(f"{stt}. {name.strip()}")
