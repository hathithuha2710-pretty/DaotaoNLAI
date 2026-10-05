import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

md_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(md_file, "r", encoding="utf-8") as f:
    text = f.read()

# Split into parts
header = text.split("## PHẦN VI. KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH AI - LỚP 5")[0]
rest = text.split("## PHẦN VI. KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH AI - LỚP 5")[1]
part5 = rest.split("## PHẦN VII")[0]
footer = "## PHẦN VII" + rest.split("## PHẦN VII")[1]

# Split part5 into core and full
p5_intro = part5.split("### 1. Khung Chuyên đề Giáo dục AI Bắt buộc - Lớp 5 (12 tiết Cốt lõi)")[0]
p5_core_full = part5.split("### 1. Khung Chuyên đề Giáo dục AI Bắt buộc - Lớp 5 (12 tiết Cốt lõi)")[1]

p5_core = p5_core_full.split("### 2. Kế hoạch Giáo dục Toàn diện môn AI - Lớp 5 (36 tiết/năm học)")[0]
p5_full = p5_core_full.split("### 2. Kế hoạch Giáo dục Toàn diện môn AI - Lớp 5 (36 tiết/năm học)")[1]

# -------------------------------------------------------------
# 1. Update Core Table (12 lessons) for Grade 5
# -------------------------------------------------------------
core_lines = p5_core.strip().split('\n')
new_core_lines = []

