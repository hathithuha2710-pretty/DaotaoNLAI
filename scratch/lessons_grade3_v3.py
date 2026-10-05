# -*- coding: utf-8 -*-
"""
Dữ liệu PPCT Lớp 3 - Phiên bản v3.0 Chuẩn hóa sâu theo Ma trận 46 Kỹ năng & QĐ 2422
Đã xử lý triệt để:
- Sửa lệch mức độ: KN11 về đúng Mức 1 (Nhận biết hiện tượng), KN33 về đúng Mức 1 (Nhận biết qua ví dụ), KN35 về đúng Mức 1 (Quan sát cô sửa máy)
- Bổ sung hành vi thực hành rõ: Tự làm trước - Tra máy sau (KN42), Thám tử kiểm chứng chống ảo giác AI (KN23), Lọc xóa ảnh rác (KN31)
- Tách bạch rõ Lập trình phản hồi Scratch (KN40) và Đồng sáng tạo sản phẩm cùng AI (KN39)
- Đảm bảo 100% YCCĐ Cốt lõi (21) và Mở rộng (11) theo QĐ 2422.
"""

GRADE3_12_CORE = [
    {
        "tiet": 1,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 1: Trợ lý học tập thông minh: Cơ hội và cách dùng đúng",
        "noidung": "Học sinh thao tác trên máy tính phòng máy có hướng dẫn: Nhấp chuột kích hoạt micro trên phần mềm học tập; tra cứu nghĩa từ mới môn Tiếng Việt và nghe phát âm mẫu Tiếng Anh; xác định vùng nhập câu lệnh và vùng hiển thị câu trả lời; áp dụng nguyên tắc chỉ dùng AI hỗ trợ giải nghĩa, không chép bài giải sẵn. Tích hợp [KN 1: Mức 2 - Thao tác phòng máy], [KN 2: Mức 2], [KN 3: Mức 2 - Thực hành có hướng dẫn].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Phòng máy tính, tai nghe có micro, phần mềm tra từ điển học tập trực quan",
        "ma_yccd": "3.A1.1, 3.A1.2"
    },
    {
        "tiet": 2,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 2: Người học thông thái: Tự suy nghĩ trước khi hỏi máy",
        "noidung": "Học sinh thực hiện bài tập thực hành '3 bước tự chủ': (1) Tự mình suy nghĩ giải bài toán đố trong 5 phút -> (2) Sử dụng AI tra cứu gợi ý phương pháp -> (3) So sánh cách làm của bản thân và AI; phân biệt giữa sử dụng AI hỗ trợ đúng lúc với phụ thuộc lười suy nghĩ; nêu các tình huống gây rủi ro khi dùng AI. Tích hợp [KN 42: Mức 2 - Thực hành có hướng dẫn].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Phiếu bài tập thực hành 3 bước tự chủ, bảng so sánh cách giải",
        "ma_yccd": "3.A1.3, 3.A1.4"
    },
    {
        "tiet": 3,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 3: Bộ ba câu hỏi vàng trước khi quyết định dùng AI",
        "noidung": "Học sinh thực hành vận dụng bộ 3 câu hỏi trước khi bấm máy: (1) Em đã tự suy nghĩ chưa? (2) Có an toàn cho thông tin cá nhân không? (3) Thầy cô có cho phép không?; phân tích tình huống: Nếu AI trả lời sai thì hậu quả gì xảy ra để rèn luyện thói quen ra quyết định có điều kiện. Tích hợp [KN 43: Mức 2 - Thực hành có hướng dẫn].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Thẻ ghi nhớ 'Bộ ba câu hỏi vàng', phiếu phân tích tình huống thực tế",
        "ma_yccd": "3.A1.5"
    },
    {
        "tiet": 4,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 4: AI trong trường học của em",
        "noidung": "Học sinh nhận biết các thiết bị và ứng dụng AI trong trường học (camera điểm danh thông minh, phần mềm luyện đọc ngoại ngữ); trình bày mục đích dùng AI là hỗ trợ học sinh, thầy cô và nhân viên; khẳng định AI không bao giờ thay thế được sự giảng dạy của thầy cô và nỗ lực cá nhân. Tích hợp [KN 3: Mức 2], [KN 17: Mức 1 - Quan sát/Thảo luận].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Sơ đồ trường học thông minh, hình ảnh camera điểm danh trường học",
        "ma_yccd": "3.A2.1, 3.A2.2, 3.A2.3"
    },
    {
        "tiet": 5,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 5: Khi AI nói sai: Kỹ năng kiểm chứng thông tin học tập",
        "noidung": "Học sinh tham gia hoạt động 'Thám tử kiểm chứng': Đọc một đoạn văn bản do AI sinh ra có chứa 3 lỗi sai kiến thức Lịch sử - Địa lý; học sinh mở sách giáo khoa đối chiếu, gạch chân điểm sai và viết lại thông tin chính xác; trình bày nguyên tắc luôn kiểm tra lại kết quả của AI. Tích hợp [KN 23: Mức 2 - Thực hành kiểm chứng có đối chiếu].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Phiếu bài đọc có lỗi ảo giác AI, sách giáo khoa môn Lịch sử & Địa lý Lớp 3",
        "ma_yccd": "3.A3.1, 3.A3.2"
    },
    {
        "tiet": 6,
        "chude": "Đạo đức AI",
        "ten_bai": "Bài 6: Cảnh giác trước nội dung giả mạo do AI tạo ra",
        "noidung": "Học sinh quan sát so sánh cặp hình ảnh: Ảnh chụp quả táo thật vs Ảnh ghép quả táo có cánh bay lơ lửng do AI tạo ra; nhận biết hiện tượng nội dung giả mạo (Deepfake); nêu được ví dụ thông tin hoặc hình ảnh do AI tạo ra có thể sai lệch hoặc gây hiểu lầm; rèn luyện thói quen không chia sẻ ảnh lạ khi chưa hỏi thầy cô. Tích hợp [KN 11: Mức 1 - Nhận biết hiện tượng].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bộ tranh so sánh ảnh thật và ảnh do AI tạo sinh, biển báo 'Chưa kiểm chứng'",
        "ma_yccd": "3.B2.1"
    },
    {
        "tiet": 7,
        "chude": "Đạo đức AI",
        "ten_bai": "Bài 7: Văn hóa AI học đường: Nói không với hành vi gây hại",
        "noidung": "Học sinh nhận biết được rằng không nên tạo ra hoặc sử dụng AI cho các hành vi sai trái, chế ảnh trêu chọc bạn hoặc gian lận bài tập; thực hành gõ câu lệnh có chủ vị đầy đủ, lịch sự trên phần mềm học tập; cam kết văn hóa ứng xử số văn minh. Tích hợp [KN 7: Mức 2 - Gõ lệnh lịch sự], [KN 15: Mức 2], [KN 16: Mức 2 - Kiểm soát không gây hại].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bản cam kết văn hóa số học sinh Lớp 3, kịch bản ứng xử tình huống",
        "ma_yccd": "3.B3.1"
    },
    {
        "tiet": 8,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 8: Khám phá Dữ liệu: Nền tảng của trí tuệ nhân tạo",
        "noidung": "Học sinh tìm hiểu khái niệm dữ liệu qua các ví dụ cụ thể (hình ảnh các loài hoa, âm thanh nốt nhạc, chữ viết văn bản); quan sát thư mục dữ liệu trên máy tính phòng máy; giải thích cách AI dựa vào các đặc trưng trong dữ liệu để nhận biết đồ vật. Tích hợp [KN 28: Mức 2 - Thao tác tệp dữ liệu], [KN 30: Mức 2 - Nhận biết nhãn tệp].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Thư mục ảnh mẫu hoa lá trên máy tính phòng máy, thẻ bài đặc trưng",
        "ma_yccd": "3.C4.1"
    },
    {
        "tiet": 9,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 9: Quy tắc Nếu - Thì trong ứng dụng thông minh",
        "noidung": "Học sinh làm quen cấu trúc logic: 'Nếu [Điều kiện cảm biến nhận được] $\rightarrow$ Thì [Hành động thực hiện]'; thực hành ghép khối lệnh logic trực quan: 'Nếu Camera thấy thẻ màu đỏ $\rightarrow$ Thì Robot phát tiếng còi dừng lại'. Tích hợp [KN 40: Mức 2 - Thực hành khối lệnh cơ bản].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Khối lệnh điều kiện Scratch in màu trực quan, mô hình cảm biến giấy",
        "ma_yccd": "3.C5.1"
    },
    {
        "tiet": 10,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 10: Học máy trên dữ liệu: Bài toán phân loại và dự đoán",
        "noidung": "Học sinh nêu đặc điểm chính của học máy là học trên dữ liệu mẫu; nêu tình huống áp dụng (nông trại thông minh phân loại rau củ, dự báo mưa lũ); nhận biết bài toán phân loại (chia đối tượng vào nhóm) và bài toán dự đoán qua trò chơi tình huống trực quan. Tích hợp [KN 33: Mức 1 - Nhận biết qua ví dụ], [KN 34: Mức 2 - Vận hành 4 bước].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Tranh ứng dụng nông nghiệp công nghệ cao, sơ đồ phân loại vs dự đoán",
        "ma_yccd": "3.C5.2, 3.C5.3, 3.C5.4"
    },
    {
        "tiet": 11,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 11: Huấn luyện AI và nguyên tắc dữ liệu chất lượng",
        "noidung": "Học sinh trình bày 2 bước cốt lõi: Thu thập ví dụ -> Cho máy học; quan sát thực nghiệm nạp tập ảnh bị dán nhầm nhãn khiến máy nhận diện sai; nêu các tiêu chuẩn dữ liệu tốt (đủ số lượng, đa dạng góc nhìn, nhãn đúng); giải thích nguyên lý 'Rác vào - Rác ra' (dữ liệu sai thì AI hoạt động sai). Tích hợp [KN 22: Mức 2], [KN 29: Mức 2], [KN 31: Mức 2 - Lọc dữ liệu].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Sơ đồ chu trình học máy, bộ dữ liệu thử nghiệm có ảnh sai nhãn",
        "ma_yccd": "3.D1.1, 3.D2.1, 3.D2.2, 3.D2.3"
    },
    {
        "tiet": 12,
        "chude": "Tích hợp 4 mạch",
        "ten_bai": "Bài 12: Tổng kết chuyên đề: Em là công dân số thông thái",
        "noidung": "Học sinh trình bày nhật ký kiểm chứng thông tin và sản phẩm thực hành học máy; khẳng định năng lực tự chủ tư duy, không phụ thuộc AI và kiểm tra dữ liệu cẩn thận; giáo viên đánh giá quá trình theo Mục VI QĐ 2422. Tích hợp [KN 42: Mức 2], [KN 46: Mức 2].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Hồ sơ học tập của học sinh, bảng tự đánh giá năng lực số Lớp 3",
        "ma_yccd": "Mục VI QĐ 2422"
    }
]

