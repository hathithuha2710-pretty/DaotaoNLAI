# KHUNG KIẾN THỨC VÀ KỸ NĂNG GIÁO DỤC TRÍ TUỆ NHÂN TẠO (AI) THEO TRỤC DỌC
## CẤP TIỂU HỌC (LỚP 1 ĐẾN LỚP 5) — TIẾN TRÌNH PHÁT TRIỂN XOẮN ỐC (SPIRAL CURRICULUM)

> **CĂN CỨ PHÁP LÝ VÀ CHUYÊN MÔN CAO NHẤT (SINGLE SOURCE OF TRUTH):**
> 1. **Quyết định số 2422/QĐ-BGDĐT** (ngày 18/8/2026 của Bộ Giáo dục và Đào tạo) ban hành *"Khung nội dung giáo dục Trí tuệ nhân tạo cho học sinh phổ thông"*: Văn bản pháp lý và chuyên môn tối cao. Quy định mục tiêu, 4 mạch nội dung (A, B, C, D), danh mục 123 YCCĐ cấp Tiểu học (80 Cốt lõi + 43 Mở rộng) và 26 thuật ngữ chuẩn hóa tại Phụ lục.
> 2. **Công văn số 5588/BGDĐT-GDPT** (ngày 19/8/2026 của Bộ GD&ĐT) hướng dẫn triển khai thực tế từ năm học 2026-2027: Bố trí các chuyên đề giáo dục AI bắt buộc 12 tiết/lớp/năm học dành cho nội dung cốt lõi, bảo đảm công bằng tiếp cận hạ tầng và an toàn dữ liệu trẻ em.
> 3. **Công văn số 2345/BGDĐT-GDTH** (ngày 07/6/2021 của Bộ GD&ĐT) về xây dựng kế hoạch giáo dục nhà trường cấp Tiểu học (thời lượng tiết học 30–35 phút cho Lớp 1–2; 35 phút cho Lớp 3–5).
> 4. **Khung tham chiếu quốc tế cập nhật:** UNESCO AI Competency Framework for Students (2024), AI4K12 5 Big Ideas, Google DeepMind & Raspberry Pi Foundation (Experience AI), MIT RAISE (Day of AI), Common Sense Education, UNICEF Policy Guidance on AI for Children (v2.0), OECD Learning Compass 2030 và Singapore MOE NDLP.
> 5. **Nền tảng tâm lý học phát triển và sư phạm:** Tiến trình xoắn ốc của Jerome Bruner, Thuyết phát triển nhận thức Jean Piaget, Vùng phát triển gần (ZPD) Lev Vygotsky, Chu trình học tập trải nghiệm David Kolb và Thang đo hành vi Bloom cải biên (Anderson & Krathwohl).

---

## PHẦN I. NGUYÊN TẮC VẬN HÀNH VÀ BẢN ĐỒ MÃ HOÁ TỔNG THỂ

### 1. Mục đích và Định vị Văn kiện
Tài liệu này được thiết kế **hoàn toàn độc lập và tách biệt với Bảng ma trận kỹ năng v2.0**. Nếu Bảng ma trận v2.0 là bộ khung năng lực đầu ra, thì tài liệu này là **Bản kiến trúc tri thức và hành vi gốc (Master Knowledge & Behavioral Architecture)** chứa đựng toàn bộ chất liệu chuyên môn cho 5 năm học Tiểu học.
* **Tích hợp đồng bộ 3 thành phần sống còn:** (1) Hạt nhân tri thức khoa học chuẩn xác $\rightarrow$ (2) Biểu hiện kỹ năng vi mô và tiêu chí hoàn thành khả thi trong 35 phút $\rightarrow$ (3) Học liệu thực tế và đáp án đối chứng thực chứng.
* **Bảo đảm tính xoắn ốc (Spiral Curriculum):** Cùng một mạch năng lực, học sinh được tiếp cận lặp lại qua các năm học nhưng ở mức độ nhận thức sâu hơn, thao tác kỹ thuật phức tạp hơn, và phạm vi đạo đức xã hội rộng lớn hơn.

### 2. Ba Nguyên tắc Thiết kế Bất biến (Core Invariant Principles)

#### Nguyên tắc 1: Bảo toàn Độ chân xác Công nghệ (Technological Accuracy Principle)
* Sư phạm tiểu học cho phép *giản lược hóa ngôn từ* cho vừa sức trẻ thơ, nhưng **tuyệt đối không được bóp méo bản chất khoa học máy tính**.
* **Đính chính các quan niệm sai lệch thường gặp:**
  * ❌ *Sai:* Mô hình ngôn ngữ lớn (Chatbot) mỗi lần trả lời đều lên mạng tìm kiếm từ ngữ hay đi liền nhau để ghép câu. $\rightarrow$ ✅ *Đúng:* Chatbot tạo văn bản dựa trên những mẫu dữ liệu đã học trong quá trình huấn luyện từ trước (Training patterns); máy tính toán xác suất từ tiếp theo dựa trên trọng số mô hình chứ không phải luôn tìm kiếm web trực tiếp thời gian thực.
  * ❌ *Sai:* Máy móc không có cảm xúc nên không biết giữ bí mật. $\rightarrow$ ✅ *Đúng:* An toàn thông tin phụ thuộc vào kiến trúc thiết kế, thuật toán và chính sách quản lý dữ liệu của con người; máy móc chỉ là công cụ tính toán thừa hành thuật toán.
  * ❌ *Sai:* Mọi lời nói, hình ảnh đều bị ghi lại và gửi lên mạng máy chủ. $\rightarrow$ ✅ *Đúng:* Nhiều ứng dụng AI xử lý dữ liệu trực tiếp tại thiết bị (On-device processing) mà không gửi dữ liệu ra ngoài.
  * ❌ *Sai:* Che vạch đen ngang mắt là bảo đảm ẩn danh 100%. $\rightarrow$ ✅ *Đúng:* Khử nhận dạng cá nhân là một phổ kỹ thuật kết hợp (cắt ảnh, xóa tên, chụp riêng vật thể, loại bỏ thông tin định danh); không có giải pháp nào là tuyệt đối nếu còn sót lại các đặc điểm kết hợp khác.

#### Nguyên tắc 2: Giới hạn Phạm vi Tiết học (Lesson-Scope Boundary Principle)
* Phân định rạch ròi giữa **Đích năng lực của cả năm học** và **Sản phẩm đầu ra khả thi trong 30–35 phút của một tiết học**.
* *Ví dụ:* Đích cả năm của Lớp 5 là thu thập 30–40 ảnh/nhãn cho dự án tốt nghiệp. Trong 01 tiết học 35 phút về Chuẩn bị dữ liệu, giáo viên phải chuẩn bị sẵn tập ảnh thô (12–14 ảnh) có cài cắm lỗi; học sinh thực hành phân loại, crop ảnh và chụp bổ sung 2 ảnh để hoàn thiện tập mẫu 8–10 ảnh sạch. Tiết sau sẽ dùng tập ảnh này để nạp vào máy huấn luyện.

#### Nguyên tắc 3: Minh chứng Thực chứng (Empirical Evidence Principle)
* Năng lực chỉ được xác nhận khi học sinh **tạo ra một sản phẩm học tập cụ thể hoặc có hành động quan sát được**, không đo bằng việc đọc đồng thanh khẩu hiệu hay dán cam kết hình thức.
* Mỗi bài học phải có: Phiếu kiểm chứng có cấu trúc, Thư mục dữ liệu đã làm sạch, Bảng ma trận kiểm thử, hoặc hành vi bấm nút dừng lại và từ chối nói thông tin bí mật.

---

### 3. Bản đồ Ánh xạ 8 Trục Năng Lực Dọc $\times$ 46 Kỹ Năng $\times$ 123 YCCĐ QĐ 2422

| Trục Năng Lực Dọc | Kỹ Năng Ma Trận v2.0 Tương Ứng | Khối Lớp & Mã YCCĐ QĐ 2422 Bao Phủ |
| :--- | :--- | :--- |
| **TRỤC 1: Nhận thức về AI, Phân biệt Người – Máy & Giới hạn công nghệ** | KN1, KN3, KN17, KN18, KN19, KN20, KN21, KN27 | **Lớp 1:** 1.A1.1, 1.A1.2, 1.A1.3, 1.A1.4, 1.A2.1, 1.A2.2, 1.A2.3, 1.C1.1, 1.C1.3<br>**Lớp 2:** 2.A1.1, 2.A1.3, 2.A1.4, 2.A2.1, 2.A2.2, 2.A2.MR1, 2.C1.1, 2.C1.MR1<br>**Lớp 3:** 3.A2.1, 3.A2.2, 3.A2.3, 3.A2.MR1, 3.A2.MR2, 3.C1.1<br>**Lớp 4:** 4.A1.1, 4.A1.2, 4.A2.1, 4.A2.2<br>**Lớp 5:** 5.A1.1, 5.A2.1, 5.A2.2, 5.A2.3, 5.A2.MR1 |
| **TRỤC 2: An toàn số, Bảo vệ Quyền riêng tư & Xử lý sự cố** | KN8, KN9, KN10, KN12 | **Lớp 1:** 1.B1.1 (tích hợp), 1.C1.2<br>**Lớp 2:** 2.A1.2, 2.A2.MR2, 2.B3.MR1<br>**Lớp 3:** 3.A1.4, 3.A1.MR3, 3.B2.1<br>**Lớp 4:** 4.B2.1, 4.B2.2<br>**Lớp 5:** 5.A1.2, 5.B2.MR1, 5.D1.1 (tích hợp khử nhận dạng) |
| **TRỤC 3: Đạo đức AI, Văn hóa số & Trách nhiệm giải trình** | KN7, KN13, KN14, KN15, KN16, KN24, KN26, KN45, KN46 | **Lớp 1:** 1.B1.1, 1.B3.1, 1.B3.2<br>**Lớp 2:** 2.B1.1, 2.B1.MR1, 2.B1.MR2, 2.B3.1, 2.B3.2, 2.B3.MR2<br>**Lớp 3:** 3.B3.1, 3.B3.MR1<br>**Lớp 4:** 4.A1.2, 4.C2.1 (ghi nguồn), 4.D2.1<br>**Lớp 5:** 5.A1.1, 5.A1.2, 5.A1.MR1, 5.B1.1, 5.B1.2, 5.B2.1, 5.B3.1, 5.D2.1 |
| **TRỤC 4: Tự chủ tư duy & Chống ỷ lại nhận thức công nghệ** | KN42, KN43, KN44 | **Lớp 1:** 1.A1.2 (tự giác)<br>**Lớp 2:** 2.A1.2, 2.A2.MR3<br>**Lớp 3:** 3.A1.3, 3.A1.4, 3.A1.5, 3.A1.MR2<br>**Lớp 4:** 4.A3.1<br>**Lớp 5:** 5.A3.1, 5.A3.2 |
| **TRỤC 5: Đánh giá, Kiểm chứng thông tin & Phòng ngừa Ảo giác, Deepfake** | KN11, KN22, KN23, KN25 | **Lớp 1:** 1.C1.3 (nhận diện nhầm)<br>**Lớp 2:** 2.C3.2 (nguyên nhân máy sai)<br>**Lớp 3:** 3.A3.1, 3.A3.2, 3.B2.1 (ảo giác AI)<br>**Lớp 4:** 4.B2.1 (deepfake), 4.A1.1<br>**Lớp 5:** 5.C5.2 (kiểm thử), 5.C5.MR3 (đánh giá mô hình) |
| **TRỤC 6: Giao tiếp với AI & Kỹ thuật đặt Câu lệnh (Prompting)** | KN2, KN4, KN5, KN6, KN39 | **Lớp 1:** 1.C1.2, 1.C1.4, 1.A2.MR1<br>**Lớp 2:** 2.A3.1, 2.A2.MR1, 2.A3.MR1<br>**Lớp 3:** 3.C2.1 (câu lệnh rõ việc)<br>**Lớp 4:** 4.C2.1, 4.C2.MR1 (lệnh 3 thành phần, AutoDraw)<br>**Lớp 5:** 5.C2.1, 5.C5.1 (lệnh 4 thành phần, Few-shot) |
| **TRỤC 7: Dữ liệu học máy — Thu thập, Gán nhãn, Làm sạch & Đa dạng hóa** | KN28, KN29, KN30, KN31, KN32 | **Lớp 1:** 1.D1.1, 1.D1.MR1, 1.D2.1, 1.D2.2<br>**Lớp 2:** 2.C3.1, 2.D2.1, 2.D2.2, 2.D1.MR1, 2.D2.MR1<br>**Lớp 3:** 3.C4.1, 3.C4.MR1, 3.C5.2, 3.C5.3, 3.C5.4, 3.D2.1, 3.D2.MR1<br>**Lớp 4:** 4.D1.1, 4.D2.1<br>**Lớp 5:** 5.B1.1, 5.B2.MR1, 5.D1.1, 5.D2.1, 5.D2.MR1 |
| **TRỤC 8: Vận hành Học máy, Kiểm thử & Thiết kế hệ thống (AI Lifecycle)** | KN33, KN34, KN35, KN36, KN37, KN38, KN40, KN41 | **Lớp 1:** 1.D1.1, 1.D2.1, 1.D2.2<br>**Lớp 2:** 2.C3.MR1, 2.D1.1, 2.D1.2<br>**Lớp 3:** 3.C5.1, 3.C5.MR1, 3.C5.2, 3.C5.MR2, 3.D1.1, 3.D2.1<br>**Lớp 4:** 4.D1.1, 4.D2.1<br>**Lớp 5:** 5.C5.1, 5.C5.MR1, 5.C5.2, 5.C5.MR2, 5.D1.1, 5.D2.1, 5.D2.MR1 |

---

## TRỤC 1: NHẬN THỨC VỀ AI, PHÂN BIỆT NGƯỜI – MÁY VÀ GIỚI HẠN CÔNG NGHỆ

### 1. Bản chất Khoa học & Định hướng Tiến trình Xoắn ốc
* **Bản chất khoa học công nghệ:** Trí tuệ nhân tạo (AI) là lĩnh vực khoa học máy tính nhằm xây dựng các hệ thống có khả năng thực hiện các tác vụ vốn đòi hỏi trí thông minh con người (nhận biết hình ảnh, nhận dạng tiếng nói, đưa ra quyết định, phân loại dữ liệu). Tuy nhiên, máy móc chỉ xử lý các phép toán và thuật toán trên dữ liệu, máy **không có ý thức (consciousness)**, **không có cảm xúc sinh học (biological emotions)**, và **không có khả năng thấu cảm hay trải nghiệm sống**.
* **Tiến trình xoắn ốc (Grades 1 to 5):**
  * *Lớp 1:* Trực quan – Cảm xúc: Nhận biết sự khác biệt giữa cảm xúc thật của con người và phản ứng mô phỏng của máy; nhận diện thiết bị thông minh quanh em (100% Unplugged).
  * *Lớp 2:* Mở rộng sang gia đình: Nhận biết AI hỗ trợ các thành viên trong gia đình; hiểu rằng con người luôn phải quan sát và hỗ trợ máy khi máy gặp sự cố vật lý/kỹ thuật.
  * *Lớp 3:* AI học đường và cảm biến dữ liệu: Hiểu AI "nhìn" bằng Camera và "nghe" bằng Micro; khẳng định AI hỗ trợ học tập chứ không thể thay thế tình cảm và sự khích lệ của thầy cô.
  * *Lớp 4:* AI trong các ngành nghề xã hội: Phân tích các trường hợp bác sĩ, nông dân dùng AI; xác lập nguyên tắc tối thượng: AI đề xuất gợi ý – Con người ra quyết định và chịu trách nhiệm.
  * *Lớp 5:* Triết học công nghệ và tính bao trùm: Khẳng định vai trò chủ đạo của con người (Human Agency); thiết kế giải pháp AI nhân văn hỗ trợ người yếu thế; nhận thức rõ những giá trị nhân văn cốt lõi mà công nghệ không thể thay thế.

---

### 2. Chi tiết Tiến trình 5 Khối Lớp của Trục 1

#### LỚP 1 — KHÁM PHÁ CẢM XÚC VÀ THIẾT BỊ QUANH EM
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `1.A1.1`: *Nhận biết được rằng con người có cảm xúc (vui, buồn, sợ hãi...) còn máy móc thì không.*
  * `1.A1.2`: *Nêu được ví dụ đơn giản về việc máy móc chỉ làm theo những gì con người đã cài đặt/lập trình sẵn.*
  * `1.A1.3`: *Nhận biết được rằng nụ cười, lời chào hay giọng nói của robot là do con người tạo ra.*
  * `1.A1.4`: *Nêu được rằng con người sáng tạo ra máy móc để phục vụ cuộc sống.*
  * `1.A2.1`: *Nêu được một vài cách mà thiết bị thông minh thể hiện sự thân thiện (như phát nhạc vui vẻ, nháy đèn, nói lời chào).*
  * `1.A2.2`: *Kể được tên một vài thiết bị thông minh quen thuộc xung quanh em (như điện thoại thông minh, tivi thông minh, loa thông minh).*
  * `1.A2.3`: *Nêu được một số lợi ích đơn giản của các thiết bị đó trong sinh hoạt hằng ngày.*
  * `1.C1.1`: *Chỉ ra được camera là 'mắt' giúp máy nhìn thấy, micro là 'tai' giúp máy nghe thấy.*
  * `1.C1.3`: *Nhận biết được rằng máy móc có thể nhìn nhầm hoặc nghe nhầm khi ánh sáng tối hoặc xung quanh quá ồn ào.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 1 (M1)`, `KN 18 (M1)`, `KN 19 (M1)`, `KN 20 (M1)`, `KN 27 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Người có cảm xúc thật - Robot chỉ có hành động mô phỏng:* Con người biết vui, buồn, đau, cười xuất phát từ trái tim và cơ thể; Robot chỉ chớp mắt hay phát tiếng cười vui nhộn vì có một kỹ sư đã viết lệnh và nạp file âm thanh vào chip nhớ bên trong.
  * *Đơn vị 2: Thiết bị thông minh phục vụ con người:* Điện thoại thông minh giúp bố mẹ gọi video cho ông bà; Tivi thông minh mở bài hát thiếu nhi khi em nói vào điều khiển; Loa thông minh trả lời dự báo thời tiết. Máy móc được con người chế tạo ra để giúp cuộc sống tiện lợi hơn.
  * *Đơn vị 3: Mắt Camera và Tai Micro:* Máy móc không có mắt thịt, tai thịt; máy dùng ống kính camera để thu nhận hình ảnh và micro để thu nhận tiếng động.
  * *Hiểu lầm cần tránh:* Không để học sinh lầm tưởng robot đồ chơi biết buồn khi bị bỏ rơi hoặc robot là một sinh vật sống có linh hồn.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Quan sát 4 tranh vẽ nét mặt (Em bé cười, Em bé mếu máo, Robot vẽ mặt cười, Loa nhấp nháy đèn), chỉ đúng và phân loại: 2 tranh cảm xúc thật vs 2 tranh máy mô phỏng.
  * *Hành vi 2:* Chỉ đúng vị trí "mắt camera" và "tai micro" trên chiếc điện thoại/mô hình loa thông minh của lớp học.
  * *Tiêu chí hoàn thành:* Phân biệt đúng 100% cảm xúc thật vs mô phỏng; gọi tên chính xác chức năng camera và micro.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bộ thẻ tranh A5:* Tranh A (Bé Mai bị ngã trầy đầu gối khóc nhè), Tranh B (Chú robot đồ chơi phát tiếng tít tít nháy đèn vàng), Tranh C (Mẹ ôm bé mỉm cười âu yếm), Tranh D (Màn hình máy tính bảng hiện mặt cười màu xanh).
  * *Đáp án giáo viên:* Thẻ A & C $\rightarrow$ Cảm xúc thật của con người; Thẻ B & D $\rightarrow$ Máy móc làm theo lập trình của con người.
* **Tiến trình Xoắn ốc:** Điểm khởi đầu: Nhận thức cảm xúc và phân biệt cơ học giữa Người và Máy (100% Unplugged).

---

