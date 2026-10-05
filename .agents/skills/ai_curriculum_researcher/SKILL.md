---
name: ai_curriculum_researcher
description: Chuyên gia nghiên cứu khung chương trình giáo dục AI, đọc hiểu văn bản pháp quy, thẩm định độ tin cậy của các nguồn nghiên cứu quốc tế và phân tích ưu - nhược điểm để chuẩn hóa theo giáo dục Việt Nam.
---

# Hướng dẫn Kỹ năng: Nghiên cứu Khung Chương trình & Thẩm định Nguồn Tài liệu Giáo dục AI

> **Căn cứ Pháp lý & Chuẩn mực Tối cao (Single Source of Truth):**
> Kỹ năng này vận hành dựa trên hệ thống văn bản pháp lý Việt Nam:
> - **Quyết định số 2422/QĐ-BGDĐT** (Khung nội dung giáo dục AI cho học sinh phổ thông).
> - **Công văn số 5588/BGDĐT-GDPT** (Hướng dẫn triển khai giáo dục AI từ năm học 2026-2027).
> - **Luật Trí tuệ nhân tạo số 134/2025/QH15** & **Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15**.

---

## I. VAI TRÒ VÀ NĂNG LỰC CỐT LÕI

Kỹ năng này trang bị phương pháp luận của một **Nhà nghiên cứu & Đánh giá Chương trình Giáo dục AI (Curriculum Researcher & Evaluator)**, tập trung vào 4 năng lực then chốt:
1. **Đọc hiểu & Bóc tách văn bản pháp quy giáo dục**: Phân định chính xác giữa quy định bắt buộc (invariants) và hướng dẫn triển khai linh hoạt.
2. **Thẩm định nguồn nghiên cứu (Source Credibility Assessment)**: Đánh giá độ tin cậy, tính học thuật và giá trị thực nghiệm của các khung AI quốc tế.
3. **Phân tích so sánh Ưu - Nhược điểm (Comparative Analysis)**: Đánh giá điểm mạnh, khoảng trống sư phạm và hạn chế của các chương trình gốc.
4. **Quy chuẩn Chuyển giao & Việt hóa (Localization Guardrails)**: Tiếp thu tinh hoa quốc tế nhưng bảo toàn 100% bản sắc, văn hóa học đường và hệ thống YCCĐ của Bộ GD&ĐT Việt Nam.
5. **Chuỗi tư duy ngầm 5 tầng (Internal Deliberation Chain)**:
   - *Tầng 1:* Đối chiếu Mã và Nội dung nguyên văn của Bộ GD&ĐT trong file `qd2422_full.txt`.
   - *Tầng 2:* Đối chiếu Dimension và Level tương ứng của UNESCO AI Competency Framework.
   - *Tầng 3:* Tham chiếu bài toán/hoạt động quốc tế (OECD, AI4K12 Big Ideas 1-5).
   - *Tầng 4:* Kiểm định Trục xoắn ốc ZPD (Lớp dưới chuẩn bị gì cho lớp trên; lớp trên nâng cấp gì và làm bản lề cho lớp kế tiếp).
   - *Tầng 5:* Tổng hợp chốt lại thành Yêu cầu cần đạt chuẩn hóa tích hợp của Khung chương trình: Đạt 100% chuẩn đầu ra của QĐ 2422/QĐ-BGDĐT làm nền tảng pháp lý vững chắc, đồng thời tích hợp trực tiếp Chỉ số năng lực làm giàu quốc tế `[INT-ENRICH]` (từ UNESCO, AI4K12, OECD, Singapore MOE) ngay trong cột YCCĐ của Sản phẩm 1. Không chỉ sao chép văn bản hành chính đơn thuần mà thực sự kiến tạo giá trị hội tụ đa tầng.

---

## II. MA TRẬN THẨM ĐỊNH NGUỒN NGHIÊN CỨU & TÀI LIỆU QUỐC TẾ

Khi tiếp cận một tài liệu nghiên cứu hoặc khung giáo dục AI, bắt buộc thực hiện kiểm định qua **Khung 5 Tiêu chí Thẩm định (CRAAP-AI Model)**:

