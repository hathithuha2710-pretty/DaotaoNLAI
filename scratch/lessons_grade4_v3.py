# -*- coding: utf-8 -*-
"""
Dữ liệu PPCT Lớp 4 - Phiên bản v3.0 Chuẩn hóa sâu theo Ma trận 46 Kỹ năng & QĐ 2422
Đã xử lý triệt để:
- Sửa lệch mức độ: KN3, 17, 35, 36, 37, 38, 39, 45 về đúng Mức 2 (Thực hành có hướng dẫn)
- Nâng KN9 (Từ chối chia sẻ) và KN12 (Xử lý sự cố) lên đúng Mức 3 (Thực hành độc lập)
- KN5 ở Mức 1 (Quan sát/So sánh Few-shot), KN10 ở Mức 1 (Dấu chân số)
- Tách bạch cấu trúc Prompt 3 thành phần (KN4) và Tinh chỉnh đa vòng (KN6)
- Đồng sáng tạo sản phẩm tranh số cùng AI (KN39: Mức 2)
- Đảm bảo 100% YCCĐ Cốt lõi (10) và Mở rộng (7) theo QĐ 2422.
"""

GRADE4_12_CORE = [
    {
        "tiet": 1,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 1: AI vì cuộc sống con người: Các ngành nghề ứng dụng",
        "noidung": "Học sinh tìm hiểu và trình bày một số lĩnh vực AI hỗ trợ con người (y tế chẩn đoán hình ảnh, giao thông điều tiết đèn tín hiệu, nông nghiệp giám sát độ ẩm đất); thực hành tra cứu có hướng dẫn thông tin về một nghề nghiệp có AI hỗ trợ. Tích hợp [KN 3: Mức 2 - Thực hành có hướng dẫn], [KN 38: Mức 2 - Đề xuất giải pháp theo ngữ cảnh].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Video tư liệu ngắn về AI trong y tế và nông nghiệp, phiếu học tập nghề nghiệp",
        "ma_yccd": "4.A1.1"
    },
    {
        "tiet": 2,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 2: Con người giữ vai trò quyết định và chịu trách nhiệm",
        "noidung": "Học sinh thảo luận tình huống thực tế: Bác sĩ sử dụng phần mềm AI gợi ý chẩn đoán nhưng chính bác sĩ là người đưa ra phác đồ điều trị cuối cùng; nhận biết AI là công cụ hỗ trợ, con người luôn giữ vai trò quyết định và chịu trách nhiệm giải trình. Tích hợp [KN 42: Mức 3 - Thực hành độc lập], [KN 46: Mức 3 - Xác lập trách nhiệm giải trình].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Nghiên cứu tình huống (Case study) y khoa học đường, bảng ma trận trách nhiệm",
        "ma_yccd": "4.A1.2"
    },
    {
        "tiet": 3,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 3: AI hỗ trợ cộng đồng và giới hạn của máy móc",
        "noidung": "Học sinh trình bày các đối tượng trong xã hội được AI hỗ trợ (bác sĩ, giáo viên, nông dân, người khuyết tật); thực hành thiết kế ý tưởng có hướng dẫn về một công cụ AI hỗ trợ bạn học khiếm thị; khẳng định AI không thể thay thế tình cảm và sự sáng tạo của con người. Tích hợp [KN 17: Mức 2 - Thực hành có hướng dẫn AI bao trùm], [KN 18: Mức 3].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Hình ảnh thiết bị kính thông minh nhận diện vật cản cho người khiếm thị",
        "ma_yccd": "4.A2.1, 4.A2.2"
    },
    {
        "tiet": 4,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 4: Ra quyết định sử dụng AI: Đúng lúc, đúng nơi, đúng quy định",
        "noidung": "Học sinh tự chủ phân tích các tình huống học đường và ra quyết định độc lập: (1) Trong giờ thi kiểm tra $\rightarrow$ Nghiêm cấm dùng AI; (2) Khi tìm ý tưởng làm bích báo $\rightarrow$ Được dùng AI gợi ý nhưng phải ghi nguồn; (3) Khi bài tập yêu cầu rèn chữ viết $\rightarrow$ Tự viết tay; giải thích lý do lựa chọn. Tích hợp [KN 43: Mức 3 - Ra quyết định độc lập].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bảng phân tích quyết định: Tình huống vs Mục đích vs Quy định cho phép",
        "ma_yccd": "4.A3.1"
    },
    {
        "tiet": 5,
        "chude": "Đạo đức AI",
        "ten_bai": "Bài 5: Bảo vệ thông tin cá nhân trong kỷ nguyên số",
        "noidung": "Học sinh nêu các loại thông tin cá nhân cần giữ bí mật tuyệt đối (mật khẩu, định vị nhà ở, số CCCD bố mẹ, ảnh góc riêng tư); thực hành thao tác từ chối độc lập: Tắt cửa sổ yêu cầu cấp quyền vị trí không cần thiết trên trình duyệt. Tích hợp [KN 8: Mức 2 - Phân loại dữ liệu nhạy cảm], [KN 9: Mức 3 - Thực hành từ chối độc lập].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Infographic bảo vệ danh tính số, giao diện giả lập thông báo cấp quyền trình duyệt",
        "ma_yccd": "4.B2.1"
    },
    {
        "tiet": 6,
        "chude": "Đạo đức AI",
        "ten_bai": "Bài 6: Hậu quả lộ thông tin cá nhân và kỹ năng phòng ngừa",
        "noidung": "Học sinh phân tích hậu quả khi thông tin cá nhân bị lộ (bị mạo danh lừa đảo, bị theo dõi vị trí, tin nhắn rác quấy rầy); thực hành phản xạ độc lập xử lý tình huống: Nghi ngờ tài khoản bị lộ $\rightarrow$ Đổi mật khẩu ngay và báo người phụ trách. Tích hợp [KN 8: Mức 2], [KN 12: Mức 3 - Xử lý sự cố độc lập].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Video tình huống an toàn mạng, phiếu quy trình 3 bước xử lý sự cố số",
        "ma_yccd": "4.B2.2"
    },
    {
        "tiet": 7,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 7: Khám phá ứng dụng AI hỗ trợ học tập và sáng tạo số",
        "noidung": "Học sinh tìm hiểu các ứng dụng AI hỗ trợ sáng tạo (AutoDraw gợi ý nét vẽ, Quick Draw nhận diện hình vẽ nhanh, Verse by Verse gợi ý vần thơ); nhận diện thanh công cụ gợi ý thông minh, nút Tạo lại (Regenerate) và điều hướng giao diện độc lập. Tích hợp [KN 1: Mức 3 - Thao tác độc lập], [KN 3: Mức 2].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Máy chiếu, trình duyệt truy cập công cụ AutoDraw, Quick, Draw!",
        "ma_yccd": "4.C2.1"
    },
    {
        "tiet": 8,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 8: Thực hành: Đồng sáng tạo tranh cổ động cùng AI",
        "noidung": "Thực hành trên phòng máy: Học sinh phác thảo nét vẽ cơ bản trên AutoDraw, chọn gợi ý nét vẽ thông minh của AI, kết hợp tô màu và tự tay viết khẩu hiệu bảo vệ môi trường của nhóm; thực hành ghi rõ nguồn 'Tranh có sự hỗ trợ của AutoDraw'. Tích hợp [KN 14: Mức 3 - Ghi nguồn tác quyền], [KN 39: Mức 2 - Đồng sáng tạo có hướng dẫn].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Phòng thực hành tin học, nền tảng AutoDraw, mẫu ghi nhận tác quyền",
        "ma_yccd": "4.C2.1 (Thực hành hóa)"
    },
    {
        "tiet": 9,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 9: Ý tưởng giải pháp AI cho các vấn đề học đường",
        "noidung": "Học sinh khảo sát một vấn đề khó khăn tại trường (thùng rác sân trường bị lẫn rác tái chế, học sinh ngồi sai tư thế); nêu ý tưởng ban đầu về cách AI có thể học trên hình ảnh để giải quyết vấn đề đó có hướng dẫn của giáo viên. Tích hợp [KN 36: Mức 2 - Thực hành có hướng dẫn], [KN 38: Mức 2].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Phiếu khảo sát thực địa trường lớp, bảng mẫu xác định bài toán",
        "ma_yccd": "4.D1.1"
    },
    {
        "tiet": 10,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 10: Thực hành: Mô hình hóa sơ đồ giải pháp AI",
        "noidung": "Thực hành theo nhóm dưới sự hướng dẫn của giáo viên: Vẽ sơ đồ khối dòng chảy giải pháp: Thu nhận ảnh rác qua Webcam $\rightarrow$ Mô hình phân loại vỏ chai / hộp sữa $\rightarrow$ Phát tín hiệu mở ngăn rác tương ứng; phân công nhiệm vụ nhóm. Tích hợp [KN 37: Mức 2 - Mô hình hóa có hướng dẫn], [KN 41: Mức 2].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bản vẽ sơ đồ kiến trúc giải pháp A3, bút dạ màu nhóm",
        "ma_yccd": "4.D1.1 (Thực hành hóa)"
    },
    {
        "tiet": 11,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 11: Đánh giá và liên tục nâng cấp hệ thống AI",
        "noidung": "Học sinh trình bày rằng hệ thống AI không thể hoàn hảo ngay từ đầu, con người cần liên tục đánh giá độ chính xác và nâng cấp bằng cách bổ sung dữ liệu mới và chỉnh sửa nhãn sai; phân tích vòng tròn nâng cấp hệ thống AI. Tích hợp [KN 35: Mức 2 - Thực hành có hướng dẫn], [KN 45: Mức 2 - Giám sát hệ thống].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Sơ đồ vòng đời hệ thống AI (AI System Lifecycle), biểu đồ theo dõi lỗi",
        "ma_yccd": "4.D2.1"
    },
    {
        "tiet": 12,
        "chude": "Tích hợp 4 mạch",
        "ten_bai": "Bài 12: Tổng kết chuyên đề: Nhà kiến tạo AI tương lai",
        "noidung": "Học sinh báo cáo sơ đồ giải pháp AI học đường; khẳng định trách nhiệm của con người trong việc bảo vệ dữ liệu cá nhân, liêm chính khi dùng công cụ sáng tạo và liên tục cải tiến hệ thống; giáo viên đánh giá quá trình theo Mục VI QĐ 2422. Tích hợp [KN 42: Mức 3], [KN 46: Mức 3].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Hồ sơ dự án sơ đồ giải pháp nhóm, phiếu đánh giá Mục VI",
        "ma_yccd": "Mục VI QĐ 2422"
    }
]

