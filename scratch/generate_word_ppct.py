# -*- coding: utf-8 -*-
"""
Script tạo file Word Phân phối chương trình Giáo dục AI Cấp Tiểu học (Lớp 1 - 5)
Chuẩn thể thức Công văn 2345/BGDĐT-GDTH, Nghị định 30/2020/NĐ-CP và Quyết định 2422/QĐ-BGDĐT.
"""
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

import json
import re

from ppct_data import GRADES_CONFIG
from lessons_grade1_v3 import GRADE1_12_CORE, GRADE1_36_EXPANDED
from lessons_grade2_v3 import GRADE2_12_CORE, GRADE2_36_EXPANDED
from lessons_grade3_v3 import GRADE3_12_CORE, GRADE3_36_EXPANDED
from lessons_grade4_v3 import GRADE4_12_CORE, GRADE4_36_EXPANDED
from lessons_grade5_v3 import GRADE5_12_CORE, GRADE5_36_EXPANDED

# Load external data
with open('scratch/yccd_all_grades.json', 'r', encoding='utf-8') as f:
    yccd_all = json.load(f)

with open('scratch/skills_46.json', 'r', encoding='utf-8') as f:
    skills_all = json.load(f)

doc = docx.Document()

# Setup Margins (Left 3.0cm, Right 1.5cm, Top 2.0cm, Bottom 2.0cm)
sections = doc.sections
for section in sections:
    section.top_margin = Inches(0.79)     # ~2.0 cm
    section.bottom_margin = Inches(0.79)  # ~2.0 cm
    section.left_margin = Inches(1.18)    # ~3.0 cm
    section.right_margin = Inches(0.59)   # ~1.5 cm
    section.page_width = Inches(8.27)     # A4
    section.page_height = Inches(11.69)

# Color Constants
HEX_NAVY = "1F4E78"
HEX_YELLOW = "FFF2CC"
HEX_BLUE = "D9E1F2"
HEX_GRAY = "F2F2F2"

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/><w:left w:val="none"/><w:right w:val="none"/><w:insideH w:val="single" w:sz="4" w:space="0" w:color="D9D9D9"/><w:insideV w:val="none"/></w:tblBorders>')
    tblPr.append(borders)

# Base Style Settings
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(11)
font.color.rgb = RGBColor(0x26, 0x26, 0x26)

# -------------------------------------------------------------
# TRANG BÌA & TIÊU NGỮ HÀNH CHÍNH (CHUẨN NĐ 30/2020 & CV 2345)
# -------------------------------------------------------------
p_header = doc.add_paragraph()
p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_h1 = p_header.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\n")
r_h1.font.bold = True
r_h1.font.size = Pt(11)
r_h1.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)

r_h2 = p_header.add_run("CHƯƠNG TRÌNH GIÁO DỤC TRÍ TUỆ NHÂN TẠO CHO HỌC SINH PHỔ THÔNG\n")
r_h2.font.bold = True
r_h2.font.size = Pt(12)

r_h3 = p_header.add_run("(Ban hành kèm theo Quyết định số 2422/QĐ-BGDĐT ngày 18/8/2026 của Bộ trưởng Bộ GD&ĐT)\n")
r_h3.font.italic = True
r_h3.font.size = Pt(10)
r_h3.font.color.rgb = RGBColor(0x59, 0x59, 0x59)

p_sep = doc.add_paragraph()
p_sep.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_sep = p_sep.add_run("—————————————")
r_sep.font.color.rgb = RGBColor(0xBF, 0xBF, 0xBF)

# Title
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(12)
p_title.paragraph_format.space_after = Pt(6)
r_title = p_title.add_run("KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH\nGIÁO DỤC TRÍ TUỆ NHÂN TẠO (AI) CẤP TIỂU HỌC\n(TỪ LỚP 1 ĐẾN LỚP 5)")
r_title.font.bold = True
r_title.font.size = Pt(15)
r_title.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)

# Subtitle
p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(18)
r_sub = p_sub.add_run("Đồng bộ tuyệt đối cùng Bảng Ma trận 46 Kỹ năng v2.0 và Khung Chuẩn đầu ra 123 YCCĐ\nBao phủ trọn vẹn Khung 12 tiết Cốt lõi bắt buộc và Khung 36 tiết Toàn diện cho trường 2 buổi/ngày")
r_sub.font.italic = True
r_sub.font.size = Pt(10.5)

# -------------------------------------------------------------
# PHẦN I: CĂN CỨ PHÁP LÝ VÀ NGUYÊN TẮC THIẾT KẾ
# -------------------------------------------------------------
p_p1 = doc.add_paragraph()
r_p1 = p_p1.add_run("PHẦN I. CĂN CỨ PHÁP LÝ VÀ QUY CHUẨN THIẾT KẾ")
r_p1.font.bold = True
r_p1.font.size = Pt(12)
r_p1.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)

