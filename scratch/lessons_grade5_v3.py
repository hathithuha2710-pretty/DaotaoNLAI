# -*- coding: utf-8 -*-
"""
Dữ liệu PPCT Lớp 5 - Phiên bản v3.0 Chuẩn hóa sâu theo Ma trận 46 Kỹ năng & QĐ 2422
Đã xử lý triệt để:
- Sửa lệch mức độ: KN26 về đúng Mức 2 (Thực hành có hướng dẫn), KN5 về đúng Mức 2 (Few-shot có hướng dẫn)
- Khai thác AI hỗ trợ học tập thực tế (KN3: Mức 3), quản lý lịch sử tương tác (KN10: Mức 2)
- Tách bạch rõ: Prompt 4 thành phần (KN4), Kỹ thuật Few-shot đưa ví dụ mẫu (KN5), Tinh chỉnh đa vòng (KN6)
- Tinh giản tải lượng dự án tốt nghiệp: Tập dữ liệu 40-50 ảnh vừa sức, khử nhận dạng toàn diện (KN8, KN9), bỏ thông số epoch/loss vượt chuẩn
- Phiếu thông tin mô hình (Model Card) thực tế và Trách nhiệm giải trình (KN25, KN26, KN46: Mức 3)
- Đảm bảo 100% YCCĐ Cốt lõi (15) và Mở rộng (9) theo QĐ 2422.
"""