GRADE4_36_EXPANDED = [
    {"tiet": 1, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 1: AI vì cuộc sống con người: Các ngành nghề ứng dụng", "noidung": "Trình bày lĩnh vực AI hỗ trợ (y tế, giao thông, nông nghiệp); thực hành tra cứu nghề nghiệp số. [4.A1.1] - Tích hợp [KN 3: Mức 2], [KN 38: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Video tư liệu ngắn về AI trong y tế và nông nghiệp", "ma_yccd": "4.A1.1"},
    {"tiet": 2, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 2: Con người giữ vai trò quyết định và chịu trách nhiệm", "noidung": "Thảo luận vai trò quyết định của con người trong ứng dụng y khoa; khẳng định trách nhiệm giải trình của người dùng. [4.A1.2] - Tích hợp [KN 42: Mức 3], [KN 46: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Nghiên cứu tình huống y tế học đường", "ma_yccd": "4.A1.2"},
    {"tiet": 3, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 3: AI hỗ trợ giải quyết bài toán thực tế địa phương", "noidung": "Nêu được ví dụ cụ thể về việc AI hỗ trợ học tập và giải quyết vấn đề thực tế địa phương (quản lý rác thải, tưới tiêu vườn trường). [4.A1.MR1] - Tích hợp [KN 36: Mức 2], [KN 38: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Tài liệu mô hình tưới nhỏ giọt tự động công nghệ cao", "ma_yccd": "4.A1.MR1"},
    {"tiet": 4, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 4: AI hỗ trợ cộng đồng và giới hạn của máy móc", "noidung": "Trình bày các đối tượng được AI hỗ trợ; khẳng định máy móc không thể thay thế tình cảm và sáng tạo của con người. [4.A2.1, 4.A2.2] - Tích hợp [KN 17: Mức 2], [KN 18: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Hình ảnh thiết bị thông minh hỗ trợ người khuyết tật", "ma_yccd": "4.A2.1, 4.A2.2"},
    {"tiet": 5, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 5: AI vì sự hòa nhập: Thiết kế ý tưởng hỗ trợ bạn học", "noidung": "Thực hành thiết kế ý tưởng công cụ AI hỗ trợ bạn học khiếm thị hoặc khó đọc chữ trong trường; mô tả cách công cụ giúp đỡ bạn. [Đào sâu 4.A2.2] - Tích hợp [KN 17: Mức 2 - Thực hành có hướng dẫn].", "phanloai": "Mở rộng", "hoclieu": "Bản mẫu thiết kế ý tưởng hỗ trợ người yếu thế A3", "ma_yccd": ""},
    {"tiet": 6, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 6: Ra quyết định sử dụng AI: Đúng lúc, đúng nơi, đúng quy định", "noidung": "Phân tích tình huống học đường và ra quyết định độc lập: tình huống nào được dùng AI, tình huống nào cấm dùng AI. [4.A3.1] - Tích hợp [KN 43: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Bảng ma trận quyết định học đường", "ma_yccd": "4.A3.1"},
    {"tiet": 7, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 7: Thực hành xử lý tình huống: Tự chủ ra quyết định sử dụng AI", "noidung": "Thực hành đưa quyết định có sử dụng AI hay không trong một số tình huống giả định cụ thể; giải thích rõ căn cứ lựa chọn. [4.A3.MR1] - Tích hợp [KN 43: Mức 3 - Thực hành độc lập].", "phanloai": "Mở rộng", "hoclieu": "Bộ 6 thẻ tình huống giả định kiểm tra bài tập", "ma_yccd": "4.A3.MR1"},
    {"tiet": 8, "chude": "Đạo đức AI", "ten_bai": "Bài 8: Bảo vệ thông tin cá nhân trong kỷ nguyên số", "noidung": "Nêu các loại thông tin cá nhân cần giữ bí mật; thực hành thao tác từ chối cấp quyền camera/vị trí độc lập. [4.B2.1] - Tích hợp [KN 8: Mức 2], [KN 9: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Infographic bảo vệ danh tính số của học sinh", "ma_yccd": "4.B2.1"},
    {"tiet": 9, "chude": "Đạo đức AI", "ten_bai": "Bài 9: Hậu quả lộ thông tin cá nhân và kỹ năng phòng ngừa", "noidung": "Phân tích hậu quả khi lộ dữ liệu; thực hành phản xạ độc lập báo ngay người phụ trách và đổi mật khẩu khi có cảnh báo. [4.B2.2] - Tích hợp [KN 8: Mức 2], [KN 12: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Video cảnh báo lừa đảo mạng học đường", "ma_yccd": "4.B2.2"},
    {"tiet": 10, "chude": "Đạo đức AI", "ten_bai": "Bài 10: Xử lý tình huống khẩn cấp khi nghi ngờ thông tin bị lộ", "noidung": "Thực hành xử lí theo hướng dẫn một tình huống giả định đơn giản khi thông tin cá nhân có nguy cơ bị lộ hoặc bị AI lợi dụng. [4.B2.MR1] - Tích hợp [KN 12: Mức 3 - Xử lý sự cố độc lập].", "phanloai": "Mở rộng", "hoclieu": "Kịch bản đóng vai: 'Tài khoản học tập bị đăng nhập lạ'", "ma_yccd": "4.B2.MR1"},
    {"tiet": 11, "chude": "Đạo đức AI", "ten_bai": "Bài 11: Nhận thức về Dấu chân kỹ thuật số (Digital Footprint)", "noidung": "Thảo luận về khái niệm 'Dấu chân số': Mọi bài đăng, bình luận, ảnh chụp tải lên mạng đều lưu lại vĩnh viễn; thực hành suy nghĩ kỹ trước khi đăng tải. [Làm giàu INT-ENRICH: Google BIA] - Tích hợp [KN 10: Mức 1 - Nhận biết/Thảo luận].", "phanloai": "Mở rộng", "hoclieu": "Tranh biểu tượng 'Dấu chân số' trên bãi cát Internet", "ma_yccd": ""},
    {"tiet": 12, "chude": "Đạo đức AI", "ten_bai": "Bài 12: Liêm chính học thuật và Minh bạch tác quyền khi dùng AI", "noidung": "Học sinh thực hành dán nhãn ghi chú minh bạch tác quyền: Phần nào do em tự vẽ/tự viết, phần nào do AI gợi ý; cam kết trung thực học thuật độc lập. [Làm giàu INT-ENRICH] - Tích hợp [KN 14: Mức 3], [KN 15: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Phiếu ghi nhận tác quyền sản phẩm số (Attribution card)", "ma_yccd": ""},
    {"tiet": 13, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 13: Khám phá ứng dụng AI hỗ trợ học tập và sáng tạo nghệ thuật", "noidung": "Nêu ứng dụng AI hỗ trợ sáng tạo (AutoDraw, Quick Draw); tự chủ điều hướng các công cụ trên giao diện ứng dụng. [4.C2.1] - Tích hợp [KN 1: Mức 3], [KN 3: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Trình chiếu giao diện AutoDraw, Quick Draw", "ma_yccd": "4.C2.1"},
    {"tiet": 14, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 14: Thực hành: Khơi nguồn cảm hứng sáng tạo cùng công cụ AI", "noidung": "Thực hành phối hợp nét vẽ phác thảo tay và gợi ý thông minh của AutoDraw để hoàn thành bức tranh cổ động môi trường. [4.C2.1 (Thực hành hóa)] - Tích hợp [KN 39: Mức 2 - Đồng sáng tạo có hướng dẫn].", "phanloai": "Cốt lõi", "hoclieu": "Phòng máy tính kết nối Internet", "ma_yccd": ""},
    {"tiet": 15, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 15: Trải nghiệm ứng dụng AI trong học tập và đời sống", "noidung": "Thực hành trải nghiệm một số ứng dụng AI trong học tập và đời sống: dùng AI gợi ý 3 tính từ miêu tả cánh đồng lúa và chọn lọc kết quả phù hợp. [4.C2.MR1] - Tích hợp [KN 3: Mức 2 - Thực hành có hướng dẫn].", "phanloai": "Mở rộng", "hoclieu": "Công cụ Verse by Verse / chatbot ngôn ngữ học tập", "ma_yccd": "4.C2.MR1"},
    {"tiet": 16, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 16: Kỹ thuật câu lệnh 3 thành phần và Tinh chỉnh đa vòng", "noidung": "Học sinh viết câu lệnh 3 thành phần: [Vai trò] + [Nhiệm vụ] + [Định dạng] (KN4: Mức 2); đọc kết quả của AI và nhập tiếp câu lệnh bổ sung vòng 2: 'Hãy viết ngắn gọn hơn trong 3 dòng' (KN6: Mức 2); quan sát so sánh với prompt có ví dụ mẫu (KN5: Mức 1). Tích hợp [KN 4: Mức 2], [KN 5: Mức 1], [KN 6: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Phiếu bài tập ghép khối lệnh 3 thành phần và ghi chép 2 vòng prompt", "ma_yccd": ""},
    {"tiet": 17, "chude": "Tích hợp", "ten_bai": "Bài 17: Đánh giá quá trình: Báo cáo hồ sơ học tập và sản phẩm Học kỳ I", "noidung": "Học sinh trình bày tranh cổ động môi trường đồng sáng tạo cùng AI, nhật ký prompt 2 vòng và phiếu xử lý sự cố an toàn; giáo viên đánh giá theo Mục VI QĐ 2422.", "phanloai": "Đánh giá quá trình", "hoclieu": "Hồ sơ học tập số lưu trên máy phòng tin", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 18, "chude": "Tích hợp", "ten_bai": "Bài 18: Triển lãm tranh số: Nghệ thuật và Công nghệ giao thoa", "noidung": "Trưng bày bộ tranh cổ động do học sinh đồng sáng tạo cùng AI; đánh giá phần học sinh tự vẽ, phần AI hỗ trợ và tính minh bạch tác quyền. [Mục VI QĐ 2422].", "phanloai": "Đánh giá quá trình", "hoclieu": "Khu triển lãm tranh số phòng máy, hoa điểm tốt", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 19, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 19: Trải nghiệm 4 bước học máy cơ bản trên công cụ trực quan", "noidung": "Thực hiện lại theo từng bước các thao tác cơ bản: (1) Thu thập & chuẩn bị dữ liệu -> (2) Huấn luyện mô hình -> (3) Kiểm thử -> (4) Ứng dụng trên Teachable Machine. [4.C5.MR1] - Tích hợp [KN 34: Mức 2 - Thực hành có hướng dẫn].", "phanloai": "Mở rộng", "hoclieu": "Nền tảng Google Teachable Machine phòng máy", "ma_yccd": "4.C5.MR1"},
    {"tiet": 20, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 20: Tự chọn dữ liệu và huấn luyện mô hình phân loại hình ảnh", "noidung": "Lặp lại đầy đủ 4 bước trên với nhóm dữ liệu tự chọn (phân loại bút chì vs thước kẻ); tự tạo 2 lớp dữ liệu (Class) và chụp ảnh qua webcam. [4.C5.MR2] - Tích hợp [KN 29: Mức 2], [KN 30: Mức 2], [KN 34: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Đồ dùng học tập làm mẫu chụp ảnh qua Webcam", "ma_yccd": "4.C5.MR2"},
    {"tiet": 21, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 21: Kiểm thử mô hình với mẫu mới và Ghi nhận kết quả đúng/sai", "noidung": "Đưa các mẫu vật mới chưa từng học trước webcam; ghi chép vào bảng kiểm thử: Số lần đoán đúng, số lần đoán sai và mức điểm số tin cậy; phát hiện nguyên nhân máy nhầm. [Đào sâu 4.C5.MR2] - Tích hợp [KN 22: Mức 2], [KN 25: Mức 2 - Đọc điểm số tin cậy].", "phanloai": "Mở rộng", "hoclieu": "Bảng ghi kết quả kiểm thử mẫu mới (Confusion table)", "ma_yccd": ""},
    {"tiet": 22, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 22: Tinh chỉnh dữ liệu và Tái huấn luyện mô hình", "noidung": "Học sinh thực hành xóa ảnh bị mờ rung (KN31: Mức 2); chụp bổ sung 10 ảnh ở góc nghiêng; bấm Train lại và so sánh bảng kết quả kiểm thử trước/sau cải tiến. [Đào sâu 4.C5.MR2] - Tích hợp [KN 31: Mức 2], [KN 35: Mức 2 - Tái huấn luyện có hướng dẫn].", "phanloai": "Mở rộng", "hoclieu": "Biểu đồ so sánh độ chính xác trước và sau khi bổ sung dữ liệu", "ma_yccd": ""},
    {"tiet": 23, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 23: Ý tưởng giải pháp AI cho các vấn đề học đường", "noidung": "Nêu một số ý tưởng ban đầu về cách AI có thể học hoặc giải quyết vấn đề đơn giản trong học tập hoặc đời sống. [4.D1.1] - Tích hợp [KN 36: Mức 2 - Thực hành có hướng dẫn].", "phanloai": "Cốt lõi", "hoclieu": "Phiếu khảo sát vấn đề rác thải sân trường", "ma_yccd": "4.D1.1"},
    {"tiet": 24, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 24: Thực hành: Mô hình hóa ý tưởng giải pháp AI", "noidung": "Thiết kế sơ đồ kiến trúc dòng dữ liệu giải pháp: Từ Camera chụp rác $\rightarrow$ Mô hình nhận diện vỏ chai nhựa $\rightarrow$ Phát âm thanh hướng dẫn. [4.D1.1 (Thực hành hóa)] - Tích hợp [KN 37: Mức 2 - Mô hình hóa có hướng dẫn].", "phanloai": "Cốt lõi", "hoclieu": "Sơ đồ kiến trúc giải pháp A3 của nhóm", "ma_yccd": ""},
    {"tiet": 25, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 25: Thiết kế giải pháp AI giải quyết tình huống giả định", "noidung": "Trình bày cách sử dụng AI để giải quyết vấn đề trong tình huống giả định (hỗ trợ phân loại rác tái chế học đường: chai nhựa vs hộp sữa giấy). [4.D1.MR1] - Tích hợp [KN 38: Mức 2 - Đề xuất giải pháp].", "phanloai": "Mở rộng", "hoclieu": "Bản thuyết minh giải pháp 'Thùng rác thông minh'", "ma_yccd": "4.D1.MR1"},
    {"tiet": 26, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 26: Đánh giá và liên tục nâng cấp hệ thống AI", "noidung": "Trình bày con người cần liên tục đánh giá và nâng cấp hệ thống AI bằng cách cải tiến dữ liệu và điều chỉnh thuật toán. [4.D2.1] - Tích hợp [KN 45: Mức 2 - Giám sát hệ thống].", "phanloai": "Cốt lõi", "hoclieu": "Sơ đồ chu trình cải tiến hệ thống AI", "ma_yccd": "4.D2.1"},
    {"tiet": 27, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 27: Thu thập dữ liệu thực tế và Kiểm toán tính đa dạng", "noidung": "Khảo sát thực địa sân trường; thu thập ảnh vỏ chai nhựa và hộp sữa bẹp; kiểm tra tính đa dạng (đủ các nhãn hiệu, màu sắc, tình trạng bẹp/nguyên). [Đào sâu 4.D2.1] - Tích hợp [KN 29: Mức 2], [KN 32: Mức 2 - Dữ liệu đa dạng].", "phanloai": "Mở rộng", "hoclieu": "Mẫu vật rác tái chế đã khử trùng sạch sẽ", "ma_yccd": ""},
    {"tiet": 28, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 28: Dự án Stem/AI: Thùng rác phân loại thông minh (Tiết 1 - Dữ liệu)", "noidung": "Các nhóm chuẩn bị tập dữ liệu: Chụp 25 ảnh vỏ chai nhựa và 25 ảnh hộp sữa giấy; thực hành lọc xóa ảnh chụp mờ hoặc lệch khỏi khung camera (Data Cleaning). [KN 29, KN 30, KN 31: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Webcam phòng máy, thùng rác mô hình bằng bìa các-tông", "ma_yccd": ""},
    {"tiet": 29, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 29: Dự án Stem/AI: Thùng rác phân loại thông minh (Tiết 2 - Huấn luyện)", "noidung": "Huấn luyện mô hình phân loại trên Teachable Machine phòng máy; kiểm thử với các mẫu rác thật đưa trước camera; ghi bảng kết quả đúng/sai. [KN 25: Mức 2], [KN 34: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Giao diện Teachable Machine, bảng kết quả kiểm thử", "ma_yccd": ""},
    {"tiet": 30, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 30: Dự án Stem/AI: Thử nghiệm thực tế và Tái huấn luyện", "noidung": "Thử nghiệm hộp sữa giấy bẹp bị nhận nhầm thành chai nhựa; chụp bổ sung 10 ảnh hộp sữa bẹp và tái huấn luyện mô hình để nâng cao độ chính xác kiểm thử. [KN 22: Mức 2], [KN 35: Mức 2 - Tái huấn luyện].", "phanloai": "Mở rộng", "hoclieu": "Mẫu vật kiểm thử góc khó, giao diện Retrain", "ma_yccd": ""},
    {"tiet": 31, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 31: Dự án Stem/AI: Lập trình âm thanh hướng dẫn trên Scratch", "noidung": "Lập trình phản hồi logic trong Scratch: 'Nếu nhận diện Chai nhựa $\rightarrow$ Phát âm thanh: Xin mời bỏ vào ngăn màu xanh bên trái' (lập trình phản hồi đúng điều kiện nhận diện). [KN 40: Mức 2 - Thực hành có hướng dẫn].", "phanloai": "Mở rộng", "hoclieu": "Môi trường lập trình khối Scratch AI", "ma_yccd": ""},
    {"tiet": 32, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 32: Báo cáo trách nhiệm: Bảo vệ môi trường và Vận hành AI", "noidung": "Thảo luận về trách nhiệm của nhóm sáng chế: Nêu rõ 1 lỗi hệ thống chưa nhận diện được, ai ra quyết định sửa và ý thức bảo vệ môi trường trường học. [KN 45: Mức 2], [KN 46: Mức 3 - Trách nhiệm giải trình].", "phanloai": "Mở rộng", "hoclieu": "Bản báo cáo kỹ thuật dự án nhóm", "ma_yccd": ""},
    {"tiet": 33, "chude": "Tích hợp", "ten_bai": "Bài 33: Đánh giá quá trình: Đánh giá dự án AI vì môi trường Học kỳ II", "noidung": "Demo trực tiếp mô hình thùng rác phân loại thông minh trước lớp; giáo viên đánh giá từng cá nhân theo rubric: thao tác dữ liệu, kiểm thử, phân tích lỗi và trách nhiệm giải trình. [Mục VI QĐ 2422].", "phanloai": "Đánh giá quá trình", "hoclieu": "Rubric đánh giá dự án STEM-AI Lớp 4", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 34, "chude": "Tích hợp", "ten_bai": "Bài 34: Ngày hội Triển lãm & Sáng tạo Công nghệ xanh Lớp 4", "noidung": "Trưng bày các mô hình thùng rác phân loại thông minh và poster tranh số bảo vệ môi trường; học sinh giao lưu, chia sẻ bài học về cải tiến dữ liệu cùng phụ huynh và thầy cô.", "phanloai": "Đánh giá quá trình", "hoclieu": "Gian hàng triển lãm ngày hội trường học, phiếu khen thưởng", "ma_yccd": ""},
    {"tiet": 35, "chude": "Tích hợp", "ten_bai": "Bài 35: Củng cố hành trang số: Bước chân nhà kiến tạo công nghệ trẻ", "noidung": "Diễn đàn trao đổi: Tổng kết 4 bước học máy, ý thức tự chủ thời gian (KN44: Mức 3), liêm chính học thuật và bảo vệ dữ liệu cá nhân; trao giải dự án xuất sắc Lớp 4.", "phanloai": "Đánh giá quá trình", "hoclieu": "Giấy chứng nhận 'Nhà kiến tạo AI xanh Lớp 4'", "ma_yccd": ""},
    {"tiet": 36, "chude": "Tích hợp", "ten_bai": "Bài 36: Báo cáo chuyên đề cốt lõi: Nhà sáng tạo nhí đồng hành cùng AI", "noidung": "Tổng kết đánh giá chuyên đề bắt buộc theo Mục VI QĐ 2422; hoàn tất hồ sơ minh chứng học tập AI Lớp 4.", "phanloai": "Cốt lõi", "hoclieu": "Sổ theo dõi đánh giá học sinh Lớp 4", "ma_yccd": "Mục VI QĐ 2422"}
]
