import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md', 'r', encoding='utf-8') as f:
    text = f.read()

from extract_official_codes import official_core, official_mr

parts = re.split(r'## PHẦN [IVXLC]+\.\s+KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH AI - LỚP (\d)', text)

for i in range(1, len(parts), 2):
    grade = int(parts[i])
    content = parts[i+1]
    
    # 1. Core table
    core_part = content.split("### 2. Kế hoạch Giáo dục Toàn diện")[0]
    core_rows = [l for l in core_part.split('\n') if re.match(r'\|\s*\*\*\d+\*\*', l)]
    core_codes = set(re.findall(rf'\b{grade}\.[A-D][1-5]\.\d+\b', core_part))
    
    # 2. 36 lessons table
    full_part = content.split("### 2. Kế hoạch Giáo dục Toàn diện")[1]
    full_rows = [l for l in full_part.split('\n') if re.match(r'\|\s*\*\*\d+\*\*', l)]
    full_core_codes = set(re.findall(rf'\b{grade}\.[A-D][1-5]\.\d+\b', full_part))
    full_mr_codes = set(re.findall(rf'\b{grade}\.[A-D][1-5]\.MR\d+\b', full_part))
    
    expected_core = set(official_core[grade])
    expected_mr = set(official_mr[grade])
    
    print(f"=== LỚP {grade} ===")
    print(f"  [12 Tiết Cốt lõi]: {len(core_rows)} dòng (Kỳ vọng: 12)")
    print(f"    Mã Core đạt: {len(core_codes)}/{len(expected_core)}")
    missing_in_core = expected_core - core_codes
    if missing_in_core:
        print(f"    -> THIẾU MÃ TRONG 12 TIẾT: {missing_in_core}")
    else:
        print(f"    -> ĐẠT 100% YCCĐ CỐT LÕI (Zero-Omission)!")
        
    print(f"  [36 Tiết Cả năm]: {len(full_rows)} dòng (Kỳ vọng: 36)")
    print(f"    Mã Core đạt: {len(full_core_codes)}/{len(expected_core)}")
    print(f"    Mã MR đạt:   {len(full_mr_codes)}/{len(expected_mr)}")
    missing_core_full = expected_core - full_core_codes
    missing_mr_full = expected_mr - full_mr_codes
    if missing_core_full or missing_mr_full:
        print(f"    -> THIẾU TRONG BẢNG CẢ NĂM: Core={missing_core_full}, MR={missing_mr_full}")
    else:
        print(f"    -> ĐẠT 100% YCCĐ TOÀN DIỆN (Core + MR)!")
