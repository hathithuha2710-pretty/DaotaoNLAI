import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

input_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(input_file, "r", encoding="utf-8") as f:
    raw_text = f.read()

# Step 1: Normalize newlines and fix all broken ightarrow lines
# In raw_text, lines were broken by \r or \n followed by ightarrow$
# Let's see the pattern:
# ' $\n+ightarrow$ ' or ' $\r\n+ightarrow$ ' or similar
fixed_text = re.sub(r'\s*\$\s*[\r\n]+\s*ightarrow\$\s*', ' -> ', raw_text)
# Also fix any remaining ightarrow
fixed_text = fixed_text.replace('ightarrow$', '-> ')
fixed_text = fixed_text.replace('ightarrow', '-> ')

# Step 2: Fix specific pedagogical text across all grades as requested by the user

# Grade 1 fixes:
# Bài 4: Luyện phát âm tập thể trước, sau đó mời đại diện phát biểu; có kịch bản demo dự phòng
fixed_text = fixed_text.replace(
    "tập phát âm đồng thanh to, rõ từ khóa lệnh ('Xin chào', 'Bật đèn'); trải nghiệm máy nhận đúng khi nói rõ và báo lỗi khi la hét; rèn luyện thói quen chào hỏi và cảm ơn thiết bị lịch thiệp.",
    "luyện phát âm tập thể trước cho chuẩn câu lệnh ('Xin chào', 'Bật đèn'), sau đó mời từng đại diện học sinh nói rõ ràng vào micro máy tính của giáo viên; trải nghiệm máy nhận đúng khi phát âm rõ và phản hồi chưa đúng khi nói lí nhí hoặc ồn ào; có kịch bản giáo viên thị phạm (demo) dự phòng. Rèn luyện thói quen chào hỏi và cảm ơn lịch thiệp."
)

# Bài 5: Bỏ đèn cảm ứng, loa nhắc giờ -> Đổi thành loa thông minh, camera nhận diện khuôn mặt, robot đồ chơi thông minh
fixed_text = fixed_text.replace(
    "kể tên các thiết bị tự động quen thuộc (robot hút bụi, đèn cảm ứng, loa nhắc giờ); ghép nối thẻ đồ dùng với công dụng có ích giúp con người tiết kiệm thời gian và giữ nhà cửa sạch sẽ.",
    "kể tên và nhận biết các thiết bị có tính năng AI quen thuộc (loa thông minh nhận lệnh tiếng nói, camera nhận diện khuôn mặt điểm danh, robot hút bụi thông minh tự tránh vật cản); ghép nối thẻ thiết bị với chức năng AI cụ thể giúp ích cho con người (nhận lệnh giọng nói, nhận biết hình ảnh, hỗ trợ việc nhà)."
)
fixed_text = fixed_text.replace(
    "Bộ thẻ tranh thiết bị gia đình, bảng ghép nối công dụng A3",
    "Bộ thẻ tranh thiết bị AI gia đình (loa thông minh, camera AI, robot hút bụi), bảng ghép nối chức năng A3"
)
fixed_text = fixed_text.replace(
    "Bộ thẻ tranh thiết bị gia đình thông minh",
    "Bộ thẻ tranh thiết bị AI (loa thông minh, camera AI, robot hút bụi)"
)

# Bài 8: An toàn bí mật cá nhân và hành vi dùng AI gây hại (1.B1.1)
fixed_text = fixed_text.replace(
    "Lắc đầu nói 'Không! Chuyện này em không nói được!' khi thiết bị thông minh hỏi chuyện riêng; nhận biết không dùng máy trêu bạn. Tích hợp [KN 8: Mức 1], [KN 9: Mức 1 - Phản xạ nói Không], [KN 16: Mức 1].",
    "Lắc đầu nói 'Không! Chuyện này em không nói được!' khi thiết bị thông minh hỏi chuyện riêng; phân tích tình huống cụ thể về hành vi dùng AI gây hại (dùng loa thông minh hoặc phần mềm tạo âm thanh để trêu chọc bạn, nói lời xúc phạm hoặc dọa nạt bạn bè) và nêu rõ đó là hành vi sai trái, gây tổn thương bạn. Tích hợp [KN 8: Mức 1], [KN 9: Mức 1 - Phản xạ nói Không], [KN 16: Mức 1 - Nhận biết hành vi gây hại]."
)

