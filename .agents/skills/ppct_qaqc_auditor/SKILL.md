---
name: ppct_qaqc_auditor
description: Chuyên gia kiểm định chất lượng (QA/QC Auditor) toàn diện cho Khung nội dung và Phân phối chương trình (PPCT) giáo dục Trí tuệ nhân tạo. Tự động kiểm tra độ tương thích sư phạm giữa Nội dung bài học và Yêu cầu cần đạt (YCCĐ) theo QĐ 2422/QĐ-BGDĐT và CV 5588/BGDĐT-GDPT trước khi xuất kết quả.
---

# Hướng dẫn Kỹ năng: Kiểm định Chất lượng (QA/QC Auditor) Phân phối Chương trình AI K-12

## Kiểm định tên bài học

Với tài liệu phát sinh Lớp 1–5, kiểm nguyên văn mọi cặp mã–tên trong phạm vi đầu ra với sổ khóa hiện hành ngày 13/10/2026, theo phần 0 của tài liệu quy tắc dưới đây. Sai chữ hoa/thường, dấu nháy, dấu câu, khoảng trắng, tên phụ hoặc dùng tên cũ đều phải sửa lại theo nguồn khóa; không tự đề xuất tên khác trong nhiệm vụ kiểm tài liệu phát sinh.

Khi nhiệm vụ có rà soát tên, đọc [Quy tắc và kỹ năng đặt tên bài học](../../../06_He_Thong_Ky_Thuat/tri_thuc_du_an/QUY_TAC_DAT_TEN_BAI_HOC.md). Kiểm tên với nội dung thực tế và kiến thức/kỹ năng chính của từng bài, rồi kiểm toàn bộ danh sách bằng cùng chín tiêu chuẩn. Nêu tiêu chuẩn chưa đạt khi đề xuất đổi; giữ nguyên tên đạt. Rà soát riêng tên không đồng nghĩa kiểm định lại toàn bộ PPCT hoặc giao sửa tệp ngoài phạm vi.

> **Căn cứ Pháp lý & Tiêu chuẩn Kiểm định Tối cao (Single Source of Truth):**
> Kỹ năng này đóng vai trò là **Hệ thống Kiểm định Độc lập (Quality Assurance & Quality Control System)** cho toàn bộ bản Khung và Phân phối chương trình (PPCT) AI từ Lớp 1 đến Lớp 12:
> - **Quyết định số 2422/QĐ-BGDĐT** (Khung nội dung và YCCĐ chuẩn quốc gia).
> - **Công văn số 5588/BGDĐT-GDPT** (Hướng dẫn tổ chức thực hiện từ năm học 2026-2027).
> - **Quy tắc dự án bất biến tại `AGENTS.md`** (Điều 0 đến Điều 11).
>
> 🚨 **QUY TẮC BẮT BUỘC:** Mọi tác vụ tạo mới, hiệu chỉnh hoặc rà soát PPCT trước khi bàn giao cho người dùng **BẮT BUỘC PHẢI CHẠY BỘ KIỂM ĐỊNH NÀY VÀ ĐÍNH KÈM BÁO CÁO KẾT QUẢ KIỂM ĐỊNH (QA/QC AUDIT REPORT)**.

---

## I. HỆ THỐNG 9 TIÊU CHÍ KIỂM ĐỊNH CHẤT LƯỢNG (THE 9-PILLAR QA/QC MATRIX)