#### LỚP 2 — AI TRONG GIA ĐÌNH VÀ VAI TRÒ GIÁM SÁT CỦA CON NGƯỜI
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `2.A1.1`: *Kể được một số tình huống trong gia đình mà thiết bị thông minh có thể hỗ trợ (như bật đèn tự động, tra cứu thời tiết, mở bài hát yêu thích).*
  * `2.A1.3`: *Nêu được ví dụ về việc con người cần quan sát, hỗ trợ hoặc điều khiển khi thiết bị thông minh gặp trục trặc.*
  * `2.A1.4`: *Thể hiện thái độ đúng đắn: Tôn trọng người sáng tạo, giữ gìn thiết bị cẩn thận, không cáu gắt hay đập phá khi máy báo lỗi.*
  * `2.A2.1`: *Nhận biết được biểu tượng micro hoặc các nút kích hoạt tính năng thông minh trên điều khiển tivi, loa thông minh.*
  * `2.A2.2`: *Kể tên các thành viên trong gia đình mà AI có thể giúp đỡ (ông bà, bố mẹ, em nhỏ).*
  * `2.A2.MR1`: *Thực hành ra lệnh đơn giản bằng giọng nói cho thiết bị thông minh dưới sự giám sát của giáo viên.*
  * `2.C1.1`: *Giải thích được ở mức đơn giản: Dữ liệu là những hình ảnh, âm thanh hoặc chữ viết mà con người cung cấp để máy học.*
  * `2.C1.MR1`: *So sánh được cách học của con người (qua trải nghiệm, thầy cô dạy) với cách học của máy (qua quét dữ liệu mẫu).*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 1 (M1)`, `KN 3 (M1)`, `KN 7 (M1)`, `KN 19 (M1)`, `KN 20 (M1)`, `KN 21 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: AI trong đời sống gia đình:* Thiết bị AI gia đình giúp ông bà nghe đọc báo khi mắt mờ; giúp bố mẹ hẹn giờ tắt điều hòa tiết kiệm điện; giúp con nhỏ nghe đọc truyện cổ tích.
  * *Đơn vị 2: Con người thông thái giám sát máy móc:* Robot hút bụi dù thông minh nhưng khi gặp dây điện rơi trên sàn hoặc chân ghế hẹp sẽ bị kẹt và kêu bíp bíp; máy điều hòa tự động có thể cảm biến sai nhiệt độ khi có ánh nắng gắt chiếu vào. Con người phải luôn ở vị trí giám sát, nhấc máy ra khỏi chỗ kẹt, vệ sinh cảm biến và điều chỉnh lại.
  * *Đơn vị 3: Thái độ văn minh với công nghệ:* Khi máy nhận sai giọng nói hoặc báo lỗi, em không được la hét, giậm chân hay đập điều khiển; cần bình tĩnh kiểm tra lại đường truyền mạng hoặc nhờ bố mẹ trợ giúp.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Nối đúng 3 thành viên gia đình (Ông bà, Bố mẹ, Em nhỏ) với 3 nhu cầu hỗ trợ công nghệ phù hợp.
  * *Hành vi 2:* Đóng vai xử lý tình huống: Khi robot hút bụi báo đèn đỏ kêu 'tít tít' vì kẹt khăn lau chân, học sinh chạy lại tắt công tắc nguồn, gỡ khăn ra và đặt robot lại mặt sàn phẳng.
  * *Tiêu chí hoàn thành:* Nêu được lý do con người phải can thiệp; thể hiện thái độ bình tĩnh bảo vệ thiết bị.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Video/Tranh mô phỏng:* Video 20 giây quay cảnh robot hút bụi bị kẹt góc thảm; Thẻ tranh 3 thành viên gia đình và các thiết bị số.
  * *Đáp án:* Khi máy kẹt $\rightarrow$ Cần con người gỡ rối và bấm chạy lại. Máy không thể tự thoát nếu không có con người hỗ trợ vật lý.
* **Tiến trình Xoắn ốc:** Mở rộng từ bản thân sang không gian Gia đình; nhận thức được sự cố kỹ thuật và xác lập vai trò giám sát, bảo vệ thiết bị của con người.

---

#### LỚP 3 — AI TRONG TRƯỜNG HỌC VÀ KHÁM PHÁ CÔNG CỤ DỰA TRÊN DỮ LIỆU
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `3.A2.1`: *Nhận biết được một số ứng dụng hoặc thiết bị AI trong môi trường trường học (như điểm danh bằng khuôn mặt, phần mềm luyện phát âm ngoại ngữ, robot hỗ trợ lễ tân).*
  * `3.A2.2`: *Nêu được mục đích của việc sử dụng AI trong trường học là hỗ trợ học sinh học tập tốt hơn và giúp thầy cô quản lý thuận tiện hơn.*
  * `3.A2.3`: *Trình bày được rằng AI không thể thay thế thầy cô giáo vì chỉ thầy cô mới có tình yêu thương, sự thấu hiểu và truyền cảm hứng cho học sinh.*
  * `3.A2.MR1`: *Mô tả được ý tưởng về trường học tương lai nơi có sự đồng hành của AI nhưng vẫn giữ trọn vẹn tình cảm thầy trò.*
  * `3.A2.MR2`: *Đề xuất được một số quy tắc học đường khi sử dụng các công cụ AI trong học tập.*
  * `3.C1.1`: *Mô tả được các đặc điểm chính của công cụ AI: Hoạt động dựa trên dữ liệu con người cung cấp, có khả năng nhận dạng và phản hồi tự động.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 1 (M2)`, `KN 3 (M2)`, `KN 17 (M1)`, `KN 19 (M2)`, `KN 20 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Hệ thống AI trường học:* Điểm danh thông minh quét khuôn mặt giúp lớp học vào giờ nhanh chóng; phần mềm tiếng Anh lắng nghe phát âm và chỉ ra từ nào đọc chưa chuẩn; camera an ninh cổng trường nhận diện người lạ.
  * *Đơn vị 2: Ranh giới bất biến - Thầy cô là duy nhất:* Phần mềm có thể dịch hàng nghìn từ vựng trong 1 giây, nhưng máy tính không biết khen ngợi khi em tiến bộ, không biết an ủi khi em buồn, không dạy em lòng nhân ái. Công nghệ chỉ là công cụ hỗ trợ (Assistant), thầy cô là người dẫn dắt (Leader).
  * *Đơn vị 3: Ý tưởng công nghệ nhân văn:* Thiết kế ý tưởng công cụ AI hỗ trợ bạn học bị khiếm thị (kính thông minh phát âm thanh báo chướng ngại vật phía trước).
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Phân loại 6 hoạt động học đường vào 2 cột: Cột 1 "AI có thể hỗ trợ hiệu quả" (Chấm trắc nghiệm nhanh, gợi ý từ điển, điểm danh) vs Cột 2 "Chỉ thầy cô và bạn bè mới làm được" (Chia sẻ nỗi buồn, uốn nắn đạo đức, truyền lửa đam mê).
  * *Hành vi 2:* Vẽ sơ đồ khối nhanh ý tưởng 1 thiết bị AI trường học hỗ trợ bạn học khuyết tật.
  * *Tiêu chí hoàn thành:* Phân biệt chính xác ranh giới năng lực máy vs con người; sơ đồ ý tưởng nêu rõ: Thiết bị giúp ai? Giúp việc gì?
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Phiếu phân loại A4:* 6 thẻ hành động in sẵn; Giấy vẽ sơ đồ ý tưởng A4.
  * *Đáp án:* 100% học sinh khẳng định không dùng AI thay thế thầy cô trong việc dạy đạo đức và cảm xúc.
* **Tiến trình Xoắn ốc:** Mở rộng sang môi trường Giáo dục; hiểu AI vận hành dựa trên dữ liệu; xác lập vị trí không thể thay thế của giáo viên và tình cảm con người.

---

#### LỚP 4 — AI TRONG CÁC NGÀNH NGHỀ XÃ HỘI VÀ VAI TRÒ RA QUYẾT ĐỊNH
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `4.A1.1`: *Nêu được một số lĩnh vực nghề nghiệp trong đời sống có sự hỗ trợ của AI (y tế, nông nghiệp, giao thông, môi trường, sản xuất).*
  * `4.A1.2`: *Trình bày được rằng trong mọi lĩnh vực nghề nghiệp, AI chỉ là công cụ trợ giúp, con người luôn giữ vai trò quyết định cuối cùng và chịu trách nhiệm.*
  * `4.A2.1`: *Trình bày được các đối tượng trong xã hội được AI hỗ trợ (bác sĩ chẩn đoán, nông dân chăm sóc mùa màng, người khuyết tật hòa nhập).*
  * `4.A2.2`: *Khẳng định được AI không thể thay thế sự sáng tạo nghệ thuật đích thực và lòng trắc ẩn của con người.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 3 (M2)`, `KN 17 (M2)`, `KN 18 (M3)`, `KN 19 (M3)`, `KN 38 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: AI trong thế giới nghề nghiệp thực tế:*
    * Y tế: Phần mềm AI hỗ trợ khoanh vùng tổn thương trên phim chụp phổi X-quang.
    * Nông nghiệp: Máy bay không người lái dùng camera AI phát hiện lá cây bị sâu bệnh để phun thuốc chính xác từng cụm.
    * Giao thông: Hệ thống camera AI tự động đếm lưu lượng xe để điều chỉnh thời gian đèn xanh đèn đỏ chống ùn tắc.
  * *Đơn vị 2: Nguyên tắc Con người quyết định cuối cùng (Human-in-the-loop):* Phần mềm y tế có thể đề xuất 3 khả năng bệnh tật, nhưng Bác sĩ phải khám lâm sàng, hỏi han tiền sử bệnh nhân, cân nhắc thể trạng để đưa ra phác đồ điều trị cuối cùng. Nếu máy sai, bác sĩ là người chịu trách nhiệm trước pháp luật và sinh mạng bệnh nhân.
  * *Đơn vị 3: Sự thấu cảm nghề nghiệp:* Người bác sĩ có cái nắm tay động viên người bệnh; chú cảnh sát giao thông biết linh hoạt nhường đường cho xe cấp cứu – những quyết định nhân văn mà thuật toán cứng nhắc không làm được.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Đọc bản tóm tắt tình huống y tế (Bệnh án giả lập: AI báo 80% viêm phổi, nhưng bác sĩ phát hiện bệnh nhân bị hen suyễn do dị ứng thời tiết); giải thích vì sao quyết định của bác sĩ đúng đắn hơn máy.
  * *Hành vi 2:* Lập ma trận so sánh 2 cột: "Việc AI làm tốt" (Tốc độ quét hàng nghìn bức ảnh, tính toán số liệu) vs "Việc chỉ chuyên gia con người làm được" (Thấu cảm, xét đoán đạo đức, chịu trách nhiệm pháp lý).
  * *Tiêu chí hoàn thành:* Trình bày rõ ràng lập luận: AI là cánh tay nối dài, con người là bộ não chỉ huy.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bản Case study Y khoa A4:* Câu chuyện ngắn 150 chữ về Bác sĩ Hùng và trợ lý AI phân tích phim X-quang.
  * *Đáp án:* Quyết định điều trị thuộc về Bác sĩ Hùng. Máy tính không phải pháp nhân chịu trách nhiệm y khoa.
* **Tiến trình Xoắn ốc:** Mở rộng ra các Ngành nghề xã hội phức tạp; xác lập cơ chế phân quyền: AI gợi ý đề xuất $\rightarrow$ Chuyên gia con người thẩm định và chịu trách nhiệm.

---

#### LỚP 5 — TƯ DUY LÀM CHỦ CÔNG NGHỆ VÀ TRÍ TUỆ NHÂN VĂN
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `5.A1.1`: *Trình bày được rằng AI có thể thực hiện một số công việc thay con người trong điều kiện nhất định nhưng con người luôn giữ vai trò chủ đạo.*
  * `5.A2.1`: *Giải thích được mục đích chính của AI là hỗ trợ con người nâng cao năng suất, giải phóng sức lao động để con người tập trung vào công việc sáng tạo.*
  * `5.A2.2`: *Trình bày được rằng AI được tạo ra nhằm phục vụ lợi ích chung của cộng đồng, bảo đảm tính nhân văn và không bỏ lại ai phía sau.*
  * `5.A2.3`: *Nêu được ví dụ cụ thể về việc AI mang lại lợi ích cho cộng đồng (cảnh báo sạt lở lũ quét, trợ lý ảo hỗ trợ người khiếm thị đọc báo).*
  * `5.A2.MR1`: *Thảo luận được về những phẩm chất và năng lực độc hữu của con người (lòng trắc ẩn, trực giác, tính chính trực, lương tâm) mà AI không bao giờ có thể sao chép được.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 3 (M3)`, `KN 17 (M3)`, `KN 18 (M3)`, `KN 46 (M3)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Vai trò chủ đạo của con người (Human Agency & Oversight):* Con người đặt ra mục tiêu cho AI, con người chọn dữ liệu dạy AI, con người kiểm tra kết quả và con người có quyền tắt công tắc hệ thống nếu AI hoạt động sai lệch.
  * *Đơn vị 2: AI vì sự tiến bộ xã hội (AI for Social Good):* Các dự án AI cứu hộ: Sử dụng ảnh vệ tinh AI phát hiện điểm sạt lở đèo núi để cứu dân trước bão; vòng đeo tay AI cảnh báo cơn co giật cho trẻ em mắc bệnh hiểm nghèo.
  * *Đơn vị 3: Nhân tính là cốt lõi:* Trí tuệ máy móc là trí tuệ tính toán (Computational intelligence); trí tuệ con người là trí tuệ cảm xúc, đạo đức và lương tâm (Human wisdom). Máy có thể thông minh hơn về tốc độ nhớ số liệu, nhưng con người vĩ đại ở năng lực yêu thương và lẽ sống.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Thảo luận nhóm 4 học sinh: Phân tích dự án "Camera AI cảnh báo rác thải đại dương", chỉ ra mục đích nhân văn và vai trò giám sát của tình nguyện viên môi trường.
  * *Hành vi 2:* Viết đoạn tuyên ngôn ngắn (3–4 câu) của bản thân về chủ đề: *"Là công dân số tương lai, em làm chủ công nghệ như thế nào?"*.
  * *Tiêu chí hoàn thành:* Sử dụng đúng các khái niệm: Nâng cao năng suất, giải phóng sức lao động, con người giữ vai trò chủ đạo, bảo đảm tính nhân văn.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Infographic:* Sơ đồ "Mô hình hợp tác Người - AI vì cộng đồng"; Phiếu Tuyên ngôn công dân số A5.
  * *Đáp án:* Minh chứng khẳng định: AI là phương tiện, Hạnh phúc và Tiến bộ của Con người là mục đích tối thượng.
* **Tiến trình Xoắn ốc:** Đỉnh cao cấp Tiểu học: Tư duy triết học công nghệ nhân bản; làm chủ bản thân, làm chủ công nghệ sẵn sàng chuyển tiếp lên cấp THCS.

---

## TRỤC 2: AN TOÀN SỐ, BẢO VỆ QUYỀN RIÊNG TƯ VÀ XỬ LÝ SỰ CỐ

### 1. Bản chất Khoa học & Định hướng Tiến trình Xoắn ốc
* **Bản chất khoa học công nghệ:** Dữ liệu cá nhân (Personal Data) là tài sản số vô giá và là mục tiêu thu thập của các mô hình học máy. Các hệ thống thông minh cần dữ liệu người dùng để cải thiện thuật toán gợi ý và quảng cáo mục tiêu. Tuy nhiên, việc rò rỉ dữ liệu cá nhân có thể dẫn đến đánh cắp danh tính, lừa đảo tài chính, thao túng tâm lý và mất an toàn thể chất. Khử nhận dạng dữ liệu cá nhân (Anonymization) và vệ sinh an toàn số (Cyber Hygiene) là những kỹ thuật nền tảng để bảo vệ con người trong thế giới kết nối.
* **Tiến trình xoắn ốc (Grades 1 to 5):**
  * *Lớp 1:* Phản xạ tự vệ hành vi: Nhận diện thông tin bí mật; dứt khoát nói KHÔNG và dừng lại khi máy hỏi chuyện riêng (100% Unplugged).
  * *Lớp 2:* Ý thức sở hữu số và nguyên tắc đồng thuận: Tôn trọng tài khoản và sản phẩm số của bạn bè; phải xin phép trước khi chụp ảnh người khác; quy trình 2 bước khi gặp sự cố số.
  * *Lớp 3:* Nhận diện bẫy thu thập dữ liệu: Phân loại dữ liệu công khai vs dữ liệu nhạy cảm; gạch bỏ thông tin nhạy cảm trên phiếu biểu mẫu số.
  * *Lớp 4:* Quản trị quyền riêng tư ứng dụng: Cơ chế cấp quyền ứng dụng (Permissions); phân tích hậu quả thực tế của lộ lọt dữ liệu; thiết lập mật khẩu mạnh.
  * *Lớp 5:* Kỹ thuật Khử nhận dạng dữ liệu cá nhân chuyên nghiệp: Thực hành Crop ảnh, che mờ mặt/tên, loại bỏ siêu dữ liệu định danh khi xây dựng tập dữ liệu cho dự án AI.

---

### 2. Chi tiết Tiến trình 5 Khối Lớp của Trục 2

#### LỚP 1 — BẢO VỆ BÍ MẬT CÁ NHÂN VÀ PHẢN XẠ NÓI KHÔNG
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `1.B1.1` (Tích hợp): *Nêu được một vài việc không nên làm khi dùng thiết bị thông minh (không tự ý cung cấp thông tin riêng).*
  * `1.C1.2`: *Thực hiện được việc nói câu lệnh đơn giản, rõ ràng vào micro để thiết bị thông minh nhận biết.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 8 (M1)`, `KN 9 (M1)`, `KN 12 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Nhận diện bí mật cá nhân:* Họ tên đầy đủ, địa chỉ nhà (số nhà, tên đường phố), số điện thoại bố mẹ, mật khẩu mở máy tính bảng, và hình ảnh riêng tư cơ thể em là những thông tin bí mật tuyệt đối gắn với an toàn tính mạng của em.
  * *Đơn vị 2: Thông tin chia sẻ được:* Tên gọi ở nhà, màu sắc em yêu thích, con vật em thích, bài hát em muốn nghe là thông tin vui vẻ, em có thể nói cho máy thông minh nghe.
  * *Đơn vị 3: Quy tắc ứng xử an toàn:* Cỗ máy kết nối mạng có thể gửi lời nói ra ngoài; tuyệt đối không tự ý nói thông tin bí mật cho loa/ứng dụng lạ; khi máy hỏi $\rightarrow$ **Dừng lại, nói "KHÔNG" và gọi bố mẹ/cô giáo**.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Chơi trò chơi "Hộp Xanh hay Hộp Đỏ": Phân loại chính xác 4 thẻ thông tin bí mật vào Hộp Đỏ và 2 thẻ sở thích vào Hộp Xanh.
  * *Hành vi 2:* Tình huống đóng vai: Giáo viên bật loa đồ chơi hỏi: *"Bé ơi nhà ở đâu? Cho xin số điện thoại của mẹ để nhận quà nào!"*. Học sinh khoanh 2 tay trước ngực, lắc đầu nói to, dứt khoát: *"KHÔNG! Con không được nói!"*.
  * *Tiêu chí hoàn thành:* Thao tác phân loại đạt 100%; phản xạ nói "KHÔNG" dứt khoát, không ngập ngừng khai báo thông tin thật.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bộ 6 thẻ tranh:* Tranh 1 (Số nhà 12 phố Hoa Hồng), Tranh 2 (Số điện thoại 0912...), Tranh 3 (Bức vẽ con mèo em thích), Tranh 4 (Mật khẩu ****), Tranh 5 (Bát phở em thích ăn), Tranh 6 (Ảnh em bé tắm).
  * *Đáp án:* Tranh 1, 2, 4, 6 $\rightarrow$ Hộp Đỏ (Bí mật tuyệt đối); Tranh 3, 5 $\rightarrow$ Hộp Xanh (Được chia sẻ).
* **Tiến trình Xoắn ốc:** Điểm khởi đầu: Hình thành phản xạ hành vi tự vệ cơ bản: Nhận diện bí mật $\rightarrow$ Khoanh tay nói Không $
ightarrow$ Báo người lớn.

---

#### LỚP 2 — SỞ HỮU SỐ, NGUYÊN TẮC XIN PHÉP VÀ XỬ LÝ SỰ CỐ
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `2.A1.2`: *Phân biệt được tình huống nên và không nên sử dụng thiết bị thông minh (không cung cấp thông tin riêng khi chưa có người lớn cho phép).*
  * `2.A2.MR2`: *Nêu được rằng không được tự ý sử dụng thiết bị AI khi chưa có sự cho phép của người lớn.*
  * `2.B3.MR1`: *Phân biệt được thứ của mình với thứ của người khác trong tình huống số (tài khoản học tập, ảnh chụp, bài vẽ).*
  * `2.B3.MR2`: *Thực hành được việc xin phép người khác trước khi chụp ảnh hoặc sử dụng hình ảnh của họ để làm dữ liệu.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 8 (M1)`, `KN 9 (M1)`, `KN 12 (M1)`, `KN 13 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Quyền sở hữu trên không gian số:* Tài khoản học toán, ảnh chụp cá nhân, bài vẽ trên máy là của riêng em; tài khoản và tranh vẽ của bạn là thuộc về bạn. Em không được tự ý vào tài khoản của bạn xem trộm hay xóa bài.
  * *Đơn vị 2: Nguyên tắc xin phép đồng thuận (Informed Consent):* Muốn chụp ảnh bức tranh của bạn để nạp cho máy nhận diện $\rightarrow$ Bắt buộc phải hỏi: *"Bạn có đồng ý cho mình chụp không?"*. Nếu bạn lắc đầu $\rightarrow$ Vui vẻ dừng lại, không ép buộc.
  * *Đơn vị 3: Quy trình 2 bước xử lý sự cố an toàn:* Khi màn hình máy tính bảng hiện video bạo lực, trang web lạ hoặc đòi nhập mã PIN: Bước 1: Ấn nút tắt màn hình/gập máy tính lại $\rightarrow$ Bước 2: Chạy đến báo ngay cho bố mẹ hoặc cô giáo.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Thực hành đóng vai theo cặp: Bạn A cầm tranh vẽ, bạn B thực hiện lời xin phép: *"Chào Lan, mình có thể chụp ảnh bức tranh bông hoa của bạn để cho robot nhận diện được không?"*. Bạn A gật đầu $\rightarrow$ Bạn B mới giơ máy chụp.
  * *Hành vi 2:* Diễn tập xử lý sự cố: Khi giáo viên giơ tấm bìa mô phỏng màn hình hiện quảng cáo trò chơi trúng thưởng đòi mật khẩu, học sinh ấn ngay tay vào nút Home/Tắt nguồn mô phỏng và đứng dậy giơ tay báo giáo viên.
  * *Tiêu chí hoàn thành:* Nói đúng câu xin phép đồng thuận; thực hiện đúng thao tác tắt máy và báo người lớn, không tò mò bấm lung tung.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Thẻ kịch bản đóng vai đồng thuận; Mô hình máy tính bảng có dán màn hình sự cố số.*
  * *Đáp án:* Hành vi đạt: Phải có sự đồng thuận mới được chụp ảnh; khi có dấu hiệu lạ, lập tức dừng lại nhờ người lớn xử lý.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 1: Nâng lên ý thức về "Tài sản số", "Sự đồng thuận của người khác" và "Quy trình xử lý sự cố 2 bước".