# Bài 11: Bỏ nồi cơm, quạt cơ học -> Đổi thành thiết bị AI làm 1 việc vs làm nhiều việc (1.D2.1, 1.D2.2)
fixed_text = fixed_text.replace(
    "phân biệt đồ dùng đơn nhiệm (nồi cơm chỉ nấu cơm, quạt chỉ quạt mát) và thiết bị đa nhiệm (điện thoại vừa gọi điện, chụp ảnh, tính giờ); thực hành xếp thẻ tranh đồ dùng vào 2 cột trên bảng lớp.",
    "phân biệt thiết bị AI làm 1 việc chuyên biệt (cân thông minh đo và đọc chỉ số cân nặng, camera đo thân nhiệt tự động) và thiết bị AI làm nhiều việc khác nhau (điện thoại thông minh có trợ lý ảo vừa nhận lệnh nói vừa dịch ngôn ngữ, máy tính bảng tương tác AI); thực hành xếp thẻ tranh vào 2 cột trên bảng lớp."
)
fixed_text = fixed_text.replace(
    "Bảng từ 2 cột 'Làm một việc' và 'Làm nhiều việc', bộ thẻ sticker",
    "Bảng 2 cột 'Thiết bị AI làm 1 việc' và 'Thiết bị AI làm nhiều việc', bộ thẻ tranh thiết bị thông minh"
)

# Full Tiết 29, 30, 31: Mô hình robot hộp giấy Unplugged phân vai cụ thể
fixed_text = fixed_text.replace(
    "Thử đưa 1 đồ vật thật hoặc 1 tranh vẽ lạ trước camera giấy của robot; quan sát tình huống 'robot bị bối rối' khi gặp mẫu chưa từng học; học sinh giải thích vì sao máy đoán nhầm.",
    "Mô phỏng Unplugged trò chơi đóng vai robot hộp giấy: Học sinh A làm người nạp dữ liệu tranh mẫu, Học sinh B đóng vai máy tính đọc nhãn dữ liệu, Học sinh C đưa một bức tranh mới lạ chưa từng học; cả lớp quan sát tình huống 'máy bị bối rối' và cùng nhau thảo luận, giải thích đơn giản vì sao máy đoán nhầm (do máy chưa từng được học bức tranh đó trước đây)."
)

# Grade 2 fixes:
# Bài 3: 2.A1.4 Trọng tâm duy trì kiểm soát và tin tưởng hợp lý
fixed_text = fixed_text.replace(
    "nhắc lại 3 quy tắc ứng xử văn minh khi dùng AI: Không la hét vào micro, biết ơn người lập trình và giữ gìn thiết bị cẩn thận.",
    "thể hiện thái độ tin tưởng hợp lý và duy trì sự kiểm soát: Nêu rõ khi thiết bị AI đưa ra câu trả lời hoặc kết quả lạ, khó hiểu thì học sinh cần dừng lại, kiểm tra lại, hỏi ý kiến bố mẹ hoặc thầy cô, không vội vàng làm theo ngay một cách mù quáng."
)

# Bài 6: Thiên lệch dữ liệu kiểm soát điều kiện âm lượng
fixed_text = fixed_text.replace(
    "học sinh quan sát thực tế loa thông minh nghe rất rõ tiếng người lớn nhưng khó nhận diện giọng trẻ con nói lí nhí; chỉ ra nguyên nhân là do dữ liệu nạp vào máy thiếu giọng nói trẻ em; kết luận cần bổ sung giọng trẻ em để máy nhận diện công bằng hơn.",
    "học sinh quan sát tình huống thực tế hoặc tranh mô phỏng: Máy nhận diện giọng nói nói chung được huấn luyện chủ yếu bằng dữ liệu giọng người lớn, nên khi trẻ em nói cùng một mức âm lượng thì máy vẫn dễ nhận nhầm hơn; chỉ ra nguyên nhân là do thiếu dữ liệu mẫu giọng trẻ em; nhận biết máy cần được học dữ liệu đa dạng của cả trẻ em để đối xử công bằng hơn."
)

