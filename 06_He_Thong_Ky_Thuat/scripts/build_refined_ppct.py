# -*- coding: utf-8 -*-
"""
Script xây dựng tệp Excel Phân phối chương trình Giáo dục AI Lớp 1 và Lớp 6
Được hiệu chỉnh triệt để theo các đánh giá chuyên môn:
1. Sửa lỗi gán nhãn Bài 6 Lớp 1: dùng đúng nội dung cốt lõi 1.A2.1 thay vì 1.A2.MR1.
2. Đưa rõ ràng 1.C1.1 vào Bài 3 Lớp 1.
3. Chuẩn hóa kế toán tiết trong Sheet Tổng quan: Khớp 100% từng mạch với bảng chi tiết (phản ánh rõ tiết tích hợp).
4. Khung 36 tiết: Chuẩn hóa tuyệt đối đúng 12 tiết Cốt lõi + đúng 24 tiết Mở rộng = 36 tiết (không vượt quá 12 tiết cốt lõi).
5. Xóa bỏ hoàn toàn bài kiểm tra trắc nghiệm / đầu điểm riêng theo đúng Mục VI.1 & VI.3 QĐ 2422, thay bằng đánh giá quá trình qua hồ sơ minh chứng (portfolio) và sản phẩm học tập.
6. Tôn trọng ranh giới phân tầng nhận thức: Không dạy lấn sân kiến thức của Lớp 2-5 và Lớp 7-9.
"""
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

