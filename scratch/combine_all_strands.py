# -*- coding: utf-8 -*-
"""
Combines all parts into the definitive master document:
03_San_Pham_Chinh_Thuc/Khung_Kien_Thuc_Va_Ky_Nang_AI_Theo_Truc_Doc_Tieu_Hoc_Lop1_5.md
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/part1_intro.txt', 'r', encoding='utf-8') as f:
    intro = f.read()

with open('scratch/strand1_2.txt', 'r', encoding='utf-8') as f:
    s12 = f.read()

with open('scratch/strand3_4.txt', 'r', encoding='utf-8') as f:
    s34 = f.read()

with open('scratch/strand5_6.txt', 'r', encoding='utf-8') as f:
    s56 = f.read()

with open('scratch/strand7_8.txt', 'r', encoding='utf-8') as f:
    s78 = f.read()

part4_conclusion = """
---

## PHẦN III. HƯỚNG DẪN ỨNG DỤNG BẢN ĐỒ TRỤC DỌC VÀO SOẠN BÀI DẠY (PPCT)

Bản đồ Kiến thức và Kỹ năng Trục dọc này là **kim chỉ nam chuyên môn tối cao** để các nhóm tác giả, chuyên gia thẩm định và giáo viên biên soạn toàn bộ 240 lượt bài học trong Bảng Phân phối chương trình (PPCT). Khi bắt tay soạn một bài học cụ thể, người soạn phải tuân thủ nghiêm ngặt **Quy trình 3 bước khớp nối**:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ BƯỚC 1: ĐỊNH VỊ BÀI HỌC TRONG PHÂN PHỐI CHƯƠNG TRÌNH                   │
│ - Mở PPCT: Tra cứu Tên bài, Số tiết, Phân loại (Core/Expanded)         │
│ - Tra cứu Mã YCCĐ bảo trợ của QĐ 2422 và Mã Kỹ năng tích hợp          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ BƯỚC 2: TRÍCH XUẤT NỘI DUNG TỪ BẢN ĐỒ TRỤC DỌC                         │
│ - Mở đúng Trục năng lực (từ Trục 1 đến Trục 8) ở đúng Khối lớp         │
│ - Lấy trọn vẹn:                                                        │
│   + Hạt nhân Kiến thức Cốt lõi (định nghĩa khoa học, ví dụ đời sống)   │
│   + Biểu hiện Kỹ năng Vi mô & Tiêu chí hoàn thành trong 35 phút        │
│   + Bộ Học liệu Chuẩn & Đáp án đối chứng thực chứng                    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ BƯỚC 3: THIẾT KẾ TIẾN TRÌNH 4 PHA KOLB TRONG 30–35 PHÚT                │
│ - Pha 1 (Khởi động - CE): Kích hoạt tình huống từ bối cảnh thực tế     │
│ - Pha 2 (Khám phá - RO): Dùng câu hỏi suy ngẫm sâu để rút ra kiến thức │
│ - Pha 3 (Luyện tập - AC): Tổ chức thực hành tạo sản phẩm theo tiêu chí │
│ - Pha 4 (Vận dụng - AE): Kiểm toán chéo nhóm hoặc xử lý tình huống mới │
└────────────────────────────────────────────────────────────────────────┘
```

---

## PHẦN IV. BẢNG KIỂM ĐỊNH CHẤT LƯỢNG QA/QC 10 TIÊU CHÍ SỐNG CÒN

Mọi bản thiết kế bài học hoặc kế hoạch bài dạy trước khi được phê duyệt ban hành bắt buộc phải tự kiểm định qua **Bộ 10 tiêu chí QA/QC**:

| STT | Tiêu chí Kiểm định QA/QC | Yêu cầu Chuẩn mực | Trạng thái Đạt |
| :---: | :--- | :--- | :---: |
| **1** | **Chuẩn xác Pháp lý (Zero-Omission)** | Neo chặt vào đúng mã YCCĐ của QĐ 2422; trích dẫn nguyên văn pháp lý, không tự sáng tác mã hoặc viết mục tiêu biến dạng. | **ĐẠT** |
| **2** | **Chính xác Công nghệ (Tech Accuracy)** | Không dạy sai cơ chế LLM; không nhân hóa máy móc sai lệch; không tuyệt đối hóa an toàn phi thực tế. | **ĐẠT** |
| **3** | **Từ vựng Chuẩn hóa (Zero-Deviation)** | Tuân thủ 100% 26 thuật ngữ Phụ lục QĐ 2422: *Câu lệnh (prompt), Ảo giác AI (hallucination), Thiên lệch (bias), Nội dung giả mạo (deepfake), Khử nhận dạng, Trách nhiệm giải trình...* | **ĐẠT** |
| **4** | **Phân rã Hành vi Vi mô (Micro-behaviors)** | Kỹ năng được viết bằng các động từ hành động đo lường được; tuyệt đối không dùng động từ tĩnh vô hình (*hiểu rằng, ý thức*). | **ĐẠT** |
| **5** | **Khả thi Thời lượng (Lesson-Scope)** | Phân định rõ đích 1 tiết với đích cả năm; nhiệm vụ thực hành hoàn thành trọn vẹn trong 30–35 phút (Lớp 1-2) hoặc 35 phút (Lớp 3-5). | **ĐẠT** |
| **6** | **Minh chứng Thực chứng (Empirical Evidence)** | Có công cụ đo lường và sản phẩm học tập cụ thể (phiếu học tập, ảnh đã crop, ma trận kiểm thử, Model Card); không đo bằng khẩu hiệu. | **ĐẠT** |
| **7** | **Đầy đủ Học liệu Chuẩn (Concrete Artifacts)** | Cung cấp đầy đủ văn bản giả lập, đoạn trích SGK, tập ảnh mẫu có sẵn lỗi và đáp án đối chứng của giáo viên. | **ĐẠT** |
| **8** | **Câu hỏi Suy ngẫm Sâu (Reflective Questions)** | Pha Khám phá (RO) có các câu hỏi kích thích tư duy để học sinh tự đúc kết kiến thức từ trải nghiệm, không nghe giảng một chiều. | **ĐẠT** |
| **9** | **Tiến trình Xoắn ốc Dọc (Vertical Spiral)** | Thể hiện rõ bậc thang nâng cao so với lớp dưới; không dẫm chân tại chỗ và không nhảy cóc độ khó. | **ĐẠT** |
| **10** | **Bình đẳng Tiếp cận (Unplugged Alternative)** | Lớp 1–2 đạt 100% Unplugged; Lớp 3–5 trên phòng máy luôn có phương án học liệu giấy dự phòng tương đương cho vùng khó khăn. | **ĐẠT** |

---
"""

full_content = intro + s12 + s34 + s56 + s78 + part4_conclusion

target_file = '03_San_Pham_Chinh_Thuc/Khung_Kien_Thuc_Va_Ky_Nang_AI_Theo_Truc_Doc_Tieu_Hoc_Lop1_5.md'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(full_content)

print(f"Master document successfully combined and overwritten to: {target_file}")
print(f"Total length of combined document: {len(full_content)} characters.")