# Tiết 21: 2.C3.MR1 So sánh cách AI phân loại với cách con người phân loại
fixed_text = fixed_text.replace(
    "Trực quan hóa cách AI phân loại đồ vật: Giáo viên demo mô hình phân loại hình tròn và hình vuông trên máy tính; học sinh quan sát máy gom nhóm dựa vào các điểm ảnh đặc trưng.",
    "Học sinh trực tiếp quan sát và so sánh cách AI phân loại với cách con người phân loại: Con người phân loại dựa vào hiểu biết sâu sắc và công dụng đồ vật (bút và thước cùng là đồ dùng học tập); còn AI phân loại dựa vào hình dáng, màu sắc từ các bức ảnh mẫu đã nạp vào máy."
)

# Tiết 23: Phiếu học tập tích dấu Đúng/Sai thay vì viết giải thích dài
fixed_text = fixed_text.replace(
    "Học sinh đưa các bức ảnh con mèo ở các góc xoay khác nhau (nghiêng 90 độ, chụp từ trên xuống); ghi nhận số lần máy đoán đúng và sai; giải thích vì sao góc nhìn lạ làm máy giảm độ chính xác.",
    "Học sinh đưa các bức ảnh con mèo ở góc thẳng và góc nghiêng; sử dụng Phiếu học tập hình ảnh trực quan tích dấu Đúng/Sai vào ô và chọn nguyên nhân bằng hình vẽ sẵn có (do ảnh bị xoay nghiêng, ảnh bị bóng mờ) thay vì viết giải thích dài."
)

# Tiết 33-35: Đổi tên dự án Robot dọn bàn học -> Mô hình robot giúp phân loại đồ dùng học tập
fixed_text = fixed_text.replace(
    "Dự án sáng tạo: Mô hình Robot dọn bàn học thông minh",
    "Dự án sáng tạo: Mô hình robot giúp phân loại đồ dùng học tập"
)
fixed_text = fixed_text.replace(
    "Mô hình Robot dọn bàn học",
    "Mô hình robot giúp phân loại đồ dùng học tập"
)

# Grade 3 fixes:
# Sửa nghiêm trọng: SGK Lịch sử & Địa lí lớp 3 -> SGK Tự nhiên và Xã hội lớp 3
fixed_text = fixed_text.replace("SGK Lịch sử & Địa lí lớp 3", "SGK Tự nhiên và Xã hội lớp 3")
fixed_text = fixed_text.replace("SGK Lịch sử & Địa lý lớp 3", "SGK Tự nhiên và Xã hội lớp 3")

# Tiết 1-2: Hướng dẫn mẫu từng bước trên phòng máy
fixed_text = fixed_text.replace(
    "Học sinh khởi động trình duyệt và đăng nhập tài khoản thực hành AI học đường; làm quen giao diện hộp trò chuyện (Chatbox), nút gửi lệnh (Send) và thanh điều khiển; tuân thủ quy định phòng thực hành tin học.",
    "Học sinh làm quen phòng thực hành tin học: Giáo viên chuẩn bị sẵn giao diện và nhiệm vụ cụ thể; học sinh thực hiện theo mẫu từng bước: nhận diện hộp trò chuyện (Chatbox), nút gửi lệnh (Send); mỗi tiết tập trung vào 1 thao tác mới có sự hỗ trợ của giáo viên."
)

# Tiết 11: Kiểm chứng câu trả lời AI bằng câu trả lời mẫu có sẵn
fixed_text = fixed_text.replace(
    "Học sinh hỏi AI về một sự kiện lịch sử hoặc bài học trong SGK Tự nhiên và Xã hội lớp 3; mở SGK đối chiếu từng câu chữ trong câu trả lời của AI; phát hiện ít nhất 1 chi tiết AI trả lời chưa chính xác hoặc mơ hồ; ghi lại bài học: Luôn kiểm chứng từ SGK.",
    "Giáo viên chuẩn bị sẵn các câu trả lời mẫu của AI (trong đó có 1 câu chứa thông tin chưa chính xác về bài học trong SGK Tự nhiên và Xã hội lớp 3) kèm đoạn văn bản ngắn trong SGK; học sinh đối chiếu từng chi tiết, khoanh tròn thông tin chưa đúng và ghi nhận bài học: Luôn kiểm chứng thông tin từ SGK và hỏi thầy cô."
)

