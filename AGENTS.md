# QUY TẮC DỰ ÁN: XÂY DỰNG CHƯƠNG TRÌNH & NỘI DUNG GIÁO DỤC AI (QĐ 2422/QĐ-BGDĐT)

> **CĂN CỨ PHÁP LÝ VÀ CHUYÊN MÔN CAO NHẤT (SINGLE SOURCE OF TRUTH):**
> Toàn bộ quá trình tư vấn, soạn thảo chương trình, kế hoạch bài dạy, tài liệu hoạt động, phân rã kỹ năng nhỏ và xây dựng câu hỏi/rubric trong dự án này bắt buộc phải tuân thủ nghiêm ngặt **Quyết định số 2422/QĐ-BGDĐT** của Bộ Giáo dục và Đào tạo ban hành *"Khung nội dung giáo dục Trí tuệ nhân tạo cho học sinh phổ thông"*.
>
> Mọi thành viên và trợ lý AI tham gia dự án phải chấp hành vô điều kiện các quy tắc bất biến dưới đây.

## QUY TẮC CỨNG: KHÓA MÃ BÀI VÀ TÊN BÀI PPCT LỚP 1–5 — 13/10/2026

Theo chỉ định trực tiếp của người dùng, áp dụng các quy tắc sau cho PPCT và tài liệu phát sinh của Lớp 1–5:

1. **Nguồn hiện hành đã được người dùng chốt.** Mọi nhiệm vụ tiếp theo có bài học Lớp 1–5 phải lấy mã và tên từ [SP3_ Phan_phoi_Chuong_Trinh_AI_Lop_1_5_36_Bai.docx](<03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_ Phan_phoi_Chuong_Trinh_AI_Lop_1_5_36_Bai.docx>), gồm năm bảng 36 bài, đã cập nhật tên ngày 13/10/2026. [Bản Markdown cùng tên](<03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_ Phan_phoi_Chuong_Trinh_AI_Lop_1_5_36_Bai.md>) là bản đối chiếu đầy đủ nội dung Word. Ver2, Rev03/Rev04, các bản Markdown cũ khác tên và các bảng tra cứu chưa đồng bộ là lịch sử, không dùng tên của chúng thay nguồn hiện hành. Chỉ định trực tiếp mới của người dùng có thể thay nguồn hoặc phạm vi này.
2. **Mã bài là khóa tra cứu.** Cột đầu tiên là `Bài`; sao chép đầy đủ mã `Bài [Lớp].[01–36].[CL hoặc MR]` từ nguồn, ví dụ `Bài 1.01.CL`, `Bài 5.02.MR`. Giữ hai chữ số, hậu tố và thứ tự 36 bài; không tự đánh số lại, chọn lại CL/MR hoặc ghép bài chỉ theo số thứ tự của một bản cũ. Thời lượng dạy học vẫn tính bằng tiết/phút.
3. **Giữ màu mã theo nguồn.** Chỉ ô mã của bài CL được tô vàng `FFFF00`; bản hiện hành có 12 ô mỗi lớp. Không tô vàng cả dòng hoặc tự lấy ánh xạ CL/MR của phiên bản khác. Phân bổ trong nguồn không tự chứng minh đã kiểm định đầy đủ YCCĐ.
4. **Phân biệt mã bài với mã YCCĐ.** Hậu tố CL/MR định danh phân bổ trong kế hoạch năm học, không thay các nhãn `VN-CORE`, `VN-MR`, `INT-ENRICH`, mã YCCĐ hay chức năng đánh giá/triển lãm. Việc khóa hoặc đồng bộ tên không cho phép tự sửa các nhãn và mã YCCĐ; lỗi kế thừa cần được ghi riêng để xem xét.
5. **Khóa nguyên văn 180 tên đã cập nhật.** [Sổ tên hiện hành](06_He_Thong_Ky_Thuat/QA_QC/Cap_Nhat_Ten_Bai_180_20261013/approved_titles_180.json) lưu tên tại `records[].title`, tra bằng `records[].code`. Giữ nguyên từng ký tự: từ ngữ, dấu tiếng Việt, chữ hoa/thường, dấu câu, dấu nháy và khoảng trắng. Không rút gọn, thay từ đồng nghĩa, thêm tên phụ, ghép tên hoạt động hoặc tự sửa tên theo tiêu chuẩn sư phạm khi soạn tài liệu phát sinh. Mã bài và các đề mục triển khai được ghi riêng với trường tên chuẩn; Word được tự ngắt dòng khi hiển thị.
6. **Áp dụng cho mọi tài liệu phát sinh trong các nhiệm vụ tiếp theo.** Hồ sơ bài học, kế hoạch bài dạy, phiếu học tập, học liệu, slide, câu hỏi/rubric, bảng nhóm kỹ năng, ma trận, bảng tra cứu và dữ liệu xuất dùng cùng cặp mã–tên đã khóa. Nhiệm vụ xây dựng nội dung, phân rã kỹ năng hoặc cải thiện hoạt động không đồng thời giao đổi tên bài. Tên tệp có thể dùng mã bài phù hợp hệ điều hành; tên chuẩn trong nội dung vẫn phải nguyên văn.
7. **Tra trước khi soạn, đối chiếu trước khi bàn giao.** Lấy đúng cặp mã–tên từ Word hiện hành, bản Markdown đã đồng bộ hoặc sổ tên; đưa nguyên văn vào phiếu giao Anti khi có giao thực hiện. Kiểm mọi bài trong phạm vi đầu ra với sổ khóa, kể cả tên lặp trong nhiều phần. Nếu nguồn và sổ khóa lệch nhau hoặc thiếu mã, ghi rõ điểm lệch và đối chiếu chỉ định mới nhất; không đoán, không lấy theo ngày sửa tệp và không âm thầm cập nhật sổ khóa. Chỉ đổi tên theo yêu cầu trực tiếp, rõ ràng của người dùng; khi được giao áp dụng, đồng bộ Word, Markdown, sổ tên và tài liệu liên quan trong phạm vi được giao. Khóa định danh không đồng nghĩa Human Lock hay nghiệm thu toàn bộ chương trình.
8. **Bảo toàn PPCT và đặt chi tiết đúng tầng sản phẩm.** Bản hiện hành có năm cột: `Bài`, `Tên bài`, `Nội dung trọng tâm & Kỹ năng tích hợp`, `Thiết bị & Học liệu`, `Mã YCCĐ`. Khi chỉ đồng bộ hoặc khóa tên, giữ nguyên các cột khác, nhãn KN, thứ tự và định dạng Word. Markdown phản ánh đầy đủ các ô của Word; không rút gọn nội dung trọng tâm. Hành động học sinh, minh chứng và thời lượng bốn pha đặt trong hồ sơ chi tiết của bài theo nhiệm vụ được giao.

## QUY TẮC ĐẶT TÊN BÀI HỌC — CẬP NHẬT 13/10/2026

Khi xây dựng tên mới hoặc được giao rà soát tên, bắt buộc đọc và áp dụng [Quy tắc và kỹ năng đặt tên bài học](06_He_Thong_Ky_Thuat/tri_thuc_du_an/QUY_TAC_DAT_TEN_BAI_HOC.md): chín tiêu chuẩn áp dụng đồng thời, cách xác định kiến thức/kỹ năng chính, quy trình giữ hoặc đổi tên và kiểm chất lượng toàn bộ danh sách. Các skill xây dựng, kiểm định và điều phối PPCT dùng cùng tài liệu này.

Các tiêu chuẩn đặt tên áp dụng khi được giao xây dựng tên mới hoặc rà soát tên. Với 180 bài đã khóa ở phần trên, nhiệm vụ biên soạn tài liệu phát sinh phải giữ tên chuẩn, không tự chạy lại vòng đổi tên. Sổ tên Ver2 giữ nguyên làm lịch sử; nguồn và sổ khóa hiện hành thay các chỉ dẫn trước đây về lấy tên Ver2 cho nhiệm vụ Lớp 1–5 tiếp theo, trừ khi người dùng chỉ định khác.

## ĐIỀU 0. THỨ BẬC VĂN BẢN PHÁP LÝ CỦA DỰ ÁN

Dự án căn cứ vào hệ thống văn bản pháp lý và hướng dẫn chuyên môn theo thứ bậc sau (từ cao xuống thấp):

1. **Quyết định số 2422/QĐ-BGDĐT** (ngày 18/8/2026 của Bộ GD&ĐT) — *"Khung nội dung giáo dục Trí tuệ nhân tạo cho học sinh phổ thông"*: **Văn bản pháp lý và chuyên môn tối cao (Single Source of Truth)**. Quy định chuẩn về mục tiêu, 4 mạch nội dung (A, B, C, D), danh mục YCCĐ cốt lõi/mở rộng từ Lớp 1 đến Lớp 12, định hướng đánh giá và 26 thuật ngữ chuẩn hóa tại Phụ lục.
2. **Công văn số 5588/BGDĐT-GDPT** (ngày 19/8/2026 của Bộ GD&ĐT) — *"V/v hướng dẫn triển khai thực hiện nội dung giáo dục trí tuệ nhân tạo cho học sinh phổ thông từ năm học 2026-2027"*: **Văn bản hướng dẫn triển khai thực tế**. Quy định 3 hình thức tổ chức (chuyên đề 12 tiết cốt lõi, lồng ghép trong các môn học, hoạt động theo nhu cầu), bảo đảm công bằng tiếp cận, điều kiện hạ tầng, an toàn dữ liệu học sinh và phân công trách nhiệm các cấp.
3. **Công văn số 5512/BGDĐT-GDTrH** (cấp THCS, THPT) và **Công văn số 2345/BGDĐT-GDTH** (cấp Tiểu học) — Khung cấu trúc kế hoạch bài dạy và phân phối chương trình chuẩn.

> **Nguyên tắc xử lý văn bản:** CV 5588 là hướng dẫn triển khai thi hành QĐ 2422. Tuyệt đối không sử dụng hướng dẫn linh hoạt của CV 5588 để làm biến dạng hoặc hạ chuẩn các YCCĐ và mạch năng lực bắt buộc đã ban hành tại QĐ 2422.

---

### BẢN ĐỒ CẤU TRÚC THƯ MỤC DỰ ÁN (6 NHÓM CHUẨN HOÁ)
Toàn bộ tệp và dữ liệu trong dự án được tổ chức nghiêm ngặt theo 6 nhóm thư mục chức năng. Mọi trợ lý AI và công cụ phải truy xuất tệp theo đúng đường dẫn mới:
* `01_Van_Ban_Phap_Ly/`: Căn cứ pháp lý Việt Nam (QĐ 2422/QĐ-BGDĐT và CV 5588/BGDĐT-GDPT).
* `02_Tai_Lieu_Quoc_Te/`: Khung tham chiếu và Benchmark quốc tế:
  * `DANH_MUC_NGUON_TAI_LIEU_QUOC_TE.md` & `README.md`: Danh mục tổng thể và quy chuẩn truy xuất nguồn (Single Source of Truth).
  * `UNESCO/`: Khung năng lực AI của UNESCO cho học sinh (`unessco.pdf`, `unesscoVN.pdf`).
  * `AI4K12/`: Khung tiến trình 5 Big Ideas của AI4K12 (`AI4K12-Big-Idea-*.pdf`).
  * `Experience_AI_Google_DeepMind/`: Giáo trình Experience AI của Google DeepMind & Raspberry Pi Foundation.
  * `MIT_Day_of_AI/`: Giáo trình Day of AI của Viện Công nghệ Massachusetts (MIT RAISE) (`DAI-*.pdf`).
  * `Common_Sense_Education/`: Giáo trình AI Literacy Lessons Lớp 6-12 của Common Sense Education.
  * `Google_for_Education_va_Stanford/`: Teaching Responsible Use of AI và Stanford AI Quests.
  * `OECD_va_Singapore_MOE/`: Khung OECD Learning Compass 2030 và Singapore MOE NDLP.
  * `Khac/`: AILF (`AILF_en.pdf`).
* `03_San_Pham_Chinh_Thuc/`: Các sản phẩm hoàn thiện bàn giao (PPCT Word/Excel, Kế hoạch bài dạy Kolb...).
* `04_Hoc_Lieu_Va_Tham_Khao/`: Ngân hàng hoạt động sư phạm tham khảo (`Ngan_Hang_Hoat_Dong_Va_Kich_Ban_Su_Pham_Tham_Khao.xlsx`), tài liệu phân tích đối chiếu, tổng hợp nguồn tâm lý phát triển học sinh (`Tong_Hop_Nguon_Tai_Lieu_Tam_Ly_Phat_Trien_Hoc_Sinh.md`), tổng hợp nguồn học liệu AI quốc tế Google/MIT/CommonSense (`Tong_Hop_Nguon_Hoc_Lieu_AI_Quoc_Te_Google_MIT_CommonSense.md`).
* `05_Bao_Cao_Chuyen_De/`: Báo cáo chuyên sâu và luật AI các nước.
* `06_He_Thong_Ky_Thuat/`: Mã nguồn scripts, dữ liệu trích xuất .txt, hình ảnh và các bản sao lưu (backups).
* **Tại thư mục gốc:** Duy trì duy nhất file `AGENTS.md` (Quy tắc bất biến) và thư mục `.agents/` (Hệ thống skills).

---

## ĐIỀU 0B. KIẾN TRÚC NĂNG LỰC AI VÀ MÔ HÌNH HỘI TỤ ĐA TẦNG

Chương trình giáo dục AI của dự án được vận hành theo Mô hình phễu hội tụ đa tầng chuẩn mực quốc tế:

```text
                  UNESCO AI COMPETENCY FRAMEWORK
              Khung tham chiếu quốc tế trung tâm
                            │
                            ▼
                 KIẾN TRÚC NĂNG LỰC AI
                            │
              ┌─────────────┴─────────────┐
              │                           │
         QĐ2422 + VN               OECD / AI4K12
    YCCĐ CỐT LÕI + MỞ RỘNG (MR)     benchmark chiều sâu
              │                           │
              └─────────────┬─────────────┘
                            │
                    INTERNATIONAL
                      CROSSWALK
                            │
               Singapore / Korea / China
                 curriculum practices
                            │
                            ▼
                  CHƯƠNG TRÌNH VIỆT NAM
                       36 tiết/năm
                 ┌──────────┴──────────┐
                 │                     │
             12 CORE              24 EXPANDED
        ┌────────────────┐   ┌────────────────────┐
        │  ĐẠT 100% YCCĐ │   │   ĐẠT 100% YCCĐ    │
        │ CỐT LÕI QĐ2422 │   │  MỞ RỘNG (MÃ MR)   │
        │   (Bắt buộc)   │   │      CỦA QĐ2422    │
        │       +        │   │        +           │
        │ Sư phạm & học  │   │ Đào sâu YCCĐ cốt lõi│
        │  liệu quốc tế  │   │        +           │
        │ (UNESCO/AI4K12)│   │ Làm giàu quốc tế   │
        └────────────────┘   │ (Dự án/OECD/Sing)  │
                 │           └────────────────────┘
                 │                     │
                 └──────────┬──────────┘
                            ▼
                MODULE → BÀI → ACTIVITY
                      → ASSESSMENT
```

### Các nguyên lý vận hành của Mô hình Kiến trúc:
1. **UNESCO là Khung tham chiếu trung tâm (North Star):** Định hình 4 chiều năng lực (Tư duy lấy con người làm trung tâm, Đạo đức, Kỹ thuật và ứng dụng, Thiết kế hệ thống) và 3 mức độ thành thạo (Understand – Apply – Create).
2. **QĐ 2422 và Pháp luật Việt Nam là Baseline bắt buộc (Hợp pháp 100%):** Mọi đầu ra chương trình đều phải neo chặt vào danh mục YCCĐ chính thức của Bộ GD&ĐT.
3. **OECD và AI4K12 là Benchmark chiều sâu:** Cung cấp độ sâu khoa học nhận thức máy tính (5 Big Ideas) và năng lực công dân số tương lai.
4. **Kinh nghiệm thực tiễn từ Singapore, Hàn Quốc, Trung Quốc (Practices):** Tích hợp tư duy tự chủ, chống ỷ lại nhận thức công nghệ (Singapore MOE); mô hình phổ cập AI (Hàn Quốc); và ứng dụng dự án thực tiễn (Trung Quốc).
5. **Traceability 3 tầng:** Mọi bài học, hoạt động đều có khả năng giải trình và truy xuất ngược 3 tầng: `Bài học` ➔ `Mã YCCĐ QĐ2422` ➔ `UNESCO Competency & Level` ➔ `Benchmark quốc tế bổ trợ`.

---

