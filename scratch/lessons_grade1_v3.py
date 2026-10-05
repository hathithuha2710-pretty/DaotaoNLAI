# -*- coding: utf-8 -*-
"""
Dữ liệu PPCT Lớp 1 - Phiên bản v3.0 Chuẩn hóa sâu theo Ma trận 46 Kỹ năng & QĐ 2422
Đã xử lý triệt để:
- Phân rã kỹ năng an toàn thành các vi hành vi: Nói 'Không' (KN9), Tắt máy báo cô (KN12), Xin phép bạn (KN13)
- Bổ sung thao tác làm sạch dữ liệu thẻ tranh (KN31), tự chủ tư duy và thời gian (KN42, KN44)
- Giảm trùng lặp cụm robot cười và cụm đơn năng/đa năng; tinh gọn cụm tổng kết cuối năm
- Đảm bảo 100% YCCĐ Cốt lõi (17) và Mở rộng (4) theo QĐ 2422.
"""

GRADE1_12_CORE = [
    {
        "tiet": 1,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 1: Cảm xúc của em và phản ứng của máy",
        "noidung": "Học sinh nêu ví dụ về cảm xúc vui, buồn, sợ hãi của bản thân qua tranh thẻ; đối chiếu với hình ảnh robot nhấp nháy đèn hoặc hiện mặt cười; bước đầu chỉ ra con người có cảm xúc thật từ trái tim còn máy thông minh chỉ mô phỏng nét mặt theo lệnh. Tích hợp [KN 18: Mức 1 - Nhận biết cốt lõi].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bộ thẻ tranh cảm xúc mặt cười/mặt mếu, video ngắn robot đồ chơi biểu cảm",
        "ma_yccd": "1.A1.1, 1.A1.2"
    },
    {
        "tiet": 2,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 2: Nụ cười của Robot do con người lập trình",
        "noidung": "Học sinh quan sát giáo viên mô phỏng nạp thẻ lệnh cử chỉ cho robot giấy; nhận biết biểu hiện cảm xúc của máy là do kỹ sư con người lập trình trước; giải thích máy không tự vui buồn mà chỉ làm theo kịch bản có sẵn. Tích hợp [KN 18: Mức 1], [KN 45: Mức 1 - Nhận biết người điều khiển].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Mô hình robot giấy, tranh vẽ kỹ sư máy tính đang lập trình",
        "ma_yccd": "1.A1.3, 1.A1.4"
    },
    {
        "tiet": 3,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 3: Đôi mắt Camera và đôi tai Micro của thiết bị AI",
        "noidung": "Học sinh so sánh quạt máy cơ học với loa thông minh; thực hành trên lớp: chỉ đúng vị trí 'mắt nhìn' (Camera) và 'tai nghe' (Micro) trên thiết bị lớp học; nhận biết giác quan nhân tạo giúp máy thu nhận hình ảnh và âm thanh. Tích hợp [KN 19: Mức 1 - Nhận biết trực quan], [KN 27: Mức 1 - Ẩn dụ trực quan].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Quạt bàn cơ thông thường, loa thông minh/camera lớp học, thẻ hình mắt/tai",
        "ma_yccd": "1.C1.1, 1.C1.3"
    },
    {
        "tiet": 4,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 4: Trò chuyện lịch thiệp cùng trợ lý giọng nói",
        "noidung": "Học sinh quan sát biểu tượng micro trên màn hình; tập phát âm đồng thanh to, rõ từ khóa lệnh ('Xin chào', 'Bật đèn'); trải nghiệm máy nhận đúng khi nói rõ và báo lỗi khi la hét; rèn luyện thói quen chào hỏi và cảm ơn thiết bị lịch thiệp. Tích hợp [KN 1: Mức 1], [KN 2: Mức 1 - Phát âm to rõ], [KN 7: Mức 1 - Giao tiếp văn minh].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Máy chiếu, trợ lý giọng nói máy tính giáo viên demo, thẻ bài micro",
        "ma_yccd": "1.C1.2, 1.C1.4"
    },
    {
        "tiet": 5,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 5: Những thiết bị AI giúp ích quanh em",
        "noidung": "Học sinh kể tên các thiết bị tự động quen thuộc (robot hút bụi, đèn cảm ứng, loa nhắc giờ); ghép nối thẻ đồ dùng với công dụng có ích giúp con người tiết kiệm thời gian và giữ nhà cửa sạch sẽ. Tích hợp [KN 20: Mức 1 - Phân loại thiết bị], [KN 36: Mức 1 - Quan sát việc nhà].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bộ thẻ tranh thiết bị gia đình, bảng ghép nối công dụng A3",
        "ma_yccd": "1.A2.2, 1.A2.3"
    },
    {
        "tiet": 6,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 6: Cách máy thông minh thể hiện sự thân thiện",
        "noidung": "Học sinh lắng nghe và chỉ ra các biểu hiện thân thiện của AI (lời chào lễ phép, giọng nói ấm áp, biểu tượng khuôn mặt vui vẻ); nhận biết giọng nói và hình ảnh dễ thương giúp con người cảm thấy thoải mái, an tâm khi hợp tác. Tích hợp [KN 1: Mức 1], [KN 7: Mức 1].",
        "phanloai": "Cốt lõi",
        "hoclieu": "File âm thanh lời chào thân thiện của robot, thẻ tranh mặt cười LED",
        "ma_yccd": "1.A2.1"
    },
    {
        "tiet": 7,
        "chude": "Đạo đức AI",
        "ten_bai": "Bài 7: Máy thông minh làm việc tốt giúp con người",
        "noidung": "Học sinh nghe kể chuyện và phân tích tranh: Chú chó dẫn đường AI giúp người khiếm thị, robot hỗ trợ bác sĩ phát thuốc; nêu được những việc làm tốt đẹp mà con người sử dụng công nghệ để phục vụ cộng đồng. Tích hợp [KN 17: Mức 1 - Cảm thụ/Nghe chuyện AI bao trùm].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bộ tranh truyện: 'Chú Robot cứu hộ tí hon', giá trưng bày tranh",
        "ma_yccd": "1.B3.2"
    },
    {
        "tiet": 8,
        "chude": "Đạo đức AI",
        "ten_bai": "Bài 8: Bảo vệ bí mật cá nhân và phản xạ an toàn số",
        "noidung": "Học sinh phân biệt thông tin chung (bài hát yêu thích) vs thông tin bí mật (họ tên đầy đủ, địa chỉ nhà, số điện thoại bố mẹ); thực hành đóng vai: Lắc đầu nói 'Không! Chuyện này em không nói được!' khi thiết bị thông minh hỏi chuyện riêng; nhận biết không dùng máy trêu bạn. Tích hợp [KN 8: Mức 1], [KN 9: Mức 1 - Phản xạ nói Không], [KN 16: Mức 1].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Thẻ đỏ từ chối, thẻ tranh bí mật cá nhân, kịch bản đóng vai",
        "ma_yccd": "1.B1.1, 1.B3.1"
    },
    {
        "tiet": 9,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 9: Máy thông minh học từ ví dụ",
        "noidung": "Học sinh tham gia trò chơi Unplugged: Giáo viên cho 'chú robot hộp giấy' xem 10 thẻ hình quả cam; học sinh quan sát và giải thích máy nhận biết được đồ vật là nhờ con người nạp vào nhiều bức tranh ví dụ mẫu. Tích hợp [KN 28: Mức 1 - Nhận biết qua mẫu], [KN 29: Mức 1 - Thu thập dữ liệu].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Hộp robot các-tông có khe nhận thẻ, bộ 10 thẻ ảnh quả cam sắc nét",
        "ma_yccd": "1.D1.1"
    },
    {
        "tiet": 10,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 10: Thực hành Unplugged: Tuyển chọn ví dụ tốt cho máy",
        "noidung": "Học sinh thực hành theo nhóm: Kiểm tra rổ thẻ tranh, phát hiện và nhặt bỏ các thẻ bị rách, hình vẽ quá mờ hoặc dán nhầm hình con mèo sang rổ con chó (nhặt rác dữ liệu); nạp các thẻ rõ đẹp vào túi nhớ của robot. Tích hợp [KN 30: Mức 1 - Nhận biết nhãn], [KN 31: Mức 1 - Trò chơi nhặt rác dữ liệu].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bộ thẻ tranh hoa quả lẫn 3 thẻ rách/mờ, thùng rác dữ liệu mini",
        "ma_yccd": "1.D1.1 (Thực hành hóa)"
    },
    {
        "tiet": 11,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 11: Đồ dùng làm một việc và đồ dùng làm nhiều việc",
        "noidung": "Học sinh phân biệt đồ dùng đơn nhiệm (nồi cơm chỉ nấu cơm, quạt chỉ quạt mát) và thiết bị đa nhiệm (điện thoại vừa gọi điện, chụp ảnh, tính giờ); thực hành xếp thẻ tranh đồ dùng vào 2 cột trên bảng lớp. Tích hợp [KN 20: Mức 1 - Nhận biết qua phân loại].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bảng từ 2 cột 'Làm một việc' và 'Làm nhiều việc', bộ thẻ sticker",
        "ma_yccd": "1.D2.1, 1.D2.2"
    },
    {
        "tiet": 12,
        "chude": "Tích hợp 4 mạch",
        "ten_bai": "Bài 12: Tổng kết chuyên đề: Em làm chủ thiết bị thông minh",
        "noidung": "Học sinh thuyết minh bức tranh 'Người bạn AI làm việc tốt' của mình; thực hành nhắc lại 3 nguyên tắc vàng: Tự làm bài trước khi tra máy, giữ bí mật thông tin và tắt máy đúng giờ; giáo viên đánh giá quá trình theo Mục VI QĐ 2422. Tích hợp [KN 42: Mức 1], [KN 44: Mức 1], [KN 46: Mức 1].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bảng triển lãm tranh học sinh, sticker huy hiệu khen thưởng",
        "ma_yccd": "Mục VI QĐ 2422"
    }
]