# Tiết 13 & Bài 8: Nhấn mạnh ảnh AI trông bình thường vẫn có thể là ảnh giả
fixed_text = fixed_text.replace(
    "phân biệt ảnh chụp thật từ camera máy ảnh vs tranh vẽ nhân tạo/ảnh do phần mềm AI tạo ra; nhận biết các dấu hiệu nhận diện ảnh AI (bàn tay 6 ngón, đường nét méo mó); rèn luyện thói quen không vội tin ảnh trên mạng.",
    "nhận biết ảnh do công nghệ AI tạo ra; phân biệt ảnh chụp thật từ máy ảnh vs ảnh do AI tạo ra; nhấn mạnh rằng nhiều bức ảnh do AI tạo ra trông rất sắc nét, đẹp mắt và bình thường nhưng vẫn có thể là ảnh giả, không phản ánh sự thật; rèn thói quen luôn đối chiếu nguồn tin và hỏi người lớn."
)

# Bài 11: 1 tình huống xuyên suốt, tách rõ nhận biết lỗi và giải thích
fixed_text = fixed_text.replace(
    "thực hành theo nhóm tìm nguyên nhân: (1) Do câu hỏi quá ngắn $ -> $ Đặt lại câu hỏi rõ hơn; (2) Do ảnh chụp bị ngược sáng $ -> $ Chụp lại ảnh góc sáng rõ; (3) Do dữ liệu chưa học $ -> $ Nạp thêm ảnh mẫu; thuyết minh cách khắc phục của nhóm.",
    "học sinh giải quyết 1 tình huống cụ thể xuyên suốt khi AI đưa ra kết quả chưa đúng: Tách rõ bước 1 (nhận biết kết quả chưa chính xác) và bước 2 (chọn nguyên nhân đơn giản từ gợi ý: do ảnh bị mờ hoặc câu hỏi chưa rõ ràng); thực hành sửa lại câu hỏi hoặc chụp lại ảnh rõ nét hơn dưới sự hướng dẫn của giáo viên."
)

# Tiết 24: Bổ sung rõ bài toán dự đoán (3.C5.MR2)
fixed_text = fixed_text.replace(
    "nhận biết AI có thể dựa vào các dữ liệu mẫu đã học trong quá khứ để dự đoán kết quả sắp xảy ra (dự báo thời tiết ngày mai có mưa không, dự đoán từ tiếp theo khi em đang gõ chữ).",
    "học sinh quan sát dãy số hoặc hình mẫu có quy luật (hình tròn - hình vuông lặp lại), thực hành dự đoán hình tiếp theo; sau đó quan sát cách máy tính tìm quy luật từ các dữ liệu mẫu trong quá khứ để dự đoán kết quả (dự báo thời tiết ngày mai, gợi ý từ tiếp theo khi gõ chữ). Phân biệt rõ hoạt động học sinh thực hành."
)

# Grade 4 fixes:
# Bài 6 & Tiết 6: 4.A3.1 Cân nhắc 3 câu hỏi gợi mở thay vì chia cứng cấm/dùng
fixed_text = fixed_text.replace(
    "phân loại các trường hợp: (1) Khi làm bài thi/kiểm tra $ -> $ Nghiêm cấm dùng AI; (2) Khi tìm ý tưởng làm bích báo $ -> $ Được dùng AI gợi ý nhưng phải ghi nguồn; (3) Khi bài tập yêu cầu rèn chữ viết $ -> $ Tự viết tay; giải thích lý do lựa chọn.",
    "thảo luận và cân nhắc việc sử dụng AI dựa trên mục đích, nhu cầu và an toàn theo 3 câu hỏi gợi mở: 'Có cần dùng không?', 'Có giúp ích cho việc học không?', 'Có an toàn không?'; phân tích các tình huống cụ thể (khi làm bài kiểm tra, khi tìm ý tưởng vẽ tranh, khi làm toán đố) và đưa ra quyết định phù hợp thay vì chia máy móc."
)