## ĐIỀU 0C. NGUYÊN TẮC NHẤT QUÁN VÀ KẾ THỪA VỚI CHƯƠNG TRÌNH MÔN TIN HỌC (CT GDPT 2018)

Khung nội dung giáo dục AI được thiết kế và vận hành theo nguyên tắc liên thông mật thiết và kế thừa nền tảng từ môn Tin học:

1. **Quan điểm xây dựng (Mục I.2): Nhất quán với môn Tin học**
   * Nền tảng kiến thức, kĩ năng của AI ở trường phổ thông là khoa học máy tính, và đó cũng là nền tảng cốt lõi của môn Tin học.
   * Khung nội dung giáo dục AI được thiết kế liên thông chặt chẽ với môn Tin học, kế thừa các mạch kiến thức/kỹ năng sẵn có và hạn chế tối đa sự trùng lặp không cần thiết.
2. **Mục tiêu giáo dục (Mục II.1): Kế thừa năng lực tin học**
   * Năng lực AI được hình thành và phát triển trên cơ sở kế thừa trực tiếp năng lực tin học đã được quy định trong CT GDPT 2018.

---

## ĐIỀU 1. CHÍNH SÁCH TỪ VỰNG CHUẨN TUYỆT ĐỐI (ZERO-DEVIATION POLICY)

Tuyệt đối **KHÔNG** sử dụng thuật ngữ tự do, từ mượn ngoại lai tùy tiện, tiếng lóng công nghệ hoặc cách dịch chưa chuẩn hóa khi đã có thuật ngữ chính thức trong **Phụ lục Giải thích thuật ngữ** của QĐ 2422.

### Bảng chuyển đổi bắt buộc (Strict Word Mapping):
* ❌ *Không dùng:* "nhắc lệnh", "prompting tự do", "câu mồi" ➔ ✅ **Câu lệnh (prompt)**
* ❌ *Không dùng:* "AI bịa chuyện", "chém gió", "ảo tưởng mô hình" ➔ ✅ **Ảo giác AI (hallucination)**
* ❌ *Không dùng:* "độ lệch", "thành kiến máy móc", "sai số kỳ thị" ➔ ✅ **Thiên lệch (bias)**
* ❌ *Không dùng:* "video giả mạo", "clip ghép mặt", "fake video" ➔ ✅ **Nội dung giả mạo do AI tạo ra (deepfake)**
* ❌ *Không dùng:* "quá tải mô hình", "khớp quá mức" ➔ ✅ **Quá khớp (overfitting)**
* ❌ *Không dùng:* "AI sinh nội dung", "AI sinh lời" ➔ ✅ **AI tạo sinh (generative AI)**
* ❌ *Không dùng:* "RAG", "AI tra tài liệu ngoài" ➔ ✅ **Kĩ thuật sinh nội dung tăng cường bằng truy xuất (Retrieval-Augmented Generation – RAG)**
* ❌ *Không dùng:* "robot trò chuyện", "bot hội thoại" ➔ ✅ **Phần mềm hội thoại tự động (Chatbot)**
* ❌ *Không dùng:* "đại lý AI", "nhân viên AI ảo" ➔ ✅ **Tác nhân AI (AI agent)**
* ❌ *Không dùng:* "giấu danh tính", "xóa tên cá nhân" ➔ ✅ **Khử nhận dạng dữ liệu cá nhân**
* ❌ *Không dùng:* "đòi hỏi trách nhiệm", "báo cáo giải trình" ➔ ✅ **Trách nhiệm giải trình (Accountability)**
* ❌ *Không dùng:* "chuẩn đầu ra bài học", "mục tiêu chuyên đề" ➔ ✅ **Yêu cầu cần đạt (YCCĐ)**
* ❌ *Không dùng:* "mô hình ngôn ngữ", "LLM", "AI ngôn ngữ" ➔ ✅ **Mô hình ngôn ngữ lớn (Large Language Model – LLM)**
* ❌ *Không dùng:* "học máy truyền thống", "học từ nhãn" ➔ ✅ **Học có giám sát (supervised learning)**
* ❌ *Không dùng:* "AI tự học không nhãn" ➔ ✅ **Học không giám sát (unsupervised learning)**
* ❌ *Không dùng:* "AI thưởng phạt" ➔ ✅ **Học tăng cường (reinforcement learning)**
* ❌ *Không dùng:* "mạng thần kinh nhân tạo", "neural net" ➔ ✅ **Mạng nơ-ron nhân tạo (artificial neural network)**
* ❌ *Không dùng:* "nhận diện hình ảnh máy tính", "AI nhìn" ➔ ✅ **Thị giác máy tính (computer vision)**
* ❌ *Không dùng:* "xử lý tiếng nói/chữ viết", "NLP" ➔ ✅ **Xử lí ngôn ngữ tự nhiên (Natural Language Processing – NLP)**
* ❌ *Không dùng:* "vòng đời phần mềm AI" ➔ ✅ **Vòng đời hệ thống AI (AI system lifecycle)**
* ❌ *Không dùng:* "12 tiết tự chọn", "môn AI riêng biệt" ➔ ✅ **Các chuyên đề giáo dục AI bắt buộc với thời lượng 12 tiết/lớp/năm học dành cho nội dung cốt lõi**

---

## ĐIỀU 2. NGUYÊN TẮC PHÂN ĐỊNH 2 LUỒNG VÀ THẨM THẤU CHẤT LƯỢNG QUỐC TẾ Ở CẢ 36 TIẾT (DUAL-TRACK & QUALITY ASSURANCE)

Mọi văn bản chương trình, kế hoạch dạy học phải phân định minh bạch, không được nhập nhèm giữa 2 luồng nội dung, đồng thời thẩm thấu tinh hoa phương pháp quốc tế xuyên suốt cả 36 tiết:

### 1. Luồng 1 - Nội dung cốt lõi (12 CORE - Bắt buộc 100% học sinh):
* **Tên gọi chuẩn:** *"Các chuyên đề giáo dục AI bắt buộc với thời lượng 12 tiết/lớp/năm học dành cho nội dung cốt lõi"*.
* **Thời lượng:** Trọn vẹn trong **12 tiết/lớp/năm học**, bố trí trong kế hoạch giáo dục nhà trường và kế hoạch dạy học 2 buổi/ngày.
* **Mục tiêu pháp lý:** Phủ kín và đạt **100% Yêu cầu cần đạt cốt lõi (`VN-CORE`)** theo QĐ 2422. Mã YCCĐ đánh số tự nhiên thuần túy (`1, 2, 3...`), ví dụ: `6.A1.1`, `8.C2.1`, `10.C3.2`.
* **Thẩm thấu chất lượng quốc tế:** Tuyệt đối không dạy lý thuyết khô khan. 12 tiết cốt lõi phải áp dụng triệt để phương pháp sư phạm trải nghiệm (David Kolb), hoạt động không máy tính (Unplugged từ AI4K12) và các case study trực quan để học sinh đạt chuẩn Bộ một cách sâu sắc nhất.
* **Phạm vi đánh giá:** Là căn cứ duy nhất nếu thực hiện đánh giá diện rộng.

### 2. Luồng 2 - Nội dung mở rộng (24 EXPANDED - Đào sâu & Làm giàu):
* **Thời lượng & Hình thức:** Bố trí linh hoạt **24 tiết bổ sung ngoài 12 tiết cốt lõi** (nâng tổng thể khung chương trình cả năm lên 36 tiết); thông qua câu lạc bộ, dự án, chuyên đề tăng cường, ngoại khóa.
* **Nhiệm vụ pháp lý bắt buộc số 1:** Phải bao phủ và đạt **100% Yêu cầu cần đạt mở rộng (`VN-MR`)** có trong QĐ 2422 cho khối lớp đó. Mã YCCĐ bắt buộc có tiền tố **`MR`** kèm số thứ tự (`MR1, MR2...`), ví dụ: `6.C3.MR1`, `1.A2.MR1`. Tuyệt đối không được bỏ sót các mã `MR` của Bộ.
* **Nhiệm vụ số 2 (Đào sâu):** Luyện tập, thực hành củng cố các YCCĐ cốt lõi, nâng cao kỹ năng kiểm chứng và xử lý sự cố.
* **Nhiệm vụ số 3 (Làm giàu quốc tế - `INT-ENRICH`):** Mở rộng các dự án sáng tạo AI (AI Creation), kỹ năng công cụ thực nghiệm, bài toán liên môn và hướng nghiệp từ các chuẩn UNESCO, OECD, MIT, Raspberry Pi.
* **Ràng buộc đánh giá:** Không thay thế, không làm giảm yêu cầu cốt lõi; **tuyệt đối không sử dụng nội dung mở rộng làm căn cứ đánh giá bắt buộc đối với mọi học sinh**.

### 3. Hệ thống 3 nhãn định danh Outcome (Outcome Taxonomy):
Mọi mục tiêu và năng lực hình thành trong chương trình phải được dán nhãn nguồn gốc rõ ràng, không được trộn lẫn:
* **`VN-CORE`**: YCCĐ cốt lõi bắt buộc theo QĐ 2422 (phủ trọn vẹn trong 12 tiết Core).
* **`VN-MR`**: YCCĐ mở rộng chính thức ban hành tại QĐ 2422 (phủ trọn vẹn trong 24 tiết Expanded).
* **`INT-ENRICH`**: Mục tiêu/Năng lực làm giàu tham chiếu từ UNESCO, OECD, AI4K12, Singapore MOE. Nhãn này được **cài cắm trực tiếp vào các phần cụ thể** (nội dung bài, phiếu học tập, hoạt động thực hành) ở cả 36 tiết, không tạo thành luồng tiết riêng biệt.

### 4. Quy tắc kỹ thuật ghi mã YCCĐ bắt buộc:
* ❌ **Sai:** `6.A1.MR`, `1.C1.MR` (thiếu số thứ tự — không tra được trong QĐ 2422).
* ✅ **Đúng:** `6.A1.MR1`, `6.A1.MR2`, `1.C1.MR1`... (phải có số thứ tự cụ thể theo QĐ 2422).
* Mỗi mã YCCĐ (cốt lõi hoặc mở rộng) **chỉ gán tại tiết học chính** — tiết trực tiếp dạy và hình thành YCCĐ đó. **Không gán lại** tại tiết tổng kết, ôn tập hay đánh giá cuối kỳ dù nội dung có liên quan, vì gây trùng lặp và mờ hoá ranh giới.

### 5. Tiết Đánh giá và Tiết Triển lãm (Loại tiết đặc biệt):
* **Căn cứ:** Mục VI QĐ 2422 quy định đánh giá năng lực AI qua *"sản phẩm, dự án, báo cáo hoặc triển lãm học tập"*.
* Các tiết Đánh giá giữa kỳ / Tổng kết / Triển lãm là hình thức **hợp lệ theo QĐ 2422**, không thuộc luồng cốt lõi cũng không thuộc luồng mở rộng — đây là **tiết đánh giá quá trình** (Assessment).
* **Quy tắc ghi mã YCCĐ** cho các tiết này:
  * ✅ Ghi: `Mục VI QĐ 2422` (tiết đánh giá quá trình chính thức)
  * ✅ Để trống cột Mã YCCĐ (tiết triển lãm / báo cáo cuối kỳ)
  * ❌ **Không ghi:** `"Triển lãm MR"`, `"Tổng kết MR"`, `"Ôn tập MR"` — không phải mã YCCĐ hợp lệ, gây nhầm lẫn khi tra cứu.

---

## ĐIỀU 3. QUY CHUẨN MÃ HOÁ VÀ CẤU TRÚC 4 MẠCH NỘI DUNG

Mọi hoạt động và tài liệu biên soạn phải thuộc về 1 trong 4 mạch nội dung chuẩn:

1. **Mạch A. Tư duy lấy con người làm trung tâm (NLa):**
   * *A1:* Tính chủ động của con người
   * *A2:* AI vì sự tiến bộ của con người
   * *A3:* Công dân trong kỉ nguyên AI
2. **Mạch B. Đạo đức AI (NLb):**
   * *B1:* Các khía cạnh đạo đức của AI
   * *B2:* Sử dụng AI an toàn và có trách nhiệm
   * *B3:* Nguyên tắc đạo đức và trách nhiệm xã hội
3. **Mạch C. Các kĩ thuật và ứng dụng AI (NLc):**
   * *C1:* Đặc điểm chính của AI
   * *C2:* Ứng dụng AI trong học tập và cuộc sống
   * *C3:* Công nghệ AI
   * *C4:* Dữ liệu trong AI
   * *C5:* Kĩ thuật và thuật toán AI
4. **Mạch D. Thiết kế hệ thống AI (NLd):**
   * *D1:* Nhận diện và hình thành giải pháp
   * *D2:* Cấu trúc và tương tác, cải tiến hệ thống

* **Cấu trúc mã YCCĐ:** `[Lớp].[Mã chủ đề].[Số thứ tự]` (Số thứ tự chỉ để định danh, không thể hiện thứ tự ưu tiên hay độ khó).

---

## ĐIỀU 4. NGUYÊN TẮC BẮT BUỘC GẮN NEO YCCĐ VÀ ĐỐI CHIẾU NGUỒN TÂM LÝ PHÁT TRIỂN

Mọi quá trình xây dựng **Yêu cầu cần đạt đầu ra (YCCĐ)**, phân rã **kỹ năng nhỏ (micro-skills / micro-behaviors)**, và thiết kế **hoạt động trong từng tiết học** bắt buộc phải tuân thủ nghiêm ngặt 2 nguyên tắc song hành:

### 1. Gắn neo pháp lý YCCĐ (Traceability):
* **Bắt buộc:** Phải ghi rõ mã YCCĐ bảo trợ của khối lớp tương ứng theo QĐ 2422 (ví dụ: *"Đáp ứng YCCĐ 1.A1.1", "Đáp ứng YCCĐ 6.A1.3 và 6.B2.1"*).
* **Mục tiêu:** Mọi kỹ năng nhỏ bổ sung phải phục vụ trực tiếp việc làm sáng tỏ và đạt được YCCĐ chính thức của Bộ GD&ĐT, tuyệt đối không đưa thêm kiến thức vượt chuẩn ngoài khung làm quá tải học sinh.

### 2. Nguyên tắc bắt buộc đối chiếu Nguồn Tâm lý phát triển học sinh:
Toàn bộ chuyên gia, kiến trúc sư và AI tham gia thiết kế chương trình phải **luôn đối chiếu với Kho 32 nguồn tâm lý phát triển chuẩn hóa** (tại `04_Hoc_Lieu_Va_Tham_Khao/Tong_Hop_Nguon_Tai_Lieu_Tam_Ly_Phat_Trien_Hoc_Sinh.md`) ở cả 2 thời điểm sống còn:

* **Khi xây dựng YCCĐ đầu ra & phân rã hành vi (Micro-behaviors):**
  * Phải căn cứ vào các mốc phát triển nhận thức, ngôn ngữ và tâm lý – xã hội của lứa tuổi (Piaget, Erikson, Vygotsky ZPD, Kohlberg, CASEL, CDC, UNICEF).
  * Sử dụng thang Bloom với các **động từ hành vi quan sát và đo lường trực tiếp được trong lớp học** (thao tác tay, lời nói, cử chỉ, chọn thẻ, đối chiếu, thử nghiệm). Tuyệt đối cấm các từ ngữ trạng thái trừu tượng, vô hình (*"hiểu rằng", "nhận ra", "tỉnh táo", "ý thức"*).
  * **Triệt để tránh 2 thái cực sai lệch:**
    * ❌ **Không mầm non hóa:** Không hạ thấp năng lực của học sinh thời đại số bằng các hành vi thụ động, cơ học (chỉ nhắc vẹt, giơ tay đơn thuần, bắt chước máy móc).
    * ❌ **Không hàn lâm / học thuật hóa:** Không ép học sinh tiếp thu khái niệm hay thao tác tư duy vượt quá Vùng phát triển gần (ZPD).
* **Khi xây dựng Hoạt động trong tiết học (Lesson Activities / Kế hoạch bài dạy):**
  * Mọi hoạt động dạy học (Khởi động CE, Khám phá RO, Luyện tập AC, Vận dụng AE theo Kolb) phải phù hợp với dung lượng chú ý (attention span), khả năng thao tác thực tế và nhu cầu tương tác xã hội của học sinh theo từng độ tuổi.
  * Tích hợp hài hòa các năng lực xã hội – cảm xúc (SEL theo CASEL & OECD SSES) trong các hoạt động nhóm, thảo luận đạo đức và xử lý tình huống số.
  * Bảo đảm đúng thời lượng tiết học chuẩn theo từng cấp lớp (Lớp 1–2: 30–35 phút; Lớp 3–5: 35–40 phút; THCS–THPT: 45 phút) và luôn có phương án mô phỏng không dùng máy tính (Unplugged) tương thích với thể trạng lứa tuổi.