GRADE3_36_EXPANDED = [
    {"tiet": 1, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 1: Trợ lý học tập thông minh: Cơ hội và cách dùng đúng", "noidung": "Nhận biết tình huống AI hỗ trợ học tập; thực hành nhấp chuột kích hoạt micro tra nghĩa từ mới; xác định vùng câu lệnh và phản hồi. [3.A1.1, 3.A1.2] - Tích hợp [KN 1: Mức 2], [KN 3: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Phần mềm từ điển thông minh phòng máy", "ma_yccd": "3.A1.1, 3.A1.2"},
    {"tiet": 2, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 2: Thực hành: Khai thác trợ lý học tập có hướng dẫn", "noidung": "Thực hành sử dụng trợ lý học tập thông minh, ứng dụng học ngoại ngữ dưới sự hướng dẫn của giáo viên: phát âm từ vựng tiếng Anh trước tai nghe có micro và quan sát điểm số đánh giá phát âm của máy. [3.A1.MR1] - Tích hợp [KN 2: Mức 2], [KN 3: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Máy tính phòng máy, tai nghe có micro", "ma_yccd": "3.A1.MR1"},
    {"tiet": 3, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 3: Người học thông thái: Tự suy nghĩ trước khi hỏi máy", "noidung": "Thực hành 3 bước tự chủ: Tự làm trước -> Tham khảo AI sau -> So sánh đối chiếu; phân biệt giữa hỗ trợ và phụ thuộc ỷ lại. [3.A1.3, 3.A1.4] - Tích hợp [KN 42: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Phiếu bài tập thực hành 3 bước tự chủ", "ma_yccd": "3.A1.3, 3.A1.4"},
    {"tiet": 4, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 4: Tự chủ tư duy: Chống ỷ lại nhận thức công nghệ", "noidung": "Nêu được hậu quả của việc phụ thuộc quá mức vào AI (giảm tư duy sáng tạo, lười suy nghĩ, mất kỹ năng tự giải quyết vấn đề); đóng vai xử lý tình huống từ chối chép đáp án của máy. [3.A1.MR2] - Tích hợp [KN 42: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Tranh biếm họa: 'Bạn nhỏ quên cách tính nhẩm', kịch bản đóng vai", "ma_yccd": "3.A1.MR2"},
    {"tiet": 5, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 5: Bộ ba câu hỏi vàng trước khi quyết định dùng AI", "noidung": "Vận dụng bộ ba câu hỏi: Tự làm chưa? An toàn không? Có được phép không?; cân nhắc hậu quả nếu AI trả lời sai để ra quyết định thận trọng. [3.A1.5] - Tích hợp [KN 43: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Thẻ 'Bộ ba câu hỏi vàng', phiếu tình huống", "ma_yccd": "3.A1.5"},
    {"tiet": 6, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 6: Người dùng có trách nhiệm: Tự bảo vệ và kiểm tra trước khi dùng", "noidung": "Giải thích được rằng việc suy nghĩ và kiểm tra trước khi dùng AI giúp tự bảo vệ bản thân và trở thành người dùng có trách nhiệm; thực hành gạch bỏ thông tin nhạy cảm trước khi nạp vào máy. [3.A1.MR3] - Tích hợp [KN 8: Mức 2], [KN 9: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Bảng tình huống thực hành gạch bỏ thông tin cá nhân", "ma_yccd": "3.A1.MR3"},
    {"tiet": 7, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 7: AI trong trường học của em", "noidung": "Nhận biết ứng dụng/thiết bị AI trong trường học; nêu mục đích dùng AI là hỗ trợ học sinh, thầy cô; nêu các đối tượng được hỗ trợ. [3.A2.1, 3.A2.2, 3.A2.3] - Tích hợp [KN 3: Mức 2], [KN 17: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Sơ đồ trường học số thông minh", "ma_yccd": "3.A2.1, 3.A2.2, 3.A2.3"},
    {"tiet": 8, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 8: Trường học tương lai: Khi công nghệ đồng hành", "noidung": "Mô tả được trường học mong muốn trong tương lai – nơi có sự hỗ trợ của AI nhưng vẫn giữ trọn vẹn tình cảm thầy trò và sự tôn trọng lẫn nhau. [3.A2.MR1] - Tích hợp [KN 37: Mức 2 - Mô hình hóa ý tưởng].", "phanloai": "Mở rộng", "hoclieu": "Giấy vẽ A3, tranh ý tưởng trường học tương lai", "ma_yccd": "3.A2.MR1"},
    {"tiet": 9, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 9: Xây dựng quy tắc sử dụng AI trong học tập", "noidung": "Đề xuất một số nguyên tắc khi sử dụng AI trong học tập; nêu rõ mục tiêu AI là hỗ trợ con người chứ không thay thế thầy cô hay sự nỗ lực của học sinh. [3.A2.MR2, 3.A2.MR3] - Tích hợp [KN 44: Mức 2 - Quản trị thời gian], [KN 45: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Bảng nội quy sử dụng thiết bị AI của lớp", "ma_yccd": "3.A2.MR2, 3.A2.MR3"},
    {"tiet": 10, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 10: Khi AI nói sai: Kỹ năng kiểm chứng thông tin học tập", "noidung": "Nêu ví dụ AI có thể sai; thực hành đối chiếu câu trả lời của AI với SGK, gạch chân lỗi sai và sửa lại đúng. [3.A3.1, 3.A3.2] - Tích hợp [KN 23: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Văn bản in câu trả lời của AI, SGK đối chiếu", "ma_yccd": "3.A3.1, 3.A3.2"},
    {"tiet": 11, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 11: Thử tài thám tử: Bắt lỗi ảo giác thông tin của máy", "noidung": "Thực hành trên máy tính phòng máy: Nhập câu hỏi và đọc phản hồi của chatbot; phát hiện 2 điểm vô lý (ảo giác AI) và ghi chú nguồn sách đối chiếu để sửa. [Đào sâu 3.A3.2] - Tích hợp [KN 23: Mức 2 - Thực hành có hướng dẫn].", "phanloai": "Mở rộng", "hoclieu": "Máy tính phòng máy, phiếu ghi chép 'Thám tử bắt lỗi AI'", "ma_yccd": ""},
    {"tiet": 12, "chude": "Đạo đức AI", "ten_bai": "Bài 12: Cảnh giác trước nội dung giả mạo do AI tạo ra", "noidung": "Nhận biết hiện tượng thông tin hoặc hình ảnh do AI tạo ra có thể sai lệch, giả mạo hoặc gây hiểu lầm; không chia sẻ khi chưa kiểm chứng. [3.B2.1] - Tích hợp [KN 11: Mức 1 - Nhận biết hiện tượng].", "phanloai": "Cốt lõi", "hoclieu": "Bộ tranh ảnh so sánh thật vs giả mạo minh họa", "ma_yccd": "3.B2.1"},
    {"tiet": 13, "chude": "Đạo đức AI", "ten_bai": "Bài 13: Quan sát dấu hiệu bất thường trên hình ảnh do AI tạo", "noidung": "Quan sát tranh ảnh minh họa: Chỉ ra các chi tiết bất thường trên ảnh vẽ do AI tạo ra (bàn tay 6 ngón, chữ viết trên biển bị biến dạng); hiểu mắt máy tính vẫn có thể nhầm lẫn. [Đào sâu 3.B2.1] - Tích hợp [KN 11: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Bộ tranh phóng to các lỗi vẽ chi tiết của AI", "ma_yccd": ""},
    {"tiet": 14, "chude": "Đạo đức AI", "ten_bai": "Bài 14: Văn hóa AI học đường: Nói không với hành vi gây hại", "noidung": "Nhận biết không được tạo ra hoặc dùng AI cho hành vi sai trái, xúc phạm hoặc gây hại cho bạn; thực hành gõ câu lệnh lịch sự. [3.B3.1] - Tích hợp [KN 7: Mức 2], [KN 16: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Bản cam kết văn hóa số học sinh Lớp 3", "ma_yccd": "3.B3.1"},
    {"tiet": 15, "chude": "Đạo đức AI", "ten_bai": "Bài 15: Cung cấp dữ liệu công bằng, không phân biệt đối xử", "noidung": "Nêu được rằng con người cần cung cấp dữ liệu đúng và đa dạng để AI không thiên kiến, không phân biệt đối xử; phân tích ví dụ tập ảnh lớp học cần đủ nam và nữ. [3.B3.MR1] - Tích hợp [KN 24: Mức 1], [KN 32: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Bộ thẻ ảnh đại diện học sinh đa dạng vùng miền", "ma_yccd": "3.B3.MR1"},
    {"tiet": 16, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 16: Làm quen với cấu trúc câu lệnh rõ ràng (Prompting)", "noidung": "Học sinh so sánh 2 câu lệnh: Lệnh cộc lốc ('Chó') vs Lệnh rõ việc ('Kể tên 3 giống chó thông minh'); nhận biết nói rõ yêu cầu giúp AI trả lời chính xác hơn; quan sát cô giáo nắn chỉnh lệnh lần 2. [Làm giàu INT-ENRICH: Google BIA] - Tích hợp [KN 4: Mức 1 - Nhận biết], [KN 6: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Bảng so sánh 2 câu lệnh trên máy chiếu", "ma_yccd": ""},
    {"tiet": 17, "chude": "Tích hợp", "ten_bai": "Bài 17: Đánh giá quá trình: Báo cáo hồ sơ học tập Học kỳ I", "noidung": "Học sinh trình bày hồ sơ số: Phiếu thám tử kiểm chứng thông tin, bài vẽ trường học tương lai và phiếu thực hành 3 bước tự chủ; giáo viên nhận xét tiến bộ theo Mục VI QĐ 2422.", "phanloai": "Đánh giá quá trình", "hoclieu": "Hồ sơ học tập số lưu trên máy tính phòng tin", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 18, "chude": "Tích hợp", "ten_bai": "Bài 18: Báo cáo dự án: Cẩm nang Sử dụng AI an toàn của Lớp 3", "noidung": "Các nhóm hoàn thiện và thuyết trình tờ gấp cẩm nang: 'Quy tắc vàng khi dùng trợ lý AI trong học tập' hướng dẫn các bạn học sinh trong trường. [Mục VI QĐ 2422].", "phanloai": "Đánh giá quá trình", "hoclieu": "Tờ gấp cẩm nang an toàn số A4 của các nhóm", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 19, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 19: Khám phá Dữ liệu: Nền tảng của trí tuệ nhân tạo", "noidung": "Trình bày khái niệm dữ liệu qua ví dụ (hình ảnh, âm thanh, văn bản) và cách AI sử dụng dữ liệu để nhận diện. [3.C4.1] - Tích hợp [KN 28: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Tệp hình ảnh các loại hoa quả trên máy tính", "ma_yccd": "3.C4.1"},
    {"tiet": 20, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 20: Xác định đặc trưng nổi bật của bộ dữ liệu", "noidung": "Xác định được đặc trưng của một số bộ dữ liệu đơn giản: chỉ ra viền mép lá, màu sắc quả, hình dạng cánh hoa trên các tệp ảnh mẫu. [3.C4.MR1] - Tích hợp [KN 28: Mức 2], [KN 30: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Bảng phân tích đặc trưng các mẫu vật", "ma_yccd": "3.C4.MR1"},
    {"tiet": 21, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 21: Quy tắc Nếu - Thì trong ứng dụng thông minh", "noidung": "Mô tả cấu trúc 'Nếu... Thì...' trong việc giải quyết tình huống bằng AI đơn giản; ghép các thẻ điều kiện logic trực quan. [3.C5.1] - Tích hợp [KN 40: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Thẻ khối lệnh logic Nếu... Thì...", "ma_yccd": "3.C5.1"},
    {"tiet": 22, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 22: Khám phá các công cụ AI dựa trên quy tắc", "noidung": "Nêu được một số công cụ AI đơn giản sử dụng cấu trúc 'Nếu... Thì...' (hệ thống tự động trả lời theo từ khóa định sẵn, hệ thống lọc thư rác); thực hành thử gõ từ khóa kích hoạt phản hồi định sẵn. [3.C5.MR1] - Tích hợp [KN 40: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Chatbot quy tắc từ khóa mẫu trên Scratch demo", "ma_yccd": "3.C5.MR1"},
    {"tiet": 23, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 23: Học máy trên dữ liệu: Bài toán phân loại và dự đoán", "noidung": "Nêu đặc điểm của học máy; nêu tình huống áp dụng; nhận biết bài toán phân loại và bài toán dự đoán qua ví dụ thực tế. [3.C5.2, 3.C5.3, 3.C5.4] - Tích hợp [KN 33: Mức 1], [KN 34: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Tranh nông nghiệp thông minh, sơ đồ 2 bài toán", "ma_yccd": "3.C5.2, 3.C5.3, 3.C5.4"},
    {"tiet": 24, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 24: Trải nghiệm bài toán phân loại trên Teachable Machine", "noidung": "Minh họa bài toán phân loại hình ảnh bằng công cụ trực quan (Google Teachable Machine): Học sinh quan sát giáo viên hướng dẫn nạp 2 lớp ảnh và kiểm thử; làm rõ Teachable Machine chuyên cho bài toán phân loại nhận diện. [3.C5.MR2] - Tích hợp [KN 34: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Trình duyệt Teachable Machine phòng máy, webcam", "ma_yccd": "3.C5.MR2"},
    {"tiet": 25, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 25: Huấn luyện AI và nguyên tắc dữ liệu chất lượng", "noidung": "Trình bày 2 bước cốt lõi: Thu thập ví dụ -> Cho máy học; hiểu dữ liệu sai thì AI hoạt động sai. [3.D1.1, 3.D2.1, 3.D2.2, 3.D2.3] - Tích hợp [KN 22: Mức 2], [KN 29: Mức 2].", "phanloai": "Cốt lõi", "hoclieu": "Sơ đồ chu trình học máy", "ma_yccd": "3.D1.1, 3.D2.1, 3.D2.2, 3.D2.3"},
    {"tiet": 26, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 26: Thực hành kiểm tra dữ liệu và loại bỏ nhãn sai", "noidung": "Thực hành kiểm tra một bộ thẻ dữ liệu mẫu trên máy tính phòng máy: Mở thư mục ảnh thực hành, phát hiện 4 ảnh bị dán nhầm nhãn và 2 ảnh quá mờ nhòe; thực hiện thao tác xóa bỏ tệp rác trước khi huấn luyện. [3.D2.MR1] - Tích hợp [KN 30: Mức 2], [KN 31: Mức 2 - Thực hành làm sạch dữ liệu].", "phanloai": "Mở rộng", "hoclieu": "Thư mục ảnh thực hành dán nhầm nhãn phòng máy", "ma_yccd": "3.D2.MR1"},
    {"tiet": 27, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 27: Thí nghiệm 'Rác vào - Rác ra' (Garbage In - Garbage Out)", "noidung": "Quan sát thử nghiệm: Khi tập dữ liệu bị nạp ảnh sai, mô hình nhận diện sẽ đưa ra kết quả nhầm lẫn; học sinh rút ra kết luận khoa học về trách nhiệm cung cấp dữ liệu sạch và trung thực. [Đào sâu 3.D2.3] - Tích hợp [KN 15: Mức 2], [KN 22: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Mô hình Teachable Machine bị nạp dữ liệu sai demo", "ma_yccd": ""},
    {"tiet": 28, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 28: Dự án Stem/AI: Nhận diện cử chỉ tay (Tiết 1 - Thu thập dữ liệu)", "noidung": "Xác định bài toán nhận diện 2 cử chỉ tay (Nắm tay và Xòe tay); các thành viên trong nhóm thực hành xin phép bạn (KN13) và chụp 20 ảnh mẫu rõ nét cho mỗi cử chỉ qua Webcam; gán nhãn tên chính xác. [KN 13: Mức 2], [KN 29: Mức 2], [KN 30: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Webcam phòng máy tính, bảng hướng dẫn tư thế tay", "ma_yccd": ""},
    {"tiet": 29, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 29: Dự án Stem/AI: Nhận diện cử chỉ tay (Tiết 2 - Huấn luyện & Kiểm thử)", "noidung": "Học sinh bấm nút 'Train Model'; quan sát thanh tiến trình học máy; thực hành đưa tay trước webcam để kiểm thử; đọc thanh chỉ số tin cậy (Confidence Bar); ghi nhận các trường hợp máy nhận diện đúng và trường hợp bị phân vân. [KN 25: Mức 1 - Quan sát thanh đo], [KN 34: Mức 2].", "phanloai": "Mở rộng", "hoclieu": "Giao diện Teachable Machine, phiếu ghi kết quả kiểm thử", "ma_yccd": ""},
    {"tiet": 30, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 30: Dự án Stem/AI: Cải tiến dữ liệu khi mô hình nhận diện sai", "noidung": "Học sinh kiểm tra lại tập ảnh huấn luyện, xóa bỏ 2 ảnh bị mờ rung (KN31); chụp bổ sung 10 ảnh tay nghiêng; quan sát cô giáo hướng dẫn bấm Train lại và so sánh kết quả cải thiện (KN35 ở mức quan sát). [KN 31: Mức 2 - Làm sạch dữ liệu], [KN 35: Mức 1 - Quan sát cô sửa sai].", "phanloai": "Mở rộng", "hoclieu": "Bộ ảnh chụp bổ sung góc nghiêng, biểu đồ so sánh kết quả", "ma_yccd": ""},
    {"tiet": 31, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 31: Lập trình phản hồi điều khiển trò chơi Scratch", "noidung": "Kết nối mô hình cử chỉ tay đã huấn luyện với dự án Scratch mẫu; lập trình khối lệnh phản hồi logic: 'Nếu nhận diện Nắm tay $\rightarrow$ Mèo Scratch nhảy lên' (lập trình phản hồi thông minh, không gán nhầm KN39). [KN 40: Mức 2 - Thực hành khối lệnh].", "phanloai": "Mở rộng", "hoclieu": "Dự án mẫu Scratch AI extension kết nối Teachable Machine", "ma_yccd": ""},
    {"tiet": 32, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 32: Báo cáo kỹ thuật: Bài học về tính trung thực và trách nhiệm", "noidung": "Mỗi học sinh trong nhóm tự giải thích phần việc mình làm (chụp ảnh, làm sạch, thử nghiệm); chỉ ra lỗi máy nhầm và cách nhóm khắc phục; cam kết trách nhiệm về dữ liệu. [KN 15: Mức 2], [KN 46: Mức 2 - Trách nhiệm giải trình].", "phanloai": "Mở rộng", "hoclieu": "Phiếu tổng kết kỹ thuật dự án nhóm", "ma_yccd": ""},
    {"tiet": 33, "chude": "Tích hợp", "ten_bai": "Bài 33: Đánh giá quá trình: Đánh giá sản phẩm dự án học máy Học kỳ II", "noidung": "Các nhóm demo trực tiếp mô hình nhận diện cử chỉ tay; giáo viên đánh giá từng học sinh theo rubric: thao tác dữ liệu, kiểm thử, trung thực và làm việc nhóm. [Mục VI QĐ 2422].", "phanloai": "Đánh giá quá trình", "hoclieu": "Rubric đánh giá sản phẩm học máy Lớp 3", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 34, "chude": "Tích hợp", "ten_bai": "Bài 34: Ngày hội Triển lãm & Trình diễn Trí tuệ nhân tạo nhí Lớp 3", "noidung": "Trưng bày toàn bộ các sản phẩm mô hình học máy cử chỉ tay và cẩm nang an toàn số của khối 3; học sinh toàn trường tham quan và trải nghiệm tương tác trực tiếp.", "phanloai": "Đánh giá quá trình", "hoclieu": "Khu vực sảnh tin học, máy tính demo tương tác", "ma_yccd": ""},
    {"tiet": 35, "chude": "Tích hợp", "ten_bai": "Bài 35: Củng cố hành trang số: Tự chủ tư duy - Không ỷ lại công nghệ", "noidung": "Diễn đàn trao đổi: Chia sẻ kinh nghiệm nhận diện tin giả, bí quyết kiểm chứng thông tin học tập và thói quen sử dụng AI có trách nhiệm; trao giải dự án xuất sắc Lớp 3.", "phanloai": "Đánh giá quá trình", "hoclieu": "Giấy khen 'Công dân số thông thái Lớp 3'", "ma_yccd": ""},
    {"tiet": 36, "chude": "Tích hợp", "ten_bai": "Bài 36: Báo cáo chuyên đề cốt lõi: Em là công dân số thông thái", "noidung": "Tổng kết đánh giá chuyên đề bắt buộc theo Mục VI QĐ 2422; hoàn tất hồ sơ minh chứng học tập AI Lớp 3.", "phanloai": "Cốt lõi", "hoclieu": "Sổ theo dõi đánh giá học sinh Lớp 3", "ma_yccd": "Mục VI QĐ 2422"}
]