Mỗi bản Khung YCCĐ (Sản phẩm 1) và PPCT (Sản phẩm 2) bắt buộc phải được chấm điểm và đối soát qua 9 trụ cột chất lượng sau:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MA TRẬN 9 TRỤ CỘT KIỂM ĐỊNH QA/QC                     │
│                                                                             │
│ [QC-1] Độ Phù hợp & Tương thích Sư phạm giữa Nội dung Bài học và YCCĐ       │
│        (Pedagogical & Cognitive Alignment - Trụ cột quan trọng nhất)       │
│ [QC-2] Độ Bao phủ Tuyệt đối YCCĐ Cốt lõi & Mở rộng (100% Coverage)          │
│ [QC-3] Chuẩn hóa Kỹ thuật Ghi mã & Tiền tố MR (Coding & Syntax Hygiene)     │
│ [QC-4] Tính Độc lập & Không Gán trùng lặp Mã (Non-Duplication Rule)         │
│ [QC-5] Quy chuẩn Tiết Đánh giá & Triển lãm (Assessment & Exhibition Rule)   │
│ [QC-6] Chính sách Từ vựng Chuẩn Tuyệt đối (Zero-Deviation Terminology)      │
│ [QC-7] Tính Cân đối 4 Mạch & Tiến trình Phát triển Xoắn ốc (Spiral Progress)│
│ [QC-8] Tính Khả thi Hạ tầng & Công bằng Tiếp cận (Equity & Accessibility)   │
│ [QC-9] Nghiệm thu Khung YCCĐ SP1, Giao thức Human Lock & Tiền kiểm tự động  │
│        (SP1 Deliverables, Age-Appropriate Blacklist & Pre-flight Gate)      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## II. CHI TIẾT TỪNG TIÊU CHÍ KIỂM ĐỊNH

### 🎯 QC-1: ĐỘ PHÙ HỢP & TƯƠNG THÍCH SƯ PHẠM GIỮA NỘI DUNG VÀ YCCĐ (TRỌNG TÂM)
*Mục tiêu: Đảm bảo Tên bài học và Mô tả hoạt động phản ánh đúng bản chất nhận thức của YCCĐ được gán, không "treo đầu dê bán thịt chó", không vượt chuẩn và không hạ chuẩn.*

1. **Kiểm định Động từ Hành vi (Action Verb Fidelity):**
   - Đối chiếu động từ trong YCCĐ gốc QĐ 2422 (*Nhận biết, Nêu được, Kể tên, Giải thích, Mô tả, Thực hành, Phân biệt, Trình bày, Đề xuất...*) với hoạt động học tập của bài học.
   - *Ví dụ vi phạm:* YCCĐ chỉ yêu cầu *"Nhận biết AI qua một số ví dụ đơn giản"* nhưng bài học lại yêu cầu *"Học sinh lập trình thuật toán Python"* ➔ **LỖI VƯỢT CHUẨN**.
   - *Ví dụ vi phạm:* YCCĐ yêu cầu *"Thực hành kiểm tra lại kết quả do AI đưa ra"* nhưng bài học chỉ cho học sinh *"Nghe giáo viên đọc kết quả"* ➔ **LỖI HẠ CHUẨN**.
2. **Kiểm định Tương thích Nội dung (Content Semantic Match):**
   - Tên bài học và hoạt động có chứa các khái niệm cốt lõi của YCCĐ không?
   - *Ví dụ:* Gán mã `6.A1.1` (Con người tạo ra và điều khiển AI) thì nội dung bắt buộc phải làm rõ vai trò con người là chủ thể tạo ra công cụ, con người kiểm soát; không thể chỉ dạy cách sử dụng phần mềm thuần túy.
3. **Kiểm định Phù hợp Tâm lý Lứa tuổi & Thời lượng Tiết học (Age-Appropriate Pedagogy & Duration):**
   - **Cấp Tiểu học:**
     - *Lớp 1 – 2 (Thời lượng 30 – 35 phút):* Hoạt động ngắn gọn, xem tranh, nghe kể chuyện, xếp thẻ, trò chơi thể chất nhẹ nhàng, Unplugged.
     - *Lớp 3 – 5 (Thời lượng 35 – 40 phút, chuẩn 35 phút):* Quy tắc đơn giản, tự suy nghĩ trước khi hỏi máy, thí nghiệm nhận diện mẫu trực quan.
   - **Cấp THCS (Lớp 6 – 9 - Thời lượng tiêu chuẩn 45 phút):** Hoạt động logic, điều tra số liệu, lập bảng đối chiếu chéo, lưu vết prompt log, tranh biện đạo đức.
   - **Cấp THPT (Lớp 10 – 12 - Thời lượng tiêu chuẩn 45 phút):** Nghiên cứu tình huống sâu (case study), thiết kế câu lệnh chuyên sâu, thử nghiệm mô hình, giải pháp xã hội.
