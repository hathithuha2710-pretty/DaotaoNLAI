import sys
sys.stdout.reconfigure(encoding='utf-8')

new_matrix_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(new_matrix_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line_no in [10, 100, 120, 152]:
    print(f"=== Line {line_no} ===")
    print(lines[line_no - 1])
    print()
