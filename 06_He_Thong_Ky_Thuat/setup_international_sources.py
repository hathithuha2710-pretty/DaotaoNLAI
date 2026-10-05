# -*- coding: utf-8 -*-
import sys
import os
import shutil

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\USER\Desktop\AI-vibe-code\KhungNLĐTAI"
intl_dir = os.path.join(base_dir, "02_Tai_Lieu_Quoc_Te")

# 1. Master Catalog File in 02_Tai_Lieu_Quoc_Te/DANH_MUC_NGUON_TAI_LIEU_QUOC_TE.md
master_catalog = """# DANH MỤC NGUỒN TÀI LIỆU VÀ CHƯƠNG TRÌNH AI QUỐC TẾ CHÍNH THỨC
*(Hệ thống cơ sở dữ liệu đối soát chuẩn mực phục vụ biên soạn chương trình GDPT AI Việt Nam theo QĐ 2422/QĐ-BGDĐT)*

---

## 📌 QUY ĐỊNH TRUY XUẤT NGUỒN (SINGLE SOURCE OF TRUTH & TRACEABILITY)
Mọi chuẩn đầu ra quốc tế (Outcome), kịch bản thực nghiệm, bài tập dữ liệu và tình huống đạo đức được trích dẫn trong Chương trình và Kế hoạch bài dạy bắt buộc phải được truy xuất chính xác từ danh mục các nguồn đã được thẩm định dưới đây. Tuyệt đối không trích dẫn tùy tiện hoặc sử dụng các nguồn không được kiểm chứng.

---

## I. KHUNG THAM CHIẾU QUỐC TẾ TRUNG TÂM (CORE BENCHMARKS)

### 1. UNESCO — AI Competency Framework for Students
* **Thư mục lưu trữ nội bộ:** `02_Tai_Lieu_Quoc_Te/UNESCO/` (`unessco.pdf`, `unesscoVN.pdf`)
* **Tổ chức bảo trợ:** UNESCO (Tổ chức Giáo dục, Khoa học và Văn hóa Liên Hợp Quốc).
* **Vai trò:** Khung tham chiếu quốc tế trung tâm (North Star), định hình 4 chiều năng lực:
  1. Tư duy lấy con người làm trung tâm (Human-centred mindset)
  2. Đạo đức AI (Ethics of AI)
  3. Kỹ thuật và ứng dụng AI (AI techniques and applications)
  4. Thiết kế hệ thống AI (AI system design)
* **3 mức độ thành thạo:** Hiểu (Understand) $\\rightarrow$ Áp dụng (Apply) $\\rightarrow$ Sáng tạo (Create).

### 2. AI4K12 — Five Big Ideas in AI
* **Thư mục lưu trữ nội bộ:** `02_Tai_Lieu_Quoc_Te/AI4K12/` (`AI4K12-Big-Idea-1` đến `5.pdf`)
* **Tổ chức bảo trợ:** AAAI (Hiệp hội Trí tuệ nhân tạo Hoa Kỳ) + CSTA (Hiệp hội Giáo viên Khoa học Máy tính Hoa Kỳ), tài trợ bởi Quỹ Khoa học Quốc gia Hoa Kỳ (NSF).
* **Vai trò:** Benchmark chiều sâu khoa học máy tính cho K-12 với 5 Ý tưởng lớn:
  * Big Idea 1: Cảm nhận (Perception)
  * Big Idea 2: Biểu diễn và lập luận (Representation & Reasoning)
  * Big Idea 3: Học máy (Machine Learning)
  * Big Idea 4: Tương tác tự nhiên (Natural Interaction)
  * Big Idea 5: Tác động xã hội (Societal Impact)

---

## II. KHUNG CHƯƠNG TRÌNH & HỌC LIỆU AI CHO HỌC SINH (K-12 CURRICULUM)

### 3. Experience AI — Google DeepMind + Raspberry Pi Foundation
* **Thư mục nội bộ:** `02_Tai_Lieu_Quoc_Te/Experience_AI_Google_DeepMind/`
* **Đường dẫn chính thức:** [https://experience-ai.org/en/units](https://experience-ai.org/en/units)
* **Tổ chức bảo trợ:** Google DeepMind hợp tác cùng Raspberry Pi Foundation (Anh Quốc).
* **Phân chia theo lứa tuổi:**
  * **8–12 tuổi (Tiểu học):** Khóa *Discovering AI* (Khái niệm AI cơ bản, dữ liệu, nhận diện quy luật - pattern, dự đoán - prediction).
  * **11–14 tuổi (THCS):** 2 Module toàn diện:
    * *Module 1 – Understanding AI:* Thị giác máy tính, Generative AI, Thiên lệch (Bias), tác động xã hội.
    * *Module 2 – Solving Problems with AI:* Thiết kế và đánh giá giải pháp AI trong thực tiễn.
    * *Foundations of AI:* 6 bài học thực hành tự huấn luyện mô hình phân loại ảnh (Teachable Machine), cây quyết định, thẻ mô hình (Model card).
* **Tài nguyên cung cấp:** Trọn gói bao gồm Lesson plan, Teacher guide, Slide bài giảng (PPTX), Phiếu bài tập (Worksheets), Bộ thuật ngữ (Glossary), Thang đánh giá rubric và đáp án.

### 4. Day of AI Curriculum Resources — MIT RAISE + i2 Learning
* **Thư mục nội bộ:** `02_Tai_Lieu_Quoc_Te/MIT_Day_of_AI/` (và lưu trữ gốc tại `02_Tai_Lieu_Quoc_Te/Khac/DAI-*`)
* **Đường dẫn chính thức:** [https://dayofai.org/curriculum-resources](https://dayofai.org/curriculum-resources)
* **Tổ chức bảo trợ:** Viện Công nghệ Massachusetts (MIT RAISE) hợp tác cùng i2 Learning.
* **Đối tượng:** Đầy đủ từ Tiểu học đến THPT (K-12).
* **Trọng tâm:** Bộ giáo trình ngày hội AI nổi tiếng của MIT; cung cấp kịch bản học tập trải nghiệm, hoạt động thực nghiệm không máy tính (Unplugged) và dự án sáng tạo AI.

### 5. AI Literacy Lessons for Grades 6–12 — Common Sense Education
* **Thư mục nội bộ:** `02_Tai_Lieu_Quoc_Te/Common_Sense_Education/`
* **Đường dẫn chính thức:** [https://www.commonsense.org/education/collections/ai-literacy-lessons-for-grades-6-12](https://www.commonsense.org/education/collections/ai-literacy-lessons-for-grades-6-12)
* **Tổ chức bảo trợ:** Common Sense Education (Hoa Kỳ - Tổ chức phi lợi nhuận hàng đầu thế giới về an toàn số học đường).
* **Đối tượng:** Học sinh Lớp 6 đến Lớp 12 (THCS & THPT).
* **Trọng tâm:** Giáo dục năng lực số (AI Literacy), đạo đức công nghệ, an toàn dữ liệu, nhận diện tin giả/nội dung giả mạo (Deepfake) và văn hóa ứng xử liêm chính học thuật.

### 6. AI Quests — Google Research + Stanford University
* **Thư mục nội bộ:** `02_Tai_Lieu_Quoc_Te/Google_for_Education_va_Stanford/`
* **Đường dẫn tra cứu:** Nằm trong hệ sinh thái [https://grow.google/intl/europe/ai-skills/](https://grow.google/intl/europe/ai-skills/)
* **Tổ chức bảo trợ:** Google Research hợp tác cùng Đại học Stanford (Hoa Kỳ).
* **Đối tượng:** Học sinh 11–14 tuổi (THCS).
* **Trọng tâm:** Tiếp cận theo hướng Game hóa (Game-based learning / Problem-solving) qua chuỗi hành trình:
  $$\\text{Nhiệm vụ (Mission)} \\rightarrow \\text{Vấn đề} \\rightarrow \\text{Dữ liệu} \\rightarrow \\text{AI} \\rightarrow \\text{Ra quyết định} \\rightarrow \\text{Phản tư (Reflection)}$$

### 7. Teaching Responsible Use of AI — Google for Education
* **Thư mục nội bộ:** `02_Tai_Lieu_Quoc_Te/Google_for_Education_va_Stanford/`
* **Đường dẫn chính thức:** [https://edu.google.com/ai/education/](https://edu.google.com/ai/education/)
* **Tổ chức bảo trợ:** Google for Education.
* **Đối tượng:** Học sinh phổ thông K-12.
* **Trọng tâm:** Khung 5 nguyên tắc đạo đức & an toàn số:
  1. AI là công nghệ - không phải con người (không nhân hóa máy móc).
  2. AI hỗ trợ năng lực chứ không thay thế con người (tư duy tự chủ).
  3. Luôn tư duy phản biện khi nhận kết quả từ AI (kiểm chứng độc lập).
  4. Nhận diện deepfake và nội dung độc hại.
  5. Bảo vệ an toàn dữ liệu và quyền riêng tư cá nhân.

---

## III. CHƯƠNG TRÌNH ĐÀO TẠO & PHÁT TRIỂN NĂNG LỰC GIÁO VIÊN (TEACHER TRAINING)

### 8. Google AI Educator Series — Google + ISTE / ASCD
* **Đường dẫn:** [https://edu.google.com/learning-center/google-ai-educator-series/](https://edu.google.com/learning-center/google-ai-educator-series/)
* **Đối tượng:** Giáo viên K-12.
* **Nội dung:** Các khóa micro-learning (15 phút/module) về: Hiểu nền tảng AI, ứng dụng sư phạm (thiết kế trải nghiệm học tập) và tối ưu quản lý hành chính (soạn giáo án, đánh giá).

### 9. Generative AI for Educators with Gemini — Google + MIT RAISE
* **Đường dẫn:** [https://grow.google/intl/europe/ai-skills/](https://grow.google/intl/europe/ai-skills/)
* **Đối tượng:** Giáo viên các cấp (không yêu cầu nền tảng kỹ thuật).
* **Nội dung:** Khóa đào tạo 2 giờ hướng dẫn viết câu lệnh (prompt), tạo học liệu giảng dạy, cá nhân hóa bài giảng và sử dụng AI có trách nhiệm (Gemini, NotebookLM).

---

## IV. CÁC KHUNG CHÍNH SÁCH & NĂNG LỰC QUỐC GIA (POLICY & JURISDICTION BENCHMARKS)

### 10. OECD — Learning Compass 2030 & AILit Framework
* **Thư mục nội bộ:** `02_Tai_Lieu_Quoc_Te/OECD_va_Singapore_MOE/`
* **Tổ chức bảo trợ:** Tổ chức Hợp tác và Phát triển Kinh tế (OECD) + Ủy ban Châu Âu (EC) phối hợp Code.org.
* **Trọng tâm:** Năng lực làm chủ kỹ thuật số (Digital Agency), an toàn và bảo vệ trẻ em trong môi trường số (Digital Safety for Minors), trách nhiệm giải trình dữ liệu (Data Accountability).

### 11. Singapore MOE — National Digital Literacy Programme (NDLP)
* **Thư mục nội bộ:** `02_Tai_Lieu_Quoc_Te/OECD_va_Singapore_MOE/`
* **Cơ quan ban hành:** Bộ Giáo dục Singapore (MOE) phối hợp AI Singapore.
* **Trọng tâm:** EdTech Masterplan 2030, chương trình Cyber Wellness (văn hóa ứng xử số, liêm chính số, chống ỷ lại nhận thức công nghệ, tôn trọng bản quyền và quy tắc xin phép đồng thuận).

---

## V. BẢNG TỔNG HỢP CÁC TỔ CHỨC QUỐC TẾ UY TÍN BẢO TRỢ
* **Google DeepMind & Google Research** (Hoa Kỳ / Anh)
* **Raspberry Pi Foundation** (Anh Quốc)
* **MIT RAISE — Viện Công nghệ Massachusetts** (Hoa Kỳ)
* **Stanford University** (Hoa Kỳ)
* **Common Sense Education** (Hoa Kỳ)
* **ISTE & ASCD** (Tổ chức Quốc tế về Công nghệ và Phát triển Giáo dục)
* **UNESCO** (Tổ chức Giáo dục, Khoa học và Văn hóa Liên Hợp Quốc)
* **AAAI & CSTA** (Hiệp hội Trí tuệ nhân tạo và Giáo viên KHMT Hoa Kỳ)
* **OECD** (Tổ chức Hợp tác và Phát triển Kinh tế)
* **Singapore MOE** (Bộ Giáo dục Singapore)
"""