# Tiết 3: 4.A1.MR1 Tự suy nghĩ, hiểu bài, không chép nguyên xi
fixed_text = fixed_text.replace(
    "học sinh thực hành phân tích tình huống: Bạn Nam dùng AI giải hộ bài toán đố rồi chép nguyên xi vào vở nộp cô; học sinh thảo luận và chỉ ra: Nam đã đánh mất cơ hội rèn luyện não bộ, không tự hiểu bài và có thể bị điểm kém khi kiểm tra một mình; khẳng định em dùng AI như người trợ lý gợi ý chứ không để AI làm thay.",
    "học sinh phân tích tình huống: Bạn Nam dùng AI giải hộ bài toán đố rồi chép nguyên xi vào vở nộp cô; học sinh thảo luận và chỉ ra: Người học cần tự suy nghĩ, hiểu bài và kiểm tra lại, chỉ sử dụng AI như công cụ hỗ trợ gợi ý ý tưởng chứ không sao chép nguyên xi kết quả của máy."
)

# Tiết 10: 4.B2.MR1 Đưa về đúng chuẩn: Thực hành xử lý tình huống theo hướng dẫn
fixed_text = fixed_text.replace(
    "thực hành quy trình xử lý sự cố an toàn số độc lập: (1) Phát hiện dấu hiệu bất thường (màn hình hiện cảnh báo lạ, AI hỏi mật khẩu) -> (2) Dừng thao tác ngay lập tức, không bấm vào liên kết lạ -> (3) Báo cáo ngay cho giáo viên quản phòng máy hoặc người phụ trách kỹ thuật; lập biên bản sự cố số đơn giản.",
    "thực hành xử lý tình huống giả định đơn giản theo hướng dẫn của giáo viên: Khi gặp thông tin lạ, màn hình cảnh báo hoặc câu hỏi yêu cầu mật khẩu cá nhân -> Học sinh thực hiện ngay 3 thao tác: (1) Dừng thao tác; (2) Ghi nhớ biểu hiện trên màn hình; (3) Báo ngay cho thầy cô giáo hoặc người lớn phụ trách."
)

# Tiết 11 & Bài 10: 4.B2.2 Hậu quả lộ thông tin và dấu chân số thực tế
fixed_text = fixed_text.replace(
    "phân tích các hậu quả nghiêm trọng khi để lộ thông tin cá nhân trên môi trường AI (bị kẻ xấu mạo danh lừa đảo người thân, bị gửi tin nhắn rác, bị đánh cắp tài khoản); thực hành quy trình ứng cứu: Đổi mật khẩu ngay và báo người phụ trách.",
    "thảo luận về hậu quả khi để lộ thông tin cá nhân và nhận thức dấu chân số: 'Thông tin đã chia sẻ lên mạng có thể được người khác lưu lại hoặc sao chép, em khó có thể kiểm soát hoàn toàn việc người khác tiếp tục sử dụng nó'; thực hành cách ứng xử khi lỡ lộ thông tin: Dừng chia sẻ, báo ngay cho bố mẹ hoặc thầy cô để được hỗ trợ kịp thời."
)

# Tiết 16: Tinh gọn câu lệnh: Nhiệm vụ + kết quả mong muốn
fixed_text = fixed_text.replace(
    "Học sinh thực hành cấu trúc câu lệnh 3 thành phần: [Vai trò] + [Nhiệm vụ cụ thể] + [Định dạng đầu ra]; thực hành hội thoại đa vòng (Multi-turn prompting): Nhận kết quả lượt 1 $ -> $ Yêu cầu AI tinh chỉnh 'Ngắn hơn', 'Thêm ví dụ vui nhộn' ở lượt 2.",
    "Học sinh thực hành kỹ năng đặt câu lệnh rõ ràng: Nêu rõ việc cần làm (nhiệm vụ) và kết quả mong muốn; thực hành điều chỉnh câu lệnh 1 lần theo gợi ý cụ thể của giáo viên để câu trả lời của AI sát hơn với bài học."
)

# Dự án Thùng rác AI Lớp 4 (Bài 4, 11, 12, Tiết 24, 31, 32, 33):
fixed_text = fixed_text.replace(
    "Mô hình phân loại vỏ chai / hộp sữa -> Phát tín hiệu mở ngăn rác tương ứng",
    "Mô hình nhận diện hình ảnh vỏ chai nhựa / hộp sữa giấy trên máy tính -> Hiển thị gợi ý phân loại và phát âm thanh hướng dẫn"
)
fixed_text = fixed_text.replace(
    "Mô hình nhận diện vỏ chai nhựa -> Phát âm thanh hướng dẫn",
    "Mô hình máy tính nhận diện ảnh vỏ chai nhựa -> Hiển thị kết quả và phát âm thanh hướng dẫn"
)