---

#### LỚP 3 — NHẬN DIỆN BẪY THU THẬP DỮ LIỆU VÀ PHÂN LOẠI DỮ LIỆU NHẠY CẢM
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `3.A1.4`: *Nêu được một số loại dữ liệu cá nhân không nên chia sẻ cho các ứng dụng AI.*
  * `3.A1.MR3`: *Giải thích được rằng việc suy nghĩ và kiểm tra trước khi cung cấp dữ liệu cho AI giúp tự bảo vệ bản thân và trở thành người dùng có trách nhiệm.*
  * `3.B2.1`: *Nhận biết được hiện tượng thông tin hoặc hình ảnh do AI tạo ra có thể sai lệch, giả mạo hoặc gây hiểu lầm.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 8 (M2)`, `KN 9 (M2)`, `KN 10 (M1)`, `KN 12 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Nhận diện bẫy thu thập dữ liệu ngầm (Dark Patterns):* Nhiều ứng dụng trò chơi giải đố AI, chỉnh sửa khuôn mặt hoạt hình miễn phí được thiết kế để dụ dỗ người dùng khai báo: Ngày tháng năm sinh, tên trường học, địa chỉ nhà, quét toàn bộ danh bạ điện thoại.
  * *Đơn vị 2: Phân loại dữ liệu theo 3 mức độ bảo mật:*
    * Mức 1 (An toàn): Biệt danh học tập, màu sắc yêu thích, môn học yêu thích.
    * Mức 2 (Thận trọng): Hình ảnh sinh hoạt chung của lớp học (phải xin phép cô giáo).
    * Mức 3 (Nhạy cảm - Cấm tuyệt đối): Mật khẩu, số CCCD bố mẹ, định vị GPS nhà ở, ảnh chụp giấy tờ gia đình.
  * *Đơn vị 3: Xóa lịch sử hội thoại cơ bản:* Nhận biết khung trò chuyện của Chatbot có tính năng lưu lịch sử (History); học sinh cần biết cách bấm nút Xóa lịch sử (Clear Chat) sau khi sử dụng máy tính công cộng ở trường.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Trên Phiếu khảo sát đăng ký "Câu lạc bộ Toán AI vui nhộn" có 6 trường thông tin, học sinh dùng bút dạ quang gạch bỏ 3 trường thông tin nhạy cảm vô lý (Số điện thoại bố mẹ, Địa chỉ nhà ở, Số CCCD).
  * *Hành vi 2:* Thao tác trên giao diện chatbot học tập phòng máy: Nhấp chuột vào biểu tượng thùng rác để xóa phiên trò chuyện vừa kết thúc.
  * *Tiêu chí hoàn thành:* Gạch bỏ chính xác 100% dữ liệu nhạy cảm; thực hiện được thao tác xóa lịch sử hội thoại trên máy.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Phiếu khảo sát mẫu in sẵn A4; Giao diện phần mềm chatbot học đường an toàn.*
  * *Đáp án:* 3 mục bị gạch bỏ: Số điện thoại, Địa chỉ, Số CCCD. Giải thích: Phần mềm giải toán chỉ cần đề bài, không cần biết nhà ở hay số điện thoại của gia đình.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 2: Biết "Đọc và Soát lỗi dữ liệu" trên giao diện đăng ký; bắt đầu hình thành thói quen dọn dẹp dấu chân số (xóa lịch sử).

---

#### LỚP 4 — QUẢN TRỊ QUYỀN RIÊNG TƯ VÀ PHÒNG NGỪA HẬU QUẢ LỘ THÔNG TIN
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `4.B2.1`: *Nêu được các loại thông tin cá nhân cần giữ bí mật khi sử dụng công nghệ số và AI (mật khẩu, định vị, số định danh, hình ảnh riêng tư).*
  * `4.B2.2`: *Phân tích được hậu quả của việc để lộ thông tin cá nhân trên môi trường mạng và đề xuất các biện pháp phòng ngừa.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 8 (M2)`, `KN 9 (M3)`, `KN 10 (M2)`, `KN 12 (M3)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Cơ chế Cấp quyền ứng dụng (App Permissions):* Khi cài đặt ứng dụng AI (như phần mềm tạo ảnh hoạt hình), máy sẽ hỏi: "Cho phép truy cập Máy ảnh?", "Cho phép truy cập Vị trí?", "Cho phép truy cập Danh bạ?". Người dùng thông thái chỉ cấp quyền thực sự cần thiết, dứt khoát từ chối các quyền vô lý (ví dụ: phần mềm vẽ tranh đòi quyền biết vị trí định vị nhà ở).
  * *Đơn vị 2: Phân tích chuỗi hậu quả của rò rỉ dữ liệu:* Lộ số điện thoại $\rightarrow$ Nhận cuộc gọi lừa đảo dọa nạt; Lộ định vị $\rightarrow$ Kẻ xấu theo dõi giờ đi học về; Lộ ảnh khuôn mặt rõ nét $\rightarrow$ Kẻ xấu dùng AI cắt ghép ảnh deepfake bôi nhọ danh dự.
  * *Đơn vị 3: Quy tắc Mật khẩu mạnh và Xác thực an toàn:* Mật khẩu mạnh phải có ít nhất 8 ký tự, kết hợp chữ hoa, chữ thường, chữ số và ký tự đặc biệt (ví dụ: `SaoBien@2026`); tuyệt đối không đặt ngày sinh hay số điện thoại làm mật khẩu.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Thao tác trên bảng điều khiển giả lập quyền riêng tư: Tắt nút chuyển (Toggle off) của quyền Vị trí và Danh bạ đối với ứng dụng vẽ tranh; chỉ giữ lại quyền Tệp ảnh.
  * *Hành vi 2:* Thiết lập và ghi vào phiếu cá nhân 01 mật khẩu an toàn theo công thức 4 thành phần bảo mật.
  * *Tiêu chí hoàn thành:* Cấu hình đúng bảng quyền riêng tư; mật khẩu tạo ra đạt mức "Mạnh" theo tiêu chuẩn an toàn thông tin.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bảng điều khiển Permissions Manager giả lập trên máy tính; Thước đo kiểm tra độ mạnh của mật khẩu.*
  * *Đáp án:* Ứng dụng vẽ tranh: Bật [Bộ nhớ ảnh] - Tắt [Vị trí] - Tắt [Danh bạ] - Tắt [Micro]. Mật khẩu đạt chuẩn: Đủ 4 yếu tố hoa/thường/số/ký tự.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 3: Nâng lên cấp độ "Quản trị quyền riêng tư hệ thống" và hiểu rõ mối đe dọa Deepfake mạo danh khuôn mặt.

---

#### LỚP 5 — KỸ THUẬT KHỬ NHẬN DẠNG DỮ LIỆU CÁ NHÂN TRONG DỰ ÁN AI
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `5.A1.2`: *Nêu được ví dụ cụ thể về trách nhiệm của người tạo và người sử dụng AI đối với việc bảo vệ thông tin và dữ liệu cá nhân.*
  * `5.B2.MR1`: *Đề xuất được một số quy tắc khi thu thập dữ liệu để bảo đảm an toàn dữ liệu cá nhân và không xâm phạm quyền riêng tư của người khác.*
  * `5.D1.1` (Tích hợp): *Thực hành quy trình chuẩn bị dữ liệu sạch và an toàn cho mô hình học máy.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 8 (M3)`, `KN 9 (M3)`, `KN 10 (M3)`, `KN 12 (M3)`, `KN 31 (M3)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Bản chất kỹ thuật của Khử nhận dạng dữ liệu cá nhân (Data Anonymization):* Là quá trình xử lý kỹ thuật để dữ liệu không còn liên kết trực tiếp hoặc gián tiếp tới danh tính của một cá nhân cụ thể, nhằm ngăn chặn việc nhận diện lại (Re-identification).
  * *Đơn vị 2: Phổ kỹ thuật bảo vệ riêng tư khi làm dữ liệu AI:*
    1. *Kỹ thuật 1 - Chụp riêng biệt:* Chỉ chụp vật thể cần học (biển báo, đồ dùng), hướng ống kính tránh xa người.
    2. *Kỹ thuật 2 - Cắt ảnh (Crop):* Dùng công cụ cắt sát viền đối tượng, loại bỏ toàn bộ khuôn mặt và người đứng phía sau.
    3. *Kỹ thuật 3 - Che mờ/Xóa bỏ:* Dùng công cụ che mờ (Blur) hoặc vẽ dải màu che kín khuôn mặt, xóa trắng bảng tên học sinh và biển số xe.
    4. *Kỹ thuật 4 - Loại bỏ tệp ảnh:* Nếu ảnh bị dính quá nhiều người hoặc thông tin nhạy cảm không thể che hết $\rightarrow$ Xóa bỏ dứt khoát khỏi tập dữ liệu.
  * *Đơn vị 3: Trách nhiệm pháp lý và đạo đức của nhà phát triển AI:* Kỹ sư AI không được phép đưa dữ liệu chưa ẩn danh của người khác lên các nền tảng học máy công cộng trên Internet.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Mở thư mục ảnh dự án thô (chứa 10 ảnh chụp biển báo sân trường có dính người cầm); thực hiện thao tác Crop hoặc che mờ mặt và thẻ tên trên toàn bộ các bức ảnh dính người.
  * *Hành vi 2:* Đổi máy kiểm toán chéo (Cross-audit): Rà soát từng ảnh của nhóm bạn xem có sót góc mặt, thẻ tên hay biển số xe nào không; ký biên bản xác nhận dữ liệu đã khử nhận dạng an toàn.
  * *Tiêu chí hoàn thành:* 100% ảnh lưu trong thư mục sạch không còn dấu hiệu nhận diện cá nhân; ký hiệu biển báo vẫn nhìn rõ nét.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Thư mục `Du_Lieu_Tho_Bi_Dinh_Nguoi` gồm 10 tệp ảnh `.jpg`; Phần mềm xử lý ảnh Paint/Photos; Biên bản kiểm toán an toàn dữ liệu A5.*
  * *Đáp án:* 10/10 ảnh đã được cắt bỏ người hoặc che kín mặt/tên. Ký hiệu tam giác vàng trên biển báo vẫn nguyên vẹn 100%.
* **Tiến trình Xoắn ốc:** Đỉnh cao cấp học: Chuyển từ "người dùng tự phòng vệ" sang "nhà phát triển có trách nhiệm đạo đức và kỹ năng kỹ thuật khử nhận dạng dữ liệu cộng đồng".

---

## TRỤC 3: ĐẠO ĐỨC AI, VĂN HÓA SỐ VÀ TRÁCH NHIỆM GIẢI TRÌNH (DO NO HARM & ACCOUNTABILITY)

### 1. Bản chất Khoa học & Định hướng Tiến trình Xoắn ốc
* **Bản chất khoa học công nghệ:** Trí tuệ nhân tạo không mang tính trung lập về mặt đạo đức. Mô hình AI phản ánh các giá trị, định kiến và mục đích của những người thu thập dữ liệu và lập trình ra nó. Đạo đức AI bao gồm các nguyên tắc cốt lõi: Không gây hại (Do no harm), Tôn trọng quyền con người, Tính công bằng và không phân biệt đối xử (Fairness & Non-discrimination), Tính minh bạch (Transparency - giải mã chiếc hộp đen), và Trách nhiệm giải trình (Accountability - con người luôn chịu trách nhiệm pháp lý và đạo đức về hành vi và sản phẩm của hệ thống AI).
* **Tiến trình xoắn ốc (Grades 1 to 5):**
  * *Lớp 1:* Đạo đức hành vi trực quan: Tuyệt đối không dùng máy móc thông minh để làm đau, làm sợ hoặc làm phiền người khác; tôn trọng cảm xúc bạn bè xung quanh.
  * *Lớp 2:* Tôn trọng bản quyền tác phẩm và nhận diện thiên lệch trực quan: Phân biệt rõ tác phẩm do mình tự vẽ vs bài của bạn; hiểu rằng nếu máy chỉ học 1 loại dữ liệu thì máy sẽ thiên vị và nhận diện sai cho nhóm khác.
  * *Lớp 3:* Văn hóa ngôn từ và Dữ liệu công bằng: Giao tiếp văn minh với AI, liêm chính học thuật cơ bản; cung cấp dữ liệu đại diện công bằng (cả nam và nữ, các vùng miền) để máy không phân biệt đối xử.
  * *Lớp 4:* Tác quyền trong kỷ nguyên AI và Trách nhiệm không đổ lỗi: Ghi nguồn minh bạch khi dùng AI hỗ trợ sáng tạo (AutoDraw); hiểu rằng con người chọn công cụ thì con người chịu trách nhiệm, không thể đổ lỗi cho cỗ máy.
  * *Lớp 5:* Quản trị AI chuyên sâu: Phân tích cơ chế hộp đen (Black-box) vs hộp kính minh bạch; thực hiện kiểm toán thiên lệch (Bias Audit); thiết lập Phiếu thông tin mô hình (**Model Card**) để giải trình trách nhiệm trước cộng đồng.

---

### 2. Chi tiết Tiến trình 5 Khối Lớp của Trục 3

#### LỚP 1 — NGUYÊN TẮC KHÔNG GÂY HẠI VÀ LÀM VIỆC TỐT CÙNG THIẾT BỊ
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `1.B1.1`: *Nêu được một vài việc không nên làm khi dùng thiết bị thông minh (như bật tiếng quá to làm phiền mọi người, dùng máy trêu chọc bạn).*
  * `1.B3.1`: *Biết và nhắc lại được quy tắc: Không được dùng máy móc thông minh để làm hại hoặc làm đau người khác.*
  * `1.B3.2`: *Nêu được việc làm tốt đẹp mà con người sử dụng máy thông minh để thực hiện (như gọi giúp đỡ khi khẩn cấp, học nghe phát âm tiếng Anh).*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 7 (M1)`, `KN 15 (M1)`, `KN 16 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Quy tắc nền tảng "Không gây hại" (Do No Harm):* Thiết bị thông minh được tạo ra để giúp ích; tuyệt đối không dùng máy để biến thành công cụ trêu chọc, dọa nạt làm bạn khóc hay đau đớn.
  * *Đơn vị 2: Những việc làm sai trái cụ thể cần tránh:*
    * Không vặn loa điện thoại/máy tính bảng hết cỡ sát tai bạn làm bạn giật mình, tổn thương thính giác.
    * Không dùng tính năng ghi âm để thu trộm tiếng bạn nói ngọng, nói nhịu rồi bật lại trước lớp để cười cợt.
    * Không dùng camera chụp lén bạn bị ngã, bạn đang khóc hoặc lúc bạn sơ ý để mang đi trêu chọc.
    * Không ra lệnh cho loa phát tiếng dọa ma, tiếng la hét làm em bé hoặc người già sợ hãi.
  * *Đơn vị 3: Sử dụng máy làm việc tốt đẹp:* Dùng máy nghe bài hát vui tươi; dùng máy học phát âm tiếng Anh chuẩn; bấm nút gọi khẩn cấp cho bố mẹ khi gặp nguy hiểm.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Quan sát 4 tranh tình huống, chỉ đúng và phân loại 2 hành vi sai (làm phiền/trêu chọc) vs 2 hành vi tốt (học tập/giúp đỡ).
  * *Hành vi 2:* Tình huống phản xạ: Khi bạn rủ lấy điện thoại ghi âm tiếng bạn khác để trêu, học sinh đứng nghiêm, nói to: *"Không được đâu, làm thế bạn sẽ buồn đấy!"*.
  * *Tiêu chí hoàn thành:* Nhận diện chính xác 100% hành vi gây hại; thể hiện thái độ phản đối rõ ràng khi bạn rủ làm việc xấu.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bộ tranh tình huống A4:* Tranh 1 (Bạn bật còi xe đồ chơi inh ỏi cạnh bạn đang đọc sách), Tranh 2 (Bạn dùng máy tính bảng học đếm số vui vẻ), Tranh 3 (Bạn chụp ảnh dìm hàng trêu bạn khóc), Tranh 4 (Bạn cùng ông xem dự báo thời tiết).
  * *Đáp án:* Tranh 1 & 3: Hành vi xấu, gây hại; Tranh 2 & 4: Hành vi tốt, có ích.
* **Tiến trình Xoắn ốc:** Điểm khởi đầu: Đạo đức hành vi cụ thể — Tôn trọng cảm xúc, không làm phiền và không gây tổn thương cho người khác.

---

#### LỚP 2 — TÔN TRỌNG TÁC QUYỀN VÀ BƯỚC ĐẦU NHẬN BIẾT THIÊN LỆCH
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `2.B1.1`: *Nhận biết được rằng AI đôi khi có thể đưa ra kết quả không hoàn toàn công bằng hoặc chỉ ưu tiên một nhóm quen thuộc (thiên lệch).*
  * `2.B1.MR1`: *Nêu được ví dụ về tình huống thiên lệch của AI trong đời sống (như máy nhận diện giọng người lớn tốt hơn giọng trẻ em).*
  * `2.B1.MR2`: *Giải thích được rằng nếu dữ liệu đưa vào máy chưa đa dạng hoặc chưa công bằng thì AI sẽ đưa ra kết quả thiên lệch.*
  * `2.B3.1`: *Nêu được ví dụ về quyền sở hữu đối với sản phẩm do con người tạo ra (như bức tranh em vẽ, bài thơ em làm).*
  * `2.B3.2`: *Thể hiện thái độ trung thực: Phân biệt rõ sản phẩm do chính mình tự làm với sản phẩm có sự hỗ trợ của thiết bị thông minh.*
  * `2.B3.MR2`: *Thực hành xin phép và nhận được sự đồng thuận trước khi sử dụng sản phẩm hoặc hình ảnh của bạn.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 13 (M1)`, `KN 14 (M1)`, `KN 15 (M1)`, `KN 24 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Quyền sở hữu sản phẩm trí tuệ:* Bức tranh vẽ, mô hình đất nặn là công sức sáng tạo của riêng bạn. Nếu em muốn lấy tranh của bạn cho robot quét mẫu $\rightarrow$ Bắt buộc phải hỏi: *"Bạn có cho phép mình mượn tranh không?"* và được bạn đồng ý.
  * *Đơn vị 2: Khái niệm Thiên lệch ban đầu (Bias):* Thiên lệch là sự thiên vị, không công bằng của máy tính. Nếu một chiếc loa thông minh chỉ được dạy bằng giọng của người lớn ở thành phố $\rightarrow$ Khi trẻ em hoặc người nói giọng địa phương ra lệnh, máy sẽ nghe nhầm hoặc không hiểu. Máy thiên lệch không phải vì máy ghét trẻ em, mà vì **con người nạp dữ liệu chưa đủ đa dạng**.
  * *Đơn vị 3: Lòng trung thực học đường:* Bức tranh nào em tự vẽ bằng tay thì nói là tự vẽ; bức tranh nào có bố mẹ hay ứng dụng gợi ý nét vẽ thì phải trung thực nói rõ, không nhận vơ công sức của máy hay của người khác về mình.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Dán nhãn tác giả nhí lên bài vẽ: Học sinh ký tên mình và dán nhãn màu xanh *"Em tự vẽ 100%"* hoặc nhãn màu vàng *"Có sự trợ giúp của máy"*.
  * *Hành vi 2:* Thí nghiệm nhận diện thiên lệch: Lắng nghe 2 đoạn ghi âm (Giọng bố nói chuẩn vs Giọng bé 4 tuổi nói lí nhí); giải thích vì sao loa thông minh chỉ thực hiện lệnh của bố mà không nghe lời bé.
  * *Tiêu chí hoàn thành:* Trung thực 100% khi phân định nguồn gốc sản phẩm; giải thích đúng nguyên nhân thiên lệch do thiếu dữ liệu giọng trẻ em.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *File âm thanh đối chứng giọng người lớn vs trẻ nhỏ; Bộ nhãn dán tác quyền nhí; Tranh minh họa quả táo xanh bị máy bỏ qua vì chỉ học táo đỏ.*
  * *Đáp án:* Loa không nhận ra vì trong bộ dữ liệu của loa thiếu giọng nói trẻ em. Giải pháp: Con người phải nạp thêm giọng của trẻ em vào để loa học.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 1: Chạm vào khái niệm "Sở hữu trí tuệ", "Lòng trung thực nguồn gốc" và hiện tượng "Thiên lệch dữ liệu (Bias)".

---

