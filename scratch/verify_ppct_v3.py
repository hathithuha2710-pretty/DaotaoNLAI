# -*- coding: utf-8 -*-
"""
Verification script for v3 PPCT data.
Checks:
1. Exact lesson counts (12 for core, 36 for comprehensive).
2. 100% Core YCCD coverage (80/80).
3. 100% MR YCCD coverage (43/43).
4. Validation of 46 Skills against Matrix v2.0 (active skills, exact proficiency levels M1/M2/M3).
"""
import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

from lessons_grade1_v3 import GRADE1_12_CORE, GRADE1_36_EXPANDED
from lessons_grade2_v3 import GRADE2_12_CORE, GRADE2_36_EXPANDED
from lessons_grade3_v3 import GRADE3_12_CORE, GRADE3_36_EXPANDED
from lessons_grade4_v3 import GRADE4_12_CORE, GRADE4_36_EXPANDED
from lessons_grade5_v3 import GRADE5_12_CORE, GRADE5_36_EXPANDED

# Load official YCCDs
with open('scratch/yccd_all_grades.json', 'r', encoding='utf-8') as f:
    yccd_all = json.load(f)

# Load 46 Skills Matrix
with open('scratch/skills_46.json', 'r', encoding='utf-8') as f:
    skills_db = json.load(f)

grades_data = {
    1: {"12": GRADE1_12_CORE, "36": GRADE1_36_EXPANDED},
    2: {"12": GRADE2_12_CORE, "36": GRADE2_36_EXPANDED},
    3: {"12": GRADE3_12_CORE, "36": GRADE3_36_EXPANDED},
    4: {"12": GRADE4_12_CORE, "36": GRADE4_36_EXPANDED},
    5: {"12": GRADE5_12_CORE, "36": GRADE5_36_EXPANDED}
}

total_errors = 0
total_warnings = 0

print("================================================================================")
print("             BẮT ĐẦU KIỂM TRA CHẤT LƯỢNG TOÀN DIỆN PPCT v3.0 (QA/QC)           ")
print("================================================================================")

for g in range(1, 6):
    print(f"\n>>> KIỂM TRA LỚP {g} <<<")
    official_core = set(yccd_all[str(g)]["core"].keys())
    official_mr = set(yccd_all[str(g)]["mr"].keys())
    print(f"- Chuẩn QĐ 2422: Core = {len(official_core)}, MR = {len(official_mr)}, Tổng YCCĐ = {len(official_core)+len(official_mr)}")
    
    # 1. Kiểm tra kế hoạch 12 tiết cốt lõi
    plan12 = grades_data[g]["12"]
    if len(plan12) != 12:
        print(f"  [ERROR] Kế hoạch 12 tiết có {len(plan12)} tiết!")
        total_errors += 1
    else:
        print(f"  [PASS] Số tiết Kế hoạch 12 tiết: Đủ 12 tiết.")
        
    found_core_12 = set()
    for row in plan12:
        codes = re.findall(rf'{g}\.[A-D]\d\.\d+', row["ma_yccd"])
        for c in codes:
            found_core_12.add(c)
            
    missing_core_12 = official_core - found_core_12
    if missing_core_12:
        print(f"  [ERROR] 12 tiết cốt lõi THIẾU mã Core: {missing_core_12}")
        total_errors += 1
    else:
        print(f"  [PASS] 12 tiết cốt lõi: Phủ kín 100% YCCĐ cốt lõi ({len(found_core_12)}/{len(official_core)} mã).")
        
    # 2. Kiểm tra kế hoạch 36 tiết
    plan36 = grades_data[g]["36"]
    if len(plan36) != 36:
        print(f"  [ERROR] Kế hoạch 36 tiết có {len(plan36)} tiết!")
        total_errors += 1
    else:
        print(f"  [PASS] Số tiết Kế hoạch 36 tiết: Đủ 36 tiết.")
        
    found_core_36 = set()
    found_mr_36 = set()
    for row in plan36:
        core_codes = re.findall(rf'{g}\.[A-D]\d\.\d+', row["ma_yccd"])
        mr_codes = re.findall(rf'{g}\.[A-D]\d\.MR\d+', row["ma_yccd"])
        for c in core_codes:
            found_core_36.add(c)
        for c in mr_codes:
            found_mr_36.add(c)
            
    missing_core_36 = official_core - found_core_36
    missing_mr_36 = official_mr - found_mr_36
    
    if missing_core_36:
        print(f"  [ERROR] Kế hoạch 36 tiết THIẾU mã Core: {missing_core_36}")
        total_errors += 1
    else:
        print(f"  [PASS] Kế hoạch 36 tiết: Phủ kín 100% YCCĐ cốt lõi ({len(found_core_36)}/{len(official_core)} mã).")
        
    if missing_mr_36:
        print(f"  [ERROR] Kế hoạch 36 tiết THIẾU mã MR: {missing_mr_36}")
        total_errors += 1
    else:
        print(f"  [PASS] Kế hoạch 36 tiết: Phủ kín 100% YCCĐ mở rộng ({len(found_mr_36)}/{len(official_mr)} mã).")
        
    # 3. Kiểm tra tính tương thích Kỹ năng & Mức độ với Ma trận v2.0
    print("  --- Kiểm tra Kỹ năng & Mức độ (Skill & Level Matrix Validation) ---")
    skill_mismatches = 0
    inactive_skills = 0
    all_rows = plan12 + plan36
    checked_tags = set()
    
    for row_idx, row in enumerate(all_rows):
        kn_str = row.get("ky_nang_tag", "")
        # Parse tags like "KN1 (M1)", "KN31 (M2)"
        tags = re.findall(r'(KN\d+)\s*\((M\d)\)', kn_str)
        for kn_id, level in tags:
            tag_key = (g, kn_id, level)
            if tag_key in checked_tags:
                continue
            checked_tags.add(tag_key)
            
            # Lookup in matrix
            sk_info = skills_db.get(kn_id)
            if not sk_info:
                print(f"    [ERROR] Kỹ năng không tồn tại: {kn_id}")
                total_errors += 1
                continue
                
            grade_level_matrix = sk_info["grade_levels"].get(str(g))
            if not grade_level_matrix:
                print(f"    [ERROR LỚP {g}] Kỹ năng {kn_id} KHÔNG được kích hoạt ở Lớp {g} trong Ma trận! (Gắn nhầm)")
                inactive_skills += 1
                total_errors += 1
            else:
                expected_level = f"M{grade_level_matrix['level']}"
                if level != expected_level:
                    print(f"    [LEVEL MISMATCH LỚP {g}] {kn_id} thực tế trong bài: {level} != Ma trận quy định: {expected_level}")
                    skill_mismatches += 1
                    total_errors += 1
                    
    if skill_mismatches == 0 and inactive_skills == 0:
        print(f"  [PASS] 100% Kỹ năng và Mức độ (M1/M2/M3) khớp hoàn hảo với Ma trận 46 kỹ năng v2.0!")
    else:
        print(f"  [FAIL] Phát hiện {skill_mismatches} lỗi lệch mức độ, {inactive_skills} lỗi gắn nhầm kỹ năng chưa kích hoạt.")

print("\n================================================================================")
print(f"KẾT QUẢ KIỂM TRA CHUNG: Tổng lỗi = {total_errors}, Tổng cảnh báo = {total_warnings}")
print("================================================================================")
