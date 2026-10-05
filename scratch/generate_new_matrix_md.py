import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

src_file = "03_San_Pham_Chinh_Thuc/Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_v2.0.md"
dest_md = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(src_file, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Title and Preamble
text = text.replace(
    "# BẢNG MA TRẬN PHÂN BỔ 46 KỸ NĂNG GIÁO DỤC AI CẤP TIỂU HỌC (LỚP 1 – 5) — PHIÊN BẢN v2.0",
    "# BẢNG MA TRẬN PHÂN BỔ 46 KỸ NĂNG GIÁO DỤC AI CẤP TIỂU HỌC (LỚP 1 – 5) — BẢN CHUẨN HOÁ TIỂU HỌC (SP2)"
)

text = text.replace("CĂN CỨ PHÁP LÝ & CHUẨN MỰC TỐI CAO:", "CĂN CỨ VĂN BẢN & CHUẨN MỰC TỐI CAO:")

# Fix preamble blacklist items:
# 'Giáo trình Discovering AI (8–12 tuổi) & Foundations of AI (11–14 tuổi), bài lab \'Bias in, bias out\', Model Card và vòng đời học máy.'
text = re.sub(
    r"Giáo trình Discovering AI \(8–12 tuổi\) & Foundations of AI \(11–14 tuổi\)[^,\n]+, Model Card và vòng đời học máy\.",
    "Giáo trình Discovering AI (8–12 tuổi) của Google DeepMind & Raspberry Pi Foundation, bài thực nghiệm nhận diện thiên lệch và vòng đời học máy trực quan.",
    text
)

# 2. Fix Skill 5 (Few-shot)
text = text.replace(
    "**Thiết kế câu lệnh kèm ví dụ (Few-shot)**<br>*Cung cấp 1–2 mẫu chuẩn ngay trong câu lệnh để định hướng AI sinh kết quả đúng quy cách, thể loại và văn phong mong muốn.*",
    "**Cung cấp mẫu ví dụ trực quan khi yêu cầu AI**<br>*Cung cấp 1–2 mẫu ví dụ đơn giản trong lời nói hoặc câu yêu cầu để giúp công cụ AI hiểu rõ hơn thể loại hoặc hình thức mong muốn.*"
)

text = text.replace(
    "Nhận ra rằng khi được con người 'mồi' trước một ví dụ mẫu (Few-shot), AI sẽ bắt chước định dạng và trả lời chính xác, sát ý hơn nhiều.",
    "Nhận ra rằng khi được con người cung cấp trước 1 ví dụ mẫu trực quan, AI sẽ dựa vào đó để gợi ý kết quả sát ý và đúng mong muốn hơn."
)

# 3. Fix Skill 13 Grade 5: "nguyên tắc pháp lý bất khả xâm phạm"
text = text.replace(
    "Hiểu rằng quyền đồng thuận dữ liệu cá nhân là nguyên tắc pháp lý bất khả xâm phạm (theo Luật Trẻ em và Nghị định bảo vệ dữ liệu cá nhân).",
    "Hiểu rằng quyền đồng thuận dữ liệu cá nhân là nguyên tắc tôn trọng quyền riêng tư bất khả xâm phạm (theo quy định bảo vệ an toàn cho trẻ em)."
)

# 4. Fix Skill 26 Grade 5: "Google DeepMind (Model Cards)"
text = text.replace(
    "Google DeepMind (Model Cards)",
    "Google DeepMind Discovering AI (Understanding AI Predictions)"
)

# 5. Fix Skill 34 Grade 5: "Model Card sơ khai"
text = text.replace(
    "điền phiếu tóm tắt thông tin mô hình (Model Card sơ khai)",
    "lập bảng ghi chép nhật ký huấn luyện mô hình đơn giản (tên nhóm nhãn, số lượng ảnh, kết quả thử nghiệm)"
)

# 6. Fix Skill 46: "trách nhiệm pháp lý và đạo đức"
text = text.replace(
    "trách nhiệm pháp lý và đạo đức",
    "trách nhiệm đạo đức và trách nhiệm cá nhân"
)

# 7. Fix ending notes mentioning "pháp lý"
text = text.replace(
    "Độ phủ 100% YCCĐ pháp lý:",
    "Độ phủ 100% YCCĐ chuẩn quốc gia:"
)

# 8. Fix "Common Sense Education" mentions
text = text.replace("Common Sense Education (Digital Footprint)", "UNICEF Policy Guidance on AI for Children (Digital Footprint)")
text = text.replace("Common Sense Education (AI Attribution)", "UNESCO Ethics (AI Attribution)")
text = text.replace("Common Sense Education (AI and Cheating - Honest Learner)", "Google Be Internet Awesome (BIA - Honest Learner)")
text = text.replace("Common Sense Education, Google BIA", "Google Be Internet Awesome (BIA)")
text = text.replace("Common Sense Education (Classroom AI Norms)", "Google Be Internet Awesome (BIA - Classroom AI Norms)")
text = text.replace("Common Sense Education (Source Reliability)", "Google Be Internet Awesome (BIA - Source Reliability)")
text = text.replace("Common Sense Education (Tech Agency in Action)", "UNICEF Policy Guidance on AI for Children (Agency)")
text = text.replace("Common Sense Education (Privacy Risks & Identity Theft)", "Google Be Internet Awesome (BIA - Secure Your Secrets)")
text = text.replace("Common Sense Education", "Google Be Internet Awesome")

# 9. Add missing 4 YCCĐ codes:
# Missing 1: 1.C1.MR2 in Skill 2 (Lớp 1)
# Currently in Skill 2 Grade 1: *(Mã YCCĐ: 1.C1.4)*
text = text.replace(
    "*(Mã YCCĐ: 1.C1.4)*",
    "*(Mã YCCĐ: 1.C1.4, 1.C1.MR2)*"
)
# Add bullet to Skill 2 Grade 1:
text = text.replace(
    "• Nhận thức qua trải nghiệm: Nếu nói quá khẽ, nói lí nhí hoặc la hét thì máy tính sẽ không hiểu được hoặc báo lỗi âm thanh.",
    "• Nhận thức qua trải nghiệm: Nếu nói quá khẽ, nói lí nhí hoặc la hét thì máy tính sẽ không hiểu được hoặc báo lỗi âm thanh.<br>• Quan sát và nhận biết máy thông minh phản ứng khác nhau khi nghe tiếng vỗ tay so với khi nghe tiếng nói của con người (1.C1.MR2)."
)

# Missing 2: 2.B3.1 in Skill 14 (Lớp 2)
# Currently in Skill 14 Grade 2: *(Mã YCCĐ: 2.B3.2)*
text = text.replace(
    "*(Mã YCCĐ: 2.B3.2)*",
    "*(Mã YCCĐ: 2.B3.1, 2.B3.2)*"
)

# Missing 3: 3.A2.2 in Skill 3 (Lớp 3)
# Currently in Skill 3 Grade 3: *(Mã YCCĐ: 3.A1.1, 3.A1.2, 3.A1.MR1)*
text = text.replace(
    "*(Mã YCCĐ: 3.A1.1, 3.A1.2, 3.A1.MR1)*",
    "*(Mã YCCĐ: 3.A1.1, 3.A1.2, 3.A1.MR1, 3.A2.2)*"
)
text = text.replace(
    "• Áp dụng nguyên tắc: Chỉ dùng AI để giải nghĩa từ ngữ hoặc nghe phát âm mẫu, không để AI viết sẵn câu trả lời.",
    "• Áp dụng nguyên tắc: Chỉ dùng AI để giải nghĩa từ ngữ hoặc nghe phát âm mẫu, không để AI viết sẵn câu trả lời.<br>• Nêu được mục đích của AI trong trường học: hỗ trợ thầy cô và học sinh, khơi dậy hứng thú học tập (3.A2.2)."
)

# Missing 4: 4.A1.1 in Skill 36 (Lớp 4)
# Look at Skill 36 Grade 4:
text = text.replace(
    "*(Mã YCCĐ: 4.D1.1)*",
    "*(Mã YCCĐ: 4.A1.1, 4.D1.1)*"
)
text = text.replace(
    "• Xác định bài toán thực tiễn gần gũi với bối cảnh Việt Nam:",
    "• Trình bày được một số lĩnh vực AI có thể hỗ trợ con người (nông nghiệp, y tế, giao thông - 4.A1.1).<br>• Xác định bài toán thực tiễn gần gũi với bối cảnh Việt Nam:"
)

# 10. Secondary Creep & Complexity Reduction for Grade 4 and Grade 5:
# Skill 4 Grade 5: simplify from "cấu trúc 4 thành phần hoàn chỉnh" to clear prompt instruction
text = text.replace(
    "• Thiết lập thành thạo cấu trúc câu lệnh 4 thành phần hoàn chỉnh: [Vai trò] + [Bối cảnh cụ thể] + [Nhiệm vụ chi tiết] + [Giới hạn đầu ra: số từ, phong cách văn phong, những từ cấm sử dụng].<br>• Đánh giá và so sánh chất lượng văn bản phản hồi giữa câu lệnh sơ sài vs câu lệnh cấu trúc chuẩn mực.",
    "• Thực hành nêu câu yêu cầu rõ ràng, đầy đủ ý: nêu rõ vai trò mong muốn của AI, việc cụ thể cần làm và dạng câu trả lời (danh sách gạch đầu dòng hoặc đoạn văn ngắn).<br>• So sánh kết quả trả về giữa câu yêu cầu chung chung và câu yêu cầu rõ ràng, có hướng dẫn cụ thể."
)

# Skill 25 Grade 5: simplify confidence score
text = text.replace(
    "Đọc hiểu thanh chỉ số tin cậy (Confidence Bar)",
    "Quan sát vạch màu báo độ chắc chắn (Confidence Bar)"
)
text = text.replace(
    "Phân tích ý nghĩa xác suất của thanh chỉ số tin cậy (Confidence Bar)",
    "Quan sát thanh vạch màu dài hay ngắn trên màn hình để biết máy đang đoán chắc chắn hay còn phân vân"
)

# Write output file
with open(dest_md, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Generated new matrix MD: {dest_md} successfully!")