GRADE5_12_CORE = [
    {
        "tiet": 1,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 1: Con người làm chủ: Vai trò chủ đạo và Trách nhiệm giải trình",
        "noidung": "Học sinh trình bày rằng AI có thể thực hiện một số công việc thay con người trong điều kiện nhất định nhưng con người luôn giữ vai trò chủ đạo; nêu ví dụ cụ thể về trách nhiệm của người tạo và người sử dụng AI đối với kết quả do AI tạo ra (Accountability); thực hành giải trình lý do lựa chọn một câu trả lời do AI hỗ trợ trong bài học. Tích hợp [KN 42: Mức 3 - Thực hành độc lập], [KN 46: Mức 3 - Trách nhiệm giải trình độc lập].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Tình huống pháp lý/đạo đức thực tế về xe tự hành hoặc chẩn đoán AI, phiếu giải trình",
        "ma_yccd": "5.A1.1, 5.A1.2"
    },
    {
        "tiet": 2,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 2: AI vì tiến bộ xã hội và lợi ích cộng đồng",
        "noidung": "Học sinh giải thích mục đích chính của AI là hỗ trợ con người nâng cao năng suất, giải phóng sức lao động; trình bày AI được tạo ra nhằm phục vụ lợi ích chung của cộng đồng, bảo đảm tính nhân văn; nêu ví dụ cụ thể về việc AI mang lại lợi ích cho cộng đồng (cảnh báo sạt lở lũ quét, trợ lý ảo hỗ trợ người khiếm thị đọc báo). Tích hợp [KN 3: Mức 3 - Khai thác độc lập], [KN 17: Mức 3 - Dự án AI bao trùm].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Video phóng sự AI trong cảnh báo thiên tai và hỗ trợ cộng đồng, bản đồ rủi ro thiên tai",
        "ma_yccd": "5.A2.1, 5.A2.2, 5.A2.3"
    },
    {
        "tiet": 3,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 3: Thích ứng trong kỷ nguyên AI: Kỹ năng số và Sử dụng phù hợp",
        "noidung": "Học sinh trình bày rằng AI ngày càng phổ biến trong đời sống, con người cần có kỹ năng số thích ứng; khẳng định việc sử dụng AI phải phù hợp với nhu cầu, bối cảnh, năng lực cá nhân và tuân thủ chuẩn mực đạo đức, pháp luật; tự xây dựng thời gian biểu cân bằng giữa hoạt động số và vận động thể chất. Tích hợp [KN 43: Mức 3 - Ra quyết định có điều kiện], [KN 44: Mức 3 - Quản trị thời gian độc lập].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Khung năng lực số công dân tương lai, mẫu thời gian biểu cân bằng số A4",
        "ma_yccd": "5.A3.1, 5.A3.2"
    },
    {
        "tiet": 4,
        "chude": "Đạo đức AI",
        "ten_bai": "Bài 4: Công bằng trong trí tuệ nhân tạo: Không phân biệt đối xử",
        "noidung": "Học sinh nêu ví dụ về sự công bằng hoặc không công bằng trong kết quả do AI tạo ra (máy nhận diện giọng nam chuẩn xác hơn giọng nữ, nhận diện sai nét mặt người cao tuổi); giải thích AI cần phục vụ con người một cách công bằng, không phân biệt đối xử và không tạo ra bất bình đẳng xã hội. Tích hợp [KN 24: Mức 3 - Phát hiện thiên lệch độc lập].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Nghiên cứu tình huống về thiên lệch dữ liệu nhận diện khuôn mặt và giọng nói",
        "ma_yccd": "5.B1.1, 5.B1.2"
    },
    {
        "tiet": 5,
        "chude": "Đạo đức AI",
        "ten_bai": "Bài 5: Giải pháp chống thiên lệch dữ liệu và Tính minh bạch của AI",
        "noidung": "Học sinh nêu các giải pháp giúp AI hoạt động công bằng hơn (thu thập dữ liệu cân bằng các nhóm, đa dạng nguồn); thảo luận có hướng dẫn về lý do con người cần hiểu cách AI đưa ra quyết định (tính minh bạch và giải trình; phân biệt chiếc hộp đen với hệ thống minh bạch). Tích hợp [KN 26: Mức 2 - Thực hành có hướng dẫn], [KN 32: Mức 3 - Kiểm soát tính đa dạng].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Sơ đồ chiếc hộp đen (Black-box) vs Hộp kính minh bạch (Glass-box), bộ dữ liệu đối sánh",
        "ma_yccd": "5.B2.1, 5.B3.1"
    },
    {
        "tiet": 6,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 6: Quy tắc Nếu - Thì trong thiết kế giải pháp AI",
        "noidung": "Học sinh nêu cách sử dụng cấu trúc Nếu... Thì... trong lập trình AI đơn giản (kết hợp các điều kiện logic lồng nhau: Nếu Camera thấy Biển báo nguy hiểm VÀ Tốc độ xe > 30km/h $\rightarrow$ Thì Phát còi cảnh báo giảm tốc độ). Tích hợp [KN 40: Mức 3 - Lập trình phản hồi độc lập].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Môi trường lập trình khối Scratch AI, bảng sơ đồ logic điều kiện phức hợp",
        "ma_yccd": "5.C5.1"
    },
    {
        "tiet": 7,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 7: Trải nghiệm công cụ học máy trực quan",
        "noidung": "Học sinh vận hành độc lập giao diện Google Teachable Machine phòng máy: Khởi tạo các lớp dữ liệu (Class), nạp dữ liệu ảnh mẫu qua webcam/tải tệp, thực hiện huấn luyện mô hình (Train Model) và quan sát tiến trình huấn luyện. Tích hợp [KN 1: Mức 3 - Thao tác độc lập], [KN 34: Mức 3 - Vận hành 4 bước học máy].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Phòng thực hành tin học, webcam, trình duyệt Google Teachable Machine",
        "ma_yccd": "5.C5.2"
    },
    {
        "tiet": 8,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 8: Thực hành: Kiểm thử mô hình và Đọc chỉ số tin cậy",
        "noidung": "Học sinh thực hành đưa các mẫu vật kiểm thử mới vào trước webcam; đọc hiểu thanh chỉ số độ tin cậy thời gian thực (Confidence Bar); lập bảng đối chiếu kết quả kiểm thử trên 10 mẫu vật: ghi nhận số ca máy nhận diện đúng, ca máy phân vân (chỉ số < 70%) và phân tích nguyên nhân. Tích hợp [KN 25: Mức 3 - Đánh giá độ tin cậy độc lập].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Mẫu vật kiểm thử góc khó, bảng ghi nhận kết quả kiểm thử (Test Matrix)",
        "ma_yccd": "5.C5.2 (Thực hành hóa)"
    },
    {
        "tiet": 9,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 9: Quy trình 5 bước thiết kế hệ thống Trí tuệ nhân tạo",
        "noidung": "Học sinh mô tả ở mức độ đơn giản về 5 bước cơ bản trong quá trình thiết kế hệ thống AI: (1) Xác định bài toán thực tiễn -> (2) Thu thập và chuẩn bị dữ liệu -> (3) Huấn luyện mô hình -> (4) Kiểm thử và đánh giá -> (5) Triển khai và liên tục cải tiến. Tích hợp [KN 34: Mức 3], [KN 41: Mức 3 - Dự án thực tế].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Infographic 5 bước vòng đời hệ thống AI (AI System Lifecycle)",
        "ma_yccd": "5.D1.1"
    },
    {
        "tiet": 10,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 10: Thực hành: Chuẩn bị dữ liệu và Khử nhận dạng cá nhân",
        "noidung": "Thực hành theo nhóm: Lựa chọn bài toán nhận diện biển báo an toàn học đường; thu thập 30 ảnh mẫu sắc nét; thực hành kỹ thuật khử nhận dạng dữ liệu cá nhân (làm mờ khuôn mặt bạn bè, che biển tên học sinh) bảo đảm an toàn dữ liệu trước khi nạp vào máy. Tích hợp [KN 8: Mức 3], [KN 9: Mức 3], [KN 29: Mức 3 - Thu thập dữ liệu độc lập].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Camera điện thoại/webcam chụp mẫu, phần mềm làm mờ ảnh đơn giản",
        "ma_yccd": "5.D1.1 (Thực hành hóa)"
    },
    {
        "tiet": 11,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 11: Cải tiến hệ thống AI thông qua nâng cao chất lượng dữ liệu",
        "noidung": "Học sinh giải thích bằng ví dụ cụ thể rằng hệ thống AI có thể được cải tiến liên tục bằng cách bổ sung dữ liệu mới đa dạng góc nhìn và sửa nhãn sai; thực hành nạp bổ sung 15 ảnh góc nghiêng, bấm Train lại và chứng minh tỷ lệ đoán đúng tăng lên trong bảng kiểm thử. Tích hợp [KN 31: Mức 3 - Làm sạch dữ liệu], [KN 35: Mức 3 - Tái huấn luyện độc lập].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Tệp ảnh bổ sung góc khó, biểu đồ so sánh độ chính xác trước/sau",
        "ma_yccd": "5.D2.1"
    },
    {
        "tiet": 12,
        "chude": "Tích hợp 4 mạch",
        "ten_bai": "Bài 12: Tổng kết chuyên đề: Em làm chủ công nghệ - Sẵn sàng bước vào tương lai",
        "noidung": "Học sinh báo cáo sản phẩm dự án học máy kèm Phiếu thông tin mô hình (Model Card); khẳng định năng lực tự chủ công nghệ, trách nhiệm giải trình và chuẩn mực đạo đức số sẵn sàng bước lên cấp THCS; giáo viên đánh giá quá trình theo Mục VI QĐ 2422. Tích hợp [KN 45: Mức 3], [KN 46: Mức 3].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Phiếu Model Card dự án nhóm, hồ sơ đánh giá năng lực AI cuối cấp",
        "ma_yccd": "Mục VI QĐ 2422"
    }
]