4. **Đối chiếu Bắt buộc Nguồn Tâm lý Phát triển Học sinh (`04_Hoc_Lieu_Va_Tham_Khao/Tong_Hop_Nguon_Tai_Lieu_Tam_Ly_Phat_Trien_Hoc_Sinh.md`):**
   - Soi chiếu YCCĐ đầu ra và hoạt động trong tiết dạy với các mốc phát triển nhận thức – cảm xúc (Piaget, Erikson, Vygotsky ZPD, CASEL K-5 & 6-8, CDC, UNICEF).
   - Nghiêm cấm **Lỗi mầm non hóa** (hành vi cơ học, nhắc vẹt, thụ động) và **Lỗi học thuật hóa** (vượt quá khả năng nhận thức ZPD).
5. **Đối chiếu Bắt buộc Kho Học liệu AI Quốc tế Chuẩn mực (`04_Hoc_Lieu_Va_Tham_Khao/Tong_Hop_Nguon_Hoc_Lieu_AI_Quoc_Te_Google_MIT_CommonSense.md`):**
   - Kiểm tra các hoạt động thực hành (Hands-on), bài thí nghiệm thiên lệch (Bias lab), bài học đạo đức số (AI Literacy) và kịch bản giải quyết vấn đề xem có được đối soát và kế thừa từ Google DeepMind (Experience AI), MIT RAISE, Common Sense Education và Stanford AI Quests hay không.

---

### 🎯 QC-2: ĐỘ BAO PHỦ 100% YCCĐ CỐT LÕI VÀ MỞ RỘNG (DUAL-TRACK FULL COVERAGE)
- Trích xuất toàn bộ danh mục mã cốt lõi và mở rộng của khối lớp từ `06_He_Thong_Ky_Thuat/extracted_data/qd2422_full.txt`.
- **Khung 12 tiết Cốt lõi (12 CORE):** Mọi mã cốt lõi (`VN-CORE`, ví dụ: `X.YZ.1`, `X.YZ.2`...) **phải xuất hiện đầy đủ 100%**. Nghiêm cấm bỏ sót bất kỳ mã cốt lõi nào.
- **Khung 24 tiết Mở rộng (24 EXPANDED):** Mọi mã mở rộng (`VN-MR`, ví dụ: `X.YZ.MR1`, `X.YZ.MR2`...) ban hành trong QĐ 2422 **bắt buộc phải xuất hiện đầy đủ 100%**. Tuyệt đối không được bỏ sót bất kỳ mã mở rộng nào của Bộ.

---

### 🎯 QC-3: KỸ THUẬT GHI MÃ, NHÃN OUTCOME & TRACEABILITY (CODING & TAXONOMY HYGIENE)
- **Quy tắc mã mở rộng:** Bắt buộc có đầy đủ số thứ tự: `X.YZ.MR1`, `X.YZ.MR2`... CẤM TUYỆT ĐỐI dạng cụt số `X.YZ.MR`.
- **Cấu trúc mã chuẩn:** `[Lớp].[Mạch/Chủ đề].[Số TT]`, ví dụ `6.C1.1`, `1.D2.MR1`. Không tự bịa mã ngoài QĐ 2422.
- **Hệ thống 3 nhãn Outcome:** 
  - `VN-CORE`: YCCĐ cốt lõi bắt buộc của Bộ.
  - `VN-MR`: YCCĐ mở rộng của Bộ.
  - `INT-ENRICH`: Mục tiêu/Năng lực làm giàu quốc tế (UNESCO, AI4K12, Singapore MOE) được cài cắm trong hoạt động ở cả 36 tiết.
- **Tính truy xuất (Traceability):** Các tiết học phải có sự tham chiếu tương ứng đến năng lực UNESCO và Benchmark chiều sâu.

---

### 🎯 QC-4: TÍNH ĐỘC LẬP & KHÔNG GÁN TRÙNG LẶP MÃ (NON-DUPLICATION)
- Mỗi mã YCCĐ chỉ được gán tại **tiết học chính** — nơi trực tiếp dạy và hình thành chuẩn đầu ra đó.
- Không gán dồn dập các mã cốt lõi đã học vào các tiết ôn tập, tổng kết hay đánh giá cuối kỳ (như lỗi Tiết 36 cũ).