---

## ĐIỀU 4B. QUY TẮC GIỚI HẠN VÀ KHOANH VÙNG TÀI LIỆU THAM KHẢO CẤP TIỂU HỌC (GRADES 1–5 / 6–11 TUỔI)

Để ngăn ngừa triệt để hiện tượng **lệch tầng nhận thức** và **"xâm lấn THCS" (Secondary Creep)** — nguyên nhân gốc rễ khiến chương trình Lớp 4 và Lớp 5 bị quá tải và quá khó — mọi quá trình biên soạn, đối soát YCCĐ, Ma trận kỹ năng và Phân phối chương trình cấp Tiểu học bắt buộc phải tuân thủ nghiêm ngặt bảng giới hạn 3 cột dưới đây:

### 1. Bảng giới hạn chuẩn hóa nguồn tham khảo cấp Tiểu học (3 Cột Chuẩn):

| Tài liệu / Chương trình | Vị trí nội dung dành cho TIỂU HỌC (Grades 1–5 / 6–11 tuổi) | Điểm dừng nhận thức chuẩn cho Tiểu học |
| :--- | :--- | :--- |
| **Quyết định 2422/QĐ-BGDĐT** *(Bộ GD&ĐT)* | **Mục IV.1: Cấp Tiểu học (Lớp 1 – Lớp 5)**<br>Phủ trọn vẹn 4 mạch A, B, C, D của 5 khối lớp (trang 4–18 bản ký). | Nhận biết trực quan; hình thành thói quen đạo đức số; làm quen trải nghiệm máy học đơn giản; không viết mã giải thuật hàn lâm. |
| **Công văn 5588/BGDĐT-GDPT** *(Bộ GD&ĐT)* | **Mục II.1: Cấp Tiểu học**<br>Bố trí 12 tiết cốt lõi trong kế hoạch dạy học 2 buổi/ngày; lồng ghép linh hoạt; bảo đảm công bằng tiếp cận. | Lớp 1–2 tuyệt đối không ép dùng thiết bị cá nhân; ưu tiên hoạt động không máy tính (Unplugged); học tập qua trải nghiệm và trò chơi. |
| **CT GDPT 2018 Môn Tin học** *(Bộ GD&ĐT)* | **Môn Tin học Lớp 3, Lớp 4, Lớp 5**<br>Các chủ đề A, B, C, D, E, F môn Tin học cấp Tiểu học.<br>*(Lớp 1–2 chưa có môn Tin học chính khóa)*. | Kế thừa kỹ năng gõ phím, rê chuột, vẽ hình, tư duy phân loại dữ liệu đồ vật; không học lập trình cấu trúc phức tạp. |
| **AI4K12 — Five Big Ideas** *(AAAI & CSTA)* | **Band K–2** (Lớp 1 – 2, ~5–8 tuổi): Cảm nhận giác quan máy tính.<br>**Band 3–5** (Lớp 3 – 5, ~8–11 tuổi): Nhận diện quy luật dữ liệu và tương tác tự nhiên. | Dừng lại ở mức nhận diện mẫu (Pattern), phân loại tranh ảnh/âm thanh; tuyệt đối không học biểu diễn tri thức dạng đồ thị hay mạng ngữ nghĩa của Band 6–8. |
| **UNESCO AI Competency Framework (2024)** | **Level 1: Understand (Tiếp thu / Hiểu)**<br>Phát triển sự hiểu biết ban đầu về AI; kết nối thực tế đời sống; nhận biết giá trị và đạo đức cơ bản. | Nhận thức lấy con người làm trung tâm; hiểu AI học từ dữ liệu ví dụ; tuyệt đối không đưa các yêu cầu kỹ thuật của Level 2 (Apply) và Level 3 (Create) vào Tiểu học. |
| **UNICEF Policy Guidance on AI for Children (v2.0)** | Các yêu cầu cốt lõi phù hợp trẻ em: **Safety** (An toàn số), **Data Privacy** (Bảo vệ thông tin cá nhân), **Well-being** (Phát triển lành mạnh, chống nghiện màn hình). | Không nhập dữ liệu cá nhân (họ tên, ảnh riêng tư) vào hệ thống AI; thực hành quy tắc xin phép đồng thuận; bảo vệ an toàn thân thể và tinh thần. |
| **Experience AI** *(Google DeepMind & Raspberry Pi)* | **Khóa Discovering AI (8–12 tuổi / Lớp 3–5):**<br>Trục tiến trình nhận thức 5 bước:<br>$$\text{AI System} \rightarrow \text{Data} \rightarrow \text{Pattern} \rightarrow \text{Prediction} \rightarrow \text{Problem}$$ | Trải nghiệm trực quan: Thấy dữ liệu thiếu/sai thì máy đoán sai; tuyệt đối không đưa các bài Decision trees, Model cards, hay lab kỹ thuật của khóa Foundations of AI (11–14 tuổi) vào Tiểu học. |
| **Google Be Internet Awesome (BIA)** *(Google for Education)* | **Grades 2–5 (Lớp 2 – 5):**<br>3 trụ cột: What is AI, Digital Citizenship, Responsible Use. | Học cách nói câu lệnh rõ ý; phân biệt ảnh thật vs ảnh ghép vô lý; rèn luyện thói quen bảo mật thông tin và tôn trọng bạn bè. |
| **Google Applied Digital Skills** *(Discover AI in Daily Life)* | Các hoạt động trực quan cho Late Elementary (Lớp 4–5): **Quick, Draw!** (vẽ nét đoán hình), **AutoDraw** (gợi ý nét vẽ), **Google Translate** cơ bản. | Chơi mà học qua công cụ trực quan không cần tạo tài khoản; tuyệt đối không yêu cầu viết prompt lập trình hay phân tích bảng dữ liệu lớn. |
| **MIT Day of AI** *(MIT RAISE)* | Tài liệu dành riêng cho **Elementary (K–2 và 3–5):**<br>Hoạt động Unplugged, phân loại động vật bằng tranh thẻ, Teachable Machine mức cơ bản trực quan. | Đóng vai làm robot; thử nghiệm dữ liệu bằng tranh ảnh và vật thật; loại bỏ toàn bộ giáo trình của Middle School (Grades 6–8) và High School (Grades 9–12). |
| **Common Sense Education** *(AI Literacy Lessons)* | ❌ **LOẠI BỎ 100% KHỎI CẤP TIỂU HỌC**<br>*(Bộ giáo trình này thiết kế chính thức cho Grades 6–12, từ 11 đến 18 tuổi)*. | Tuyệt đối không trích dẫn hoặc sử dụng bất kỳ bài học nào của Common Sense Education cho Lớp 1–5 để tránh làm "già hóa" chương trình. |
| **Singapore MOE & OECD** | **Singapore MOE Primary AI (P3–P5: AI for Fun / AI for Kids P4)**: Chống ỷ lại nhận thức.<br>**OECD**: Năng lực tự chủ số mức cơ bản (Engage). | Giữ vững triết lý: "AI hỗ trợ - Em tự suy nghĩ"; tự giác làm bài tập độc lập; không để máy làm thay; không áp dụng chuẩn khảo sát PISA 2029 (15 tuổi). |

### 2. Danh mục các nội dung BẮT BUỘC LOẠI BỎ khỏi cấp Tiểu học (Blacklist):
1. **Thuật toán & Kỹ thuật máy học chuyên sâu:** Cây quyết định (Decision Trees), Mạng nơ-ron đa tầng, Ma trận nhầm lẫn (Confusion Matrix), Quy trình Train/Test/Validation công nghiệp.
2. **Kỹ thuật Prompt nâng cao:** Prompt đa tầng phức tạp (Role-based, Chain-of-thought, Few-shot chuyên sâu) đòi hỏi tư duy trừu tượng cấp 2. Tiểu học chỉ dừng ở mức: Nêu rõ yêu cầu, đủ ý, lịch thiệp.
3. **Thẻ mô hình (Model Cards) & Báo cáo kỹ thuật:** Đòi hỏi đọc hiểu các chỉ số thống kê, giới hạn kỹ thuật và độ lệch thuật toán đa biến.
4. **Phân tích thiên lệch đa chiều (Systemic Bias):** Tiểu học chỉ dừng ở nhận biết trực quan: Dữ liệu thiếu/lệch thì máy đoán sai (ví dụ: máy chỉ thấy táo đỏ nên không nhận ra táo xanh). Không bàn luận các vấn đề thiên lệch chính trị - xã hội phức tạp của THCS/THPT.

---

## ĐIỀU 5. TUÂN THỦ TIẾN TRÌNH SƯ PHẠM, THỜI LƯỢNG TIẾT HỌC VÀ HẠ TẦNG THEO TỪNG CẤP HỌC

Quy định thời lượng chuẩn của từng tiết học và tiến trình sư phạm bắt buộc phải tuân thủ nghiêm ngặt theo đặc điểm tâm sinh lý lứa tuổi và quy định pháp lý của Bộ Giáo dục và Đào tạo:

### 1. Cấp Tiểu học (Lớp 1 – 5):
* **Thời lượng tiết học chuẩn:**
  * **Lớp 1 và Lớp 2:** Mỗi tiết học kéo dài từ **30 đến 35 phút**.
  * **Lớp 3, Lớp 4 và Lớp 5:** Mỗi tiết học kéo dài từ **35 đến 40 phút** (chuẩn phổ biến nhất là **35 phút** cho mỗi tiết dạy học trong kế hoạch 2 buổi/ngày).
* **Đặc trưng sư phạm:** Trực quan – Trải nghiệm ban đầu. Ưu tiên kể chuyện, tranh thẻ, trò chơi, đóng vai, xử lý tình huống đơn giản.
* **Hạ tầng:** Ưu tiên hoạt động không cần tạo tài khoản, không lệ thuộc thiết bị cá nhân; dùng thiết bị chung dưới sự giám sát; chuẩn bị sẵn phương án mô phỏng thủ công không dùng máy tính (Unplugged) khi thiếu thiết bị.

### 2. Cấp THCS (Lớp 6 – 9):
* **Thời lượng tiết học chuẩn:**
  * Mỗi tiết học tiêu chuẩn kéo dài **45 phút**. 
  * Mỗi buổi học thường gồm 4 đến 5 tiết, có thời gian nghỉ giữa giờ (ra chơi) khoảng 15–20 phút giữa các tiết.
* **Đặc trưng sư phạm:** Logic – Khoa học – Kiểm chứng. Chú trọng điều tra, đối chiếu nguồn tin, nhận diện thiên lệch và deepfake, tạo sản phẩm số đơn giản.
* **Bắt buộc lưu vết minh chứng:** Học sinh phải ghi nhật ký câu lệnh (prompt log), lưu nguồn dữ liệu và kết quả thử nghiệm để thực hiện trách nhiệm giải trình và liêm chính học thuật.

### 3. Cấp THPT (Lớp 10 – 12):
* **Thời lượng tiết học chuẩn:** Tiết học tiêu chuẩn **45 phút**.
* **Đặc trưng sư phạm:** Phân tích – Phản biện – Thiết kế giải pháp. Nghiên cứu trường hợp (case study), tranh biện đạo đức/pháp lý, thiết kế câu lệnh chuyên sâu (Role-based, Chain-of-thought, Few-shot), kiểm thử và tối ưu mô hình, định hướng nghề nghiệp.

---

## ĐIỀU 6. QUY TẮC THAM CHIẾU QUỐC TẾ & ĐỊNH VỊ NGÂN HÀNG HOẠT ĐỘNG SƯ PHẠM

Hệ thống tài liệu quốc tế và tài liệu học thuật trong dự án được tổ chức tại `02_Tai_Lieu_Quoc_Te/` và `04_Hoc_Lieu_Va_Tham_Khao/`. Khi nghiên cứu và áp dụng, bắt buộc tuân thủ 3 nguyên tắc sau:

### 1. Phân định vai trò Khung tham chiếu và Benchmark chiều sâu:
* **UNESCO AI Competency Framework (`02_Tai_Lieu_Quoc_Te/UNESCO/`):** Là **Khung tham chiếu quốc tế trung tâm** định hướng 4 chiều năng lực và 3 mức độ thành thạo (Understand – Apply – Create).
* **AI4K12, OECD, Singapore MOE (`02_Tai_Lieu_Quoc_Te/AI4K12/`, `Khac/`):** Là **Benchmark chiều sâu và thực tiễn sư phạm** (5 Big Ideas, Unplugged activities, case study chống thiên lệch, rèn luyện tư duy tự chủ, chống ỷ lại nhận thức công nghệ).
* **Nguyên tắc đồng hóa:** Phải chuyển đổi toàn bộ khái niệm nước ngoài về đúng 4 mạch nội dung (A, B, C, D) và 26 thuật ngữ chuẩn của QĐ 2422. Không áp đặt nguyên bản làm biến dạng YCCĐ của Bộ GD&ĐT.

### 2. Quy chuẩn định vị tệp Ngân hàng hoạt động sư phạm (`04_Hoc_Lieu_Va_Tham_Khao/`):
* Tệp **`Ngan_Hang_Hoat_Dong_Va_Kich_Ban_Su_Pham_Tham_Khao.xlsx`** (tiền thân là `Khung_Chuong_Trinh_AI_TieuHoc_THCS.xlsx`) là một bản dự thảo nghiên cứu/đề xuất học thuật nội bộ dựa trên UNESCO và 6 nguồn quốc tế.
* **Những điều NGHIÊM CẤM:**
  * ❌ Tuyệt đối **KHÔNG dùng tệp này làm Khung chương trình** hay căn cứ xác định YCCĐ (vì thiếu hơn 50% số lượng YCCĐ của Bộ, mã số không chuẩn và không có phân định 2 luồng Cốt lõi/Mở rộng).
* **Phạm vi sử dụng DUY NHẤT:**
  * ✅ **Chuyên dùng làm "Ngân hàng ý tưởng hoạt động trải nghiệm & kịch bản sư phạm tham khảo" (Activity Bank)**: Khai thác các kịch bản trò chơi Unplugged không máy tính (theo CV 5588), hoạt động khởi động 7–10 phút (pha CE của Kolb), thử thách vận dụng (pha AE của Kolb), và các tình huống đạo đức/an toàn số gần gũi lứa tuổi khi bắt tay vào soạn Kế hoạch bài dạy chi tiết (Giáo án) hoặc phiếu học tập.

### 3. Quy chuẩn tham chiếu Tâm lý phát triển học sinh (7–11 tuổi Tiểu học và 12–15 tuổi THCS):
* **Căn cứ tài liệu:** Tệp `04_Hoc_Lieu_Va_Tham_Khao/Tong_Hop_Nguon_Tai_Lieu_Tam_Ly_Phat_Trien_Hoc_Sinh.md` là kho tư liệu chuẩn hóa gồm 32 nguồn thuộc 5 nhóm:
  * **Nhóm A:** Tổ chức quốc tế & chính phủ uy tín cao nhất (CDC, WHO, UNICEF, APA, NICHD, AAP, UNESCO, OECD).
  * **Nhóm B:** Khung lý thuyết nền tảng (Piaget, Erikson, Vygotsky ZPD, James Marcia, Kohlberg).
  * **Nhóm C:** Khung SEL / kỹ năng sống chuyên biệt (CASEL K-5 & 6-8, Second Step, WHO Life Skills, UNESCO LSCE).
  * **Nhóm D:** Cơ sở dữ liệu học thuật & tạp chí bình duyệt (PubMed, APA PsycNet, ERIC, Journal of Research on Adolescence, Child Development, Developmental Psychology).
  * **Nhóm E:** Nguồn bối cảnh Việt Nam (UNICEF Việt Nam, Chương trình GDPT 2018 Bộ GD&ĐT, Viện Tâm lý học).
* **Nguyên tắc áp dụng bắt buộc:**
  * Mọi phân rã hành vi học sinh (micro-behaviors), kịch bản sư phạm, câu hỏi và mức độ tư duy Bloom phải đối chiếu nghiêm ngặt với các mốc phát triển nhận thức – xã hội – cảm xúc của lứa tuổi theo các nguồn này.
  * **Tuyệt đối tránh 2 thái cực sai lệch:**
    * ❌ **Mầm non hóa:** Thiết kế hành vi quá đơn giản, thụ động cơ học (chỉ giơ tay, nhắc vẹt, vỗ tay) làm đánh giá thấp năng lực của trẻ thời đại số.
    * ❌ **Hàn lâm/Học thuật hóa:** Đưa ra các khái niệm, yêu cầu tư duy trừu tượng vượt quá vùng phát triển gần (ZPD) của lứa tuổi.
  * Ưu tiên trích dẫn nhóm A và D khi bảo vệ học thuật; áp dụng nhóm C cho hoạt động thực hành; và luôn đối chiếu nhóm E để chuẩn hóa theo thực tiễn giáo dục Việt Nam.

