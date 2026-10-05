import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Output directory
output_dir = r"c:\Users\USER\Desktop\AI-vibe-code\KhungNLĐTAI\03_San_Pham_Chinh_Thuc"
os.makedirs(output_dir, exist_ok=True)

data = [
    # Nhóm I
    ("I", "NHÓM 1: GIAO TIẾP VỚI THIẾT BỊ VÀ PHẦN MỀM THÔNG MINH", "", "", "", "", "", "GROUP_HEADER"),
    ("1", "Nhận biết biểu tượng thông minh", "X", "X", "X", "", "", "Dạy nền tảng ở L1–L3; lên L4–L5 các em đã quen thuộc."),
    ("2", "Nói câu lệnh rõ ràng", "X", "X", "X", "X", "X", "Rèn xuyên suốt cả 5 lớp (tập phát âm to, tròn vành rõ chữ)."),
    ("3", "Nêu rõ điều mình muốn nhờ máy", "", "X", "X", "X", "X", "Lớp 1 chỉ nghe lệnh mẫu; từ L2 bắt đầu tự diễn đạt yêu cầu."),
    ("4", "Nói lại khi máy chưa hiểu", "", "X", "X", "X", "X", "Tập phản xạ điều chỉnh câu nói khi trợ lý ảo không nghe rõ."),
    # Nhóm II
    ("II", "NHÓM 2: AN TOÀN SỐ VÀ TỰ BẢO VỆ", "", "", "", "", "", "GROUP_HEADER"),
    ("5", "Giữ kín thông tin riêng tư", "X", "X", "X", "X", "X", "Kỹ năng sinh tồn số, bắt buộc nhắc lại và rèn cả 5 năm học."),
    ("6", "Từ chối khi bị hỏi thông tin", "X", "X", "X", "X", "X", "Rèn phản xạ dứt khoát nói \"KHÔNG\" trước các ứng dụng lạ."),
    ("7", "Cảnh giác với hình ảnh và giọng nói giả", "", "X", "X", "X", "X", "Từ L2 bắt đầu cho xem ví dụ ảnh ghép; L3–L5 học cảnh giác sâu."),
    ("8", "Báo ngay cho người lớn khi gặp sự cố", "X", "X", "X", "X", "X", "Nguyên tắc bảo vệ an toàn cốt lõi, thực hành xuyên suốt."),
    ("9", "Cân bằng giờ dùng máy", "X", "X", "X", "X", "X", "Rèn thói quen rời màn hình đúng giờ, bảo vệ mắt và sức khỏe."),
    # Nhóm III
    ("III", "NHÓM 3: TƯ DUY PHÂN BIỆT VÀ KIỂM CHỨNG CỤ THỂ", "", "", "", "", "", "GROUP_HEADER"),
    ("10", "Phân biệt người thật và máy móc", "X", "X", "X", "", "", "Trọng tâm L1–L3 để chống nhân hóa AI; lên L4–L5 đã hiểu rõ."),
    ("11", "Phân biệt đồ dùng cơ và đồ dùng thông minh", "X", "X", "", "", "", "Dạy trực quan ở L1–L2 (quạt cơ vs quạt cảm biến); L3–L5 không cần dạy lại."),
    ("12", "Phân biệt đồ dùng làm một việc và nhiều việc", "X", "X", "", "", "", "Dạy nhận biết ở L1–L2 (cân điện tử vs điện thoại); L3–L5 không cần lặp lại."),
    ("13", "So sánh cách học của người và máy", "", "X", "X", "X", "X", "Bắt đầu từ L2 (người học qua trải nghiệm, máy học qua ảnh)."),
    ("14", "Nhận ra máy có thể nhìn nhầm", "", "X", "X", "X", "X", "L2 thấy máy nhầm bóng cam/quả cam; L3–L5 mổ xẻ khi máy đoán sai."),
    ("15", "Không tin tuyệt đối vào máy (Kiểm chứng)", "", "", "X", "X", "X", "Từ L3 trẻ đọc viết thạo mới biết mở SGK ra đối chiếu kiểm tra."),
    # Nhóm IV
    ("IV", "NHÓM 4: KHÁM PHÁ DỮ LIỆU VÀ CÁCH DẠY MÁY HỌC", "", "", "", "", "", "GROUP_HEADER"),
    ("16", "Hiểu giác quan của máy (Cam = mắt, Mic = tai)", "X", "X", "X", "", "", "Ẩn dụ trực quan cho L1–L3; lên L4–L5 các em đã nắm vững."),
    ("17", "Hiểu máy học từ ví dụ mẫu", "X", "X", "X", "X", "X", "L1 xem tranh mèo; L2–L5 phát triển thành bài học về dữ liệu."),
    ("18", "Cùng chọn ví dụ rõ nét để dạy máy", "", "X", "X", "X", "X", "Từ L2 tập chọn ảnh rõ bỏ ảnh mờ; L3–L5 thực hành sâu hơn."),
    ("19", "Nhận ra máy có thể nghe nhầm tiếng vùng miền", "", "X", "X", "X", "X", "Làm quen từ L2; L3–L5 hiểu nguyên nhân do dữ liệu thiếu giọng địa phương."),
    ("20", "Quan sát quy trình dạy máy cùng thầy cô", "", "", "X", "X", "X", "Từ L3 mới bắt đầu tiếp cận quy trình trên phần mềm học máy."),
    # Nhóm V
    ("V", "NHÓM 5: SÁNG TẠO Ý TƯỞNG VÀ LẬP TRÌNH ĐƠN GIẢN", "", "", "", "", "", "GROUP_HEADER"),
    ("21", "Phát hiện việc vất vả cần máy giúp", "X", "X", "X", "X", "X", "Khơi gợi quan sát từ việc nhà (L1–L2) đến việc trường lớp, xã hội (L3–L5)."),
    ("22", "Vẽ tranh hoặc kể chuyện về robot mơ ước", "X", "X", "X", "", "", "Hình thức trực quan phù hợp L1–L3; lên L4–L5 chuyển sang dự án thực tế."),
    ("23", "Đóng góp dữ liệu cho dự án chung của lớp", "", "", "X", "X", "X", "Từ L3 học sinh mới có bài tập nhóm cùng góp ảnh, đồ vật dạy máy."),
    ("24", "Dùng lệnh \"Nếu... thì...\" để điều khiển nhân vật", "", "", "X", "X", "X", "Khớp với môn Tin học L3–L5 (bắt đầu học kéo thả Scratch/Blockly)."),
    ("25", "Nhờ máy gợi ý ý tưởng học tập", "", "", "X", "X", "X", "Từ L3 khi bắt đầu làm bài văn, vẽ tranh đề tài mới cần AI gợi ý."),
    # Nhóm VI
    ("VI", "NHÓM 6: THÁI ĐỘ ĐẠO ĐỨC VÀ TỰ CHỊU TRÁCH NHIỆM", "", "", "", "", "", "GROUP_HEADER"),
    ("26", "Không dùng máy làm phiền người khác", "X", "X", "X", "X", "X", "Quy tắc đạo đức cốt lõi, nhắc nhở và rèn luyện cả 5 năm học."),
    ("27", "Hỏi xin phép trước khi mượn đồ", "X", "X", "X", "X", "X", "Xác lập ranh giới \"của bạn và của tớ\", rèn nếp sống văn minh."),
    ("28", "Trung thực về sản phẩm của máy", "", "X", "X", "X", "X", "Từ L2 bắt đầu dán nhãn \"AI vẽ\"; L3–L5 rèn thói quen trung thực học tập."),
    ("29", "Tự giác suy nghĩ trước khi nhờ máy", "", "", "X", "X", "X", "Từ L3 có nhiều bài tập về nhà hơn, phải rèn kiên quyết chống ỷ lại."),
    ("30", "Tự làm tự chịu, không đổ lỗi cho máy", "X", "X", "X", "X", "X", "Trách nhiệm giải trình phiên bản trẻ thơ, giáo dục xuyên suốt 5 năm.")
]