#### LỚP 3 — VĂN HÓA GIAO TIẾP VỚI AI VÀ DỮ LIỆU CÔNG BẰNG HỌC ĐƯỜNG
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `3.B3.1`: *Nhận biết được rằng không được tạo ra hoặc sử dụng các công cụ AI cho các hành vi sai trái, xúc phạm hoặc gây hại cho người khác.*
  * `3.B3.MR1`: *Nêu được rằng con người cần cung cấp dữ liệu đúng đắn và đa dạng để AI không thiên vị, không phân biệt đối xử giữa các nhóm người.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 7 (M2)`, `KN 15 (M2)`, `KN 16 (M2)`, `KN 24 (M1)`, `KN 32 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Văn hóa giao tiếp số (Digital Civility):* Dù Chatbot là cỗ máy vô tri, con người văn minh luôn sử dụng ngôn từ lịch sự, nhã nhặn khi ra lệnh; tuyệt đối không dùng từ ngữ thô tục, chửi bới hoặc bắt máy viết những lời độc ác về bạn học.
  * *Đơn vị 2: Liêm chính học thuật cơ bản:* AI có thể viết một đoạn văn ngắn trong 2 giây, nhưng nếu học sinh copy nguyên văn đoạn đó nộp cho cô giáo và nhận là mình tự viết $\rightarrow$ Đó là hành vi gian lận, không trung thực, vi phạm đạo đức học sinh.
  * *Đơn vị 3: Dữ liệu công bằng trong lớp học:* Khi xây dựng tập ảnh dữ liệu để dạy máy nhận diện "Học sinh tiểu học chăm ngoan", nếu ta chỉ chụp ảnh các bạn nam đeo kính $\rightarrow$ Cỗ máy tạo ra sẽ cho rằng các bạn nữ hoặc các bạn không đeo kính không phải là học sinh chăm ngoan. Đó là sự bất công do dữ liệu thiên vị!
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Đọc 3 câu lệnh nạp cho chatbot, phát hiện câu lệnh có từ ngữ thô tục, bất lịch sự và sửa lại thành câu lệnh chuẩn mực, có văn hóa.
  * *Hành vi 2:* Đánh giá một tập 10 bức ảnh đại diện học sinh mẫu: Phát hiện tập ảnh đang bị lệch (8 ảnh bạn nam, chỉ có 2 ảnh bạn nữ); đề xuất bổ sung thêm 6 ảnh bạn nữ để bảo đảm công bằng giới tính.
  * *Tiêu chí hoàn thành:* Sửa câu lệnh đúng văn phong giao tiếp lịch thiệp; chỉ ra chính xác sự mất cân bằng trong tập dữ liệu mẫu.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Phiếu bài tập "Ngôn từ văn minh khi dùng AI"; Tập 10 thẻ ảnh học sinh mẫu có sẵn sự mất cân bằng.*
  * *Đáp án:* Câu lệnh chuẩn: "Xin chào bạn AI, vui lòng gợi ý giúp mình 3 câu đố về hoa quả". Tập ảnh cần thêm ảnh bạn nữ để tỷ lệ nam/nữ cân bằng 50/50.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 2: Rèn luyện đạo đức ngôn từ (Civility), liêm chính học thuật và ý thức chủ động kiểm soát tính công bằng của dữ liệu.

---

#### LỚP 4 — MINH BẠCH TÁC QUYỀN VÀ TRÁCH NHIỆM KHÔNG ĐỔ LỖI CHO CỖ MÁY
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `4.A1.2`: *Trình bày được rằng con người luôn giữ vai trò quyết định và chịu trách nhiệm về sản phẩm do công nghệ tạo ra.*
  * `4.C2.1` (Tác quyền): *Thực hành sáng tạo sản phẩm số có sự hỗ trợ của AI và thực hiện việc ghi nhận nguồn gốc tác quyền minh bạch.*
  * `4.D2.1` (Giám sát): *Nêu được rằng con người phải liên tục giám sát và nâng cấp hệ thống để tránh các sai sót gây hại cho cộng đồng.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 14 (M3)`, `KN 15 (M2)`, `KN 45 (M2)`, `KN 46 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Quy tắc Ghi nguồn minh bạch (Attribution & Citation):* Khi học sinh sử dụng phần mềm AI tạo tranh (AutoDraw) hoặc công cụ gợi ý ý tưởng làm bài thuyết trình, bắt buộc phải có dòng chú thích minh bạch ở góc sản phẩm: *"Sản phẩm được sáng tạo bởi Nhóm 1, có sự hỗ trợ của công cụ AutoDraw"*. Đây là chuẩn mực tôn trọng trí tuệ và trung thực khoa học.
  * *Đơn vị 2: Nguyên tắc Không đổ lỗi cho công nghệ:* Khi một sản phẩm do AI gợi ý có chứa thông tin sai lệch hoặc hình ảnh phản cảm, học sinh không được biện minh: *"Tại cái máy tính nó vẽ thế, con không biết!"*. Con người là người lựa chọn, bấm nút và nộp bài, nên con người phải chịu 100% trách nhiệm về nội dung sản phẩm đó.
  * *Đơn vị 3: Trách nhiệm giám sát liên tục:* Hệ thống AI sau khi triển khai có thể bị suy giảm độ chính xác theo thời gian; con người phải theo dõi, ghi nhận lỗi và cải tiến dữ liệu.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Xuất bức tranh cổ động môi trường vẽ trên AutoDraw; thực hiện thao tác chèn khung văn bản ở góc dưới bên phải ghi đúng mẫu câu tác quyền quy định.
  * *Hành vi 2:* Đọc tình huống phân xử tranh chấp: Bạn Nam dùng AI dịch bài văn tiếng Anh bị sai nghĩa làm nhóm bị điểm kém, Nam đổ lỗi tại Google Dịch; học sinh viết đoạn phân tích 3 dòng chỉ ra vì sao Nam phải chịu trách nhiệm chứ không thể đổ lỗi cho công cụ dịch.
  * *Tiêu chí hoàn thành:* Tranh xuất ra có đầy đủ dòng ghi nguồn tác quyền chuẩn mực; bài phân tích nêu rõ trách nhiệm thuộc về người sử dụng.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Khung nhãn ghi nguồn tác quyền in sẵn; Phiếu nghiên cứu tình huống "Lời bào chữa của Nam".*
  * *Đáp án:* Nam là người chọn dùng bản dịch mà không kiểm tra lại với từ điển, Nam là người nộp bài nên Nam phải chịu trách nhiệm trước nhóm.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 3: Xác lập chuẩn mực liêm chính học thuật cấp độ cao: Ghi nhận tác quyền minh bạch và triệt tiêu tư duy đổ lỗi cho công nghệ.

---

#### LỚP 5 — TÍNH MINH BẠCH, KIỂM TOÁN THIÊN LỆCH VÀ TRÁCH NHIỆM GIẢI TRÌNH
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `5.A1.1`: *Trình bày được rằng con người luôn giữ vai trò chủ đạo và chịu trách nhiệm cao nhất về kết quả của hệ thống AI.*
  * `5.A1.2`: *Nêu được ví dụ cụ thể về trách nhiệm giải trình của người tạo và người sử dụng AI (Accountability).*
  * `5.A1.MR1`: *Trình bày được rằng con người chịu trách nhiệm cuối cùng về mọi quyết định và hậu quả khi sử dụng AI.*
  * `5.B1.1`: *Nêu được một số ví dụ về sự công bằng hoặc không công bằng trong kết quả do AI tạo ra (nhận diện sai nét mặt người già, thiên vị vùng miền).*
  * `5.B1.2`: *Giải thích được rằng AI cần phải phục vụ con người một cách công bằng, không phân biệt đối xử và không tạo ra bất bình đẳng xã hội.*
  * `5.B2.1`: *Nêu được các giải pháp giúp AI hoạt động công bằng hơn (thu thập dữ liệu cân bằng các nhóm, đa dạng nguồn dữ liệu).*
  * `5.B3.1`: *Giải thích được vì sao con người cần hiểu cách AI đưa ra quyết định (tính minh bạch và trách nhiệm giải trình).*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 15 (M3)`, `KN 24 (M3)`, `KN 26 (M2)`, `KN 32 (M3)`, `KN 45 (M3)`, `KN 46 (M3)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Khái niệm Hộp đen (Black-box) vs Tính minh bạch (Transparency):* Nhiều mô hình AI hiện đại như một "chiếc hộp đen" – người dùng chỉ thấy đầu vào và đầu ra mà không hiểu vì sao máy đưa ra quyết định đó. Tính minh bạch đòi hỏi hệ thống AI phải có khả năng giải thích được lý do đưa ra kết luận (Explainable AI), giúp con người tin tưởng và kiểm soát được máy.
  * *Đơn vị 2: Kiểm toán thiên lệch dữ liệu (Bias Audit):* Phân tích các ca nghiên cứu thực tế: Hệ thống tuyển dụng AI tự động lọc bỏ hồ sơ của phụ nữ do dữ liệu quá khứ chỉ toàn nam giới; phần mềm nhận diện khuôn mặt có tỷ lệ nhận nhầm người da màu cao gấp 5 lần người da trắng. Giải pháp: Phải kiểm toán tập dữ liệu, cân bằng số lượng mẫu của mọi nhóm đối tượng trước khi huấn luyện.
  * *Đơn vị 3: Trách nhiệm giải trình (Accountability) và Model Card:*
    * Khái niệm chuẩn hóa: Trách nhiệm giải trình là nghĩa vụ của người thiết kế và người sử dụng AI trong việc giải thích, minh chứng và chịu trách nhiệm về hoạt động và tác động của hệ thống.
    * Công cụ thực hiện: Thiết lập Phiếu thông tin mô hình (**Model Card**) công khai 4 yếu tố: Mục đích hệ thống, Nguồn gốc dữ liệu, Tỷ lệ chính xác qua kiểm thử, và Các giới hạn cảnh báo khi sử dụng.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Kiểm toán một tập dữ liệu âm thanh nhận dạng giọng nói: Chỉ ra điểm thiên lệch vùng miền (tập dữ liệu có 30 mẫu giọng miền Bắc, chỉ có 2 mẫu giọng miền Trung và 2 mẫu giọng miền Nam); đề xuất giải pháp kỹ thuật bổ sung dữ liệu cân bằng.
  * *Hành vi 2:* Hoàn thiện Phiếu thông tin mô hình (Model Card) cho dự án AI nhận diện biển báo an toàn học đường của nhóm; đại diện nhóm đứng lên thuyết trình giải trình trách nhiệm trước lớp.
  * *Tiêu chí hoàn thành:* Phát hiện chính xác lỗi thiên lệch dữ liệu; bản Model Card điền đầy đủ 4 trường thông tin trung thực, không giấu giếm các trường hợp máy còn nhận diện sai.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Biểu mẫu Model Card chuẩn Experience AI tinh giản khổ A4; Bảng số liệu tập dữ liệu âm thanh 3 miền; Kịch bản thuyết trình giải trình.*
  * *Đáp án:* Bản Model Card hợp lệ phải nêu rõ: Tỷ lệ chính xác đạt 85%, máy còn bị nhầm lẫn khi ánh sáng quá yếu hoặc góc nghiêng > 45 độ; Nhóm học sinh Lớp 5A chịu trách nhiệm về mô hình này.
* **Tiến trình Xoắn ốc:** Đỉnh cao cấp Tiểu học: Tiếp cận đầy đủ các trụ cột quản trị AI quốc tế: Tính minh bạch (Hộp kính), Kiểm toán thiên lệch (Bias Audit), và Trách nhiệm giải trình (Accountability qua Model Card).

---

## TRỤC 4: TỰ CHỦ TƯ DUY VÀ CHỐNG Ỷ LẠI NHẬN THỨC CÔNG NGHỆ (LEARNER AGENCY)

### 1. Bản chất Khoa học & Định hướng Tiến trình Xoắn ốc
* **Bản chất khoa học công nghệ:** Sự tiện lợi và tốc độ phản hồi tức thì của các hệ thống AI tạo sinh (Generative AI) dễ tạo ra hiện tượng **Ỷ lại nhận thức (Cognitive Offloading)** – nơi học sinh ngừng tư duy sâu, ngừng rèn luyện kỹ năng giải quyết vấn đề cơ bản và phó mặc toàn bộ quá trình suy nghĩ cho máy móc. Năng lực tự chủ của người học (Learner Agency) trong kỷ nguyên số đòi hỏi học sinh phải biết định vị AI là công cụ hỗ trợ tư duy chứ không phải là bộ não thay thế; biết kiểm soát thời gian màn hình, duy trì tư duy độc lập và có khả năng ra quyết định có điều kiện.
* **Tiến trình xoắn ốc (Grades 1 to 5):**
  * *Lớp 1:* Rèn thói quen tự làm bằng tay và niềm vui tự tạo sản phẩm; tuân thủ chuông hẹn giờ rời màn hình máy tính (100% Unplugged).
  * *Lớp 2:* Nhận diện tình huống không nên dùng AI; nhận thức rõ nếu bài gì cũng hỏi máy thì não bộ sẽ lười suy nghĩ và mất kỹ năng tự giải quyết vấn đề.
  * *Lớp 3:* Vận dụng Quy tắc 3 bước Tự chủ tư duy ("Nghĩ trước - Hỏi sau - Đối chiếu") và Bộ ba câu hỏi vàng trước khi quyết định mở ứng dụng AI.
  * *Lớp 4:* Năng lực ra quyết định có điều kiện theo bối cảnh học đường (Contextual Decision-making); kiên quyết từ chối chép bài văn/lời giải của máy.
  * *Lớp 5:* Quản trị bản thân và Thích ứng số toàn diện (Digital Resilience); tự xây dựng thời gian biểu cân bằng giữa hoạt động số và đời sống thể chất, tương tác xã hội.

---

### 2. Chi tiết Tiến trình 5 Khối Lớp của Trục 4

#### LỚP 1 — NIỀM VUI TỰ LÀM VÀ THỜI GIAN MÀN HÌNH HỢP LÝ
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `1.A1.2` (Tích hợp): *Nêu được rằng con người có khả năng tự suy nghĩ và tự sáng tạo ra các sản phẩm của mình.*
  * `1.B1.1` (Tích hợp): *Nhận biết được việc sử dụng thiết bị quá nhiều sẽ gây hại cho mắt và sức khỏe.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 42 (M1)`, `KN 44 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Bàn tay và khối óc của em là kỳ diệu nhất:* Tự tay vẽ một bông hoa, tự tay xếp hình ngôi nhà mang lại niềm tự hào lớn hơn nhiều so với việc chỉ bấm nút xem máy làm sẵn.
  * *Đơn vị 2: Giới hạn thời gian màn hình (Screen Time):* Đôi mắt và cơ thể của học sinh lớp 1 đang lớn; nếu ngồi dán mắt vào tivi hay máy tính bảng quá 15–20 phút sẽ bị mỏi mắt, gù lưng và đau đầu.
  * *Đơn vị 3: Quy tắc Đồng hồ reo:* Khi chuông báo hẹn giờ reo $\rightarrow$ Bé vui vẻ cất máy tính bảng, đứng dậy tập thể dục, uống nước hoặc ra sân chơi cùng bạn bè.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Tự tay dùng bút sáp vẽ và tô màu một bức tranh đồ chơi em yêu thích trên giấy A5; kiên trì vẽ xong mới xin phép xem máy tính bảng.
  * *Hành vi 2:* Diễn tập tình huống hẹn giờ: Khi chuông báo 15 phút vang lên, học sinh lập tức đặt máy tính bảng đồ chơi xuống bàn, đứng dậy vươn vai hai tay lên cao.
  * *Tiêu chí hoàn thành:* Hoàn thành tranh vẽ tự tay; tự giác rời thiết bị khi có tín hiệu chuông reo mà không phụng phịu, đòi hỏi.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Đồng hồ hẹn giờ chuông reo; Giấy vẽ A5 và hộp bút màu; Bảng sao khen thưởng "Bé tự giác".*
  * *Đáp án:* Hành vi đạt: Tự vẽ trước, rời máy ngay khi chuông reo.
* **Tiến trình Xoắn ốc:** Điểm khởi đầu: Nếp sinh hoạt số lành mạnh — Yêu thích lao động sáng tạo bằng tay và biết ngắt kết nối đúng giờ.

---

#### LỚP 2 — NHẬN BIẾT BẪY LƯỜI SUY NGHĨ VÀ TÌNH HUỐNG KHÔNG NÊN DÙNG AI
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `2.A1.2`: *Phân biệt được tình huống nên và không nên sử dụng thiết bị thông minh (khi làm bài tập rèn tư duy thì không dùng AI làm hộ).*
  * `2.A2.MR3`: *Nêu được rằng việc phụ thuộc quá nhiều vào AI sẽ làm giảm khả năng tự suy nghĩ và tự học của bản thân.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 42 (M1)`, `KN 43 (M1)`, `KN 44 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Bộ não giống như cơ bắp:* Muốn tay chân khỏe mạnh thì phải tập thể dục; muốn não bộ thông minh thì phải tự suy nghĩ, tự tính toán. Nếu bài toán nào cũng bấm máy hỏi đáp án ngay $\rightarrow$ "Cơ bắp não" sẽ bị teo đi, học sinh sẽ quên mất cách tư duy.
  * *Đơn vị 2: Bảng phân loại Nên vs Không nên dùng AI:*
    * *Nên dùng:* Tra từ điển cách đọc từ mới tiếng Anh; nhờ máy phát bài nhạc tập thể dục; tra cứu thời tiết ngày mai.
    * *Không nên dùng:* Nhờ máy làm tính cộng trừ đố; nhờ máy viết câu trả lời môn Tiếng Việt; dùng máy khi chưa xin phép bố mẹ; dùng máy quá 30 phút một ngày.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Phân loại 4 thẻ tình huống học tập trên bảng gài vào 2 cột: Cột "Nên dùng AI" vs Cột "Tự suy nghĩ - Không dùng AI".
  * *Hành vi 2:* Xử lý tình huống đóng vai: Bạn rủ bật trợ lý ảo giải hộ bài toán đố $7 + 6$, học sinh lắc đầu nói: *"Bài này dễ mà, chúng mình cùng nhẩm tính xem ai ra kết quả trước nhé!"*.
  * *Tiêu chí hoàn thành:* Phân loại đúng 4/4 tình huống; thể hiện tinh thần hào hứng tự giải bài tập bằng trí não của mình.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Tranh biếm họa vui: "Bạn nhỏ quên cách làm tính vì nhờ robot làm hộ"; Bộ 4 thẻ tình huống học tập A5.*
  * *Đáp án:* Bài tính nhẩm, bài tập viết $\rightarrow$ Tuyệt đối không dùng AI. Tra cứu cách phát âm tiếng Anh $\rightarrow$ Được phép dùng hỗ trợ.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 1: Nhận thức sâu sắc về tác hại của việc "ỷ lại công nghệ" và chủ động từ chối dùng AI trong các bài tập rèn luyện tư duy nền tảng.

---

#### LỚP 3 — QUY TẮC 3 BƯỚC TỰ CHỦ TƯ DUY VÀ BỘ BA CÂU HỎI VÀNG
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `3.A1.3`: *Nêu được sự khác biệt giữa việc sử dụng AI như một công cụ hỗ trợ học tập với việc ỷ lại, phụ thuộc hoàn toàn vào AI.*
  * `3.A1.4`: *Trình bày được hậu quả của việc lạm dụng AI trong học tập (lười suy nghĩ, giảm khả năng sáng tạo, mất tự tin).*
  * `3.A1.5`: *Vận dụng được bộ ba câu hỏi trước khi quyết định sử dụng AI trong một nhiệm vụ học tập.*
  * `3.A1.MR2`: *Đóng vai xử lý tình huống từ chối việc chép nguyên văn câu trả lời của AI và thể hiện tinh thần tự chủ.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 42 (M2)`, `KN 43 (M2)`, `KN 44 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Quy tắc 3 bước Tự chủ tư duy (Three-step Agency Rule):*
    1. *Bước 1 - Tự làm trước:* Luôn đọc kỹ đề bài, tự nháp và viết ra câu trả lời của bản thân trước.
    2. *Bước 2 - Tham khảo AI sau:* Chỉ mở công cụ AI khi đã hoàn thành bài nháp hoặc khi thực sự bế tắc cần gợi ý hướng đi mới.
    3. *Bước 3 - Đối chiếu và chọn lọc:* So sánh bài làm của mình với câu trả lời của AI; tự mình chỉnh sửa câu chữ chứ không bao giờ chép nguyên văn của máy.
  * *Đơn vị 2: "Bộ ba câu hỏi vàng" định hướng hành vi:*
    ```text
    ┌────────────────────────────────────────────────────────┐
    │                 BỘ BA CÂU HỎI VÀNG                     │
    ├────────────────────────────────────────────────────────┤
    │ 1. Em đã tự suy nghĩ và cố gắng hết sức mình chưa?      │
    │ 2. Việc hỏi AI câu này có an toàn cho dữ liệu của em?   │
    │ 3. Thầy cô giáo có cho phép sử dụng AI trong bài này? │
    └────────────────────────────────────────────────────────┘
    ```
    *(Chỉ khi câu trả lời cho cả 3 câu đều là CÓ thì mới được phép mở công cụ AI).*
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Làm việc trên Phiếu bài tập 2 cột: Cột 1 "Em tự giải nháp trước" (Học sinh ghi phép tính tự tính), sau đó mới lật mảnh giấy che Cột 2 xem AI gợi ý; tự gạch chân so sánh điểm giống và khác nhau.
  * *Hành vi 2:* Tự chấm điểm 3 câu hỏi vàng trên thẻ bỏ túi trước khi mở máy tính phòng máy.
  * *Tiêu chí hoàn thành:* Có minh chứng bài tự giải nháp trước; trả lời đúng Bộ ba câu hỏi vàng; không có hiện tượng chép bài thụ động.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Phiếu bài tập 2 cột A4 có dán giấy che kết quả; Thẻ bỏ túi in màu "Bộ ba câu hỏi vàng".*
  * *Đáp án:* Học sinh đạt chuẩn: Cột 1 có chữ viết tự giải của học sinh; Cột 2 có các nét bút chì đối chiếu, bổ sung.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 2: Chuyển hóa nhận thức thành quy trình thao tác chuẩn mực (Quy tắc 3 bước) và công cụ tự giám sát (Bộ ba câu hỏi vàng).

---

