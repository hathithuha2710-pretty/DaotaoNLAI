import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

new_matrix_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(new_matrix_file, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Line 10 fix
text = text.replace(
    "Giáo trình Discovering AI (8–12 tuổi) & Foundations of AI (11–14 tuổi), bài lab 'Bias in, bias out', Model Card và vòng đời học máy.",
    "Giáo trình Discovering AI (8–12 tuổi) của Google DeepMind & Raspberry Pi Foundation, bài thực nghiệm nhận diện thiên lệch và vòng đời học máy trực quan."
)

# 2. Skill 26 fix (Model Card)
text = text.replace(
    "Experience AI Model Card",
    "Experience AI Discovering AI"
)
text = text.replace(
    "Lập thẻ thông tin mô hình (Model Card đơn giản) cho sản phẩm AI của nhóm: Ghi rõ dữ liệu học từ đâu, độ chính xác bao nhiêu, những hạn chế chưa làm được.",
    "Lập bảng ghi chép tóm tắt thông tin sản phẩm AI của nhóm: Ghi rõ dữ liệu ảnh học từ đâu, máy nhận diện đúng những gì và những trường hợp máy chưa nhận diện được."
)

# 3. Skill 34 fix (Foundations of AI & Model Card)
text = text.replace(
    "Experience AI Foundations",
    "Experience AI Discovering AI"
)
text = text.replace(
    "Tự chủ vận hành trọn vẹn quy trình Mini AI Lifecycle: Xác định vấn đề -> Lập kế hoạch dữ liệu -> Thu thập & Gán nhãn -> Huấn luyện mô hình -> Kiểm thử & Tái huấn luyện -> Đóng gói Model Card.<br>• Quản lý hồ sơ dự án AI khoa học, bài bản.",
    "Vận hành trọn vẹn 4 bước học máy trực quan: Xác định vấn đề -> Thu thập dữ liệu -> Dạy máy học -> Kiểm tra và đánh giá kết quả.<br>• Ghi lại nhật ký thử nghiệm mô hình một cách rõ ràng, ngăn nắp."
)

# 4. Skill 46 fix (phap ly)
text = text.replace(
    "máy móc không thể gánh trách nhiệm pháp lý hay đạo đức",
    "máy móc không thể chịu trách nhiệm thay cho con người"
)
text = text.replace(
    "(ví dụ: trách nhiệm pháp lý khi xe tự lái gây tai nạn, trách nhiệm của kỹ sư khi thuật toán phân biệt đối xử)",
    "(ví dụ: bác sĩ cần kiểm tra lại và chịu trách nhiệm điều chỉnh khi AI chẩn đoán bệnh, kỹ sư cần sửa lại khi máy phân biệt đối xử)"
)

with open(new_matrix_file, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.md!")
