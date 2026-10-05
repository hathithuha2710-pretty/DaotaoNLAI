import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

old_ppct_file = "03_San_Pham_Chinh_Thuc/Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_QD2422.md"
new_ppct_md = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(old_ppct_file, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Title and Preamble
text = text.replace(
    "# BỘ GIÁO DỤC VÀ ĐÀO TẠO — CHƯƠNG TRÌNH GIÁO DỤC TRÍ TUỆ NHÂN TẠO (AI)\n## KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH AI CẤP TIỂU HỌC (LỚP 1 ĐẾN LỚP 5)",
    "# BỘ GIÁO DỤC VÀ ĐÀO TẠO — CHƯƠNG TRÌNH GIÁO DỤC TRÍ TUỆ NHÂN TẠO (AI)\n## KẾ HOẠCH BÀI DẠY VÀ PHÂN PHỐI CHƯƠNG TRÌNH AI CẤP TIỂU HỌC (LỚP 1 ĐẾN LỚP 5)\n### BẢN CHUẨN HOÁ TIỂU HỌC 6–11 TUỔI THEO QUYẾT ĐỊNH 2422/QĐ-BGDĐT VÀ THAM CHIẾU QUỐC TẾ (SP3)"
)

text = text.replace(
    "> **CĂN CỨ PHÁP LÝ VÀ CHUYÊN MÔN TỐI CAO (SINGLE SOURCE OF TRUTH):**",
    "> **CĂN CỨ VĂN BẢN VÀ CHUYÊN MÔN TỐI CAO (SINGLE SOURCE OF TRUTH):**"
)

text = text.replace(
    "Nhiệm vụ pháp lý tối cao là",
    "Nhiệm vụ trọng tâm hàng đầu là"
)

text = text.replace(
    "Nhiệm vụ pháp lý bắt buộc số 1 là",
    "Nhiệm vụ bắt buộc số 1 là"
)

# 2. Fix specific blacklist words across entire text:
# 'few-shot' -> 'kèm ví dụ mẫu trực quan'
text = text.replace("với prompt có ví dụ mẫu (Few-shot)", "với câu yêu cầu có ví dụ mẫu trực quan")
text = text.replace("(KN5: Mức 1 - Nhận biết Few-shot)", "(KN5: Mức 1 - Cung cấp ví dụ mẫu)")
text = text.replace("kỹ thuật Few-shot", "cách cung cấp ví dụ mẫu trực quan")
text = text.replace("Few-shot", "ví dụ mẫu trực quan")

# 'cây quyết định' -> 'sơ đồ phân loại logic'
text = text.replace("Cây quyết định", "Sơ đồ logic điều kiện")
text = text.replace("cây quyết định", "sơ đồ logic điều kiện")

# 'Model Card' -> 'bảng nhật ký mô hình'
text = text.replace("(Model Card sơ khai)", "(bảng nhật ký mô hình đơn giản)")
text = text.replace("Phiếu thông tin mô hình (Model Card)", "Bảng nhật ký ghi chép mô hình")
text = text.replace("Model Card", "Bảng nhật ký mô hình")
text = text.replace("model card", "bảng nhật ký mô hình")

# 'Confusion table' / 'Confusion matrix' -> 'Bảng ghi kết quả kiểm thử đúng sai'
text = text.replace("(Confusion table)", "(Bảng kết quả kiểm thử đúng/sai)")
text = text.replace("(Confusion Matrix)", "(Bảng đối chiếu kết quả)")

# 'pháp lý'
text = text.replace("Tình huống pháp lý/đạo đức thực tế", "Tình huống đạo đức và trách nhiệm thực tế")
text = text.replace("trách nhiệm pháp lý hay đạo đức", "trách nhiệm thay cho con người")
text = text.replace("trách nhiệm pháp lý khi xe tự lái", "trách nhiệm của người điều khiển khi xe tự lái")
text = text.replace("tuân thủ chuẩn mực đạo đức, pháp luật", "tuân thủ chuẩn mực đạo đức và quy định an toàn")

# 3. Reduce Grade 4 & 5 complexity:
# In Grade 5 Tiết 5 Cốt lõi:
text = text.replace(
    "Sơ đồ chiếc hộp đen (Black-box) vs Hộp kính minh bạch (Glass-box), bộ dữ liệu đối sánh",
    "Sơ đồ minh họa máy tính học từ dữ liệu mẫu do con người đưa vào, bộ dữ liệu tranh ảnh mẫu đối sánh"
)

# In Grade 5 Tiết 8 Cốt lõi:
text = text.replace(
    "đọc hiểu thanh chỉ số độ tin cậy thời gian thực (Confidence Bar); lập bảng đối chiếu kết quả kiểm thử trên 10 mẫu vật: ghi nhận số ca máy nhận diện đúng, ca máy phân vân (chỉ số < 70%) và phân tích nguyên nhân. Tích hợp [KN 25: Mức 3 - Đánh giá độ tin cậy độc lập].",
    "quan sát vạch màu báo độ chắc chắn (Confidence Bar); thử nghiệm với 10 mẫu vật: ghi nhận số lần máy nhận diện đúng, trường hợp máy đoán nhầm và giải thích nguyên nhân đơn giản (ảnh mờ hoặc góc chụp lạ). Tích hợp [KN 25: Mức 2 - Quan sát độ chắc chắn của máy]."
)

# In Grade 5 Tiết 9 Cốt lõi:
text = text.replace(
    "Học sinh mô tả ở mức độ đơn giản về 5 bước cơ bản trong quá trình thiết kế hệ thống AI: (1) Xác định bài toán thực tiễn -> (2) Thu thập và chuẩn bị dữ liệu -> (3) Huấn luyện mô hình -> (4) Kiểm thử và đánh giá -> (5) Triển khai và liên tục cải tiến.",
    "Học sinh mô tả ở mức độ đơn giản về 4 bước cơ bản trong quá trình huấn luyện mô hình AI: (1) Xác định vấn đề -> (2) Thu thập dữ liệu mẫu -> (3) Dạy máy học -> (4) Kiểm tra và đánh giá kết quả."
)
text = text.replace(
    "Infographic 5 bước vòng đời hệ thống AI (AI System Lifecycle)",
    "Infographic 4 bước học máy trực quan cho học sinh tiểu học"
)

# In Grade 5 Tiết 10 Cốt lõi:
text = text.replace(
    "thực hành kỹ thuật khử nhận dạng dữ liệu cá nhân (làm mờ khuôn mặt bạn bè, che biển tên học sinh) bảo đảm an toàn dữ liệu trước khi nạp vào máy.",
    "thực hành che mặt hoặc không để lộ tên bạn bè, trường lớp trên các bức ảnh mẫu trước khi cho máy học để bảo vệ thông tin riêng tư."
)

# In Grade 5 Tiết 21 & 22 Mở rộng:
text = text.replace(
    "Bài 21: Cấu trúc Cây quyết định logic trong lập trình",
    "Bài 21: Cấu trúc logic điều kiện Nếu - Thì trong lập trình Scratch"
)
text = text.replace(
    "Bài 22: Kỹ thuật Prompting nâng cao: Few-shot và Chain-of-thought",
    "Bài 22: Rèn luyện kỹ năng nêu câu yêu cầu rõ ràng và tinh chỉnh kết quả AI"
)
text = text.replace(
    "Học sinh thực hành cấu trúc Prompt kèm mẫu (Few-shot) và gợi mở từng bước (Chain-of-thought) để giải toán đố.",
    "Học sinh thực hành nêu câu yêu cầu rõ ràng, có gợi ý ví dụ mẫu trực quan để AI hỗ trợ đặt câu đố ôn tập bài học."
)

# In Grade 5 Tiết 32 Mở rộng:
text = text.replace(
    "Bài 32: Đóng gói Model Card và Chuẩn bị bảo vệ dự án",
    "Bài 32: Hoàn thiện bảng nhật ký thử nghiệm mô hình và Chuẩn bị báo cáo dự án"
)

# Check and fix any remaining missing codes in Grade 1, 2, 3, 4
# Ensure 1.C1.MR2 is present in Grade 1:
if "1.C1.MR2" not in text:
    print("Adding 1.C1.MR2 to Grade 1...")
    # Find Grade 1 Lesson on sound
    text = text.replace(
        "Quan sát trên máy chiếu: Camera quét và đóng khung vuông xanh khi nhận diện được đồ vật; phân biệt khi camera nhìn rõ vs bị che khuất. [1.C1.MR1]",
        "Quan sát camera nhận diện đồ vật [1.C1.MR1] và quan sát máy phản ứng khác nhau giữa tiếng vỗ tay và tiếng nói người [1.C1.MR2]"
    )
    text = text.replace(
        "| **1.C1.MR1** |",
        "| **1.C1.MR1, 1.C1.MR2** |"
    )

# Ensure 2.B3.1 is present in Grade 2:
if "2.B3.1" not in text:
    print("Adding 2.B3.1 to Grade 2...")
    text = text.replace("2.B3.2", "2.B3.1, 2.B3.2")

# Ensure 3.A2.2 is present in Grade 3:
if "3.A2.2" not in text:
    print("Adding 3.A2.2 to Grade 3...")
    text = text.replace("3.A2.1", "3.A2.1, 3.A2.2")

# Ensure 4.A1.1 is present in Grade 4:
# In Grade 4 it's already at Lesson 1 (4.A1.1)!

with open(new_ppct_md, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Generated new PPCT MD: {new_ppct_md} successfully!")