GRADE5_36_EXPANDED = [
    {"tiet": 1, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 1: Con người làm chủ: Vai trò chủ đạo và Trách nhiệm giải trình", "noidung": "Trình bày vai trò chủ đạo của con người; nêu ví dụ trách nhiệm của người tạo và người dùng AI (Accountability); thực hành giải trình lý do chọn kết quả do AI hỗ trợ. [5.A1.1, 5.A1.2] - Tích hợp [KN 42: Mức 3], [KN 46: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Nghiên cứu tình huống pháp lý y khoa thực tế", "ma_yccd": "5.A1.1, 5.A1.2"},
    {"tiet": 2, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 2: Quyết định cuối cùng thuộc về con người: Phân tích trách nhiệm", "noidung": "Trình bày được con người chịu trách nhiệm cuối cùng về mọi quyết định và hậu quả khi sử dụng AI; không đổ lỗi cho cỗ máy; phân tích tình huống thực tế của học sinh. [5.A1.MR1] - Tích hợp [KN 46: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Phiếu phân tích trách nhiệm đạo đức số", "ma_yccd": "5.A1.MR1"},
    {"tiet": 3, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 3: AI vì tiến bộ xã hội và lợi ích cộng đồng", "noidung": "Giải thích mục đích chính của AI là hỗ trợ nâng cao năng suất, phục vụ lợi ích chung cộng đồng; nêu ví dụ cụ thể về AI mang lại lợi ích xã hội. [5.A2.1, 5.A2.2, 5.A2.3] - Tích hợp [KN 3: Mức 3], [KN 17: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Video phóng sự AI cứu hộ thiên tai và bảo vệ rừng", "ma_yccd": "5.A2.1, 5.A2.2, 5.A2.3"},
    {"tiet": 4, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 4: Trái tim con người và cỗ máy: Tình cảm và lòng trắc ẩn", "noidung": "Trình bày được rằng dù AI làm được nhiều việc thay con người, nhưng chỉ con người mới có tình cảm, lòng trắc ẩn và sự thấu cảm sâu sắc; thảo luận những điều AI không thể thay thế. [5.A2.MR1] - Tích hợp [KN 18: Mức 3 - Phân biệt cảm xúc].", "phanloai": "Mở rộng", "hoclieu": "Phiếu thảo luận: 'Điều gì làm con người luôn là duy nhất?'", "ma_yccd": "5.A2.MR1"},
    {"tiet": 5, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 5: Thích ứng trong kỷ nguyên AI: Kỹ năng số và Sử dụng phù hợp", "noidung": "Trình bày rằng AI ngày càng phổ biến, con người cần kỹ năng số thích ứng; sử dụng AI phải phù hợp nhu cầu, bối cảnh và tuân thủ đạo đức/pháp luật. [5.A3.1, 5.A3.2] - Tích hợp [KN 43: Mức 3], [KN 44: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Phiếu tự khảo sát thói quen số của học sinh", "ma_yccd": "5.A3.1, 5.A3.2"},
    {"tiet": 6, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 6: Đô thị thông minh tương lai: Ý tưởng và hành trang công dân số", "noidung": "Trình bày được ý tưởng về một số tình huống trong tương lai khi AI tham gia vào đời sống và sự chuẩn bị của bản thân; thiết kế sơ đồ ý tưởng Smart City. [5.A3.MR1] - Tích hợp [KN 36: Mức 3], [KN 37: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Mô hình Smart City 2030, giấy vẽ khổ lớn A3", "ma_yccd": "5.A3.MR1"},
    {"tiet": 7, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 7: Khai thác AI hỗ trợ học tập: Đặt câu lệnh cấu trúc 4 thành phần", "noidung": "Thực hành độc lập sử dụng AI làm 'Bạn cùng học' (AI Study Buddy): Nhập câu lệnh 4 thành phần hoàn chỉnh [Vai trò] + [Bối cảnh] + [Nhiệm vụ] + [Giới hạn đầu ra] để yêu cầu AI tạo 3 câu hỏi trắc nghiệm ôn tập Lịch sử. Tích hợp [KN 3: Mức 3], [KN 4: Mức 3 - Cấu trúc Prompting độc lập].", "phanloai": "Mở rộng", "hoclieu": "Giao diện chatbot học tập phòng máy, bảng mẫu 4 thành phần", "ma_yccd": ""},
    {"tiet": 8, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 8: Kỹ thuật câu lệnh kèm ví dụ mẫu (Few-shot) và Tinh chỉnh đa vòng", "noidung": "Thực hành có hướng dẫn: Cung cấp 1-2 khổ thơ 4 chữ mẫu vào prompt để định hướng AI sáng tác tiếp đúng vần điệu (KN5: Mức 2); thực hiện tương tác vòng 2, vòng 3 nắn chỉnh câu chữ cho đến khi đạt yêu cầu (KN6: Mức 3). Tích hợp [KN 5: Mức 2 - Few-shot có hướng dẫn], [KN 6: Mức 3 - Tinh chỉnh đa vòng].", "phanloai": "Mở rộng", "hoclieu": "Phiếu bài tập Few-shot prompt mẫu, chatbot văn học", "ma_yccd": ""},
    {"tiet": 9, "chude": "Đạo đức AI", "ten_bai": "Bài 9: Công bằng trong trí tuệ nhân tạo: Không phân biệt đối xử", "noidung": "Nêu một số ví dụ về sự công bằng hoặc không công bằng trong kết quả do AI tạo ra; giải thích AI cần phục vụ con người một cách công bằng. [5.B1.1, 5.B1.2] - Tích hợp [KN 24: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Nghiên cứu tình huống thiên lệch thuật toán nhận diện", "ma_yccd": "5.B1.1, 5.B1.2"},
    {"tiet": 10, "chude": "Đạo đức AI", "ten_bai": "Bài 10: Giải pháp chống thiên lệch dữ liệu và Tính minh bạch của AI", "noidung": "Nêu các giải pháp giúp AI hoạt động công bằng; giải thích vì sao cần hiểu cách AI đưa ra quyết định (tính minh bạch và giải trình). [5.B2.1, 5.B3.1] - Tích hợp [KN 26: Mức 2 - Thảo luận có hướng dẫn], [KN 32: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Sơ đồ chiếc hộp đen vs Hộp kính minh bạch", "ma_yccd": "5.B2.1, 5.B3.1"},
    {"tiet": 11, "chude": "Đạo đức AI", "ten_bai": "Bài 11: Xây dựng quy tắc thu thập dữ liệu công bằng và Khử nhận dạng", "noidung": "Đề xuất được một số quy tắc khi thu thập dữ liệu để có được hệ thống AI công bằng và không thiên lệch (khử nhận dạng dữ liệu cá nhân, cân bằng mẫu các nhóm). [5.B2.MR1] - Tích hợp [KN 8: Mức 3], [KN 9: Mức 3], [KN 32: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Bảng quy tắc 5 bước chuẩn hóa và ẩn danh dữ liệu", "ma_yccd": "5.B2.MR1"},
    {"tiet": 12, "chude": "Đạo đức AI", "ten_bai": "Bài 12: Kiểm toán thiên lệch dữ liệu: Bài lab 'Bias in, bias out'", "noidung": "Thực hành trên máy tính phòng máy: Thử nghiệm mô hình nhận diện giọng nói với ngữ điệu các vùng miền khác nhau; chỉ ra trường hợp mô hình nhận diện sai lệch do dữ liệu nạp vào bị thiên vị (bài lab Experience AI). [Làm giàu INT-ENRICH] - Tích hợp [KN 24: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Tệp âm thanh giọng đọc đa vùng miền phòng máy", "ma_yccd": ""},
    {"tiet": 13, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 13: Quy tắc Nếu - Thì trong thiết kế giải pháp AI", "noidung": "Nêu cách sử dụng cấu trúc Nếu... Thì... trong lập trình AI đơn giản; thiết kế cây quyết định logic xử lý tình huống thông minh. [5.C5.1] - Tích hợp [KN 40: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Sơ đồ cây quyết định phân loại rẽ nhánh", "ma_yccd": "5.C5.1"},
    {"tiet": 14, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 14: Thực hành lập trình cấu trúc Nếu - Thì trên Scratch AI", "noidung": "Thực hành sử dụng cấu trúc Nếu... Thì... trong lập trình AI đơn giản (lập trình nhân vật Scratch đưa ra quyết định khi phát hiện chướng ngại vật qua camera). [5.C5.MR1] - Tích hợp [KN 40: Mức 3 - Lập trình phản hồi độc lập].", "phanloai": "Mở rộng", "hoclieu": "Phần mềm Scratch 3.0 phòng máy tính", "ma_yccd": "5.C5.MR1"},
    {"tiet": 15, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 15: Trải nghiệm công cụ học máy trực quan", "noidung": "Thao tác độc lập trên Google Teachable Machine: Tạo lớp, nạp dữ liệu ảnh mẫu, huấn luyện mô hình. [5.C5.2] - Tích hợp [KN 1: Mức 3], [KN 34: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Trình duyệt truy cập Teachable Machine", "ma_yccd": "5.C5.2"},
    {"tiet": 16, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 16: Thực hành: Kiểm thử mô hình và Đọc chỉ số tin cậy", "noidung": "Kiểm thử mô hình với mẫu mới; đọc hiểu thanh chỉ số độ tin cậy; phân biệt chỉ số tự tin của một dự đoán với tỷ lệ đúng qua kiểm tra thực tế. [5.C5.2 (Thực hành hóa)] - Tích hợp [KN 25: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Bảng ghi chép kiểm thử thời gian thực", "ma_yccd": ""},
    {"tiet": 17, "chude": "Tích hợp", "ten_bai": "Bài 17: Đánh giá quá trình: Báo cáo hồ sơ học tập và sản phẩm Học kỳ I", "noidung": "Học sinh trình bày dự án Scratch Nếu-Thì, bảng prompt đa vòng kèm ví dụ mẫu và kết quả bài lab chống thiên lệch; giáo viên đánh giá theo Mục VI QĐ 2422.", "phanloai": "Đánh giá quá trình", "hoclieu": "Hồ sơ học tập số cá nhân trên Google Drive", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 18, "chude": "Tích hợp", "ten_bai": "Bài 18: Diễn đàn học tập: Liêm chính học thuật và Quản lý lịch sử số", "noidung": "Thực hành có hướng dẫn kiểm tra và xóa lịch sử hội thoại trên chatbot (KN10: Mức 2); thảo luận về liêm chính học thuật: tuyệt đối không dùng AI viết hộ bài văn nộp chấm điểm (KN15: Mức 3). [Mục VI QĐ 2422].", "phanloai": "Đánh giá quá trình", "hoclieu": "Giao diện quản lý lịch sử trò chuyện trình duyệt", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 19, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 19: Huấn luyện mô hình phân loại hình ảnh trên Teachable Machine", "noidung": "Huấn luyện được một mô hình phân loại đơn giản trên công cụ trải nghiệm AI trực quan (phân loại 3 loại biển báo an toàn trường học: Biển cấm, Biển chỉ dẫn, Biển cảnh báo). [5.C5.MR2] - Tích hợp [KN 34: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Bộ 45 ảnh mẫu biển báo giao thông/học đường đã chuẩn hóa", "ma_yccd": "5.C5.MR2"},
    {"tiet": 20, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 20: Kiểm thử mô hình và phân tích trường hợp đúng, sai", "noidung": "Kiểm tra được kết quả do mô hình đưa ra trên tập mẫu mới; lập bảng thống kê chỉ ra những trường hợp máy nhận diện đúng và trường hợp bị nhầm lẫn kèm nguyên nhân kỹ thuật. [5.C5.MR3] - Tích hợp [KN 22: Mức 3], [KN 25: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Bảng kiểm thử đối sánh (Confusion Table), mẫu biển báo kiểm thử", "ma_yccd": "5.C5.MR3"},
    {"tiet": 21, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 21: Quy trình 5 bước thiết kế hệ thống Trí tuệ nhân tạo", "noidung": "Mô tả ở mức độ đơn giản về 5 bước cơ bản trong quá trình thiết kế hệ thống AI: Xác định bài toán -> Chuẩn bị dữ liệu -> Huấn luyện -> Kiểm thử -> Cải tiến. [5.D1.1] - Tích hợp [KN 34: Mức 3], [KN 41: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Sơ đồ quy trình 5 bước vòng đời AI", "ma_yccd": "5.D1.1"},
    {"tiet": 22, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 22: Thực hành: Chuẩn bị dữ liệu và Khử nhận dạng cá nhân", "noidung": "Thực hành xác định bài toán nhóm; thu thập 30 ảnh mẫu; thực hành làm mờ khuôn mặt bạn bè và che biển tên học sinh trên ảnh mẫu để khử nhận dạng. [5.D1.1 (Thực hành hóa)] - Tích hợp [KN 8: Mức 3], [KN 9: Mức 3], [KN 29: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Công cụ làm mờ ảnh đơn giản, bảng kiểm tra ẩn danh", "ma_yccd": ""},
    {"tiet": 23, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 23: Thực hành thu thập dữ liệu giải quyết bài toán học đường", "noidung": "Thực hành thu thập dữ liệu nhằm huấn luyện mô hình AI giải quyết một bài toán nhỏ trong học tập hoặc trường lớp (nhận diện đồ vật an toàn trong sân trường); bảo đảm nguyên tắc đồng thuận xin phép bạn trước khi chụp. [5.D1.MR1] - Tích hợp [KN 13: Mức 3], [KN 29: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Camera điện thoại/webcam chụp thực địa", "ma_yccd": "5.D1.MR1"},
    {"tiet": 24, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 24: Cải tiến hệ thống AI thông qua nâng cao chất lượng dữ liệu", "noidung": "Giải thích bằng ví dụ rằng hệ thống AI có thể được cải tiến liên tục bằng cách bổ sung dữ liệu mới và sửa nhãn sai; chứng minh kết quả cải thiện trên bảng kiểm thử. [5.D2.1] - Tích hợp [KN 31: Mức 3], [KN 35: Mức 3].", "phanloai": "Cốt lõi", "hoclieu": "Biểu đồ theo dõi độ chính xác qua các vòng huấn luyện", "ma_yccd": "5.D2.1"},
    {"tiet": 25, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 25: Bổ sung dữ liệu đa dạng và Tái huấn luyện mô hình", "noidung": "Thực hành cải tiến hệ thống AI bằng cách bổ sung dữ liệu: chụp thêm 15 ảnh ở điều kiện ánh sáng yếu và góc nghiêng; bấm Train lại và so sánh kết quả kiểm thử. [5.D2.MR1] - Tích hợp [KN 32: Mức 3], [KN 35: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Thư mục ảnh bổ sung góc khó phòng máy", "ma_yccd": "5.D2.MR1"},
    {"tiet": 26, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 26: Thiết lập Phiếu thông tin mô hình (Model Card) tinh giản", "noidung": "Thực hành lập phiếu Model Card vừa sức cho mô hình của nhóm: (1) Mục đích mô hình; (2) Nguồn dữ liệu và số lượng ảnh; (3) Tỷ lệ đoán đúng qua kiểm thử; (4) Giới hạn nhận diện và người chịu trách nhiệm. [Làm giàu INT-ENRICH: DeepMind] - Tích hợp [KN 25: Mức 3], [KN 26: Mức 2], [KN 46: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Biểu mẫu Model Card chuẩn Experience AI tinh giản", "ma_yccd": ""},
    {"tiet": 27, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 27: Dự án AI tốt nghiệp Tiểu học: Hệ thống Trường học an toàn (Tiết 1)", "noidung": "Xác định bài toán thiết thực vừa sức: Nhận diện 3 biển báo an toàn sân trường (Cầu thang trơn trượt, Khu vực đang sửa chữa, Lối thoát hiểm); lập kế hoạch phân công nhóm. [KN 36: Mức 3], [KN 37: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Bản mô tả bài toán và mục tiêu giải pháp nhóm", "ma_yccd": ""},
    {"tiet": 28, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 28: Dự án AI tốt nghiệp Tiểu học: Hệ thống Trường học an toàn (Tiết 2)", "noidung": "Thu thập và làm sạch tập 45 ảnh mẫu (15 ảnh cho mỗi lớp); khử nhận dạng hoàn toàn nếu có hình ảnh người; xóa bỏ ảnh rung mờ. [KN 29, KN 30, KN 31: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Camera chụp mẫu, thư mục lưu trữ ảnh đã lọc sạch", "ma_yccd": ""},
    {"tiet": 29, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 29: Dự án AI tốt nghiệp Tiểu học: Hệ thống Trường học an toàn (Tiết 3)", "noidung": "Huấn luyện mô hình học máy trên Teachable Machine; tiến hành kiểm thử với 10 mẫu ảnh độc lập chưa từng dùng để huấn luyện; ghi nhận tỷ lệ đúng/sai. [KN 25: Mức 3], [KN 34: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Phòng thực hành tin học kết nối mạng", "ma_yccd": ""},
    {"tiet": 30, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 30: Dự án AI tốt nghiệp Tiểu học: Hệ thống Trường học an toàn (Tiết 4)", "noidung": "Phát hiện trường hợp máy nhầm lẫn; bổ sung 10 ảnh mẫu góc nghiêng và tái huấn luyện mô hình; kiểm tra lại để khẳng định tỷ lệ nhận diện đúng được cải thiện. [KN 22: Mức 3], [KN 35: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Mẫu vật kiểm thử góc khó, bảng so sánh kết quả cải tiến", "ma_yccd": ""},
    {"tiet": 31, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 31: Dự án AI tốt nghiệp Tiểu học: Hệ thống Trường học an toàn (Tiết 5)", "noidung": "Xuất mã nhúng mô hình; kết nối vào Scratch AI để lập trình phát thông báo hướng dẫn: 'Chú ý: Cầu thang trơn trượt, xin mời đi chậm!'; hoàn thiện giao diện ứng dụng. [KN 39: Mức 3 - Đồng sáng tạo sản phẩm số], [KN 40: Mức 3].", "phanloai": "Mở rộng", "hoclieu": "Dự án mẫu Scratch AI extension kết nối Teachable Machine", "ma_yccd": ""},
    {"tiet": 32, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 32: Hoàn thiện hồ sơ dự án và Chuẩn bị thuyết trình giải trình", "noidung": "Hoàn thiện Phiếu thông tin mô hình (Model Card); mỗi thành viên chuẩn bị phần thuyết minh giải trình về lựa chọn dữ liệu, trách nhiệm của nhóm và giới hạn hệ thống. [KN 45: Mức 3], [KN 46: Mức 3 - Trách nhiệm giải trình].", "phanloai": "Mở rộng", "hoclieu": "Bộ poster dự án và slide thuyết trình nhóm", "ma_yccd": ""},
    {"tiet": 33, "chude": "Tích hợp", "ten_bai": "Bài 33: Hội đồng đánh giá Dự án AI tốt nghiệp Tiểu học", "noidung": "Đánh giá quá trình: Các nhóm thuyết trình và demo trực tiếp sản phẩm trước Hội đồng chuyên môn nhà trường; đánh giá từng học sinh theo rubric theo Mục VI QĐ 2422.", "phanloai": "Đánh giá quá trình", "hoclieu": "Rubric đánh giá dự án STEM-AI tốt nghiệp Tiểu học", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 34, "chude": "Tích hợp", "ten_bai": "Bài 34: Ngày hội Triển lãm AI Expo Tiểu học: Sản phẩm sáng tạo vì cộng đồng", "noidung": "Triển lãm toàn trường các dự án AI trường học an toàn và các poster cẩm nang số; học sinh tự tin trình diễn và trả lời câu hỏi của các bạn khối dưới và phụ huynh.", "phanloai": "Đánh giá quá trình", "hoclieu": "Gian hàng triển lãm AI Expo trường học", "ma_yccd": ""},
    {"tiet": 35, "chude": "Tích hợp", "ten_bai": "Bài 35: Diễn đàn Hành trang số: Tự tin bước vào cấp THCS", "noidung": "Tổng kết 5 năm giáo dục AI cấp Tiểu học: Đúc kết 4 trụ cột năng lực (Con người làm chủ, Đạo đức số, Học máy trên dữ liệu, Thiết kế hệ thống); trao chứng nhận tốt nghiệp AI Tiểu học.", "phanloai": "Đánh giá quá trình", "hoclieu": "Kỷ yếu dự án AI Tiểu học, chứng nhận hoàn thành chương trình", "ma_yccd": ""},
    {"tiet": 36, "chude": "Tích hợp", "ten_bai": "Bài 36: Báo cáo chuyên đề cốt lõi: Em làm chủ công nghệ - Sẵn sàng bước vào tương lai", "noidung": "Tổng kết đánh giá chuyên đề bắt buộc theo Mục VI QĐ 2422; hoàn tất bàn giao hồ sơ minh chứng năng lực số liên thông lên cấp THCS.", "phanloai": "Cốt lõi", "hoclieu": "Hồ sơ học tập toàn cấp Tiểu học (Lớp 1 - 5)", "ma_yccd": "Mục VI QĐ 2422"}
]