# ----------------- 1. EXPORT EXCEL -----------------
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Ma Tran Ky Nang AI Tieu Hoc"

# Title block
ws.merge_cells("A1:H1")
ws["A1"] = "BẢNG MA TRẬN PHÂN BỔ KỸ NĂNG GIÁO DỤC AI CẤP TIỂU HỌC (LỚP 1 – 5)"
ws["A1"].font = Font(name="Calibri", size=16, bold=True, color="1F497D")
ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[1].height = 35

ws.merge_cells("A2:H2")
ws["A2"] = "Căn cứ pháp lý: Quyết định số 2422/QĐ-BGDĐT | Chuẩn hóa theo Thang Bloom & Khung UNESCO AI 2024"
ws["A2"].font = Font(name="Calibri", size=11, italic=True, color="595959")
ws["A2"].alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[2].height = 20

# Header
headers = ["STT", "Tên kỹ năng chuẩn hóa", "Lớp 1", "Lớp 2", "Lớp 3", "Lớp 4", "Lớp 5", "Định hướng sư phạm theo lứa tuổi"]
ws.append([]) # Row 3 blank
ws.append(headers) # Row 4
ws.row_dimensions[4].height = 28

header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
thin_border = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

for col_num in range(1, 9):
    cell = ws.cell(row=4, column=col_num)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