with open(os.path.join(intl_dir, "DANH_MUC_NGUON_TAI_LIEU_QUOC_TE.md"), "w", encoding="utf-8") as f:
    f.write(master_catalog)

with open(os.path.join(intl_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(master_catalog)

# 2. Create subdirectories in 02_Tai_Lieu_Quoc_Te/
folders = {
    "Experience_AI_Google_DeepMind": """# TÀI LIỆU CHƯƠNG TRÌNH: EXPERIENCE AI (GOOGLE DEEPMIND & RASPBERRY PI)
* **Đơn vị:** Google DeepMind + Raspberry Pi Foundation (Anh Quốc).
* **Website:** https://experience-ai.org/en/units
* **Chương trình:**
  - Tiểu học (8-12 tuổi): Discovering AI (Khái niệm cơ bản, dữ liệu, quy luật, dự đoán).
  - THCS (11-14 tuổi): Module 1 (Understanding AI), Module 2 (Solving Problems with AI), Foundations of AI (6 bài học thực hành tự huấn luyện mô hình).
* **Tài nguyên:** Giáo án chi tiết, slide PPTX, bài tập học sinh, thang rubric, bảng thuật ngữ glossary.""",

    "MIT_Day_of_AI": """# TÀI LIỆU CHƯƠNG TRÌNH: DAY OF AI (MIT RAISE & i2 LEARNING)
* **Đơn vị:** Viện Công nghệ Massachusetts (MIT RAISE) + i2 Learning.
* **Website:** https://dayofai.org/curriculum-resources
* **Đối tượng:** Toàn bộ K-12.
* **Trọng tâm:** Bộ giáo trình ngày hội AI nổi tiếng của MIT; kịch bản học tập trải nghiệm, hoạt động không máy tính (Unplugged) và dự án sáng tạo AI.
* **Tệp tài liệu gốc lưu trữ tại thư mục:** Các file PDF `DAI-*` đã được tích hợp đầy đủ.""",

    "Common_Sense_Education": """# TÀI LIỆU CHƯƠNG TRÌNH: AI LITERACY (COMMON SENSE EDUCATION)
* **Đơn vị:** Common Sense Education (Hoa Kỳ).
* **Website:** https://www.commonsense.org/education/collections/ai-literacy-lessons-for-grades-6-12
* **Đối tượng:** Lớp 6 đến Lớp 12 (THCS & THPT).
* **Trọng tâm:** Năng lực hiểu biết số (AI Literacy), đạo đức công nghệ, an toàn dữ liệu, nhận diện deepfake và văn hóa ứng xử mạng.""",

    "Google_for_Education_va_Stanford": """# TÀI LIỆU CHƯƠNG TRÌNH: GOOGLE FOR EDUCATION & STANFORD AI QUESTS
* **Google for Education - Teaching Responsible Use of AI:** https://edu.google.com/ai/education/
  - Khung 5 nguyên tắc đạo đức & an toàn số: AI là công nghệ; AI hỗ trợ - không thay thế; Tư duy phản biện; Nhận diện deepfake; Bảo vệ dữ liệu.
* **Stanford AI Quests (Google Research + Stanford University):** https://grow.google/intl/europe/ai-skills/
  - Tiếp cận Game hóa (Game-based learning) giải quyết vấn đề cho học sinh 11-14 tuổi.
* **Đào tạo giáo viên:** Google AI Educator Series (với ISTE/ASCD) và Generative AI for Educators (với MIT RAISE).""",

    "OECD_va_Singapore_MOE": """# TÀI LIỆU KHUNG CHÍNH SÁCH: OECD & SINGAPORE MOE
* **OECD Learning Compass 2030 & AILit Framework:**
  - Định hướng phát triển năng lực tự chủ số (Digital Agency), bảo vệ an toàn cho trẻ vị thành niên trên không gian mạng, tính công bằng và chống thiên lệch dữ liệu.
* **Singapore MOE - National Digital Literacy Programme (NDLP) & Cyber Wellness:**
  - Triết lý giáo dục tự chủ, kiên quyết chống ỷ lại nhận thức vào công nghệ số, liêm chính học thuật, đạo đức tôn trọng bản quyền và quy tắc xin phép đồng thuận."""
}

for folder_name, desc in folders.items():
    fpath = os.path.join(intl_dir, folder_name)
    os.makedirs(fpath, exist_ok=True)
    with open(os.path.join(fpath, "THONG_TIN_CHUONG_TRINH.md"), "w", encoding="utf-8") as f:
        f.write(desc)

# 3. Copy DAI files from Khac to MIT_Day_of_AI for convenience
khac_dir = os.path.join(intl_dir, "Khac")
mit_dir = os.path.join(intl_dir, "MIT_Day_of_AI")
if os.path.exists(khac_dir):
    for fn in os.listdir(khac_dir):
        if fn.startswith("DAI"):
            src = os.path.join(khac_dir, fn)
            dst = os.path.join(mit_dir, fn)
            if not os.path.exists(dst):
                shutil.copy2(src, dst)

print("Setup completed successfully in 02_Tai_Lieu_Quoc_Te!")