GRADE1_36_EXPANDED = [
    {"tiet": 1, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 1: Cảm xúc của em và phản ứng của máy", "noidung": "Học sinh phân biệt cảm xúc thật của con người (vui, buồn, sợ hãi) với nét mặt mô phỏng của máy thông minh qua thẻ tranh. [1.A1.1, 1.A1.2] - Tích hợp [KN 18: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Bộ thẻ cảm xúc mặt cười/mặt mếu", "ma_yccd": "1.A1.1, 1.A1.2"},
    {"tiet": 2, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 2: Nụ cười của Robot do con người lập trình", "noidung": "Nhận biết biểu hiện cảm xúc của AI là do con người lập trình trước; máy không tự vui buồn. [1.A1.3, 1.A1.4] - Tích hợp [KN 18: Mức 1], [KN 45: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Mô hình robot giấy, tranh vẽ kỹ sư", "ma_yccd": "1.A1.3, 1.A1.4"},
    {"tiet": 3, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 3: Trò chơi đóng vai: Em là Robot biết cười", "noidung": "Học sinh đóng vai robot phản hồi nụ cười khi nghe hiệu lệnh quy ước trước; trải nghiệm cảm giác làm theo kịch bản máy móc. [Làm giàu INT-ENRICH: AI4K12 Big Idea 1] - Tích hợp [KN 18: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Mũ hóa trang robot, thẻ lệnh cử chỉ", "ma_yccd": ""},
    {"tiet": 4, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 4: Bàn tay con người sáng tạo và kiểm soát Robot", "noidung": "Khám phá công việc của các kỹ sư thiết kế robot; thực hành thao tác bấm nút công tắc dừng khẩn cấp khi máy gặp sự cố. [Đào sâu 1.A1.3] - Tích hợp [KN 45: Mức 1 - Phản xạ dừng máy].", "phanloai": "Mở rộng", "hoclieu": "Mô hình công tắc bật/tắt bằng bìa các-tông", "ma_yccd": ""},
    {"tiet": 5, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 5: Cách máy thông minh thể hiện sự thân thiện", "noidung": "Chỉ ra các cách máy thể hiện cảm xúc qua hình ảnh mặt cười, lời chào lễ phép, giọng nói thân thiện. [1.A2.1] - Tích hợp [KN 1: Mức 1], [KN 7: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "File âm thanh lời chào robot thân thiện", "ma_yccd": "1.A2.1"},
    {"tiet": 6, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 6: Những thiết bị AI giúp ích quanh em", "noidung": "Kể tên và mô tả công dụng của các thiết bị thông minh tự động trong đời sống gia đình. [1.A2.2, 1.A2.3] - Tích hợp [KN 20: Mức 1], [KN 36: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Bộ thẻ tranh thiết bị gia đình thông minh", "ma_yccd": "1.A2.2, 1.A2.3"},
    {"tiet": 7, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 7: Lời chào dễ thương giúp hợp tác vui vẻ", "noidung": "Nêu được rằng biểu hiện thân thiện giúp AI giao tiếp tự nhiên hơn, khiến người dùng cảm thấy thoải mái và dễ hợp tác. [1.A2.MR1] - Tích hợp [KN 7: Mức 1 - Giao tiếp văn minh].", "phanloai": "Mở rộng", "hoclieu": "Loa phát các đoạn hội thoại mẫu", "ma_yccd": "1.A2.MR1"},
    {"tiet": 8, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 8: Đôi mắt Camera và đôi tai Micro của thiết bị AI", "noidung": "Chỉ đúng vị trí camera và micro trên thiết bị; hiểu camera là mắt nhìn, micro là tai nghe của AI. [1.C1.1, 1.C1.3] - Tích hợp [KN 19: Mức 1], [KN 27: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Webcam lớp học, loa thông minh, thẻ mắt/tai", "ma_yccd": "1.C1.1, 1.C1.3"},
    {"tiet": 9, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 9: Khám phá 'Mắt thần' Camera nhận diện đồ vật", "noidung": "Quan sát trên máy chiếu: Camera quét và đóng khung vuông xanh khi nhận diện được đồ vật; phân biệt khi camera nhìn rõ vs bị che khuất. [1.C1.MR1] - Tích hợp [KN 1: Mức 1], [KN 22: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Máy chiếu, camera nhận diện đồ vật trực quan", "ma_yccd": "1.C1.MR1"},
    {"tiet": 10, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 10: Trò chuyện lịch thiệp cùng trợ lý giọng nói", "noidung": "Tập phát âm câu lệnh ngắn, rõ ràng; nhận biết trợ lý ảo hiểu lệnh đơn giản theo kịch bản định sẵn dưới sự giám sát. [1.C1.2, 1.C1.4] - Tích hợp [KN 2: Mức 1], [KN 7: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Trợ lý ảo trên máy tính giáo viên demo", "ma_yccd": "1.C1.2, 1.C1.4"},
    {"tiet": 11, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 11: So sánh cách học của người và cách học của máy", "noidung": "Trò chơi đối chiếu Unplugged: Em học nhận biết con mèo nhờ mẹ chỉ và vuốt ve mèo thật; máy học nhận biết mèo nhờ xem nhiều bức ảnh con mèo. [Làm giàu INT-ENRICH: AI4K12] - Tích hợp [KN 21: Mức 1 - Nhận biết qua ví dụ].", "phanloai": "Mở rộng", "hoclieu": "Bảng so sánh tranh vẽ 'Em học vs Máy học'", "ma_yccd": ""},
    {"tiet": 12, "chude": "Đạo đức AI", "ten_bai": "Bài 12: Máy thông minh làm việc tốt giúp con người", "noidung": "Nêu ví dụ con người sử dụng AI đúng cách vì mục đích tốt đẹp (bác sĩ chẩn đoán, xe cứu thương tự hành). [1.B3.2] - Tích hợp [KN 17: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Tranh truyện bác sĩ robot và người khiếm thị", "ma_yccd": "1.B3.2"},
    {"tiet": 13, "chude": "Đạo đức AI", "ten_bai": "Bài 13: Vẽ tranh: Người bạn AI làm việc tốt", "noidung": "Học sinh tự vẽ và thuyết minh bức tranh về việc tốt mà chú robot giúp đỡ gia đình hoặc bạn bè; nói rõ 'giúp ai, giúp việc gì'. [Đào sâu 1.B3.2] - Tích hợp [KN 37: Mức 1 - Vẽ tranh robot mơ ước].", "phanloai": "Mở rộng", "hoclieu": "Giấy vẽ A4, sáp màu, khung treo tranh", "ma_yccd": ""},
    {"tiet": 14, "chude": "Đạo đức AI", "ten_bai": "Bài 14: Bảo vệ bí mật cá nhân và phản xạ an toàn số", "noidung": "Nhận biết các thông tin bí mật cần bảo vệ; nhắc lại quy tắc không dùng máy thông minh để trêu chọc hoặc làm hại người khác. [1.B1.1, 1.B3.1] - Tích hợp [KN 8: Mức 1], [KN 16: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Tranh tình huống Nên và Không nên làm", "ma_yccd": "1.B1.1, 1.B3.1"},
    {"tiet": 15, "chude": "Đạo đức AI", "ten_bai": "Bài 15: Phản xạ nói 'Không!' khi máy hỏi chuyện riêng", "noidung": "Thực hành đóng vai tình huống: Đồ chơi thông minh hỏi tên trường lớp, số điện thoại của mẹ $\rightarrow$ Học sinh dứt khoát giơ thẻ đỏ và nói 'Không! Em không nói đâu!'. [Đào sâu 1.B1.1] - Tích hợp [KN 9: Mức 1 - Phản xạ hành vi].", "phanloai": "Mở rộng", "hoclieu": "Bộ thẻ đỏ/xanh, loa đồ chơi thông minh mô phỏng", "ma_yccd": ""},
    {"tiet": 16, "chude": "Đạo đức AI", "ten_bai": "Bài 16: Xử lý sự cố và Nguyên tắc đồng thuận của bé", "noidung": "Thực hành phản xạ: Thấy màn hình hiện hình ảnh đáng sợ $\rightarrow$ Tắt máy và gọi cô giáo (KN12); Muốn lấy tranh vẽ của bạn cho robot xem $\rightarrow$ Quay sang xin phép bạn (KN13). [Đào sâu 1.B3.1] - Tích hợp [KN 12: Mức 1], [KN 13: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Kịch bản đóng vai: 'Xin phép bạn trước khi chụp ảnh'", "ma_yccd": ""},
    {"tiet": 17, "chude": "Tích hợp", "ten_bai": "Bài 17: Đánh giá quá trình: Thử thách phản xạ an toàn Học kỳ I", "noidung": "Đánh giá quá trình theo tình huống: Từng học sinh bốc thăm 1 thẻ tình huống (máy hỏi tên, thấy ảnh lạ) và thể hiện phản xạ nói/hành động; giáo viên ghi nhận xét. [Mục VI QĐ 2422].", "phanloai": "Đánh giá quá trình", "hoclieu": "Bộ thẻ bốc thăm tình huống thực tế, bảng kiểm nhận xét", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 18, "chude": "Tích hợp", "ten_bai": "Bài 18: Báo cáo hồ sơ học tập và góc tranh số Học kỳ I", "noidung": "Học sinh giới thiệu hồ sơ tranh vẽ người bạn AI làm việc tốt; tự đánh giá thói quen sử dụng máy ngoan; giáo viên nhận xét tiến bộ. [Mục VI QĐ 2422].", "phanloai": "Đánh giá quá trình", "hoclieu": "Hồ sơ học tập của từng học sinh", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 19, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 19: Khám phá 'Tai thính' Micro phân biệt âm thanh", "noidung": "Quan sát và nhận biết máy thông minh phản ứng khác nhau khi nghe tiếng còi xe, tiếng chuông reo hoặc tiếng người nói. [1.C1.MR2] - Tích hợp [KN 27: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Loa máy tính phát các tệp âm thanh mẫu", "ma_yccd": "1.C1.MR2"},
    {"tiet": 20, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 20: Trò chơi Unplugged: Máy lắng nghe tiếng còi và tiếng nhạc", "noidung": "Trải nghiệm mô phỏng cơ chế xử lý âm thanh: Bạn đóng vai 'Micro' lắng nghe và giơ thẻ quy ước để bạn đóng vai 'Bộ não' ra quyết định. [Đào sâu 1.C1.MR2] - Tích hợp [KN 27: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Chuông lắc, còi nhựa, trống nhỏ, thẻ hành động", "ma_yccd": ""},
    {"tiet": 21, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 21: Tự chủ tư duy: Em tự làm bài trước khi hỏi máy", "noidung": "Học sinh thực hành phân biệt: Tự suy nghĩ làm tính đố trước khi dùng máy tính; không ỷ lại công nghệ; dừng chơi khi chuông báo hết giờ 20 phút. [Làm giàu INT-ENRICH: Singapore MOE] - Tích hợp [KN 42: Mức 1], [KN 44: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Đồng hồ cát 15 phút, phiếu bài tập tự làm", "ma_yccd": ""},
    {"tiet": 22, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 22: Máy thông minh học từ ví dụ", "noidung": "Nêu ví dụ về việc con người cho máy xem nhiều bức tranh để máy nhận biết được một đồ vật (xem nhiều ảnh quả cam). [1.D1.1] - Tích hợp [KN 28: Mức 1], [KN 29: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Bộ thẻ tranh mẫu quả cam, hộp nạp dữ liệu", "ma_yccd": "1.D1.1"},
    {"tiet": 23, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 23: Cần nhiều ví dụ khác nhau để máy học đúng", "noidung": "Giải thích được rằng nếu chỉ đưa 1 bức tranh thì máy dễ đoán nhầm khi gặp đồ vật ở góc nhìn khác hoặc màu sắc khác. [1.D1.MR1] - Tích hợp [KN 22: Mức 1], [KN 32: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "5 bức ảnh chụp cùng một đồ vật ở góc thẳng/nghiêng/xa/gần", "ma_yccd": "1.D1.MR1"},
    {"tiet": 24, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 24: Trò chơi Unplugged: Dọn rác dữ liệu dạy máy", "noidung": "Thực hành theo nhóm: Tìm và loại bỏ các bức tranh vẽ nguệch ngoạc, tranh dán nhầm nhãn trước khi đưa vào 'bộ nhớ' của robot. [Đào sâu 1.D1.MR1] - Tích hợp [KN 30: Mức 1], [KN 31: Mức 1 - Trò chơi nhặt rác dữ liệu].", "phanloai": "Mở rộng", "hoclieu": "Tập thẻ hình con vật có 4 thẻ sai nhãn, thùng rác dữ liệu", "ma_yccd": ""},
    {"tiet": 25, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 25: Nhận biết máy thông minh đơn năng", "noidung": "Nhận biết được có đồ dùng chỉ làm được một việc riêng (nồi cơm điện, cân điện tử, quạt cảm ứng). [1.D2.1] - Tích hợp [KN 20: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Bộ thẻ tranh thiết bị gia dụng đơn năng", "ma_yccd": "1.D2.1"},
    {"tiet": 26, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 26: Xếp nhóm máy làm một việc và nhiều việc", "noidung": "Xếp được các thẻ tranh đồ dùng thông minh vào 2 nhóm: nhóm chỉ làm một việc và nhóm làm nhiều việc khác nhau. [1.D2.2] - Tích hợp [KN 20: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Bảng phân loại A3 hai cột, thẻ sticker", "ma_yccd": "1.D2.2"},
    {"tiet": 27, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 27: Trò chơi vận động: Đi tìm đồ dùng đa năng", "noidung": "Trò chơi vận động tiếp sức: Học sinh chạy lên gắn đúng thẻ đồ dùng đa nhiệm (điện thoại thông minh, máy tính bảng) vào ngôi nhà công nghệ. [Đào sâu 1.D2.2] - Tích hợp [KN 20: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Mô hình ngôi nhà thông minh treo tường, rổ thẻ bài", "ma_yccd": ""},
    {"tiet": 28, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 28: Kể chuyện 4 bước dạy máy thông minh", "noidung": "Lắng nghe câu chuyện trực quan 4 bước: (1) Thu thập ví dụ -> (2) Dạy máy học -> (3) Đố máy nhận diện -> (4) Máy giúp con người. [Làm giàu INT-ENRICH: Experience AI] - Tích hợp [KN 34: Mức 1 - Nghe kể chuyện 4 bước].", "phanloai": "Mở rộng", "hoclieu": "Bộ tranh liên hoàn 4 cảnh 'Bé dạy cún máy học việc'", "ma_yccd": ""},
    {"tiet": 29, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 29: Khởi động dự án: Chú Robot giấy của em (Thiết kế thân máy)", "noidung": "Học sinh dùng hộp các-tông tái chế trang trí thân robot; gắn biểu tượng Camera ở mắt và Micro ở tai. [Tích hợp KN 27, KN 36, KN 37: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Hộp giấy tái chế, giấy màu, kéo an toàn, hồ dán", "ma_yccd": ""},
    {"tiet": 30, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 30: Chế tạo túi dữ liệu mẫu cho Robot giấy", "noidung": "Mỗi nhóm vẽ 6 thẻ tranh mẫu về hoa quả hoặc con vật; dán nhãn tên rõ ràng để nạp vào túi dữ liệu của robot. [Tích hợp KN 29, KN 30: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Thẻ bìa cứng cắt sẵn kích thước chuẩn, bút dạ màu", "ma_yccd": ""},
    {"tiet": 31, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 31: Thử thách kiểm tra: Đố Robot nhận diện mẫu mới", "noidung": "Thử đưa 1 đồ vật thật hoặc 1 tranh vẽ lạ trước camera giấy của robot; quan sát tình huống 'robot bị bối rối' khi gặp mẫu chưa từng học; học sinh giải thích vì sao máy đoán nhầm. [Tích hợp KN 22: Mức 1 - Quan sát trực quan].", "phanloai": "Mở rộng", "hoclieu": "Vật mẫu kiểm thử lạ (quả khế nhựa, mũ len)", "ma_yccd": ""},
    {"tiet": 32, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 32: Dán nhãn quy tắc an toàn và trách nhiệm của bé", "noidung": "Học sinh gắn 3 nhãn dán quy ước lên thân robot: 'Giữ bí mật', 'Tắt máy khi không dùng', 'Em chịu trách nhiệm'. [Tích hợp KN 45, KN 46: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Bộ sticker nội quy sử dụng robot an toàn", "ma_yccd": ""},
    {"tiet": 33, "chude": "Tích hợp", "ten_bai": "Bài 33: Đánh giá quá trình: Đánh giá kỹ năng qua dự án Robot giấy", "noidung": "Giáo viên quan sát từng nhóm thuyết minh: Giới thiệu camera/micro, giải thích dữ liệu nạp vào, trình bày quy tắc an toàn; đánh giá theo bảng kiểm. [Mục VI QĐ 2422].", "phanloai": "Đánh giá quá trình", "hoclieu": "Bảng kiểm quan sát năng lực học sinh Lớp 1", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 34, "chude": "Tích hợp", "ten_bai": "Bài 34: Ngày hội Triển lãm & Sáng tạo AI nhí Lớp 1", "noidung": "Trưng bày toàn bộ mô hình robot giấy và bộ tranh của lớp; học sinh tham quan, giải thích ý tưởng sản phẩm cho các bạn lớp khác và thầy cô.", "phanloai": "Đánh giá quá trình", "hoclieu": "Khu vực trưng bày sản phẩm, phiếu khen thưởng", "ma_yccd": ""},
    {"tiet": 35, "chude": "Tích hợp", "ten_bai": "Bài 35: Củng cố hành trang số: Bé tự tin và an toàn cùng công nghệ", "noidung": "Trò chơi rung chuông vàng mini củng cố phản xạ: Giữ bí mật cá nhân, lễ phép với máy, tự giác làm bài tập; trao huy hiệu hoàn thành Lớp 1.", "phanloai": "Đánh giá quá trình", "hoclieu": "Huy hiệu 'Nhà sáng tạo AI nhí Lớp 1'", "ma_yccd": ""},
    {"tiet": 36, "chude": "Tích hợp", "ten_bai": "Bài 36: Báo cáo chuyên đề cốt lõi: Em làm chủ thiết bị thông minh", "noidung": "Tổng kết đánh giá chuyên đề bắt buộc theo Mục VI QĐ 2422; hoàn thiện hồ sơ minh chứng học tập năm học Lớp 1.", "phanloai": "Cốt lõi", "hoclieu": "Sổ theo dõi đánh giá quá trình học sinh Lớp 1", "ma_yccd": "Mục VI QĐ 2422"}
]