# Data Rows
current_row = 5
group_fill = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
group_font = Font(name="Calibri", size=11, bold=True, color="1F497D")
x_font = Font(name="Calibri", size=12, bold=True, color="C00000")
regular_font = Font(name="Calibri", size=10, color="000000")

for item in data:
    stt, name, l1, l2, l3, l4, l5, note = item
    if note == "GROUP_HEADER":
        ws.merge_cells(start_row=current_row, start_column=2, end_row=current_row, end_column=8)
        cell_stt = ws.cell(row=current_row, column=1, value=stt)
        cell_name = ws.cell(row=current_row, column=2, value=name)
        cell_stt.fill = group_fill
        cell_stt.font = group_font
        cell_stt.alignment = Alignment(horizontal="center", vertical="center")
        cell_name.fill = group_fill
        cell_name.font = group_font
        cell_name.alignment = Alignment(horizontal="left", vertical="center")
        ws.row_dimensions[current_row].height = 24
    else:
        ws.cell(row=current_row, column=1, value=int(stt))
        ws.cell(row=current_row, column=2, value=name)
        ws.cell(row=current_row, column=3, value=l1)
        ws.cell(row=current_row, column=4, value=l2)
        ws.cell(row=current_row, column=5, value=l3)
        ws.cell(row=current_row, column=6, value=l4)
        ws.cell(row=current_row, column=7, value=l5)
        ws.cell(row=current_row, column=8, value=note)
        
        ws.cell(row=current_row, column=1).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=current_row, column=2).alignment = Alignment(horizontal="left", vertical="center")
        for c in range(3, 8):
            cell = ws.cell(row=current_row, column=c)
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if cell.value == "X":
                cell.font = x_font
        ws.cell(row=current_row, column=8).alignment = Alignment(horizontal="left", vertical="center")
        ws.row_dimensions[current_row].height = 22

    for col_num in range(1, 9):
        ws.cell(row=current_row, column=col_num).border = thin_border
    current_row += 1

# Column widths
ws.column_dimensions['A'].width = 8
ws.column_dimensions['B'].width = 46
ws.column_dimensions['C'].width = 10
ws.column_dimensions['D'].width = 10
ws.column_dimensions['E'].width = 10
ws.column_dimensions['F'].width = 10
ws.column_dimensions['G'].width = 10
ws.column_dimensions['H'].width = 65

import sys
sys.stdout.reconfigure(encoding='utf-8')
excel_path = os.path.join(output_dir, "Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5.xlsx")
wb.save(excel_path)
print("Saved Excel successfully!")

# ----------------- 2. EXPORT WORD (DOCX) -----------------
doc = docx.Document()

# Set landscape or wide margins
sections = doc.sections
for section in sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

# Title
title_p = doc.add_paragraph()
title_run = title_p.add_run("BẢNG MA TRẬN PHÂN BỔ KỸ NĂNG GIÁO DỤC AI CẤP TIỂU HỌC (LỚP 1 – 5)")
title_run.font.name = "Calibri"
title_run.font.size = Pt(16)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

sub_p = doc.add_paragraph()
sub_run = sub_p.add_run("Căn cứ pháp lý: Quyết định số 2422/QĐ-BGDĐT | Chuẩn hóa theo Thang Bloom & Khung UNESCO AI 2024\nPhù hợp điều kiện thực tế lớp học Việt Nam (sĩ số 40–50 học sinh, GV thị phạm + tương tác)")
sub_run.font.name = "Calibri"
sub_run.font.size = Pt(10.5)
sub_run.font.italic = True
sub_run.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph() # Spacing

# Table
table = doc.add_table(rows=1, cols=8)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.autofit = False

col_widths = [Inches(0.5), Inches(2.2), Inches(0.55), Inches(0.55), Inches(0.55), Inches(0.55), Inches(0.55), Inches(2.6)]

# Format header
hdr_cells = table.rows[0].cells
headers = ["STT", "Tên kỹ năng chuẩn hóa", "L1", "L2", "L3", "L4", "L5", "Định hướng sư phạm theo lứa tuổi"]