### 4. Quy chuẩn Bắt buộc Đối soát Kho Học liệu AI Quốc tế Chuẩn mực & Chống Bịa Nguồn (Strict Grounding Policy):
* **Căn cứ tài liệu:** Tệp `02_Tai_Lieu_Quoc_Te/DANH_MUC_NGUON_TAI_LIEU_QUOC_TE.md` và `04_Hoc_Lieu_Va_Tham_Khao/Tong_Hop_Nguon_Hoc_Lieu_AI_Quoc_Te_Google_MIT_CommonSense.md` là kho học liệu thực nghiệm và kịch bản sư phạm quốc tế chuẩn mực gồm 3 nhóm nguồn chính thức:
  * **Nhóm I. Khung chương trình & Học liệu cho học sinh (K-12 Curriculum):**
    1. **Experience AI (Google DeepMind + Raspberry Pi Foundation):** Khóa *Discovering AI* (8–12 tuổi) và 2 Module chuyên sâu *Understanding AI / Solving Problems with AI* (11–14 tuổi) kèm *Foundations of AI* (6 bài học thực hành huấn luyện mô hình, Bias lab). [experience-ai.org/en/units](https://experience-ai.org/en/units)
    2. **AI Literacy Lessons for Grades 6–12 (Common Sense Education):** Đạo đức công nghệ, an toàn dữ liệu, nhận diện tin giả/deepfake, liêm chính học thuật. [commonsense.org/education/collections/ai-literacy-lessons-for-grades-6-12](https://www.commonsense.org/education/collections/ai-literacy-lessons-for-grades-6-12)
    3. **Day of AI Curriculum Resources (MIT RAISE + i2 Learning):** Kịch bản trải nghiệm, hoạt động không máy tính (Unplugged), dự án sáng tạo AI (Lưu trữ tại `02_Tai_Lieu_Quoc_Te/MIT_Day_of_AI/`). [dayofai.org/curriculum-resources](https://dayofai.org/curriculum-resources)
    4. **AI Quests (Google Research + Stanford University):** Game-based learning giải quyết vấn đề (Nhiệm vụ $\rightarrow$ Vấn đề $\rightarrow$ Dữ liệu $\rightarrow$ AI $\rightarrow$ Ra quyết định $\rightarrow$ Phản tư). [grow.google/intl/europe/ai-skills](https://grow.google/intl/europe/ai-skills/)
    5. **Teaching Responsible Use of AI (Google for Education):** Khung 5 nguyên tắc đạo đức & an toàn số (*Technology not human, Empower not replace, Critically evaluate, Detect suspicious content, Data privacy*). [edu.google.com/ai/education](https://edu.google.com/ai/education/)
  * **Nhóm II. Đào tạo giáo viên (Teacher Training):**
    6. **Google AI Educator Series (Google + ISTE / ASCD):** Khóa micro-learning 15 phút về nền tảng, thiết kế sư phạm và đánh giá. [edu.google.com/learning-center/google-ai-educator-series](https://edu.google.com/learning-center/google-ai-educator-series/)
    7. **Generative AI for Educators with Gemini (Google + MIT RAISE):** Kỹ thuật câu lệnh (Prompting), tạo học liệu phân hóa, kiểm soát đạo đức. [grow.google/intl/europe/ai-skills](https://grow.google/intl/europe/ai-skills/)
  * **Nhóm III. Khung tham chiếu chuẩn & Chính sách quốc gia:**
    8. **UNESCO AI Competency Framework for Students:** 4 chiều năng lực x 3 mức độ thành thạo (`02_Tai_Lieu_Quoc_Te/UNESCO/`).
    9. **AI4K12 Five Big Ideas in AI (AAAI + CSTA + NSF):** Tiến trình 5 Big Ideas theo 4 dải tuổi (`02_Tai_Lieu_Quoc_Te/AI4K12/`).
    10. **OECD Learning Compass 2030 & Singapore MOE NDLP:** Năng lực tự chủ số (Digital Agency), chống ỷ lại nhận thức (Cognitive Offloading), an toàn trẻ em và Cyber Wellness (`02_Tai_Lieu_Quoc_Te/OECD_va_Singapore_MOE/`).
* **Nguyên tắc Chống Bịa Nguồn & Đảm bảo Tính Truy xuất (Strict Grounding & Anti-Hallucination):**
  * Tuyệt đối **KHÔNG trích dẫn nguồn chung chung, mơ hồ hoặc tự ý đưa vào các nguồn không nằm trong danh mục trên**.
  * Cột Chuẩn đầu ra tham chiếu nguồn quốc tế (Cột 5 trong SP1) bắt buộc phải ghi rõ tên chương trình và module/bài học tương ứng (ví dụ: *Google DeepMind - Experience AI: Discovering AI*, *MIT Day of AI: Unplugged Activity*, *Common Sense Education: AI Literacy (dành cho THCS)*).
  * Mọi tài liệu tham khảo phải được truy xuất trực tiếp từ các thư mục lưu trữ thực tế tại `02_Tai_Lieu_Quoc_Te/` và `04_Hoc_Lieu_Va_Tham_Khao/`. Tuân thủ nghiêm ngặt bảng giới hạn cấp học tại Điều 4B.

---

## ĐIỀU 6B. QUY CHUẨN NGHIỆM THU SẢN PHẨM 1 (KHUNG YCCĐ & NĂNG LỰC ĐẦU RA): BẢN ĐỒ ĐỊNH MỨC K-12, GIAO THỨC KHÓA CHUẨN LỨA TUỔI (HUMAN LOCK) VÀ ĐỊNH DẠNG ĐẦU RA BẮT BUỘC

Sản phẩm 1 (Khung Yêu cầu cần đạt và Năng lực đầu ra) là viên gạch nền móng pháp lý và chuyên môn cao nhất định hình toàn bộ các sản phẩm tiếp theo (PPCT, Kế hoạch bài dạy, Hoạt động học tập, Đánh giá). Mọi tài liệu thuộc Sản phẩm 1 bắt buộc phải tuân thủ nghiêm ngặt 4 quy chuẩn bất biến sau:

### 1. Bản đồ định mức số lượng YCCĐ bất biến toàn cấp K-12 (284 YCCĐ chuẩn QĐ 2422):
Tuyệt đối không được tự ý thêm bớt, chia nhỏ hay gộp mã YCCĐ làm biến dạng số lượng chuẩn quốc gia do Bộ GD&ĐT ban hành tại Mục IV QĐ 2422. Số lượng mã YCCĐ chính thức của từng khối lớp được ấn định bất biến như sau:
* **Cấp Tiểu học (Lớp 1 – 5): Đúng 123 YCCĐ** (80 Cốt lõi + 43 Mở rộng)
  * Lớp 1: **21 YCCĐ** (17 Cốt lõi + 4 Mở rộng)
  * Lớp 2: **29 YCCĐ** (17 Cốt lõi + 12 Mở rộng)
  * Lớp 3: **32 YCCĐ** (21 Cốt lõi + 11 Mở rộng)
  * Lớp 4: **17 YCCĐ** (10 Cốt lõi + 7 Mở rộng)
  * Lớp 5: **24 YCCĐ** (15 Cốt lõi + 9 Mở rộng)
* **Cấp THCS (Lớp 6 – 9): Đúng 88 YCCĐ** (53 Cốt lõi + 35 Mở rộng)
  * Lớp 6: **19 YCCĐ** (12 Cốt lõi + 7 Mở rộng)
  * Lớp 7: **21 YCCĐ** (12 Cốt lõi + 9 Mở rộng)
  * Lớp 8: **23 YCCĐ** (14 Cốt lõi + 9 Mở rộng)
  * Lớp 9: **25 YCCĐ** (15 Cốt lõi + 10 Mở rộng)
* **Cấp THPT (Lớp 10 – 12): Đúng 73 YCCĐ** (48 Cốt lõi + 25 Mở rộng)
  * Lớp 10: **24 YCCĐ** (16 Cốt lõi + 8 Mở rộng)
  * Lớp 11: **26 YCCĐ** (17 Cốt lõi + 9 Mở rộng)
  * Lớp 12: **23 YCCĐ** (15 Cốt lõi + 8 Mở rộng)
* **Tổng toàn bộ 12 khối lớp K-12:** Chuẩn xác **284 YCCĐ** (181 Cốt lõi + 103 Mở rộng).

### 2. Giao thức Khóa chuẩn Con người (Human Lock Protocol) & Bộ từ vựng cấm theo lứa tuổi:
Nhằm triệt tiêu tận gốc 2 thái cực sai lệch (Mầm non hóa và Hàn lâm hóa), mọi diễn đạt YCCĐ và chuẩn đầu ra phải qua bộ lọc 6 nguyên tắc kiểm định:
1. **Không gán trách nhiệm pháp lý cho học sinh phổ thông (đặc biệt Tiểu học):**
   * ❌ *Cấm:* "chịu trách nhiệm pháp lý", "ràng buộc trách nhiệm hình sự/dân sự".
   * ✅ *Chuẩn hóa:* "con người chịu trách nhiệm cuối cùng về mọi quyết định hoặc kết quả do AI tạo ra; không phó mặc hay đổ lỗi cho máy tính."
2. **Tuyệt đối tránh ngôn từ khẩu hiệu, cực đoan hoặc thần thánh hóa:**
   * ❌ *Cấm:* "3 phẩm chất độc quyền của con người", "năng lực độc tôn".
   * ✅ *Chuẩn hóa:* "những năng lực con người giữ vai trò trung tâm (sáng tạo, thấu cảm, phán đoán đạo đức)".
   * ❌ *Cấm:* "kiên quyết bài trừ".
   * ✅ *Chuẩn hóa:* "hình thành thói quen sử dụng chừng mực, tránh lạm dụng, không chia sẻ bừa bãi và không tin tưởng tuyệt đối vào máy".
3. **Không tuyệt đối hóa ưu thế giữa người và máy:**
   * ❌ *Cấm:* Khẳng định "con người luôn nhanh/chính xác hơn AI trong mọi việc".
   * ✅ *Chuẩn hóa:* Nhận biết AI xử lý dữ liệu lớn tốc độ cao, nhưng con người giữ vai trò kiểm chứng, định hướng và quyết định.
   * Tương tác dữ liệu với AI phải có tính điều kiện: "dữ liệu có thể được ghi nhận/sử dụng" thay vì khẳng định luôn luôn.
4. **Không học thuật hóa / dùng thuật ngữ kỹ sư AI đối với học sinh Tiểu học:**
   * ❌ *Cấm:* "kiểm thử đối kháng" (adversarial testing) ➔ ✅ *Thay bằng:* "kiểm tra kết quả trên nhiều trường hợp/nhóm đối tượng khác nhau".
   * ❌ *Cấm:* "nguyên lý học liên tục" (continual learning) ➔ ✅ *Thay bằng:* "hệ thống AI có thể được cải tiến khi dữ liệu được bổ sung, cập nhật và hệ thống được huấn luyện phù hợp".
   * ❌ *Cấm:* Khẳng định chắc chắn "tái huấn luyện giúp nâng cao độ chính xác" ➔ ✅ *Thay bằng:* "thực hành tái huấn luyện (Retrain) và kiểm tra xem kết quả có cải thiện hay không".
   * ❌ *Cấm:* "thao tác thành thạo", "đo lường độ tin cậy" ➔ ✅ *Thay bằng:* "thực hiện thao tác cơ bản", "quan sát điểm số tin cậy (confidence score) nếu công cụ hiển thị".
5. **Tiết chế mức độ làm chủ theo vùng phát triển nhận thức (ZPD):**
   * Lớp 3: Bỏ các từ đao to búa lớn như "tất yếu / vô hiệu" ➔ thay bằng "cần thiết / mất tác dụng".
   * Lớp 4 – 5: Bỏ chuẩn "tự chủ hoàn toàn / nắm vững vòng đời hệ thống AI" ➔ thay bằng "mô tả được ở mức độ đơn giản 4 bước cơ bản của chu trình huấn luyện AI".

### 3. Quy chuẩn 2 định dạng đầu ra bắt buộc (Dual-Format Delivery):
Mọi khối lớp khi xuất Sản phẩm 1 bắt buộc phải có đủ 2 định dạng độc lập nhưng tương thích 1-1 về mặt ngữ nghĩa:
* **Bản Đầy đủ (Full Version):**
  * Thiết kế bảng **5 cột**, khổ giấy **A4 Landscape (Nằm ngang)**.
  * Cấu trúc: STT | Mã YCCĐ | Mạch nội dung & Chủ đề con (QĐ 2422) | Yêu cầu cần đạt Chuẩn Quốc gia (Bộ GD&ĐT) | Chuẩn đầu ra tham chiếu Đa nguồn Quốc tế (UNESCO, OECD, Singapore MOE, AI4K12, Google DeepMind).
  * Mục đích: Dùng cho thẩm định học thuật, bảo vệ trước Hội đồng chuyên môn và truy xuất nguồn gốc (Traceability 3 tầng).
* **Bản Rút gọn (Compact Version):**
  * Thiết kế bảng **4 cột**, khổ giấy **A4 Portrait (Đứng)**.
  * Cấu trúc: STT | Mạch năng lực | Chủ đề con | YCCĐ (Chuẩn đầu ra năng lực súc tích).
  * Mục đích: Tinh gọn các chú giải nguồn, phục vụ trực tiếp cho giáo viên xây dựng Kế hoạch bài dạy (Giáo án) và Phân phối chương trình giảng dạy thực tế.
* **Bộ tệp bàn giao chuẩn cấp học:**
  * Tệp riêng cho từng khối lớp: `SP1_Khung_YCCD_AI_Lop{X}_Day_Du.[docx/md]` và `SP1_Khung_YCCD_AI_Lop{X}_Rut_Gon.[docx/md]`.
  * Tệp Master tổng hợp toàn cấp: `SP1_Khung_YCCD_AI_[CapHoc]_Day_Du.[docx/md]` và `SP1_Khung_YCCD_AI_[CapHoc]_Rut_Gon.[docx/md]`.

### 4. Quy trình Tự kiểm định tiền xuất bản (Pre-flight Audit Gate):
Trước khi bàn giao Sản phẩm 1, hệ thống bắt buộc kích hoạt script kiểm tra tự động đạt 100% qua 3 cổng:
* **Gate 1:** Kiểm đếm số hàng bảng = $100\%$ số lượng YCCĐ chính thức của QĐ 2422.
* **Gate 2:** Regex quét sạch toàn bộ danh mục từ cấm theo lứa tuổi.
* **Gate 3:** Đối soát độ nhất quán 1-1 giữa tệp `.md` và tệp `.docx`.

---

## ĐIỀU 7. QUY LUẬT XÂY DỰNG PHÂN PHỐI CHƯƠNG TRÌNH: PHỦ ĐỦ 4 MẠCH & TIẾN TRÌNH XOẮN ỐC

Khi chuyển hoá từ Khung nội dung tĩnh của QĐ 2422 sang Kế hoạch dạy học / Phân phối chương trình (PPCT) chi tiết theo tuần/tiết (chuẩn Công văn 5512/BGDĐT-GDTrH và 2345/BGDĐT-GDTH), bắt buộc phải tuân thủ 4 nguyên tắc kỹ thuật sau:

### 1. Nguyên tắc phủ đủ 4 mạch nội dung trong từng khối lớp:
* Trong bất kỳ khối lớp nào từ Lớp 1 đến Lớp 12, bản PPCT (cả khung 12 tiết bắt buộc và khung 36 tiết) **bắt buộc phải có sự hiện diện đầy đủ, cân đối của cả 4 mạch**: Mạch A (NLa), Mạch B (NLb), Mạch C (NLc) và Mạch D (NLd).
* Tuyệt đối không để xảy ra tình trạng thiên lệch (ví dụ: lớp chỉ dạy kỹ thuật, lớp chỉ dạy đạo đức).
* **Nguyên tắc phân bổ tiết theo từng mạch:**
  * Số tiết phân bổ cho mỗi mạch (A, B, C, D) **không cố định** mà phụ thuộc vào số lượng YCCĐ thực tế của từng mạch tại từng khối lớp cụ thể theo QĐ 2422.
  * Quy tắc bắt buộc duy nhất: **Cả 4 mạch đều phải có sự hiện diện** trong khung 12 tiết cốt lõi và khung 36 tiết toàn diện — không được bỏ trắng bất kỳ mạch nào.
  * Tổng thời lượng giữ nguyên: **12 tiết cốt lõi** và **36 tiết toàn diện** (bao gồm cả tiết đánh giá định kỳ).

### 2. Nguyên tắc phát triển năng lực xoắn ốc (Spiral Progression) từ Lớp 1 đến Lớp 9:
* Các khái niệm và năng lực nền tảng (*Quyền kiểm soát của con người, Dữ liệu cá nhân, Bản chất máy học, Sửa sai cho mô hình*) được lặp lại ở các lớp trên theo hình xoắn ốc với độ sâu nhận thức, tính tự chủ và độ phức tạp kỹ thuật tăng dần:
  * **Lớp 1 – 2 (Trực quan, nhận biết):** Cảm xúc người - máy, an toàn sơ khai, bật/tắt thiết bị, máy học từ ví dụ đơn giản.
  * **Lớp 3 – 5 (Quy tắc, tự chủ nền tảng):** Khi nào nên dùng AI, phân biệt máy học vs luật If-Then, dữ liệu tốt/xấu, bảo vệ thông tin cá nhân.
  * **Lớp 6 – 7 (Logic, khoa học, kiểm chứng):** Kiến trúc Dữ liệu - Thuật toán - Mô hình, viết câu lệnh có cấu trúc, phòng chống deepfake, lưu prompt log, huấn luyện mô hình trực quan.
  * **Lớp 8 – 9 (Phản biện, tự chủ, tối ưu):** Phản biện thiên lệch thuật toán, phòng chống thao túng, kiểm thử đối kháng, trách nhiệm giải trình, dự án giải quyết vấn đề thực tế.

### 3. Nguyên tắc tích hợp đồng thời các năng lực (Mục III.3 QĐ 2422):
* Bốn thành phần năng lực không được tách rời thành các khối kiến thức độc lập mà phải được **huy động đồng thời trong các bài học và dự án**.
* Khuyến khích thiết kế các bài học tích hợp: Học sinh vừa rèn luyện thao tác kỹ thuật (Mạch C), vừa phân tích dữ liệu bài toán (Mạch D), vừa gắn với ý thức con người làm chủ (Mạch A) và tuân thủ bản quyền, an toàn số (Mạch B).

### 4. Quy tắc bắt buộc Tự kiểm định QA/QC & Gửi kèm Báo cáo (Skill `ppct_qaqc_auditor`):
* Sau **mỗi lần hoàn thành bất kỳ sản phẩm nào** (Khung nội dung YCCĐ SP1, PPCT 36 tiết SP2, Kế hoạch bài dạy SP3, Học liệu/Rubric SP4 hay bất kỳ khối lớp nào), hệ thống **BẮT BUỘC PHẢI CHẠY QUY TRÌNH KIỂM ĐỊNH THỰC TẾ** qua 8 trụ cột chất lượng (sử dụng script kiểm đếm và đối soát văn bản).
* **BẮT BUỘC GỬI KÈM BÁO CÁO:** Khi xuất và bàn giao kết quả, **bắt buộc phải gửi kèm bản "Báo cáo Kết quả Kiểm định Chất lượng (QA/QC Audit Report)"** chi tiết điểm số từng tiêu chí ngay trong phản hồi cho người dùng.
* **NGHIÊM CẤM:** Tuyệt đối không được bàn giao sản phẩm suông, không được "nói bằng miệng", và không được bỏ qua bước kiểm định độc lập. Mọi sản phẩm chỉ được coi là hoàn thành khi đã có biên bản QA/QC phê duyệt đạt chuẩn.

---

## ĐIỀU 8. QUY TRÌNH THIẾT KẾ TIẾT HỌC THEO CHU TRÌNH HỌC TẬP TRẢI NGHIỆM DAVID KOLB (KOLB'S EXPERIENTIAL LEARNING CYCLE)

Mọi kế hoạch bài dạy (giáo án), kịch bản chuyên đề 12 tiết cốt lõi hoặc nội dung mở rộng khi xây dựng cho từng tiết học đều phải tuân thủ nghiêm ngặt **Chu trình học tập trải nghiệm 4 giai đoạn khép kín của David Kolb** và tương thích cấu trúc bài dạy chuẩn của Bộ GD&ĐT (Công văn 5512/BGDĐT-GDTrH đối với THCS và Công văn 2345/BGDĐT-GDTH đối với Tiểu học):

### 1. Cấu trúc 4 giai đoạn chuẩn tương ứng theo thời lượng từng cấp học:

* **KHUNG THỜI LƯỢNG CHUẨN CẤP THCS (45 PHÚT):**
  1. *Giai đoạn 1: Trải nghiệm cụ thể (CE):* **7 – 10 phút** (Khởi động / Trải nghiệm kích hoạt).
  2. *Giai đoạn 2: Quan sát & Phản tư (RO):* **8 – 10 phút** (Khảo sát / Phân tích hiện tượng).
  3. *Giai đoạn 3: Khái quát hóa trừu tượng (AC):* **10 – 12 phút** (Hình thành kiến thức / Đúc kết quy luật 26 thuật ngữ).
  4. *Giai đoạn 4: Thử nghiệm tích cực (AE):* **12 – 15 phút** (Luyện tập & Vận dụng bối cảnh mới / Prompt log).

* **KHUNG THỜI LƯỢNG CHUẨN TIỂU HỌC LỚP 3, 4, 5 (35 PHÚT):**
  1. *Giai đoạn 1: Trải nghiệm cụ thể (CE):* **5 – 7 phút** (Trò chơi trực quan / Kích hoạt vấn đề).
  2. *Giai đoạn 2: Quan sát & Phản tư (RO):* **6 – 8 phút** (Học sinh trao đổi, chỉ ra điểm khác biệt).
  3. *Giai đoạn 3: Khái quát hóa trừu tượng (AC):* **8 – 10 phút** (Giáo viên chốt quy tắc đơn giản, dễ nhớ).
  4. *Giai đoạn 4: Thử nghiệm tích cực (AE):* **10 – 12 phút** (Thực hành phiếu bài tập / Unplugged hoặc máy tính).

* **KHUNG THỜI LƯỢNG CHUẨN TIỂU HỌC LỚP 1, 2 (30 – 35 PHÚT):**
  1. *Giai đoạn 1: Trải nghiệm cụ thể (CE):* **5 – 6 phút** (Xem tranh, nghe kể chuyện, trò chơi thể chất nhẹ nhàng).
  2. *Giai đoạn 2: Quan sát & Phản tư (RO):* **5 – 7 phút** (Hỏi đáp nhanh, giơ thẻ Đúng/Sai).
  3. *Giai đoạn 3: Khái quát hóa trừu tượng (AC):* **7 – 8 phút** (Quy tắc bằng thơ/vè hoặc hình vẽ biểu tượng).
  4. *Giai đoạn 4: Thử nghiệm tích cực (AE):* **8 – 10 phút** (Dán thẻ, tô màu, ghép tranh Unplugged).

### 2. Bộ câu hỏi dẫn dắt chuyển pha (Scaffolding Framework):
* **Nhóm RO (What?):** *"Em vừa quan sát thấy điều gì? Kết quả thực tế khác gì so với dự đoán ban đầu?"*
* **Nhóm AC (So what?):** *"Điều này phản ánh nguyên lý/quy luật gì của AI? Công thức hay quy tắc nào giúp giải thích hoặc khắc phục hiện tượng này?"*
* **Nhóm AE (Now what?):** *"Nếu gặp tình huống mới trong thực tế, em sẽ áp dụng quy tắc này như thế nào để đạt kết quả tối ưu?"*

### 3. Ba nguyên tắc bất biến khi triển khai:
1. **Không rơi vào bẫy "Trải nghiệm rỗng" (Activity without Reflection):** Trải nghiệm (CE) chỉ chiếm 7–10 phút để tạo vấn đề, không chiếm toàn bộ thời gian của tiết học.
2. **Không giải thích thay ở bước Phản tư (RO):** Phải trao quyền phát hiện cho học sinh trước khi giáo viên chốt kiến thức chuẩn hóa.
3. **Tính xoắn ốc liên tục:** Pha AE của tiết học trước là nền tảng trải nghiệm (CE) kích hoạt cho tiết học hoặc chủ đề tiếp theo.

---

## ĐIỀU 9. QUY TẮC ĐÁNH GIÁ KẾT QUẢ GIÁO DỤC AI (MỤC VI QĐ 2422 & CV 5588)

Mọi hoạt động và tài liệu đánh giá trong chương trình bắt buộc phải tuân thủ nghiêm ngặt các nguyên tắc sau:

### 1. Những điều bắt buộc (Căn cứ Mục VI QĐ 2422 & CV 5588):
* **Bám sát YCCĐ cốt lõi:** Việc đánh giá phải bám sát các yêu cầu cần đạt thuộc nội dung cốt lõi của từng lớp; không sử dụng nội dung mở rộng làm căn cứ đánh giá bắt buộc đối với mọi học sinh.
* **Đánh giá quá trình giữ vai trò chủ đạo:** Đánh giá kết quả giáo dục AI là một bộ phận của quá trình tổ chức dạy học, được thực hiện thường xuyên qua quan sát, trao đổi, câu hỏi, nhiệm vụ, thực hành, sản phẩm và hồ sơ học tập.
* **Hình thức ghi nhận:** Kết quả được ghi nhận bằng **nhận xét hoặc mức độ đáp ứng YCCĐ** trên cơ sở các minh chứng thu thập được.
* **Đánh giá định kỳ:** Có thể thực hiện sau một chuyên đề, một nhóm nội dung hoặc một giai đoạn học tập qua: bài thực hành, xử lý tình huống, bài trình bày, dự án nhỏ, sản phẩm, hồ sơ học tập hoặc **triển lãm học tập**.
* **Đánh giá dựa trên đa minh chứng:** Kết luận đánh giá phải dựa trên nhiều minh chứng; tuyệt đối không suy rộng thành kết luận về toàn bộ năng lực AI chỉ từ một sản phẩm, một lần thực hiện nhiệm vụ hoặc kết quả dùng một công cụ cụ thể.

### 2. Những điều nghiêm cấm tuyệt đối:
* ❌ **Không tổ chức bài kiểm tra, bài thi riêng:** Khung không quy định bài kiểm tra, bài thi hoặc đầu điểm riêng đối với nội dung giáo dục AI.
* ❌ **Không xác lập đầu điểm riêng:** Không cho điểm số riêng biệt cho môn/chuyên đề AI.
* ❌ **Không đánh giá theo công cụ:** Không đánh giá dựa vào mức độ thành thạo một phần mềm hoặc nền tảng riêng biệt mà chú trọng khả năng vận dụng kiến thức, kỹ năng, thái độ và trách nhiệm. Khung không đồng nhất năng lực AI với kỹ năng thao tác công cụ hay viết câu lệnh.
* ❌ **Không gây bất lợi về hạ tầng:** Đánh giá không gây bất lợi cho học sinh do thiếu thiết bị, tài khoản, kết nối Internet hoặc khả năng tiếp cận công cụ AI cụ thể.

### 3. Quy tắc khi học sinh sử dụng AI trong sản phẩm học tập:
* Học sinh phải thực hiện **trách nhiệm giải trình và liêm chính học thuật**: nêu rõ công cụ AI đã dùng, mục đích, phạm vi hỗ trợ, phần việc do học sinh trực tiếp thực hiện, cách kiểm chứng và chỉnh sửa kết quả.
* Việc khai báo sử dụng AI là minh chứng về **tính trung thực và trách nhiệm**, không phải là căn cứ để tự động tăng hoặc giảm kết quả đánh giá.

---

## ĐIỀU 10. QUY TẮC HẠ TẦNG VÀ CÔNG BẰNG TIẾP CẬN (CV 5588/BGDĐT-GDPT)

Căn cứ Mục I.2 và Mục II.3 Công văn 5588/BGDĐT-GDPT, mọi kế hoạch dạy học và tài liệu hoạt động phải tuân thủ:

### 1. Nguyên tắc công bằng tiếp cận:
* **Bảo đảm cơ hội tiếp cận công bằng** cho mọi học sinh, đặc biệt học sinh ở vùng có điều kiện kinh tế - xã hội khó khăn, học sinh thiếu thiết bị hoặc kết nối Internet.
* **Ưu tiên công cụ mở và miễn phí:** Ưu tiên tận dụng phần mềm mã nguồn mở, miễn phí và nền tảng trực quan đã được rà soát, phù hợp với mục tiêu sư phạm và năng lực nhận thức của học sinh.
* **Bắt buộc có phương án dự phòng không dùng máy tính:** Luôn xây dựng song song phương án học tập thay thế phù hợp (mô phỏng thủ công bằng giấy-bút, thẻ tranh, đóng vai, thuật toán bằng lời) cho các trường hợp thiếu thiết bị.
* **Cấm thương mại hóa:** Tuyệt đối không yêu cầu học sinh phải sử dụng tài khoản cá nhân, mua tài khoản, thiết bị hay dịch vụ trả phí để tham gia các hoạt động giáo dục AI bắt buộc.

### 2. Nguyên tắc an toàn và bảo vệ dữ liệu cá nhân:
* Tuân thủ Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15, Luật Trí tuệ nhân tạo số 134/2025/QH15 và Luật An toàn thông tin.
* Cơ sở giáo dục phải ban hành **quy tắc sử dụng AI trong nhà trường**, rà soát công cụ, tài khoản và chính sách dữ liệu trước khi đưa vào giảng dạy.
* Không chia sẻ thông tin nhận dạng cá nhân của học sinh lên các nền tảng AI công cộng chưa được rà soát.
* Phải có quy trình tiếp nhận, xử lý và báo cáo sự cố liên quan đến việc sử dụng AI.

### 3. Ba hình thức triển khai theo CV 5588 (Mục II.2):
* **Hình thức 1: Các chuyên đề giáo dục AI** — Bố trí trong kế hoạch dạy học 2 buổi/ngày, đảm bảo tối thiểu 12 tiết/lớp/năm học đối với nội dung cốt lõi; có thể bổ sung nội dung mở rộng phù hợp.
* **Hình thức 2: Lồng ghép trong các môn học và hoạt động giáo dục** — Nhằm củng cố, vận dụng nội dung cốt lõi và có thể triển khai một phần nội dung mở rộng. Lồng ghép không làm thay đổi hoặc gia tăng YCCĐ của môn học.
* **Hình thức 3: Tổ chức hoạt động giáo dục theo nhu cầu** — Áp dụng đối với nội dung mở rộng qua CLB, dự án, tham quan, ngoại khóa trên tinh thần tự nguyện, tự chọn.

---

## ĐIỀU 11. BẢNG THUẬT NGỮ CHUẨN HOÁ ĐẦY ĐỦ (PHỤ LỤC QĐ 2422)

Toàn bộ 26 thuật ngữ chính thức được trích xuất nguyên bản từ Phụ lục Giải thích thuật ngữ QĐ 2422 làm căn cứ đối chiếu:

| STT | Thuật ngữ tiếng Việt | Thuật ngữ tiếng Anh | Định nghĩa cốt lõi theo QĐ 2422 |
|:---:|---|---|---|
| 1 | **Trí tuệ nhân tạo** | Artificial Intelligence (AI) | Việc thực hiện bằng điện tử các năng lực trí tuệ của con người (học tập, suy luận, nhận thức, phán đoán, hiểu ngôn ngữ tự nhiên). |
| 2 | **AI tạo sinh** | Generative AI | Loại AI có khả năng tạo ra nội dung mới như văn bản, hình ảnh, âm thanh, video, mã nguồn hoặc dữ liệu, dựa trên dữ liệu đã học. |
| 3 | **Hệ thống AI** | AI system | Hệ thống dựa trên máy, suy luận từ dữ liệu đầu vào để tạo ra dự đoán, nội dung, khuyến nghị hoặc quyết định. |
| 4 | **Vòng đời hệ thống AI** | AI system lifecycle | Các giai đoạn từ xác định vấn đề, chuẩn bị dữ liệu, thiết kế, thử nghiệm, triển khai, giám sát, xử lý sự cố đến kết thúc sử dụng. |
| 5 | **Mô hình AI** | AI model | Thành phần tạo ra đầu ra từ đầu vào dựa trên tham số hoặc quy tắc đã học/xây dựng sẵn. |
| 6 | **Thuật toán** | Algorithm | Dãy hữu hạn các bước, quy tắc rõ ràng nhằm giải quyết một bài toán hoặc thực hiện một nhiệm vụ. |
| 7 | **Học máy** | Machine learning | Phương pháp cho máy "học" từ dữ liệu thay vì lập trình tường minh từng quy tắc. |
| 8 | **Học có giám sát** | Supervised learning | Học từ dữ liệu đã được gán nhãn (có cặp đầu vào và kết quả đúng) để dự đoán kết quả mới. |
| 9 | **Học không giám sát** | Unsupervised learning | Mô hình tự tìm cấu trúc, quy luật hoặc nhóm trong dữ liệu chưa được gán nhãn. |
| 10 | **Học tăng cường** | Reinforcement learning | Học qua thử nghiệm, nhận phản hồi dạng thưởng/phạt để tối ưu hành động. |
| 11 | **Mạng nơ-ron nhân tạo** | Artificial neural network | Mô hình tính toán nhiều nút liên kết, tổ chức nhiều lớp lấy cảm hứng từ nơ-ron sinh học. |
| 12 | **Học sâu** | Deep learning | Nhánh học máy dùng mạng nơ-ron nhân tạo nhiều lớp để tự động học đặc trưng từ dữ liệu. |
| 13 | **Xử lí ngôn ngữ tự nhiên** | Natural Language Processing (NLP) | Lĩnh vực kỹ thuật giúp máy hiểu, phân tích và tạo ra ngôn ngữ con người. |
| 14 | **Thị giác máy tính** | Computer vision | Giúp máy phân tích hình ảnh, video để nhận dạng, phân loại đối tượng. |
| 15 | **Phần mềm hội thoại tự động** | Chatbot | Ứng dụng giao tiếp với người dùng bằng hội thoại (văn bản hoặc giọng nói). |
| 16 | **Mô hình ngôn ngữ lớn** | Large Language Model (LLM) | Mô hình AI tạo sinh huấn luyện trên khối lượng văn bản rất lớn, hiểu và tạo ngôn ngữ tự nhiên. |
| 17 | **Tác nhân AI** | AI agent | Hệ thống AI có khả năng lập kế hoạch và tự thực hiện chuỗi hành động nhằm đạt mục tiêu dưới sự giám sát của con người. |
| 18 | **Kĩ thuật sinh nội dung tăng cường bằng truy xuất** | Retrieval-Augmented Generation (RAG) | Cho phép mô hình truy xuất thông tin ngoài trước khi tạo câu trả lời nhằm tăng độ chính xác, giảm thông tin sai. |
| 19 | **Câu lệnh** | Prompt | Chỉ dẫn, câu hỏi, dữ liệu hoặc ngữ cảnh do người dùng cung cấp để AI tạo ra đầu ra tương ứng. |
| 20 | **Ảo giác AI** | Hallucination | Hiện tượng AI tạo ra đầu ra có vẻ hợp lý nhưng sai, thiếu căn cứ hoặc không tồn tại (hạn chế kỹ thuật, không có chủ đích). |
| 21 | **Thiên lệch** | Bias | Sai lệch có tính hệ thống trong đầu ra của AI phát sinh từ dữ liệu/thiết kế, có thể dẫn đến thiếu công bằng hoặc phân biệt đối xử. |
| 22 | **Nội dung giả mạo do AI tạo ra** | Deepfake | Hình ảnh, âm thanh, video do AI tạo/chỉnh sửa nhằm mô phỏng người, sự kiện thật với độ chân thực cao. |
| 23 | **Quá khớp** | Overfitting | Hiện tượng mô hình học quá sát dữ liệu huấn luyện nên hoạt động kém với dữ liệu mới. |
| 24 | **Trải nghiệm người dùng** | User Experience (UX) | Tổng thể cảm nhận, mức độ thuận tiện và hiệu quả khi tương tác với sản phẩm, hệ thống. |
| 25 | **Dữ liệu cá nhân** | Personal data | Dữ liệu xác định hoặc giúp xác định một con người cụ thể (cơ bản và nhạy cảm). Sau khi khử nhận dạng không còn là dữ liệu cá nhân. |
| 26 | **Trách nhiệm giải trình** | Accountability | Nghĩa vụ giải thích, cung cấp thông tin và chịu trách nhiệm về quyết định, quy trình và tác động liên quan đến sử dụng, phát triển AI. |

---

## ĐIỀU 12. QUY CHUẨN BỘ 4 SẢN PHẨM CỐT LÕI VÀ MÔ HÌNH CHUYỂN HOÁ DỮ LIỆU 4 TẦNG (4-TIER CURRICULUM ARCHITECTURE)

Bốn sản phẩm này không phải là 4 tài liệu rời rạc, mà tạo thành một **dây chuyền thiết kế giáo dục chuẩn mực quốc tế**, vận hành từ cấp độ **Kiến trúc vĩ mô (Macro)** xuống đến **Từng phút dạy học vi mô (Micro)**:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ TẦNG 1: KHUNG CHƯƠNG TRÌNH (Curriculum Framework)                            │
│ ➔ Trả lời: CHUẨN ĐẦU RA LÀ GÌ? (Việt Nam + Quốc tế + Tiến trình xoắn ốc)    │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ (Phân rã thành hành vi đo lường được)
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ TẦNG 2: MA TRẬN KỸ NĂNG & TIỂU KỸ NĂNG (Skill & Micro-Skill Matrix)         │
│ ➔ Trả lời: HỌC SINH LÀM ĐƯỢC THAO TÁC GÌ? (Nhiệm vụ thực hành quan sát được)│
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ (Rải vào kế hoạch thời gian 36 tuần)
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ TẦNG 3: PHÂN PHỐI CHƯƠNG TRÌNH 36 TIẾT (Scope & Sequence / Syllabus)        │
│ ➔ Trả lời: DẠY BÀI NÀO VÀO TUẦN NÀO? (12 Core bắt buộc + 24 Expanded)       │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ (Đặc tả sư phạm cho từng tiết 45 phút)
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ TẦNG 4: HỒ SƠ KIẾN THỨC – KỸ NĂNG TỪNG TIẾT (Lesson Specifications)         │
│ ➔ Trả lời: 45 PHÚT TRÊN LỚP DẠY CỤ THỂ CÁI GÌ? (Mục tiêu, Kiến thức, Kỹ năng)│
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1. SẢN PHẨM 1: KHUNG CHƯƠNG TRÌNH TIỂU HỌC & THCS (CURRICULUM FRAMEWORK)
* **Bản chất & Mục đích:** Bản hiến pháp chuyên môn của toàn bộ dự án; điểm tựa pháp lý và học thuật cao nhất. Sản phẩm 1 **tuyệt đối không chỉ dừng lại ở việc sao chép nguyên văn văn bản của Bộ GD&ĐT**, mà phải là **Khung Chương trình Tích hợp Làm giàu Quốc tế (Hybrid Enriched Framework)**: Bảo đảm đáp ứng trọn vẹn 100% chuẩn đầu ra của QĐ 2422/QĐ-BGDĐT (hợp pháp tại Việt Nam), đồng thời **tích hợp trực tiếp các chỉ số năng lực và hành vi làm giàu quốc tế `[INT-ENRICH]`** (tham chiếu từ UNESCO 2024, AI4K12 5 Big Ideas, OECD, Singapore MOE) ngay tại từng YCCĐ.
* **Cấu trúc trường thông tin chuẩn (Data Schema):**
  1. *Lớp:* Từ Lớp 1 đến Lớp 9.
  2. *Mạch nội dung / Chủ đề chuẩn:* Mạch A (A1, A2, A3), Mạch B (B1, B2, B3), Mạch C (C1 đến C5), Mạch D (D1, D2).
  3. *Mã YCCĐ Việt Nam:* Ghi rõ mã kèm nhãn: `[VN-CORE]` (cốt lõi) hoặc `[VN-MR]` (mở rộng).
  4. *Yêu cầu cần đạt chuẩn hóa tích hợp:*
     - **Chuẩn Bộ GD&ĐT (Baseline):** Đảm bảo 100% yêu cầu cần đạt chính thức của QĐ 2422.
     - **Chỉ số năng lực làm giàu quốc tế `[INT-ENRICH]`:** Chỉ số hành vi/năng lực bổ trợ cụ thể chắt lọc từ chuẩn UNESCO, AI4K12, OECD, Singapore MOE.
  5. *Định vị Tiến trình Xoắn ốc (Spiral Progression):* Bảo đảm liên thông ZPD từ Lớp 1 đến Lớp 9.
* **Ví dụ minh họa (Lớp 1 - Mã 1.C1.3):**
  * *Mã & Nội dung chuẩn Bộ:* `[VN-CORE] 1.C1.3`: Nhận biết được các thiết bị thông minh có các bộ phận giống với bộ phận của con người (ví dụ: camera là “mắt” và micro là “tai” của các thiết bị đó).
  * *Tích hợp làm giàu quốc tế:* `[INT-ENRICH: AI4K12 Big Idea 1 - Perception]`: Biết thử nghiệm đóng vai che "mắt" (camera) hoặc bịt "tai" (micro) của thiết bị để nhận ra khi thiếu cảm biến, AI không thể thu nhận thông tin từ thế giới xung quanh.

### 2. SẢN PHẨM 2: MA TRẬN KỸ NĂNG TIỂU HỌC & THCS (SKILL & MICRO-SKILL MATRIX)
* **Bản chất & Mục đích:** Bước "Giải mã hành vi" (Operationalization): Phân rã từng YCCĐ thành 3 – 5 tiểu kỹ năng (Micro-skills) có thể quan sát, thao tác và đo lường trực tiếp trên lớp học; cung cấp nội dung/tình huống thực hành kỹ năng cụ thể (theo cả bối cảnh Việt Nam và học liệu thực nghiệm quốc tế).
* **Cấu trúc trường thông tin chuẩn:**
  1. *Lớp & Chủ đề.*
  2. *Mã YCCĐ bảo trợ (QĐ 2422 & UNESCO).*
  3. *Nhóm kỹ năng (Skill Cluster):* Kỹ năng bậc cao tổng quát (ví dụ: Kỹ năng kiểm chứng thông tin do AI sinh ra, Kỹ năng bảo vệ dữ liệu cá nhân).
  4. *Tiểu kỹ năng (Micro-skills):* Thao tác kỹ thuật (Technical), Tư duy phản biện (Cognitive), Trách nhiệm đạo đức (Ethical).
  5. *Nội dung / Nhiệm vụ thực hành kỹ năng:* Tình huống thực nghiệm trên lớp (Unplugged, công cụ số, nhập vai đối kháng).
  6. *Bằng chứng đánh giá (Evidence of Mastery):* Sản phẩm hoặc hành vi cụ thể chứng minh học sinh đã thành thạo kỹ năng.
* **Ví dụ minh họa (Lớp 6 - Từ YCCĐ 6.A1.3: Kiểm tra lại kết quả AI đưa ra):**
  * *Nhóm kỹ năng:* Kỹ năng thẩm định và kiểm chứng thông tin (Fact-checking & Verification).
  * *Tiểu kỹ năng 1 (Kỹ thuật):* Biết lưu lại nguyên văn câu trả lời của AI và trích xuất các từ khóa chính cần kiểm chứng.
  * *Tiểu kỹ năng 2 (Phản biện):* Biết mở ít nhất 2 nguồn tin cậy độc lập (SGK, website chính thống) để đối chiếu chéo số liệu.
  * *Tiểu kỹ năng 3 (Ghi nhận):* Biết lập bảng so sánh 3 cột: `[AI trả lời] - [Nguồn kiểm chứng] - [Kết luận đúng/sai]`.
  * *Nhiệm vụ thực hành:* Đưa tình huống AI giải thích sai hiện tượng khoa học; học sinh đóng vai "Thám tử số" dùng SGK vạch ra lỗi ảo giác (hallucination) của AI.

### 3. SẢN PHẨM 3: PHÂN PHỐI CHƯƠNG TRÌNH 36 TIẾT (SCOPE & SEQUENCE / SYLLABUS)
* **Bản chất & Mục đích:** Kế hoạch thời khóa biểu và tiến trình dạy học thực tế được chuẩn hóa theo quy định của Bộ GD&ĐT (chuẩn Công văn 5512 đối với THCS và Công văn 2345 đối với Tiểu học); quy hoạch đúng 36 tiết/lớp/năm học cân đối giữa 12 tiết Cốt lõi, 24 tiết Mở rộng và các tiết Đánh giá quá trình / Triển lãm (Mục VI QĐ 2422).
* **Cấu trúc trường thông tin chuẩn:**
  1. *Lớp.*
  2. *Tiết thứ:* Từ Tiết 1 đến Tiết 36.
  3. *Mạch / Chủ đề:* Đảm bảo cả 4 mạch A, B, C, D đều hiện diện.
  4. *Tên bài học:* Thể hiện bản chất nội dung, tuân thủ chính sách từ vựng Zero-Deviation.
  5. *Loại tiết:* `Cốt lõi` (12 Core), `Mở rộng` (24 Expanded), `Đánh giá quá trình`, `Triển lãm / Báo cáo`.
  6. *Mã YCCĐ chính thức:* Ghi rõ mã chuẩn QĐ 2422 (`X.YZ.N` cho cốt lõi; `X.YZ.MRn` cho mở rộng; `Mục VI QĐ 2422` cho đánh giá; để trống cho triển lãm).
  7. *Nội dung trọng tâm & Dấu ấn quốc tế:* Mô tả cô đọng hoạt động sư phạm, kèm thẻ định danh `[INT-ENRICH: Nguồn]`.
* **Ví dụ minh họa (Lớp 6):**
  * *Tiết 1:* Con người làm chủ công nghệ AI | Mạch A1 | Cốt lõi | Mã: `6.A1.1` | Thảo luận vai trò con người lập trình và điều khiển AI `[INT-ENRICH: UNESCO-Agency]`.
  * *Tiết 12:* Đánh giá quá trình: Báo cáo kỹ năng số giai đoạn 1 | Đánh giá | Mã: `Mục VI QĐ 2422` | Trình bày sản phẩm nhật ký câu lệnh cá nhân.
  * *Tiết 13:* Khám phá Mô hình Thị giác máy tính nâng cao | Mạch C3 | Mở rộng | Mã: `6.C3.MR1` | Huấn luyện mô hình phân loại cử chỉ với Teachable Machine `[INT-ENRICH: AI4K12-Learning]`.

### 4. SẢN PHẨM 4: HỒ SƠ KIẾN THỨC – KỸ NĂNG TỪNG TIẾT (LESSON SPECIFICATIONS / PROFILES)
* **Bản chất & Mục đích:** Bản vẽ thiết kế kỹ thuật sư phạm chi tiết cho từng tiết học (định lượng chuẩn theo cấp học: 30–35 phút cho Lớp 1–2; 35 phút cho Lớp 3–5; 45 phút cho Lớp 6–9), đứng giữa Khung PPCT và Kế hoạch bài dạy (Giáo án) chi tiết. Giúp giáo viên biết chính xác mục tiêu 3 thành phần, kiến thức trọng tâm (26 thuật ngữ), kỹ năng hình thành, kịch bản 4 pha David Kolb tương ứng thời lượng và phương án Unplugged không máy tính.
* **Cấu trúc trường thông tin chuẩn (Cho từng bài / từng tiết):**
  1. *Định danh:* Lớp, Tiết thứ, Tên bài học, Mạch nội dung, Mã YCCĐ bảo trợ, Thời lượng tiết học (30–35p hoặc 35p hoặc 45p).
  2. *Mục tiêu bài học (Chuẩn CV 5512 & CV 2345):* Kiến thức, Kỹ năng, Phẩm chất/Thái độ.
  3. *Kiến thức trọng tâm (Core Concepts):* Định nghĩa chuẩn theo 26 thuật ngữ QĐ 2422; Bảng chẩn đoán Quan niệm sai lầm phổ biến (Misconceptions) cần uốn nắn.
  4. *Kỹ năng cốt lõi hình thành (Target Micro-skills):* Thao tác cụ thể trong thời lượng tiết học, yêu cầu bằng chứng số (prompt log, ảnh mô hình, phiếu bài tập).
  5. *Đặc tả kịch bản sư phạm 4 pha David Kolb (Phân bổ phút theo chuẩn cấp học):*
     * Pha 1: Trải nghiệm cụ thể (CE): Tình huống kích hoạt, trò chơi Unplugged hoặc thử nghiệm gây bất ngờ.
     * Pha 2: Quan sát & Phản tư (RO): Câu hỏi phản tư (*What?*), học sinh tự chỉ ra nghịch lý.
     * Pha 3: Khái quát hóa trừu tượng (AC): Giáo viên chuẩn hóa khái niệm, công thức chốt (*So what?*).
     * Pha 4: Thử nghiệm tích cực (AE): Thử thách giải quyết bài toán mới trong bối cảnh mới (*Now what?*).
  6. *Phương án dự phòng không dùng máy tính (Unplugged Fallback):* Cách dạy bằng thẻ giấy, đóng vai khi phòng máy mất điện hoặc thiếu thiết bị theo CV 5588.

---

## ĐIỀU 13. NGUYÊN TẮC RÀNG BUỘC TRỤC XOẮN ỐC (SPIRAL PROGRESSION & ZPD) VÀ HỆ THỐNG 5 TẦNG SẢN PHẨM

> **QUY CHUẨN CẬP NHẬT KIẾN TRÚC DỰ ÁN (CHÍNH THỨC):**
> Dự án **LOẠI BỎ HOÀN TOÀN** sản phẩm *"Kế hoạch bài dạy chi tiết (giáo án)"* để tập trung nguồn lực xây dựng chuẩn hóa **HỆ THỐNG 5 TẦNG SẢN PHẨM** với lộ trình ưu tiên cuốn chiếu:
> * **ƯU TIÊN 1 (Hoàn thành trước):** Toàn bộ 5 Tầng sản phẩm cho **TIỂU HỌC (LỚP 1 – 5)**.
> * **ƯU TIÊN 2 (Triển khai sau khi hoàn thành Tiểu học):** Toàn bộ 5 Tầng sản phẩm cho **THCS (LỚP 6 – 9)**.

### 1. Bản chất sư phạm của Trục xoắn ốc và Vùng phát triển gần nhất (ZPD):
* **Không lặp lại cơ học (Anti-Redundancy):** Tuyệt đối không nhắc lại kiến thức cũ ở dạng phẳng. Kiến thức ở lớp dưới làm nền tảng (scaffolding/baseline) cho lớp trên.
* **Nâng tầng nhận thức và mở rộng ZPD:** Cùng một đối tượng nghiên cứu, khi lặp lại ở lớp trên phải mở ra:
  1. *Một hiểu biết bản chất mới (Conceptual Depth):* Từ hiện tượng bề ngoài sang bản chất thuật toán, xác suất.
  2. *Một phương thức thực hành mới (Operational Upgrade):* Từ thẻ bài thủ công Unplugged sang kéo thả mô hình số, viết câu lệnh prompt có cấu trúc và kiểm chứng đa nguồn.
  3. *Một yếu tố/biến số mới thêm vào (Contextual & Ethical Complexity):* Thêm biến số thiên lệch, rủi ro deepfake, trách nhiệm giải trình và liêm chính học thuật.

### 2. Định nghĩa Hệ thống 5 Tầng Sản phẩm Chuẩn hóa:
1. **Tầng 1 · Khung YCCĐ (Curriculum Framework & Traceability Crosswalk):** 
   * Bảng đối soát toàn diện: Mã QĐ 2422 | YCCĐ Bộ GD&ĐT | Chuẩn UNESCO | Benchmark Quốc tế OECD/AI4K12.
2. **Tầng 2 · Ma trận Kỹ năng (Micro-skill & Behavioral Matrix):** 
   * Giải mã từng YCCĐ tĩnh thành các tiểu kỹ năng (Micro-skills) và hành vi đo lường được trên lớp; phân loại rõ 3 nhánh: Kỹ thuật (Technical), Phản biện (Cognitive), Đạo đức (Ethical) + Evidence of Mastery.
3. **Tầng 3 · Phân phối Chương trình (PPCT 36 tiết/lớp/năm học):** 
   * Phân định minh bạch 12 tiết Cốt lõi (`VN-CORE`) và 24 tiết Mở rộng (`VN-MR` & `INT-ENRICH`), sắp xếp theo tiến trình nhận thức phát triển liền mạch.
4. **Tầng 4 · KT-KN & Thuật ngữ Chuẩn hóa (Knowledge-Skill Specs & Terminology):** 
   * Hồ sơ Kiến thức cốt lõi, Kỹ năng trọng tâm và Giải thích chuẩn xác 26 thuật ngữ theo QĐ 2422 (chống sai lệch, chống dùng từ lóng công nghệ).
5. **Tầng 5 · Wiki & Tập huấn GV (Teacher Training & Knowledge Base Wiki):** 
   * Cẩm nang sư phạm, bộ tài liệu hướng dẫn giáo viên, hệ thống kịch bản tình huống tham khảo, bộ công cụ Unplugged và cẩm nang giải đáp tình huống sư phạm khi triển khai thực tế.

### 3. Mối quan hệ hữu cơ và tính truy xuất 2 chiều (Bi-directional Traceability):
* **Quan hệ 1 - 1 và 1 - N:** 1 YCCĐ ở Tầng 1 sinh ra 2–4 Tiểu kỹ năng ở Tầng 2; phân bổ vào 1–2 tiết ở Tầng 3; được làm rõ kiến thức/thuật ngữ ở Tầng 4; và hỗ trợ phương pháp giảng dạy ở Tầng 5.
* **Không có "YCCĐ mồ côi" (No Orphan Requirements):** Mọi YCCĐ trong Khung (cả Core lẫn MR) đều phải tìm thấy "địa chỉ cư trú" ở Tầng 2, 3, 4, 5.
* **Không có "Nội dung trôi nổi" (No Unanchored Activities):** Không nội dung nào trong Tầng 3, 4, 5 xuất hiện nếu không truy xuất ngược được về mã YCCĐ bảo trợ ở Tầng 1.

### 4. Lộ trình Triển khai Dự án:
```text
┌────────────────────────────────────────────────────────┐
│             TIỂU HỌC · LỚP 1–5 — ƯU TIÊN 1             │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Tầng 1 · Khung YCCĐ [ĐÃ HOÀN THÀNH 100%]        │  │
│  └────────────────────────┬─────────────────────────┘  │
│                           ▼                            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Tầng 2 · Ma trận kỹ năng [ĐANG TRIỂN KHAI]      │  │
│  └────────────────────────┬─────────────────────────┘  │
│                           ▼                            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Tầng 3 · Phân phối chương trình                 │  │
│  └────────────────────────┬─────────────────────────┘  │
│                           ▼                            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Tầng 4 · KT-KN & Thuật ngữ chuẩn hóa            │  │
│  └────────────────────────┬─────────────────────────┘  │
│                           ▼                            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Tầng 5 · Wiki & Tập huấn GV                     │  │
│  └──────────────────────────────────────────────────┘  │
└───────────────────────────┬────────────────────────────┘
                            │
                            │ Hoàn thành toàn bộ Tiểu học
                            ▼
┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐
  THCS · LỚP 6–9 — ƯU TIÊN 2                              
│ ┌──────────────────────────────────────────────────┐    │
  │  Tầng 1 · Khung YCCĐ                             │    
│ └────────────────────────┬─────────────────────────┘    │
                           ▼                              
│ ┌──────────────────────────────────────────────────┐    │
  │  Tầng 2 · Ma trận kỹ năng                        │    
│ └────────────────────────┬─────────────────────────┘    │
                           ▼                              
│ ┌──────────────────────────────────────────────────┐    │
  │  Tầng 3 · Phân phối chương trình                 │    
│ └────────────────────────┬─────────────────────────┘    │
                           ▼                              
│ ┌──────────────────────────────────────────────────┐    │
  │  Tầng 4 · KT-KN & Thuật ngữ chuẩn hóa            │    
│ └────────────────────────┬─────────────────────────┘    │
                           ▼                              
│ ┌──────────────────────────────────────────────────┐    │
  │  Tầng 5 · Wiki & Tập huấn GV                     │    
│ └──────────────────────────────────────────────────┘    │
└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘
```

---

## ĐIỀU 14. QUY CHUẨN ĐỘI NGŨ NHÂN SỰ CHUYÊN TRÁCH VÀ CƠ CHẾ KIỂM SOÁT CHẤT LƯỢNG (QC GATES)

Để vận hành chính xác mô hình chuyển hoá 5 tầng sản phẩm theo quy chuẩn tối cao QĐ 2422/QĐ-BGDĐT và chuẩn quốc tế:

### 1. Cơ cấu Đội ngũ 5 Vị trí Nhân sự chuyên trách:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   VỊ TRÍ 1: KIẾN TRÚC SƯ TRƯỞNG                        │
│            (Lead Curriculum Architect - Macro Alignment)               │
│   • Phụ trách: Sản phẩm 1 (Khung K-9, VN-UNESCO Crosswalk, Trục ZPD)   │
│   • Skill bảo trợ: ai_curriculum_researcher, qd2422_ai_curriculum_expert│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Bàn giao SP1 (Khung chuẩn K-9)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│             VỊ TRÍ 2: CHUYÊN GIA PHÂN RÃ MA TRẬN KỸ NĂNG               │
│        (Learning Outcome & Micro-skill Specialist - Operationalization)│
│   • Phụ trách: Sản phẩm 2 (Ma trận kỹ năng K-9: Kỹ thuật/Phản biện/Đạo đức)│
│   • Skill bảo trợ: qd2422_ai_curriculum_expert, skill_matrix_decomposer │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Bàn giao SP2 (Ma trận Kỹ năng K-9)
                                    │ (Điểm tách phân hệ dự án)
                  ┌─────────────────┴─────────────────┐
                  ▼                                   ▼
┌───────────────────────────────────┐ ┌───────────────────────────────────┐
│  VỊ TRÍ 3: CHUYÊN GIA TIỂU HỌC     │ │    VỊ TRÍ 4: CHUYÊN GIA THCS      │
│  (Primary Pedagogical Specialist) │ │  (Secondary Pedagogical Specialist)│
│ • Phụ trách: SP3A (PPCT L1–5)     │ │ • Phụ trách: SP3B (PPCT L6–9)     │
│              SP4A (Specs 30–35p)  │ │              SP4B (Specs 45p)     │
│ • Chuẩn: CV 2345, Unplugged, tranh│ │ • Chuẩn: CV 5512, Prompt log,     │
│ • Skill: cv2345_primary_specialist│ │   chống deepfake, liêm chính số   │
│          qd2422_ppct_builder      │ │ • Skill: qd2422_ppct_builder      │
│                                   │ │          thcs_story_evaluator     │
└─────────────────┬─────────────────┘ └─────────────────┬─────────────────┘
                  │                                     │
                  └─────────────────┬───────────────────┘
                                    │ Chuyển giao nghiệm thu
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│              VỊ TRÍ 5: TRƯỞNG BAN KIỂM ĐỊNH CHẤT LƯỢNG ĐỘC LẬP         │
│          (Independent QA/QC Auditor - Final Quality Gatekeeper)        │
│   • Phụ trách: Thẩm định 8 trụ cột chất lượng, xuất Biên bản QC Report │
│   • Quyền hạn: Quyền phủ quyết (VETO), từ chối nghiệm thu sản phẩm lỗi  │
│   • Skill bảo trợ: ppct_qaqc_auditor                                   │
└────────────────────────────────────────────────────────────────────────┘
```

#### Chi tiết vai trò, căn cứ chuyên môn và sản phẩm bàn giao của từng vị trí:

1. **Vị trí 1: KIẾN TRÚC SƯ TRƯỞNG CHƯƠNG TRÌNH (Lead Curriculum Architect):**
   * *Vai trò:* Định hình kiến trúc tổng thể, bảo đảm tính pháp lý tối cao của QĐ 2422, đối sánh chuẩn quốc tế UNESCO/AI4K12 và thiết kế tiến trình xoắn ốc liên thông 9 năm.
   * *Chuỗi tư duy ngầm 5 tầng (Internal Deliberation Chain - Chạy ngầm trước khi xuất kết quả):*
     - *Tầng 1:* Đối chiếu Mã và Nội dung nguyên văn của Bộ GD&ĐT trong file `qd2422_full.txt`.
     - *Tầng 2:* Đối chiếu Dimension và Level tương ứng của UNESCO AI Competency Framework.
     - *Tầng 3:* Tham chiếu bài toán/hoạt động quốc tế (OECD, AI4K12 Big Ideas 1-5).
     - *Tầng 4:* Kiểm định Trục xoắn ốc ZPD (Lớp dưới chuẩn bị gì cho lớp trên; lớp trên nâng cấp gì và làm bản lề cho lớp kế tiếp).
     - *Tầng 5:* Tổng hợp chốt lại thành Yêu cầu cần đạt chuẩn hóa của Khung chương trình (kết quả đúc kết duy nhất hiển thị tại cột YCCĐ của bảng Khung chương trình).
   * *Căn cứ chuyên môn:* QĐ 2422 (Mục I, II, III, IV, V, Phụ lục); UNESCO AI Framework; AI4K12 5 Big Ideas; Singapore MOE AI Literacy Framework.
   * *Kỹ năng/Skill tương ứng:* `ai_curriculum_researcher`, `qd2422_ai_curriculum_expert`.
   * *Sản phẩm bàn giao:* **Sản phẩm 1 (Khung chương trình chuẩn K-9)** dạng bảng đối soát hoàn chỉnh.

2. **Vị trí 2: CHUYÊN GIA PHÂN RÃ MA TRẬN KỸ NĂNG (Learning Outcome & Micro-skill Specialist):**
   * *Vai trò:* Giải mã hành vi của từng YCCĐ tĩnh thành các cụm kỹ năng và tiểu kỹ năng (Micro-skills) đo lường được trên lớp; phân loại rõ 3 nhánh: Kỹ thuật (Technical), Phản biện (Cognitive), Đạo đức (Ethical).
   * *Căn cứ chuyên môn:* Điều 3, Điều 4 `AGENTS.md`; Thang đo nhận thức Bloom cải tiến; Khung kỹ năng đo lường OECD K-12.
   * *Kỹ năng/Skill tương ứng:* `qd2422_ai_curriculum_expert`, `skill_matrix_decomposer` (cần bổ sung).
   * *Sản phẩm bàn giao:* **Sản phẩm 2 (Ma trận Kỹ năng K-9)** kèm bằng chứng đánh giá năng lực (*Evidence of Mastery*).

3. **Vị trí 3: CHUYÊN GIA SƯ PHẠM TIỂU HỌC (Primary Pedagogical Specialist):**
   * *Vai trò:* Chuyển hóa mục tiêu thành phân phối chương trình, hồ sơ kiến thức - kỹ năng trọng tâm và tài liệu hướng dẫn giáo viên chuyên biệt cho học sinh Lớp 1 đến Lớp 5 (CV 2345, tranh thẻ, Unplugged, 30–35 phút).
   * *Căn cứ chuyên môn:* Công văn 2345/BGDĐT-GDTH; CV 5588; Điều 5.1 và Điều 8.1 (Chuẩn thời lượng 30–35 phút cho Lớp 1–2; 35 phút cho Lớp 3–5).
   * *Kỹ năng/Skill tương ứng:* `qd2422_ppct_builder`, `cv2345_primary_specialist`.
   * *Sản phẩm bàn giao:* **Tầng 3A (PPCT 36 tiết Lớp 1–5)**, **Tầng 4A (Hồ sơ KT-KN & Thuật ngữ chuẩn hóa Lớp 1–5)** và **Tầng 5A (Wiki & Hướng dẫn tập huấn GV Lớp 1–5)**.

4. **Vị trí 4: CHUYÊN GIA SƯ PHẠM THCS (Secondary Pedagogical Specialist):**
   * *Vai trò:* Thiết kế tiến trình dạy học logic, khoa học, thực nghiệm kiểm chứng cho học sinh Lớp 6 đến Lớp 9; xây dựng kịch bản tình huống thực tế, chống deepfake, lưu vết nhật ký câu lệnh (*prompt log*) và rèn luyện liêm chính học thuật (CV 5512, 45 phút).
   * *Căn cứ chuyên môn:* Công văn 5512/BGDĐT-GDTrH; CV 5588; Điều 5.2 và Điều 8.1 (Chuẩn thời lượng 45 phút); Khung 18 Master Rules tình huống THCS.
   * *Kỹ năng/Skill tương ứng:* `qd2422_ppct_builder`, `thcs_story_evaluator`, `role_based_activity_builder`.
   * *Sản phẩm bàn giao:* **Tầng 3B (PPCT 36 tiết Lớp 6–9)**, **Tầng 4B (Hồ sơ KT-KN & Thuật ngữ chuẩn hóa Lớp 6–9)** và **Tầng 5B (Wiki & Hướng dẫn tập huấn GV Lớp 6–9)**.

5. **Vị trí 5: TRƯỞNG BAN KIỂM ĐỊNH CHẤT LƯỢNG ĐỘC LẬP (Independent QA/QC Auditor):**
   * *Vai trò:* Người gác cổng chất lượng tối cao (Quality Gatekeeper), hoạt động độc lập, không tham gia biên soạn trực tiếp để bảo đảm tính khách quan; rà soát đối chiếu toàn diện 8 trụ cột kỹ thuật và xuất Biên bản thẩm định chất lượng trước khi sản phẩm được phát hành.
   * *Căn cứ chuyên môn:* Toàn bộ 14 Điều của `AGENTS.md`; Skill `ppct_qaqc_auditor`.
   * *Kỹ năng/Skill tương ứng:* `ppct_qaqc_auditor`.
   * *Sản phẩm bàn giao:* **Báo cáo Thẩm định Chất lượng (QA/QC Audit Report)** kèm chữ ký phê duyệt hoặc lệnh VETO yêu cầu sửa đổi.

---

### 2. Quy trình Kiểm soát Chất lượng 3 vòng (3-Gate Quality Control Pipeline):

* **VÒNG 1 (Gate 1 - Self-Audit tại từng nhân sự):**
  * Từng chuyên gia trước khi bàn giao sản phẩm của mình phải tự đối chiếu với bảng Checklist quy chuẩn và từ điển 26 thuật ngữ chuẩn hóa. Tuyệt đối không bàn giao bản nháp chưa tự soát lỗi chính tả, từ lóng hay mã cụt số `.MR`.
* **VÒNG 2 (Gate 2 - Cross-Verification giữa các vị trí liên đới):**
  * Nhân sự ở mắt xích sau phải kiểm tra đầu vào do nhân sự mắt xích trước bàn giao (ví dụ: Chuyên gia THCS kiểm tra xem Ma trận kỹ năng từ Chuyên gia SP2 có khả thi trong tiết học 45 phút hay không; Kiến trúc sư trưởng kiểm tra xem PPCT có bám đúng trục xoắn ốc của Khung K-9 hay không).
* **VÒNG 3 (Gate 3 - Final Independent Audit của Trưởng ban QA/QC):**
  * Chạy tự động và rà soát thủ công toàn diện trên 8 tiêu chí kiểm định:
    1. *QC-1: Chuẩn thời lượng theo cấp học (30–35p cho L1–2; 35p cho L3–5; 45p cho THCS).*
    2. *QC-2: Bao phủ 100% YCCĐ cốt lõi (`VN-CORE`) và 100% YCCĐ mở rộng (`VN-MR`).*
    3. *QC-3: Hệ thống 3 nhãn Outcome (`VN-CORE`, `VN-MR`, `INT-ENRICH`) và Traceability 3 tầng.*
    4. *QC-4: Chính sách từ vựng Zero-Deviation (26 thuật ngữ chuẩn, cấm từ lóng).*
    5. *QC-5: Chu trình Kolb 4 pha khép kín và câu hỏi chuyển pha (What - So what - Now what).*
    6. *QC-6: Phương án dự phòng không máy tính (Unplugged Fallback) bắt buộc cho 100% bài học.*
    7. *QC-7: Ràng buộc Trục xoắn ốc ZPD (Không lặp phẳng, không YCCĐ mồ côi, không nội dung trôi nổi).*
    8. *QC-8: Quy chuẩn thể thức quản lý giáo dục (CV 2345 cho Tiểu học, CV 5512 cho THCS).*

---

### 3. Bảng Chẩn đoán 8 Lỗi Ảo giác / Sai lầm kinh điển của AI và Biện pháp khắc phục:

| STT | Tên lỗi / Ảo giác thường gặp | Biểu hiện sai phạm cụ thể | Biện pháp ngăn chặn & Xử lý bắt buộc |
| :---: | :--- | :--- | :--- |
| **1** | **Bịa đặt hoặc Gán sai mã YCCĐ** *(Hallucinated Codes)* | Tự sinh ra mã không có trong QĐ 2422 (như `6.C3.3` trong khi lớp 6 chỉ có đến C3.2), hoặc gán sai nội dung YCCĐ sang bài học không liên quan. | Đối soát tự động 1:1 với tệp cơ sở dữ liệu gốc `06_He_Thong_Ky_Thuat/extracted_data/qd2422_full.txt`. Sai lệch 1 ký tự phạt fail toàn bộ. |
| **2** | **Làm rơi rụng mã Mở rộng** *(Dropped MR Codes)* | Soạn đủ 12 tiết cốt lõi nhưng bỏ quên hoặc chỉ chọn vài mã `MR`, làm mất quyền lợi học tập của học sinh. | Chạy script kiểm đếm: Số lượng mã `VN-MR` trong PPCT 36 tiết phải bằng chính xác 100% số lượng mã `MR` ban hành tại QĐ 2422 cho khối lớp đó. |
| **3** | **Vi phạm Zero-Deviation (Dùng từ lóng)** *(Vocabulary Drift)* | Dùng từ ngữ tự do tiếng Anh hoặc tiếng lóng ("prompting tự do", "chém gió", "AI bịa", "chatbot", "RAG", "độ lệch"). | Rà quét từ khóa tự động; bắt buộc thay bằng 26 thuật ngữ chuẩn: *Câu lệnh*, *Ảo giác AI*, *Thiên lệch*, *Kỹ thuật RAG*... theo Phụ lục QĐ 2422. |
| **4** | **Trục xoắn ốc giả tạo (Lặp lại phẳng)** *(Fake Spiral Progression)* | Lớp 7 dạy lại y hệt định nghĩa AI hay phân loại dữ liệu của Lớp 6 mà không nâng tầng nhận thức hoặc không mở rộng ZPD. | Kiểm tra tính tăng tiến: Bài học lớp trên phải chỉ rõ 3 yếu tố nâng cấp: (1) Hiểu biết bản chất mới, (2) Thao tác mới, (3) Rủi ro/Đạo đức phức tạp hơn. |
| **5** | **Áp đặt thời lượng THCS cho Tiểu học** *(Time Mismatch)* | Thiết kế kịch bản bài học Tiểu học kéo dài 45 phút, bắt học sinh lớp 1–2 ngồi học nặng nề như học sinh cấp 2. | Bắt buộc định lượng: Lớp 1–2 tối đa 30–35 phút; Lớp 3–5 chuẩn 35 phút (CV 2345). Chỉ cấp THCS mới áp dụng khung 45 phút (CV 5512). |
| **6** | **Phân rã kỹ năng vượt chuẩn (Quá tải)** *(Over-scaffolding / Scope Creep)* | Đưa các thuật toán phức tạp (Backpropagation, code Python chuyên sâu) vào cấp THCS hoặc ép học sinh làm việc của kỹ sư AI. | Ràng buộc: Mọi tiểu kỹ năng (Micro-skills) ở SP2 phải giải nghĩa đúng động từ hành vi của QĐ 2422, tuyệt đối không đưa kiến thức vượt trần. |
| **7** | **Nội dung trôi nổi & YCCĐ mồ côi** *(Orphans & Unanchored Content)* | Đưa hoạt động trò chơi rất hay nhưng không gắn mã YCCĐ nào; hoặc có mã YCCĐ trong Khung nhưng không tiết nào dạy tới. | Bắt buộc Traceability 2 chiều: 100% YCCĐ phải có tiết dạy chính; 100% hoạt động bài dạy phải trỏ đúng về mã YCCĐ bảo trợ. |
| **8** | **Lý thuyết suông, thiếu kịch bản Unplugged** *(Over-reliance on Devices)* | Toàn bộ bài học đều phụ thuộc vào việc học sinh có máy tính và internet tốc độ cao, thiếu tính khả thi vùng khó khăn. | Bắt buộc Điều 10 `AGENTS.md`: 100% bài học phải có phương án Unplugged Fallback mô phỏng bằng thẻ bài/đóng vai theo đúng CV 5588. |

---

### 4. Bộ Câu hỏi Sát hạch Chuyên môn (Interrogation Prompts) dành cho Người Quản lý:

Khi người quản lý tiếp nhận bất kỳ sản phẩm nào từ đội ngũ, hãy sử dụng các câu hỏi sát hạch sau đây để "bắt lỗi" nhanh và đánh giá độ trung thực chuyên môn:

1. **Sát hạch Kiến trúc sư trưởng (SP1):**
   * *"Anh/Chị hãy chỉ rõ: YCCĐ này kế thừa từ lớp dưới ở điểm nào và chuẩn bị nền tảng nhận thức cho lớp trên ở điểm nào? Đối sánh với chuẩn UNESCO thì YCCĐ này nằm ở Dimension và Competency Level nào?"*
2. **Sát hạch Chuyên gia Phân rã Ma trận Kỹ năng (SP2):**
   * *"Tiểu kỹ năng này giúp học sinh bộc lộ hành vi gì cụ thể trên lớp? Có tình huống nào để đo lường độc lập giữa kỹ năng kỹ thuật và tư duy phản biện hay không? Bằng chứng đánh giá (Evidence) là gì?"*
3. **Sát hạch Chuyên gia Tiểu học (SP3A & SP4A):**
   * *"Bài này dạy trong 35 phút (hoặc 30–35 phút với lớp 1–2), nếu phòng máy hỏng hoặc mất mạng thì học sinh học bằng đồ dùng gì? Các câu hỏi đã bảo đảm ngôn từ trong sáng, phù hợp tâm lý lứa tuổi Tiểu học chưa?"*
4. **Sát hạch Chuyên gia THCS (SP3B & SP4B):**
   * *"Học sinh lưu vết minh chứng (prompt log) ở đâu trong tiết học này? Đã có kịch bản đối chứng nguồn tin cậy để vạch lỗi ảo giác của AI chưa? Tình huống bài học có vi phạm 18 Master Rules không?"*
5. **Sát hạch Trưởng ban QA/QC (Vị trí 5):**
   * *"Anh/Chị đã quét mã YCCĐ tự động chưa? Có mã nào bị cụt số (.MR) không? Đã đủ 100% mã mở rộng chưa? Có bài nào dùng từ ngoài 26 thuật ngữ chuẩn không? Đưa ra Biên bản thẩm định chi tiết!"*

---

## ĐIỀU 15. QUY TẮC VẬN HÀNH DÂY CHUYỀN SẢN XUẤT 4 KHÂU LIÊN HOÀN (STRICT 4-STAGE ASSEMBLY PIPELINE)

Để bảo đảm dự án đi đúng lộ trình, **tuyệt đối không rẽ nhánh lung tung, không thêm việc ngoài lề không cần thiết**, toàn bộ hệ thống bắt buộc phải vận hành theo kỷ luật cuốn chiếu nghiêm ngặt:

### 1. Bốn Nguyên tắc Vận hành Kỷ luật Thép:
1. **Nguyên tắc Khóa cổng (Gate-Lock Principle):**
   * Sản phẩm của Khâu trước là Đầu vào bất biến của Khâu sau. Khâu sau chỉ được phép khởi động khi Sản phẩm của Khâu trước đã được nghiệm thu và duyệt chính thức.
   * Tuyệt đối **KHÔNG LÀM NHẢY CÓC** (Ví dụ: Chưa xong SP1 đã vội soạn giáo án SP4; chưa phân rã Ma trận kỹ năng SP2 đã vội xếp thời khóa biểu SP3).
2. **Nguyên tắc "Một đường thẳng - Không rẽ nhánh" (No-Tangent Rule):**
   * Mọi nỗ lực và tài nguyên tính toán chỉ tập trung giải quyết đúng **Bộ 4 Sản phẩm cốt lõi (SP1 ➔ SP2 ➔ SP3 ➔ SP4)**.
   * Tuyệt đối không tự ý mở thêm các chuyên đề ngoài luồng, không tranh biện lý thuyết lan man, không viết tài liệu phụ trợ khi chưa hoàn thành 4 sản phẩm chính.
3. **Nguyên tắc Bắt buộc Chạy Kiểm định & Gửi kèm Báo cáo QA/QC (Mandatory Audit & Verification Report):**
   * Sau **MỖI LẦN LÀM XONG BẤT KỲ SẢN PHẨM NÀO** (từ SP1 đến SP4, từng khối lớp hay từng cụm bài):
     * **BẮT BUỘC PHẢI CHẠY KIỂM ĐỊNH THỰC TẾ:** Tự động chạy script kiểm đếm dữ liệu và đối soát qua 8 trụ cột chất lượng (Skill `ppct_qaqc_auditor`).
     * **BẮT BUỘC GỬI KÈM BIÊN BẢN KIỂM ĐỊNH (QA/QC AUDIT REPORT):** Ngay trong phản hồi bàn giao cho người dùng, phải trình bày đầy đủ bảng kết quả chấm điểm từng tiêu chí và kết luận phê duyệt/chưa đạt.
     * **LUẬT BẤT BIẾN:** Tuyệt đối không bàn giao sản phẩm suông mà không có báo cáo kiểm định đi kèm. Mọi khẳng định "đã đạt chuẩn" bắt buộc phải đi kèm bằng chứng đối soát thực tế.
4. **Cơ chế Tự động Nhắc việc Chuyển khâu (Automated Stage Handover):**
   * Khi một nhân sự hoàn thành sản phẩm ở khâu của mình:
     * *Bước 1:* Báo cáo tóm tắt sản phẩm bàn giao kèm **Bản báo cáo kiểm định chất lượng (QA/QC Audit Report)**.
     * *Bước 2:* Chủ động hiển thị **Prompt chuẩn hóa để người dùng giao việc cho Nhân sự ở Khâu tiếp theo**.
     * *Bước 3:* Chờ lệnh phê duyệt của người dùng trước khi triển khai khâu kế tiếp.

---

### 2. Bản đồ Trình tự 4 Khâu Liên hoàn:

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│ KHÂU 1: XÂY DỰNG SẢN PHẨM 1 - KHUNG CHƯƠNG TRÌNH CHUẨN K-9                       │
│ • Nhân sự: Vị trí 1 (Kiến trúc sư trưởng).                                       │
│ • Việc làm: Chạy chuỗi Tư duy ngầm 5 tầng (Bộ GD&ĐT + UNESCO + AI4K12 ➔ ZPD).   │
│ • Đầu ra bàn giao: Bảng Khung K-9 (STT, Lớp, Mạch, Chủ đề con, YCCĐ chuẩn hóa    │
│   tích hợp 100% chuẩn Bộ GD&ĐT kèm Chỉ số năng lực làm giàu quốc tế [INT-ENRICH]).│
│ ➔ HOÀN THÀNH: Nhắc người dùng kích hoạt Khâu 2.                                  │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ KHÂU 2: XÂY DỰNG SẢN PHẨM 2 - MA TRẬN KỸ NĂNG & MICRO-SKILLS K-9                 │
│ • Nhân sự: Vị trí 2 (Chuyên gia Phân rã Ma trận Kỹ năng).                        │
│ • Việc làm: Giải mã hành vi 3 nhánh: Kỹ thuật - Phản biện - Đạo đức.             │
│ • Đầu ra bàn giao: Bảng Ma trận Kỹ năng K-9 kèm Bằng chứng đánh giá (Evidence).  │
│ ➔ HOÀN THÀNH: Nhắc người dùng kích hoạt Khâu 3 (Tách phân hệ cấp học).           │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ KHÂU 3: TÁCH PHÂN HỆ ĐÓNG GÓI SẢN PHẨM SƯ PHẠM THEO CẤP HỌC                     │
│ ├─ KHÂU 3A (TIỂU HỌC L1–5):                                                      │
│ │  • Nhân sự: Vị trí 3 (Chuyên gia Tiểu học).                                    │
│ │  • Chuẩn: CV 2345, 30–35p/35p, 100% kịch bản Unplugged.                        │
│ │  • Đầu ra bàn giao: SP3A (PPCT 36 tiết) & SP4A (Lesson Specs Tiểu học).        │
│ └─ KHÂU 3B (THCS L6–9):                                                          │
│    • Nhân sự: Vị trí 4 (Chuyên gia THCS).                                        │
│    • Chuẩn: CV 5512, 45p, Prompt log, phòng chống deepfake.                      │
│    • Đầu ra bàn giao: SP3B (PPCT 36 tiết) & SP4B (Lesson Specs THCS).            │
│ ➔ HOÀN THÀNH: Nhắc người dùng kích hoạt Khâu 4 (Kiểm định độc lập).              │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ KHÂU 4: KIỂM ĐỊNH ĐỘC LẬP & RA QUYẾT ĐỊNH NGHIỆM THU CUỐI CÙNG                   │
│ • Nhân sự: Vị trí 5 (Trưởng ban Kiểm định QA/QC Độc lập).                        │
│ • Việc làm: Chạy script kiểm đếm, đối soát 8 trụ cột kỹ thuật.                   │
│ • Đầu ra bàn giao: Báo cáo Thẩm định (QA/QC Audit Report) & Lệnh Duyệt / VETO.   │
│ ➔ HOÀN THÀNH: Bàn giao toàn bộ gói sản phẩm hoàn chỉnh cho Người quản lý.        │
└──────────────────────────────────────────────────────────────────────────────────┘
```


