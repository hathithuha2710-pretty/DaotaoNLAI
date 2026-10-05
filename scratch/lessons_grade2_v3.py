# -*- coding: utf-8 -*-
"""
Dữ liệu PPCT Lớp 2 - Phiên bản v3.0 Chuẩn hóa sâu theo Ma trận 46 Kỹ năng & QĐ 2422
Đã xử lý triệt để:
- Xóa bỏ hoàn toàn nhãn KN35 (Tái huấn luyện) không thuộc phân bổ Lớp 2
- Bổ sung hành vi quan sát giáo viên tinh chỉnh câu lệnh lần hai (KN6: Mức 1)
- Bổ sung phản xạ từ chối chia sẻ dữ liệu riêng tư (KN9) và báo người lớn khi gặp sự cố (KN12)
- Phân biệt rõ quyền sở hữu, xin phép đồng thuận (KN13) và trung thực nói rõ sản phẩm có AI hỗ trợ (KN14)
- Phân biệt bài toán phân loại và bài toán dự đoán (KN33: Mức 1)
- Đảm bảo 100% YCCĐ Cốt lõi (17) và Mở rộng (12) theo QĐ 2422.
"""

GRADE2_12_CORE = [
    {
        "tiet": 1,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 1: AI quanh em trong đời sống gia đình",
        "noidung": "Học sinh trình bày tình huống AI hỗ trợ gia đình (bật đèn tự động, tra cứu thời tiết, gợi ý bài hát); chỉ đúng biểu tượng micro trên điều khiển tivi, camera giám sát nhà; phân biệt nút bấm cơ học vs nút kích hoạt chế độ nhận biết tự động của AI. Tích hợp [KN 1: Mức 1 - Quan sát/Nhận biết], [KN 19: Mức 1], [KN 27: Mức 1].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Điều khiển tivi thông minh, mô hình loa thông minh gia đình, tranh ảnh",
        "ma_yccd": "2.A1.1, 2.A2.1"
    },
    {
        "tiet": 2,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 2: AI giúp đỡ các thành viên trong gia đình",
        "noidung": "Học sinh kể tên các thành viên trong nhà mà AI có thể giúp đỡ (ông bà tra cứu tin tức, bố mẹ quản lý việc nhà, em nhỏ nghe đọc thơ); thực hiện trò chơi ghép nối thành viên gia đình với thiết bị AI phù hợp. Tích hợp [KN 3: Mức 1 - Quan sát/Cảm thụ], [KN 36: Mức 1 - Nhận diện việc gia đình].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Tranh gia đình sum vầy cùng thiết bị thông minh, thẻ ghép nối A3",
        "ma_yccd": "2.A2.2"
    },
    {
        "tiet": 3,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 3: Con người thông thái giám sát máy thông minh",
        "noidung": "Học sinh quan sát video robot hút bụi bị kẹt chân ghế; nêu ví dụ con người cần giám sát và hỗ trợ máy; thể hiện thái độ đúng đắn: biết ơn người chế tạo, giữ gìn thiết bị cẩn thận, không đập phá hay la hét khi máy báo lỗi. Tích hợp [KN 7: Mức 1], [KN 45: Mức 1 - Nhận biết], [KN 46: Mức 1].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Video robot hút bụi gặp vật cản báo lỗi, thẻ tình huống ứng xử",
        "ma_yccd": "2.A1.3, 2.A1.4"
    },
    {
        "tiet": 4,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 4: Khi nào em không nên dùng AI? An toàn và tự chủ",
        "noidung": "Học sinh phân loại các tình huống: (1) Tự suy nghĩ làm tính đố $\rightarrow$ Không dùng AI; (2) Thiết bị hỏi thông tin nhạy cảm $\rightarrow$ Tuyệt đối từ chối và báo bố mẹ; (3) Chưa có sự cho phép của người lớn $\rightarrow$ Không tự ý bật máy. Tích hợp [KN 8: Mức 1], [KN 9: Mức 1], [KN 42: Mức 1], [KN 43: Mức 1].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Phiếu phân loại tình huống Nên / Cần thận trọng / Không nên dùng AI",
        "ma_yccd": "2.A1.2"
    },
    {
        "tiet": 5,
        "chude": "Tư duy lấy con người làm trung tâm",
        "ten_bai": "Bài 5: Trò chuyện cùng AI và câu chuyện dữ liệu",
        "noidung": "Học sinh nhận biết mỗi câu hỏi, mỗi mệnh lệnh em nói vào máy là đang cung cấp thêm thông tin cho hệ thống; giải thích 'dữ liệu' là những ví dụ cụ thể (hình ảnh, âm thanh, chữ viết) mà con người đưa vào để AI học tập. Tích hợp [KN 2: Mức 1 - Thực hành tập thể], [KN 28: Mức 1 - Nhận biết vai trò dữ liệu].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Mô hình hộp dữ liệu nạp thẻ, micro lớp học kết nối máy tính",
        "ma_yccd": "2.A3.1, 2.C1.1"
    },
    {
        "tiet": 6,
        "chude": "Đạo đức AI",
        "ten_bai": "Bài 6: Của em và của bạn: Tôn trọng quyền sở hữu sản phẩm",
        "noidung": "Học sinh kể tên những thứ thuộc về riêng em (bài vẽ, tài khoản, ảnh chụp cá nhân) và của bạn khác; nêu ví dụ quyền sở hữu đối với sản phẩm trí tuệ; hình thành ý thức: muốn sử dụng bài hoặc tranh của bạn thì phải hỏi và được bạn đồng ý. Tích hợp [KN 13: Mức 1 - Xin phép], [KN 14: Mức 1 - Nhận biết quyền sở hữu].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bức tranh vẽ của bạn học, thẻ tên tác giả nhí, tem quyền sở hữu",
        "ma_yccd": "2.B3.1, 2.B3.2"
    },
    {
        "tiet": 7,
        "chude": "Đạo đức AI",
        "ten_bai": "Bài 7: Khi máy thông minh nhận nhầm: Tìm hiểu thiên lệch",
        "noidung": "Học sinh quan sát tình huống thực tế: Trợ lý ảo nhận diện rất tốt giọng nói của bố mẹ nhưng không nghe rõ giọng nói lí nhí của trẻ em; nhận biết AI đôi khi có thể thiên kiến (thiên lệch), ưu tiên nhóm quen thuộc hơn do thiếu dữ liệu đa dạng. Tích hợp [KN 22: Mức 1], [KN 24: Mức 1 - Quan sát trực quan thiên lệch].",
        "phanloai": "Cốt lõi",
        "hoclieu": "File ghi âm thử nghiệm giọng người lớn vs giọng trẻ nhỏ, tranh so sánh",
        "ma_yccd": "2.B1.1"
    },
    {
        "tiet": 8,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 8: Máy thông minh học phân loại đồ vật",
        "noidung": "Học sinh nhận biết bài toán phân loại: AI có khả năng nhận biết đặc điểm (hình dáng, màu sắc) để chia các đồ vật vào đúng các nhóm khác nhau; phân biệt với bài toán đoán việc sắp xảy ra. Tích hợp [KN 30: Mức 1 - Dán nhãn giấy], [KN 33: Mức 1 - Trò chơi chia nhóm].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bộ đồ chơi mô hình hoa quả và phương tiện giao thông, 2 khay phân loại",
        "ma_yccd": "2.C3.1"
    },
    {
        "tiet": 9,
        "chude": "Các kĩ thuật và ứng dụng AI",
        "ten_bai": "Bài 9: Vì sao máy phân loại sai?",
        "noidung": "Học sinh thực hành đưa ra các đồ vật lạ (quả khế hình sao, đồ chơi nhìn nghiêng hoặc phòng bị tối); giải thích nguyên nhân máy đoán sai: do đồ vật quá lạ, hình ảnh bị mờ hoặc âm thanh bị lẫn tiếng ồn; nhận thức cỗ máy không hoàn hảo. Tích hợp [KN 22: Mức 1 - Quan sát so sánh], [KN 23: Mức 1].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Vật thể góc nhìn lạ, đèn pin chiếu mờ, loa phát tạp âm thử nghiệm",
        "ma_yccd": "2.C3.2"
    },
    {
        "tiet": 10,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 10: Ý tưởng máy thông minh giải quyết việc nhà",
        "noidung": "Học sinh nêu một vấn đề khó khăn gần gũi ở nhà (sách vở bừa bộn, quên tắt đèn khi ngủ); vẽ tranh hoặc kể chuyện về ý tưởng chú robot thông minh giúp giải quyết vấn đề đó (giúp ai, giúp việc gì, phản hồi thế nào). Tích hợp [KN 36: Mức 1 - Nhận diện việc], [KN 37: Mức 1 - Kể chuyện theo tranh].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Giấy vẽ A4, bút màu, tranh gợi ý các tình huống việc nhà cần hỗ trợ",
        "ma_yccd": "2.D1.1, 2.D1.2"
    },
    {
        "tiet": 11,
        "chude": "Thiết kế hệ thống AI",
        "ten_bai": "Bài 11: Dữ liệu tốt giúp máy thông minh học giỏi",
        "noidung": "Học sinh giải thích vì sao cần cung cấp cho AI dữ liệu đúng, rõ nét và đủ số lượng ví dụ; đối chiếu bộ 10 thẻ ảnh quả táo chụp sắc nét ở các góc vs 1 ảnh mờ; hiểu dữ liệu tốt là chìa khóa để máy học chính xác. Tích hợp [KN 28: Mức 1], [KN 29: Mức 1 - Thu thập tranh ảnh], [KN 32: Mức 1].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bộ thẻ dữ liệu chuẩn: 10 bức ảnh sắc nét đa dạng góc nhìn",
        "ma_yccd": "2.D2.1, 2.D2.2"
    },
    {
        "tiet": 12,
        "chude": "Tích hợp 4 mạch",
        "ten_bai": "Bài 12: Tổng kết chuyên đề: Em làm chủ AI trong gia đình",
        "noidung": "Học sinh trình bày mô hình ý tưởng robot gia đình; nhắc lại nguyên tắc xin phép bố mẹ trước khi dùng máy, tôn trọng bản quyền của bạn và kiểm tra kết quả; giáo viên đánh giá quá trình theo Mục VI QĐ 2422. Tích hợp [KN 43: Mức 1], [KN 45: Mức 1], [KN 46: Mức 1].",
        "phanloai": "Cốt lõi",
        "hoclieu": "Bảng triển lãm tranh ý tưởng Lớp 2, bảng kiểm đánh giá Mục VI",
        "ma_yccd": "Mục VI QĐ 2422"
    }
]