---

### 🎯 QC-5: QUY CHUẨN TIẾT ĐÁNH GIÁ & TRIỂN LÃM (MỤC VI QĐ 2422)
- **Tiết Đánh giá định kỳ quá trình:** Ghi chuẩn mã **`Mục VI QĐ 2422`**.
- **Tiết Triển lãm / Báo cáo sản phẩm / Ngày hội tổng kết:** **ĐỂ TRỐNG** cột Mã YCCĐ.
- **Nghiêm cấm:** Không ghi các nhãn tự do như `"Ôn tập MR"`, `"Tổng kết MR"`, `"Triển lãm MR"`.
- Không đưa các bài thi trắc nghiệm lý thuyết riêng biệt hoặc đầu điểm số độc lập vào chương trình.

---

### 🎯 QC-6: CHÍNH SÁCH TỪ VỰNG CHUẨN TUYỆT ĐỐI (ZERO-DEVIATION)
- Soát lỗi văn bản tự động dựa trên Điều 1 và Điều 11 `AGENTS.md`.
- Cấm toàn bộ từ lóng/tự do:
  - *"nhắc lệnh"* ➔ **Câu lệnh (prompt)**
  - *"ảo tưởng mô hình / AI chém gió"* ➔ **Ảo giác AI (hallucination)**
  - *"thành kiến máy móc"* ➔ **Thiên lệch (bias)**
  - *"video giả / clip ghép mặt"* ➔ **Nội dung giả mạo do AI tạo ra (deepfake)**
  - *"quá tải mô hình"* ➔ **Quá khớp (overfitting)**
  - *"ẩn danh tính, che mặt"* ➔ **Khử nhận dạng dữ liệu cá nhân**
  - *"12 tiết tự chọn"* ➔ **Các chuyên đề giáo dục AI bắt buộc với thời lượng 12 tiết/lớp/năm học dành cho nội dung cốt lõi**.

---

### 🎯 QC-7: TÍNH CÂN ĐỐI 4 MẠCH & TIẾN TRÌNH PHÁT TRIỂN XOẮN ỐC (SPIRAL PROGRESSION & ZPD)
- **Đủ 4 mạch:** Cả 4 mạch **A (Con người), B (Đạo đức), C (Kỹ thuật/Ứng dụng), D (Thiết kế hệ thống)** đều phải hiện diện trong phân phối chương trình của mọi khối lớp.
- **Tiến trình Xoắn ốc & ZPD (Vertical Alignment):**
  - Kiến thức lớp dưới làm bệ phóng cho lớp trên, mở rộng vùng phát triển gần nhất (ZPD).
  - Nghiêm cấm lặp lại phẳng (không copy nguyên si hoạt động lớp dưới lên lớp trên mà không có hiểu biết mới hoặc công cụ thực hành mới).
  - Có các tiết kích hoạt lại tri thức cũ (Prior Knowledge Activation) trước khi đưa thử thách mới.
- **Bảo toàn liên kết giữa các sản phẩm:**
  - *Không có YCCĐ mồ côi:* 100% YCCĐ cốt lõi và mở rộng của QĐ 2422 đều phải có mặt trong PPCT.
  - *Không có nội dung trôi nổi:* Mọi bài học/hoạt động đều phải truy xuất ngược được về mã YCCĐ bảo trợ.

---

### 🎯 QC-8: TÍNH KHẢ THI HẠ TẦNG & CÔNG BẰNG TIẾP CẬN (CV 5588)
- Phân phối chương trình phải có các hoạt động dự phòng **không dùng máy tính (Unplugged)** cho các trường vùng khó khăn.
- Tuyệt đối không có bài học nào bắt buộc học sinh/phụ huynh phải mua tài khoản trả phí hay thiết bị chuyên dụng.

---

### 🎯 QC-9: NGHIỆM THU KHUNG YCCĐ (SẢN PHẨM 1), GIAO THỨC HUMAN LOCK & TIỀN KIỂM TỰ ĐỘNG (PRE-FLIGHT GATE)
*Mục tiêu: Đảm bảo Sản phẩm 1 (Khung YCCĐ & Năng lực đầu ra) đạt chuẩn tuyệt đối về số lượng pháp lý, độ an toàn ngôn ngữ tâm lý lứa tuổi và tính đồng bộ đa định dạng trước khi bàn giao.*