# Grade 5 fixes:
# Bài 6: 5.C5.1 Scratch logic điều kiện trực quan
fixed_text = fixed_text.replace(
    "Học sinh nêu cách sử dụng cấu trúc Nếu... Thì... trong lập trình AI đơn giản (kết hợp các điều kiện logic lồng nhau: Nếu Camera thấy Biển báo nguy hiểm VÀ Tốc độ xe > 30km/h -> Thì Phát còi cảnh báo giảm tốc độ). Tích hợp [KN 40: Mức 3 - Lập trình phản hồi độc lập].",
    "Học sinh nêu cách sử dụng cấu trúc Nếu... Thì... trong lập trình AI đơn giản: Sử dụng môi trường khối lệnh Scratch 3.0 trực quan để lập trình điều kiện: 'Nếu Camera nhận diện đúng đồ dùng học tập A thì nhân vật phát âm thanh chào và hiển thị thông tin giới thiệu'. Tích hợp [KN 40: Mức 2 - Lập trình phản hồi có hướng dẫn]."
)

# Bài 9: Thống nhất 4 bước dạy máy học trực quan
fixed_text = fixed_text.replace(
    "Học sinh mô tả ở mức độ đơn giản về 4 bước cơ bản trong quá trình huấn luyện mô hình AI: (1) Xác định vấn đề -> (2) Thu thập dữ liệu mẫu -> (3) Dạy máy học -> (4) Kiểm tra và đánh giá kết quả.",
    "Học sinh mô tả ở mức độ đơn giản về 4 bước cơ bản trong quá trình dạy máy học trực quan: (1) Xác định vấn đề -> (2) Thu thập dữ liệu mẫu -> (3) Dạy máy học -> (4) Kiểm tra và đánh giá kết quả."
)

# Bài 10 & Tiết 22: Quyền riêng tư và an toàn dữ liệu
fixed_text = fixed_text.replace(
    "thực hành che mặt hoặc không để lộ tên bạn bè, trường lớp trên các bức ảnh mẫu trước khi cho máy học để bảo vệ thông tin riêng tư.",
    "hướng dẫn học sinh ưu tiên chụp riêng đồ vật, đồ dùng học tập; thực hành quy tắc an toàn: Không chụp để lộ gương mặt bạn bè, bảng tên hoặc thông tin riêng tư trên các bức ảnh mẫu trước khi cho máy học để bảo vệ quyền riêng tư."
)

# Bài 11 & Tiết 24, 30: So sánh trước sau, trung thực khoa học, không ép tăng
fixed_text = fixed_text.replace(
    "đối chiếu kết quả nhận diện trước và sau khi bổ sung dữ liệu; chứng minh tỷ lệ nhận diện đúng tăng lên rõ rệt khi dữ liệu mẫu được mở rộng.",
    "học sinh so sánh kết quả nhận diện trước và sau khi bổ sung dữ liệu: Nhận xét khách quan xem máy nhận diện tốt hơn, chưa đổi hay kém hơn; rèn luyện tính trung thực trong thực nghiệm khoa học, không ép buộc kết quả luôn phải tăng."
)

# Tiết 33-35: Báo cáo trong lớp học, bỏ hội đồng chuyên môn
fixed_text = fixed_text.replace(
    "trước hội đồng chuyên môn và giáo viên",
    "trước thầy cô giáo và các bạn trong lớp học"
)
fixed_text = fixed_text.replace(
    "Hội đồng chuyên môn",
    "Thầy cô và các bạn trong lớp"
)

# Hạ tầng và điều kiện tổ chức phòng máy:
fixed_text = fixed_text.replace(
    "Mỗi học sinh 1 máy tính kết nối Internet tốc độ cao",
    "Bố trí 2 học sinh / máy tính (hoặc nhóm 3–4 học sinh); máy tính có webcam hoặc sử dụng bộ ảnh mẫu chuẩn bị sẵn; phần mềm giao diện tiếng Việt hoặc khối lệnh trực quan; luôn có phương án bài tập Unplugged dự phòng"
)

# Write updated text back to input_file
with open(input_file, "w", encoding="utf-8") as f:
    f.write(fixed_text)

print("Đã hoàn thành Step 1 & Step 2 trong SP3 Markdown!")
