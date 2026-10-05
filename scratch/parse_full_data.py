import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

full_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md"

with open(full_file, "r", encoding="utf-8") as f:
    text = f.read()

# Split into grades
grade_sections = re.split(r'## PHẦN [I|V|X]+: KHUNG NỘI DUNG GIÁO DỤC AI – LỚP (\d)', text)

# grade_sections has [preamble, '1', content1, '2', content2, ...]
grades_data = {}
for i in range(1, len(grade_sections), 2):
    grade_num = int(grade_sections[i])
    content = grade_sections[i+1]
    
    rows = []
    lines = content.strip().split('\n')
    for line in lines:
        if line.startswith('| **') or line.startswith('|**'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 5:
                stt = parts[0].replace('**', '')
                code = parts[1].replace('**', '')
                topic_raw = parts[2]
                vn_req = parts[3]
                intl_req = parts[4]
                
                # topic_raw looks like: A. Tư duy lấy con người làm trung tâm<br>• *Tính chủ động của con người – Con người có cảm xúc, AI thì không*
                topic_parts = topic_raw.split('<br>')
                mach = topic_parts[0].strip()
                subtopic = topic_parts[1].replace('•', '').replace('*', '').strip() if len(topic_parts) > 1 else ""
                
                rows.append({
                    "stt": stt,
                    "code": code,
                    "mach": mach,
                    "subtopic": subtopic,
                    "vn": vn_req,
                    "intl": intl_req
                })
    grades_data[grade_num] = rows
    print(f"Lớp {grade_num}: {len(rows)} YCCĐ")

print(f"Tổng cộng: {sum(len(r) for r in grades_data.values())} YCCĐ")