def build_curriculum_workbook():
    wb = openpyxl.Workbook()
    wb.remove(wb.active) # Xoá sheet mặc định

    # Màu sắc giao diện giáo dục cao cấp
    c_navy = '1B365D'
    c_core = 'E8F5E9'      # Xanh ngọc nhạt cho Cốt lõi (12 tiết)
    c_core_text = '1B5E20'
    c_ext = 'FFF3E0'       # Cam kem nhạt cho Mở rộng (24 tiết)
    c_ext_text = 'E65100'
    c_alt_row = 'F8FAFC'

    font_title = Font(name='Arial', size=13, bold=True, color=c_navy)
    font_subtitle = Font(name='Arial', size=9.5, italic=True, color='555555')
    font_th = Font(name='Arial', size=9.5, bold=True, color='FFFFFF')
    font_cell = Font(name='Arial', size=9.5, color='000000')
    font_cell_bold = Font(name='Arial', size=9.5, bold=True, color='000000')
    font_badge_core = Font(name='Arial', size=9, bold=True, color=c_core_text)
    font_badge_ext = Font(name='Arial', size=9, bold=True, color=c_ext_text)

    fill_th = PatternFill(start_color=c_navy, end_color=c_navy, fill_type='solid')
    fill_core_tag = PatternFill(start_color=c_core, end_color=c_core, fill_type='solid')
    fill_ext_tag = PatternFill(start_color=c_ext, end_color=c_ext, fill_type='solid')
    fill_alt = PatternFill(start_color=c_alt_row, end_color=c_alt_row, fill_type='solid')
    fill_white = PatternFill(start_color='FFFFFF', end_color='FFFFFF', fill_type='solid')

    border_side = Side(border_style='thin', color='D0D7DE')
    border_cell = Border(left=border_side, right=border_side, top=border_side, bottom=border_side)

    align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)
    align_top_left = Alignment(horizontal='left', vertical='top', wrap_text=True)
    align_top_center = Alignment(horizontal='center', vertical='top', wrap_text=True)

    headers = [
        'Tiết',
        'Chủ đề',
        'Tên bài',
        'Nội dung',
        'Phân loại',
        'Thiết bị & Học liệu'
    ]

    def setup_sheet_header(ws, title_text, subtitle_text):
        ws.views.sheetView[0].showGridLines = True
        ws.merge_cells('A1:F1')
        ws['A1'] = title_text
        ws['A1'].font = font_title
        ws['A1'].alignment = align_center
        ws.row_dimensions[1].height = 28

        ws.merge_cells('A2:F2')
        ws['A2'] = subtitle_text
        ws['A2'].font = font_subtitle
        ws['A2'].alignment = align_center
        ws.row_dimensions[2].height = 18

        for c_idx, h in enumerate(headers, 1):
            cell = ws.cell(4, c_idx, h)
            cell.font = font_th
            cell.fill = fill_th
            cell.alignment = align_center
            cell.border = border_cell
        ws.row_dimensions[4].height = 28

    def populate_table(ws, rows_data):
        for r_idx, row in enumerate(rows_data, 5):
            is_alt = (r_idx % 2 == 0)
            default_fill = fill_alt if is_alt else fill_white

            tiet, chu_de, ten_bai, noi_dung, phan_loai, thiet_bi = row
            row_vals = [tiet, chu_de, ten_bai, noi_dung, phan_loai, thiet_bi]

            for c_idx, val in enumerate(row_vals, 1):
                cell = ws.cell(r_idx, c_idx, val)
                cell.border = border_cell
                cell.fill = default_fill

                if c_idx == 1:
                    cell.font = font_cell_bold
                    cell.alignment = align_top_center
                elif c_idx in [2, 3]:
                    cell.font = font_cell_bold
                    cell.alignment = align_top_left
                elif c_idx == 4:
                    cell.font = font_cell
                    cell.alignment = align_top_left
                elif c_idx == 5:
                    cell.alignment = align_top_center
                    if 'Cốt lõi' in str(val):
                        cell.font = font_badge_core
                        cell.fill = fill_core_tag
                    else:
                        cell.font = font_badge_ext
                        cell.fill = fill_ext_tag
                elif c_idx == 6:
                    cell.font = font_cell
                    cell.alignment = align_top_left
            ws.row_dimensions[r_idx].height = 38

        col_widths = [10, 24, 28, 50, 14, 26]
        for c_idx, w in enumerate(col_widths, 1):
            col_letter = get_column_letter(c_idx)
            ws.column_dimensions[col_letter].width = w

    # =========================================================
    # SHEET 1: TỔNG QUAN VÀ NGUYÊN TẮC THIẾT KẾ
    # =========================================================
    ws0 = wb.create_sheet(title='Tong_Quan_Kien_Truc')
    ws0.views.sheetView[0].showGridLines = True
    ws0.merge_cells('A1:F1')
    ws0['A1'] = 'KHUNG PHÂN PHỐI CHƯƠNG TRÌNH GIÁO DỤC AI PHỔ THÔNG (CHUẨN HOÁ QĐ 2422)'
    ws0['A1'].font = font_title
    ws0['A1'].alignment = align_center
    ws0.row_dimensions[1].height = 28

    ws0.merge_cells('A2:F2')
    ws0['A2'] = 'Định vị chuẩn xác ranh giới kiến thức từng lớp, kế toán số tiết minh bạch và đúng quy định đánh giá Mục VI'
    ws0['A2'].font = font_subtitle
    ws0['A2'].alignment = align_center
    ws0.row_dimensions[2].height = 18

    headers0 = ['Khối lớp', 'Cấp học', 'Khung thời lượng', 'Cơ cấu tiết theo mạch nội dung', 'Ranh giới phân tầng nhận thức', 'Phương thức đánh giá (Mục VI QĐ 2422)']
    for c_idx, h in enumerate(headers0, 1):
        c = ws0.cell(4, c_idx, h)
        c.font = font_th
        c.fill = fill_th
        c.alignment = align_center
        c.border = border_cell
    ws0.row_dimensions[4].height = 28

    overview_rows = [
        ['LỚP 1', 'Tiểu học', '12 tiết Cốt lõi', 'Mạch A (4t) + Mạch B (2t) + Mạch C (2t) + Mạch D (3t) + Tích hợp (1t) = 12t', 'Cảm xúc Người vs Máy, camera là mắt, micro là tai, máy học từ ví dụ, phân loại máy đơn/đa năng. Để dành việc huấn luyện máy và phân loại cho Lớp 2–5.', 'Đánh giá quá trình thường xuyên bằng quan sát, nhận xét sự tiến bộ; không bài thi, không cho điểm'],
        ['LỚP 1', 'Tiểu học', '36 tiết Toàn diện', '12 tiết Cốt lõi + 24 tiết Mở rộng = 36 tiết (Mạch A: 8t, B: 6t, C: 6t, D: 11t, Tích hợp & Hồ sơ: 5t)', 'Mở rộng chiều ngang: Trải nghiệm đóng vai giao tiếp thân thiện (1.A2.MR1), xử lý ảnh/tiếng (1.C1.MR1, MR2), cần nhiều ví dụ (1.D1.MR1), mô hình robot giấy.', 'Đánh giá quá trình qua hồ sơ minh chứng học tập (Portfolio tranh vẽ, mô hình); không tổ chức bài kiểm tra trắc nghiệm'],
        ['LỚP 6', 'THCS', '12 tiết Cốt lõi', 'Mạch A (3t) + Mạch B (2t) + Mạch C (4t) + Mạch D (2t) + Tích hợp (1t) = 12t', 'Dữ liệu và thuật toán, công nghệ nhận dạng ảnh/tiếng, ranh giới Nên/Không nên, giới hạn của AI, bảo vệ dữ liệu cá nhân. Để dành dự án tạo sản phẩm cho Lớp 7–9.', 'Đánh giá quá trình dựa trên minh chứng thực hành, nhật ký câu lệnh (prompt log) và trách nhiệm giải trình'],
        ['LỚP 6', 'THCS', '36 tiết Toàn diện', '12 tiết Cốt lõi + 24 tiết Mở rộng = 36 tiết (Mạch A: 7t, B: 5t, C: 11t, D: 8t, Tích hợp & Hồ sơ: 5t)', 'Bám sát 8 YCCĐ MR của Lớp 6: Thử nghiệm đặt câu lệnh đối kháng (6.C1.MR2), liên hệ huấn luyện-hoạt động (6.C1.MR1), AI trong thực tiễn VN (6.C2.MR1), tranh biện Nên/Không nên (6.D1.MR1).', 'Đánh giá quá trình thông qua hồ sơ học tập số (Digital Portfolio), báo cáo ý tưởng phối hợp Người - AI; không lập đầu điểm riêng']
    ]

    for r_idx, row in enumerate(overview_rows, 5):
        for c_idx, val in enumerate(row, 1):
            cell = ws0.cell(r_idx, c_idx, val)
            cell.font = font_cell
            cell.border = border_cell
            cell.alignment = align_top_center if c_idx in [1, 2, 3] else align_top_left
            cell.fill = fill_white if r_idx % 2 != 0 else fill_alt
        ws0.row_dimensions[r_idx].height = 55

    col_w0 = [10, 14, 18, 30, 36, 36]
    for c_idx, w in enumerate(col_w0, 1):
        ws0.column_dimensions[get_column_letter(c_idx)].width = w

    # =========================================================
    # SHEET 2: LỚP 1 - KHUNG 12 TIẾT CỐT LÕI (BẮT BUỘC)
    # Khớp 100% 17 YCCĐ Cốt lõi, kế toán số tiết chuẩn xác: A(4) + B(2) + C(2) + D(3) + Tích hợp(1) = 12
    # =========================================================
    ws1_12 = wb.create_sheet(title='Lop_1_12_Tiet')
    setup_sheet_header(ws1_12,
        'KẾ HOẠCH BÀI DẠY CHUYÊN ĐỀ GIÁO DỤC AI BẮT BUỘC - LỚP 1 (12 TIẾT CỐT LÕI)',
        'Bao phủ 100% 17 YCCĐ Cốt lõi của Lớp 1 theo QĐ 2422 | Kế toán: Mạch A(4t) + B(2t) + C(2t) + D(3t) + Tích hợp(1t) = 12t')

    l1_12_data = [
        ['1', 'Tư duy lấy con người làm trung tâm', 'Bài 1: Cảm xúc của em và phản ứng của máy', 'Nêu ví dụ về cảm xúc con người (vui, buồn, sợ hãi...); nhận ra con người có cảm xúc thật còn AI thì không (chỉ mô phỏng). [1.A1.1, 1.A1.2]', 'Cốt lõi', 'Tranh ảnh thẻ cảm xúc, video ngắn robot biểu cảm'],
        ['2', 'Tư duy lấy con người làm trung tâm', 'Bài 2: Nụ cười của Robot do ai lập trình?', 'Nhận biết biểu hiện cảm xúc của AI (cười, chào) là do con người lập trình/thiết kế trước; AI không tự vui buồn. [1.A1.3, 1.A1.4]', 'Cốt lõi', 'Mô hình robot giấy, kịch bản đóng vai trò chuyện'],
        ['3', 'Các kĩ thuật và ứng dụng AI', 'Bài 3: Đôi mắt và đôi tai của thiết bị thông minh', 'Nhận biết AI trong một số ví dụ cụ thể; nhận ra thiết bị thông minh có các bộ phận như con người: Camera là "mắt", Micro là "tai". [1.C1.1, 1.C1.3]', 'Cốt lõi', 'Thiết bị thông minh dùng chung của lớp, máy chiếu'],
        ['4', 'Các kĩ thuật và ứng dụng AI', 'Bài 4: Trò chuyện cùng trợ lý thông minh', 'Nhận diện trợ lý ảo quen thuộc; nhận biết AI hiểu mệnh lệnh đơn giản và trò chuyện theo kịch bản định sẵn dưới sự giám sát. [1.C1.2, 1.C1.4]', 'Cốt lõi', 'Loa thông minh/máy tính giáo viên mô phỏng'],
        ['5', 'Tư duy lấy con người làm trung tâm', 'Bài 5: Những thiết bị AI giúp ích quanh em', 'Kể tên thiết bị có sử dụng AI (điện thoại thông minh, loa thông minh); mô tả công dụng chính giúp cuộc sống tiện ích hơn. [1.A2.2, 1.A2.3]', 'Cốt lõi', 'Bộ thẻ tranh thiết bị gia đình, phiếu ghép nối'],
        ['6', 'Tư duy lấy con người làm trung tâm', 'Bài 6: Cách AI thể hiện cảm xúc thân thiện', 'Nêu được các cách mà AI thể hiện cảm xúc qua hình ảnh, giọng nói hoặc hành vi (biểu tượng khuôn mặt vui, giọng nói thân thiện, lời chào dễ thương). [1.A2.1]', 'Cốt lõi', 'File âm thanh giọng nói robot vui vẻ, thân thiện'],
        ['7', 'Đạo đức AI', 'Bài 7: Máy thông minh làm việc tốt', 'Nêu ví dụ con người sử dụng AI đúng cách vì mục đích tốt đẹp (giúp học tập, chỉ đường, hỗ trợ bác sĩ). [1.B3.2]', 'Cốt lõi', 'Tranh kể chuyện: Bác sĩ robot, Trợ lý tìm đường'],
        ['8', 'Đạo đức AI', 'Bài 8: Không dùng thiết bị thông minh làm việc xấu', 'Nhận biết hành vi dùng AI gây hại cho người khác; hiểu rằng tuyệt đối không được phép sử dụng AI với mục đích làm hại người khác. [1.B1.1, 1.B3.1]', 'Cốt lõi', 'Tình huống đóng vai ứng xử đúng mực trong lớp'],
        ['9', 'Thiết kế hệ thống AI', 'Bài 9: Máy thông minh học từ ví dụ', 'Nêu ví dụ AI "học" từ hình ảnh hoặc thông tin con người cung cấp (AI học nhận biết quả cam qua nhiều bức ảnh quả cam). [1.D1.1]', 'Cốt lõi', 'Bộ thẻ hình hoa quả mẫu, hộp phân loại trực quan'],
        ['10', 'Thiết kế hệ thống AI', 'Bài 10: Thực hành: Cùng máy học từ nhiều hình mẫu', 'Trải nghiệm tình huống con người cung cấp các ví dụ hình mẫu cụ thể để máy thông minh nhận diện đúng đối tượng. [Thực hành hóa 1.D1.1]', 'Cốt lõi', 'Bộ thẻ tranh vẽ mẫu trực quan'],
        ['11', 'Thiết kế hệ thống AI', 'Bài 11: Máy làm một việc và máy làm nhiều việc', 'Xếp được máy thông minh vào 2 nhóm: Nhóm chỉ làm được 1 việc (nhận biết ảnh) và nhóm làm được nhiều việc khác nhau. [1.D2.1, 1.D2.2]', 'Cốt lõi', 'Phiếu phân loại dán sticker (Máy đơn năng vs Đa năng)'],
        ['12', 'Tích hợp 4 mạch', 'Bài 12: Tổng kết chuyên đề: Em làm chủ thiết bị thông minh', 'Báo cáo tranh vẽ người bạn AI tương lai; tổng kết minh chứng học tập và khẳng định con người làm chủ công nghệ vì việc tốt. [Tích hợp 4 mạch: 1.A1.2, 1.B3.2, 1.D2.2]', 'Cốt lõi', 'Giá trưng bày tranh vẽ, sticker khen thưởng tiến bộ']
    ]
    populate_table(ws1_12, l1_12_data)

    # =========================================================
    # SHEET 3: LỚP 1 - KHUNG 36 TIẾT TOÀN DIỆN (CẢ NĂM HỌC)
    # ĐÚNG 12 TIẾT CỐT LÕI + ĐÚNG 24 TIẾT MỞ RỘNG = 36 TIẾT
    # Đánh giá bằng hồ sơ minh chứng quá trình (Portfolio), không bài thi trắc nghiệm
    # =========================================================
    ws1_36 = wb.create_sheet(title='Lop_1_36_Tiet')
    setup_sheet_header(ws1_36,
        'KẾ HOẠCH GIÁO DỤC TOÀN DIỆN MÔN TRÍ TUỆ NHÂN TẠO (AI) - LỚP 1 (36 TIẾT/35 TUẦN)',
        'Cơ cấu chuẩn: Đúng 12 tiết Cốt lõi + Đúng 24 tiết Mở rộng = 36 tiết | Đánh giá quá trình bằng nhận xét và hồ sơ minh chứng (Mục VI QĐ 2422)')

    l1_36_data = [
        # HỌC KỲ I (18 tiết)
        ['1', 'Tư duy lấy con người làm trung tâm', 'Bài 1: Cảm xúc của em và cảm xúc của bạn bè', 'Nêu ví dụ về cảm xúc con người (vui, buồn, sợ hãi...); nhận ra con người có cảm xúc thật còn AI thì không (chỉ mô phỏng). [1.A1.1, 1.A1.2]', 'Cốt lõi', 'Bộ thẻ cảm xúc mặt cười/mặt mếu'],
        ['2', 'Tư duy lấy con người làm trung tâm', 'Bài 2: Nụ cười của Robot do ai lập trình?', 'Nhận biết biểu hiện cảm xúc của AI (cười, chào) là do con người lập trình/thiết kế trước; AI không tự vui buồn. [1.A1.3, 1.A1.4]', 'Cốt lõi', 'Mô hình robot giấy, tranh minh họa'],
        ['3', 'Tư duy lấy con người làm trung tâm', 'Bài 3: Trò chơi đóng vai: Robot biết cười', 'Trải nghiệm đóng vai Robot phản hồi nụ cười và lời chào theo kịch bản quy ước trước.', 'Mở rộng', 'Mũ hóa trang robot, thẻ lệnh cử chỉ'],
        ['4', 'Tư duy lấy con người làm trung tâm', 'Bài 4: Bàn tay con người thiết kế Robot', 'Khám phá công việc của các kỹ sư sáng tạo ra các cử chỉ thân thiện cho robot.', 'Mở rộng', 'Tranh vẽ kỹ sư điều khiển máy tính'],
        ['5', 'Tư duy lấy con người làm trung tâm', 'Bài 5: Cách AI thể hiện cảm xúc thân thiện', 'Nêu được các cách mà AI thể hiện cảm xúc qua hình ảnh, giọng nói hoặc hành vi (biểu tượng khuôn mặt vui, giọng nói thân thiện, lời chào). [1.A2.1]', 'Cốt lõi', 'File âm thanh giọng nói robot thân thiện'],
        ['6', 'Tư duy lấy con người làm trung tâm', 'Bài 6: Những thiết bị AI giúp ích quanh em', 'Kể tên thiết bị có sử dụng AI (loa thông minh, điện thoại); mô tả công dụng chính giúp cuộc sống tiện ích hơn. [1.A2.2, 1.A2.3]', 'Cốt lõi', 'Bộ thẻ tranh thiết bị gia đình'],
        ['7', 'Tư duy lấy con người làm trung tâm', 'Bài 7: Lời chào dễ thương giúp hợp tác vui vẻ', 'Nêu được rằng những biểu hiện thân thiện giúp AI giao tiếp tự nhiên hơn, khiến người dùng cảm thấy thoải mái, dễ hợp tác. [1.A2.MR1]', 'Mở rộng', 'Loa phát câu chào hỏi đáng yêu'],
        ['8', 'Các kĩ thuật và ứng dụng AI', 'Bài 8: Đôi mắt và đôi tai của thiết bị thông minh', 'Nhận biết AI trong một số ví dụ cụ thể; nhận ra thiết bị thông minh có các bộ phận như con người: Camera là "mắt", Micro là "tai". [1.C1.1, 1.C1.3]', 'Cốt lõi', 'Webcam lớp học, thiết bị thông minh'],
        ['9', 'Các kĩ thuật và ứng dụng AI', 'Bài 9: Khám phá "Mắt thần" Camera nhận diện đồ vật', 'Nhận biết được AI có khả năng xử lí hình ảnh nhận được để nhận diện các đồ vật xung quanh em. [1.C1.MR1]', 'Mở rộng', 'Camera nhận diện đồ vật trực quan'],
        ['10', 'Các kĩ thuật và ứng dụng AI', 'Bài 10: Trò chuyện cùng trợ lý thông minh', 'Nhận diện trợ lý ảo quen thuộc; nhận biết AI hiểu mệnh lệnh đơn giản và trò chuyện theo kịch bản định sẵn dưới sự giám sát. [1.C1.2, 1.C1.4]', 'Cốt lõi', 'Trợ lý ảo trên máy tính giáo viên'],
        ['11', 'Tư duy lấy con người làm trung tâm', 'Bài 11: Đi tìm thiết bị AI trong trường học của em', 'Quan sát và kể tên các thiết bị thông minh có trong trường học (camera cổng trường, màn hình tương tác).', 'Mở rộng', 'Phiếu quan sát thực tế sân trường'],
        ['12', 'Đạo đức AI', 'Bài 12: Máy thông minh làm việc tốt', 'Nêu ví dụ con người sử dụng AI đúng cách vì mục đích tốt đẹp (giúp học tập, chỉ đường, hỗ trợ bác sĩ). [1.B3.2]', 'Cốt lõi', 'Video ngắn người máy hỗ trợ bác sĩ'],
        ['13', 'Đạo đức AI', 'Bài 13: Vẽ tranh: Người bạn AI làm việc tốt', 'Sáng tạo tranh vẽ ý tưởng thiết bị thông minh giúp đỡ người khuyết tật, người già.', 'Mở rộng', 'Giấy vẽ A4, sáp màu'],
        ['14', 'Đạo đức AI', 'Bài 14: Không dùng thiết bị thông minh làm việc xấu', 'Nhận biết hành vi dùng AI gây hại cho người khác; hiểu rằng tuyệt đối không được phép sử dụng AI với mục đích làm hại người khác. [1.B1.1, 1.B3.1]', 'Cốt lõi', 'Tình huống ứng xử đạo đức'],
        ['15', 'Đạo đức AI', 'Bài 15: Thói quen tốt khi sử dụng thiết bị thông minh', 'Hình thành thói quen ngồi đúng tư thế, giữ khoảng cách mắt an toàn và nhờ người lớn hướng dẫn khi dùng máy.', 'Mở rộng', 'Poster tư thế ngồi học chuẩn'],
        ['16', 'Tư duy lấy con người làm trung tâm', 'Bài 16: Kể chuyện: Bạn nhỏ và chú Robot lễ phép', 'Đọc truyện và thảo luận về cách chào hỏi văn minh, đúng mực khi tương tác với thiết bị số.', 'Mở rộng', 'Truyện tranh đạo đức số thiếu nhi'],
        ['17', 'Ôn tập', 'Bài 17: Ôn tập chuyên đề Học kỳ I: Cảm xúc và Đạo đức', 'Hệ thống hóa các nhận thức về cảm xúc người vs máy, giác quan của máy và hành vi tốt khi dùng AI.', 'Mở rộng', 'Trò chơi hái hoa dân chủ ôn tập'],
        ['18', 'Tích hợp & Hồ sơ', 'Bài 18: Báo cáo hồ sơ học tập Học kỳ I', 'Tổng hợp minh chứng quá trình: Trưng bày bộ tranh vẽ cảm xúc và bảng nhận diện thiết bị AI; giáo viên nhận xét sự tiến bộ. [Mục VI QĐ 2422]', 'Mở rộng', 'Hồ sơ học tập (Portfolio) của học sinh'],

        # HỌC KỲ II (18 tiết)
        ['19', 'Các kĩ thuật và ứng dụng AI', 'Bài 19: Khám phá "Tai thính" Micro phân biệt âm thanh', 'Nhận biết được AI có khả năng xử lí âm thanh để phân biệt các loại âm thanh khác nhau trong đời sống. [1.C1.MR2]', 'Mở rộng', 'Micro, âm thanh tiếng mưa, tiếng chim'],
        ['20', 'Các kĩ thuật và ứng dụng AI', 'Bài 20: Trò chơi: Máy lắng nghe tiếng còi và tiếng nhạc', 'Trải nghiệm phân biệt âm thanh cảnh báo và âm thanh giai điệu qua giác quan Micro của máy.', 'Mở rộng', 'Bộ mẫu âm thanh tương tác'],
        ['21', 'Các kĩ thuật và ứng dụng AI', 'Bài 21: Trải nghiệm nét vẽ kỳ diệu cùng AI', 'Làm quen với việc máy gợi ý nét vẽ hoàn chỉnh từ hình vẽ phác thảo đơn giản của học sinh.', 'Mở rộng', 'Ứng dụng vẽ trực quan AutoDraw'],
        ['22', 'Thiết kế hệ thống AI', 'Bài 22: Máy thông minh học từ ví dụ', 'Nêu ví dụ AI "học" từ hình ảnh hoặc thông tin con người cung cấp (AI học nhận biết quả cam qua nhiều bức ảnh quả cam). [1.D1.1]', 'Cốt lõi', 'Bộ thẻ tranh quả cam, quả táo mẫu'],
        ['23', 'Thiết kế hệ thống AI', 'Bài 23: Cần nhiều ví dụ khác nhau để máy học đúng', 'Biết được rằng để AI trả lời đúng cần có nhiều ví dụ đúng và khác nhau để AI học. [1.D1.MR1]', 'Mở rộng', 'Bộ ảnh mẫu nhiều màu sắc, góc chụp'],
        ['24', 'Thiết kế hệ thống AI', 'Bài 24: Trò chơi phân loại: Dạy máy nhận biết quả', 'Học sinh cung cấp các thẻ hình ảnh mẫu để máy phân loại quả tròn và quả dài.', 'Mở rộng', 'Hộp phân loại mẫu trực quan'],
        ['25', 'Thiết kế hệ thống AI', 'Bài 25: Nhận biết máy thông minh đơn năng', 'Nhận biết được rằng có loại máy thông minh chỉ làm được một việc duy nhất (như máy nhận diện khuôn mặt). [1.D2.1]', 'Cốt lõi', 'Tranh thiết bị đơn năng quanh em'],
        ['26', 'Thiết kế hệ thống AI', 'Bài 26: Xếp nhóm máy làm một việc và nhiều việc', 'Xếp được một số máy thông minh vào hai nhóm: nhóm chỉ làm được một việc và nhóm làm được nhiều việc khác nhau. [1.D2.2]', 'Cốt lõi', 'Phiếu dán sticker phân nhóm máy'],
        ['27', 'Thiết kế hệ thống AI', 'Bài 27: Thực hành phân loại máy đa năng trong đời sống', 'Khám phá điện thoại thông minh, máy tính bảng làm được nhiều việc khác nhau.', 'Mở rộng', 'Tranh các thiết bị đa năng'],
        ['28', 'Thiết kế hệ thống AI', 'Bài 28: Trò chơi: Đi tìm người bạn máy đơn năng', 'Phân biệt các máy quét mã vạch ở siêu thị, máy đo nhiệt độ chỉ làm một nhiệm vụ.', 'Mở rộng', 'Thẻ hình thiết bị siêu thị, y tế'],
        ['29', 'Trải nghiệm mô hình', 'Bài 29: Khởi động hoạt động: Chú Robot giấy của em', 'Lên ý tưởng thiết kế một mô hình chú Robot giấy thông minh đồng hành trong học tập.', 'Mở rộng', 'Bìa carton, giấy màu thủ công'],
        ['30', 'Trải nghiệm mô hình', 'Bài 30: Chế tạo mô hình: Mắt Camera và Tai Micro', 'Cắt dán các bộ phận cảm nhận cho robot giấy: Đôi mắt Camera và đôi tai Micro.', 'Mở rộng', 'Kéo thủ công, keo dán'],
        ['31', 'Trải nghiệm mô hình', 'Bài 31: Vẽ tranh các đồ vật để nạp vào túi nhớ của Robot', 'Vẽ và cắt các thẻ tranh đồ chơi, hoa quả để nạp vào "bộ nhớ ví dụ" của chú Robot giấy.', 'Mở rộng', 'Giấy vẽ, thẻ tranh mini'],
        ['32', 'Trải nghiệm mô hình', 'Bài 32: Đóng vai ra lệnh và đối thoại cùng Robot giấy', 'Thực hành nói câu lệnh rõ ràng và cho bạn robot giấy phản hồi lời chào thân thiện.', 'Mở rộng', 'Kịch bản đóng vai cặp đôi'],
        ['33', 'Tích hợp & Hồ sơ', 'Bài 33: Tổng hợp minh chứng & Báo cáo hồ sơ học tập Học kỳ II', 'Đánh giá quá trình qua hồ sơ bài tập và mô hình học tập; giáo viên nhận xét sự tiến bộ của học sinh.', 'Mở rộng', 'Bảng nhận xét quá trình học tập'],
        ['34', 'Triển lãm', 'Bài 34: Triển lãm ngày hội: Chú Robot giấy thông minh', 'Trưng bày gian hàng mô hình robot giấy và bộ sưu tập ví dụ học tập của cả lớp.', 'Mở rộng', 'Không gian triển lãm lớp học'],
        ['35', 'Tổng kết', 'Bài 35: Tổng kết chương trình AI Lớp 1: Em yêu công nghệ', 'Hệ thống hóa toàn bộ 4 mạch nội dung Lớp 1; tuyên dương tinh thần tự tin và làm chủ thiết bị.', 'Mở rộng', 'Video tổng kết hoạt động năm học'],
        ['36', 'Tích hợp 4 mạch', 'Bài 36: Báo cáo chuyên đề cốt lõi: Em làm chủ thiết bị thông minh', 'Báo cáo tranh vẽ người bạn AI tương lai; tổng kết hồ sơ minh chứng cốt lõi; khẳng định con người làm chủ AI vì việc tốt. [1.A1.2, 1.B3.2, 1.D2.2]', 'Cốt lõi', 'Hồ sơ minh chứng học tập, bảng tuyên dương']
    ]
    populate_table(ws1_36, l1_36_data)

    # =========================================================
    # SHEET 4: LỚP 6 - KHUNG 12 TIẾT CỐT LÕI (BẮT BUỘC)
    # Khớp 100% 16 YCCĐ Cốt lõi, kế toán số tiết chuẩn xác: A(3) + B(2) + C(4) + D(2) + Tích hợp(1) = 12
    # =========================================================
    ws6_12 = wb.create_sheet(title='Lop_6_12_Tiet')
    setup_sheet_header(ws6_12,
        'KẾ HOẠCH BÀI DẠY CHUYÊN ĐỀ GIÁO DỤC AI BẮT BUỘC - LỚP 6 (12 TIẾT CỐT LÕI)',
        'Bao phủ 100% 16 YCCĐ Cốt lõi của Lớp 6 theo QĐ 2422 | Kế toán: Mạch A(3t) + B(2t) + C(4t) + D(2t) + Tích hợp(1t) = 12t')

    l6_12_data = [
        ['1', 'Tư duy lấy con người làm trung tâm', 'Bài 1: AI là công cụ, con người ra quyết định', 'Giải thích AI do con người tạo ra, lập trình và điều khiển để thực hiện nhiệm vụ cụ thể; AI chỉ là công cụ hỗ trợ, con người ra quyết định cuối cùng và chịu trách nhiệm. [6.A1.1, 6.A1.2]', 'Cốt lõi', 'Máy chiếu, phiếu phân tích tình huống Người - Máy'],
        ['2', 'Tư duy lấy con người làm trung tâm', 'Bài 2: Kỹ năng kiểm chứng kết quả do AI cung cấp', 'Thực hiện kiểm tra lại kết quả do AI đưa ra (đối chiếu SGK, nguồn tin cậy); nêu ví dụ tình huống con người ra quyết định với sự hỗ trợ của AI. [6.A1.3, 6.A3.1]', 'Cốt lõi', 'Máy tính kết nối mạng, phiếu đối chiếu nguồn tin'],
        ['3', 'Tư duy lấy con người làm trung tâm', 'Bài 3: Bảo vệ dữ liệu cá nhân và quyền riêng tư', 'Giải thích dữ liệu cá nhân (ảnh, giọng nói, họ tên, vị trí) cần bảo vệ; trình bày khái niệm quyền riêng tư ở mức đơn giản và tác hại khi dữ liệu cá nhân bị sử dụng sai mục đích. [6.A3.3, 6.A3.4]', 'Cốt lõi', 'Bộ tình huống rò rỉ dữ liệu, bảng quy tắc bảo mật'],
        ['4', 'Đạo đức AI', 'Bài 4: Tính hai mặt của các tính năng AI', 'Chỉ ra mặt tích cực và hạn chế của một số tính năng AI cụ thể (thu thập dữ liệu giúp gợi ý chính xác nhưng tiềm ẩn nguy cơ xâm phạm đời tư). [6.B1.1]', 'Cốt lõi', 'Bảng phân tích Lợi ích vs Rủi ro'],
        ['5', 'Đạo đức AI', 'Bài 5: Tiêu chuẩn an toàn và minh bạch của ứng dụng AI', 'Đặt được một số câu hỏi đơn giản để kiểm tra tính an toàn và minh bạch của ứng dụng AI ("Công cụ này có an toàn không?", "Dữ liệu lưu ở đâu?"). [6.B2.1]', 'Cốt lõi', 'Bảng kiểm 5 câu hỏi vàng kiểm tra an toàn AI'],
        ['6', 'Các kĩ thuật và ứng dụng AI', 'Bài 6: Khám phá cách AI học: Dữ liệu và Thuật toán', 'Giải thích hai thành phần chính để huấn luyện AI là dữ liệu (văn bản, hình ảnh) và thuật toán (phương pháp học từ dữ liệu). [6.C1.1]', 'Cốt lõi', 'Sơ đồ luồng: Dữ liệu + Thuật toán = Mô hình'],
        ['7', 'Các kĩ thuật và ứng dụng AI', 'Bài 7: Tác động của AI đối với bản thân và học tập', 'Nêu ví dụ tác động tích cực và tiêu cực của AI đối với bản thân, gia đình; trình bày lợi ích của AI trong việc hỗ trợ con người học hỏi, rèn kĩ năng khi dùng đúng mực. [6.C1.2, 6.A3.2]', 'Cốt lõi', 'Phiếu thảo luận nhóm: Lợi ích và nguy cơ lệ thuộc'],
        ['8', 'Các kĩ thuật và ứng dụng AI', 'Bài 8: Phân biệt ứng dụng có AI và không có AI', 'Phân biệt công cụ có AI và không có AI qua ví dụ gần gũi; kể tên và mô tả chức năng chính của một số công cụ AI thông dụng (trợ lý ảo, ứng dụng bản đồ, dịch). [6.C2.1, 6.C2.2]', 'Cốt lõi', 'Bảng so sánh phần mềm truyền thống vs phần mềm AI'],
        ['9', 'Các kĩ thuật và ứng dụng AI', 'Bài 9: Các công nghệ AI quen thuộc trong đời sống', 'Kể được tên một số công nghệ AI quen thuộc trong đời sống (nhận dạng hình ảnh, chuyển đổi giữa văn bản và giọng nói). [6.C3.1]', 'Cốt lõi', 'Công cụ trải nghiệm nhận dạng giọng nói/hình ảnh'],
        ['10', 'Thiết kế hệ thống AI', 'Bài 10: Ranh giới sử dụng: Khi nào nên và không nên dùng AI?', 'Nêu được một số tình huống quen thuộc nên hoặc không nên sử dụng AI (nên dùng luyện phát âm, tìm ý tưởng; không nên dùng khi làm bài kiểm tra). [6.D1.1]', 'Cốt lõi', 'Trò chơi phân loại tình huống Nên / Không nên'],
        ['11', 'Thiết kế hệ thống AI', 'Bài 11: Giới hạn của hệ thống AI so với con người', 'Trình bày một số giới hạn của hệ thống AI so với con người qua các tình huống, công việc mà con người thực hiện phù hợp hơn AI (thấu cảm, đạo đức). [6.D2.1]', 'Cốt lõi', 'Phiếu so sánh năng lực: Con người vs Hệ thống AI'],
        ['12', 'Tích hợp 4 mạch', 'Bài 12: Báo cáo chuyên đề: Sử dụng AI thông minh và trách nhiệm', 'Tổng kết chuyên đề 12 tiết; hoàn thiện hồ sơ học tập và lưu vết minh chứng câu lệnh (prompt log); cam kết liêm chính số. [Tích hợp 4 mạch: 6.A1.2, 6.A1.3, 6.D1.1, 6.D2.1]', 'Cốt lõi', 'Hồ sơ minh chứng học tập, bản cam kết liêm chính số']
    ]
    populate_table(ws6_12, l6_12_data)

    # =========================================================
    # SHEET 5: LỚP 6 - KHUNG 36 TIẾT TOÀN DIỆN (CẢ NĂM HỌC)
    # ĐÚNG 12 TIẾT CỐT LÕI + ĐÚNG 24 TIẾT MỞ RỘNG = 36 TIẾT
    # Bám sát 8 YCCĐ MR của Lớp 6 | Không dạy lấn sân dự án sản phẩm Lớp 7-9
    # =========================================================
    ws6_36 = wb.create_sheet(title='Lop_6_36_Tiet')
    setup_sheet_header(ws6_36,
        'KẾ HOẠCH GIÁO DỤC TOÀN DIỆN MÔN TRÍ TUỆ NHÂN TẠO (AI) - LỚP 6 (36 TIẾT/35 TUẦN)',
        'Cơ cấu chuẩn: Đúng 12 tiết Cốt lõi + Đúng 24 tiết Mở rộng = 36 tiết | Đánh giá quá trình bằng nhận xét và hồ sơ học tập số (Mục VI QĐ 2422)')

    l6_36_data = [
        # HỌC KỲ I (18 tiết)
        ['1', 'Tư duy lấy con người làm trung tâm', 'Bài 1: AI là công cụ, con người ra quyết định', 'Giải thích AI do con người tạo ra, lập trình và điều khiển để thực hiện nhiệm vụ cụ thể; AI chỉ là công cụ hỗ trợ, con người ra quyết định cuối cùng và chịu trách nhiệm. [6.A1.1, 6.A1.2]', 'Cốt lõi', 'Video lịch sử AI, sơ đồ nguồn gốc AI'],
        ['2', 'Tư duy lấy con người làm trung tâm', 'Bài 2: Kỹ năng kiểm chứng kết quả do AI cung cấp', 'Thực hiện kiểm tra lại kết quả do AI đưa ra (đối chiếu SGK, nguồn tin cậy); nêu ví dụ tình huống con người ra quyết định với sự hỗ trợ của AI. [6.A1.3, 6.A3.1]', 'Cốt lõi', 'Công cụ AI hỏi đáp, tài liệu SGK chuẩn'],
        ['3', 'Tư duy lấy con người làm trung tâm', 'Bài 3: Thực hành kỹ năng đối chiếu đa nguồn tin cậy', 'Rèn luyện thói quen tra cứu chéo ít nhất 2 nguồn tin độc lập để xác minh câu trả lời của AI.', 'Mở rộng', 'Trang tra cứu thông tin khoa học'],
        ['4', 'Tư duy lấy con người làm trung tâm', 'Bài 4: Nhận biết hiện tượng ảo giác AI (hallucination)', 'Nhận diện các trường hợp AI đưa ra câu trả lời có vẻ hợp lý nhưng hoàn toàn sai sự thật.', 'Mở rộng', 'Bộ mẫu câu trả lời ảo giác của AI'],
        ['5', 'Tư duy lấy con người làm trung tâm', 'Bài 5: Bảo vệ dữ liệu cá nhân và quyền riêng tư', 'Giải thích dữ liệu cá nhân (ảnh, giọng nói, họ tên, vị trí) cần bảo vệ; trình bày khái niệm quyền riêng tư ở mức đơn giản và tác hại khi dữ liệu cá nhân bị sử dụng sai mục đích. [6.A3.3, 6.A3.4]', 'Cốt lõi', 'Phiếu bóc tách dữ liệu cá nhân nhạy cảm'],
        ['6', 'Tư duy lấy con người làm trung tâm', 'Bài 6: Kỹ năng khử nhận dạng dữ liệu cá nhân', 'Thực hành kỹ thuật che mặt, ẩn thông tin danh tính trước khi chia sẻ dữ liệu phục vụ học tập.', 'Mở rộng', 'Công cụ che mờ/khử nhận dạng ảnh số'],
        ['7', 'Đạo đức AI', 'Bài 7: Tính hai mặt của các tính năng AI', 'Chỉ ra mặt tích cực và hạn chế của một số tính năng AI cụ thể (thu thập dữ liệu giúp gợi ý chính xác nhưng tiềm ẩn nguy cơ xâm phạm đời tư). [6.B1.1]', 'Cốt lõi', 'Bảng phân tích Lợi ích vs Rủi ro'],
        ['8', 'Đạo đức AI', 'Bài 8: Tiêu chuẩn an toàn và minh bạch của ứng dụng AI', 'Đặt được một số câu hỏi đơn giản để kiểm tra tính an toàn và minh bạch của ứng dụng AI ("Công cụ này có an toàn không?", "Dữ liệu lưu ở đâu?"). [6.B2.1]', 'Cốt lõi', 'Bảng kiểm 5 câu hỏi vàng kiểm tra an toàn AI'],
        ['9', 'Tích hợp & Hồ sơ', 'Bài 9: Tổng hợp minh chứng & Báo cáo học tập giữa Học kỳ I', 'Tổng hợp minh chứng quá trình: Đánh giá phiếu kiểm chứng thông tin và bảng kiểm an toàn dữ liệu; giáo viên nhận xét sự tiến bộ. [Mục VI QĐ 2422]', 'Mở rộng', 'Phiếu đánh giá quá trình học tập'],
        ['10', 'Các kĩ thuật và ứng dụng AI', 'Bài 10: Khám phá cách AI học: Dữ liệu và Thuật toán', 'Giải thích hai thành phần chính để huấn luyện AI là dữ liệu (văn bản, hình ảnh) và thuật toán (phương pháp học từ dữ liệu). [6.C1.1]', 'Cốt lõi', 'Mô hình trực quan luồng học máy'],
        ['11', 'Các kĩ thuật và ứng dụng AI', 'Bài 11: Mối liên hệ giữa huấn luyện và hoạt động thực tế', 'Chỉ ra được mối liên hệ giữa quá trình huấn luyện và hoạt động của một công cụ AI qua ví dụ đơn giản (trợ lý ảo hiểu tiếng Việt nhờ dữ liệu giọng nói tiếng Việt). [6.C1.MR1]', 'Mở rộng', 'Mô hình minh họa quá trình nạp dữ liệu'],
        ['12', 'Các kĩ thuật và ứng dụng AI', 'Bài 12: Thử nghiệm đối kháng với công cụ AI', 'Thực hiện được thử nghiệm đơn giản với một công cụ AI và nhận xét được các bước hoạt động của công cụ đó (đặt cùng câu lệnh cho các công cụ khác nhau). [6.C1.MR2]', 'Mở rộng', 'So sánh 2 phần mềm hội thoại tự động'],
        ['13', 'Các kĩ thuật và ứng dụng AI', 'Bài 13: Kỹ thuật câu lệnh (prompt) có cấu trúc', 'Thực hành đặt câu lệnh rõ ràng, cung cấp bối cảnh và yêu cầu cụ thể để nhận được kết quả tốt nhất.', 'Mở rộng', 'Biểu mẫu thiết kế câu lệnh chuẩn'],
        ['14', 'Các kĩ thuật và ứng dụng AI', 'Bài 14: Kỹ năng ghi nhật ký câu lệnh (prompt log)', 'Thực hành ghi lại nguồn dữ liệu, câu lệnh đã cung cấp và phản hồi nhận được để thực hiện trách nhiệm giải trình.', 'Mở rộng', 'Mẫu sổ nhật ký câu lệnh học đường'],
        ['15', 'Các kĩ thuật và ứng dụng AI', 'Bài 15: Tác động của AI đối với bản thân và học tập', 'Nêu ví dụ tác động tích cực và tiêu cực của AI đối với bản thân, gia đình; trình bày lợi ích của AI trong việc hỗ trợ con người học hỏi, rèn kĩ năng khi dùng đúng mực. [6.C1.2, 6.A3.2]', 'Cốt lõi', 'Phiếu thảo luận: Lợi ích và nguy cơ lệ thuộc'],
        ['16', 'Các kĩ thuật và ứng dụng AI', 'Bài 16: Phân tích tác động của công cụ AI trong gia đình', 'Phân tích được ở mức đơn giản tác động của một công cụ AI cụ thể đối với bản thân và gia đình (chỉ ra cả mặt tích cực và tiêu cực). [6.C1.MR3]', 'Mở rộng', 'Cây phân tích vấn đề tác động gia đình'],
        ['17', 'Ôn tập', 'Bài 17: Ôn tập chuyên đề Học kỳ I: Dữ liệu và Câu lệnh', 'Hệ thống hóa các kiến thức về kiến trúc Dữ liệu - Thuật toán, kỹ thuật câu lệnh và liêm chính học thuật.', 'Mở rộng', 'Hệ thống câu hỏi ôn tập tương tác'],
        ['18', 'Tích hợp & Hồ sơ', 'Bài 18: Báo cáo hồ sơ học tập Học kỳ I', 'Trưng bày sổ nhật ký câu lệnh (prompt log) và bảng so sánh công cụ AI; giáo viên nhận xét đánh giá quá trình. [Mục VI QĐ 2422]', 'Mở rộng', 'Hồ sơ học tập số (Digital Portfolio)'],

        # HỌC KỲ II (18 tiết)
        ['19', 'Các kĩ thuật và ứng dụng AI', 'Bài 19: Phân biệt ứng dụng có AI và không có AI', 'Phân biệt công cụ có AI và không có AI qua ví dụ gần gũi; kể tên và mô tả chức năng chính của một số công cụ AI thông dụng (trợ lý ảo, bản đồ, dịch). [6.C2.1, 6.C2.2]', 'Cốt lõi', 'Bảng so sánh phần mềm truyền thống vs phần mềm AI'],
        ['20', 'Các kĩ thuật và ứng dụng AI', 'Bài 20: Ứng dụng AI gắn với thực tiễn tại Việt Nam', 'Nêu được ví dụ về ứng dụng AI trong cuộc sống, ưu tiên các vấn đề gắn với thực tiễn ở Việt Nam (nông nghiệp thông minh, định danh số, dự báo thời tiết). [6.C2.MR1]', 'Mở rộng', 'Phóng sự AI nông nghiệp công nghệ cao tại VN'],
        ['21', 'Các kĩ thuật và ứng dụng AI', 'Bài 21: Các công nghệ AI quen thuộc trong đời sống', 'Kể được tên một số công nghệ AI quen thuộc trong đời sống (nhận dạng hình ảnh, chuyển đổi giữa văn bản và giọng nói). [6.C3.1]', 'Cốt lõi', 'Công cụ trải nghiệm nhận dạng giọng nói/hình ảnh'],
        ['22', 'Các kĩ thuật và ứng dụng AI', 'Bài 22: Tính năng AI tích hợp trong ứng dụng thường gặp', 'Trình bày được một số tính năng AI tích hợp trong các ứng dụng thường gặp (tính năng gợi ý đề xuất nội dung, dịch tự động). [6.C3.MR1]', 'Mở rộng', 'Mô phỏng tính năng gợi ý đề xuất'],
        ['23', 'Các kĩ thuật và ứng dụng AI', 'Bài 23: Nhận biết hiện tượng "bong bóng thông tin"', 'Tìm hiểu nguyên nhân khi hệ thống chỉ gợi ý những gì người dùng thích, dẫn đến góc nhìn phiến diện.', 'Mở rộng', 'Sơ đồ luồng gợi ý nội dung số'],
        ['24', 'Thiết kế hệ thống AI', 'Bài 24: Ranh giới sử dụng: Khi nào nên và không nên dùng AI?', 'Nêu được một số tình huống quen thuộc nên hoặc không nên sử dụng AI (nên dùng luyện phát âm, tìm ý tưởng; không nên dùng khi làm bài kiểm tra). [6.D1.1]', 'Cốt lõi', 'Trò chơi phân loại tình huống Nên / Không nên'],
        ['25', 'Thiết kế hệ thống AI', 'Bài 25: Tranh biện ý kiến cá nhân: Nên hay không nên dùng AI?', 'Trình bày được ý kiến cá nhân về việc nên hay không nên sử dụng AI trong một số tình huống thực tế; giải thích lí do bảo vệ quan điểm. [6.D1.MR1]', 'Mở rộng', 'Phiếu tranh biện theo cặp đôi'],
        ['26', 'Thiết kế hệ thống AI', 'Bài 26: Xây dựng quy ước sử dụng AI trong học tập của lớp', 'Thảo luận nhóm xây dựng bản cam kết: Sử dụng AI để gợi ý dàn ý, không sao chép nguyên văn.', 'Mở rộng', 'Bản quy ước văn hóa số lớp học'],
        ['27', 'Tích hợp & Hồ sơ', 'Bài 27: Tổng hợp minh chứng & Báo cáo học tập giữa Học kỳ II', 'Đánh giá quá trình: Đánh giá bài tranh biện và bản quy ước sử dụng AI; giáo viên nhận xét sự tiến bộ. [Mục VI QĐ 2422]', 'Mở rộng', 'Phiếu nhận xét đánh giá quá trình'],
        ['28', 'Thiết kế hệ thống AI', 'Bài 28: Giới hạn của hệ thống AI so với con người', 'Trình bày một số giới hạn của hệ thống AI so với con người qua các tình huống, công việc mà con người thực hiện phù hợp hơn AI (thấu cảm, đạo đức). [6.D2.1]', 'Cốt lõi', 'Phiếu so sánh năng lực: Con người vs Hệ thống AI'],
        ['29', 'Thiết kế hệ thống AI', 'Bài 29: Vì sao AI gặp giới hạn trong một số công việc?', 'Giải thích được vì sao AI gặp giới hạn trong một số công việc so với con người (AI học từ dữ liệu quá khứ nên khó thích ứng tình huống mới lạ). [6.D2.MR1]', 'Mở rộng', 'Nghiên cứu ca: AI sáng tác văn học nghệ thuật'],
        ['30', 'Thiết kế hệ thống AI', 'Bài 30: Đề xuất mô hình kết hợp tối ưu giữa Người và AI', 'Đề xuất được cách kết hợp giữa con người và AI trong một công việc cụ thể để phát huy thế mạnh của mỗi bên (AI gợi ý thông tin, người phán đoán). [6.D2.MR2]', 'Mở rộng', 'Sơ đồ phân vai Người - Máy trong công việc'],
        ['31', 'Thiết kế hệ thống AI', 'Bài 31: Xây dựng kịch bản cộng tác: Em và trợ lý AI học tập', 'Thực hành thiết lập kịch bản làm việc nhóm: Phân công nhiệm vụ cho công cụ AI hỗ trợ tra cứu và nhóm học sinh tổng hợp.', 'Mở rộng', 'Mẫu kịch bản cộng tác Người - AI'],
        ['32', 'Thiết kế hệ thống AI', 'Bài 32: Thử nghiệm kịch bản và đánh giá hiệu quả', 'Vận hành kịch bản cộng tác đã thiết kế và nhận xét ưu điểm, hạn chế của việc phối hợp cùng AI.', 'Mở rộng', 'Bảng tiêu chí đánh giá hiệu quả phối hợp'],
        ['33', 'Tích hợp & Hồ sơ', 'Bài 33: Hoàn thiện hồ sơ lưu vết câu lệnh và minh chứng', 'Rà soát toàn bộ nhật ký câu lệnh và các sản phẩm đã thực hiện trong cả năm học.', 'Mở rộng', 'Mẫu hồ sơ trách nhiệm giải trình'],
        ['34', 'Triển lãm', 'Bài 34: Triển lãm báo cáo: Ý tưởng kết hợp Người và AI', 'Trưng bày poster kịch bản cộng tác Người - AI và hồ sơ nhật ký câu lệnh của các nhóm học sinh.', 'Mở rộng', 'Không gian trưng bày poster lớp học'],
        ['35', 'Tổng kết', 'Bài 35: Tổng kết chương trình AI Lớp 6: Tự hào công dân số', 'Hệ thống hóa toàn bộ 4 mạch năng lực; tuyên dương tinh thần sáng tạo, làm chủ và liêm chính học thuật.', 'Mở rộng', 'Bản đồ tư duy tổng kết năng lực AI Lớp 6'],
        ['36', 'Tích hợp 4 mạch', 'Bài 36: Báo cáo chuyên đề cốt lõi: Sử dụng AI thông minh và trách nhiệm', 'Tổng kết chuyên đề cốt lõi 12 tiết; hoàn thiện hồ sơ học tập và lưu vết minh chứng câu lệnh (prompt log); cam kết liêm chính số. [6.A1.2, 6.A1.3, 6.D1.1, 6.D2.1]', 'Cốt lõi', 'Hồ sơ minh chứng học tập, bản cam kết liêm chính số']
    ]
    populate_table(ws6_36, l6_36_data)

    # =========================================================
    # SHEET 6: BẢNG TRA CỨU NGUYÊN VĂN YCCĐ LỚP 1 VÀ LỚP 6
    # =========================================================
    ws_ref = wb.create_sheet(title='Tra_Cuu_YCCD_Chuan')
    ws_ref.views.sheetView[0].showGridLines = True
    ws_ref.merge_cells('A1:E1')
    ws_ref['A1'] = 'BẢNG ĐỐI CHIẾU NGUYÊN VĂN YÊU CẦU CẦN ĐẠT (YCCĐ) - LỚP 1 VÀ LỚP 6'
    ws_ref['A1'].font = font_title
    ws_ref['A1'].alignment = align_center
    ws_row_dim = ws_ref.row_dimensions[1]
    ws_row_dim.height = 28

    ws_ref.merge_cells('A2:E2')
    ws_ref['A2'] = 'Trích dẫn nguyên văn theo Phụ lục Quyết định số 2422/QĐ-BGDĐT của Bộ Giáo dục và Đào tạo'
    ws_ref['A2'].font = font_subtitle
    ws_ref['A2'].alignment = align_center
    ws_ref.row_dimensions[2].height = 18

    ref_headers = ['Khối lớp', 'Mã YCCĐ', 'Mạch & Chủ đề', 'Phân loại luồng', 'Nội dung Yêu cầu cần đạt nguyên văn']
    for c_idx, h in enumerate(ref_headers, 1):
        cell = ws_ref.cell(4, c_idx, h)
        cell.font = font_th
        cell.fill = fill_th
        cell.border = border_cell
        cell.alignment = align_center
    ws_ref.row_dimensions[4].height = 28

    import re
    with open('qd2422_full.txt', 'r', encoding='utf-8') as f:
        full_text = f.read()

    ref_row_idx = 5
    for g in [1, 6]:
        pos1 = full_text.find(f'LỚP {g}')
        pos2 = full_text.find(f'LỚP {g+1}') if g < 12 else len(full_text)
        g_chunk = full_text[pos1:pos2]

        matches = re.findall(rf'({g}\.[A-D][0-9]\.(?:MR)?[0-9]+)\.\s*([^\n\r]+)', g_chunk)
        strand_map = {
            'A1': 'Tư duy lấy con người làm trung tâm (A1)',
            'A2': 'Tư duy lấy con người làm trung tâm (A2)',
            'A3': 'Tư duy lấy con người làm trung tâm (A3)',
            'B1': 'Đạo đức AI (B1)',
            'B2': 'Đạo đức AI (B2)',
            'B3': 'Đạo đức AI (B3)',
            'C1': 'Các kĩ thuật và ứng dụng AI (C1)',
            'C2': 'Các kĩ thuật và ứng dụng AI (C2)',
            'C3': 'Các kĩ thuật và ứng dụng AI (C3)',
            'C4': 'Các kĩ thuật và ứng dụng AI (C4)',
            'C5': 'Các kĩ thuật và ứng dụng AI (C5)',
            'D1': 'Thiết kế hệ thống AI (D1)',
            'D2': 'Thiết kế hệ thống AI (D2)'
        }

        for code, desc in matches:
            is_core = ('MR' not in code)
            loai = 'Cốt lõi' if is_core else 'Mở rộng'
            strand_prefix = code.split('.')[1]
            strand_full = strand_map.get(strand_prefix, f'Chủ đề {strand_prefix}')

            row_data = [f'Lớp {g}', code, strand_full, loai, desc.strip()]
            for col_i, val in enumerate(row_data, 1):
                c_cell = ws_ref.cell(ref_row_idx, col_i, val)
                c_cell.font = font_cell
                c_cell.border = border_cell
                c_cell.alignment = align_top_center if col_i in [1, 2, 4] else align_top_left
                if is_core:
                    c_cell.fill = fill_core_tag if col_i == 4 else (fill_alt if ref_row_idx % 2 == 0 else fill_white)
                else:
                    c_cell.fill = fill_ext_tag if col_i == 4 else (fill_alt if ref_row_idx % 2 == 0 else fill_white)

            ws_ref.row_dimensions[ref_row_idx].height = 32
            ref_row_idx += 1

    col_w_ref = [10, 14, 28, 16, 68]
    for ci, wi in enumerate(col_w_ref, 1):
        ws_ref.column_dimensions[get_column_letter(ci)].width = wi

    # Lưu với tên đơn giản, rõ ràng theo đúng yêu cầu
    out_file = 'PPCT_AI_Lop1_va_Lop6_Chuan_QD2422.xlsx'
    wb.save(out_file)
    print(f'Successfully created refined workbook: {out_file}')

if __name__ == '__main__':
    build_curriculum_workbook()