for idx, text in enumerate(headers):
    hdr_cells[idx].text = text
    hdr_cells[idx].width = col_widths[idx]
    p = hdr_cells[idx].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="1F497D"/>')
    hdr_cells[idx]._tc.get_or_add_tcPr().append(shd)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    for child in tcPr:
        if child.tag.endswith('shd'):
            tcPr.remove(child)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

# Add data rows
for item in data:
    stt, name, l1, l2, l3, l4, l5, note = item
    row_cells = table.add_row().cells
    for i in range(8):
        row_cells[i].width = col_widths[i]

    if note == "GROUP_HEADER":
        # Group header row
        # merge cells 1 to 7 (i.e. col 2 to 8)
        row_cells[0].text = stt
        p0 = row_cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.runs[0]
        r0.font.name = "Calibri"
        r0.font.bold = True
        r0.font.size = Pt(10)
        r0.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

        # Merge remaining
        a = row_cells[1]
        b = row_cells[7]
        a.merge(b)
        a.text = name
        pa = a.paragraphs[0]
        pa.alignment = WD_ALIGN_PARAGRAPH.LEFT
        ra = pa.runs[0]
        ra.font.name = "Calibri"
        ra.font.bold = True
        ra.font.size = Pt(10)
        ra.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

        set_cell_background(row_cells[0], "DCE6F1")
        set_cell_background(a, "DCE6F1")
    else:
        row_cells[0].text = stt
        p0 = row_cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.runs[0].font.name = "Calibri"
        p0.runs[0].font.size = Pt(9.5)

        row_cells[1].text = name
        p1 = row_cells[1].paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p1.runs[0].font.name = "Calibri"
        p1.runs[0].font.size = Pt(9.5)

        levels = [l1, l2, l3, l4, l5]
        for idx_l, val in enumerate(levels):
            cell_idx = idx_l + 2
            row_cells[cell_idx].text = val
            pl = row_cells[cell_idx].paragraphs[0]
            pl.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if len(pl.runs) > 0:
                pl.runs[0].font.name = "Calibri"
                pl.runs[0].font.size = Pt(10)
                pl.runs[0].font.bold = True
                pl.runs[0].font.color.rgb = RGBColor(0xC0, 0x00, 0x00)

        row_cells[7].text = note
        p7 = row_cells[7].paragraphs[0]
        p7.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p7.runs[0].font.name = "Calibri"
        p7.runs[0].font.size = Pt(9)
        p7.runs[0].font.italic = True

# Add Summary block
doc.add_paragraph()
sum_h = doc.add_paragraph()
sum_hrun = sum_h.add_run("TỔNG KẾT TIẾN TRÌNH SƯ PHẠM BÁO CÁO LÃNH ĐẠO:")
sum_hrun.font.name = "Calibri"
sum_hrun.font.bold = True
sum_hrun.font.size = Pt(11)
sum_hrun.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

p_sum1 = doc.add_paragraph(style='List Bullet')
r1 = p_sum1.add_run("Nhóm kỹ năng rèn luyện xuyên suốt cả 5 khối lớp (13 kỹ năng): ")
r1.bold = True
p_sum1.add_run("Tập trung vào An toàn số (KN 5, 6, 8, 9) và Đạo đức, trách nhiệm cốt lõi (KN 2, 17, 21, 26, 27, 30). Đây là nền tảng sinh tồn và nhân cách số cần được nhắc nhở, củng cố liên tục hàng năm.")

p_sum2 = doc.add_paragraph(style='List Bullet')
r2 = p_sum2.add_run("Nhóm kỹ năng hoàn thành ở các lớp đầu cấp L1–L3 (5 kỹ năng): ")
r2.bold = True
p_sum2.add_run("Bao gồm các kỹ năng trực quan sơ khởi (KN 1, 10, 11, 12, 16, 22). Lên Lớp 4–5 các em đã hình thành tự nhiên, không cần tốn thời lượng dạy lại, giúp tinh gọn chương trình.")

p_sum3 = doc.add_paragraph(style='List Bullet')
r3 = p_sum3.add_run("Nhóm kỹ năng phát triển từ Lớp 3 trở lên (8 kỹ năng): ")
r3.bold = True
p_sum3.add_run("Đòi hỏi năng lực đọc viết thành thạo và tư duy logic: kiểm chứng SGK (KN 15), quan sát quy trình dạy máy (KN 20), đóng góp dữ liệu dự án (KN 23), lập trình khối lệnh Scratch (KN 24), kiên quyết chống ỷ lại (KN 29).")

docx_path = os.path.join(output_dir, "Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5.docx")
doc.save(docx_path)
print("Saved Word successfully!")