#### LỚP 4 — RA QUYẾT ĐỊNH CÓ ĐIỀU KIỆN THEO BỐI CẢNH VÀ QUẢN TRỊ THỜI GIAN
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `4.A3.1`: *Đánh giá được tính phù hợp của việc sử dụng AI trong các tình huống học tập cụ thể dựa trên mục đích, bối cảnh và quy định của nhà trường.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 42 (M3)`, `KN 43 (M3)`, `KN 44 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Ra quyết định sử dụng AI theo ngữ cảnh (Contextual Decision-making):*
    * *Bối cảnh 1 (CẤM TUYỆT ĐỐI):* Trong các giờ kiểm tra 15 phút, thi giữa kỳ, thi cuối kỳ, hoặc các bài rèn kỹ năng viết chữ đẹp, tính toán cơ bản $\rightarrow$ Tuyệt đối không dùng AI; dùng AI là vi phạm quy chế thi.
    * *Bối cảnh 2 (CHO PHÉP CÓ ĐIỀU KIỆN):* Khi chuẩn bị bài thuyết trình nhóm, khi tìm ý tưởng vẽ tranh cổ động bích báo, khi tìm từ đồng nghĩa để mở rộng vốn từ $\rightarrow$ Được phép dùng AI gợi ý, nhưng bắt buộc phải tự viết lại và ghi rõ nguồn tham khảo.
    * *Bối cảnh 3 (KHUYẾN KHÍCH):* Khi tự học ngoại ngữ tại nhà, luyện hội thoại giao tiếp với chatbot tiếng Anh.
  * *Đơn vị 2: Năng lực tự từ chối gian lận (Academic Integrity):* Biết nói lời từ chối dứt khoát khi bạn trong nhóm rủ chép bài văn do AI tạo ra để nộp lấy điểm cao; hiểu rằng điểm số cao giả tạo sẽ phá hủy năng lực thật của bản thân.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Phân tích Bảng ma trận 4 tình huống học đường phức tạp: Điền cột Quyết định (Dùng / Không dùng / Dùng có điều kiện) và viết 1 câu giải thích lý do pháp lý/đạo đức.
  * *Hành vi 2:* Đóng vai phản biện: Viết 1 đoạn đối thoại ngắn 3 câu thuyết phục bạn không được chép bài luận của AI nộp chấm điểm.
  * *Tiêu chí hoàn thành:* Phân định đúng 100% bối cảnh kiểm tra vs bối cảnh sáng tạo; lời thuyết phục chạm đúng giá trị lòng tự trọng và sự tiến bộ cá nhân.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bảng ma trận quyết định bối cảnh A4; Kịch bản đóng vai "Bài văn điểm 10 của Chatbot".*
  * *Đáp án:* Giờ thi $\rightarrow$ Cấm; Bài tập rèn văn ở nhà $\rightarrow$ Dùng gợi ý dàn ý, tự viết thân bài; Luyện nói tiếng Anh $\rightarrow$ Khuyến khích.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 3: Nâng lên năng lực "Đánh giá bối cảnh và ra quyết định độc lập" gắn liền với quy chế học đường và liêm chính học thuật.

---

#### LỚP 5 — NĂNG LỰC THÍCH ỨNG SỐ VÀ CÂN BẰNG TOÀN DIỆN CUỘC SỐNG
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `5.A3.1`: *Trình bày được rằng AI ngày càng phổ biến trong đời sống, con người cần có kỹ năng số thích ứng nhưng không đánh mất năng lực tự chủ và bản sắc cá nhân.*
  * `5.A3.2`: *Khẳng định được việc sử dụng AI phải phù hợp với nhu cầu, bối cảnh, năng lực cá nhân và tuân thủ các chuẩn mực đạo đức, pháp luật.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 42 (M3)`, `KN 43 (M3)`, `KN 44 (M3)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Năng lực Thích ứng số (Digital Resilience):* Thích ứng không có nghĩa là chạy theo công nghệ mù quáng, mà là biết làm chủ công cụ, sử dụng AI để giải phóng sức lao động chân tay, tập trung thời gian vào tư duy sáng tạo, kỹ năng xã hội và phát triển bản thân.
  * *Đơn vị 2: Nhận diện bẫy thao túng thuật toán:* Các nền tảng video ngắn (TikTok, YouTube Shorts) sử dụng thuật toán AI để giữ chân người dùng liên tục; nếu không có bản lĩnh tự chủ, học sinh sẽ bị thuật toán "dắt mũi", lãng phí hàng giờ vô ích, sa sút học tập và mất ngủ.
  * *Đơn vị 3: Thiết lập Thời gian biểu Cân bằng số (Digital Wellbeing Schedule):*
    * Quy tắc 20-20-20: Cứ 20 phút nhìn màn hình $\rightarrow$ Nhìn xa 20 feet (6 mét) trong 20 giây.
    * Nguyên tắc Cân bằng 3-3-3: Mỗi ngày bảo đảm: Ít nhất 1 giờ vận động thể thao/ngoài trời; Ít nhất 1 giờ tương tác trực tiếp với gia đình/bạn bè; Thời gian màn hình giải trí không vượt quá 1 giờ.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Làm bài trắc nghiệm tự đánh giá "Mức độ tự chủ số của em" (Gồm 5 câu hỏi về thói quen dùng thiết bị, tự tính điểm và nhận diện điểm yếu).
  * *Hành vi 2:* Thiết lập và ký tên vào bản "Thời gian biểu cân bằng số cho tuần tới": Phân bổ khung giờ học tập, thể thao, đọc sách và thời gian dùng thiết bị hợp lý.
  * *Tiêu chí hoàn thành:* Bảng thời gian biểu bảo đảm các tỷ lệ an toàn sức khỏe; học sinh trình bày được 2 biện pháp cụ thể để cưỡng lại sức hút của thuật toán gợi ý video.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bản trắc nghiệm tự đánh giá Digital Wellbeing; Biểu mẫu in sẵn "Thời gian biểu Cân bằng số Tuần lễ mới A4".*
  * *Đáp án:* Thời gian biểu đạt chuẩn: Thời gian màn hình giải trí $\le 1$ giờ/ngày; có khung giờ thể thao và ăn tối cùng gia đình không dùng thiết bị (Device-free zone).
* **Tiến trình Xoắn ốc:** Đỉnh cao cấp Tiểu học: Hoàn thiện năng lực Tự chủ tư duy và Tự quản trị cuộc sống số; xây dựng bản lĩnh công dân số độc lập, vững vàng chuẩn bị bước vào cấp THCS.

---

## TRỤC 5: ĐÁNH GIÁ, KIỂM CHỨNG THÔNG TIN VÀ PHÒNG NGỪA ẢO GIÁC AI, DEEPFAKE

### 1. Bản chất Khoa học & Định hướng Tiến trình Xoắn ốc
* **Bản chất khoa học công nghệ:** 
  * Mô hình trí tuệ nhân tạo (đặc biệt là mô hình thị giác máy tính và mô hình ngôn ngữ lớn) hoạt động dựa trên các hàm xác suất thống kê và phép tính ma trận; chúng **không có khả năng hiểu biết ngữ nghĩa thật sự hay nhận thức về sự thật khách quan (ground truth)**.
  * Hiện tượng **Ảo giác AI (Hallucination)** là việc mô hình ngôn ngữ tạo ra văn bản nghe rất hợp lý, đúng ngữ pháp và tự tin, nhưng lại chứa các sự kiện, số liệu, tên riêng hoặc khái niệm hoàn toàn sai lệch hoặc bịa đặt.
  * Công nghệ **Nội dung giả mạo do AI tạo ra (Deepfake)** sử dụng mạng nơ-ron đối nghịch (GANs) hoặc mô hình khuếch tán (Diffusion models) để hoán đổi khuôn mặt, tổng hợp giọng nói hoặc tạo video người thật làm những việc họ chưa từng làm.
  * Do đó, năng lực cốt lõi của công dân số là **Tư duy phản biện và Hoài nghi khoa học (Critical Evaluation)**: Luôn kiểm chứng bằng chứng, đối chiếu đa nguồn và không bao giờ tin cậy mù quáng vào kết quả do AI tạo ra.
* **Tiến trình xoắn ốc (Grades 1 to 5):**
  * *Lớp 1:* Trực quan môi trường: Nhận biết camera có thể nhìn nhầm khi trời tối, micro có thể nghe nhầm khi xung quanh ồn ào; máy không phải lúc nào cũng đúng (100% Unplugged).
  * *Lớp 2:* Thử nghiệm giới hạn: Chủ động xoay đồ vật góc khó, đưa vật thể lạ vào để tìm ra trường hợp khiến máy phân loại sai.
  * *Lớp 3:* Làm chủ văn bản và bắt lỗi Ảo giác AI: Hiểu bản chất ghép từ của Chatbot; thực hành Quy trình 3 bước kiểm chứng: Chọn điều cần kiểm tra $\rightarrow$ Tìm bằng chứng trong SGK $\rightarrow$ Kết luận (Đúng / Sai / Chưa đủ thông tin).
  * *Lớp 4:* Phòng ngừa Deepfake và Kiểm chứng chéo đa nguồn: Soi tìm các lỗi bất thường trên ảnh/video do AI tạo (bàn tay thừa ngón, chữ méo); thực hiện kỹ thuật đối chiếu chéo trên 2 nguồn tài liệu in độc lập.
  * *Lớp 5:* Kiểm thử định lượng mô hình: Đọc hiểu thanh chỉ số độ tin cậy thời gian thực (**Confidence Bar**), lập **Bảng ma trận kiểm thử (Test Matrix)** trên 10 mẫu độc lập; phát hiện vùng phân vân của thuật toán.

---

### 2. Chi tiết Tiến trình 5 Khối Lớp của Trục 5

#### LỚP 1 — MÔI TRƯỜNG TÁC ĐỘNG VÀ CẢM NHẬN MÁY MÓC CÓ THỂ SAI
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `1.C1.3`: *Nhận biết được rằng máy móc có thể nhìn nhầm hoặc nghe nhầm khi ánh sáng tối hoặc xung quanh quá ồn ào.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 22 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Mắt camera và Tai micro bị giới hạn bởi môi trường:*
    * Mắt camera của máy cũng giống như mắt người: Khi tắt hết đèn hoặc phòng bị tối om, camera không nhìn thấy màu sắc, dễ nhìn nhầm quả bóng thành cái đĩa tròn màu đen.
    * Tai micro của máy khi bị cả lớp cùng nói chuyện ồn ào sẽ bị lẫn tạp âm, máy không phân biệt được tiếng cô giáo nói hay tiếng quạt gió kêu.
  * *Đơn vị 2: Máy móc không hoàn hảo 100%:* Đồ chơi thông minh hay robot cũng có lúc đoán sai, chỉ sai; học sinh không được tin ngay mọi câu trả lời của đồ chơi, khi thấy điều lạ phải hỏi người lớn.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Thí nghiệm Unplugged tại lớp: Giáo viên che một tấm vải mờ trước ống kính camera đồ chơi, học sinh quan sát màn hình và chỉ ra: *"Máy nhìn nhầm con gấu bông thành cái gối vì bị tối và mờ"*.
  * *Hành vi 2:* Đưa ra giải pháp: Khi máy nghe nhầm tiếng hát, học sinh biết đề xuất: *"Cả lớp phải giữ trật tự và em nói lại gần micro hơn"*.
  * *Tiêu chí hoàn thành:* Nêu đúng nguyên nhân máy nhìn nhầm/nghe nhầm do điều kiện môi trường (ánh sáng/tiếng ồn).
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Đèn pin, tấm vải che mờ, đồ vật mẫu (quả bóng, đĩa nhựa, gấu bông); Loa đồ chơi thử nghiệm phát âm.*
  * *Đáp án:* Nguyên nhân máy sai: Do thiếu ánh sáng hoặc do môi trường quá ồn ào.
* **Tiến trình Xoắn ốc:** Điểm khởi đầu: Nhận thức thực tế rằng cỗ máy công nghệ hoàn toàn có thể nhầm lẫn do điều kiện vật lý môi trường.

---

#### LỚP 2 — THỬ NGHIỆM TÌM RA ĐIỀU KIỆN KHIẾN MÁY PHÂN LOẠI SAI
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `2.C3.2`: *Nêu được rằng AI có thể phân loại sai khi đồ vật nhìn quá lạ, hình ảnh bị mờ hoặc âm thanh bị lẫn tạp âm.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 22 (M1)`, `KN 23 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Bản chất của sự nhận nhầm ở bài toán phân loại:* Máy thông minh phân loại dựa trên những góc chụp quen thuộc trong dữ liệu. Khi gặp một vật thể ở góc nhìn bất thường (ví dụ: chiếc cốc nhìn từ trên đáy xuống, con mèo bị che khuất nửa mặt), máy sẽ không tìm thấy đặc trưng quen thuộc và đoán sai.
  * *Đơn vị 2: Điều kiện giới hạn của thuật toán:* Đồ vật bị che khuất một phần, đồ vật bị biến dạng hình học, hoặc ảnh chụp bị rung tay nhòe nét là 3 nguyên nhân hàng đầu khiến AI phân loại sai.
  * *Đơn vị 3: Thái độ khoa học:* Coi việc máy sai là bình thường; nhiệm vụ của con người là tìm ra chỗ sai để hoàn thiện dữ liệu cho máy.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Thử nghiệm đưa đồ vật vào các góc khó: Đưa hộp bút xoay góc nghiêng 90 độ, lấy tay che nửa thân hộp bút; ghi nhận phản hồi của ứng dụng nhận diện mẫu.
  * *Hành vi 2:* Lập bảng theo dõi 2 cột trên phiếu cá nhân: Cột "Mẫu máy đoán đúng" (Chụp thẳng, rõ) vs Cột "Mẫu máy đoán sai" (Chụp nghiêng, che khuất).
  * *Tiêu chí hoàn thành:* Ghi lại được ít nhất 2 trường hợp cụ thể máy nhận diện sai và giải thích được lý do kỹ thuật (bị che khuất hoặc góc nhìn quá lạ).
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Mẫu vật đồ dùng học tập thật (hộp bút, compa, thước dây); Ứng dụng nhận diện đồ vật trực quan trên máy tính giáo viên; Bảng theo dõi lỗi A4.*
  * *Đáp án:* Mẫu nhìn thẳng $\rightarrow$ Đoán đúng 100%. Mẫu bị che khuất 50% hoặc nhìn từ đáy $\rightarrow$ Máy báo nhầm sang đồ vật khác.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 1: Học sinh chủ động tạo ra các tình huống thử thách để khám phá giới hạn nhận diện của thuật toán.

---

#### LỚP 3 — QUY TRÌNH 3 BƯỚC KIỂM CHỨNG THÔNG TIN VÀ PHÁT HIỆN ẢO GIÁC AI
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `3.A3.1`: *Nêu được một số ví dụ cụ thể về việc AI có thể sai (như phần mềm hội thoại tự động Chatbot đưa ra thông tin không đúng sự thật).*
  * `3.A3.2`: *Trình bày được rằng khi sử dụng AI, học sinh cần kiểm tra lại kết quả, so sánh với nhiều nguồn thông tin khác nhau và trao đổi với giáo viên hoặc người lớn để xác minh.*
  * `3.B2.1`: *Nhận biết được hiện tượng thông tin hoặc hình ảnh do AI tạo ra có thể sai lệch, giả mạo hoặc gây hiểu lầm.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 22 (M2)`, `KN 23 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Bản chất của hiện tượng Ảo giác AI (AI Hallucination):*
    * Chatbot (như ChatGPT, Gemini) tạo câu trả lời dựa trên các mẫu ngôn ngữ đã học trong quá trình huấn luyện; máy không có trải nghiệm thực tế đời sống và không có khả năng tự nhận thức đúng/sai.
    * Máy tính toán xác suất từ ngữ để tạo ra một câu văn nghe rất tự nhiên, rất thuyết phục nhưng thông tin bên trong có thể hoàn toàn sai sự thật (bịa ra tên tác giả, nhầm lẫn con số, gán nhầm đặc điểm sinh học).
  * *Đơn vị 2: Nguồn tài liệu tin cậy đối chứng:* Sách giáo khoa của Bộ GD&ĐT, từ điển chính thống, và lời giảng của thầy cô là chuẩn mực đối chứng cho học sinh tiểu học; không dùng một câu trả lời AI khác để kiểm chứng cho câu trả lời của AI đầu tiên.
  * *Đơn vị 3: Quy trình 3 bước kiểm chứng thông tin chuẩn mực:*
    ```text
    Bước 1: CHỌN ĐIỀU CẦN KIỂM TRA (Claim)
            ──► Câu trả lời đang khẳng định chi tiết gì cụ thể? (Con số, năm tháng, địa danh, đặc điểm khoa học).
    Bước 2: TÌM BẰNG CHỨNG (Evidence)
            ──► Mở đúng bài trong Sách giáo khoa, dùng ngón tay chỉ vào dòng chữ chứa thông tin đó.
    Bước 3: ĐƯA RA KẾT LUẬN (Conclusion)
            ──► ĐÚNG / SAI / CHƯA ĐỦ THÔNG TIN ĐỂ KẾT LUẬN. (Nếu sai, viết câu đính chính trích từ SGK).
    ```
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Đọc đoạn văn bản giả lập của Chatbot; dùng bút dạ quang khoanh tròn chi tiết nghi vấn (Ví dụ: *"Miền Nam có mùa bão tuyết"*).
  * *Hành vi 2:* Mở đúng trang SGK Tự nhiên và Xã hội (hoặc Lịch sử - Địa lý) đối chứng; chép lại chính xác dòng trích dẫn làm bằng chứng.
  * *Hành vi 3:* Khoanh tròn ô kết luận "SAI" và viết câu đính chính: *"Miền Nam có mùa mưa và mùa khô (Theo SGK trang 34)"*.
  * *Tiêu chí hoàn thành:* Điền đầy đủ 3 mục trên Phiếu kiểm chứng thông tin; chỉ đúng số trang và dòng sách làm căn cứ đối chứng.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Đoạn văn bản Chatbot giả lập:* "Khí hậu nước ta chia làm 2 miền. Miền Bắc có 4 mùa: xuân, hạ, thu, đông. Miền Nam nóng quanh năm, có 2 mùa rõ rệt là mùa mưa và mùa bão tuyết."
  * *Tài liệu đối chứng:* SGK Tự nhiên và Xã hội Lớp 3 (Bài Khí hậu nước ta, trang 34 dòng 5: *"Miền Nam có hai mùa rõ rệt là mùa mưa và mùa khô"*).
  * *Phiếu kiểm chứng 3 dòng; Đáp án giáo viên:* Kết luận: **SAI**. Đính chính: Mùa khô.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 2: Chuyển lên cấp độ văn bản số; làm chủ quy trình kiểm chứng khoa học 3 bước đối chiếu với tài liệu xuất bản chuẩn mực.

---

#### LỚP 4 — PHÒNG NGỪA NỘI DUNG GIẢ MẠO DEEPFAKE VÀ KIỂM CHỨNG CHÉO ĐA NGUỒN
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `4.B2.1` (Tích hợp): *Nhận biết được nguy cơ của các nội dung giả mạo do AI tạo ra (Deepfake) và kỹ năng phòng ngừa.*
  * `4.A1.1` (Tích hợp): *Nêu được ví dụ về việc công nghệ AI có thể bị lợi dụng để tạo thông tin sai lệch trên môi trường mạng.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 11 (M2)`, `KN 22 (M2)`, `KN 23 (M3)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Bản chất của Nội dung giả mạo do AI tạo ra (Deepfake):*
    * Thuật ngữ chuẩn hóa: Deepfake là hình ảnh, âm thanh hoặc video được tạo ra hoặc chỉnh sửa bằng công nghệ AI tinh vi, khiến người xem tin rằng một người đang nói hoặc làm những điều mà họ chưa từng nói hay làm trong thực tế.
    * Mục đích xấu của kẻ tạo Deepfake: Lừa đảo tiền bạc, bôi nhọ danh dự bạn bè, giả mạo giọng nói bố mẹ gọi điện xin tiền, tạo tin giả gây hoang mang dư luận.
  * *Đơn vị 2: Các dấu hiệu nhận diện bất thường trên ảnh/video Deepfake:*
    * Trên hình ảnh: Bàn tay có 6 ngón hoặc các ngón tay dính liền nhau; mắt nhìn chằm chằm không chớp; nền phía sau bị méo mó, lượn sóng; chữ viết trên bảng hiệu bị biến dạng thành các ký tự vô nghĩa.
    * Trên video/âm thanh: Cử động môi không khớp với lời nói; ánh sáng trên khuôn mặt không khớp với bóng đổ của cơ thể; giọng nói đều đều như robot, thiếu nhịp thở tự nhiên.
  * *Đơn vị 3: Quy tắc Kiểm chứng chéo đa nguồn (Cross-Verification):* Khi tiếp nhận thông tin giật gân, bất thường $
ightarrow$ Không vội tin, không bấm nút Chia sẻ $
ightarrow$ Phải tìm kiếm ít nhất **2 nguồn tin cậy độc lập** (ví dụ: Trang web chính thức của trường và báo Thiếu niên Tiền phong) để đối chiếu.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Soi kính lúp trên 2 bức ảnh (Ảnh chụp thật vs Ảnh vẽ bằng AI); dùng bút khoanh tròn đúng 2 điểm bất thường trên ảnh AI (bàn tay 6 ngón và chữ biển hiệu bị méo).
  * *Hành vi 2:* Đọc 1 mẩu tin giật gân giả lập trên mạng xã hội; thực hành tra cứu chéo trên 2 nguồn tài liệu in giáo viên cung cấp; viết kết luận xác minh: Tin giả do AI tạo ra.
  * *Tiêu chí hoàn thành:* Chỉ ra chính xác các chi tiết bất thường của deepfake; thực hiện đúng thao tác đối chiếu chéo 2 nguồn tài liệu.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bộ 2 ảnh so sánh A4 phóng to chi tiết; Phiếu tin tức giả mạo "Trường tiểu học nghỉ học 1 tháng do bão tuyết"; 2 tài liệu đối chứng (Thông báo chính thức của Ban Giám hiệu và Bản tin thời tiết VTV).*
  * *Đáp án:* Bức ảnh là sản phẩm AI vì bàn tay nhân vật có 6 ngón; Mẩu tin tức là tin giả mạo vì Thông báo của trường và Bản tin VTV khẳng định thời tiết bình thường.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 3: Nhận diện thủ đoạn làm giả đa phương tiện (Deepfake) và nâng cấp lên kỹ năng đối chiếu chéo trên 2 nguồn tài liệu độc lập.