for line in core_lines:
    if re.match(r'\|\s*\*\*3\*\*', line):
        new_core_lines.append("| **3** | **Bài 3: Em chọn cách dùng AI phù hợp** | Học sinh tìm hiểu một số tình huống AI hỗ trợ trẻ em, người lớn và người cao tuổi; nêu được vì sao mọi người cần biết cách sử dụng AI an toàn, hiệu quả. Với tình huống học tập hoặc sinh hoạt quen thuộc, học sinh lựa chọn có dùng AI hay không và giải thích dựa trên việc cần làm, khả năng sử dụng và sự an toàn. Thực hành chọn cách dùng phù hợp: tự suy nghĩ trước, không cung cấp thông tin riêng tư, kiểm tra kết quả và dừng khi hoàn thành việc cần làm. Tích hợp [KN 43: Mức 2 - Quyết định có sử dụng AI hay không], [KN 44: Mức 2 - Dùng thiết bị đúng mục đích, biết điểm dừng]. | `Cốt lõi` | Thẻ tình huống học tập và sinh hoạt, phiếu câu hỏi gợi ý '3 câu hỏi quyết định' | **5.A3.1, 5.A3.2** |")
    elif re.match(r'\|\s*\*\*4\*\*', line):
        new_core_lines.append("| **4** | **Bài 4: AI cần phục vụ mọi người công bằng** | Học sinh quan sát tình huống một ứng dụng luyện đọc thường nhận đúng lời của một nhóm bạn nhưng hay nhận sai lời của nhóm bạn khác, dù các bạn đều đọc đúng và được thử trong điều kiện tương tự. Học sinh chỉ ra nhóm bạn đang gặp bất lợi, nêu ảnh hưởng đối với các bạn và giải thích vì sao AI cần phục vụ mọi người công bằng, không phân biệt giới tính, vùng miền hay hoàn cảnh. Nêu được một việc nên làm khi gặp kết quả có dấu hiệu không công bằng, như đề nghị kiểm tra lại hoặc nhờ giáo viên hỗ trợ. Tích hợp [KN 24: Mức 2 - Nhận ra dấu hiệu AI phục vụ chưa công bằng qua tình huống và kết quả được cung cấp]. | `Cốt lõi` | Tình huống ứng dụng luyện đọc kèm bảng so sánh kết quả nhận diện, phiếu thảo luận nhóm | **5.B1.1, 5.B1.2** |")
    elif re.match(r'\|\s*\*\*5\*\*', line):
        new_core_lines.append("| **5** | **Bài 5: Giúp AI công bằng và dễ kiểm tra hơn** | Từ tình huống ứng dụng luyện đọc chưa phục vụ các bạn công bằng, học sinh lựa chọn thêm những mẫu giọng nói còn thiếu trong bộ thẻ do giáo viên chuẩn bị; giải thích vì sao máy cần được học từ nhiều ví dụ khác nhau. Nêu một số cách giúp AI phục vụ mọi người công bằng hơn, như bổ sung ví dụ đa dạng và kiểm tra lại kết quả với các nhóm người dùng khác nhau. Qua thông tin giới thiệu ứng dụng, học sinh tìm hiểu máy sử dụng thông tin gì để đưa ra kết quả; giải thích vì sao cần biết điều này để kiểm tra khi có nghi ngờ và tránh tin hoàn toàn vào máy. Tích hợp [KN 32: Mức 2 - Nhận ra ví dụ còn thiếu và bổ sung mẫu phù hợp], [KN 26: Mức 2 - Nêu được lý do cần biết thông tin AI sử dụng và cách kiểm tra]. | `Cốt lõi` | Bộ thẻ mẫu giọng nói bổ sung, phiếu thông tin giới thiệu cách hoạt động của ứng dụng | **5.B2.1, 5.B3.1** |")
    elif re.match(r'\|\s*\*\*6\*\*', line):
        new_core_lines.append("| **6** | **Bài 6: Điều khiển bằng quy tắc Nếu… thì…** | Qua ví dụ, học sinh nêu cách dùng quy tắc 'Nếu… thì…' để tạo phản hồi trong một chương trình có sử dụng AI: nếu máy nhận ra biển cảnh báo thì nhân vật phát lời nhắc. Tích hợp [KN 40: Mức 2 - Xác định điều kiện và phản hồi tương ứng]. | `Cốt lõi` | Sơ đồ trực quan quy tắc Nếu... thì..., thẻ tình huống điều kiện - hành động | **5.C5.1** |")
    elif re.match(r'\|\s*\*\*7\*\*', line):
        new_core_lines.append("| **7** | **Bài 7: Dạy máy phân biệt đồ vật** | Học sinh mở công cụ, đặt tên hai nhóm đồ vật, đưa ảnh mẫu vào đúng nhóm, cho máy học và thử bằng một ảnh mới. Tích hợp [KN 1: Mức 2 - Thực hiện thao tác cơ bản trên giao diện], [KN 34: Mức 2 - Thực hiện trình tự dạy máy theo hướng dẫn bằng hình]. | `Cốt lõi` | Phòng máy tính, công cụ học máy trực quan (Teachable Machine), bộ ảnh mẫu đồ vật lớp học | **5.C5.2** |")
    elif re.match(r'\|\s*\*\*8\*\*', line):
        new_core_lines.append("| **8** | **Bài 8: Kiểm thử mô hình với đồ vật mới** | Học sinh đưa các đồ vật mới trước webcam; quan sát máy nhận diện đúng hay đoán nhầm; ghi nhận số lần đúng trên tổng số lượt thử và giải thích nguyên nhân đơn giản (ảnh mờ, góc chụp lạ) theo gợi ý của giáo viên. Tích hợp [KN 25: Mức 2 - Quan sát và ghi nhận kết quả thử nghiệm]. | `Cốt lõi` | Đồ vật thực tế kiểm thử, phiếu ghi kết quả đúng/sai | **5.C5.2 (Thực hành hóa)** |")
    elif re.match(r'\|\s*\*\*9\*\*', line):
        # Update KN level to Mức 2
        line = line.replace("Mức 3", "Mức 2")
        new_core_lines.append(line)
    elif re.match(r'\|\s*\*\*10\*\*', line):
        # Update KN level to Mức 2
        line = line.replace("Mức 3", "Mức 2")
        new_core_lines.append(line)
    elif re.match(r'\|\s*\*\*11\*\*', line):
        # Update KN level to Mức 2
        line = line.replace("Mức 3", "Mức 2")
        new_core_lines.append(line)
    elif re.match(r'\|\s*\*\*12\*\*', line):
        # Update KN level to Mức 2
        line = line.replace("Mức 3", "Mức 2")
        new_core_lines.append(line)
    else:
        new_core_lines.append(line)

updated_p5_core = '\n'.join(new_core_lines)

# -------------------------------------------------------------
# 2. Update Full Table (36 lessons) for Grade 5
# -------------------------------------------------------------
full_lines = p5_full.strip().split('\n')
new_full_lines = []

