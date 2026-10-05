# -*- coding: utf-8 -*-
"""
Verification script for all 5 grades PPCT.
Checks coverage of 100% Core and 100% MR YCCDs against official QĐ 2422 database.
"""
import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

from lessons_grade1 import GRADE1_12_CORE, GRADE1_36_EXPANDED
from lessons_grade2 import GRADE2_12_CORE, GRADE2_36_EXPANDED
from lessons_grade3 import GRADE3_12_CORE, GRADE3_36_EXPANDED
from lessons_grade4 import GRADE4_12_CORE, GRADE4_36_EXPANDED
from lessons_grade5 import GRADE5_12_CORE, GRADE5_36_EXPANDED

# Load official YCCDs
with open('scratch/yccd_all_grades.json', 'r', encoding='utf-8') as f:
    yccd_all = json.load(f)

grades_data = {
    1: {"12": GRADE1_12_CORE, "36": GRADE1_36_EXPANDED},
    2: {"12": GRADE2_12_CORE, "36": GRADE2_36_EXPANDED},
    3: {"12": GRADE3_12_CORE, "36": GRADE3_36_EXPANDED},
    4: {"12": GRADE4_12_CORE, "36": GRADE4_36_EXPANDED},
    5: {"12": GRADE5_12_CORE, "36": GRADE5_36_EXPANDED}
}

total_errors = 0

for g in range(1, 6):
    print(f"\n================ CHECKING GRADE {g} ================")
    official_core = set(yccd_all[str(g)]["core"].keys())
    official_mr = set(yccd_all[str(g)]["mr"].keys())
    print(f"Official QĐ 2422: Core={len(official_core)}, MR={len(official_mr)}, Total={len(official_core)+len(official_mr)}")
    
    # 1. Check 12-core plan
    plan12 = grades_data[g]["12"]
    if len(plan12) != 12:
        print(f"ERROR: 12-core plan has {len(plan12)} lessons instead of 12!")
        total_errors += 1
    
    # Extract YCCD in 12-core
    found_core_12 = set()
    for row in plan12:
        codes = re.findall(rf'{g}\.[A-D]\d\.\d+', row["ma_yccd"])
        for c in codes:
            found_core_12.add(c)
    
    missing_core_12 = official_core - found_core_12
    if missing_core_12:
        print(f"ERROR in 12-core plan: Missing Core YCCDs: {missing_core_12}")
        total_errors += 1
    else:
        print(f"SUCCESS: 12-core plan covers 100% Core YCCDs ({len(found_core_12)}/{len(official_core)})")
        
    # 2. Check 36-lesson plan
    plan36 = grades_data[g]["36"]
    if len(plan36) != 36:
        print(f"ERROR: 36-lesson plan has {len(plan36)} lessons instead of 36!")
        total_errors += 1
        
    core_lessons = [r for r in plan36 if r["phanloai"] == "Cốt lõi"]
    expanded_lessons = [r for r in plan36 if r["phanloai"] in ["Mở rộng", "Đánh giá quá trình"]]
    print(f"36-plan breakdown: Core lessons = {len(core_lessons)}, Expanded/Assessment = {len(expanded_lessons)}")
    
    found_core_36 = set()
    found_mr_36 = set()
    for row in plan36:
        core_c = re.findall(rf'{g}\.[A-D]\d\.\d+', row["ma_yccd"])
        mr_c = re.findall(rf'{g}\.[A-D]\d\.MR\d+', row["ma_yccd"])
        for c in core_c:
            found_core_36.add(c)
        for m in mr_c:
            found_mr_36.add(m)
            
    missing_core_36 = official_core - found_core_36
    missing_mr_36 = official_mr - found_mr_36
    
    if missing_core_36:
        print(f"ERROR in 36-plan: Missing Core YCCDs: {missing_core_36}")
        total_errors += 1
    else:
        print(f"SUCCESS: 36-plan covers 100% Core YCCDs ({len(found_core_36)}/{len(official_core)})")
        
    if missing_mr_36:
        print(f"ERROR in 36-plan: Missing MR YCCDs: {missing_mr_36}")
        total_errors += 1
    else:
        print(f"SUCCESS: 36-plan covers 100% MR YCCDs ({len(found_mr_36)}/{len(official_mr)})")

print(f"\n================ FINAL VERIFICATION RESULT ================")
if total_errors == 0:
    print("ALL 5 GRADES PASSED 100% VERIFICATION WITH 0 ERRORS!")
else:
    print(f"FAILED WITH {total_errors} ERRORS!")