---

#### LỚP 5 — KIỂM THỬ ĐỊNH LƯỢNG MÔ HÌNH VÀ ĐÁNH GIÁ ĐỘ TIN CẬY THỜI GIAN THỰC
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `5.C5.2` (Kiểm thử): *Thực hành kiểm tra và đánh giá kết quả do mô hình học máy đưa ra trên các dữ liệu mới.*
  * `5.C5.MR3`: *Kiểm tra được kết quả do mô hình đưa ra trên tập mẫu mới; lập bảng thống kê chỉ ra những trường hợp máy nhận diện đúng và trường hợp bị nhầm lẫn kèm nguyên nhân kỹ thuật.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 22 (M3)`, `KN 23 (M3)`, `KN 25 (M3)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Bản chất của Kiểm thử mô hình (Testing in Machine Learning):*
    * Huấn luyện (Train) là cho máy học trên tập bài tập có sẵn giải; Kiểm thử (Test) là cho máy làm bài thi với các đề bài hoàn toàn mới toanh mà máy chưa từng nhìn thấy bao giờ.
    * Nếu dùng ảnh cũ đã dạy để kiểm tra thì máy chỉ việc nhớ lại; chỉ khi kiểm tra bằng ảnh mới thì mới biết máy có thực sự học được quy luật hay không.
  * *Đơn vị 2: Đọc hiểu Thanh chỉ số độ tin cậy (Confidence Bar):*
    * Khi đưa một hình ảnh trước webcam, mô hình AI không trả lời tuyệt đối mà đưa ra xác suất: Biển sàn trơn (92%), Biển thoát hiểm (8%).
    * Vùng an toàn: Chỉ số $\ge 80\%$ (Máy rất tự tin và thường đoán đúng).
    * Vùng phân vân: Chỉ số từ $50\%$ đến $70\%$ (Máy đang lưỡng lự, rất dễ nhận nhầm).
  * *Đơn vị 3: Lập Bảng ma trận kiểm thử (Test Matrix) và tính toán độ chính xác:*
    * Thống kê: $\text{Tỷ lệ chính xác (\%)} = \frac{\text{Số mẫu đoán đúng}}{\text{Tổng số mẫu kiểm thử}} \times 100\%$.
    * Phân tích nguyên nhân kỹ thuật khi máy đoán sai: Do góc chụp quá nghiêng, do ánh sáng bị ngược sáng, hoặc do vật thể bị biến dạng.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Thao tác trên Google Teachable Machine: Lần lượt đưa 10 mẫu vật/ảnh mới độc lập trước webcam; quan sát thanh Confidence Bar; ghi nhận kết quả và chỉ số % vào Bảng ma trận kiểm thử.
  * *Hành vi 2:* Tính toán tỷ lệ phần trăm chính xác của mô hình nhóm (Ví dụ: 8/10 mẫu đúng = 80%); chỉ ra 2 trường hợp máy đoán sai và nêu đúng lý do kỹ thuật.
  * *Tiêu chí hoàn thành:* Bảng ma trận kiểm thử ghi chép đủ 10 lượt thử nghiệm thực tế; con số tính toán % chính xác; phân tích được nguyên nhân thất bại của mô hình.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Tập 10 ảnh kiểm thử độc lập (chưa nạp vào tập huấn luyện); Giao diện Teachable Machine Preview; Biểu mẫu Bảng ma trận kiểm thử A4.*
  * *Đáp án:* Bảng kiểm thử hợp lệ: Ghi rõ tên mẫu, dự đoán của máy, chỉ số Confidence %, kết luận Đúng/Sai. Tỷ lệ chính xác trung bình từ 70% đến 90%.
* **Tiến trình Xoắn ốc:** Đỉnh cao cấp Tiểu học: Chuyển từ kiểm chứng định tính sang kiểm thử định lượng bằng số liệu; làm chủ công cụ đánh giá độ tin cậy xác suất và ma trận kiểm thử của kỹ sư AI.

---

## TRỤC 6: GIAO TIẾP VỚI AI VÀ KỸ THUẬT ĐẶT CÂU LỆNH (PROMPTING & CO-CREATION)

### 1. Bản chất Khoa học & Định hướng Tiến trình Xoắn ốc
* **Bản chất khoa học công nghệ:** 
  * Kỹ thuật đặt câu lệnh (Prompt Engineering) là nghệ thuật và khoa học về việc thiết kế các dữ liệu đầu vào (văn bản, giọng nói, hình ảnh) để dẫn dắt các mô hình AI tạo sinh đưa ra kết quả tối ưu, chính xác và phù hợp nhất với mục đích của con người.
  * Nguyên lý vận hành cốt lõi: *"Chất lượng đầu ra phụ thuộc trực tiếp vào chất lượng và ngữ cảnh của đầu vào"* (Garbage Prompt In, Garbage Output Out).
  * Đồng sáng tạo cùng AI (AI Co-creation): Mô hình AI đóng vai trò là cộng sự/trợ lý tạo sinh phác thảo ban đầu; con người giữ vai trò định hướng ý tưởng, tinh chỉnh nghệ thuật, chọn lọc và ra quyết định hoàn thiện sản phẩm.
* **Tiến trình xoắn ốc (Grades 1 to 5):**
  * *Lớp 1:* Khẩu ngữ tự nhiên: Cầm micro đúng khoảng cách, phát âm câu lệnh ngắn 3–4 từ rõ ràng, tròn vành rõ chữ, có lời chào lịch thiệp.
  * *Lớp 2:* Vòng lặp tương tác: Nhận biết cỗ máy nghe chưa rõ lần 1 $\rightarrow$ Chủ động nắn chỉnh câu lệnh lần 2 chi tiết hơn, chậm rãi hơn.
  * *Lớp 3:* Chuyển sang văn bản số: Phân biệt câu lệnh cộc lốc vs câu lệnh rõ việc; nắm vững nguyên tắc *"Đầu vào rõ $\rightarrow$ Đầu ra chuẩn"*.
  * *Lớp 4:* Cấu trúc Câu lệnh 3 thành phần (`[Bối cảnh]` + `[Nhiệm vụ]` + `[Định dạng]`); thực hành kỹ thuật tinh chỉnh đa vòng (Multi-turn Prompting); đồng sáng tạo tranh cổ động trên AutoDraw.
  * *Lớp 5:* Cấu trúc Câu lệnh 4 thành phần hoàn chỉnh; kỹ thuật cung cấp ví dụ mẫu (**Few-shot Prompting**); biến Chatbot thành 'Bạn cùng học' (AI Study Buddy) hỗ trợ học tập cá nhân hóa.

---

### 2. Chi tiết Tiến trình 5 Khối Lớp của Trục 6

#### LỚP 1 — GIAO TIẾP KHẨU NGỮ TỰ NHIÊN VÀ CÂU LỆNH ĐẦU TIÊN
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `1.C1.2`: *Thực hiện được việc nói câu lệnh đơn giản, rõ ràng vào micro để thiết bị thông minh nhận biết.*
  * `1.C1.4`: *Thể hiện thái độ lịch thiệp, vui vẻ khi trò chuyện với trợ lý ảo hoặc điều khiển thiết bị thông minh.*
  * `1.A2.MR1`: *Nêu được rằng lời chào dễ thương, câu nói rõ ràng sẽ giúp việc hợp tác giữa người và máy trở nên vui vẻ, hiệu quả hơn.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 2 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Câu lệnh (Prompt) bằng giọng nói:* Câu lệnh là lời nói em truyền vào tai micro để bảo máy làm một việc cụ thể (ví dụ: mở bài hát, kể chuyện).
  * *Đơn vị 2: Kỹ thuật nói vào micro:* Cầm micro hoặc ghé miệng cách micro từ 5 đến 10 cm; nói tròn vành rõ chữ, tốc độ vừa phải; không hét to vào micro gây rè tiếng, không nói thì thầm lí nhí khiến máy không nghe thấy.
  * *Đơn vị 3: Lời chào văn minh:* Bắt đầu bằng lời chào và kết thúc bằng từ ngữ lịch sự: *"Xin chào Robot, xin mở bài hát Cháu yêu bà ạ!"*.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Thao tác cầm micro/điện thoại đúng tư thế và khoảng cách; phát âm rõ ràng câu lệnh mẫu gồm 4 từ: *"Xin chào, mở nhạc thiếu nhi"*.
  * *Hành vi 2:* Lắng nghe tín hiệu phản hồi của loa (đèn LED xanh sáng hoặc tiếng bíp) xác nhận máy đã nhận lệnh thành công.
  * *Tiêu chí hoàn thành:* Máy/loa thông minh nhận diện được khẩu lệnh ngay từ lần nói đầu tiên; giọng nói rõ ràng, có từ ngữ lễ phép.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Mô hình micro lớp học kết nối loa thông minh; Tranh minh họa tư thế cầm micro đúng vs sai (cầm quá sát miệng vs cầm quá xa).*
  * *Đáp án:* Hành vi đạt: Khoảng cách miệng - micro 5–10 cm; câu lệnh tròn vành rõ chữ; máy nhận diện phát đúng bài hát.
* **Tiến trình Xoắn ốc:** Điểm khởi đầu: Giao tiếp khẩu ngữ tự nhiên; rèn kỹ thuật phát âm và nếp văn hóa giao tiếp công nghệ.

---

#### LỚP 2 — VÒNG LẶP NẮN CHỈNH CÂU LỆNH GIỌNG NÓI LẦN THỨ HAI
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `2.A3.1`: *Nhận biết được rằng mỗi câu hỏi, mỗi mệnh lệnh em nói vào máy là đang cung cấp thêm dữ liệu cho hệ thống.*
  * `2.A2.MR1`: *Thực hành ra lệnh đơn giản bằng giọng nói cho thiết bị thông minh dưới sự giám sát của giáo viên.*
  * `2.A3.MR1`: *Nêu được rằng con người có vai trò quan trọng trong việc cung cấp thông tin đúng sự thật, ngôn từ lịch sự khi tương tác với AI.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 2 (M1)`, `KN 6 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Hiện tượng máy nghe chưa rõ lần 1:* Khi trợ lý ảo trả lời: *"Xin lỗi, tôi chưa hiểu yêu cầu của bạn"* $
ightarrow$ Con người không được cáu gắt mà phải hiểu máy đang thiếu thông tin.
  * *Đơn vị 2: Kỹ thuật nắn chỉnh câu lệnh lần 2 (Prompt Refinement):* Con người chủ động nói lại câu lệnh lần thứ hai bằng cách: Nói chậm hơn, phát âm rõ từng tiếng hơn, và bổ sung thêm từ khóa cụ thể.
    * Ví dụ: Lần 1 nói cộc lốc: *"Mở nhạc"* (Máy bối rối không biết nhạc gì) $
ightarrow$ Lần 2 nắn chỉnh chi tiết: *"Mở bài hát Chú ếch con thiếu nhi"*.
  * *Đơn vị 3: Vai trò chủ động của con người:* Máy chỉ là công cụ tiếp nhận; con người đóng vai trò thuyền trưởng điều khiển và nắn chỉnh kết quả của máy.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Quan sát cô giáo thị phạm tình huống máy không tìm thấy kết quả ở lệnh 1; chỉ ra điểm thiếu sót của câu lệnh lần 1.
  * *Hành vi 2:* Thực hành nói lại câu lệnh lần 2 bằng cách thêm tên bài hát cụ thể; giúp trợ lý ảo phát đúng bài hát yêu cầu.
  * *Tiêu chí hoàn thành:* Câu lệnh lần 2 có bổ sung từ khóa cụ thể; tốc độ phát âm chậm rãi, rõ ràng hơn lần 1; máy nhận lệnh thành công.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Máy chiếu kết nối ứng dụng trợ lý ảo Google Assistant/Siri demo; Thẻ kịch bản tình huống nắn chỉnh câu lệnh 2 lần.*
  * *Đáp án:* Lệnh 1 thất bại do từ khóa chung chung; Lệnh 2 thành công vì bổ sung từ khóa rõ việc: Tên bài hát + Thể loại thiếu nhi.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 1: Nhận thức được vòng lặp tương tác: Thử nghiệm lệnh 1 $\rightarrow$ Đọc phản hồi của máy $\rightarrow$ Nắn chỉnh lệnh 2 chi tiết hơn.

---

#### LỚP 3 — CHUYỂN DỊCH SANG VĂN BẢN VÀ NGUYÊN TẮC CÂU LỆNH RÕ VIỆC
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `3.C2.1` (Tích hợp): *Làm quen với việc sử dụng câu lệnh dạng văn bản để tìm kiếm và tạo ra thông tin học tập.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 4 (M1)`, `KN 6 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Chuyển dịch từ giọng nói sang văn bản gõ phím:* Trên máy tính, con người giao tiếp với AI bằng các dòng chữ gõ vào khung nhập liệu (Prompt Box).
  * *Đơn vị 2: So sánh Câu lệnh cộc lốc vs Câu lệnh rõ việc:*
    * *Câu lệnh cộc lốc (Vague Prompt):* Chỉ gõ 1 từ duy nhất: *"Chó"* hoặc *"Cây cối"* $
ightarrow$ AI trả lời lan man, dài dòng, không đúng thứ em cần.
    * *Câu lệnh rõ việc (Specific Prompt):* Gõ đầy đủ đối tượng, số lượng và yêu cầu: *"Kể tên 3 giống chó thông minh và hiền lành, giải thích ngắn gọn trong 1 câu"* $
ightarrow$ AI trả lời chính xác, đúng trọng tâm.
  * *Đơn vị 3: Nguyên tắc vàng của Prompting:* "Đầu vào càng rõ ràng $\rightarrow$ Đầu ra càng chính xác và hữu ích".
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Đọc bảng đối chiếu 3 cặp câu lệnh; dùng bút đánh dấu tick $(\checkmark)$ vào câu lệnh sẽ giúp AI trả lời tốt hơn.
  * *Hành vi 2:* Đọc 1 câu lệnh cộc lốc giáo viên cho trước (Ví dụ: *"Thời tiết"*); viết lại thành 1 câu lệnh rõ việc hoàn chỉnh vào phiếu bài tập.
  * *Tiêu chí hoàn thành:* Câu lệnh viết lại có đầy đủ: Địa điểm, thời gian và câu hỏi cụ thể (Ví dụ: *"Dự báo thời tiết ngày mai tại Hà Nội có mưa không?"*).
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Phiếu bài tập "Bí kíp đặt câu lệnh rõ việc"; Bảng so sánh 3 cặp câu lệnh cộc lốc vs rõ ràng in trên khổ A3.*
  * *Đáp án:* Câu lệnh viết lại hợp lệ: Có đầy đủ 3 thành phần: Đối tượng cần hỏi + Địa điểm/Phạm vi + Yêu cầu cụ thể.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 2: Chuyển từ khẩu ngữ sang văn bản số; nắm vững nguyên lý cấu trúc câu lệnh rõ việc để kiểm soát chất lượng phản hồi của AI.

---

#### LỚP 4 — CẤU TRÚC CÂU LỆNH 3 THÀNH PHẦN VÀ ĐỒNG SÁNG TẠO SỐ
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `4.C2.1`: *Sử dụng được một số công cụ AI cơ bản để hỗ trợ học tập và sáng tạo (như công cụ gợi ý nét vẽ thông minh, gợi ý từ ngữ).*
  * `4.C2.MR1`: *Thực hành tạo ra sản phẩm sáng tạo số đơn giản với sự trợ giúp của AI và giới thiệu sản phẩm đó trước lớp.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 4 (M2)`, `KN 6 (M2)`, `KN 39 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Công thức Câu lệnh 3 thành phần chuẩn mực:*
    ```text
    ┌────────────────────────────────────────────────────────────────────────┐
    │              CÔNG THỨC CÂU LỆNH 3 THÀNH PHẦN (LỚP 4)                   │
    ├────────────────────────────────────────────────────────────────────────┤
    │ [THÀNH PHẦN 1: BỐI CẢNH / VAI TRÒ] ──► "Em là học sinh lớp 4 đang làm   │
    │                                         bích báo bảo vệ môi trường,"   │
    │ [THÀNH PHẦN 2: NHIỆM VỤ CỤ THỂ]    ──► "hãy gợi ý 3 khẩu hiệu ngắn gọn," │
    │ [THÀNH PHẦN 3: ĐỊNH DẠNG ĐẦU RA]   ──► "mỗi khẩu hiệu không quá 8 từ."   │
    └────────────────────────────────────────────────────────────────────────┘
    ```
  * *Đơn vị 2: Kỹ thuật Tinh chỉnh đa vòng (Multi-turn Prompting):*
    * Vòng 1: Gửi câu lệnh ban đầu $\rightarrow$ Đọc kết quả.
    * Vòng 2: Nắn chỉnh sâu hơn: *"Em thích câu số 2, nhưng hãy thay từ 'rác' bằng từ dễ thương hơn cho học sinh tiểu học"*.
    * Vòng 3: Hoàn thiện sản phẩm cuối cùng.
  * *Đơn vị 3: Khái niệm Đồng sáng tạo cùng AI (AI Co-creation):*
    * Khi dùng nền tảng AutoDraw: Học sinh tự tay phác thảo nét vẽ nguệch ngoạc ban đầu bằng chuột $\rightarrow$ AI nhận diện và đưa ra thanh gợi ý các nét vẽ hoàn chỉnh $\rightarrow$ Học sinh bấm chọn nét vẽ đẹp nhất, tự tay tô màu, sắp xếp bố cục và gõ thông điệp của nhóm.
    * Con người là tác giả chính (lên ý tưởng, chỉ đạo), AI là trợ thủ thực thi nét vẽ.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Viết một câu lệnh 3 thành phần vào khung Prompt Box trên phần mềm học tập theo đúng cấu trúc mẫu.
  * *Hành vi 2:* Thao tác trên AutoDraw: Phác nét chiếc lá/thùng rác $\rightarrow$ Chọn nét vẽ thông minh của AI $\rightarrow$ Tô màu xanh lá $\rightarrow$ Gõ chữ khẩu hiệu *"Bảo vệ cây xanh"* $\rightarrow$ Xuất file ảnh `.png` về máy.
  * *Tiêu chí hoàn thành:* Câu lệnh có đủ 3 thành phần; hoàn thành bức tranh cổ động số trên AutoDraw có ghi nguồn gốc tác quyền.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Công thức thẻ nhớ Câu lệnh 3 thành phần; Phòng máy tính kết nối nền tảng AutoDraw (autodraw.com); Khung mẫu tranh cổ động A4.*
  * *Đáp án:* Sản phẩm số hợp lệ: Tệp ảnh xuất ra có nét vẽ AutoDraw phối hợp màu sắc tự chọn và khẩu hiệu tự tay học sinh gõ.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 3: Làm chủ cấu trúc câu lệnh 3 thành phần; thực hành kỹ thuật tinh chỉnh đa vòng và trải nghiệm trọn vẹn quy trình Đồng sáng tạo cùng AI.

---

#### LỚP 5 — CÂU LỆNH 4 THÀNH PHẦN, KỸ THUẬT FEW-SHOT VÀ AI BẠN CÙNG HỌC
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `5.C2.1` (Tích hợp): *Khai thác các công cụ AI như một trợ thủ hỗ trợ tự học, ôn tập kiến thức và sáng tạo nội dung.*
  * `5.C5.1` (Quy tắc): *Hiểu cách sử dụng các quy tắc và câu lệnh logic để điều khiển hành vi của hệ thống AI.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 4 (M3)`, `KN 5 (M2)`, `KN 6 (M3)`, `KN 39 (M3)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Công thức Câu lệnh 4 thành phần hoàn chỉnh (Master Prompt):*
    1. *[Vai trò - Persona]:* "Đóng vai một giáo viên Lịch sử tiểu học vui tính..."
    2. *[Bối cảnh - Context]:* "...chúng em đang ôn tập bài Chiến thắng Bạch Đằng năm 938..."
    3. *[Nhiệm vụ - Task]:* "...hãy tạo 3 câu hỏi trắc nghiệm vui nhộn kèm đáp án..."
    4. *[Giới hạn & Ràng buộc - Constraints]:* "...mỗi câu hỏi có 3 phương án A, B, C; không dùng từ ngữ quá khó, độ dài toàn bài dưới 100 từ."
  * *Đơn vị 2: Kỹ thuật đưa Ví dụ mẫu (Few-shot Prompting):*
    * Đưa 1 hoặc 2 ví dụ mẫu hoàn chỉnh vào câu lệnh để "dạy nhanh" cho AI phong cách, cấu trúc và định dạng đầu ra mong muốn.
    * *Ví dụ:* Khi muốn AI sáng tác thơ 4 chữ: Cung cấp sẵn khổ 1: *"Cây xanh trong vườn / Đung đưa trước gió / Chim hót lí lo / Chào ngày mới tới"* $\rightarrow$ Ra lệnh: *"Hãy viết tiếp khổ 2 theo đúng vần điệu và phong cách trên"*. AI sẽ bắt chước mẫu cực kỳ chuẩn xác!
  * *Đơn vị 3: Mô hình "Bạn cùng học" (AI Study Buddy):* Sử dụng AI để thử thách bản thân: Yêu cầu AI đặt câu hỏi kiểm tra bài cũ cho em, AI đóng vai người chấm thi, em trả lời và nhờ AI nhận xét điểm mạnh, điểm yếu.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Viết một câu lệnh hoàn chỉnh có đủ 4 thành phần và chứa ít nhất 01 ví dụ mẫu (Few-shot Prompt) trên giao diện Chatbot học đường an toàn.
  * *Hành vi 2:* Thực hiện tương tác vòng 2 để tinh chỉnh: Yêu cầu AI sửa đổi câu hỏi số 2 vì đáp án quá lộ liễu; lưu lại nhật ký hội thoại 2 vòng.
  * *Tiêu chí hoàn thành:* Câu lệnh nạp vào có đầy đủ 4 thành phần và 1 ví dụ mẫu; kết quả AI phản hồi tuân thủ đúng giới hạn độ dài và định dạng yêu cầu.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Mẫu bảng cấu trúc Prompt 4 thành phần A4; Giao diện chatbot AI học đường an toàn; Phiếu nhật ký tương tác Prompt đa vòng.*
  * *Đáp án:* Câu lệnh đạt chuẩn Few-shot: Có đoạn văn bản mẫu làm khuôn mẫu định dạng; sản phẩm AI sinh ra khớp 100% phong cách của ví dụ mẫu.