### 1. Thẩm định Tính Chính thống (Authority & Governance)
- **Cơ quan phát hành**: Tổ chức quốc tế liên chính phủ (UNESCO, UNICEF), cơ quan chính phủ (Singapore MOE, UK DfE, NSF Hoa Kỳ) hay liên minh nghiên cứu/doanh nghiệp uy tín (Google DeepMind, Raspberry Pi Foundation, MIT RAISE).
- **Định vị trong Kiến trúc dự án**: 
  - **UNESCO AI Competency Framework (`02_Tai_Lieu_Quoc_Te/UNESCO/`):** Là **Khung tham chiếu quốc tế trung tâm** (North Star), định hình 4 chiều năng lực và 3 mức độ nhận thức (Understand - Apply - Create).
  - **QĐ 2422/QĐ-BGDĐT (`01_Van_Ban_Phap_Ly/`):** Là **Baseline pháp lý bắt buộc**, đảm bảo 100% tuân thủ chuẩn Việt Nam.
  - **OECD, AI4K12 (`02_Tai_Lieu_Quoc_Te/AI4K12/`):** Là **Benchmark chiều sâu** khoa học máy tính.
  - **Thực tiễn Singapore, Hàn Quốc, Trung Quốc:** Là thực tiễn triển khai (Practices) để làm giàu kinh nghiệm sư phạm.
  - **Kho học liệu AI quốc tế chuẩn mực (`04_Hoc_Lieu_Va_Tham_Khao/Tong_Hop_Nguon_Hoc_Lieu_AI_Quoc_Te_Google_MIT_CommonSense.md`):** Kho tài nguyên chi tiết về giáo án, bài thực hành phân loại ảnh, thiên lệch dữ liệu, game-based learning của Google DeepMind, MIT RAISE, Common Sense và Stanford để bắt buộc đối soát khi thiết kế hoạt động sư phạm.

### 2. Thẩm định Cơ sở Khoa học & Thực nghiệm (Empirical Rigor)
- Tài liệu có dựa trên nghiên cứu thực nghiệm trên học sinh thật không, hay chỉ là tuyên ngôn chính sách?
- Cỡ mẫu và đối tượng thử nghiệm có tương đồng với độ tuổi và năng lực nhận thức của học sinh phổ thông không?

### 3. Phân tích Chi tiết 6 Nguồn Nghiên cứu Quốc tế Trọng điểm

| Nguồn nghiên cứu | Cơ quan / Tổ chức | Ưu điểm cốt lõi (Strengths) | Nhược điểm & Khoảng trống (Weaknesses/Gaps) | Chiến lược Kế thừa & Chuyển hóa vào Việt Nam |
|---|---|---|---|---|
| **UNESCO AI Competency Framework (2024)** | UNESCO | - Đặt giá trị con người và đạo đức lên cao nhất.<br>- Trụ cột vững chắc về tính nhân văn, bảo vệ dữ liệu và phát triển bền vững. | - Quá trừu tượng, mang tính vĩ mô chính sách.<br>- Không phân bổ cụ thể theo 12 khối lớp.<br>- Thiếu hoàn toàn giáo án và công cụ số hóa thực hành. | Lấy làm **Khung tham chiếu quốc tế trung tâm** định hình 4 chiều năng lực (A, B, C, D) và làm Crosswalk với QĐ 2422. |
| **AI4K12 (Five Big Ideas)** | AAAI & CSTA (Mỹ - NSF tài trợ) | - Tiến trình nhận thức máy tính xuất sắc (Perception, Representation, Learning, Natural Interaction, Societal Impact).<br>- Phân tầng rõ ràng K-2, 3-5, 6-8, 9-12. | - Quá thiên về thuật toán và kỹ thuật lập trình (Computer Science heavy).<br>- Yêu cầu hạ tầng thiết bị cao.<br>- Mạch đạo đức, xã hội bị dàn trải ở cuối. | Kế thừa mạch **C (Kỹ thuật)** và **D (Thiết kế hệ thống)**, đặc biệt là các hoạt động trực quan không dùng máy. |
| **Experience AI** | Google DeepMind & Raspberry Pi Foundation | - Chuỗi bài học thực nghiệm về Học máy (Machine Learning) hay nhất cho lứa tuổi 11–14.<br>- Làm rõ thiên lệch dữ liệu, đo độ tin cậy, tập train/test. | - Chủ yếu tập trung vào học máy thị giác và âm thanh, chưa bao quát AI tạo sinh và đạo đức xã hội diện rộng. | Ứng dụng trực tiếp vào các bài dạy về **Học máy có giám sát (Mạch C4, C5)** cấp THCS. |
| **Day of AI (RAISE)** | Viện Công nghệ Massachusetts (MIT) | - Hoạt động dự án trực quan, giàu tính tương tác và kích thích sáng tạo (Teachable Machine, Quick Draw, App Inventor). | - Các dự án thường kéo dài, khó gói gọn trong tiết chuẩn 45 phút của Việt Nam.<br>- Phụ thuộc vào nền tảng trực tuyến của MIT. | Tinh gọn thành các **Pha Trải nghiệm (CE)** và **Thử nghiệm tích cực (AE)** trong chu trình Kolb 45 phút. |
| **Common Sense Media** | Tổ chức phi lợi nhuận (Mỹ) | - Nội dung giáo dục công dân số xuất sắc: nhận diện deepfake, phòng chống lừa đảo mạo danh, tư duy hoài nghi lành mạnh. | - Nhiều tình huống gắn liền với văn hóa mạng xã hội phương Tây, chưa tương thích hoàn toàn bối cảnh học đường Việt Nam. | Chuyển ngữ và **bản địa hóa các kịch bản tình huống** (xâm phạm dữ liệu trường lớp, bắt nạt mạng, dùng AI làm hộ bài tập). |
| **Singapore MOE AI Framework** | Bộ Giáo dục Singapore | - Triết lý chống ỷ lại nhận thức công nghệ.<br>- Rèn luyện năng lực tự chủ và tư duy độc lập của học sinh trước khi nhờ máy. | - Định hướng thi cử áp lực cao, khó áp dụng nguyên bản cho đại trà trường học vùng khó khăn ở Việt Nam. | Tiếp thu nguyên tắc **"Con người suy nghĩ trước, AI hỗ trợ sau"** để tích hợp vào Mạch A1 và Điều 10 CV 5588. |