1. **Khóa cứng số lượng YCCĐ theo QĐ 2422 (Row Integrity Check):**
   - Lớp 1: Đúng **21 YCCĐ** (17 Cốt lõi + 4 Mở rộng).
   - Lớp 2: Đúng **29 YCCĐ** (17 Cốt lõi + 12 Mở rộng).
   - Lớp 3: Đúng **32 YCCĐ** (21 Cốt lõi + 11 Mở rộng).
   - Lớp 4: Đúng **17 YCCĐ** (10 Cốt lõi + 7 Mở rộng).
   - Lớp 5: Đúng **24 YCCĐ** (15 Cốt lõi + 9 Mở rộng).
   - Toàn cấp Tiểu học: Đúng **123 YCCĐ** (80 Cốt lõi + 43 Mở rộng).
   - Sai lệch dù chỉ 1 dòng cũng bị đánh trượt (FAIL).
2. **Bộ lọc từ cấm theo lứa tuổi (Age-Appropriate Blacklist Filter):**
   - Quét regex tự động phát hiện các cụm từ bị cấm:
     - ❌ *"pháp lý"* (không gán trách nhiệm pháp lý cho trẻ tiểu học).
     - ❌ *"độc quyền", "phẩm chất độc quyền"* (thay bằng năng lực giữ vai trò trung tâm).
     - ❌ *"kiên quyết bài trừ"* (thay bằng tránh lạm dụng, không chia sẻ bừa bãi).
     - ❌ *"kiểm thử đối kháng"* (thay bằng kiểm tra kết quả trên nhiều trường hợp/nhóm khác nhau).
     - ❌ *"nguyên lý học liên tục"* (thay bằng cải tiến hệ thống khi dữ liệu được bổ sung/cập nhật).
     - ❌ *"thao tác thành thạo", "đo lường độ tin cậy"* (thay bằng thao tác cơ bản, quan sát điểm số tin cậy).
     - ❌ *"tất yếu / vô hiệu"* ở Lớp 3 (thay bằng cần thiết / mất tác dụng).
3. **Đồng bộ hóa 2 định dạng đầu ra (Dual-Format Sync):**
   - Bản Đầy đủ: Bảng 5 cột, A4 Landscape (Ngang), đầy đủ đối sánh quốc tế 3 tầng.
   - Bản Rút gọn: Bảng 4 cột, A4 Portrait (Dọc), chuẩn đầu ra năng lực súc tích.
   - Nội dung ngữ nghĩa giữa 2 bản phải khớp 1-1, đồng bộ cả tệp Word và Markdown.
4. **Kiểm định Giới hạn Tài liệu Tham khảo Tiểu học (Anti-Secondary Creep Gate):**
   - Tuyệt đối cấm đưa các bài học, thuật ngữ và yêu cầu kỹ thuật của THCS (11–15 tuổi / Grades 6–8) vào cấp Tiểu học (Lớp 1–5):
     - ❌ Cấm Decision trees (Cây quyết định), Mạng nơ-ron đa tầng, Ma trận nhầm lẫn, Thẻ mô hình (Model cards).
     - ❌ Cấm viết Prompt đa tầng phức tạp (Role-based, Chain-of-thought, Few-shot chuyên sâu).
     - ❌ Cấm trích dẫn hoặc sử dụng học liệu của Common Sense Education (Grades 6–12) cho Lớp 1–5.
   - Phát hiện bất kỳ yếu tố xâm lấn THCS nào trong sản phẩm Tiểu học đều bị đánh trượt (FAIL).

---

## III. QUY TRÌNH KIỂM ĐỊNH VÀ XUẤT BÁO CÁO (QA/QC PROTOCOL)

