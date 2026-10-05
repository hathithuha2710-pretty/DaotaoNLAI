import sys
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.xlsx')
print("Sheets in workbook:", wb.sheetnames)

for sname in wb.sheetnames:
    ws = wb[sname]
    max_r = ws.max_row
    # count non-empty rows in column A
    rows_with_data = 0
    tiet_nums = []
    for r in range(1, max_r + 1):
        v = ws.cell(row=r, column=1).value
        if v is not None:
            v_str = str(v).strip()
            if v_str.isdigit():
                rows_with_data += 1
                tiet_nums.append(int(v_str))
    print(f"Sheet '{sname}': {rows_with_data} data rows (Tiết: {len(tiet_nums)} -> max={max(tiet_nums) if tiet_nums else 0})")