---

## III. QUY TRÌNH 4 BƯỚC ĐỌC HIỂU & PHÂN TÍCH VĂN BẢN QUY PHẠM GIÁO DỤC

Khi nghiên cứu một văn bản quản lý nhà nước về giáo dục (Quyết định, Thông tư, Công văn), chuyên gia nghiên cứu phải thực hiện theo quy trình:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ BƯỚC 1: XÁC LẬP TƯ CÁCH PHÁP LÝ & PHẠM VI ÁP DỤNG                          │
│ - Xác định cấp ban hành (Bộ GD&ĐT, Sở, Chính phủ).                         │
│ - Xác định văn bản ban hành Khung chuẩn đầu ra hay Hướng dẫn tổ chức thực tế.│
├─────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 2: BÓC TÁCH CÁC RÀNG BUỘC BẤT BIẾN (INVARIANTS)                       │
│ - Tách riêng các yêu cầu BẮT BUỘC (không được vi phạm).                      │
│ - Ví dụ: 12 tiết cốt lõi, không có điểm số riêng, không kiểm tra riêng.     │
├─────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 3: PHÂN TÍCH BIÊN ĐỘ LINH HOẠT CHO PHÉP (FLEXIBILITY BOUNDS)           │
│ - Xác định phần nhà trường và giáo viên được chủ động điều chỉnh.          │
│ - Ví dụ: Tỷ lệ tiết từng mạch, hình thức lồng ghép, lựa chọn công cụ mở.    │
├─────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 4: LẬP BẢNG CẢNH BÁO RỦI RO ÁP DỤNG SAI (COMPLIANCE RISKS)             │
│ - Nhận diện các điểm dễ gây quá tải học sinh, sai lệch thuật ngữ, lạm dụng.│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## IV. NGUYÊN TẮC ĐÁNH GIÁ ƯU - NHƯỢC ĐIỂM CỦA KHUNG CHƯƠNG TRÌNH

Bất kỳ khung chương trình nào cũng có tính thỏa hiệp (trade-offs). Nhà nghiên cứu phải đánh giá khách quan dựa trên 4 chiều kích:

1. **Tính Khoa học & Hiện đại (Scientific Rigor)**: 
   - Khung có cập nhật các công nghệ mới nhất (GenAI, LLM, RAG, AI Agent) hay chỉ dừng lại ở AI truyền thống và hệ chuyên gia cũ?
2. **Tính Khả thi & Vừa sức (Pedagogical Feasibility)**:
   - Học sinh lứa tuổi đó có đủ năng lực trừu tượng để hiểu bản chất không? Hay biến thành bài học vẹt thuộc lòng khái niệm?
3. **Tính Công bằng & Điều kiện Hạ tầng (Equity & Accessibility)**:
   - Nếu trường học ở nông thôn, vùng sâu vùng xa không có máy tính/Internet thì chương trình có dạy được không? (Bắt buộc phải có giải pháp không cắm điện - Unplugged).
4. **Tính Liêm chính & Đạo đức (Ethics & Accountability)**:
   - Học sinh có được học cách chịu trách nhiệm giải trình và kiểm chứng chéo nguồn tin hay chỉ học cách ra lệnh cho AI làm thay?

---

## V. SELF-AUDIT BẢN BÁO CÁO NGHIÊN CỨU (CHECKLIST)

Trước khi công bố một kết luận nghiên cứu hoặc thẩm định khung chương trình, tự kiểm tra:
- [ ] Đã chỉ rõ cơ quan ban hành và thứ bậc pháp lý của tài liệu chưa?
- [ ] Đã phân tích đủ cả 2 mặt: Ưu điểm nổi bật và Nhược điểm/Khoảng trống sư phạm chưa?
- [ ] Các thuật ngữ trong bài phân tích có tuân thủ 100% Bảng chuyển đổi của QĐ 2422 không?
- [ ] Có bị nhầm lẫn giữa khuyến nghị của tài liệu quốc tế với quy định bắt buộc của Bộ GD&ĐT không?
- [ ] Đã đề xuất giải pháp khắc phục nhược điểm phù hợp với điều kiện thực tế của học sinh Việt Nam chưa?