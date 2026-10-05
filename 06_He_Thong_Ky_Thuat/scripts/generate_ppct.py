# -*- coding: utf-8 -*-
"""
Script khởi tạo tệp Excel Phân phối chương trình Giáo dục AI Lớp 1 và Lớp 6
Đã tinh chỉnh:
- Gộp 3 cột (Tuần, Tiết thứ, Số tiết) thành 1 cột "Tiết"
- Tinh gọn tên Chủ đề: chỉ để tên thuần túy của 4 mạch
- Tinh gọn Nội dung: bỏ tiền tố thừa "Đáp ứng YCCĐ ...:"
- Giữ giao diện chuyên nghiệp, thoáng mắt, dễ đọc
"""
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

def build_curriculum_workbook():
    wb = openpyxl.Workbook()
    wb.remove(wb.active) # xoá sheet mặc định

    # Màu sắc giao diện
    c_navy = '1B365D'
    c_core = 'E8F5E9'      # Xanh nhạt cho Cốt lõi
    c_core_text = '1B5E20'
    c_ext = 'FFF3E0'       # Cam nhạt cho Mở rộng
    c_ext_text = 'E65100'
    c_eval = 'EDE7F6'      # Tím nhạt cho Đánh giá / Ôn tập
    c_eval_text = '4A148C'
    c_alt_row = 'F8FAFC'

    font_title = Font(name='Arial', size=13, bold=True, color=c_navy)
    font_subtitle = Font(name='Arial', size=9.5, italic=True, color='555555')
    font_th = Font(name='Arial', size=9.5, bold=True, color='FFFFFF')
    font_cell = Font(name='Arial', size=9.5, color='000000')
    font_cell_bold = Font(name='Arial', size=9.5, bold=True, color='000000')
    font_badge_core = Font(name='Arial', size=9, bold=True, color=c_core_text)
    font_badge_ext = Font(name='Arial', size=9, bold=True, color=c_ext_text)
    font_badge_eval = Font(name='Arial', size=9, bold=True, color=c_eval_text)

    fill_th = PatternFill(start_color=c_navy, end_color=c_navy, fill_type='solid')
    fill_core_tag = PatternFill(start_color=c_core, end_color=c_core, fill_type='solid')
    fill_ext_tag = PatternFill(start_color=c_ext, end_color=c_ext, fill_type='solid')
    fill_eval_tag = PatternFill(start_color=c_eval, end_color=c_eval, fill_type='solid')
    fill_alt = PatternFill(start_color=c_alt_row, end_color=c_alt_row, fill_type='solid')
    fill_white = PatternFill(start_color='FFFFFF', end_color='FFFFFF', fill_type='solid')

    border_side = Side(border_style='thin', color='D0D7DE')
    border_cell = Border(left=border_side, right=border_side, top=border_side, bottom=border_side)

    align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)
    align_top_left = Alignment(horizontal='left', vertical='top', wrap_text=True)
    align_top_center = Alignment(horizontal='center', vertical='top', wrap_text=True)

    # 6 CỘT CHUẨN TINH GỌN
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
                elif c_idx == 2:
                    cell.font = font_cell_bold
                    cell.alignment = align_top_left
                elif c_idx == 3:
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
                    elif 'Mở rộng' in str(val):
                        cell.font = font_badge_ext
                        cell.fill = fill_ext_tag
                    else:
                        cell.font = font_badge_eval
                        cell.fill = fill_eval_tag
                elif c_idx == 6:
                    cell.font = font_cell
                    cell.alignment = align_top_left
            ws.row_dimensions[r_idx].height = 38

        # Độ rộng cột tối ưu
        col_widths = [10, 24, 28, 48, 14, 26]
        for c_idx, w in enumerate(col_widths, 1):
            col_letter = get_column_letter(c_idx)
            ws.column_dimensions[col_letter].width = w

    # =========================================================
    # SHEET 1: TỔNG QUAN VÀ NGUYÊN TẮC
    # =========================================================
    ws0 = wb.create_sheet(title='Tong_Quan_Kien_Truc')
    ws0.views.sheetView[0].showGridLines = True
    ws0.merge_cells('A1:F1')
    ws0['A1'] = 'KHUNG PHÂN PHỐI CHƯƠNG TRÌNH GIÁO DỤC AI PHỔ THÔNG (QĐ 2422/QĐ-BGDĐT)'
    ws0['A1'].font = font_title
    ws0['A1'].alignment = align_center
    ws0.row_dimensions[1].height = 28

    ws0.merge_cells('A2:F2')
    ws0['A2'] = 'Thiết kế đối chiếu đồng thời cho Lớp 1 (Khởi đầu Tiểu học) và Lớp 6 (Bản lề THCS)'
    ws0['A2'].font = font_subtitle
    ws0['A2'].alignment = align_center
    ws0.row_dimensions[2].height = 18

    headers0 = ['Khối lớp', 'Cấp học', 'Khung thời lượng', 'Cơ cấu 4 mạch nội dung', 'Đặc trưng phương pháp', 'Sản phẩm đầu ra kỳ vọng']
    for c_idx, h in enumerate(headers0, 1):
        c = ws0.cell(4, c_idx, h)
        c.font = font_th
        c.fill = fill_th
        c.alignment = align_center
        c.border = border_cell
    ws0.row_dimensions[4].height = 28

    overview_rows = [
        ['LỚP 1', 'Tiểu học', '12 tiết Cốt lõi', 'Mạch A (4t) + Mạch B (2t) + Mạch C (3t) + Mạch D (3t)', 'Trực quan, sinh động, thẻ tranh, đóng vai, không cần tài khoản riêng, ưu tiên thiết bị dùng chung', 'Nhận biết AI không có cảm xúc thật; không dùng AI làm việc xấu; phân loại máy thông minh'],
        ['LỚP 1', 'Tiểu học', '36 tiết Toàn diện', 'Mạch A (8t) + Mạch B (6t) + Mạch C (10t) + Mạch D (10t) + Đánh giá (2t)', 'Trải nghiệm đa giác quan, trò chơi không cắm điện (Unplugged AI), tạo mô hình giấy, kịch bản tương tác', 'Bộ sưu tập tranh vẽ AI tốt quanh em; đóng vai trợ lý ảo; phân loại mẫu đồ vật qua thẻ hình'],
        ['LỚP 6', 'THCS', '12 tiết Cốt lõi', 'Mạch A (3t) + Mạch B (2t) + Mạch C (4t) + Mạch D (3t)', 'Logic, khoa học, kiểm chứng; bắt buộc ghi nhật ký câu lệnh (prompt log) và lưu nguồn dữ liệu', 'Nắm vững kiến trúc Dữ liệu - Thuật toán - Mô hình; nhận diện ranh giới nên/không nên dùng AI'],
        ['LỚP 6', 'THCS', '36 tiết Toàn diện', 'Mạch A (5t) + Mạch B (5t) + Mạch C (11t) + Mạch D (11t) + Đánh giá (4t)', 'Phương pháp dự án (PBL), điều tra thực tế, thu thập dữ liệu thật, gán nhãn, huấn luyện mô hình trực quan', 'Mô hình học máy trực quan nhận diện đồ vật/cử chỉ; sản phẩm Scratch AI học đường; Triển lãm AI']
    ]

    for r_idx, row in enumerate(overview_rows, 5):
        for c_idx, val in enumerate(row, 1):
            cell = ws0.cell(r_idx, c_idx, val)
            cell.font = font_cell
            cell.border = border_cell
            cell.alignment = align_top_center if c_idx in [1, 2, 3] else align_top_left
            cell.fill = fill_white if r_idx % 2 != 0 else fill_alt
        ws0.row_dimensions[r_idx].height = 42

    col_w0 = [10, 14, 18, 28, 36, 36]
    for c_idx, w in enumerate(col_w0, 1):
        ws0.column_dimensions[get_column_letter(c_idx)].width = w

    # =========================================================
    # SHEET 2: LỚP 1 - KHUNG 12 TIẾT CỐT LÕI (BẮT BUỘC)
    # =========================================================
    ws1_12 = wb.create_sheet(title='Lop_1_12_Tiet')
    setup_sheet_header(ws1_12,
        'KẾ HOẠCH BÀI DẠY CHUYÊN ĐỀ GIÁO DỤC AI BẮT BUỘC - LỚP 1 (12 TIẾT CỐT LÕI)',
        'Thời lượng: 12 tiết/năm học dành cho nội dung cốt lõi | Bố trí trong kế hoạch giáo dục 2 buổi/ngày')

    l1_12_data = [
        ['1', 'Tư duy lấy con người làm trung tâm', 'Bài 1: Cảm xúc của em và phản ứng của máy', 'Nêu ví dụ về cảm xúc con người (vui, buồn, sợ hãi...); nhận ra con người có cảm xúc thật còn AI thì không (chỉ mô phỏng).', 'Cốt lõi', 'Tranh ảnh thẻ cảm xúc, video ngắn robot biểu cảm'],
        ['2', 'Tư duy lấy con người làm trung tâm', 'Bài 2: Nụ cười của Robot do ai lập trình?', 'Nhận biết biểu hiện cảm xúc của AI (cười, chào) là do con người lập trình/thiết kế trước; AI không tự vui buồn.', 'Cốt lõi', 'Mô hình robot giấy, kịch bản đóng vai trò chuyện'],
        ['3', 'Các kĩ thuật và ứng dụng AI', 'Bài 3: Đôi mắt và đôi tai của thiết bị thông minh', 'Nhận biết AI quanh em; nhận ra thiết bị thông minh có các bộ phận như con người: Camera là "mắt", Micro là "tai".', 'Cốt lõi', 'Thiết bị thông minh dùng chung của lớp, máy chiếu'],
        ['4', 'Các kĩ thuật và ứng dụng AI', 'Bài 4: Trò chuyện cùng trợ lý thông minh', 'Nhận diện trợ lý ảo quen thuộc; nhận biết AI hiểu lệnh đơn giản và trò chuyện theo kịch bản định sẵn dưới sự giám sát.', 'Cốt lõi', 'Loa thông minh/máy tính giáo viên mô phỏng'],
        ['5', 'Tư duy lấy con người làm trung tâm', 'Bài 5: Những thiết bị AI giúp ích quanh em', 'Kể tên thiết bị có sử dụng AI (điện thoại thông minh, loa thông minh); mô tả công dụng giúp cuộc sống tiện lợi hơn.', 'Cốt lõi', 'Bộ thẻ tranh thiết bị gia đình, phiếu ghép nối'],
        ['6', 'Tư duy lấy con người làm trung tâm', 'Bài 6: Cảm xúc AI giúp giao tiếp thân thiện', 'Nêu được cách AI thể hiện giọng nói thân thiện, mặt cười giúp con người cảm thấy gần gũi, thoải mái khi hợp tác.', 'Cốt lõi', 'File âm thanh giọng nói robot vui vẻ, thân thiện'],
        ['7', 'Đạo đức AI', 'Bài 7: Máy thông minh làm việc tốt', 'Nêu ví dụ con người sử dụng AI đúng cách vì mục đích tốt đẹp (giúp học tập, chỉ đường, hỗ trợ bác sĩ).', 'Cốt lõi', 'Tranh kể chuyện: Bác sĩ robot, Trợ lý tìm đường'],
        ['8', 'Đạo đức AI', 'Bài 8: Không dùng thiết bị thông minh làm việc xấu', 'Nhận biết hành vi dùng AI gây hại cho người khác; hiểu rằng tuyệt đối không dùng AI để làm việc xấu hoặc trêu chọc bạn.', 'Cốt lõi', 'Tình huống đóng vai ứng xử đúng mực trong lớp'],
        ['9', 'Thiết kế hệ thống AI', 'Bài 9: Máy thông minh học từ ví dụ', 'Nêu ví dụ AI "học" từ hình ảnh hoặc thông tin con người cung cấp (AI học nhận biết quả cam qua nhiều bức ảnh quả cam).', 'Cốt lõi', 'Bộ thẻ hình hoa quả mẫu, hộp phân loại trực quan'],
        ['10', 'Thiết kế hệ thống AI', 'Bài 10: Cùng dạy máy thông minh học đúng', 'Trải nghiệm đưa các ví dụ mẫu chuẩn xác để "dạy" mô hình phân biệt hình tròn và hình vuông; máy học từ ví dụ con người đưa.', 'Cốt lõi', 'Phần mềm trực quan không tài khoản (Quick Draw / Teachable Machine)'],
        ['11', 'Thiết kế hệ thống AI', 'Bài 11: Máy làm một việc và máy làm nhiều việc', 'Xếp được máy thông minh vào 2 nhóm: Nhóm chỉ làm được 1 việc (nhận biết ảnh) và nhóm làm được nhiều việc khác nhau.', 'Cốt lõi', 'Phiếu phân loại dán sticker (Máy đơn năng vs Đa năng)'],
        ['12', 'Tích hợp 4 mạch', 'Bài 12: Ngày hội: Em làm chủ công nghệ', 'Báo cáo tranh vẽ người bạn AI tương lai; khẳng định con người làm chủ và sử dụng máy thông minh vì việc tốt.', 'Cốt lõi', 'Giá trưng bày tranh vẽ, sticker khen thưởng tiến bộ']
    ]
    populate_table(ws1_12, l1_12_data)

    # =========================================================
    # SHEET 3: LỚP 1 - KHUNG 36 TIẾT TOÀN DIỆN (CẢ NĂM HỌC)
    # =========================================================
    ws1_36 = wb.create_sheet(title='Lop_1_36_Tiet')
    setup_sheet_header(ws1_36,
        'KẾ HOẠCH GIÁO DỤC TOÀN DIỆN MÔN TRÍ TUỆ NHÂN TẠO (AI) - LỚP 1 (36 TIẾT/35 TUẦN)',
        'Tích hợp 12 tiết Cốt lõi bắt buộc + 20 tiết Mở rộng trải nghiệm + 4 tiết Đánh giá định kỳ & Báo cáo')

    l1_36_data = [
        # HỌC KỲ I (18 tiết)
        ['1', 'Tư duy lấy con người làm trung tâm', 'Bài 1: Cảm xúc của em và cảm xúc của bạn bè', 'Nhận diện các cảm xúc vui, buồn, ngạc nhiên, tức giận trong đời sống hàng ngày.', 'Cốt lõi', 'Bộ thẻ cảm xúc mặt cười/mặt mếu'],
        ['2', 'Tư duy lấy con người làm trung tâm', 'Bài 2: Robot có biết buồn như em không?', 'Phân biệt con người có cảm xúc thật, AI chỉ mô phỏng chứ không có cảm xúc.', 'Cốt lõi', 'Video ngắn chú robot diễn xuất'],
        ['3', 'Tư duy lấy con người làm trung tâm', 'Bài 3: Trò chơi đóng vai Robot biết cười', 'Trải nghiệm đóng vai Robot phản hồi theo kịch bản quy ước trước.', 'Mở rộng', 'Mũ hóa trang robot, thẻ lệnh cử chỉ'],
        ['4', 'Tư duy lấy con người làm trung tâm', 'Bài 4: Bàn tay con người lập trình nụ cười Robot', 'Nhận biết AI thể hiện cảm xúc là do con người lập trình sẵn; con người tạo ra AI.', 'Cốt lõi', 'Tranh vẽ kỹ sư điều khiển máy tính'],
        ['5', 'Tư duy lấy con người làm trung tâm', 'Bài 5: AI nói lời yêu thương giúp con người vui vẻ', 'Hiểu rằng biểu hiện thân thiện của AI giúp giao tiếp tự nhiên và gần gũi hơn.', 'Mở rộng', 'Loa phát câu chào hỏi đáng yêu'],
        ['6', 'Các kĩ thuật và ứng dụng AI', 'Bài 6: Khám phá "Mắt thần" Camera của máy', 'Nhận biết Camera là "mắt", AI có khả năng xử lý hình ảnh nhận diện đồ vật.', 'Cốt lõi', 'Webcam lớp học, đồ chơi con vật'],
        ['7', 'Các kĩ thuật và ứng dụng AI', 'Bài 7: Khám phá "Tai thính" Micro của máy', 'Nhận biết Micro là "tai", AI có khả năng xử lý âm thanh phân biệt tiếng động.', 'Cốt lõi', 'Micro, âm thanh tiếng mưa, tiếng còi'],
        ['8', 'Các kĩ thuật và ứng dụng AI', 'Bài 8: Trò chơi: Máy nghe lệnh tìm đồ vật', 'Nhận biết AI hiểu mệnh lệnh đơn giản (ví dụ: bật đèn, phát bài hát thiếu nhi).', 'Cốt lõi', 'Ứng dụng nhận diện giọng nói giáo viên'],
        ['9', 'Đánh giá định kỳ', 'Bài 9: Kiểm tra, đánh giá giữa Học kỳ I', 'Đánh giá mức độ nhận biết về cảm xúc con người vs máy và các giác quan của máy.', 'Đánh giá', 'Phiếu bài tập hình ảnh tô màu'],
        ['10', 'Tư duy lấy con người làm trung tâm', 'Bài 10: Đi tìm thiết bị AI trong gia đình', 'Kể tên sản phẩm có AI: máy hút bụi thông minh, tivi nhận diện giọng nói.', 'Cốt lõi', 'Mô hình ngôi nhà thông minh cắt dán'],
        ['11', 'Tư duy lấy con người làm trung tâm', 'Bài 11: AI đã giúp cả nhà em như thế nào?', 'Mô tả công dụng thiết bị AI giúp tiết kiệm thời gian cho bố mẹ.', 'Cốt lõi', 'Tranh vẽ sinh hoạt gia đình'],
        ['12', 'Đạo đức AI', 'Bài 12: Những việc tốt chú Robot có thể làm', 'Nêu ví dụ AI làm việc tốt giúp đỡ con người: bác sĩ AI, người máy cứu hỏa.', 'Cốt lõi', 'Video cứu hộ có robot hỗ trợ'],
        ['13', 'Đạo đức AI', 'Bài 13: Vẽ tranh: Người bạn AI làm việc tốt quanh em', 'Sáng tạo tranh vẽ ý tưởng thiết bị thông minh giúp đỡ người khuyết tật.', 'Mở rộng', 'Giấy vẽ A4, sáp màu'],
        ['14', 'Đạo đức AI', 'Bài 14: Khi nào thiết bị thông minh bị dùng sai?', 'Nhận diện việc dùng AI làm hại người khác; tuyệt đối không dùng sai.', 'Cốt lõi', 'Tình huống ứng xử đạo đức'],
        ['15', 'Đạo đức AI', 'Bài 15: Quy tắc vàng: Dùng máy đúng giờ, đúng việc', 'Hình thành thói quen sử dụng thiết bị số an toàn, bảo vệ mắt và sức khỏe.', 'Mở rộng', 'Bảng thời gian biểu sử dụng máy'],
        ['16', 'Tư duy lấy con người làm trung tâm', 'Bài 16: Góc kể chuyện: Chú Robot biết lắng nghe', 'Củng cố tư duy con người làm chủ và phẩm chất nhân ái trong xã hội số.', 'Mở rộng', 'Truyện tranh giáo dục AI'],
        ['17', 'Ôn tập', 'Bài 17: Ôn tập chuyên đề Học kỳ I', 'Tổng kết: Cảm xúc, Giác quan và Hành vi tốt khi sử dụng AI.', 'Ôn tập', 'Trò chơi hái hoa dân chủ'],
        ['18', 'Đánh giá định kỳ', 'Bài 18: Kiểm tra, đánh giá cuối Học kỳ I', 'Đánh giá hồ sơ tranh vẽ và khả năng phân biệt hành vi đúng/sai khi dùng AI.', 'Đánh giá', 'Bảng kiểm quan sát hành vi'],

        # HỌC KỲ II (18 tiết)
        ['19', 'Thiết kế hệ thống AI', 'Bài 19: Làm sao máy biết quả táo màu đỏ?', 'Nhận biết máy học nhận dạng từ hình ảnh ví dụ do người nạp vào.', 'Cốt lõi', 'Quả táo thật và bộ tranh quả táo'],
        ['20', 'Thiết kế hệ thống AI', 'Bài 20: Càng nhiều ví dụ, máy càng học giỏi', 'Hiểu rằng cần nhiều ví dụ đúng và khác nhau để AI trả lời chuẩn.', 'Mở rộng', 'Tập ảnh mẫu chó và mèo nhiều góc chụp'],
        ['21', 'Thiết kế hệ thống AI', 'Bài 21: Trò chơi: Em làm giáo viên dạy Robot', 'Thực hành cung cấp thẻ mẫu cho robot nhận diện phân loại đồ vật.', 'Cốt lõi', 'Hộp phân loại mẫu trực quan'],
        ['22', 'Thiết kế hệ thống AI', 'Bài 22: Thử tài chú Robot: Đoán hình con vật', 'Trải nghiệm tình huống máy đoán đúng và máy đoán nhầm khi thiếu ảnh mẫu.', 'Mở rộng', 'Màn hình tương tác phân loại con vật'],
        ['23', 'Thiết kế hệ thống AI', 'Bài 23: Sửa sai cho Robot bằng cách thêm ảnh mẫu', 'Hiểu rằng khi máy đoán sai, con người cần bổ sung ví dụ đúng để sửa cho máy.', 'Mở rộng', 'Thẻ ảnh bổ sung chỉnh lỗi'],
        ['24', 'Thiết kế hệ thống AI', 'Bài 24: Nhận biết máy thông minh đơn năng', 'Nhận biết máy chỉ làm được 1 việc duy nhất (camera nhận diện khuôn mặt).', 'Cốt lõi', 'Tranh các thiết bị đơn năng'],
        ['25', 'Thiết kế hệ thống AI', 'Bài 25: Khám phá máy thông minh đa năng', 'Nhận biết máy làm được nhiều việc khác nhau (điện thoại thông minh).', 'Cốt lõi', 'Tranh các thiết bị đa năng'],
        ['26', 'Thiết kế hệ thống AI', 'Bài 26: Xếp hàng cho các loại máy thông minh', 'Xếp máy thông minh vào 2 nhóm: Nhóm làm 1 việc và nhóm làm nhiều việc.', 'Cốt lõi', 'Phiếu phân loại dán nhãn nhóm'],
        ['27', 'Đánh giá định kỳ', 'Bài 27: Kiểm tra, đánh giá giữa Học kỳ II', 'Đánh giá năng lực hiểu về cách máy học từ ví dụ và phân loại máy thông minh.', 'Đánh giá', 'Thao tác phân loại thẻ tranh'],
        ['28', 'Các kĩ thuật và ứng dụng AI', 'Bài 28: Trải nghiệm AI nhận diện nét vẽ nét chữ', 'Khám phá AI đoán nét vẽ nghuệch ngoạc của học sinh thành bức tranh đẹp.', 'Mở rộng', 'AutoDraw trực quan trên bảng tương tác'],
        ['29', 'Các kĩ thuật và ứng dụng AI', 'Bài 29: AI giúp biến nét vẽ thành giai điệu', 'Trải nghiệm âm thanh số khi AI tự tạo nhạc nền theo cảm xúc vui tươi.', 'Mở rộng', 'Ứng dụng Chrome Music Lab'],
        ['30', 'Thiết kế hệ thống AI', 'Bài 30: Khởi động Dự án: Người bạn Robot của em', 'Lên ý tưởng thiết kế một mô hình Robot giấy làm việc tốt cho trường lớp.', 'Mở rộng', 'Bìa carton, kéo thủ công, keo dán'],
        ['31', 'Thiết kế hệ thống AI', 'Bài 31: Chế tạo mô hình Robot thông minh', 'Tạo hình các bộ phận của robot: mắt camera, tai micro, màn hình cười.', 'Mở rộng', 'Nguyên vật liệu tái chế'],
        ['32', 'Thiết kế hệ thống AI', 'Bài 32: Dạy cho Robot nhận biết bạn bè trong lớp', 'Vẽ tranh các bạn mẫu để dán vào bộ nhớ học tập của chú Robot giấy.', 'Mở rộng', 'Bộ sưu tập tranh vẽ chân dung'],
        ['33', 'Thiết kế hệ thống AI', 'Bài 33: Thử nghiệm kịch bản chào hỏi của Robot', 'Tập nói câu lệnh và cho robot phát lời chào thân thiện, lễ phép.', 'Mở rộng', 'Đóng vai giao tiếp'],
        ['34', 'Tích hợp 4 mạch', 'Bài 34: Ngày hội công nghệ nhí: Gian hàng AI của em', 'Trưng bày mô hình robot giấy và bộ sưu tập ví dụ huấn luyện của học sinh.', 'Mở rộng', 'Không gian triển lãm lớp học'],
        ['35', 'Ôn tập', 'Bài 35: Tổng kết: Em tự tin làm chủ công nghệ', 'Hệ thống hóa toàn bộ 4 mạch kiến thức Lớp 1, sẵn sàng lên Lớp 2.', 'Ôn tập', 'Video tổng kết hoạt động năm học'],
        ['36', 'Đánh giá định kỳ', 'Bài 36: Kiểm tra, đánh giá cuối Học kỳ II', 'Đánh giá tổng hợp hồ sơ sản phẩm dự án và nhật ký trải nghiệm Lớp 1.', 'Đánh giá', 'Bảng tiêu chí đánh giá sản phẩm']
    ]
    populate_table(ws1_36, l1_36_data)

    # =========================================================
    # SHEET 4: LỚP 6 - KHUNG 12 TIẾT CỐT LÕI (BẮT BUỘC)
    # =========================================================
    ws6_12 = wb.create_sheet(title='Lop_6_12_Tiet')
    setup_sheet_header(ws6_12,
        'KẾ HOẠCH BÀI DẠY CHUYÊN ĐỀ GIÁO DỤC AI BẮT BUỘC - LỚP 6 (12 TIẾT CỐT LÕI)',
        'Thời lượng: 12 tiết/năm học dành cho nội dung cốt lõi | Chuẩn hóa phương pháp Logic, Khoa học và Kiểm chứng')

    l6_12_data = [
        ['1', 'Tư duy lấy con người làm trung tâm', 'Bài 1: AI là công cụ, con người ra quyết định', 'Giải thích AI do con người tạo ra, lập trình và điều khiển; AI chỉ hỗ trợ, con người ra quyết định cuối cùng và chịu trách nhiệm.', 'Cốt lõi', 'Máy chiếu, phiếu phân tích tình huống Người - Máy'],
        ['2', 'Tư duy lấy con người làm trung tâm', 'Bài 2: Kỹ năng kiểm chứng kết quả do AI cung cấp', 'Thực hiện kiểm tra lại kết quả của AI bằng cách đối chiếu SGK, nguồn tin cậy; nêu ví dụ con người quyết định với trợ giúp AI.', 'Cốt lõi', 'Máy tính kết nối mạng, phiếu đối chiếu nguồn tin'],
        ['3', 'Tư duy lấy con người làm trung tâm', 'Bài 3: Bảo vệ dữ liệu cá nhân và quyền riêng tư', 'Giải thích dữ liệu cá nhân (ảnh, giọng nói, họ tên, vị trí) cần bảo vệ; trình bày khái niệm quyền riêng tư và tác hại khi lộ lọt dữ liệu.', 'Cốt lõi', 'Bộ tình huống rò rỉ dữ liệu, bảng quy tắc bảo mật'],
        ['4', 'Đạo đức AI', 'Bài 4: Tính hai mặt của các tính năng AI', 'Chỉ ra mặt tích cực và hạn chế của tính năng AI (thu thập dữ liệu giúp gợi ý chính xác nhưng tiềm ẩn nguy cơ mất quyền riêng tư).', 'Cốt lõi', 'Bảng phân tích Lợi ích vs Rủi ro (SWOT đơn giản)'],
        ['5', 'Đạo đức AI', 'Bài 5: Tiêu chuẩn an toàn và minh bạch của ứng dụng AI', 'Đặt các câu hỏi kiểm tra an toàn/minh bạch: "Công cụ này có an toàn không?", "Dữ liệu được lưu ở đâu?", "AI có giải thích được vì sao không?".', 'Cốt lõi', 'Bảng kiểm 5 câu hỏi vàng kiểm tra an toàn AI'],
        ['6', 'Các kĩ thuật và ứng dụng AI', 'Bài 6: Khám phá cách AI học: Dữ liệu và Thuật toán', 'Giải thích 2 thành phần chính để huấn luyện AI là Dữ liệu (văn bản, hình ảnh) và Thuật toán (phương pháp học từ dữ liệu).', 'Cốt lõi', 'Sơ đồ luồng: Dữ liệu + Thuật toán = Mô hình'],
        ['7', 'Các kĩ thuật và ứng dụng AI', 'Bài 7: Tác động của AI đối với bản thân và học tập', 'Nêu ví dụ tác động tích cực và tiêu cực của AI; trình bày lợi ích của AI giúp mở rộng tri thức và rèn kĩ năng khi dùng đúng mực.', 'Cốt lõi', 'Phiếu thảo luận nhóm: Lợi ích và nguy cơ lệ thuộc'],
        ['8', 'Các kĩ thuật và ứng dụng AI', 'Bài 8: Phân biệt ứng dụng có AI và không có AI', 'Phân biệt tính năng có AI và không có AI trong đời sống; kể tên và mô tả chức năng của trợ lý ảo, ứng dụng bản đồ, công cụ dịch.', 'Cốt lõi', 'Bảng so sánh phần mềm truyền thống vs phần mềm AI'],
        ['9', 'Các kĩ thuật và ứng dụng AI', 'Bài 9: Các công nghệ AI quen thuộc trong đời sống', 'Kể tên một số công nghệ AI quen thuộc: Nhận dạng hình ảnh (thị giác máy tính), Chuyển văn bản thành giọng nói và ngược lại (xử lý ngôn ngữ).', 'Cốt lõi', 'Công cụ trải nghiệm nhận dạng giọng nói/hình ảnh'],
        ['10', 'Thiết kế hệ thống AI', 'Bài 10: Ranh giới sử dụng: Khi nào nên và không nên dùng AI?', 'Nêu tình huống quen thuộc nên dùng AI (luyện phát âm ngoại ngữ, gợi ý tài liệu) và không nên dùng (làm bài kiểm tra, quyết định cá nhân).', 'Cốt lõi', 'Trò chơi phân loại tình huống Nên / Không nên'],
        ['11', 'Thiết kế hệ thống AI', 'Bài 11: Giới hạn của hệ thống AI so với con người', 'Trình bày giới hạn của AI so với con người qua các công việc đòi hỏi sự thấu cảm, phán đoán đạo đức, sáng tạo nghệ thuật đích thực.', 'Cốt lõi', 'Phiếu so sánh năng lực: Con người vs Hệ thống AI'],
        ['12', 'Tích hợp 4 mạch', 'Bài 12: Báo cáo chuyên đề: Sử dụng AI thông minh và trách nhiệm', 'Tổng kết chuyên đề 12 tiết; trình bày cam kết sử dụng AI an toàn, có lưu vết câu lệnh (prompt log) và liêm chính.', 'Cốt lõi', 'Hồ sơ minh chứng học tập, bản cam kết liêm chính số']
    ]
    populate_table(ws6_12, l6_12_data)

    # =========================================================
    # SHEET 5: LỚP 6 - KHUNG 36 TIẾT TOÀN DIỆN (CẢ NĂM HỌC)
    # =========================================================
    ws6_36 = wb.create_sheet(title='Lop_6_36_Tiet')
    setup_sheet_header(ws6_36,
        'KẾ HOẠCH GIÁO DỤC TOÀN DIỆN MÔN TRÍ TUỆ NHÂN TẠO (AI) - LỚP 6 (36 TIẾT/35 TUẦN)',
        'Tích hợp 16 YCCĐ Cốt lõi + 8 YCCĐ Mở rộng + Dự án thực hành máy học & Triển lãm sản phẩm số')

    l6_36_data = [
        # HỌC KỲ I (18 tiết)
        ['1', 'Tư duy lấy con người làm trung tâm', 'Bài 1: AI là sản phẩm do con người sáng tạo', 'Giải thích AI do con người tạo ra, lập trình và điều khiển; AI không tự ý thức.', 'Cốt lõi', 'Video lịch sử AI, sơ đồ nguồn gốc AI'],
        ['2', 'Tư duy lấy con người làm trung tâm', 'Bài 2: Con người là người ra quyết định cuối cùng', 'AI chỉ là công cụ hỗ trợ; con người nắm quyền kiểm soát và chịu trách nhiệm.', 'Cốt lõi', 'Tình huống y tế/giao thông AI hỗ trợ người'],
        ['3', 'Tư duy lấy con người làm trung tâm', 'Bài 3: Thực hành kiểm chứng thông tin do AI tạo ra', 'Thực hiện đối chiếu câu trả lời của AI với SGK và nguồn tin cậy trên mạng.', 'Cốt lõi', 'Công cụ AI hỏi đáp, tài liệu SGK chuẩn'],
        ['4', 'Tư duy lấy con người làm trung tâm', 'Bài 4: Kỹ thuật tra cứu đối chiếu chéo nhiều nguồn', 'Kỹ thuật Fact-checking, sử dụng nhiều công cụ tìm kiếm để xác minh tin giả.', 'Mở rộng', 'Trang kiểm chứng tin tức độc lập'],
        ['5', 'Tư duy lấy con người làm trung tâm', 'Bài 5: Nhận diện dữ liệu cá nhân trong thế giới số', 'Giải thích các loại dữ liệu cá nhân cần bảo vệ (họ tên, địa chỉ, ảnh mặt, giọng nói).', 'Cốt lõi', 'Phiếu bóc tách dữ liệu cá nhân nhạy cảm'],
        ['6', 'Tư duy lấy con người làm trung tâm', 'Bài 6: Quyền riêng tư và kỹ năng khử nhận dạng dữ liệu', 'Hiểu quyền riêng tư; thực hành che mặt, xóa thông tin cá nhân trước khi đưa lên mạng.', 'Cốt lõi', 'Công cụ che mờ/khử nhận dạng ảnh số'],
        ['7', 'Đạo đức AI', 'Bài 7: Lợi ích và rủi ro của tính năng thu thập dữ liệu', 'Phân tích mặt tích cực (cá nhân hóa) và hạn chế (nguy cơ lộ bí mật đời tư).', 'Cốt lõi', 'Nghiên cứu trường hợp ứng dụng nghe lén/gợi ý'],
        ['8', 'Đạo đức AI', 'Bài 8: Đặt câu hỏi kiểm tra an toàn và minh bạch ứng dụng', 'Thực hành bộ câu hỏi kiểm tra ứng dụng: nguồn gốc dữ liệu, chính sách riêng tư.', 'Cốt lõi', 'Bảng kiểm đánh giá độ tin cậy phần mềm'],
        ['9', 'Đánh giá định kỳ', 'Bài 9: Kiểm tra, đánh giá giữa Học kỳ I', 'Đánh giá kiến thức: Tư duy con người làm chủ, kiểm chứng và an toàn dữ liệu.', 'Đánh giá', 'Đề kiểm tra thực hành kết hợp trắc nghiệm'],
        ['10', 'Các kĩ thuật và ứng dụng AI', 'Bài 10: Kiến trúc cơ bản: Dữ liệu và Thuật toán trong AI', 'Giải thích 2 thành phần chính để huấn luyện AI: Dữ liệu mẫu và Thuật toán.', 'Cốt lõi', 'Mô hình trực quan luồng học máy'],
        ['11', 'Các kĩ thuật và ứng dụng AI', 'Bài 11: Mối liên hệ giữa huấn luyện và hoạt động thực tế', 'Chỉ ra mối liên hệ giữa dữ liệu đưa vào huấn luyện và phản hồi của công cụ AI.', 'Mở rộng', 'Phần mềm mô phỏng huấn luyện trực quan'],
        ['12', 'Các kĩ thuật và ứng dụng AI', 'Bài 12: Thử nghiệm đối kháng với công cụ AI', 'Đặt cùng câu lệnh cho nhiều công cụ AI khác nhau và so sánh các bước xử lý.', 'Mở rộng', 'So sánh 2 phần mềm hội thoại tự động'],
        ['13', 'Các kĩ thuật và ứng dụng AI', 'Bài 13: Kỹ thuật câu lệnh (prompt) có cấu trúc', 'Thực hành cấu trúc câu lệnh rõ ràng: [Vai trò] + [Bối cảnh] + [Nhiệm vụ cụ thể] + [Định dạng].', 'Mở rộng', 'Biểu mẫu thiết kế câu lệnh chuẩn'],
        ['14', 'Các kĩ thuật và ứng dụng AI', 'Bài 14: Thực hành lưu nhật ký câu lệnh (prompt log)', 'Kỹ năng lưu vết minh chứng: Chụp màn hình câu lệnh, ghi chép nguồn dữ liệu để giải trình.', 'Mở rộng', 'Mẫu sổ tay nhật ký câu lệnh học đường'],
        ['15', 'Các kĩ thuật và ứng dụng AI', 'Bài 15: Tác động đa chiều của AI đến cuộc sống gia đình', 'Phân tích cả mặt tích cực (tiện nghi) và tiêu cực (ít giao tiếp thật).', 'Cốt lõi', 'Cây vấn đề: Tác động của AI đến gia đình'],
        ['16', 'Các kĩ thuật và ứng dụng AI', 'Bài 16: Phân biệt sản phẩm có AI và phần mềm thông thường', 'So sánh máy tính bỏ túi (không AI) vs ứng dụng dịch giọng nói (có AI).', 'Cốt lõi', 'Bảng so sánh tính năng thích ứng'],
        ['17', 'Ôn tập', 'Bài 17: Ôn tập chuyên đề Học kỳ I', 'Tổng kết kiến thức: Tư duy con người, Đạo đức và Kĩ thuật AI; kiểm tra sổ nhật ký câu lệnh.', 'Ôn tập', 'Hệ thống câu hỏi ôn tập tương tác'],
        ['18', 'Đánh giá định kỳ', 'Bài 18: Kiểm tra, đánh giá cuối Học kỳ I', 'Đánh giá sản phẩm thực hành câu lệnh và bài thuyết trình kiểm chứng thông tin.', 'Đánh giá', 'Rubric đánh giá sản phẩm thực hành'],

        # HỌC KỲ II (18 tiết)
        ['19', 'Các kĩ thuật và ứng dụng AI', 'Bài 19: Công nghệ AI trong đời sống thực tiễn Việt Nam', 'Khám phá AI trong nông nghiệp thông minh, bản đồ giao thông tại Việt Nam.', 'Cốt lõi', 'Phóng sự AI nông nghiệp công nghệ cao'],
        ['20', 'Các kĩ thuật và ứng dụng AI', 'Bài 20: Thuật toán gợi ý mạng xã hội và hiện tượng thiên lệch', 'Phân tích tính năng đề xuất video; nguy cơ bị giam trong "bong bóng thông tin".', 'Mở rộng', 'Sơ đồ luồng thuật toán gợi ý video'],
        ['21', 'Thiết kế hệ thống AI', 'Bài 21: Tình huống thực tế nên và không nên sử dụng AI', 'Trình bày và tranh biện quan điểm cá nhân về giới hạn sử dụng AI.', 'Cốt lõi', 'Phiếu tranh biện theo cặp: Nên vs Không nên'],
        ['22', 'Thiết kế hệ thống AI', 'Bài 22: Giới hạn của AI: Vì sao AI khó làm thơ hay bằng người?', 'Giải thích AI học từ quá khứ nên thiếu trải nghiệm sống và sự thấu cảm.', 'Cốt lõi', 'Tác phẩm văn học so sánh: Người viết vs AI'],
        ['23', 'Thiết kế hệ thống AI', 'Bài 23: Hợp tác Người - AI: Mô hình cộng tác tối ưu', 'Đề xuất cách kết hợp: AI làm việc lặp lại xử lý nhanh, con người sáng tạo và phán đoán.', 'Mở rộng', 'Sơ đồ phân vai Người - Máy trong dự án'],
        ['24', 'Thiết kế hệ thống AI', 'Bài 24: Dự án AI Lớp 6: Phân loại rác thông minh học đường', 'Lập kế hoạch dự án nhóm: Xác định bài toán phân loại rác tái chế và rác hữu cơ.', 'Mở rộng', 'Bản kế hoạch dự án nhóm (Canvas)'],
        ['25', 'Thiết kế hệ thống AI', 'Bài 25: Kỹ thuật thu thập tập dữ liệu hình ảnh thực tế', 'Chụp ảnh các loại chai nhựa, vỏ hộp sữa, lá cây trong khuôn viên trường học.', 'Mở rộng', 'Camera điện thoại/webcam, mẫu rác sạch'],
        ['26', 'Thiết kế hệ thống AI', 'Bài 26: Thực hành làm sạch và gán nhãn dữ liệu (Data Labeling)', 'Tổ chức dữ liệu vào 2 thư mục nhãn: [Rac_Tai_Che] và [Rac_Huu_Co]. Loại bỏ ảnh mờ.', 'Mở rộng', 'Phần mềm quản lý tệp, thư mục dữ liệu'],
        ['27', 'Đánh giá định kỳ', 'Bài 27: Kiểm tra, đánh giá giữa Học kỳ II', 'Đánh giá tiến độ dự án: Kiểm tra chất lượng tập dữ liệu mẫu và bảng phân công nhóm.', 'Đánh giá', 'Bảng tiêu chí kiểm tra dữ liệu sạch'],
        ['28', 'Thiết kế hệ thống AI', 'Bài 28: Huấn luyện mô hình nhận diện rác bằng Teachable Machine', 'Tải tập dữ liệu lên nền tảng huấn luyện trực quan no-code; bắt đầu quá trình huấn luyện máy.', 'Mở rộng', 'Nền tảng Google Teachable Machine'],
        ['29', 'Thiết kế hệ thống AI', 'Bài 29: Kiểm thử mô hình và bắt lỗi nhận diện sai', 'Đưa mẫu rác lạ hoặc thay đổi ánh sáng để kiểm tra xem mô hình đoán đúng bao nhiêu %.', 'Mở rộng', 'Phiếu ghi chép tỷ lệ nhận dạng chính xác'],
        ['30', 'Thiết kế hệ thống AI', 'Bài 30: Cải thiện độ chính xác bằng cách bổ sung dữ liệu', 'Bổ sung các góc chụp mới cho các trường hợp máy đoán nhầm; tái huấn luyện mô hình.', 'Mở rộng', 'Tập dữ liệu bổ sung sửa lỗi'],
        ['31', 'Thiết kế hệ thống AI', 'Bài 31: Tích hợp mô hình AI vào phần mềm Scratch', 'Kết nối mô hình đã huấn luyện vào Scratch để điều khiển nhân vật thùng rác tự mở nắp.', 'Mở rộng', 'Phần mềm Scratch kết nối tiện ích AI'],
        ['32', 'Thiết kế hệ thống AI', 'Bài 32: Thiết kế giao diện trải nghiệm người dùng (UX)', 'Thiết kế thông báo âm thanh "Cảm ơn bạn đã bỏ rác đúng nơi", nút bấm điều khiển.', 'Mở rộng', 'Giao diện tương tác người dùng'],
        ['33', 'Thiết kế hệ thống AI', 'Bài 33: Soạn thảo hồ sơ trách nhiệm giải trình của dự án', 'Viết báo cáo: Dự án giải quyết việc gì? Dữ liệu lấy từ đâu? AI có thể đoán sai khi nào?', 'Mở rộng', 'Mẫu báo cáo trách nhiệm giải trình'],
        ['34', 'Tích hợp 4 mạch', 'Bài 34: Triển lãm ngày hội sáng tạo AI học đường', 'Trưng bày gian hàng máy phân loại rác thông minh của các nhóm; thuyết trình sản phẩm.', 'Mở rộng', 'Không gian trưng bày, máy tính demo'],
        ['35', 'Ôn tập', 'Bài 35: Tổng kết chương trình AI Lớp 6: Tự hào công dân số', 'Tổng kết toàn bộ 4 mạch năng lực; tuyên dương tinh thần sáng tạo và liêm chính học thuật.', 'Ôn tập', 'Bản đồ tư duy tổng kết năng lực'],
        ['36', 'Đánh giá định kỳ', 'Bài 36: Kiểm tra, đánh giá cuối Học kỳ II', 'Đánh giá tổng hợp điểm dự án nhóm, hồ sơ lưu vết câu lệnh và bài báo cáo giải trình.', 'Đánh giá', 'Rubric đánh giá dự án tích hợp 4 mạch']
    ]
    populate_table(ws6_36, l6_36_data)

    # =========================================================
    # SHEET 6: TRA CỨU NGUYÊN VĂN YCCĐ LỚP 1 VÀ LỚP 6
    # =========================================================
    ws_ref = wb.create_sheet(title='Tra_Cuu_YCCD_Chuan')
    ws_ref.views.sheetView[0].showGridLines = True
    ws_ref.merge_cells('A1:E1')
    ws_ref['A1'] = 'BẢNG ĐỐI CHIẾU NGUYÊN VĂN YÊU CẦU CẦN ĐẠT (YCCĐ) - LỚP 1 VÀ LỚP 6'
    ws_ref['A1'].font = font_title
    ws_ref['A1'].alignment = align_center
    ws_ref.row_dimensions[1].height = 28

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

    # Save
    out_name = 'Phan_Phoi_Chuong_Trinh_AI_Lop1_va_Lop6_QD2422.xlsx'
    try:
        wb.save(out_name)
        print(f'Successfully updated workbook: {out_name}')
    except PermissionError:
        out_name_v2 = 'Phan_Phoi_Chuong_Trinh_AI_Lop1_va_Lop6_QD2422_v2.xlsx'
        wb.save(out_name_v2)
        print(f'File {out_name} đang được mở trong Excel. Đã lưu thành công bản mới tại: {out_name_v2}')

if __name__ == '__main__':
    build_curriculum_workbook()
