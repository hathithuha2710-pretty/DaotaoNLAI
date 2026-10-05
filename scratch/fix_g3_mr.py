with open('scratch/rewrite_grades_1_2_3_pedagogical.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_t15_16 = """| **15** | **Bài 15: Phục vụ công bằng, không phân biệt đối xử** | Thảo luận câu chuyện: Phần mềm cần giúp đỡ công bằng tất cả các bạn học sinh trong lớp, không thiên vị hay bỏ quên bạn nào. [3.B3.MR1] - Tích hợp [KN 24: Mức 2]. | `Mở rộng` | Tranh truyện tình bạn lớp học | **3.B3.MR1** |
| **16** | **Bài 16: Làm quen với cách gõ câu hỏi rõ ràng trên máy** | Thực hành gõ câu hỏi ngắn gọn, rõ nghĩa trên phần mềm học tập: Nêu rõ từ muốn tra cứu hoặc bài học cần hỏi. [3.A2.MR1] - Tích hợp [KN 4: Mức 2]. | `Mở rộng` | Phần mềm tra từ điển học tập trực quan | **3.A2.MR1** |"""

new_t15_16 = """| **15** | **Bài 15: Phục vụ công bằng, không phân biệt đối xử** | Thảo luận câu chuyện: Phần mềm cần giúp đỡ công bằng tất cả các bạn học sinh trong lớp, không thiên vị; nêu mục tiêu máy tính hỗ trợ mọi người dạy và học bình đẳng, dễ dàng hơn. [3.B3.MR1, 3.A2.MR3] - Tích hợp [KN 17: Mức 2], [KN 24: Mức 2]. | `Mở rộng` | Tranh truyện tình bạn lớp học | **3.B3.MR1, 3.A2.MR3** |
| **16** | **Bài 16: Quy tắc dùng máy và Ngôi trường tương lai của em** | Đề xuất các nguyên tắc đúng đắn khi dùng máy tính trong học tập; tưởng tượng và kể về ngôi trường tương lai có máy tính thông minh hỗ trợ các bạn. [3.A2.MR1, 3.A2.MR2] - Tích hợp [KN 4: Mức 2], [KN 37: Mức 2]. | `Mở rộng` | Giấy vẽ, phần mềm tra từ điển học tập trực quan | **3.A2.MR1, 3.A2.MR2** |"""

if old_t15_16 in text:
    text = text.replace(old_t15_16, new_t15_16)
    with open('scratch/rewrite_grades_1_2_3_pedagogical.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("REPLACED SUCCESSFULLY IN SCRIPT!")
else:
    print("OLD TEXT NOT FOUND!")