* **Tiến trình Xoắn ốc:** Đỉnh cao cấp Tiểu học: Đạt đến trình độ Prompting chuyên nghiệp: Few-shot Prompting, Ràng buộc giới hạn đa chiều và Khai thác AI thành công cụ cá nhân hóa việc tự học.

---

## TRỤC 7: DỮ LIỆU HỌC MÁY — THU THẬP, GÁN NHÃN, LÀM SẠCH VÀ ĐA DẠNG HÓA

### 1. Bản chất Khoa học & Định hướng Tiến trình Xoắn ốc
* **Bản chất khoa học công nghệ:** 
  * Dữ liệu (Data) là nền tảng cốt lõi của Trí tuệ nhân tạo hiện đại. Các mô hình học máy (Machine Learning) không hoạt động dựa trên các dòng mã lệnh quy tắc cứng nhắc của lập trình viên, mà tự rút ra các quy luật toán học (patterns/weights) thông qua việc phân tích hàng nghìn ví dụ mẫu trong dữ liệu.
  * Nguyên lý vàng của kỹ thuật dữ liệu: **"Rác vào - Rác ra" (Garbage In - Garbage Out - GIGO)**: Nếu dữ liệu huấn luyện bị sai nhãn (mislabelled), bị mờ nhòe, nhiễu loạn hoặc thiếu đa dạng (biased/unrepresentative), thì mô hình AI tạo ra chắc chắn sẽ đưa ra kết quả sai lệch, thiên vị và nguy hiểm trong thực tế.
  * Chu trình kỹ thuật dữ liệu bao gồm 4 công đoạn nền tảng: (1) Xác định yêu cầu dữ liệu $\rightarrow$ (2) Thu thập dữ liệu mẫu $\rightarrow$ (3) Gán nhãn (Annotation) $\rightarrow$ (4) Làm sạch và khử nhiễu (Data Cleaning & Preprocessing).
* **Tiến trình xoắn ốc (Grades 1 to 5):**
  * *Lớp 1:* Khái niệm trực quan: Máy học từ các ví dụ mẫu; cần nhiều ví dụ mẫu khác nhau về kích thước, màu sắc thì máy mới học đúng (100% Unplugged).
  * *Lớp 2:* Thao tác làm sạch thủ công: Dùng kính lúp đồ chơi soi bộ thẻ tranh ảnh; nhặt bỏ ảnh mờ bẩn, ảnh dán nhầm nhãn sang thùng rác dữ liệu mini.
  * *Lớp 3:* Dữ liệu số trên máy tính: Phân biệt bài toán phân loại vs dự đoán; hiểu bản chất khoa học nguyên lý GIGO; mở thư mục ảnh trên máy tính để xóa tệp ảnh lỗi.
  * *Lớp 4:* Thu thập có định hướng và kỹ thuật Cắt ảnh (Crop): Lập kế hoạch thu thập ảnh đa góc nhìn; dùng công cụ Crop loại bỏ người và hậu cảnh thừa để vật thể chiếm trọn khung hình.
  * *Lớp 5:* Kỹ thuật dữ liệu dự án chuyên sâu: Thiết lập 2 thư mục nhãn cân bằng; làm sạch dữ liệu, khử nhận dạng cá nhân 100%; kiểm toán chéo tính đa dạng của dữ liệu để chống thiên lệch (Bias Audit).

---

### 2. Chi tiết Tiến trình 5 Khối Lớp của Trục 7

#### LỚP 1 — KHÁI NIỆM VÍ DỤ MẪU VÀ SỰ ĐA DẠNG BAN ĐẦU
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `1.D1.1`: *Nhận biết được rằng máy móc thông minh cần được 'dạy' bằng các ví dụ cụ thể do con người cung cấp.*
  * `1.D1.MR1`: *Nêu được rằng cần cung cấp nhiều ví dụ khác nhau thì máy mới nhận biết chính xác được đối tượng.*
  * `1.D2.1`: *Nhận biết được một số đồ dùng, thiết bị chỉ làm được một việc (đơn năng).*
  * `1.D2.2`: *Nhận biết được một số thiết bị thông minh có thể làm được nhiều việc khác nhau (đa năng).*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 28 (M1)`, `KN 29 (M1)`, `KN 32 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Máy học bằng ví dụ mẫu (Examples):* Muốn chú robot giấy nhận biết được đâu là "Quả bóng", em không thể nói luật trừu tượng mà phải cho robot xem các tấm thẻ vẽ quả bóng. Những tấm thẻ đó gọi là **Ví dụ mẫu**.
  * *Đơn vị 2: Vì sao cần nhiều ví dụ mẫu khác nhau?* Nếu em chỉ cho robot xem 1 bức tranh vẽ quả bóng màu đỏ nhỏ xíu $\rightarrow$ Khi đưa quả bóng màu xanh to đùng, robot sẽ không nhận ra! Muốn robot thông minh, ta phải nạp nhiều ví dụ: bóng đỏ, bóng xanh, bóng sọc, bóng to, bóng nhỏ.
  * *Đơn vị 3: Đồ dùng đơn năng vs Đa năng:* Chiếc bút chì chỉ dùng để viết vẽ (đơn năng); chiếc điện thoại thông minh vừa xem giờ, vừa gọi điện, vừa chụp ảnh, vừa mở nhạc (đa năng).
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Chơi trò chơi "Nạp dữ liệu cho Robot": Chọn đúng 5 thẻ tranh vẽ quả táo với các hình thái khác nhau (táo đỏ, táo xanh, táo có cuống lá, quả to, quả nhỏ) đặt vào khay nạp thẻ của robot giấy.
  * *Hành vi 2:* Phân loại 4 đồ vật thật trong lớp vào 2 rổ: Rổ đồ dùng làm 1 việc (cục tẩy, thước kẻ) vs Rổ đồ dùng làm nhiều việc (máy tính bảng, đồng hồ thông minh).
  * *Tiêu chí hoàn thành:* Chọn đủ 5 thẻ mẫu đa dạng màu sắc/kích thước; phân loại đúng 100% đồ dùng đơn năng vs đa năng.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bộ 10 thẻ tranh A5 (5 quả bóng đủ màu, 5 quả táo đủ màu); Mô hình hộp Robot giấy có khay nạp thẻ; Rổ đồ dùng học tập thật.*
  * *Đáp án:* Khay dữ liệu quả táo phải chứa đủ 5 thẻ táo đa dạng. Rổ đa năng: Điện thoại, máy tính bảng; Rổ đơn năng: Bút chì, tẩy.
* **Tiến trình Xoắn ốc:** Điểm khởi đầu: Nhận thức trực quan về "Ví dụ mẫu" và "Tính đa dạng của mẫu" thông qua thao tác tay trên tranh thẻ (100% Unplugged).

---

#### LỚP 2 — BÀI TOÁN PHÂN LOẠI TRỰC QUAN VÀ DỌN RÁC DỮ LIỆU BẰNG KÍNH LÚP
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `2.C3.1`: *Nhận biết được rằng AI có thể phân loại đồ vật (chia đồ vật vào các nhóm khác nhau dựa trên hình ảnh hoặc âm thanh).*
  * `2.D2.1`: *Giải thích được vai trò quan trọng của dữ liệu đối với hoạt động của máy thông minh.*
  * `2.D2.2`: *Giải thích được rằng cần cung cấp dữ liệu đúng đắn, rõ ràng và đủ số lượng ví dụ thì máy mới học tốt.*
  * `2.D1.MR1`: *Nêu được một số ví dụ phù hợp để 'dạy' AI trong một tình huống cụ thể.*
  * `2.D2.MR1`: *Thực hành thu thập một số dữ liệu đơn giản (thẻ tranh, âm thanh) để dạy AI trong bài toán phân loại.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 28 (M1)`, `KN 29 (M1)`, `KN 30 (M1)`, `KN 31 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Bài toán Phân loại trực quan (Classification):* Phân loại là việc gom các đồ vật có đặc điểm giống nhau vào cùng một nhóm (Ví dụ: Nhóm Con vật vs Nhóm Phương tiện giao thông; Nhóm Quả ngọt vs Nhóm Quả chua).
  * *Đơn vị 2: Tiêu chuẩn của Dữ liệu tốt (Good Data):*
    * Dữ liệu phải rõ nét, đủ ánh sáng, không bị nhòe nét.
    * Dữ liệu phải đúng nhãn: Không được để lẫn thẻ ảnh chiếc ô tô vào hộp dán nhãn con vật.
    * Đủ số lượng: Mỗi nhóm phải có ít nhất 5 đến 10 ví dụ mẫu.
  * *Đơn vị 3: Thao tác Dọn rác dữ liệu bằng kính lúp:* Trước khi cho máy học, con người phải đóng vai "bác sĩ dữ liệu", dùng kính lúp soi từng thẻ tranh để phát hiện: Thẻ ảnh bị bẩn lem mực $\rightarrow$ Nhặt bỏ; Thẻ dán sai nhãn $\rightarrow$ Đổi sang hộp đúng.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Cầm kính lúp nhựa soi tập 12 thẻ tranh do giáo viên phát (chứa 10 ảnh chuẩn, 1 ảnh bị nhòe mực hoàn toàn, 1 ảnh con mèo bị xếp nhầm sang hộp ô tô).
  * *Hành vi 2:* Nhặt thẻ ảnh nhòe mực thả vào "Thùng rác dữ liệu"; chuyển thẻ ảnh con mèo về đúng hộp "Động vật".
  * *Tiêu chí hoàn thành:* Phát hiện chính xác 2 thẻ ảnh lỗi; hoàn thiện 2 hộp dữ liệu sạch đạt 100% đúng nhãn và sắc nét.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Kính lúp nhựa trẻ em; Bộ 12 thẻ tranh in màu A5 có cài cắm sẵn lỗi; 2 hộp đựng dữ liệu dán nhãn [Phương tiện giao thông] và [Động vật]; Thùng rác dữ liệu mini.*
  * *Đáp án:* 2 thẻ bị xử lý: Thẻ ảnh chiếc xe bus bị lem mực đen $\rightarrow$ Thùng rác; Thẻ ảnh con mèo $\rightarrow$ Chuyển sang hộp Động vật.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 1: Nâng lên kỹ năng "Phân loại theo nhóm" và thực hành thao tác tay "Soi lỗi và làm sạch dữ liệu thủ công".

---

#### LỚP 3 — DỮ LIỆU SỐ TRÊN MÁY TÍNH VÀ NGUYÊN LÝ "RÁC VÀO - RÁC RA"
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `3.C4.1`: *Trình bày được khái niệm dữ liệu qua các ví dụ cụ thể (hình ảnh, âm thanh, văn bản) và cách AI sử dụng dữ liệu để nhận diện.*
  * `3.C4.MR1`: *Xác định được đặc trưng nổi bật của một số bộ dữ liệu đơn giản (hình dáng, màu sắc, âm thanh).*
  * `3.C5.2`: *Nêu được đặc điểm chính của học máy là học dựa trên dữ liệu mẫu.*
  * `3.C5.3`: *Nêu được một số tình huống áp dụng học máy trong đời sống.*
  * `3.C5.4`: *Nhận biết được bài toán phân loại và bài toán dự đoán qua các ví dụ thực tế.*
  * `3.D2.1`: *Trình bày được rằng nếu dữ liệu đưa vào máy bị sai lệch hoặc thiếu thì mô hình AI tạo ra sẽ hoạt động không chính xác.*
  * `3.D2.MR1`: *Thực hành kiểm tra một bộ dữ liệu mẫu trên máy tính, phát hiện và loại bỏ các dữ liệu bị nhầm lẫn hoặc không đạt yêu cầu.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 28 (M2)`, `KN 29 (M2)`, `KN 30 (M2)`, `KN 31 (M2)`, `KN 33 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Dữ liệu số (Digital Data) và Đặc trưng (Features):* Dữ liệu trong máy tính lưu dưới dạng tệp ảnh `.png`, `.jpg`, tệp âm thanh `.mp3`. AI nhận diện vật thể bằng cách trích xuất các đặc trưng nổi bật: Viền mép lá cây hình răng cưa, màu sắc vỏ quả cam có chấm tinh dầu.
  * *Đơn vị 2: Phân biệt Bài toán Phân loại vs Bài toán Dự đoán:*
    * *Phân loại (Classification):* Chia đối tượng vào các nhóm danh mục đã định sẵn (Ví dụ: Thư đến là Thư rác hay Thư thường; Ảnh quét là Chó hay Mèo).
    * *Dự đoán (Prediction):* Ước tính một giá trị hoặc sự kiện sắp xảy ra trong tương lai dựa trên dữ liệu quá khứ (Ví dụ: Nhìn độ ẩm và mây để dự đoán trời mưa; nhìn diện tích nhà để dự đoán giá tiền).
  * *Đơn vị 3: Nguyên lý khoa học "Rác vào - Rác ra" (Garbage In - Garbage Out):* Máy tính không có trực giác sửa sai; nếu ta nạp 3 ảnh quả ớt vào thư mục quả cà chua $\rightarrow$ Mô hình sau khi huấn luyện sẽ nhận nhầm quả ớt thành cà chua. Dữ liệu rác tạo ra mô hình rác!
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Mở thư mục ảnh thực hành `Tap_Du_Lieu_Hoa_Qua` trên máy tính phòng máy (gồm 12 tệp ảnh); dùng chuột duyệt qua từng ảnh; bấm phím Delete xóa 1 tệp ảnh bị nhòe nét hoàn toàn; đổi tên/chuyển 1 tệp ảnh quả chuối bị lưu nhầm trong thư mục quả táo.
  * *Hành vi 2:* Phân loại 4 tình huống thực tế vào 2 cột trên phiếu: Cột "Bài toán phân loại" vs Cột "Bài toán dự đoán".
  * *Tiêu chí hoàn thành:* Thư mục ảnh trên máy tính được dọn sạch hoàn toàn; phân biệt đúng 100% giữa phân loại và dự đoán.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Thư mục ảnh thực hành `Tap_Du_Lieu_Hoa_Qua` cài sẵn trên máy tính phòng máy; Phiếu học tập phân biệt 2 bài toán.*
  * *Đáp án:* Nhận diện biển báo, lọc thư rác $\rightarrow$ Phân loại; Dự báo thời tiết, đoán giá nhà $\rightarrow$ Dự đoán. Thư mục sau khi làm sạch còn lại đúng 10 ảnh sắc nét.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 2: Chuyển hoàn toàn sang thao tác dữ liệu số trên máy tính; làm chủ nguyên lý khoa học GIGO và phân biệt rõ 2 bài toán học máy nền tảng.

---

#### LỚP 4 — THU THẬP CÓ ĐỊNH HƯỚNG VÀ KỸ THUẬT CẮT ẢNH LOẠI BỎ HẬU CẢNH
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `4.D1.1`: *Xác định được bài toán thực tế cần giải quyết và lập kế hoạch thu thập dữ liệu phù hợp.*
  * `4.D2.1`: *Trình bày được rằng chất lượng của hệ thống AI có thể được cải tiến liên tục thông qua việc nâng cao chất lượng và số lượng dữ liệu.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 29 (M2)`, `KN 30 (M2)`, `KN 31 (M2)`, `KN 32 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Kế hoạch thu thập dữ liệu có định hướng:* Không chụp ảnh bừa bãi; một kế hoạch thu thập dữ liệu chuẩn mực phải xác định:
    * Đối tượng nhận diện là gì? (Ví dụ: Vỏ hộp sữa học đường).
    * Cần bao nhiêu ảnh? (Tối thiểu 8–10 ảnh cho một buổi thực hành).
    * Cần những góc chụp nào? (Chụp chính diện mặt trước, chụp mặt sau, chụp nghiêng góc 45 độ, chụp khi vỏ hộp bị bẹp một phần).
  * *Đơn vị 2: Kỹ thuật Cắt ảnh (Crop) để tập trung đối tượng:*
    * Khi dùng webcam/điện thoại chụp mẫu vật, ảnh thường bị dính bàn tay người cầm, góc bàn bừa bộn hoặc các bạn học sinh đi qua lại phía sau.
    * Nếu để nguyên hậu cảnh lộn xộn, AI sẽ học nhầm các đặc trưng của bức tường hay bàn tay thay vì học chiếc vỏ hộp sữa.
    * Kỹ thuật: Dùng công cụ Crop kéo khung viền sát vào chiếc vỏ hộp sữa, loại bỏ hoàn toàn người và hậu cảnh thừa, bảo đảm vật thể chiếm ít nhất 70% diện tích ảnh.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Lập bảng phân công nhóm 3 học sinh thu thập dữ liệu vỏ hộp sữa và chai nhựa: Bạn A cầm vật mẫu xoay góc, Bạn B bấm chụp webcam, Bạn C phụ trách kiểm tra ảnh.
  * *Hành vi 2:* Mở ảnh vừa chụp trong phần mềm Photos/Paint; thực hiện thao tác kéo khung Crop cắt bỏ bàn tay và nền lớp học; lưu tệp ảnh sạch vào thư mục `Du_Lieu_Hop_Sua_Clean`.
  * *Tiêu chí hoàn thành:* Thu thập đủ 8 ảnh sắc nét ở 3 góc nhìn khác nhau; 100% ảnh đã được crop gọn gàng, vật thể chiếm trọn khung hình.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Mẫu vật thật: 02 vỏ hộp sữa giấy, 02 chai nước khoáng rỗng; Webcam kết nối máy tính; Phần mềm Crop ảnh mặc định Windows.*
  * *Đáp án:* Tập ảnh đạt chuẩn: Vật thể nằm chính giữa, không dính bàn tay người cầm, không có người lạ đi qua hậu cảnh.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 3: Chủ động lập kế hoạch thu thập đa góc nhìn và thành thạo thao tác kỹ thuật Cắt ảnh (Crop) để tối ưu hóa đặc trưng cho máy học.

---

#### LỚP 5 — QUẢN TRỊ DỮ LIỆU DỰ ÁN, CÂN BẰNG NHÃN VÀ KIỂM TOÁN THIÊN LỆCH
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `5.B1.1`, `5.B1.2`: *Nhận biết và phòng ngừa thiên lệch dữ liệu dẫn đến kết quả phân biệt đối xử trong hệ thống AI.*
  * `5.B2.MR1`: *Đề xuất được các quy tắc thu thập dữ liệu công bằng, khử nhận dạng và bảo đảm tính đại diện của dữ liệu.*
  * `5.D1.1`: *Thực hành bước Chuẩn bị dữ liệu hoàn chỉnh trong quy trình thiết kế hệ thống AI.*
  * `5.D2.1`: *Chứng minh được bằng số liệu thực tế rằng việc bổ sung dữ liệu đa dạng sẽ giúp mô hình cải thiện độ chính xác.*
  * `5.D2.MR1`: *Thực hành cải tiến hệ thống AI bằng cách bổ sung dữ liệu các góc khó và tái huấn luyện mô hình.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 29 (M3)`, `KN 30 (M3)`, `KN 31 (M3)`, `KN 32 (M3)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Cấu trúc Tổ chức Thư mục Nhãn chuẩn mực (Dataset Architecture):*
    * Khi làm dự án nhận diện biển báo an toàn học đường, phải thiết lập 2 thư mục con mang đúng tên nhãn kỹ thuật không dấu: `Bien_Canh_Bao_San_Tron` và `Bien_Chi_Dan_Thoat_Hiem`.
    * Nguyên tắc Cân bằng dữ liệu (Class Balance): Số lượng ảnh giữa 2 lớp phải tương đương nhau (ví dụ: 10 ảnh vs 10 ảnh). Nếu một lớp có 30 ảnh mà lớp kia chỉ có 3 ảnh $