GRADE2_36_EXPANDED = [
    {"tiet": 1, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 1: AI quanh em trong đời sống gia đình", "noidung": "Học sinh nhận diện thiết bị AI gia đình (tivi, loa, điều hòa thông minh); chỉ đúng các nút kích hoạt AI và cảm biến. [2.A1.1, 2.A2.1] - Tích hợp [KN 1: Mức 1], [KN 27: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Bộ tranh thẻ thiết bị gia đình thông minh", "ma_yccd": "2.A1.1, 2.A2.1"},
    {"tiet": 2, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 2: AI giúp đỡ các thành viên trong gia đình", "noidung": "Kể tên các thành viên trong gia đình mà AI hỗ trợ (ông bà nghe tin, bố mẹ làm việc nhà, con học tập). [2.A2.2] - Tích hợp [KN 3: Mức 1], [KN 36: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Tranh gia đình sum họp cùng thiết bị AI", "ma_yccd": "2.A2.2"},
    {"tiet": 3, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 3: Trải nghiệm thiết bị AI gia đình có hướng dẫn", "noidung": "Học sinh thực hành ra câu lệnh ngắn (3-5 từ), phát âm rõ ràng để tìm kiếm bài hát thiếu nhi dưới sự giám sát của giáo viên. [2.A2.MR1] - Tích hợp [KN 2: Mức 1 - Thực hành tập thể].", "phanloai": "Mở rộng", "hoclieu": "Loa thông minh/máy tính giáo viên demo", "ma_yccd": "2.A2.MR1"},
    {"tiet": 4, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 4: Nguyên tắc an toàn: Có sự đồng ý của bố mẹ", "noidung": "Nêu được rằng không được tự ý sử dụng thiết bị AI khi chưa có sự cho phép của người lớn; nêu mục tiêu AI giúp gia đình an toàn, gắn kết. [2.A2.MR2, 2.A2.MR3] - Tích hợp [KN 43: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Bảng quy tắc gia đình, sticker 'Xin phép trước khi dùng'", "ma_yccd": "2.A2.MR2, 2.A2.MR3"},
    {"tiet": 5, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 5: Con người thông thái giám sát máy thông minh", "noidung": "Nêu ví dụ con người giám sát AI; rèn luyện thái độ đúng đắn: tôn trọng thiết bị, không la hét, biết ơn người sáng tạo. [2.A1.3, 2.A1.4] - Tích hợp [KN 7: Mức 1], [KN 45: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Video robot hút bụi gặp sự cố, thẻ tình huống", "ma_yccd": "2.A1.3, 2.A1.4"},
    {"tiet": 6, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 6: Khi nào em không nên dùng AI? An toàn và tự chủ", "noidung": "Phân loại tình huống không nên dùng AI: tự làm bài tập, bảo vệ dữ liệu bí mật, khi chưa xin phép. [2.A1.2] - Tích hợp [KN 8: Mức 1], [KN 42: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Phiếu trắc nghiệm tranh tình huống Nên/Không nên", "ma_yccd": "2.A1.2"},
    {"tiet": 7, "chude": "Đạo đức AI", "ten_bai": "Bài 7: Phản xạ từ chối và Xử lý sự cố an toàn thông tin", "noidung": "Đóng vai xử lý tình huống: Thiết bị hỏi mật khẩu, địa chỉ phòng ngủ $\rightarrow$ Học sinh dứt khoát từ chối (KN9); Màn hình hiện video lạ $\rightarrow$ Tắt máy báo ngay bố mẹ (KN12). [Đào sâu 2.A1.2] - Tích hợp [KN 9: Mức 1], [KN 12: Mức 1 - Phản xạ tức thì].", "phanloai": "Mở rộng", "hoclieu": "Bộ thẻ tình huống giả định, kịch bản đóng vai", "ma_yccd": ""},
    {"tiet": 8, "chude": "Đạo đức AI", "ten_bai": "Bài 8: Thứ của em và thứ của bạn trên không gian số", "noidung": "Phân biệt được thứ của mình với thứ của người khác trong tình huống số (tài khoản học tập, ảnh chụp, tranh vẽ của bạn). [2.B3.MR1] - Tích hợp [KN 13: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Thẻ tranh: Ảnh của em vs Ảnh của bạn trên máy tính", "ma_yccd": "2.B3.MR1"},
    {"tiet": 9, "chude": "Đạo đức AI", "ten_bai": "Bài 9: Nguyên tắc đồng thuận: Muốn dùng phải xin phép", "noidung": "Thực hành lời nói xin phép: 'Bạn cho mình chụp bức tranh của bạn để cho máy nhận diện nhé!'; chỉ dùng khi bạn đồng ý. [2.B3.MR2] - Tích hợp [KN 13: Mức 1 - Thực hành lời nói đồng thuận].", "phanloai": "Mở rộng", "hoclieu": "Kịch bản đóng vai xin phép mượn tranh ảnh", "ma_yccd": "2.B3.MR2"},
    {"tiet": 10, "chude": "Đạo đức AI", "ten_bai": "Bài 10: Tôn trọng quyền sở hữu và Trung thực nguồn gốc", "noidung": "Nêu ví dụ quyền sở hữu tác phẩm của con người; rèn luyện đức tính trung thực: nói thật tranh nào em tự vẽ, tranh nào được AI hỗ trợ. [2.B3.1, 2.B3.2] - Tích hợp [KN 14: Mức 1], [KN 15: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Tranh vẽ có chữ ký tác giả nhí, nhãn 'Có AI hỗ trợ'", "ma_yccd": "2.B3.1, 2.B3.2"},
    {"tiet": 11, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 11: So sánh cách học của người và cách học của máy", "noidung": "So sánh ở mức cơ bản: Người học bằng cảm nhận, trải nghiệm, thầy cô dạy; AI học bằng cách quét các mẫu dữ liệu con người đưa vào. [2.C1.MR1] - Tích hợp [KN 21: Mức 1 - Nhận biết đối chiếu].", "phanloai": "Mở rộng", "hoclieu": "Bảng so sánh 2 cột Người vs Máy trực quan", "ma_yccd": "2.C1.MR1"},
    {"tiet": 12, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 12: Trò chuyện cùng AI và câu chuyện dữ liệu", "noidung": "Nhận biết mỗi lần trò chuyện/đặt câu hỏi là cung cấp thêm dữ liệu cho máy; giải thích 'dữ liệu' là những ví dụ cụ thể. [2.A3.1, 2.C1.1] - Tích hợp [KN 28: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Mô hình hộp dữ liệu, thẻ từ khóa", "ma_yccd": "2.A3.1, 2.C1.1"},
    {"tiet": 13, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 13: Quan sát cô giáo tinh chỉnh câu lệnh lần hai", "noidung": "Quan sát cô giáo nói lại câu lệnh chi tiết hơn khi trợ lý ảo nghe chưa rõ lần 1; nhận biết con người đóng vai trò chủ động nắn chỉnh câu lệnh. [Đào sâu 2.A3.1] - Tích hợp [KN 6: Mức 1 - Quan sát tinh chỉnh prompt].", "phanloai": "Mở rộng", "hoclieu": "Máy chiếu, trợ lý ảo thử nghiệm câu lệnh 2 lần", "ma_yccd": ""},
    {"tiet": 14, "chude": "Tư duy lấy con người làm trung tâm", "ten_bai": "Bài 14: Trách nhiệm con người khi cung cấp dữ liệu cho AI", "noidung": "Nêu được rằng con người có vai trò quan trọng trong việc cung cấp thông tin đúng sự thật, ngôn từ lịch sự và không ác ý cho hệ thống AI. [2.A3.MR1] - Tích hợp [KN 7: Mức 1], [KN 16: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Bảng đối chiếu câu nói lịch thiệp vs câu nói ác ý", "ma_yccd": "2.A3.MR1"},
    {"tiet": 15, "chude": "Đạo đức AI", "ten_bai": "Bài 15: Khi máy thông minh nhận nhầm: Tìm hiểu thiên lệch", "noidung": "Nhận biết AI đôi khi có thể thiên kiến (thiên lệch), đưa ra kết quả không hoàn toàn công bằng hoặc chỉ ưu tiên nhóm quen thuộc. [2.B1.1] - Tích hợp [KN 24: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Thẻ hình ví dụ máy chỉ nhận biết giọng người lớn", "ma_yccd": "2.B1.1"},
    {"tiet": 16, "chude": "Đạo đức AI", "ten_bai": "Bài 16: Những tình huống thiên lệch quanh em", "noidung": "Nêu ví dụ về tình huống thiên lệch của AI: Máy nhận diện đúng bạn đội mũ bảo hiểm nhưng không nhận diện được bạn đội nón lá. [2.B1.MR1] - Tích hợp [KN 24: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Bộ tranh tình huống máy nhận nhầm do thiếu trang phục vùng miền", "ma_yccd": "2.B1.MR1"},
    {"tiet": 17, "chude": "Đạo đức AI", "ten_bai": "Bài 17: Dữ liệu đa dạng để máy không thiên lệch", "noidung": "Giải thích được rằng nếu dữ liệu chưa đa dạng hoặc chưa công bằng thì AI sẽ đưa ra kết quả thiên lệch, thiếu chính xác cho các nhóm đối tượng khác. [2.B1.MR2] - Tích hợp [KN 32: Mức 1 - Nhận biết tính đa dạng].", "phanloai": "Mở rộng", "hoclieu": "Bộ thẻ tranh quả táo đủ màu (đỏ, xanh, vàng)", "ma_yccd": "2.B1.MR2"},
    {"tiet": 18, "chude": "Tích hợp", "ten_bai": "Bài 18: Đánh giá quá trình: Hồ sơ minh chứng học tập Học kỳ I", "noidung": "Tổng hợp phiếu học tập, kết quả đóng vai an toàn và bản vẽ thiết bị gia đình; giáo viên đánh giá sự tiến bộ theo Mục VI QĐ 2422.", "phanloai": "Đánh giá quá trình", "hoclieu": "Hồ sơ học tập cá nhân của học sinh", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 19, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 19: Máy học phân loại đồ vật", "noidung": "Nhận biết rằng AI có thể phân loại (nhận biết và chia đồ vật thành các nhóm khác nhau dựa trên hình ảnh/âm thanh). [2.C3.1] - Tích hợp [KN 30: Mức 1], [KN 33: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Hộp phân loại đồ chơi con vật và phương tiện", "ma_yccd": "2.C3.1"},
    {"tiet": 20, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 20: Phân biệt bài toán phân loại và bài toán dự đoán", "noidung": "Trò chơi so sánh trực quan: Phân loại đồ vật vào nhóm (quả ngọt vs quả chua) vs Dự đoán điều sắp xảy ra (nhìn mây đen đoán trời mưa). [Làm giàu INT-ENRICH: Experience AI] - Tích hợp [KN 33: Mức 1 - Trò chơi chia nhóm].", "phanloai": "Mở rộng", "hoclieu": "Thẻ tranh phân loại đồ vật và tranh dự báo thời tiết", "ma_yccd": ""},
    {"tiet": 21, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 21: Quan sát cô giáo thị phạm phân loại trên phần mềm trực quan", "noidung": "Quan sát được thao tác phân loại đồ vật do giáo viên thực hiện trên công cụ thông minh trực quan (Quick, Draw! hoặc Google Arts demo). [2.C3.MR1] - Tích hợp [KN 34: Mức 1], [KN 39: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Máy chiếu, ứng dụng Quick, Draw! demo", "ma_yccd": "2.C3.MR1"},
    {"tiet": 22, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 22: Vì sao máy phân loại sai?", "noidung": "Nêu được rằng AI có thể phân loại sai khi đồ vật nhìn quá lạ, hình ảnh bị mờ hoặc âm thanh bị lẫn tạp âm. [2.C3.2] - Tích hợp [KN 22: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Thẻ tranh con mèo bị che khuất mặt, ảnh thiếu sáng", "ma_yccd": "2.C3.2"},
    {"tiet": 23, "chude": "Các kĩ thuật và ứng dụng AI", "ten_bai": "Bài 23: Trò chơi: Tìm điều kiện khiến máy nhận diện nhầm", "noidung": "Thử nghiệm đưa đồ vật xoay góc 90 độ hoặc làm rung tay; học sinh ghi chép các trường hợp máy nhầm lẫn và giải thích nguyên nhân. [Đào sâu 2.C3.2] - Tích hợp [KN 22: Mức 1 - Quan sát so sánh].", "phanloai": "Mở rộng", "hoclieu": "Đồ vật mẫu xoay góc nghiêng, phiếu ghi lỗi", "ma_yccd": ""},
    {"tiet": 24, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 24: Dữ liệu tốt giúp máy thông minh học giỏi", "noidung": "Giải thích vai trò của dữ liệu; giải thích cần cung cấp dữ liệu đúng, rõ ràng và đủ số lượng ví dụ thì máy mới học tốt. [2.D2.1, 2.D2.2] - Tích hợp [KN 28: Mức 1], [KN 29: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Thẻ dữ liệu mẫu chuẩn: 10 bức ảnh sắc nét", "ma_yccd": "2.D2.1, 2.D2.2"},
    {"tiet": 25, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 25: Chọn ví dụ phù hợp để dạy máy thông minh", "noidung": "Nêu một số ví dụ phù hợp để 'dạy' AI trong tình huống cụ thể (cung cấp 5 ảnh quả táo đỏ và 5 ảnh quả chuối vàng để máy phân loại). [2.D1.MR1] - Tích hợp [KN 29: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Bộ thẻ tranh quả táo và quả chuối đa dạng", "ma_yccd": "2.D1.MR1"},
    {"tiet": 26, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 26: Thực hành thu thập dữ liệu dạy máy", "noidung": "Thực hành thu thập một số dữ liệu để 'dạy' AI trong một tình huống cụ thể (sưu tầm thẻ tranh con vật, phân chia thành 2 nhóm rõ ràng). [2.D2.MR1] - Tích hợp [KN 29: Mức 1], [KN 30: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Rổ thẻ tranh động vật nuôi và động vật hoang dã", "ma_yccd": "2.D2.MR1"},
    {"tiet": 27, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 27: Làm sạch dữ liệu: Soi kính lúp tìm ảnh lỗi", "noidung": "Học sinh dùng kính lúp nhựa kiểm tra bộ thẻ tranh, phát hiện và nhặt bỏ ảnh mờ nhòe, ảnh dán nhầm nhãn trước khi nạp vào máy. [Đào sâu 2.D2.MR1] - Tích hợp [KN 31: Mức 1 - Phát hiện ảnh lỗi].", "phanloai": "Mở rộng", "hoclieu": "Kính lúp nhựa, thùng rác dữ liệu mini", "ma_yccd": ""},
    {"tiet": 28, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 28: Ý tưởng máy thông minh giải quyết việc nhà", "noidung": "Nêu vấn đề gần gũi trong đời sống có thể giải quyết bằng máy thông minh; nêu ý tưởng máy thông minh hỗ trợ cuộc sống. [2.D1.1, 2.D1.2] - Tích hợp [KN 36: Mức 1], [KN 37: Mức 1].", "phanloai": "Cốt lõi", "hoclieu": "Tranh gợi ý các vấn đề gia đình cần hỗ trợ", "ma_yccd": "2.D1.1, 2.D1.2"},
    {"tiet": 29, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 29: Dự án Stem/Unplugged: Chế tạo Robot dọn bàn học (Tiết 1)", "noidung": "Lên ý tưởng và thiết kế vỏ robot từ bìa các-tông; tạo khay phân loại đồ dùng học tập (bút viết vs sách vở). [KN 36: Mức 1], [KN 37: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Hộp bánh quy tái chế, giấy thủ công, kéo an toàn", "ma_yccd": ""},
    {"tiet": 30, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 30: Dự án Stem/Unplugged: Chế tạo Robot dọn bàn học (Tiết 2)", "noidung": "Chuẩn bị tập 10 thẻ tranh dữ liệu mẫu (5 ảnh bút viết, 5 ảnh quyển sách); dán nhãn tên chính xác và kiểm tra tính sắc nét. [KN 29, KN 30, KN 31: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Thẻ bìa cứng, sticker nhãn màu", "ma_yccd": ""},
    {"tiet": 31, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 31: Dự án Stem/Unplugged: Thử nghiệm phân loại và Khắc phục lỗi", "noidung": "Thử nghiệm đưa mẫu mới lạ vào khay; phát hiện trường hợp hộp bút màu bị robot nhận nhầm thành sách; học sinh giải thích nguyên nhân và đề xuất bổ sung thêm ảnh mẫu đa dạng (không gán KN35). [KN 22: Mức 1], [KN 32: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Mẫu vật thử nghiệm (hộp bút, thước dây), bảng ghi lỗi", "ma_yccd": ""},
    {"tiet": 32, "chude": "Thiết kế hệ thống AI", "ten_bai": "Bài 32: Dán nhãn quy tắc an toàn và trách nhiệm người dùng", "noidung": "Học sinh xử lý một tình huống thực tế rồi chọn quy tắc tương ứng để dán lên robot: 'Xin phép bố mẹ', 'Chỉ dùng 20 phút', 'Tắt máy khi xong việc'. [KN 43, KN 44, KN 45: Mức 1].", "phanloai": "Mở rộng", "hoclieu": "Bộ sticker nội quy an toàn số Lớp 2", "ma_yccd": ""},
    {"tiet": 33, "chude": "Tích hợp", "ten_bai": "Bài 33: Đánh giá quá trình: Đánh giá kỹ năng qua dự án Robot gia đình", "noidung": "Học sinh giới thiệu mô hình robot dọn bàn học, bộ dữ liệu và quy tắc an toàn; giáo viên đánh giá theo bảng kiểm hành vi. [Mục VI QĐ 2422].", "phanloai": "Đánh giá quá trình", "hoclieu": "Bảng kiểm đánh giá kỹ năng Lớp 2", "ma_yccd": "Mục VI QĐ 2422"},
    {"tiet": 34, "chude": "Tích hợp", "ten_bai": "Bài 34: Ngày hội Triển lãm & Trình diễn Robot gia đình thông minh", "noidung": "Trưng bày toàn bộ mô hình robot gia đình của các nhóm; giao lưu thuyết minh ý tưởng, chia sẻ kinh nghiệm chọn dữ liệu sạch cho các bạn.", "phanloai": "Đánh giá quá trình", "hoclieu": "Bàn triển lãm, phiếu hoa điểm tốt bình chọn", "ma_yccd": ""},
    {"tiet": 35, "chude": "Tích hợp", "ten_bai": "Bài 35: Củng cố kỹ năng số: Tự chủ tư duy và An toàn gia đình", "noidung": "Trò chơi giải cứu dữ liệu: Ôn tập phản xạ từ chối thông tin riêng tư, nói thật nguồn gốc tác phẩm và kiểm tra lỗi của máy; trao chứng nhận hoàn thành Lớp 2.", "phanloai": "Đánh giá quá trình", "hoclieu": "Giấy chứng nhận 'Công dân AI nhí Lớp 2'", "ma_yccd": ""},
    {"tiet": 36, "chude": "Tích hợp", "ten_bai": "Bài 36: Báo cáo chuyên đề cốt lõi: Em làm chủ AI trong gia đình", "noidung": "Tổng kết đánh giá chuyên đề bắt buộc theo Mục VI QĐ 2422; hoàn tất hồ sơ minh chứng học tập Lớp 2.", "phanloai": "Cốt lõi", "hoclieu": "Sổ theo dõi đánh giá học sinh Lớp 2", "ma_yccd": "Mục VI QĐ 2422"}
]