bullets_p1 = [
    "Căn cứ pháp lý cao nhất (Single Source of Truth): Quyết định số 2422/QĐ-BGDĐT ngày 18/8/2026 của Bộ trưởng Bộ GD&ĐT ban hành 'Khung nội dung giáo dục Trí tuệ nhân tạo cho học sinh phổ thông'.",
    "Căn cứ triển khai thực tế: Công văn số 5588/BGDĐT-GDPT ngày 19/8/2026 của Bộ GD&ĐT hướng dẫn tổ chức thực hiện từ năm học 2026-2027.",
    "Căn cứ cấu trúc kế hoạch giáo dục: Công văn số 2345/BGDĐT-GDTH ngày 07/6/2021 của Bộ GD&ĐT về việc xây dựng kế hoạch giáo dục nhà trường cấp Tiểu học.",
    "Bảng tham chiếu năng lực cốt lõi: Bảng Ma trận phân bổ 46 kỹ năng giáo dục AI cấp Tiểu học (Lớp 1 – 5) phiên bản v2.0.",
    "Nguyên tắc 2 luồng thời lượng: (1) Khung 12 tiết Cốt lõi (VN-CORE) dành cho 100% học sinh, bảo đảm phủ kín 100% YCCĐ cốt lõi của Bộ; (2) Khung 36 tiết Toàn diện (12 Core + 24 Expanded) dành cho các trường dạy 2 buổi/ngày, câu lạc bộ, dự án liên môn và phủ kín 100% YCCĐ mở rộng (VN-MR).",
    "Nguyên tắc đánh giá (Mục VI QĐ 2422): Tuyệt đối không dùng bài thi trắc nghiệm hay chấm điểm số đơn thuần; đánh giá quá trình thường xuyên thông qua quan sát hành vi, nhận xét sản phẩm, hồ sơ minh chứng học tập (Portfolio) và triển lãm dự án."
]

for b in bullets_p1:
    bp = doc.add_paragraph(style='List Bullet')
    bp.paragraph_format.space_after = Pt(3)
    r = bp.add_run(b)
    r.font.size = Pt(10)

# -------------------------------------------------------------
# BẢNG TỔNG QUAN KIẾN TRÚC
# -------------------------------------------------------------
p_tbl_arch = doc.add_paragraph()
p_tbl_arch.paragraph_format.space_before = Pt(6)
r_ta = p_tbl_arch.add_run("Bảng 1: Tổng quan Kiến trúc và Phân bổ thời lượng cấp Tiểu học")
r_ta.font.bold = True
r_ta.font.size = Pt(10.5)

table_arch = doc.add_table(rows=6, cols=5)
table_arch.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(table_arch)

t_headers = ["Khối lớp", "Thời lượng / tiết", "Số lượng YCCĐ", "Cơ cấu tiết theo mạch (36 tiết)", "Đặc trưng sư phạm & Hạ tầng"]
col_widths_arch = [Inches(0.9), Inches(1.1), Inches(1.3), Inches(2.2), Inches(2.3)]

for col_idx, h in enumerate(t_headers):
    cell = table_arch.cell(0, col_idx)
    cell.text = h
    set_cell_shading(cell, HEX_NAVY)
    set_cell_margins(cell, 120, 120, 120, 120)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.runs[0]
    r.font.bold = True
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

arch_rows_data = [
    ["LỚP 1", "30–35 phút", "21 (17 Core + 4 MR)", "Mạch A (8t) + B (6t) + C (6t) + D (11t) + Đánh giá (5t)", "Trực quan, Unplugged 100% không dùng máy tính cá nhân, thẻ tranh"],
    ["LỚP 2", "30–35 phút", "29 (17 Core + 12 MR)", "Mạch A (9t) + B (7t) + C (6t) + D (9t) + Đánh giá (5t)", "AI gia đình, nhận diện dữ liệu, giáo viên demo trên máy chiếu"],
    ["LỚP 3", "35 phút", "32 (21 Core + 11 MR)", "Mạch A (11t) + B (5t) + C (6t) + D (9t) + Đánh giá (5t)", "AI trường học, bắt đầu thực hành phòng máy, Teachable Machine"],
    ["LỚP 4", "35 phút", "17 (10 Core + 7 MR)", "Mạch A (7t) + B (5t) + C (6t) + D (13t) + Đánh giá (5t)", "Sáng tạo cùng AI (AutoDraw), 4 bước học máy, dự án thực tiễn"],
    ["LỚP 5", "35 phút", "24 (15 Core + 9 MR)", "Mạch A (7t) + B (5t) + C (6t) + D (13t) + Đánh giá (5t)", "Thiết kế hệ thống, Trách nhiệm giải trình, Dự án AI tốt nghiệp"]
]