ightarrow$ Mô hình sẽ bị thiên lệch nghiêm trọng về lớp có nhiều ảnh hơn!
  * *Đơn vị 2: Khử nhận dạng dữ liệu cá nhân chuyên sâu:* Tuyệt đối không để sót khuôn mặt bạn bè, thẻ tên học sinh hay biển số xe trong tập dữ liệu; kết hợp linh hoạt giữa Crop ảnh và che mờ (Blur) bảo mật.
  * *Đơn vị 3: Kiểm toán chất lượng và tính đại diện của dữ liệu (Data Audit):*
    * Bảng kiểm tra 4 tiêu chí sống còn: (1) Đủ số lượng cân bằng? (2) Đúng nhãn 100%? (3) Đa dạng điều kiện (ánh sáng mạnh, ánh sáng yếu, góc nghiêng)? (4) An toàn quyền riêng tư 100%?
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Độc lập tạo cấu trúc thư mục dự án trên máy tính; phân loại và nạp đúng 10 ảnh cho mỗi lớp nhãn; bảo đảm tỷ lệ cân bằng 10 : 10.
  * *Hành vi 2:* Đổi máy kiểm toán chéo (Cross-audit): Rà soát từng ảnh của nhóm bạn theo Bảng tiêu chí kiểm toán dữ liệu; ký biên bản xác nhận dữ liệu đã sẵn sàng để huấn luyện.
  * *Tiêu chí hoàn thành:* Hai thư mục nhãn có số lượng cân bằng; 100% ảnh đúng nhãn; không có ảnh mờ hỏng; không vi phạm quyền riêng tư.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Mẫu bài toán Biển báo an toàn trường học; Webcam và mô hình biển báo; Biểu mẫu Bảng kiểm toán dữ liệu (Data Audit Checklist) A4.*
  * *Đáp án:* Biên bản kiểm toán đạt chuẩn: Thư mục `Bien_San_Tron` (10 ảnh), `Bien_Thoat_Hiem` (10 ảnh); không còn mặt người; có đủ mẫu góc nghiêng 45 độ và chụp thẳng.
* **Tiến trình Xoắn ốc:** Đỉnh cao cấp Tiểu học: Làm chủ toàn bộ chuỗi kỹ thuật quản trị dữ liệu học máy chuyên nghiệp: Cấu trúc nhãn, Cân bằng số lượng, Khử nhận dạng và Kiểm toán thiên lệch dữ liệu.

---

## TRỤC 8: VẬN HÀNH HỌC MÁY, KIỂM THỬ VÀ QUY TRÌNH THIẾT KẾ HỆ THỐNG AI (AI LIFECYCLE)

### 1. Bản chất Khoa học & Định hướng Tiến trình Xoắn ốc
* **Bản chất khoa học công nghệ:** 
  * Vòng đời hệ thống AI (AI System Lifecycle) là quy trình kỹ thuật hoàn chỉnh để phát triển, triển khai và bảo trì một giải pháp trí tuệ nhân tạo giải quyết vấn đề thực tiễn.
  * Khác với lập trình truyền thống (viết mã lệnh quy tắc cứng), học máy vận hành theo chu trình 4 bước: **Thu thập dữ liệu mẫu $\rightarrow$ Huấn luyện mô hình (Training) $\rightarrow$ Kiểm thử định lượng (Testing) $\rightarrow$ Triển khai và Tái huấn luyện (Deployment & Retraining)**.
  * Tích hợp hệ thống: Mô hình học máy sau khi huấn luyện được xuất mã nhúng để kết nối với các môi trường ứng dụng (như ngôn ngữ lập trình khối Scratch AI) nhằm điều khiển nhân vật, phát âm thanh hoặc kích hoạt thiết bị phần cứng thông minh.
* **Tiến trình xoắn ốc (Grades 1 to 5):**
  * *Lớp 1:* Kể chuyện ý tưởng và chế tạo mô hình robot giấy thủ công Unplugged; trải nghiệm quy trình nạp ví dụ mẫu đơn giản.
  * *Lớp 2:* Ý tưởng giải pháp việc nhà thực tế; quan sát ứng dụng phân loại tự động thời gian thực; thử nghiệm phát hiện khoảnh khắc máy sai.
  * *Lớp 3:* Tiếp cận tư duy thuật toán Nếu - Thì (Rule-based logic); quan sát và gọi tên đúng 4 bước chu trình học máy trên công cụ trực quan Google Teachable Machine.
  * *Lớp 4:* Mô hình hóa kiến trúc hệ thống bằng sơ đồ khối dòng chảy (Flowchart); tự tay thực hiện thao tác tái huấn luyện (Retraining) khi phát hiện máy nhận nhầm.
  * *Lớp 5:* Vận hành độc lập trọn vẹn 5 bước vòng đời hệ thống AI; xuất mã nhúng kết nối Scratch AI lập trình phản hồi thông minh; lập Phiếu thông tin mô hình (**Model Card**) giải trình trách nhiệm.

---

### 2. Chi tiết Tiến trình 5 Khối Lớp của Trục 8

#### LỚP 1 — Ý TƯỞNG CỖ MÁY GIẢI QUYẾT VIỆC NHỎ VÀ CHẾ TẠO MÔ HÌNH GIẤY
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `1.D1.1`: *Nhận biết được rằng máy móc thông minh cần được 'dạy' bằng các ví dụ cụ thể do con người cung cấp.*
  * `1.D2.1`: *Nhận biết được đồ dùng đơn năng.*
  * `1.D2.2`: *Nhận biết được thiết bị đa năng.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 36 (M1)`, `KN 37 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Ý tưởng cỗ máy thông minh giúp em:* Học sinh nêu một khó khăn nhỏ trong ngày (ví dụ: hay quên cất bút chì vào hộp, hay quên giờ đánh răng); tưởng tượng ra một chú robot đồ chơi nhắc nhở em.
  * *Đơn vị 2: Chế tạo mô hình Robot giấy thủ công (STEM/Unplugged):* Dùng hộp bánh quy hoặc bìa các-tông tái chế; cắt dán thân robot, vẽ mắt camera, vẽ miệng cười và tạo một chiếc khay đựng thẻ phía trước bụng.
  * *Đơn vị 3: Diễn tập quy trình dạy máy:* Em cho robot xem thẻ bút chì $\rightarrow$ Robot kêu 'bíp' khen ngoan $\rightarrow$ Em cất bút vào hộp.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Cùng bạn trong bàn cắt dán hoàn thiện mô hình chú robot giấy có khay nạp thẻ từ vật liệu tái chế.
  * *Hành vi 2:* Đứng trước lớp cầm mô hình robot giấy, nói 2 câu giới thiệu: Robot tên là gì và giúp em giải quyết việc gì.
  * *Tiêu chí hoàn thành:* Hoàn thành mô hình robot có khay chứa thẻ; lời giới thiệu nêu rõ công dụng giúp đỡ việc tốt.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Hộp các-tông nhỏ, giấy màu thủ công, kéo an toàn, hồ dán, bút dạ; Thẻ tranh đồ dùng học tập.*
  * *Đáp án:* Sản phẩm hoàn thiện: Mô hình robot đứng vững, có khay nạp thẻ; học sinh trình bày ý tưởng tự tin.
* **Tiến trình Xoắn ốc:** Điểm khởi đầu: Tư duy thiết kế giải pháp ban đầu thông qua hoạt động tạo hình thủ công và kể chuyện sáng tạo (100% Unplugged).

---

#### LỚP 2 — BÀI TOÁN VIỆC NHÀ VÀ TRẢI NGHIỆM PHÂN LOẠI TỰ ĐỘNG THỜI GIAN THỰC
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `2.C3.MR1`: *Quan sát được thao tác phân loại đồ vật do giáo viên thực hiện trên công cụ thông minh trực quan.*
  * `2.D1.1`: *Nêu được một vấn đề gần gũi trong đời sống gia đình có thể giải quyết bằng máy thông minh.*
  * `2.D1.2`: *Nêu được ý tưởng máy thông minh hỗ trợ cuộc sống (giúp ai, giúp việc gì, phản hồi thế nào).*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 34 (M1)`, `KN 36 (M1)`, `KN 37 (M1)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Nhận diện bài toán gia đình thực tế:* Bát đĩa ăn xong bừa bộn; sàn nhà có nhiều vụn bánh rơi; quên tắt đèn phòng khi đi ngủ.
  * *Đơn vị 2: Ý tưởng giải pháp 3 yếu tố:* (1) Máy giúp ai? (Bố mẹ, em nhỏ) $\rightarrow$ (2) Giúp việc gì? (Tự dọn đồ chơi vào rổ) $\rightarrow$ (3) Phản hồi thế nào? (Phát tiếng nhạc vui vẻ khi sàn nhà sạch bóng).
  * *Đơn vị 3: Trải nghiệm phần mềm phân loại trực quan:* Quan sát cô giáo vẽ một nét ngoằn ngoèo trên ứng dụng Quick, Draw!; AI đoán trong 1 giây: "Tôi đoán đây là con rắn, hoặc chiếc boomerang!". Học sinh reo hò và nhận biết tốc độ nhận dạng của thuật toán.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Vẽ một bức tranh ý tưởng A4 về "Cỗ máy dọn bàn học thông minh": Thể hiện rõ bộ phận camera quét bàn và khay đựng bút.
  * *Hành vi 2:* Lên bảng vẽ thử 1 nét trên ứng dụng Quick, Draw! và đọc to phán đoán của AI trên màn hình chiếu.
  * *Tiêu chí hoàn thành:* Tranh vẽ thể hiện đủ 3 yếu tố (Đối tượng phục vụ, Công việc giúp đỡ, Cách phản hồi); tham gia tương tác với phần mềm phân loại.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Giấy vẽ A4, bút màu; Máy tính giáo viên kết nối máy chiếu mở trang Quick, Draw! (quickdraw.withgoogle.com).*
  * *Đáp án:* Bức tranh ý tưởng đạt chuẩn: Có chú thích chức năng của cỗ máy; học sinh gọi tên được khoảnh khắc AI đoán trúng nét vẽ.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 1: Gắn vào bài toán gia đình cụ thể; tiếp xúc trực tiếp với phần mềm nhận dạng phân loại tự động của thế giới thực.

---

#### LỚP 3 — THUẬT TOÁN LOGIC NẾU - THÌ VÀ 4 BƯỚC HỌC MÁY TRÊN TEACHABLE MACHINE
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `3.C5.1`: *Mô tả được cấu trúc 'Nếu... Thì...' trong việc giải quyết tình huống bằng AI đơn giản.*
  * `3.C5.MR1`: *Nêu được một số công cụ AI đơn giản sử dụng cấu trúc 'Nếu... Thì...' (hệ thống lọc thư rác, trả lời tự động).*
  * `3.C5.2`: *Nêu được đặc điểm chính của học máy là học dựa trên dữ liệu mẫu.*
  * `3.C5.MR2`: *Minh họa được bài toán phân loại hình ảnh bằng công cụ trải nghiệm AI trực quan.*
  * `3.D1.1`: *Trình bày được 2 bước cốt lõi ban đầu: Thu thập ví dụ và Cho máy học.*
  * `3.D2.1`: *Hiểu được rằng nếu dữ liệu sai thì mô hình học máy sẽ hoạt động sai.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 34 (M2)`, `KN 40 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Cấu trúc logic Nếu - Thì (Rule-based AI):*
    * Mọi quyết định phản hồi cơ bản đều tuân theo nguyên lý: `NẾU [Điều kiện đúng] THÌ [Thực hiện hành động]`.
    * Ví dụ: *Nếu camera thấy bàn tay giơ lên $\rightarrow$ Thì phát tiếng chuông chào; Nếu camera không thấy ai $\rightarrow$ Thì chuyển sang chế độ ngủ*.
  * *Đơn vị 2: Chu trình 4 bước học máy (Machine Learning Workflow):*
    1. *Bước 1: Thu thập dữ liệu mẫu (Data Collection):* Chụp các bức ảnh mẫu cho từng nhóm.
    2. *Bước 2: Huấn luyện mô hình (Training):* Bấm nút Train Model để máy tính tìm quy luật.
    3. *Bước 3: Kiểm thử mô hình (Testing):* Đưa mẫu vật mới trước webcam để kiểm tra.
    4. *Bước 4: Đánh giá và Cải tiến (Evaluation):* Xem máy đoán đúng hay sai, bổ sung thêm ảnh nếu máy còn nhầm.
  * *Đơn vị 3: Trải nghiệm trên Google Teachable Machine:* Quan sát cô giáo tạo 2 lớp dữ liệu: Lớp 1 (Nắm tay) vs Lớp 2 (Xòe tay); bấm Train Model và xem thanh tiến trình học máy.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Ghép 3 cặp thẻ khối lệnh logic Nếu - Thì trên bảng gài thành các quy tắc điều khiển thông minh hoàn chỉnh.
  * *Hành vi 2:* Đọc tên và sắp xếp đúng thứ tự 4 bước chu trình học máy trên sơ đồ Infographic A4; chỉ đúng nút 'Train Model' trên giao diện Teachable Machine.
  * *Tiêu chí hoàn thành:* Ghép đúng 100% logic Nếu-Thì; ghi nhớ chính xác tên và thứ tự 4 bước học máy.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bộ thẻ khối lệnh Nếu - Thì bằng bìa cứng; Infographic 4 bước học máy A4; Giao diện Google Teachable Machine demo.*
  * *Đáp án:* 3 cặp logic: Nếu [Trời tối] Thì [Bật đèn]; Nếu [Phát hiện rác] Thì [Mở nắp thùng]; Nếu [Thấy người lạ] Thì [Báo động]. Thứ tự 4 bước: Thu thập $\rightarrow$ Huấn luyện $\rightarrow$ Kiểm thử $\rightarrow$ Đánh giá.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 2: Tiếp cận tư duy lập trình thuật toán logic (Nếu - Thì) và nắm vững chu trình 4 bước học máy khoa học.

---

#### LỚP 4 — SƠ ĐỒ DÒNG CHẢY HỆ THỐNG VÀ KỸ THUẬT TÁI HUẤN LUYỆN (RETRAINING)
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `4.D1.1`: *Lập được sơ đồ mô tả giải pháp AI cho một vấn đề học đường đơn giản.*
  * `4.D2.1`: *Trình bày được rằng hệ thống AI có thể được cải tiến liên tục; thực hành việc bổ sung dữ liệu và huấn luyện lại mô hình.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 35 (M2)`, `KN 37 (M2)`, `KN 38 (M2)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Sơ đồ dòng chảy kiến trúc hệ thống AI (System Architecture Flowchart):*
    ```text
    ┌────────────────┐       ┌────────────────────┐       ┌────────────────────────┐
    │ KHỐI ĐẦU VÀO   │ ────► │ KHỐI XỬ LÝ HỌC MÁY │ ────► │ KHỐI ĐẦU RA PHẢN HỒI   │
    │ (Webcam chụp ảnh│       │ (Mô hình phân loại │       │ (Phát loa hướng dẫn    │
    │  rác sân trường)│      │  Hộp sữa / Chai nhựa│      │  hoặc mở ngăn thùng rác│
    └────────────────┘       └────────────────────┘       └────────────────────────┘
    ```
  * *Đơn vị 2: Vòng tròn nâng cấp hệ thống (AI System Lifecycle):* Một cỗ máy AI sau khi huấn luyện xong chưa bao giờ là hoàn hảo vĩnh viễn; khi ra thực tế gặp tình huống mới (vỏ hộp sữa bị dẫm bẹp dúm), máy nhận nhầm $\rightarrow$ Cần con người can thiệp nâng cấp.
  * *Đơn vị 3: Kỹ thuật Tái huấn luyện (Retraining):* Quy trình nâng cấp mô hình: Bước 1: Phát hiện mẫu máy đoán sai $\rightarrow$ Bước 2: Chụp bổ sung 5 ảnh mẫu ở góc bị sai đó nạp thêm vào Class $\rightarrow$ Bước 3: Bấm nút Train Model lần thứ hai $\rightarrow$ Bước 4: Kiểm thử lại để khẳng định độ chính xác đã được cải thiện.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Vẽ sơ đồ khối dòng chảy 3 thành phần cho bài toán "Thùng rác phân loại thông minh" trên giấy A3 nhóm.
  * *Hành vi 2:* Thao tác trên Teachable Machine phòng máy: Nhận một mô hình đang đoán sai mẫu hộp sữa bẹp; chụp bổ sung 5 ảnh hộp sữa bẹp; bấm nút Train lại; kiểm thử lại và chứng minh máy đã nhận diện đúng.
  * *Tiêu chí hoàn thành:* Vẽ đúng sơ đồ 3 khối kiến trúc; thực hiện thành công thao tác tái huấn luyện (Retrain); tỷ lệ nhận diện mẫu lỗi tăng lên.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Bản vẽ sơ đồ khối kiến trúc A3; Mô hình Teachable Machine mẫu đang bị thiếu dữ liệu góc khó; Mẫu vật thử nghiệm.*
  * *Đáp án:* Sơ đồ có đủ 3 khối: Đầu vào $\rightarrow$ Mô hình $\rightarrow$ Đầu ra; Mô hình sau khi Train lại nhận diện đúng mẫu hộp sữa bẹp với độ tin cậy $> 80\%$.
* **Tiến trình Xoắn ốc:** Bước tiến từ Lớp 3: Nâng lên cấp độ "Mô hình hóa kiến trúc hệ thống" và tự tay làm chủ kỹ thuật "Tái huấn luyện (Retraining)" để cải tiến cỗ máy.

---

#### LỚP 5 — HOÀN THIỆN VÒNG ĐỜI HỆ THỐNG AI: KẾT NỐI SCRATCH VÀ MODEL CARD
* **Mã YCCĐ QĐ 2422 bảo trợ:**
  * `5.C5.1`: *Nêu được cách sử dụng cấu trúc Nếu... Thì... trong lập trình AI đơn giản.*
  * `5.C5.MR1`: *Thực hành sử dụng cấu trúc Nếu... Thì... trong lập trình AI đơn giản trên phần mềm lập trình khối.*
  * `5.C5.2`: *Vận hành độc lập công cụ học máy trực quan (tạo lớp, nạp dữ liệu, huấn luyện, kiểm thử).*
  * `5.C5.MR2`: *Huấn luyện được một mô hình phân loại đơn giản trên công cụ trải nghiệm AI trực quan.*
  * `5.D1.1`: *Mô tả được ở mức độ đơn giản về 5 bước cơ bản trong quá trình thiết kế hệ thống AI.*
  * `5.D2.1`: *Chứng minh được hệ thống AI có thể cải tiến thông qua chất lượng dữ liệu.*
  * `5.D2.MR1`: *Thực hành cải tiến hệ thống AI bằng cách bổ sung dữ liệu và tái huấn luyện.*
* **Kỹ năng tích hợp (Ma trận v2.0):** `KN 34 (M3)`, `KN 35 (M3)`, `KN 36 (M3)`, `KN 37 (M3)`, `KN 40 (M3)`, `KN 41 (M3)`.
* **Hạt nhân Kiến thức Cốt lõi (Dạy cái gì?):**
  * *Đơn vị 1: Quy trình 5 bước Vòng đời Hệ thống AI (Complete AI Lifecycle):*
    1. *Bước 1: Xác định bài toán thực tiễn* (Nhận diện biển báo an toàn sảnh trường học).
    2. *Bước 2: Chuẩn bị dữ liệu sạch & khử nhận dạng* (10 ảnh/nhãn, che mờ mặt người).
    3. *Bước 3: Huấn luyện mô hình* (Train Model trên Google Teachable Machine).
    4. *Bước 4: Kiểm thử định lượng* (Test Matrix trên 10 mẫu độc lập).
    5. *Bước 5: Triển khai & Tinh chỉnh* (Xuất model kết nối Scratch và lập Model Card).
  * *Đơn vị 2: Kết nối Mô hình AI với Lập trình khối Scratch AI:*
    * Xuất đường link mô hình (Export Model $\rightarrow$ Upload my model) từ Teachable Machine.
    * Mở Scratch 3.0 với tiện ích mở rộng Teachable Machine / AI Extension; dán đường link mô hình vào khối lệnh khởi tạo.
    * Lập trình kịch bản phản hồi:
      ```text
      KHI [Nhận diện được Biển_San_Tron]
      THÌ [Cho nhân vật phát âm thanh: "Cảnh báo: Sàn trượt, xin đi chậm!"] VÀ [Hiển thị biển cảnh báo màu vàng]
      ```
  * *Đơn vị 3: Lập Phiếu thông tin mô hình (Model Card) giải trình trách nhiệm:* Hoàn thiện tài liệu kỹ thuật công khai minh bạch: Mục đích mô hình, Số lượng ảnh huấn luyện, Tỷ lệ chính xác qua kiểm thử, Giới hạn sai sót và Chữ ký trách nhiệm của nhóm học sinh.
* **Biểu hiện Kỹ năng Vi mô & Tiêu chí Đánh giá (Trong 35 phút):**
  * *Hành vi 1:* Xuất mã nhúng từ Teachable Machine; kết nối thành công vào dự án Scratch phòng máy; lập trình khối lệnh Nếu-Thì phát âm thanh cảnh báo khi đưa biển báo trước camera.
  * *Hành vi 2:* Hoàn thiện 4 mục trên Phiếu Model Card bằng giấy A4; đại diện nhóm đứng lên demo trực tiếp sản phẩm trước Hội đồng chuyên môn của lớp.
  * *Tiêu chí hoàn thành:* Nhân vật Scratch phản hồi chính xác khi đưa biển báo trước webcam; bản Model Card được điền đầy đủ và trung thực về các trường hợp máy còn nhận nhầm.
* **Bộ Học liệu Chuẩn & Đáp án:**
  * *Phòng máy tính kết nối Internet; Môi trường Scratch 3.0 có tiện ích Teachable Machine; Biểu mẫu Model Card A4; 02 biển báo an toàn vẽ tay.*
  * *Đáp án:* Sản phẩm hoàn thiện: Dự án Scratch AI chạy mượt mà theo thời gian thực; bản Model Card có đầy đủ chữ ký cam kết trách nhiệm của các thành viên trong nhóm.
* **Tiến trình Xoắn ốc:** Đỉnh cao cấp Tiểu học: Khép lại toàn bộ vòng đời hệ thống AI: Tích hợp mô hình học máy vào ứng dụng phần mềm Scratch và thực hành chuẩn mực đạo đức trách nhiệm giải trình bằng Model Card.

---

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