Khi hoàn thành việc xây dựng hoặc chỉnh sửa bất kỳ bản Khung YCCĐ hay PPCT nào, AI phải thực hiện quy trình 3 bước sau:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ BƯỚC 1: CHẠY SCRIPT TỰ ĐỘNG QUÉT DỮ LIỆU TỆP (.docx / .xlsx / .md)           │
│ - Quét mã lỗi cụt số (.MR không có số).                                     │
│ - Quét số lượng hàng bảng khớp 100% định mức QĐ 2422 (QC-9 Gate 1).         │
│ - Quét từ khóa vi phạm blacklist lứa tuổi (QC-9 Gate 2).                    │
│ - Thống kê tần suất xuất hiện và kiểm tra tính trùng lặp của từng mã YCCĐ.  │
├─────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 2: SOÁT NỘI DUNG SƯ PHẠM ĐỐI CHIẾU VỚI TỪNG MÃ YCCĐ (QC-1 & QC-9)     │
│ - Đọc từng dòng: Tên bài + Hoạt động có tương thích với YCCĐ QĐ 2422 không?│
│ - Soát lỗi từ vựng theo bảng Zero-Deviation (QC-6) và Human Lock (QC-9).    │
├─────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 3: XUẤT BÁO CÁO KẾT QUẢ KIỂM ĐỊNH (QA/QC AUDIT REPORT)                │
│ - Lập bảng điểm 9 tiêu chí kèm nhận xét bằng chứng cụ thể.                 │
│ - Đưa ra kết luận chính thức: ĐẠT / CẦN SỬA / KHÔNG ĐẠT.                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## IV. BIỂU MẪU CHUẨN BÁO CÁO KẾT QUẢ KIỂM ĐỊNH (MẪU BẮT BUỘC ĐÍNH KÈM)

Mọi báo cáo kết quả gửi người dùng phải tuân thủ đúng khung cấu trúc markdown dưới đây:

```markdown
# BÁO CÁO KẾT QUẢ KIỂM ĐỊNH CHẤT LƯỢNG (QA/QC AUDIT REPORT)
**Đối tượng kiểm định:** [Tên tệp và Khối lớp]
**Thời điểm kiểm định:** [Ngày/Tháng/Năm]
**Căn cứ:** QĐ 2422/QĐ-BGDĐT, CV 5588/BGDĐT-GDPT và AGENTS.md

### BẢNG CHẤM ĐIỂM 9 TIÊU CHÍ
| Mã Tiêu chí | Nội dung Kiểm định | Điểm số (1-10) | Đánh giá | Minh chứng & Ghi chú |
|:---:|---|:---:|:---:|---|
| QC-1 | Độ phù hợp giữa Nội dung & YCCĐ | .../10 | ĐẠT/CHƯA | ... |
| QC-2 | Độ bao phủ 100% YCCĐ cốt lõi & mở rộng | .../10 | ĐẠT/CHƯA | ... |
| QC-3 | Kỹ thuật ghi mã & tiền tố MR | .../10 | ĐẠT/CHƯA | ... |
| QC-4 | Tính độc lập & Không trùng lặp | .../10 | ĐẠT/CHƯA | ... |
| QC-5 | Quy chuẩn Tiết Đánh giá (Mục VI) | .../10 | ĐẠT/CHƯA | ... |
| QC-6 | Chuẩn hóa từ vựng Zero-Deviation | .../10 | ĐẠT/CHƯA | ... |
| QC-7 | Cân đối 4 mạch & Tiến trình xoắn ốc| .../10 | ĐẠT/CHƯA | ... |
| QC-8 | Hạ tầng & Công bằng tiếp cận | .../10 | ĐẠT/CHƯA | ... |
| QC-9 | Nghiệm thu SP1 & Giao thức Human Lock | .../10 | ĐẠT/CHƯA | ... |
| 🏆 | **ĐIỂM TỔNG KẾT CHẤT LƯỢNG** | **.../10** | **KẾT LUẬN CHÍNH THỨC** |

### CHI TIẾT ĐỐI SOÁT ĐỘ PHÙ HỢP SƯ PHẠM (QC-1 & QC-9 HIGHLIGHTS)
- [Liệt kê các điểm khóa chuẩn tiêu biểu chứng minh độ tương thích nhận thức và lứa tuổi]

### KẾT LUẬN & KIẾN NGHỊ PHÊ DUYỆT
- [Kết luận rõ ràng: Sản phẩm có đủ điều kiện đưa vào sử dụng hay cần điều chỉnh gì thêm]
```