for row_idx, r_vals in enumerate(arch_rows_data, 1):
    for col_idx, val in enumerate(r_vals):
        cell = table_arch.cell(row_idx, col_idx)
        cell.text = val
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx < 3 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.runs[0]
        r.font.size = Pt(9)
        if col_idx == 0:
            r.font.bold = True
        if row_idx % 2 == 1:
            set_cell_shading(cell, HEX_GRAY)

# Set widths
for row in table_arch.rows:
    for i, w in enumerate(col_widths_arch):
        row.cells[i].width = w

# -------------------------------------------------------------
# HÀM TẠO BẢNG PPCT TRONG WORD
# -------------------------------------------------------------
def render_ppct_table(doc, title, subtitle, lessons_list, is_12_core=False):
    p_t = doc.add_paragraph()
    p_t.paragraph_format.space_before = Pt(14)
    p_t.paragraph_format.space_after = Pt(2)
    r_t = p_t.add_run(title)
    r_t.font.bold = True
    r_t.font.size = Pt(11)
    r_t.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(6)
    r_s = p_sub.add_run(subtitle)
    r_s.font.italic = True
    r_s.font.size = Pt(9)
    r_s.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
    
    table = doc.add_table(rows=len(lessons_list)+1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)
    
    headers = ["Tiết", "Tên bài học / Chuyên đề", "Nội dung trọng tâm & Kỹ năng tích hợp", "Mã YCCĐ"]
    col_widths = [Inches(0.6), Inches(2.2), Inches(3.8), Inches(1.2)]
    
    # Header Row
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        set_cell_shading(hdr_cells[i], HEX_NAVY)
        set_cell_margins(hdr_cells[i], 100, 100, 100, 100)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.runs[0]
        r.font.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    for r_idx, lesson in enumerate(lessons_list, 1):
        row_cells = table.rows[r_idx].cells
        row_cells[0].text = str(lesson["tiet"])
        row_cells[1].text = lesson["ten_bai"]
        row_cells[2].text = lesson["noidung"]
        row_cells[3].text = lesson["ma_yccd"]
        
        for c in row_cells:
            set_cell_margins(c, 70, 70, 80, 80)
            
        row_cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row_cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        row_cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        row_cells[3].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        row_cells[0].paragraphs[0].runs[0].font.bold = True
        row_cells[0].paragraphs[0].runs[0].font.size = Pt(9)
        
        row_cells[1].paragraphs[0].runs[0].font.bold = True
        row_cells[1].paragraphs[0].runs[0].font.size = Pt(9)
        
        row_cells[2].paragraphs[0].runs[0].font.size = Pt(8.5)
        
        if row_cells[3].paragraphs[0].runs:
            row_cells[3].paragraphs[0].runs[0].font.bold = True
            row_cells[3].paragraphs[0].runs[0].font.size = Pt(8.5)
            row_cells[3].paragraphs[0].runs[0].font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)
            
        # Shading
        if lesson["phanloai"] == "Cốt lõi":
            for c in row_cells:
                set_cell_shading(c, HEX_YELLOW)
        elif lesson["phanloai"] == "Đánh giá quá trình":
            for c in row_cells:
                set_cell_shading(c, HEX_BLUE)

    for row in table.rows:
        for i, w in enumerate(col_widths):
            row.cells[i].width = w

# -------------------------------------------------------------
# PHẦN II ĐẾN PHẦN VI: KẾ HOẠCH BÀI DẠY CHO 5 KHỐI LỚP
# -------------------------------------------------------------
grades_dict = {
    1: {"cfg": GRADES_CONFIG[1], "12": GRADE1_12_CORE, "36": GRADE1_36_EXPANDED},
    2: {"cfg": GRADES_CONFIG[2], "12": GRADE2_12_CORE, "36": GRADE2_36_EXPANDED},
    3: {"cfg": GRADES_CONFIG[3], "12": GRADE3_12_CORE, "36": GRADE3_36_EXPANDED},
    4: {"cfg": GRADES_CONFIG[4], "12": GRADE4_12_CORE, "36": GRADE4_36_EXPANDED},
    5: {"cfg": GRADES_CONFIG[5], "12": GRADE5_12_CORE, "36": GRADE5_36_EXPANDED}
}

roman_parts = {1: "PHẦN II", 2: "PHẦN III", 3: "PHẦN IV", 4: "PHẦN V", 5: "PHẦN VI"}

