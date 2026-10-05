# -*- coding: utf-8 -*-
"""
Script to generate the Master Skill Matrix (Ma trận 46 kỹ năng AI Tiểu học Lớp 1 - 5)
Formats: Markdown (.md), Excel (.xlsx), Word (.docx)
Compliant with QĐ 2422/QĐ-BGDĐT, CV 5588/BGDĐT-GDPT, UNESCO AI Competency Framework 2024
"""

import os
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# Define 46 skills with group, strand, definition, and grade allocations
SKILLS_DATA = [
    # NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI (7 kỹ năng)
    {
        "stt": 1,
        "nhom": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "nhom_con": "1.1. Tương tác kỹ thuật & Tiếp nhận lệnh",
        "ten": "Nhận diện giao diện AI",
        "dinh_nghia": "Nhận biết và chỉ đúng biểu tượng micro, camera và khung nhận diện khuôn mặt trên màn hình.",
        "mach_nl": "NLc",
        "lop1": {"muc_do": "Mức 1: Quan sát", "loai": "VN-CORE", "noi_dung": "Nhận diện biểu tượng micro, camera và khung viền AI trên máy chiếu lớp học"},
        "lop2": {"muc_do": "Mức 1: Quan sát", "loai": "VN-CORE", "noi_dung": "Nhận biết các nút chức năng AI trên màn hình ứng dụng thông minh"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Chỉ đúng và bấm kích hoạt micro/camera trên phần mềm học tập phòng máy"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-MR", "noi_dung": "Nhận diện các vùng chức năng (hộp lệnh, vùng phản hồi) trên giao diện AI"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Thao tác thành thạo giao diện công cụ AI (Teachable Machine: Webcam/Upload/Preview)"}
    },
    {
        "stt": 2,
        "nhom": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "nhom_con": "1.1. Tương tác kỹ thuật & Tiếp nhận lệnh",
        "ten": "Phát âm câu lệnh chuẩn xác",
        "dinh_nghia": "Phát âm to, rõ ràng, tròn vành rõ chữ trước micro để cảm biến âm thanh thu nhận tối ưu.",
        "mach_nl": "NLc",
        "lop1": {"muc_do": "Mức 1: Quan sát / Bắt chước", "loai": "VN-CORE", "noi_dung": "Nghe cô demo và tập nói to, rõ 1-2 từ đơn giản trước micro lớp"},
        "lop2": {"muc_do": "Mức 1: Thực hành tập thể", "loai": "VN-CORE", "noi_dung": "Luyện phát âm câu lệnh ngắn (3-5 từ) tròn vành rõ chữ theo nhóm"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Tự phát âm câu lệnh trước mic máy tính cá nhân để AI nhận diện chuẩn xác"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-MR", "noi_dung": "Tự điều chỉnh tốc độ, âm lượng khi trợ lý AI không nhận diện được khẩu âm"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-MR", "noi_dung": "Phát âm câu lệnh tiếng Việt/tiếng Anh có ngữ điệu tự nhiên, chính xác"}
    },
    {
        "stt": 3,
        "nhom": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "nhom_con": "1.1. Tương tác kỹ thuật & Tiếp nhận lệnh",
        "ten": "Khai thác AI hỗ trợ học tập",
        "dinh_nghia": "Sử dụng câu lệnh để tra cứu từ mới, luyện phát âm ngoại ngữ và tìm kiếm ý tưởng học bài.",
        "mach_nl": "NLc",
        "lop1": None,
        "lop2": {"muc_do": "Mức 1: Quan sát", "loai": "VN-MR", "noi_dung": "Xem cô giáo hỏi trợ lý ảo phát âm từ vựng tiếng Anh minh họa"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Dùng lệnh giọng nói/gõ chữ tra cứu nghĩa từ mới môn Tiếng Việt, Tiếng Anh"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Nhờ AI gợi ý ý tưởng làm bài tập làm văn, vẽ tranh đề tài lịch sử/tự nhiên"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Sử dụng AI như bạn học hỗ trợ giải thích hiện tượng khoa học và lập dàn ý"}
    },
    {
        "stt": 4,
        "nhom": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "nhom_con": "1.2. Kỹ thuật câu lệnh & Tinh chỉnh tương tác",
        "ten": "Cấu trúc câu lệnh tường minh (Prompting)",
        "dinh_nghia": "Thiết lập câu lệnh hoàn chỉnh gồm: vai trò, bối cảnh, nhiệm vụ cụ thể và giới hạn đầu ra.",
        "mach_nl": "NLc",
        "lop1": None,
        "lop2": None,
        "lop3": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-MR", "noi_dung": "Nhận biết câu lệnh đủ ý (Ai? Làm gì?) giúp máy hiểu nhanh hơn câu nói cộc lốc"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Thực hành cấu trúc câu lệnh 3 thành phần: Vai trò + Nhiệm vụ + Kết quả cần"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-MR", "noi_dung": "Thiết lập câu lệnh 4 thành phần: Vai trò, Bối cảnh, Nhiệm vụ cụ thể, Giới hạn đầu ra"}
    },
    {
        "stt": 5,
        "nhom": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "nhom_con": "1.2. Kỹ thuật câu lệnh & Tinh chỉnh tương tác",
        "ten": "Thiết kế câu lệnh kèm ví dụ (Few-shot)",
        "dinh_nghia": "Cung cấp 1–2 mẫu chuẩn ngay trong câu lệnh để định hướng AI sinh kết quả đúng quy cách.",
        "mach_nl": "NLc",
        "lop1": None,
        "lop2": None,
        "lop3": None,
        "lop4": {"muc_do": "Mức 1: Quan sát / So sánh", "loai": "VN-MR", "noi_dung": "Quan sát so sánh: Câu lệnh không có mẫu vs Câu lệnh kèm 1 ví dụ mẫu minh họa"},
        "lop5": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Viết câu lệnh kèm 1-2 mẫu chuẩn để định hướng AI sinh thơ/câu đố đúng thể thơ"}
    },
    {
        "stt": 6,
        "nhom": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "nhom_con": "1.2. Kỹ thuật câu lệnh & Tinh chỉnh tương tác",
        "ten": "Tinh chỉnh câu lệnh đa vòng",
        "dinh_nghia": "Đọc kết quả của AI và viết tiếp câu lệnh bổ sung để nắn chỉnh phản hồi cho đến khi đạt yêu cầu.",
        "mach_nl": "NLc",
        "lop1": None,
        "lop2": {"muc_do": "Mức 1: Quan sát", "loai": "VN-MR", "noi_dung": "Xem cô giáo nói câu lệnh lần 2 rõ hơn khi trợ lý ảo chưa hiểu lệnh lần 1"},
        "lop3": {"muc_do": "Mức 1: Quan sát / Thảo luận", "loai": "VN-MR", "noi_dung": "Đọc câu trả lời của AI và thảo luận xem cần yêu cầu thêm gì để máy trả lời tốt hơn"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Nhập tiếp câu lệnh bổ sung ('Hãy viết ngắn hơn', 'Hãy thêm 2 ví dụ') để nắn chỉnh"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-MR", "noi_dung": "Đối thoại 2-3 vòng liên tục với AI để cải tiến sản phẩm đầu ra đạt chuẩn yêu cầu"}
    },
    {
        "stt": 7,
        "nhom": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "nhom_con": "1.2. Kỹ thuật câu lệnh & Tinh chỉnh tương tác",
        "ten": "Thực hành giao tiếp số văn minh",
        "dinh_nghia": "Sử dụng ngôn từ lịch thiệp, tôn trọng và văn hóa khi tương tác với các hệ thống AI.",
        "mach_nl": "NLb",
        "lop1": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Hình thành thói quen nói lời lễ phép, không la hét trước thiết bị thông minh"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Nhận biết không dùng lời lẽ thô tục, quát mắng khi ra lệnh cho trợ lý ảo"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Thực hành gõ câu lệnh có chủ vị, lịch sự và đúng chuẩn mực học đường"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Duy trì văn hóa giao tiếp tôn trọng, lịch thiệp trên mọi ứng dụng AI"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Gương mẫu trong ứng xử số; nhắc nhở bạn bè không trêu chọc, chửi bới AI"}
    },

    # NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ (10 kỹ năng)
    {
        "stt": 8,
        "nhom": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "nhom_con": "2.1. Bảo mật dữ liệu & Ứng phó sự cố",
        "ten": "Phân loại thông tin cá nhân cần bảo mật",
        "dinh_nghia": "Nhận diện và giữ bí mật tuyệt đối họ tên, ngày sinh, địa chỉ, trường lớp, mật khẩu, ảnh mặt trước AI.",
        "mach_nl": "NLb",
        "lop1": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Nhận biết: Họ tên, nhà ở, trường học là bí mật, không kể cho loa thông minh/đồ chơi"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Phân biệt thông tin chung (món ăn thích) vs thông tin riêng tư (số điện thoại, địa chỉ)"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Gạch bỏ thông tin nhạy cảm (mật khẩu, ảnh mặt) trên phiếu bài tập tình huống"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Nhận diện nguy cơ lộ dữ liệu khi điền thông tin gia đình vào ứng dụng AI trực tuyến"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Thiết lập nguyên tắc bảo vệ danh tính số và dữ liệu nhạy cảm trước mọi hệ thống AI"}
    },
    {
        "stt": 9,
        "nhom": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "nhom_con": "2.1. Bảo mật dữ liệu & Ứng phó sự cố",
        "ten": "Thực hành từ chối chia sẻ dữ liệu",
        "dinh_nghia": "Dứt khoát không nhập thông tin nhạy cảm vào các phần mềm hội thoại tự động hay trang mạng lạ.",
        "mach_nl": "NLb",
        "lop1": {"muc_do": "Mức 1: Phản xạ hành vi", "loai": "VN-CORE", "noi_dung": "Dứt khoát nói 'KHÔNG' và gọi người lớn khi robot/thiết bị gặng hỏi thông tin nhà"},
        "lop2": {"muc_do": "Mức 1: Đóng vai xử lý", "loai": "VN-CORE", "noi_dung": "Đóng vai từ chối app trò chơi thông minh yêu cầu cấp quyền vị trí, hình ảnh"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Bấm nút 'Từ chối' (Deny) khi ứng dụng đòi hỏi thông tin cá nhân không cần thiết"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Chủ động thoát khỏi trang web/app AI khi có biểu mẫu thu thập dữ liệu bất thường"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Phản biện và ngăn chặn hành vi dụ dỗ chia sẻ tài khoản, mật khẩu trên mạng"}
    },
    {
        "stt": 10,
        "nhom": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "nhom_con": "2.1. Bảo mật dữ liệu & Ứng phó sự cố",
        "ten": "Quản lý dấu chân kỹ thuật số",
        "dinh_nghia": "Kiểm soát nội dung tương tác trên môi trường mạng để tránh bị thu thập và khai thác dữ liệu hành vi.",
        "mach_nl": "NLb",
        "lop1": None,
        "lop2": None,
        "lop3": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-MR", "noi_dung": "Hiểu rằng mỗi bức ảnh chụp, câu nói trên mạng đều để lại 'dấu chân số' lưu mãi"},
        "lop4": {"muc_do": "Mức 1: Nhận biết / Thảo luận", "loai": "VN-MR", "noi_dung": "Nhận biết công ty công nghệ có thể theo dõi sở thích qua lịch sử tìm kiếm"},
        "lop5": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Kiểm tra lịch sử tìm kiếm và thực hành xóa lịch sử hội thoại trên ứng dụng AI"}
    },
    {
        "stt": 11,
        "nhom": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "nhom_con": "2.1. Bảo mật dữ liệu & Ứng phó sự cố",
        "ten": "Phát hiện nội dung giả mạo (Deepfake)",
        "dinh_nghia": "Phân tích các dấu hiệu bất thường để nhận diện hình ảnh, video, âm thanh do AI làm giả.",
        "mach_nl": "NLb",
        "lop1": None,
        "lop2": {"muc_do": "Mức 1: Nhận biết qua tranh", "loai": "VN-MR", "noi_dung": "Xem tranh nhận biết ảnh nhân vật hoạt hình bị ghép mặt vụng về"},
        "lop3": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-MR", "noi_dung": "Nhận biết video ghép mặt và giọng nói máy tính giả danh người quen trên mạng"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Soi 3 dấu hiệu deepfake: chớp mắt bất thường, viền miệng nhòe, âm thanh giật"},
        "lop5": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Thẩm định video/hình ảnh nghi vấn bằng quy tắc đối chứng trực tiếp với người thật"}
    },
    {
        "stt": 12,
        "nhom": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "nhom_con": "2.1. Bảo mật dữ liệu & Ứng phó sự cố",
        "ten": "Xử lý sự cố an toàn thông tin",
        "dinh_nghia": "Dừng ngay ứng dụng và thực hiện báo cáo kịp thời cho cha mẹ/thầy cô khi gặp nguy cơ mất an toàn.",
        "mach_nl": "NLb",
        "lop1": {"muc_do": "Mức 1: Phản xạ tức thì", "loai": "VN-CORE", "noi_dung": "Ngừng bấm máy và báo ngay cho cô giáo khi màn hình xuất hiện hình ảnh lạ, đáng sợ"},
        "lop2": {"muc_do": "Mức 1: Phản xạ tức thì", "loai": "VN-CORE", "noi_dung": "Tắt màn hình và kể ngay cho bố mẹ khi nhận tin nhắn đe dọa hoặc đòi tiền"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Thực hiện quy trình an toàn 3 bước: Dừng lại -> Tắt mạng -> Báo cáo người lớn"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Biết chụp ảnh màn hình lưu bằng chứng và báo cáo tài khoản lạ với thầy cô"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Hướng dẫn bạn bè quy trình ứng phó khi bị lộ mật khẩu hoặc bị kẻ xấu mạo danh"}
    },
    {
        "stt": 13,
        "nhom": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "nhom_con": "2.2. Liêm chính học thuật & Trách nhiệm xã hội",
        "ten": "Thực hành nguyên tắc đồng thuận",
        "dinh_nghia": "Xác lập ranh giới tài sản cá nhân; hỏi xin phép và chỉ sử dụng tài liệu của bạn khi được đồng ý.",
        "mach_nl": "NLb",
        "lop1": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Hỏi xin phép bạn trước khi chạm vào đồ chơi thông minh của bạn"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Không tự ý lấy ảnh chụp của bạn đưa vào phần mềm chỉnh sửa AI"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Hỏi xin phép bằng lời và được bạn đồng ý mới chụp ảnh bạn làm dữ liệu dạy máy"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Tôn trọng ranh giới riêng tư: Chỉ chia sẻ dữ liệu nhóm khi tất cả thành viên đồng thuận"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Hiểu quyền đồng thuận dữ liệu cá nhân là quy định bắt buộc theo Luật pháp Việt Nam"}
    },
    {
        "stt": 14,
        "nhom": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "nhom_con": "2.2. Liêm chính học thuật & Trách nhiệm xã hội",
        "ten": "Minh bạch tác quyền AI (Attribution)",
        "dinh_nghia": "Dán nhãn ghi rõ 'Tạo bởi AI' đối với sản phẩm do máy tạo ra, không mạo nhận là tự sáng tác.",
        "mach_nl": "NLb",
        "lop1": None,
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-MR", "noi_dung": "Tập thói quen nói rõ với thầy cô: 'Bức tranh này em nhờ máy tính gợi ý vẽ'"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Ghi chú thích nguồn rõ ràng: 'Ý tưởng bài thơ được gợi ý từ trợ lý AI'"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Dán nhãn chuẩn hóa 'Tạo bởi AI' (AI-generated) cho mọi sản phẩm ảnh/chữ do máy làm"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Phân định minh bạch trong báo cáo dự án: Phần nào tự làm, phần nào AI hỗ trợ"}
    },
    {
        "stt": 15,
        "nhom": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "nhom_con": "2.2. Liêm chính học thuật & Trách nhiệm xã hội",
        "ten": "Thực hành liêm chính học thuật",
        "dinh_nghia": "Tự giác làm bài tập độc lập, không sử dụng AI làm thay để gian lận điểm số hay thi cử.",
        "mach_nl": "NLb",
        "lop1": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Bé tự làm bài của mình, không nhờ máy làm thay để cô giáo chấm điểm thật"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Hiểu rằng nếu nhờ máy làm hộ bài tập thì não mình sẽ không phát triển thông minh"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Cam kết tự làm bài kiểm tra; chỉ dùng AI tra cứu sau khi đã tự suy nghĩ hoàn thành bài"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Kiên quyết không sao chép nguyên văn lời giải của AI vào bài tập về nhà"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Tự hào về năng lực sáng tạo thực chất; từ chối mọi hành vi gian lận thi cử bằng AI"}
    },
    {
        "stt": 16,
        "nhom": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "nhom_con": "2.2. Liêm chính học thuật & Trách nhiệm xã hội",
        "ten": "Kiểm soát hành vi không gây hại",
        "dinh_nghia": "Không sử dụng các công cụ AI để chế ảnh bôi nhọ, bắt nạt trực tuyến hoặc làm tổn thương bạn bè.",
        "mach_nl": "NLb",
        "lop1": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Không dùng loa phát tiếng quá to làm phiền ông bà; không dùng máy hù dọa bạn"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Không dùng app chỉnh ảnh méo mó mặt bạn để chọc cười làm bạn buồn khóc"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Thảo luận tình huống: 'Nụ cười của em có làm bạn tổn thương không?' khi chế ảnh AI"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Nhận diện hành vi bắt nạt qua mạng bằng công nghệ AI và dứt khoát không tham gia"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Ký cam kết văn hóa số: Sử dụng công nghệ thông minh vì điều tốt, không gây hại cho ai"}
    },
    {
        "stt": 17,
        "nhom": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "nhom_con": "2.2. Liêm chính học thuật & Trách nhiệm xã hội",
        "ten": "Xây dựng giải pháp AI bao trùm",
        "dinh_nghia": "Hướng ý tưởng ứng dụng AI vào việc phục vụ bình đẳng xã hội, hỗ trợ người khuyết tật và người yếu thế.",
        "mach_nl": "NLa",
        "lop1": {"muc_do": "Mức 1: Cảm thụ", "loai": "VN-MR", "noi_dung": "Xem tranh và nghe câu chuyện robot dẫn đường cho người khiếm thị qua đường"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-MR", "noi_dung": "Nhận biết AI giúp đọc to sách báo cho người già mắt kém hoặc người không biết chữ"},
        "lop3": {"muc_do": "Mức 1: Quan sát / Thảo luận", "loai": "VN-MR", "noi_dung": "Tìm hiểu công cụ AI nhận diện giọng nói giúp bạn khuyết tật tay điều khiển máy tính"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Thiết kế ý tưởng 'Trợ lý AI học tiếng Việt cho các bạn nhỏ vùng cao'"},
        "lop5": {"muc_do": "Mức 3: Vận dụng / Dự án", "loai": "VN-MR", "noi_dung": "Xây dựng đề án nhóm: Ứng dụng AI phân loại rác hoặc hỗ trợ giao tiếp cho người câm điếc"}
    },

    # NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG (9 kỹ năng)
    {
        "stt": 18,
        "nhom": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "nhom_con": "3.1. Phân tích & Bóc tách bản chất",
        "ten": "Phân biệt cảm xúc người và máy",
        "dinh_nghia": "Nhận diện cảm xúc chân thực của con người và phân biệt với tín hiệu mô phỏng do AI lập trình.",
        "mach_nl": "NLa",
        "lop1": {"muc_do": "Mức 1: Nhận biết cốt lõi", "loai": "VN-CORE", "noi_dung": "Con người có cảm xúc thật từ trái tim; AI chỉ là bóng đèn, mặt cười do con người lập trình"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Nhận biết giọng nói ngọt ngào của trợ lý ảo chỉ là sóng âm mô phỏng, máy không biết buồn vui"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Phân tích tình huống: Tại sao robot hỏi thăm ân cần nhưng không thể thay thế mẹ chăm sóc?"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Chống nhân hóa AI: Khẳng định máy móc là công cụ vô tri, không có tâm hồn hay đạo đức"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Biện luận sự khác biệt bản chất: Trí tuệ sinh học giàu trắc ẩn vs Trí tuệ nhân tạo tính toán dữ liệu"}
    },
    {
        "stt": 19,
        "nhom": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "nhom_con": "3.1. Phân tích & Bóc tách bản chất",
        "ten": "Phân biệt thiết bị cơ học và thiết bị AI",
        "dinh_nghia": "Chỉ ra sự khác biệt giữa đồ dùng cơ học (bấm nút cơ) và thiết bị AI (cảm biến tự nhận biết người).",
        "mach_nl": "NLc",
        "lop1": {"muc_do": "Mức 1: Nhận biết trực quan", "loai": "VN-CORE", "noi_dung": "Quạt cơ phải bấm nút mới quay; quạt thông minh tự quay khi nhận biết có người lại gần"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Thùng rác đạp chân cơ học vs Thùng rác cảm ứng tự mở nắp khi em đưa tay lại gần"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Lập bảng so sánh 5 đồ dùng cơ và đồ dùng thông minh tương ứng trong gia đình"},
        "lop4": None,
        "lop5": None
    },
    {
        "stt": 20,
        "nhom": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "nhom_con": "3.1. Phân tích & Bóc tách bản chất",
        "ten": "Phân loại thiết bị đơn nhiệm và đa nhiệm",
        "dinh_nghia": "Phân biệt đồ dùng chỉ làm một việc (cân điện tử) và thiết bị làm nhiều việc (điện thoại thông minh).",
        "mach_nl": "NLd",
        "lop1": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Cân điện tử chỉ đo cân nặng (đơn nhiệm); Điện thoại vừa chụp ảnh, xem giờ, gọi điện (đa nhiệm)"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Xếp các đồ dùng trong gia đình vào 2 rổ: Làm đúng 1 việc vs Làm được nhiều việc"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Phân tích ưu nhược điểm: Robot chuyên dụng hút bụi vs Thiết bị đa năng thông minh"},
        "lop4": None,
        "lop5": None
    },
    {
        "stt": 21,
        "nhom": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "nhom_con": "3.1. Phân tích & Bóc tách bản chất",
        "ten": "So sánh phương thức học tập",
        "dinh_nghia": "So sánh cách con người học qua trải nghiệm sống thực tế vs cách máy học bằng tính toán dữ liệu số hóa.",
        "mach_nl": "NLc",
        "lop1": {"muc_do": "Mức 1: Nhận biết ví dụ", "loai": "VN-MR", "noi_dung": "Em học chữ qua chơi đùa, nghe cô kể chuyện; máy học qua hàng trăm bức tranh cô nạp vào"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Người bị ngã biết đau để lần sau cẩn thận; máy phải được nạp số liệu mới biết đường tránh"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Lập bảng đối chiếu: Người học qua trải nghiệm thực tế vs Máy học qua dữ liệu số"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Phân tích vì sao người chỉ cần nhìn 1 lần là nhớ con voi, máy cần nạp hàng ngàn bức ảnh voi"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Thuyết trình: Não người có khả năng liên tưởng và sáng tạo vượt xa thuật toán máy tính"}
    },
    {
        "stt": 22,
        "nhom": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "nhom_con": "3.2. Kiểm chứng & Thẩm định độ tin cậy",
        "ten": "Phân tích nguyên nhân sai số của AI",
        "dinh_nghia": "Mổ xẻ các lý do kỹ thuật khiến AI nhận diện sai (vật bị che khuất, ảnh mờ, hai đồ vật quá giống nhau).",
        "mach_nl": "NLc",
        "lop1": {"muc_do": "Mức 1: Quan sát", "loai": "VN-CORE", "noi_dung": "Quan sát camera nhận nhầm quả bóng màu cam thành quả cam ăn được vì cùng màu"},
        "lop2": {"muc_do": "Mức 1: Quan sát / Thảo luận", "loai": "VN-CORE", "noi_dung": "Nhận ra máy đoán sai vì ảnh chụp bị tối, mờ hoặc vật mẫu bị ngón tay che khuất"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Thử nghiệm đưa vật mẫu ở các góc chụp khó (ngược sáng, nghiêng) xem máy đoán nhầm"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Phân loại 3 lý do kỹ thuật: Ảnh mờ, thiếu dữ liệu góc chụp, hai vật quá giống nhau"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Đề xuất phương án khắc phục sai số cho mô hình (chụp lại, thêm mẫu, cân bằng ánh sáng)"}
    },
    {
        "stt": 23,
        "nhom": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "nhom_con": "3.2. Kiểm chứng & Thẩm định độ tin cậy",
        "ten": "Kiểm chứng thông tin (Chống ảo giác AI)",
        "dinh_nghia": "Nghi ngờ lành mạnh trước câu trả lời của AI, chủ động đối chiếu chéo với SGK và nguồn tin cậy.",
        "mach_nl": "NLb",
        "lop1": None,
        "lop2": {"muc_do": "Mức 1: Nhận thức ban đầu", "loai": "VN-MR", "noi_dung": "Biết rằng máy móc cũng có lúc nói sai, không được tin tưởng 100% vào mọi điều máy nói"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Mở sách giáo khoa trang tương ứng để kiểm tra lại câu trả lời lịch sử/địa lý của AI"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Thực hiện quy tắc kiểm chứng 2 nguồn: Luôn tra cứu thêm 1 nguồn sách hoặc hỏi thầy cô"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Nhận diện hiện tượng 'Ảo giác AI' (tự bịa chuyện rất tự tin) và lập biên bản sửa lỗi cho AI"}
    },
    {
        "stt": 24,
        "nhom": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "nhom_con": "3.2. Kiểm chứng & Thẩm định độ tin cậy",
        "ten": "Phát hiện thiên lệch thuật toán (Bias)",
        "dinh_nghia": "Nhận diện khi kết quả AI đưa ra bị thiếu công bằng do tập dữ liệu huấn luyện bị lệch mẫu.",
        "mach_nl": "NLb",
        "lop1": None,
        "lop2": {"muc_do": "Mức 1: Quan sát trực quan", "loai": "VN-CORE", "noi_dung": "Quan sát thấy máy chỉ nhận diện được mèo trắng vì cô giáo chỉ nạp ảnh mèo trắng"},
        "lop3": {"muc_do": "Mức 1: Quan sát / Nhận xét", "loai": "VN-CORE", "noi_dung": "Phát hiện máy không nhận ra quả chuối xanh vì bộ dữ liệu mẫu chỉ toàn quả chuối vàng"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Làm thí nghiệm 'Thiên lệch dữ liệu': Cố tình nạp thiếu mẫu và chứng kiến máy đoán lệch"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Đánh giá tính công bằng của dữ liệu; tự bổ sung mẫu đa dạng để xóa bỏ thiên lệch"}
    },
    {
        "stt": 25,
        "nhom": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "nhom_con": "3.2. Kiểm chứng & Thẩm định độ tin cậy",
        "ten": "Đánh giá điểm số tin cậy mô hình",
        "dinh_nghia": "Đọc hiểu chỉ số tin cậy (Confidence Score) để thẩm định mức độ an toàn trước khi sử dụng kết quả.",
        "mach_nl": "NLc",
        "lop1": None,
        "lop2": None,
        "lop3": {"muc_do": "Mức 1: Quan sát thanh đo", "loai": "VN-MR", "noi_dung": "Quan sát thanh phần trăm trên màn hình demo (thanh dài = máy rất chắc chắn)"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Đọc hiểu tỷ lệ: 80% chắc là quả táo, 20% nghi ngờ là quả cà chua trên phần mềm"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Đặt ngưỡng an toàn: Chỉ chấp nhận kết quả khi độ tin cậy >= 85%; dưới mức đó phải soi lại"}
    },
    {
        "stt": 26,
        "nhom": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "nhom_con": "3.2. Kiểm chứng & Thẩm định độ tin cậy",
        "ten": "Đánh giá tính minh bạch của AI",
        "dinh_nghia": "Giải thích lý do con người cần hiểu cách AI đưa ra quyết định để đảm bảo sự an toàn và tin cậy.",
        "mach_nl": "NLb",
        "lop1": None,
        "lop2": None,
        "lop3": {"muc_do": "Mức 1: Nhận thức", "loai": "VN-MR", "noi_dung": "Cần biết lý do vì sao máy tính lại chọn bức tranh này đẹp hơn bức tranh kia"},
        "lop4": {"muc_do": "Mức 1: Thảo luận", "loai": "VN-MR", "noi_dung": "Hiểu rằng máy chấm điểm phải nói rõ tiêu chí chấm thi thì học sinh mới tin phục"},
        "lop5": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Tìm hiểu khái niệm 'Hộp đen AI' và giải thích vì sao bác sĩ không thể tin ngay kết luận của máy"}
    },

    # NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY (9 kỹ năng)
    {
        "stt": 27,
        "nhom": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "nhom_con": "4.1. Nhận thức cơ chế & Vai trò dữ liệu",
        "ten": "Mô tả chức năng cảm biến máy tính",
        "dinh_nghia": "Giải thích được Camera là 'mắt nhìn', Micro là 'tai nghe', Mạng cảm biến là 'xúc giác' của AI.",
        "mach_nl": "NLc",
        "lop1": {"muc_do": "Mức 1: Ẩn dụ trực quan", "loai": "VN-CORE", "noi_dung": "Camera là mắt nhìn, Micro là tai nghe của robot để đón nhận hình ảnh và tiếng nói"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Cảm biến chạm ở mũi robot hút bụi giống xúc giác, giúp robot quay đầu khi gặp tường"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Khám phá các cảm biến trên tablet: cảm biến ánh sáng, cảm biến xoay màn hình"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Giải thích luồng: Cảm biến thu tín hiệu thực tế -> Chuyển thành số liệu -> AI xử lý"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Sơ đồ hóa mối liên hệ giữa các loại cảm biến ngoại vi và thuật toán nhận dạng thông minh"}
    },
    {
        "stt": 28,
        "nhom": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "nhom_con": "4.1. Nhận thức cơ chế & Vai trò dữ liệu",
        "ten": "Xác định vai trò của dữ liệu",
        "dinh_nghia": "Giải thích được mối quan hệ bản chất: máy tính chỉ học và thông minh được khi có tập dữ liệu ví dụ mẫu.",
        "mach_nl": "NLc",
        "lop1": {"muc_do": "Mức 1: Nhận biết qua mẫu", "loai": "VN-CORE", "noi_dung": "Máy tính không tự biết gì cả, nhờ cô giáo cho xem nhiều tranh mẫu máy mới nhận ra đồ vật"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Càng cho máy xem nhiều ví dụ đúng, máy đoán càng chuẩn xác"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Định nghĩa dữ liệu học máy: Là tập hợp hình ảnh, âm thanh, chữ viết để huấn luyện máy"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Khẳng định: 'Dữ liệu là thức ăn của AI' - Dữ liệu sai thì AI phán đoán sai"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Phân tích tác động cốt tử của số lượng và chất lượng dữ liệu đối với mô hình AI"}
    },
    {
        "stt": 29,
        "nhom": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "nhom_con": "4.2. Thu thập & Tiền xử lý dữ liệu",
        "ten": "Thu thập và chọn lọc dữ liệu mẫu",
        "dinh_nghia": "Tìm kiếm, chụp ảnh, thu âm có chọn lọc các tập mẫu đạt chuẩn (rõ nét, đúng chủ đề) để dạy máy.",
        "mach_nl": "NLc",
        "lop1": {"muc_do": "Mức 1: Hoạt động tập thể", "loai": "VN-MR", "noi_dung": "Cùng cô giáo nhặt đồ vật thật (cục tẩy, thước kẻ) xếp vào góc lớp làm mẫu"},
        "lop2": {"muc_do": "Mức 1: Chọn ảnh mẫu", "loai": "VN-MR", "noi_dung": "Cùng nhặt các bức tranh rõ nét bỏ vào rổ tranh làm dữ liệu dạy máy"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Dùng camera chụp 10 bức ảnh đồ dùng học tập theo hướng dẫn của giáo viên"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Thu thập 2 bộ dữ liệu ảnh phân biệt (lá lành vs lá sâu bệnh) đạt chuẩn rõ nét"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Tự thiết kế và chụp bộ dữ liệu 30 ảnh cho 2 nhóm đối tượng phục vụ dự án"}
    },
    {
        "stt": 30,
        "nhom": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "nhom_con": "4.2. Thu thập & Tiền xử lý dữ liệu",
        "ten": "Gán nhãn dữ liệu (Data Labeling)",
        "dinh_nghia": "Thiết lập hệ thống danh mục nhãn chuẩn xác và phân loại đúng từng mẫu vào nhóm tương ứng.",
        "mach_nl": "NLc",
        "lop1": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-MR", "noi_dung": "Đọc tên nhãn dán trên rổ: Rổ 'Chó', Rổ 'Mèo' khi chơi trò phân loại"},
        "lop2": {"muc_do": "Mức 1: Dán sticker trên giấy", "loai": "VN-MR", "noi_dung": "Dán sticker đúng tên con vật dưới các tấm tranh mẫu trước khi đưa cho cô"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Đặt tên nhãn lớp (Class: 'Hộp bút', 'Vở viết') trên phần mềm Teachable Machine"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Phân loại và kéo-thả chính xác từng tệp dữ liệu vào đúng thư mục nhãn"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Xây dựng cây nhãn dữ liệu chuẩn xác, không bị trùng lặp ngữ nghĩa cho bài toán"}
    },
    {
        "stt": 31,
        "nhom": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "nhom_con": "4.2. Thu thập & Tiền xử lý dữ liệu",
        "ten": "Làm sạch dữ liệu (Data Cleaning)",
        "dinh_nghia": "Kiểm tra bộ mẫu và loại bỏ các ảnh mờ, âm thanh tạp hoặc các thẻ bị gán sai nhãn trước khi huấn luyện.",
        "mach_nl": "NLc",
        "lop1": {"muc_do": "Mức 1: Trò chơi nhặt rác", "loai": "VN-MR", "noi_dung": "Nhặt bỏ các bức tranh rách, hình vẽ bậy ra khỏi rổ tranh mẫu"},
        "lop2": {"muc_do": "Mức 1: Phát hiện ảnh lỗi", "loai": "VN-MR", "noi_dung": "Chỉ ra bức ảnh bị chụp mờ nhòe cần loại bỏ trước khi cô nạp vào máy"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Kiểm tra tập ảnh trên máy tính và bấm nút Xóa các ảnh bị rung tay, nhòe sáng"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Soát lỗi gán nhầm nhãn (ảnh chuối nằm trong nhãn cam) và chuyển về đúng chỗ"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Thực hiện quy trình làm sạch dữ liệu chuẩn mực trước khi bấm nút huấn luyện mô hình"}
    },
    {
        "stt": 32,
        "nhom": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "nhom_con": "4.2. Thu thập & Tiền xử lý dữ liệu",
        "ten": "Kiểm soát tính đa dạng của dữ liệu",
        "dinh_nghia": "Thu thập mẫu từ nhiều góc độ, bối cảnh khác nhau để mô hình nhận diện chính xác và công bằng.",
        "mach_nl": "NLc",
        "lop1": None,
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-MR", "noi_dung": "Nhận biết cần nạp cả ảnh mèo trắng, mèo đen, mèo vàng để máy nhận ra mọi loại mèo"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Chụp mẫu vật từ nhiều góc độ: nhìn thẳng, nhìn nghiêng, nhìn từ trên xuống"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Thu thập mẫu trong các điều kiện khác nhau: nền sáng, nền tối, có bóng râm"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Đảm bảo tính đa dạng và công bằng (thu thập mẫu nhiều kích cỡ, màu sắc, nguồn gốc)"}
    },
    {
        "stt": 33,
        "nhom": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "nhom_con": "4.3. Huấn luyện & Tối ưu mô hình",
        "ten": "Phân loại bài toán học máy",
        "dinh_nghia": "Phân biệt bài toán Phân loại đối tượng (cam vs chuối) và bài toán Dự đoán xu hướng (thời tiết mưa/nắng).",
        "mach_nl": "NLc",
        "lop1": None,
        "lop2": {"muc_do": "Mức 1: Trò chơi chia nhóm", "loai": "VN-MR", "noi_dung": "Trò chơi: Nhóm tranh cùng loại (phân loại) vs Đoán xem ngày mai mưa hay nắng (dự đoán)"},
        "lop3": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Phân biệt: Nhận diện khuôn mặt quen/lạ vs Dự đoán chiều cao theo tuổi"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Nhận diện 2 dạng bài toán trong đời sống: Phân loại email rác vs Dự báo nhiệt độ"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Xác định đúng loại bài toán học máy tương ứng với nhu cầu thực tế cần giải quyết"}
    },
    {
        "stt": 34,
        "nhom": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "nhom_con": "4.3. Huấn luyện & Tối ưu mô hình",
        "ten": "Vận hành quy trình 4 bước học máy",
        "dinh_nghia": "Thực hiện thuần thục 4 bước trên phần mềm trực quan: Đặt tên nhãn -> Nạp mẫu -> Dạy máy -> Kiểm thử.",
        "mach_nl": "NLd",
        "lop1": {"muc_do": "Mức 1: Nghe kể chuyện 4 bước", "loai": "VN-MR", "noi_dung": "Câu chuyện 4 bước: 1. Đặt tên -> 2. Xem tranh -> 3. Nhớ bài -> 4. Đố vui nhận diện"},
        "lop2": {"muc_do": "Mức 1: Quan sát cô demo", "loai": "VN-MR", "noi_dung": "Quan sát cô giáo thao tác đủ 4 bước trên phần mềm học máy chiếu lên bảng"},
        "lop3": {"muc_do": "Mức 2: Thực hành nhóm có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Cùng nhóm thực hiện từng bước dưới sự hướng dẫn trực tiếp của giáo viên"},
        "lop4": {"muc_do": "Mức 2: Thực hành cá nhân có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Tự hoàn thành 4 bước trên Teachable Machine với 2 nhãn đơn giản"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Vận hành thuần thục quy trình 4 bước: Đặt nhãn -> Nạp mẫu -> Train -> Test cho dự án riêng"}
    },
    {
        "stt": 35,
        "nhom": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "nhom_con": "4.3. Huấn luyện & Tối ưu mô hình",
        "ten": "Tái huấn luyện mô hình (Retraining)",
        "dinh_nghia": "Nạp bổ sung dữ liệu mới tại những điểm AI nhận diện kém và cho máy học lại để nâng cao độ chính xác.",
        "mach_nl": "NLd",
        "lop1": None,
        "lop2": None,
        "lop3": {"muc_do": "Mức 1: Quan sát cô sửa sai cho máy", "loai": "VN-MR", "noi_dung": "Xem cô nạp thêm 3 bức ảnh con mèo bị nhận nhầm và bấm nút cho máy học lại"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Tìm mẫu bị máy đoán sai -> Bổ sung 5 ảnh góc chụp đó -> Bấm Train lại"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "So sánh tỷ lệ chính xác trước và sau khi tái huấn luyện; ghi chép nhật ký cải tiến mô hình"}
    },

    # NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ (6 kỹ năng)
    {
        "stt": 36,
        "nhom": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "nhom_con": "5.1. Nhận diện vấn đề & Thiết kế ý tưởng",
        "ten": "Xác định bài toán thực tiễn",
        "dinh_nghia": "Phát hiện các khó khăn trong học tập và đời sống (nhặt rác gầm bàn, lau bảng trên cao) có thể áp dụng AI.",
        "mach_nl": "NLd",
        "lop1": {"muc_do": "Mức 1: Quan sát việc nhà", "loai": "VN-CORE", "noi_dung": "Thấy mẹ quét nhà vất vả -> mơ ước có robot hút bụi thông minh phụ giúp"},
        "lop2": {"muc_do": "Mức 1: Nhận diện việc trường lớp", "loai": "VN-CORE", "noi_dung": "Phát hiện việc lau bảng trên cao khó khăn, mong muốn có cánh tay robot lau bảng"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Điều tra các công việc lặp đi lặp lại mệt nhọc ở trường (tưới cây, nhặt lá sân trường)"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Chọn lọc bài toán vừa sức giải quyết bằng AI: Phân loại rác hữu cơ và vô cơ"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Xác định vấn đề cấp thiết của trường/cộng đồng địa phương có thể áp dụng giải pháp AI"}
    },
    {
        "stt": 37,
        "nhom": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "nhom_con": "5.1. Nhận diện vấn đề & Thiết kế ý tưởng",
        "ten": "Mô hình hóa ý tưởng giải pháp",
        "dinh_nghia": "Vẽ tranh, viết kịch bản hoặc vẽ sơ đồ mô tả ý tưởng robot thông minh phục vụ cộng đồng.",
        "mach_nl": "NLd",
        "lop1": {"muc_do": "Mức 1: Vẽ tranh robot mơ ước", "loai": "VN-CORE", "noi_dung": "Vẽ tranh chú robot thông minh giúp mẹ rửa bát, dọn đồ chơi theo trí tưởng tượng"},
        "lop2": {"muc_do": "Mức 1: Kể chuyện theo tranh", "loai": "VN-CORE", "noi_dung": "Kể câu chuyện 3 câu về cách robot nhận diện và giúp đỡ các bạn học sinh khuyết tật"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Vẽ sơ đồ khối đơn giản: Mắt robot thấy gì -> Não robot nghĩ gì -> Tay robot làm gì"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Thiết kế poster dự án AI: Tên giải pháp, Cảm biến sử dụng, Lợi ích cho cộng đồng"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Lập bản đề xuất giải pháp AI hoàn chỉnh: Bài toán, Kế hoạch dữ liệu, Mô hình, Đánh giá"}
    },
    {
        "stt": 38,
        "nhom": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "nhom_con": "5.1. Nhận diện vấn đề & Thiết kế ý tưởng",
        "ten": "Đề xuất giải pháp AI theo ngữ cảnh",
        "dinh_nghia": "Đưa ra ý tưởng ứng dụng AI giải quyết bài toán môi trường hoặc văn hóa tại Việt Nam.",
        "mach_nl": "NLd",
        "lop1": None,
        "lop2": None,
        "lop3": {"muc_do": "Mức 1: Thảo luận ý tưởng", "loai": "VN-MR", "noi_dung": "Ý tưởng: Camera thông minh nhắc nhở bạn nhỏ đội mũ bảo hiểm trước cổng trường"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Đề xuất ý tưởng AI bảo vệ rừng ngập mặn hoặc cảnh báo sớm bão lũ tại Việt Nam"},
        "lop5": {"muc_do": "Mức 3: Vận dụng sáng tạo", "loai": "VN-MR", "noi_dung": "Xây dựng ý tưởng AI nhận diện trang phục các dân tộc Việt Nam hoặc di tích lịch sử"}
    },
    {
        "stt": 39,
        "nhom": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "nhom_con": "5.2. Đồng sáng tạo & Hiện thực hóa giải pháp",
        "ten": "Đồng sáng tạo sản phẩm cùng AI",
        "dinh_nghia": "Kết hợp gợi ý của AI với tư duy cá nhân để phát triển thành tác phẩm sáng tạo hoàn thiện.",
        "mach_nl": "NLc",
        "lop1": None,
        "lop2": {"muc_do": "Mức 1: Quan sát gợi ý nét vẽ", "loai": "VN-MR", "noi_dung": "Quan sát AI gợi ý nét vẽ hoàn chỉnh khi em vẽ phác thảo bông hoa (Quick, Draw!)"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Nhận 3 từ khóa gợi ý từ AI và tự tay viết tiếp thành đoạn văn ngắn giàu cảm xúc"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Dùng AI tạo tranh phong cảnh nền, sau đó tự tay vẽ thêm nhân vật và lồng lời thoại"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Kết hợp AI tạo sinh và tư duy cá nhân để xuất bản một tập truyện tranh số ngắn"}
    },
    {
        "stt": 40,
        "nhom": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "nhom_con": "5.2. Đồng sáng tạo & Hiện thực hóa giải pháp",
        "ten": "Lập trình phản hồi thông minh",
        "dinh_nghia": "Ứng dụng cấu trúc logic Nếu... thì... trên Scratch để lập trình nhân vật tương tác theo quy tắc.",
        "mach_nl": "NLd",
        "lop1": None,
        "lop2": None,
        "lop3": {"muc_do": "Mức 2: Thực hành khối lệnh cơ bản", "loai": "VN-CORE", "noi_dung": "Lắp ghép khối lệnh: 'Nếu phím Cách được bấm -> Mèo Scratch nói Xin chào'"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Lập trình logic: 'Nếu camera nhận diện mặt cười -> Phát tiếng vỗ tay khen ngợi'"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Kết nối mô hình Teachable Machine vào Scratch để điều khiển nhân vật theo cử chỉ tay"}
    },
    {
        "stt": 41,
        "nhom": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "nhom_con": "5.2. Đồng sáng tạo & Hiện thực hóa giải pháp",
        "ten": "Xây dựng mô hình AI hoàn chỉnh",
        "dinh_nghia": "Tự thu thập dữ liệu, dạy máy học trên phần mềm và thử nghiệm tạo ra sản phẩm AI thực tế.",
        "mach_nl": "NLd",
        "lop1": None,
        "lop2": None,
        "lop3": {"muc_do": "Mức 1: Tham gia nạp ảnh", "loai": "VN-MR", "noi_dung": "Đóng góp 3 bức ảnh của bản thân cho mô hình AI nhận diện khẩu trang chung của lớp"},
        "lop4": {"muc_do": "Mức 2: Thực hành theo nhóm", "loai": "VN-CORE", "noi_dung": "Cùng nhóm hoàn thiện sản phẩm AI nhận diện đồ dùng học tập và chạy thử trước lớp"},
        "lop5": {"muc_do": "Mức 3: Dự án thực tế độc lập", "loai": "VN-CORE", "noi_dung": "Tự chủ xây dựng hoàn chỉnh một ứng dụng AI giải quyết bài toán nhỏ và thuyết trình báo cáo"}
    },

    # NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH (5 kỹ năng)
    {
        "stt": 42,
        "nhom": "NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH",
        "nhom_con": "6.1. Tự chủ tư duy & Cân bằng số",
        "ten": "Duy trì tư duy độc lập (Chống ỷ lại)",
        "dinh_nghia": "Tự suy nghĩ và giải quyết vấn đề trước khi tham khảo AI, bảo vệ năng lực tư duy cá nhân.",
        "mach_nl": "NLa",
        "lop1": {"muc_do": "Mức 1: Nhận thức", "loai": "VN-CORE", "noi_dung": "Bé tự suy nghĩ cách xếp đồ chơi vào giỏ, không ngồi chờ đồ chơi tự di chuyển"},
        "lop2": {"muc_do": "Mức 1: Nhận thức", "loai": "VN-CORE", "noi_dung": "Tự tìm đường đi trong mê cung giấy trước khi xem gợi ý của ứng dụng thông minh"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Tự viết dàn ý nháp bài văn ra vở trước khi mở máy tính xem AI gợi ý từ ngữ"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Thực hiện nguyên tắc: '5 phút tự suy nghĩ' trước khi quyết định gõ câu lệnh hỏi AI"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Đánh giá phản biện câu trả lời của AI; giữ vững chính kiến độc lập nếu gợi ý của AI thiếu thuyết phục"}
    },
    {
        "stt": 43,
        "nhom": "NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH",
        "nhom_con": "6.1. Tự chủ tư duy & Cân bằng số",
        "ten": "Ra quyết định sử dụng có điều kiện",
        "dinh_nghia": "Đưa ra quyết định độc lập: chỉ dùng AI khi an toàn/có ích, từ chối dùng khi có nguy cơ rủi ro.",
        "mach_nl": "NLa",
        "lop1": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Chỉ sử dụng máy tính, đồ chơi thông minh khi có sự đồng ý và giám sát của cha mẹ"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Phân biệt việc nên nhờ AI (học phát âm) vs việc không nên nhờ AI (viết hộ chính tả)"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Lập bảng quy ước 'Đèn xanh - Đèn đỏ': Khi nào được dùng AI và khi nào cấm dùng AI"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Tự cân nhắc lợi ích và nguy cơ trước khi cài đặt hoặc cấp quyền cho một app AI mới"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Xây dựng 'Bộ quy tắc sử dụng AI thông thái' cho bản thân và chia sẻ với gia đình"}
    },
    {
        "stt": 44,
        "nhom": "NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH",
        "nhom_con": "6.1. Tự chủ tư duy & Cân bằng số",
        "ten": "Quản trị thời gian tương tác số",
        "dinh_nghia": "Tự giác tắt thiết bị khi hết giờ, cân bằng giữa hoạt động trên màn hình và đời sống thể chất thực tế.",
        "mach_nl": "NLa",
        "lop1": {"muc_do": "Mức 1: Tuân thủ", "loai": "VN-CORE", "noi_dung": "Rời mắt khỏi màn hình ngay khi chuông hẹn giờ 15 phút reo; tập bài tập thể dục mắt"},
        "lop2": {"muc_do": "Mức 1: Tuân thủ", "loai": "VN-CORE", "noi_dung": "Tự giác bấm nút hẹn giờ 20 phút trước khi bắt đầu dùng máy tính bảng học tập"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-MR", "noi_dung": "Viết 'Nhật ký thời gian số': Ghi lại số phút học với máy tính mỗi ngày và cam kết không quá giờ"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Thực hiện nghiêm túc quy tắc 20-20-20 (nhìn xa 20 feet sau 20 phút) để bảo vệ thị lực"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Tự giác cân bằng thời gian sử dụng công nghệ số với vận động thể thao và trò chuyện gia đình"}
    },
    {
        "stt": 45,
        "nhom": "NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH",
        "nhom_con": "6.2. Giám sát & Xác lập trách nhiệm",
        "ten": "Giám sát và kiểm soát hệ thống AI",
        "dinh_nghia": "Giữ vững quyền hạn kiểm tra, can thiệp và phê duyệt quyết định cuối cùng trong mọi việc có AI hỗ trợ.",
        "mach_nl": "NLa",
        "lop1": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Con người là chủ nhân; em có quyền bấm nút TẮT nguồn (OFF) khi đồ chơi chạy sai"},
        "lop2": {"muc_do": "Mức 1: Nhận biết", "loai": "VN-CORE", "noi_dung": "Biết nút dừng khẩn cấp trên robot hút bụi hoặc nút đóng ứng dụng khi phần mềm bị đơ"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Bấm nút Dừng màu đỏ trên phần mềm Scratch khi nhân vật phản hồi sai kịch bản"},
        "lop4": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Giám sát chặt chẽ kết quả của AI và quyết định chấp nhận hay bác bỏ gợi ý của máy"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Xác lập nguyên tắc 'Con người nắm quyền kiểm soát cuối cùng' (Human-in-the-loop)"}
    },
    {
        "stt": 46,
        "nhom": "NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH",
        "nhom_con": "6.2. Giám sát & Xác lập trách nhiệm",
        "ten": "Xác lập trách nhiệm giải trình (Accountability)",
        "dinh_nghia": "Chịu trách nhiệm toàn diện 100% về mọi quyết định và sản phẩm tạo ra, không đổ lỗi cho AI.",
        "mach_nl": "NLa",
        "lop1": {"muc_do": "Mức 1: Nhận thức", "loai": "VN-CORE", "noi_dung": "Làm đổ đồ chơi là do tay em bấm nút, em xin lỗi và dọn dẹp, không đổ lỗi cho chiếc xe"},
        "lop2": {"muc_do": "Mức 1: Nhận thức", "loai": "VN-CORE", "noi_dung": "Bài vẽ bị điểm kém không được thanh minh: 'Tại máy tính gợi ý xấu'"},
        "lop3": {"muc_do": "Mức 2: Thực hành có hướng dẫn", "loai": "VN-CORE", "noi_dung": "Tự chịu trách nhiệm về nội dung bài viết và lỗi chính tả dù có dùng trợ lý AI hỗ trợ"},
        "lop4": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Thảo luận tình huống đạo đức: Nếu xe tự lái gây tai nạn thì trách nhiệm thuộc về ai?"},
        "lop5": {"muc_do": "Mức 3: Thực hành độc lập", "loai": "VN-CORE", "noi_dung": "Tuyên ngôn trách nhiệm: 'Em là người tạo ra sản phẩm - Em chịu trách nhiệm 100% về kết quả'"}
    }
]

def generate_markdown(filepath):
    lines = []
    lines.append("# BẢNG MA TRẬN PHÂN BỔ 46 KỸ NĂNG GIÁO DỤC AI CẤP TIỂU HỌC (LỚP 1 – 5)")
    lines.append("")
    lines.append("> **Căn cứ pháp lý & Chuẩn mực cao nhất:**  ")
    lines.append("> - **Quyết định số 2422/QĐ-BGDĐT** ngày 18/8/2026 của Bộ GD&ĐT ban hành *\"Khung nội dung giáo dục Trí tuệ nhân tạo cho học sinh phổ thông\"*.  ")
    lines.append("> - **Công văn số 5588/BGDĐT-GDPT** ngày 19/8/2026 hướng dẫn triển khai thực tế.  ")
    lines.append("> - **Khung năng lực AI của UNESCO (2024)** & **AI4K12 Five Big Ideas**.  ")
    lines.append("")
    lines.append("> **Mục tiêu ma trận:** Làm căn cứ phân phối chương trình chính thức — quyết định khối lớp nào học kỹ năng nào, ở bài nào, học ở mức độ nào, thuộc luồng Cốt lõi (`VN-CORE` - 12 tiết) hay Mở rộng (`VN-MR` / `INT-ENRICH` - 24 tiết) để suy ra tổng thời lượng 36 tiết/lớp/năm học.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## I. QUY CHUẨN MA TRẬN VÀ 3 NGUYÊN TẮC PHÂN BỔ BẮT BUỘC")
    lines.append("")
    lines.append("### 1. Thang 3 Mức độ yêu cầu (Proficiency Levels):")
    lines.append("- **Mức 1: Quan sát / Nhận biết (Observation / Recognition):** Học sinh tiếp cận qua trải nghiệm thị giác, tranh thẻ, tình huống kể chuyện, trò chơi không cắm điện (Unplugged) hoặc xem giáo viên demo trực quan.")
    lines.append("- **Mức 2: Thực hành có hướng dẫn (Guided Practice):** Học sinh thao tác theo nhóm hoặc cá nhân dưới sự hướng dẫn từng bước của giáo viên (Step-by-step scaffolding).")
    lines.append("- **Mức 3: Thực hành độc lập / Vận dụng (Independent Practice / Application):** Học sinh tự chủ thực hiện thao tác, tự thẩm định kết quả, sáng tạo giải pháp và hoàn thành dự án/bài tập.")
    lines.append("")
    lines.append("### 2. Hai luồng thời lượng (Dual-Track 36 tiết/năm):")
    lines.append("- **`VN-CORE` (Cốt lõi - 12 tiết/năm):** Bắt buộc 100% học sinh, bám sát và phủ kín 100% Yêu cầu cần đạt cốt lõi của Bộ GD&ĐT theo QĐ 2422.")
    lines.append("- **`VN-MR` / `INT-ENRICH` (Mở rộng - 24 tiết/năm):** Nội dung tăng cường, đào sâu kỹ năng, câu lạc bộ, dự án liên môn và làm giàu chuẩn quốc tế.")
    lines.append("")
    lines.append("### 3. Ràng buộc hạ tầng thiết bị (Infrastructure Guardrail):")
    lines.append("- **Lớp 1 – Lớp 2:** Học sinh **hoàn toàn không thao tác máy tính cá nhân**. Mọi kỹ năng thuộc mạch Kỹ thuật (NLc) và Thiết kế hệ thống (NLd) **chỉ được gán mức Mức 1 (Quan sát / Nhận biết)** (giáo viên demo hoặc học sinh chơi thẻ bài Unplugged).")
    lines.append("- **Lớp 3 – Lớp 5:** Bắt đầu chuyển dịch lên **Mức 2 (Thực hành có hướng dẫn)** và **Mức 3 (Thực hành độc lập)** trên máy tính (phối hợp phòng máy môn Tin học).")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## II. BẢNG MA TRẬN CHI TIẾT 46 KỸ NĂNG × 5 KHỐI LỚP")
    lines.append("")

    current_group = ""
    for s in SKILLS_DATA:
        if s["nhom"] != current_group:
            current_group = s["nhom"]
            lines.append(f"### {current_group}")
            lines.append("")
            lines.append("| STT | Tên kỹ năng & Định nghĩa chuẩn hóa | Mạch NL | Lớp 1 (30–35 phút) | Lớp 2 (30–35 phút) | Lớp 3 (35 phút) | Lớp 4 (35 phút) | Lớp 5 (35 phút) |")
            lines.append("| :---: | :--- | :---: | :--- | :--- | :--- | :--- | :--- |")
        
        row_str = f"| **{s['stt']}** | **{s['ten']}**<br>*{s['dinh_nghia']}* | `{s['mach_nl']}` | "
        
        for g_key in ["lop1", "lop2", "lop3", "lop4", "lop5"]:
            cell = s[g_key]
            if cell is None:
                row_str += "- | "
            else:
                track_badge = f"**[{cell['loai']}]**" if cell['loai'] == "VN-CORE" else f"*[{cell['loai']}]*"
                cell_text = f"**{cell['muc_do']}**<br>{track_badge}<br>• {cell['noi_dung']}"
                row_str += cell_text + " | "
        lines.append(row_str)
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## III. BẢNG TỔNG HỢP THỐNG KÊ & SUY LUẬN PHÂN PHỐI CHƯƠNG TRÌNH")
    lines.append("")
    
    # Calculate stats
    stats = {
        "lop1": {"core": 0, "mr": 0, "total": 0},
        "lop2": {"core": 0, "mr": 0, "total": 0},
        "lop3": {"core": 0, "mr": 0, "total": 0},
        "lop4": {"core": 0, "mr": 0, "total": 0},
        "lop5": {"core": 0, "mr": 0, "total": 0},
    }
    for s in SKILLS_DATA:
        for g_key in stats.keys():
            if s[g_key] is not None:
                stats[g_key]["total"] += 1
                if s[g_key]["loai"] == "VN-CORE":
                    stats[g_key]["core"] += 1
                else:
                    stats[g_key]["mr"] += 1

    lines.append("| Chỉ số thống kê kỹ năng | Lớp 1 | Lớp 2 | Lớp 3 | Lớp 4 | Lớp 5 | Toàn cấp Tiểu học |")
    lines.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
    lines.append(f"| **Tổng số kỹ năng kích hoạt** | **{stats['lop1']['total']}** | **{stats['lop2']['total']}** | **{stats['lop3']['total']}** | **{stats['lop4']['total']}** | **{stats['lop5']['total']}** | **46 kỹ năng** |")
    lines.append(f"| • Số lượt kỹ năng Cốt lõi (`VN-CORE`) | {stats['lop1']['core']} | {stats['lop2']['core']} | {stats['lop3']['core']} | {stats['lop4']['core']} | {stats['lop5']['core']} | {sum(stats[k]['core'] for k in stats)} lượt |")
    lines.append(f"| • Số lượt kỹ năng Mở rộng (`VN-MR`) | {stats['lop1']['mr']} | {stats['lop2']['mr']} | {stats['lop3']['mr']} | {stats['lop4']['mr']} | {stats['lop5']['mr']} | {sum(stats[k]['mr'] for k in stats)} lượt |")
    lines.append(f"| **Thời lượng quy chuẩn cả năm** | **36 tiết** | **36 tiết** | **36 tiết** | **36 tiết** | **36 tiết** | **180 tiết** |")
    lines.append(f"| • Tiết Cốt lõi (Bắt buộc theo QĐ 2422) | 12 tiết | 12 tiết | 12 tiết | 12 tiết | 12 tiết | 60 tiết |")
    lines.append(f"| • Tiết Mở rộng (Nova thiết kế thêm) | 24 tiết | 24 tiết | 24 tiết | 24 tiết | 24 tiết | 120 tiết |")
    lines.append("")
    lines.append("### Nhận định quy luật sư phạm:")
    lines.append(f"1. **Tiến trình tăng dần số lượng kỹ năng:** Lớp 1 bắt đầu với {stats['lop1']['total']} kỹ năng cơ bản (chủ yếu là nhận biết và an toàn), phát triển lên {stats['lop2']['total']} kỹ năng ở Lớp 2, {stats['lop3']['total']} kỹ năng ở Lớp 3, và hoàn thiện sâu ở Lớp 4 ({stats['lop4']['total']} kỹ năng) cùng Lớp 5 ({stats['lop5']['total']} kỹ năng).")
    lines.append("2. **Chuyển dịch phương thức học tập theo hạ tầng:**")
    lines.append("   - Lớp 1–2: 100% kỹ năng NLc và NLd ở Mức 1 (Quan sát/Nhận thức). Phương tiện dạy học là tranh ảnh, câu chuyện, vật thật và giáo viên làm mẫu.")
    lines.append("   - Lớp 3: Bản lề chuyển tiếp — học sinh bắt đầu thực hành có hướng dẫn (Mức 2) trên phần mềm học máy phòng máy Tin học.")
    lines.append("   - Lớp 4–5: Phát triển năng lực tự chủ (Mức 3 - Thực hành độc lập), tự làm sạch dữ liệu, tự huấn luyện mô hình Teachable Machine và thực hiện dự án giải quyết vấn đề thực tế.")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated Markdown: {filepath}")

def generate_excel(filepath):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Ma Tran 46 Ky Nang AI L1-5"

    # Set up styles
    font_title = Font(name="Times New Roman", size=15, bold=True, color="1F497D")
    font_sub = Font(name="Times New Roman", size=11, italic=True)
    font_header = Font(name="Times New Roman", size=11, bold=True, color="FFFFFF")
    font_group = Font(name="Times New Roman", size=11, bold=True, color="002060")
    font_cell = Font(name="Times New Roman", size=10)
    font_badge_core = Font(name="Times New Roman", size=9, bold=True, color="C00000")
    font_badge_mr = Font(name="Times New Roman", size=9, bold=True, color="0070C0")

    fill_header = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    fill_group = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
    fill_core = PatternFill(start_color="FDE9D9", end_color="FDE9D9", fill_type="solid")
    fill_mr = PatternFill(start_color="EBF1F5", end_color="EBF1F5", fill_type="solid")

    thin_border = Border(
        left=Side(style='thin', color='BFBFBF'),
        right=Side(style='thin', color='BFBFBF'),
        top=Side(style='thin', color='BFBFBF'),
        bottom=Side(style='thin', color='BFBFBF')
    )

    # Title rows
    ws.merge_cells("A1:H1")
    ws["A1"] = "BẢNG MA TRẬN PHÂN BỔ 46 KỸ NĂNG GIÁO DỤC AI CẤP TIỂU HỌC (LỚP 1 – 5)"
    ws["A1"].font = font_title
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")

    ws.merge_cells("A2:H2")
    ws["A2"] = "Căn cứ: QĐ 2422/QĐ-BGDĐT & CV 5588/BGDĐT-GDPT | Cấu trúc: 36 tiết/lớp (12 Cốt lõi + 24 Mở rộng)"
    ws["A2"].font = font_sub
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")

    # Header row
    headers = [
        "STT", "Tên kỹ năng chuẩn hóa", "Định nghĩa năng lực", "Mạch NL",
        "Lớp 1 (30–35p)", "Lớp 2 (30–35p)", "Lớp 3 (35p)", "Lớp 4 (35p)", "Lớp 5 (35p)"
    ]
    # Header starts at row 4
    for col_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws.row_dimensions[4].height = 28

    current_row = 5
    current_group = ""

    for s in SKILLS_DATA:
        if s["nhom"] != current_group:
            current_group = s["nhom"]
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=9)
            g_cell = ws.cell(row=current_row, column=1, value=f"{current_group} ({s['nhom_con']})")
            g_cell.font = font_group
            g_cell.fill = fill_group
            g_cell.alignment = Alignment(horizontal="left", vertical="center")
            ws.row_dimensions[current_row].height = 24
            current_row += 1

        ws.cell(row=current_row, column=1, value=s["stt"]).alignment = Alignment(horizontal="center", vertical="top")
        ws.cell(row=current_row, column=2, value=s["ten"]).alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws.cell(row=current_row, column=3, value=s["dinh_nghia"]).alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws.cell(row=current_row, column=4, value=s["mach_nl"]).alignment = Alignment(horizontal="center", vertical="top")

        for c_idx in range(1, 5):
            ws.cell(row=current_row, column=c_idx).font = font_cell
            ws.cell(row=current_row, column=c_idx).border = thin_border

        for g_idx, g_key in enumerate(["lop1", "lop2", "lop3", "lop4", "lop5"], 5):
            cell_data = s[g_key]
            c = ws.cell(row=current_row, column=g_idx)
            c.border = thin_border
            if cell_data is None:
                c.value = "-"
                c.alignment = Alignment(horizontal="center", vertical="center")
                c.font = font_cell
            else:
                text_val = f"[{cell_data['loai']}] {cell_data['muc_do']}\n• {cell_data['noi_dung']}"
                c.value = text_val
                c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
                c.font = font_cell
                if cell_data['loai'] == "VN-CORE":
                    c.fill = fill_core
                else:
                    c.fill = fill_mr

        ws.row_dimensions[current_row].height = 65
        current_row += 1

    # Adjust column widths
    col_widths = {1: 6, 2: 24, 3: 32, 4: 10, 5: 32, 6: 32, 7: 32, 8: 32, 9: 32}
    for col_idx, width in col_widths.items():
        ws.column_dimensions[openpyxl.utils.get_column_letter(col_idx)].width = width

    wb.save(filepath)
    print(f"Generated Excel: {filepath}")

def generate_docx(filepath):
    doc = docx.Document()
    
    # Set landscape orientation for wide table
    for section in doc.sections:
        section.orientation = docx.enum.section.WD_ORIENT.LANDSCAPE
        section.page_width = Inches(11.69)
        section.page_height = Inches(8.27)
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.5)
        section.right_margin = Inches(0.5)

    title_p = doc.add_paragraph()
    title_run = title_p.add_run("BẢNG MA TRẬN PHÂN BỔ 46 KỸ NĂNG GIÁO DỤC AI CẤP TIỂU HỌC (LỚP 1 – 5)")
    title_run.font.name = "Times New Roman"
    title_run.font.size = Pt(15)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(31, 73, 125)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    sub_p = doc.add_paragraph()
    sub_run = sub_p.add_run("Căn cứ: Quyết định 2422/QĐ-BGDĐT & Công văn 5588/BGDĐT-GDPT | Cấu trúc: 36 tiết/lớp (12 Cốt lõi + 24 Mở rộng)")
    sub_run.font.name = "Times New Roman"
    sub_run.font.size = Pt(10)
    sub_run.font.italic = True
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    table = doc.add_table(rows=1, cols=8)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    headers = ["STT", "Tên kỹ năng & Định nghĩa", "Mạch NL", "Lớp 1", "Lớp 2", "Lớp 3", "Lớp 4", "Lớp 5"]
    widths = [Inches(0.4), Inches(2.2), Inches(0.6), Inches(1.5), Inches(1.5), Inches(1.5), Inches(1.5), Inches(1.5)]

    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].paragraphs[0].runs[0].font.name = "Times New Roman"
        hdr_cells[i].paragraphs[0].runs[0].font.size = Pt(9.5)
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        hdr_cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        hdr_cells[i].width = widths[i]

    current_group = ""
    for s in SKILLS_DATA:
        if s["nhom"] != current_group:
            current_group = s["nhom"]
            grp_row = table.add_row()
            grp_cells = grp_row.cells
            # Merge all cells in this row
            a = grp_cells[0]
            b = grp_cells[7]
            a.merge(b)
            a.text = f"{current_group} ({s['nhom_con']})"
            a.paragraphs[0].runs[0].font.name = "Times New Roman"
            a.paragraphs[0].runs[0].font.size = Pt(9.5)
            a.paragraphs[0].runs[0].font.bold = True
            a.paragraphs[0].runs[0].font.color.rgb = RGBColor(0, 32, 96)

        row_cells = table.add_row().cells
        row_cells[0].text = str(s["stt"])
        row_cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        name_p = row_cells[1].paragraphs[0]
        run_name = name_p.add_run(s["ten"] + "\n")
        run_name.font.bold = True
        run_def = name_p.add_run(s["dinh_nghia"])
        run_def.font.italic = True
        run_def.font.size = Pt(8.5)

        row_cells[2].text = s["mach_nl"]
        row_cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

        for g_idx, g_key in enumerate(["lop1", "lop2", "lop3", "lop4", "lop5"], 3):
            cell_data = s[g_key]
            c = row_cells[g_idx]
            if cell_data is None:
                c.text = "-"
                c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p = c.paragraphs[0]
                run_badge = p.add_run(f"[{cell_data['loai']}] {cell_data['muc_do']}\n")
                run_badge.font.bold = True
                run_badge.font.size = Pt(8.5)
                if cell_data['loai'] == "VN-CORE":
                    run_badge.font.color.rgb = RGBColor(192, 0, 0)
                else:
                    run_badge.font.color.rgb = RGBColor(0, 112, 192)
                
                run_desc = p.add_run(f"• {cell_data['noi_dung']}")
                run_desc.font.size = Pt(8.5)

        for i in range(8):
            row_cells[i].width = widths[i]
            for p in row_cells[i].paragraphs:
                for r in p.runs:
                    r.font.name = "Times New Roman"

    doc.save(filepath)
    print(f"Generated Word: {filepath}")

if __name__ == "__main__":
    md_path = "03_San_Pham_Chinh_Thuc/Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5.md"
    xlsx_path = "03_San_Pham_Chinh_Thuc/Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5.xlsx"
    docx_path = "03_San_Pham_Chinh_Thuc/Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5.docx"

    generate_markdown(md_path)
    generate_excel(xlsx_path)
    generate_docx(docx_path)
    print("All 3 matrix files successfully updated with 46 skills!")