for line in full_lines:
    m = re.match(r'\|\s*\*\*(\d+)\*\*', line)
    tiet_num = int(m.group(1)) if m else None

    if tiet_num == 5:
        new_full_lines.append("| **5** | **Bài 5: Em chọn cách dùng AI phù hợp** | Học sinh tìm hiểu một số tình huống AI hỗ trợ trẻ em, người lớn và người cao tuổi; nêu được vì sao mọi người cần biết cách sử dụng AI an toàn, hiệu quả. Với tình huống học tập hoặc sinh hoạt quen thuộc, học sinh lựa chọn có dùng AI hay không và giải thích dựa trên việc cần làm, khả năng sử dụng và sự an toàn. Thực hành chọn cách dùng phù hợp: tự suy nghĩ trước, không cung cấp thông tin riêng tư, kiểm tra kết quả và dừng khi hoàn thành việc cần làm. Tích hợp [KN 43: Mức 2 - Quyết định có sử dụng AI hay không], [KN 44: Mức 2 - Dùng thiết bị đúng mục đích, biết điểm dừng]. | `Cốt lõi` | Thẻ tình huống học tập và sinh hoạt, phiếu câu hỏi gợi ý '3 câu hỏi quyết định' | **5.A3.1, 5.A3.2** |")
    elif tiet_num == 9:
        new_full_lines.append("| **9** | **Bài 9: AI cần phục vụ mọi người công bằng** | Học sinh quan sát tình huống một ứng dụng luyện đọc thường nhận đúng lời của một nhóm bạn nhưng hay nhận sai lời của nhóm bạn khác, dù các bạn đều đọc đúng và được thử trong điều kiện tương tự. Học sinh chỉ ra nhóm bạn đang gặp bất lợi, nêu ảnh hưởng đối với các bạn và giải thích vì sao AI cần phục vụ mọi người công bằng, không phân biệt giới tính, vùng miền hay hoàn cảnh. Nêu được một việc nên làm khi gặp kết quả có dấu hiệu không công bằng, như đề nghị kiểm tra lại hoặc nhờ giáo viên hỗ trợ. Tích hợp [KN 24: Mức 2 - Nhận ra dấu hiệu AI phục vụ chưa công bằng qua tình huống và kết quả được cung cấp]. | `Cốt lõi` | Tình huống ứng dụng luyện đọc kèm bảng so sánh kết quả nhận diện, phiếu thảo luận nhóm | **5.B1.1, 5.B1.2** |")
    elif tiet_num == 10:
        new_full_lines.append("| **10** | **Bài 10: Giúp AI công bằng và dễ kiểm tra hơn** | Từ tình huống ứng dụng luyện đọc chưa phục vụ các bạn công bằng, học sinh lựa chọn thêm những mẫu giọng nói còn thiếu trong bộ thẻ do giáo viên chuẩn bị; giải thích vì sao máy cần được học từ nhiều ví dụ khác nhau. Nêu một số cách giúp AI phục vụ mọi người công bằng hơn, như bổ sung ví dụ đa dạng và kiểm tra lại kết quả với các nhóm người dùng khác nhau. Qua thông tin giới thiệu ứng dụng, học sinh tìm hiểu máy sử dụng thông tin gì để đưa ra kết quả; giải thích vì sao cần biết điều này để kiểm tra khi có nghi ngờ và tránh tin hoàn toàn vào máy. Tích hợp [KN 32: Mức 2 - Nhận ra ví dụ còn thiếu và bổ sung mẫu phù hợp], [KN 26: Mức 2 - Nêu được lý do cần biết thông tin AI sử dụng và cách kiểm tra]. | `Cốt lõi` | Bộ thẻ mẫu giọng nói bổ sung, phiếu thông tin giới thiệu cách hoạt động của ứng dụng | **5.B2.1, 5.B3.1** |")
    elif tiet_num == 11:
        new_full_lines.append("| **11** | **Bài 11: Chọn dữ liệu đa dạng và an toàn** | Học sinh xem một bộ ảnh mẫu, phát hiện nhóm hình còn thiếu và đề xuất bổ sung. Nhận biết ảnh có tên, khuôn mặt hoặc thông tin riêng tư; lựa chọn ảnh không chứa những thông tin đó để sử dụng. Tích hợp [KN 32: Mức 2 - Chọn ví dụ đa dạng], [KN 8, KN 9: Mức 2 - Nhận biết và tránh đưa thông tin cá nhân không cần thiết vào dữ liệu]. | `Mở rộng` | Bộ ảnh mẫu học đường lẫn ảnh có thông tin riêng tư, phiếu lọc dữ liệu | **5.B2.MR1** |")
    elif tiet_num == 12:
        new_full_lines.append("| **12** | **Bài 12: AI đã nhận đúng cho mọi người chưa?** | Học sinh quan sát bảng kết quả thử nghiệm do giáo viên chuẩn bị; so sánh số lần nhận đúng, nhận sai giữa các nhóm giọng nói. Chỉ ra nhóm thường bị nhận sai và đề xuất cần kiểm tra thêm hoặc bổ sung mẫu. Tích hợp [KN 24: Mức 2 - Nhận ra dấu hiệu kết quả chưa công bằng; chưa yêu cầu tự kết luận nguyên nhân kỹ thuật]. | `Mở rộng` | Bảng thống kê kết quả thử nghiệm đa nhóm người dùng, phiếu ghi nhận xét | **** |")
    elif tiet_num == 13:
        new_full_lines.append("| **13** | **Bài 13: Điều khiển bằng quy tắc Nếu… thì…** | Qua ví dụ, học sinh nêu cách dùng quy tắc 'Nếu… thì…' để tạo phản hồi trong một chương trình có sử dụng AI: nếu máy nhận ra biển cảnh báo thì nhân vật phát lời nhắc. Tích hợp [KN 40: Mức 2 - Xác định điều kiện và phản hồi tương ứng]. | `Cốt lõi` | Sơ đồ trực quan quy tắc Nếu... thì..., thẻ tình huống điều kiện - hành động | **5.C5.1** |")
    elif tiet_num == 14:
        new_full_lines.append("| **14** | **Bài 14: Tạo lời nhắc từ kết quả AI** | Với dự án mẫu đã được giáo viên chuẩn bị, học sinh ghép khối lệnh để nhân vật đưa ra lời nhắc phù hợp với kết quả nhận diện; chạy thử và sửa phản hồi chưa đúng. Tích hợp [KN 40: Mức 2 - Thực hành quy tắc 'Nếu… thì…' theo mẫu, có hỗ trợ khi cần]. | `Mở rộng` | Dự án mẫu Scratch AI đã cài sẵn khối lệnh nhận diện, máy tính học sinh | **5.C5.MR1** |")
    elif tiet_num == 15:
        new_full_lines.append("| **15** | **Bài 15: Dạy máy phân biệt đồ vật** | Học sinh mở công cụ, đặt tên hai nhóm đồ vật, đưa ảnh mẫu vào đúng nhóm, cho máy học và thử bằng một ảnh mới. Tích hợp [KN 1: Mức 2 - Thực hiện thao tác cơ bản trên giao diện], [KN 34: Mức 2 - Thực hiện trình tự dạy máy theo hướng dẫn bằng hình]. | `Cốt lõi` | Phòng máy tính, công cụ học máy trực quan (Teachable Machine), bộ ảnh mẫu đồ vật lớp học | **5.C5.2** |")
    elif tiet_num == 16:
        new_full_lines.append("| **16** | **Bài 16: Kiểm thử mô hình với đồ vật mới** | Học sinh đưa các đồ vật mới trước webcam; quan sát máy nhận diện đúng hay đoán nhầm; ghi nhận số lần đúng trên tổng số lượt thử và giải thích nguyên nhân đơn giản (ảnh mờ, góc chụp lạ) theo gợi ý của giáo viên. Tích hợp [KN 25: Mức 2 - Quan sát và ghi nhận kết quả thử nghiệm]. | `Cốt lõi` | Đồ vật thực tế kiểm thử, phiếu ghi kết quả đúng/sai | **** |")
    elif tiet_num == 20:
        new_full_lines.append("| **20** | **Bài 20: Thử xem máy nhận đúng hay sai** | Học sinh dùng bộ ảnh mới để thử mô hình; ghi máy nhận đúng hay sai, đếm số lần nhận đúng trên tổng số lượt thử và chỉ ra trường hợp bị nhầm. Tích hợp [KN 22: Mức 2 - Kiểm tra kết quả], [KN 25: Mức 2 - Đọc và trình bày kết quả thử nghiệm bằng số liệu đơn giản]. | `Mở rộng` | Bộ ảnh thử nghiệm góc mới lạ, bảng phiếu đếm kết quả đúng/sai | **5.C5.MR3** |")
    elif tiet_num and tiet_num >= 21:
        # Tone down Mức 3 to Mức 2 in project lessons where applicable
        line = line.replace("Mức 3 - độc lập", "Mức 2 - có hướng dẫn")
        line = line.replace("Mức 3 - Thao tác độc lập", "Mức 2 - Thao tác theo mẫu")
        line = line.replace("Mức 3 - Lập trình phản hồi độc lập", "Mức 2 - Lập trình theo mẫu có hỗ trợ")
        line = line.replace("Mức 3 - Tái huấn luyện độc lập", "Mức 2 - Tái huấn luyện có hướng dẫn")
        line = line.replace("Mức 3 - Thu thập dữ liệu độc lập", "Mức 2 - Thu thập dữ liệu theo nhóm")
        new_full_lines.append(line)
    else:
        new_full_lines.append(line)

updated_p5_full = '\n'.join(new_full_lines)

# Reassemble file
new_text = header + "## PHẦN VI. KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH AI - LỚP 5" + p5_intro + "### 1. Khung Chuyên đề Giáo dục AI Bắt buộc - Lớp 5 (12 tiết Cốt lõi)\n\n" + updated_p5_core + "\n\n### 2. Kế hoạch Giáo dục Toàn diện môn AI - Lớp 5 (36 tiết/năm học)\n\n" + updated_p5_full + "\n\n" + footer

with open(md_file, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Đã cập nhật thành công các bài theo đề xuất của Hội đồng vào file Markdown!")