for g in range(1, 6):
    doc.add_page_break()
    g_info = grades_dict[g]
    cfg = g_info["cfg"]
    
    p_sec = doc.add_paragraph()
    r_sec = p_sec.add_run(f"{roman_parts[g]}. KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH AI - LỚP {g}")
    r_sec.font.bold = True
    r_sec.font.size = Pt(13)
    r_sec.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)
    
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(4)
    r_m = p_meta.add_run(f"• Thời lượng chuẩn: {cfg['duration']} | Tổng số YCCĐ: {cfg['total_yccd']} ({cfg['core_count']} Cốt lõi + {cfg['mr_count']} Mở rộng)\n"
                         f"• Đặc trưng sư phạm: {cfg['pedagogy']}\n"
                         f"• Phương thức đánh giá: {cfg['assessment']}")
    r_m.font.size = Pt(9.5)
    r_m.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    # 1. Bảng 12 tiết Cốt lõi
    t12 = f"1. Khung Chuyên đề Giáo dục AI Bắt buộc - Lớp {g} (12 tiết Cốt lõi)"
    sub12 = f"Bao phủ trọn vẹn 100% {cfg['core_count']} YCCĐ Cốt lõi theo QĐ 2422 | Bắt buộc đối với 100% học sinh"
    render_ppct_table(doc, t12, sub12, g_info["12"], is_12_core=True)
    
    # 2. Bảng 36 tiết Toàn diện
    t36 = f"2. Kế hoạch Giáo dục Toàn diện môn AI - Lớp {g} (36 tiết/năm học)"
    sub36 = f"Gồm 12 tiết Cốt lõi (tô vàng) + 24 tiết Mở rộng/Đánh giá (nền trắng/xanh) | Phủ kín 100% YCCĐ Cốt lõi & Mở rộng"
    render_ppct_table(doc, t36, sub36, g_info["36"], is_12_core=False)

# -------------------------------------------------------------
# PHẦN VII: HƯỚNG DẪN THỰC HIỆN VÀ ĐÁNH GIÁ HỌC SINH (MỤC VI)
# -------------------------------------------------------------
doc.add_page_break()
p_guide = doc.add_paragraph()
r_g = p_guide.add_run("PHẦN VII. HƯỚNG DẪN THỰC HIỆN VÀ ĐÁNH GIÁ QUÁ TRÌNH (MỤC VI QĐ 2422)")
r_g.font.bold = True
r_g.font.size = Pt(13)
r_g.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)

guide_paragraphs = [
    ("1. Hướng dẫn tổ chức dạy học linh hoạt theo điều kiện nhà trường:",
     "• Đối với các trường có phòng máy tính kết nối Internet: Triển khai kết hợp hài hòa giữa hoạt động trải nghiệm không máy tính (Unplugged) và thực hành trực tiếp trên các nền tảng mở như Google Teachable Machine, AutoDraw, Scratch AI.\n"
     "• Đối với các trường vùng khó khăn, thiếu thiết bị: 100% các tiết Cốt lõi (12 CORE) đều đã được thiết kế sẵn phương án mô phỏng bằng thẻ tranh, đóng vai, mô hình giấy và sơ đồ khối, bảo đảm học sinh vẫn đạt chuẩn YCCĐ của Bộ GD&ĐT mà không bị phụ thuộc vào máy móc cá nhân."),
    
    ("2. Quy chuẩn đánh giá quá trình và kiểm định chất lượng (Mục VI QĐ 2422):",
     "• Hình thức đánh giá: Đánh giá thường xuyên trong từng tiết học kết hợp đánh giá định kỳ qua hồ sơ học tập (Portfolio), sản phẩm dự án sáng tạo và các buổi triển lãm ngày hội STEM-AI.\n"
     "• Công cụ đánh giá: Sử dụng Bảng kiểm hành vi (Checklist), Thang đo quan sát (Rating Scale) và Phiếu đánh giá theo tiêu chí (Rubric) được lượng hóa trực tiếp từ Bảng Ma trận 46 Kỹ năng v2.0.\n"
     "• Tuyệt đối không tổ chức thi trắc nghiệm lý thuyết, không cho điểm số đơn thuần; chỉ dùng nhận xét đánh giá sự tiến bộ, tính tự chủ và trách nhiệm đạo đức số của học sinh."),
     
    ("3. Trách nhiệm giải trình và liêm chính học thuật trong nhà trường:",
     "• Khẳng định nguyên tắc con người làm chủ: Học sinh phải luôn là chủ thể tư duy; AI chỉ đóng vai trò trợ lý khơi gợi cảm hứng và hỗ trợ kỹ thuật.\n"
     "• Rèn luyện thói quen kiểm chứng nguồn tin (chống ảo giác AI), minh bạch tác quyền khi sử dụng sản phẩm do AI hỗ trợ và bảo vệ tuyệt đối dữ liệu cá nhân trên môi trường mạng.")
]

for title, body in guide_paragraphs:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(title + "\n")
    r1.font.bold = True
    r1.font.size = Pt(10.5)
    r2 = p.add_run(body)
    r2.font.size = Pt(10)

word_out = '03_San_Pham_Chinh_Thuc/Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_QD2422.docx'
doc.save(word_out)
print(f"Generated Word document successfully at: {word_out}")
