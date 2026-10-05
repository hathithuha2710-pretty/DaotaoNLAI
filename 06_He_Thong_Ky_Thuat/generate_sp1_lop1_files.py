# -*- coding: utf-8 -*-
"""
Script tạo 3 file YCCĐ Lớp 1 chuẩn hóa:
1. SP1_Khung_YCCD_AI_Lop1_Day_Du.docx (Bảng 5 cột đối sánh đầy đủ)
2. SP1_Khung_YCCD_AI_Lop1_Day_Du.md (Bản Markdown 5 cột đầy đủ)
3. SP1_Khung_YCCD_AI_Lop1_Rut_Gon.docx (Bản Word rút gọn 4 cột chỉ gồm STT | Mạch năng lực | Chủ đề con | YCCĐ)
"""
import os
import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

data_lop1 = [
    {
        "stt": 1, "code": "1.A1.1",
        "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "Tính chủ động của con người – Con người có cảm xúc, AI thì không",
        "yccd_vn": "Nêu được ví dụ về các cảm xúc quen thuộc của bản thân (vui, buồn, tức giận, sợ hãi) và nhận ra rằng con người cảm thấy vui buồn thật sự, còn máy móc thì không.",
        "intl_full": "• UNESCO (Human-Centred Mindset): Nhận biết cảm xúc tự nhiên chân thực của con người; hiểu rằng máy móc, AI không có cảm xúc thật sự mà chỉ là thiết bị nhân tạo.\n• Singapore MOE (Cyber Wellness): Nhận thức sự khác biệt giữa người và máy; tránh nhân hóa công nghệ số (Avoiding anthropomorphism).",
        "intl_compact": "Nhận biết cảm xúc tự nhiên chân thực của con người; hiểu rằng máy móc, AI không có cảm xúc thật sự mà chỉ là thiết bị nhân tạo. Tránh nhân hóa công nghệ số (Avoiding anthropomorphism)."
    },
    {
        "stt": 2, "code": "1.A1.2",
        "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "Tính chủ động của con người – Con người có cảm xúc, AI thì không",
        "yccd_vn": "Nêu được rằng máy thông minh chỉ bắt chước hoặc nhận biết nét mặt của con người, chứ không có cảm xúc như con người.",
        "intl_full": "• OECD (Learning Compass 2030): Phân biệt biểu hiện mô phỏng của máy với cảm xúc chân thật; không ngộ nhận máy có sự đồng cảm như con người.\n• AI4K12 (Big Idea 5 - Facial Recognition): Nhận biết AI có thể nhận diện một số biểu hiện nét mặt con người (vui, buồn, ngạc nhiên) nhưng không có cảm xúc thật.",
        "intl_compact": "Nhận biết AI có thể nhận diện một số biểu hiện nét mặt con người (vui, buồn, ngạc nhiên) nhưng máy móc không có cảm xúc thật; không ngộ nhận tín hiệu mô phỏng của máy là sự đồng cảm."
    },
    {
        "stt": 3, "code": "1.A1.3",
        "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "Tính chủ động của con người – AI thể hiện cảm xúc do con người lập trình",
        "yccd_vn": "Nêu được rằng việc AI thể hiện cảm xúc (như hình mặt cười, giọng nói vui vẻ) là do con người tạo ra hoặc lập trình từ trước.",
        "intl_full": "• UNESCO (Human Agency & Oversight): Khẳng định con người là chủ thể thiết kế, lập trình và xây dựng hệ thống AI.\n• Singapore MOE (Primary Computing): Nhận biết rằng khả năng AI thể hiện hoặc mô phỏng cảm xúc (mặt cười, giọng vui vẻ) là do con người thiết kế và tạo ra; AI không tự có cảm xúc.",
        "intl_compact": "Nhận biết rằng khả năng AI thể hiện hoặc mô phỏng cảm xúc (mặt cười, giọng vui vẻ) là do con người thiết kế, lập trình và xây dựng hệ thống; AI không tự có cảm xúc như con người."
    },
    {
        "stt": 4, "code": "1.A1.4",
        "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "Tính chủ động của con người – AI thể hiện cảm xúc do con người lập trình",
        "yccd_vn": "Nêu được ví dụ khi máy phát ra câu chào hoặc cười theo mẫu do con người thiết kế (ví dụ: loa thông minh nói 'Chào bạn, tôi có thể giúp gì?').",
        "intl_full": "• Singapore MOE (Independent Thinking): Nhận biết lời nói hoặc câu chào của trợ lý AI là phản hồi do hệ thống tạo ra theo cách con người thiết kế, rèn luyện thói quen tự chủ, không ngộ nhận đó là cảm xúc thật của máy.\n• AI4K12 (Big Idea 5 - Natural Interaction): Phân biệt sự giao tiếp chân thực giữa con người với phản hồi do hệ thống công nghệ tạo ra.",
        "intl_compact": "Nhận biết lời nói hoặc câu chào giống cảm xúc của trợ lý AI là phản hồi do hệ thống tạo ra theo cách con người thiết kế, không phải cảm xúc thật của máy; phân biệt giao tiếp người với phản hồi của máy."
    },
    {
        "stt": 5, "code": "1.A2.1",
        "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "AI vì sự tiến bộ của con người – Ý nghĩa cảm xúc mà AI thể hiện",
        "yccd_vn": "Chỉ ra được các cách máy thông minh thể hiện cảm xúc (như nháy đèn, hiện hình mặt cười, phát giọng nói nhẹ nhàng).",
        "intl_full": "• UNESCO (AI Interface Literacy): Nhận diện các cách AI mô phỏng trạng thái hoặc cảm xúc qua hình ảnh (mặt cười), tín hiệu ánh sáng (nháy đèn) và âm thanh (giọng nói nhẹ nhàng).\n• OECD (Human-AI Interaction): Làm quen với các hình thức biểu đạt trực quan và thính giác mà công nghệ sử dụng để tương tác với người dùng.",
        "intl_compact": "Nhận diện các cách máy thông minh thể hiện trạng thái và cảm xúc mô phỏng qua hình ảnh (mặt cười), ánh sáng (nháy đèn) và âm thanh (giọng nói nhẹ nhàng) khi tương tác."
    },
    {
        "stt": 6, "code": "1.A2.MR1",
        "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "AI vì sự tiến bộ của con người – Ý nghĩa cảm xúc mà AI thể hiện",
        "yccd_vn": "Nêu được rằng giọng nói thân thiện và hình ảnh dễ thương giúp con người cảm thấy gần gũi, dễ chịu khi nhờ máy giúp đỡ.",
        "intl_full": "• OECD (Digital Well-being for Children): Hiểu rằng các biểu hiện thân thiện (giọng nói nhẹ nhàng, hình ảnh dễ thương) giúp người dùng cảm thấy gần gũi, thoải mái và dễ tương tác khi nhờ máy giúp đỡ.\n• Singapore MOE (Cyber Wellness): Tạo tâm lý tích cực, tự tin và an tâm khi giao tiếp với các thiết bị công nghệ thông minh.",
        "intl_compact": "Hiểu rằng giọng nói thân thiện và hình ảnh dễ thương giúp con người cảm thấy gần gũi, dễ chịu và thuận tiện hơn khi giao tiếp, nhờ máy thông minh giúp đỡ."
    },
    {
        "stt": 7, "code": "1.A2.2",
        "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "AI vì sự tiến bộ của con người – Nhận diện AI trong cuộc sống",
        "yccd_vn": "Kể tên được một số đồ dùng thông minh quen thuộc có thể tự thực hiện việc đơn giản (như robot hút bụi, camera nhận mặt, loa nghe lệnh).",
        "intl_full": "• Singapore MOE (Smart Nation in Daily Life): Nhận diện các đồ dùng, thiết bị quen thuộc có ứng dụng AI hỗ trợ đời sống (như robot hút bụi, camera nhận diện khuôn mặt, loa thông minh nhận lệnh giọng nói).\n• AI4K12 (Big Idea 5 - Societal Impact): Nhận biết sự hiện diện của các ứng dụng AI xung quanh môi trường gia đình và trường học.",
        "intl_compact": "Kể tên và nhận diện các thiết bị quen thuộc có sử dụng AI trong gia đình và trường học (như robot hút bụi, camera nhận diện khuôn mặt, loa thông minh nghe lệnh giọng nói)."
    },
    {
        "stt": 8, "code": "1.A2.3",
        "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "AI vì sự tiến bộ của con người – Nhận diện AI trong cuộc sống",
        "yccd_vn": "Nói được việc làm có ích của từng đồ dùng thông minh (như robot hút bụi giúp quét nhà sạch sẽ, loa giúp mở bài hát theo lời nói).",
        "intl_full": "• UNESCO (AI Solutions for Daily Life): Mô tả công dụng có ích cụ thể của từng thiết bị ứng dụng AI (robot hút bụi giúp quét dọn sạch sẽ, loa thông minh phát nhạc theo yêu cầu) và cách AI giúp thiết bị hoạt động thông minh, tiện lợi hơn.\n• OECD (Future Skills 2030): Nhận thức về sự hỗ trợ thiết thực của công nghệ thông minh giúp cuộc sống con người thuận tiện hơn.",
        "intl_compact": "Mô tả được công dụng có ích của từng đồ dùng có sử dụng AI (robot quét nhà, loa mở nhạc theo lời nói) và cách AI giúp đồ dùng hoạt động thông minh, phục vụ con người hiệu quả hơn."
    },
    {
        "stt": 9, "code": "1.B1.1",
        "strand": "B. Đạo đức AI",
        "subtopic": "Các khía cạnh đạo đức của AI – Việc làm tốt và việc làm xấu",
        "yccd_vn": "Nêu được một vài việc không nên làm khi dùng thiết bị thông minh (như bật tiếng quá to làm phiền mọi người, dùng máy trêu chọc bạn).",
        "intl_full": "• UNESCO (Ethics of AI - Harm Prevention): Nêu được những hành vi không nên làm khi sử dụng công cụ hoặc thiết bị AI, như dùng loa thông minh/robot để phát âm thanh quá to làm phiền, hoặc dùng AI để trêu chọc, làm bạn buồn.\n• Singapore MOE (Cyber Wellness - Respect): Có ý thức tôn trọng người khác, không biến thiết bị công nghệ thành công cụ gây khó chịu hay làm tổn thương người xung quanh.",
        "intl_compact": "Nêu được một số việc không nên làm khi dùng AI: không dùng loa thông minh/robot phát âm thanh quá to làm phiền, không dùng công cụ AI để trêu chọc hay làm người khác buồn."
    },
    {
        "stt": 10, "code": "1.B3.1",
        "strand": "B. Đạo đức AI",
        "subtopic": "Nguyên tắc đạo đức và trách nhiệm xã hội – Máy thông minh làm việc tốt",
        "yccd_vn": "Biết và nhắc lại được quy tắc: Không được dùng máy móc thông minh để làm hại hoặc làm đau người khác.",
        "intl_full": "• UNESCO (Ethics of AI - 'Do No Harm'): Nhận biết và nhắc lại được quy tắc đạo đức nền tảng: Tuyệt đối không sử dụng máy móc thông minh hay công cụ AI để làm hại, làm đau hoặc đe dọa người khác.\n• OECD (Responsible Citizenship): Bước đầu hình thành ý thức trách nhiệm đạo đức khi tiếp xúc với công nghệ.",
        "intl_compact": "Nhận biết và ghi nhớ quy tắc đạo đức cơ bản: Tuyệt đối không được sử dụng máy móc thông minh hay công nghệ AI để làm hại, làm đau hoặc gây tổn thương cho người khác."
    },
    {
        "stt": 11, "code": "1.B3.2",
        "strand": "B. Đạo đức AI",
        "subtopic": "Nguyên tắc đạo đức và trách nhiệm xã hội – Máy thông minh làm việc tốt",
        "yccd_vn": "Nêu được việc làm tốt đẹp mà con người sử dụng máy thông minh để thực hiện (như gọi giúp đỡ khi khẩn cấp, học nghe phát âm tiếng Anh).",
        "intl_full": "• Singapore MOE (AI for Good): Khuyến khích sử dụng AI phục vụ mục đích xây dựng: học tập tri thức và hỗ trợ gia đình.\n• OECD (Prosocial Behavior): Hành vi số mang lại giá trị tích cực cho cộng đồng.",
        "intl_compact": "Sử dụng AI phục vụ mục đích xây dựng: học tập tri thức cá nhân và hỗ trợ người thân trong gia đình. Hình thành hành vi số mang lại giá trị tích cực cho cộng đồng."
    },
    {
        "stt": 12, "code": "1.C1.1",
        "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "Đặc điểm chính của AI – Nhận biết AI và ứng dụng AI",
        "yccd_vn": "Chỉ ra được sự khác biệt đơn giản giữa quạt máy thông thường (bật nút là quay) và quạt thông minh (tự quay khi có người đến gần).",
        "intl_full": "• AI4K12 (Big Idea 1 - Sensing vs Simple Machines): Nhận biết sự khác biệt đơn giản qua ví dụ thực tế: quạt thông thường cần người trực tiếp thao tác bấm nút, còn thiết bị thông minh có khả năng nhận biết người ở gần để hoạt động.\n• Singapore MOE (Primary Computing): Làm quen với cách thiết bị thông minh tiếp nhận tín hiệu từ môi trường xung quanh (Input → Process → Output).",
        "intl_compact": "Chỉ ra sự khác biệt đơn giản qua ví dụ cụ thể: đồ dùng thông thường cần bấm nút cơ học để chạy, còn thiết bị thông minh có thể nhận biết người ở gần để tự hoạt động."
    },
    {
        "stt": 13, "code": "1.C1.2",
        "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "Đặc điểm chính của AI – Nhận biết AI và ứng dụng AI",
        "yccd_vn": "Nhận biết được hình ảnh biểu tượng trợ lí giọng nói (micro) hoặc ô vuông nhận diện khuôn mặt trên màn hình điện thoại do cô giáo chỉ.",
        "intl_full": "• Singapore MOE (Baseline Digital Literacy): Nhận diện biểu tượng giao diện của các tính năng AI quen thuộc trên màn hình (như biểu tượng micro của trợ lý giọng nói, ô vuông nhận diện khuôn mặt khi chụp ảnh).\n• AI4K12 (Big Idea 1 - Visual Interface): Làm quen với dấu hiệu giao diện trực quan cho thấy tính năng AI đang hoạt động.",
        "intl_compact": "Nhận diện được biểu tượng giao diện của một số tính năng AI quen thuộc trên thiết bị (biểu tượng micro của trợ lý giọng nói, khung vuông nhận diện khuôn mặt trên màn hình)."
    },
    {
        "stt": 14, "code": "1.C1.3",
        "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "Đặc điểm chính của AI – Chức năng và công cụ AI",
        "yccd_vn": "Nhận biết được camera giống như 'mắt nhìn' và micro giống như 'tai nghe' của thiết bị thông minh.",
        "intl_full": "• AI4K12 (Big Idea 1 - Perception): Hiểu camera và micro là các bộ phận tiếp nhận hình ảnh ('mắt nhìn') và âm thanh ('tai nghe') của máy tính thông minh.\n• OECD (Tech Literacy): Làm quen với sự tương đồng trực quan giữa các giác quan con người và thiết bị thu nhận của máy.",
        "intl_compact": "Nhận biết camera giống như 'mắt nhìn' giúp máy nhận hình ảnh, và micro giống như 'tai nghe' giúp máy nghe âm thanh, tương tự các giác quan của con người."
    },
    {
        "stt": 15, "code": "1.C1.4",
        "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "Đặc điểm chính của AI – Chức năng và công cụ AI",
        "yccd_vn": "Nêu được rằng máy thông minh có thể hiểu được một số câu nói ngắn, rõ ràng của con người và trả lời lại theo cách con người đã dạy.",
        "intl_full": "• AI4K12 (Big Idea 4 - Natural Interaction / NLP Intro): Nhận biết máy thông minh có thể hiểu được một số câu nói ngắn, rõ ràng và phản hồi lại theo cách con người đã thiết kế.\n• Singapore MOE (Primary Communication): Thực hành nói câu ngắn, phát âm rõ ràng khi tương tác với trợ lý giọng nói.",
        "intl_compact": "Nhận biết máy thông minh có thể tiếp nhận câu nói ngắn, rõ ràng và trả lời lại theo cách con người đã dạy; tập nói câu ngắn gọn, rõ lời khi tương tác với thiết bị."
    },
    {
        "stt": 16, "code": "1.C1.MR1",
        "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "Đặc điểm chính của AI – Chức năng và công cụ AI",
        "yccd_vn": "Quan sát và nhận biết được hình ảnh camera của máy đóng khung xung quanh quả táo hoặc chú mèo trên màn hình.",
        "intl_full": "• AI4K12 (Big Idea 1 - Computer Vision / Object Detection): Quan sát khung viền hiển thị bao quanh đồ vật (như quả táo, chú mèo) trên màn hình khi camera AI nhận diện đối tượng.\n• UNESCO (Techniques & Applications): Làm quen với hiện tượng máy nhận ra và đóng khung đánh dấu đồ vật trong hình ảnh.",
        "intl_compact": "Quan sát và nhận biết được khung viền/ô vuông xuất hiện bao quanh đồ vật hoặc con vật (như quả táo, con mèo) khi camera của máy nhận diện được đối tượng."
    },
    {
        "stt": 17, "code": "1.C1.MR2",
        "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "Đặc điểm chính của AI – Chức năng và công cụ AI",
        "yccd_vn": "Quan sát được máy thông minh phản ứng khác nhau khi nghe tiếng vỗ tay so với khi nghe tiếng nói của con người.",
        "intl_full": "• Singapore MOE (Code For Fun - Audio Processing): Khám phá các sự kiện kích hoạt từ âm thanh khác nhau.\n• AI4K12 (Big Idea 1 - Audio Classification): Nhận biết khả năng phân biệt âm thanh của máy: phân biệt giữa tiếng động cơ học (tiếng vỗ tay) và giọng nói con người.",
        "intl_compact": "Quan sát và nhận biết máy thông minh có thể phản ứng khác nhau trước các âm thanh khác nhau (phân biệt giữa tiếng vỗ tay và tiếng người nói)."
    },
    {
        "stt": 18, "code": "1.D1.1",
        "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "Nhận diện và hình thành giải pháp – Máy thông minh học từ ví dụ",
        "yccd_vn": "Nêu được ví dụ về việc con người cho máy xem nhiều bức tranh con mèo để máy biết nhận ra con mèo.",
        "intl_full": "• AI4K12 & Google DeepMind (Experience AI - Big Idea 3: Learning from Examples): Nhận biết qua ví dụ trực quan rằng con người cho máy xem nhiều tranh mẫu (như nhiều bức tranh con mèo) để máy học cách nhận ra đối tượng đó.\n• OECD (Foundational Data Awareness): Làm quen với ý niệm máy tính cần được con người cung cấp nhiều hình ảnh ví dụ để học tập.",
        "intl_compact": "Nêu được ví dụ đơn giản về việc con người cho máy xem nhiều hình ảnh mẫu (như tranh các chú mèo) để máy học cách nhận biết đối tượng."
    },
    {
        "stt": 19, "code": "1.D1.MR1",
        "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "Nhận diện và hình thành giải pháp – Máy thông minh học từ ví dụ",
        "yccd_vn": "Giải thích được rằng nếu chỉ đưa 1 bức tranh thì máy dễ đoán sai; máy cần xem nhiều bức tranh khác nhau để học đúng.",
        "intl_full": "• AI4K12 & Google DeepMind (Experience AI - Big Idea 3): Nhận biết rằng nếu chỉ xem 1 bức tranh thì máy dễ đoán sai; máy cần được con người cho xem nhiều ví dụ đúng và khác nhau để nhận biết tốt hơn.\n• UNESCO (Data Sufficiency): Làm quen với yêu cầu máy cần nhiều ví dụ phong phú để học chính xác (tiền đề cho chất lượng dữ liệu ở các lớp sau).",
        "intl_compact": "Giải thích được rằng máy cần xem nhiều ví dụ đúng và khác nhau để học nhận biết tốt hơn; nếu chỉ cho máy xem 1 bức tranh thì máy sẽ dễ nhận nhầm hoặc đoán sai."
    },
    {
        "stt": 20, "code": "1.D2.1",
        "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "Cấu trúc và tương tác, cải tiến hệ thống – Nhiều loại máy thông minh",
        "yccd_vn": "Nhận biết được có đồ dùng chỉ làm được một việc riêng (như cân điện tử), có đồ dùng làm được nhiều việc (như điện thoại vừa nghe, vừa chụp ảnh).",
        "intl_full": "• Singapore MOE (Systems Thinking - Device Functions): Phân biệt đồ dùng, thiết bị chuyên thực hiện một việc riêng (như cân điện tử) với thiết bị thực hiện được nhiều việc khác nhau (như điện thoại thông minh).\n• UNESCO (System Concepts): Nhận biết các thiết bị công nghệ xung quanh có phạm vi công dụng khác nhau.",
        "intl_compact": "Nhận biết được sự khác nhau giữa đồ dùng thông minh chỉ làm một việc riêng (như cân điện tử) và thiết bị làm được nhiều việc khác nhau (như điện thoại thông minh vừa nghe gọi, vừa chụp ảnh)."
    },
    {
        "stt": 21, "code": "1.D2.2",
        "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "Cấu trúc và tương tác, cải tiến hệ thống – Nhiều loại máy thông minh",
        "yccd_vn": "Xếp được các thẻ tranh đồ dùng thông minh vào 2 nhóm: nhóm chỉ làm 1 việc và nhóm làm được nhiều việc khác nhau.",
        "intl_full": "• Singapore MOE (Computational Thinking - Sorting & Classification): Thực hành xếp thẻ tranh đồ dùng thông minh vào 2 nhóm: nhóm làm một việc và nhóm làm nhiều việc.\n• OECD (Hands-on Practice): Rèn luyện tư duy phân loại đồ vật theo công dụng thực tế và nói được lý do phân loại đơn giản.",
        "intl_compact": "Thực hành xếp các thẻ tranh đồ dùng thông minh vào đúng 2 nhóm: nhóm chỉ làm một việc và nhóm làm nhiều việc khác nhau, nêu được lý do sắp xếp đơn giản."
    }
]

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def generate_markdown_day_du(output_path):
    lines = [
        "# KHUNG CHƯƠNG TRÌNH GIÁO DỤC TRÍ TUỆ NHÂN TẠO – LỚP 1 (BẢN ĐẦY ĐỦ)",
        "",
        "> **Căn cứ pháp lý:** Quyết định số 2422/QĐ-BGDĐT ngày 18/8/2026 của Bộ Giáo dục và Đào tạo.  ",
        "> **Căn cứ tham chiếu quốc tế:** UNESCO AI Competency Framework, OECD Learning Compass 2030, Singapore MOE, AI4K12 (Hoa Kỳ).",
        "",
        "---",
        "",
        "| STT | Mã YCCĐ | Mạch nội dung & Chủ đề con (QĐ 2422) | Yêu cầu cần đạt Chuẩn Quốc gia (Bộ GD&ĐT - QĐ 2422) | Chuẩn đầu ra tham chiếu Đa nguồn Quốc tế (UNESCO, OECD, Singapore MOE, AI4K12) |",
        "| :---: | :---: | :--- | :--- | :--- |"
    ]
    for it in data_lop1:
        intl_fmt = it["intl_full"].replace("\n", "<br>")
        row = f"| **{it['stt']}** | **{it['code']}** | **{it['strand']}**<br>• *{it['subtopic']}* | {it['yccd_vn']} | {intl_fmt} |"
        lines.append(row)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Exported MD full: {output_path}")

def generate_docx_day_du(output_path):
    doc = docx.Document()
    # Landscape orientation for 5-column table
    for section in doc.sections:
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width = Inches(11.69) # A4 landscape
        section.page_height = Inches(8.27)
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.6)
        section.right_margin = Inches(0.6)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("BẢNG ĐỐI SÁNH CHUẨN ĐẦU RA AI LỚP 1 (QĐ 2422/QĐ-BGDĐT – ĐA NGUỒN QUỐC TẾ)")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(14)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 32, 96)
    p_title.paragraph_format.space_after = Pt(2)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Bản đầy đủ: Đối sánh nguyên văn chuẩn Bộ GD&ĐT và Chuẩn đầu ra tham chiếu Quốc tế (UNESCO, OECD, Singapore MOE, AI4K12)")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(10)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(80, 80, 80)
    p_sub.paragraph_format.space_after = Pt(10)

    # Table 5 columns
    headers = [
        ("STT", Inches(0.6)),
        ("Mã YCCĐ", Inches(0.9)),
        ("Mạch nội dung & Chủ đề con", Inches(2.3)),
        ("Yêu cầu cần đạt Chuẩn Quốc gia\n(Bộ GD&ĐT - QĐ 2422)", Inches(3.3)),
        ("Chuẩn đầu ra tham chiếu Đa nguồn Quốc tế\n(UNESCO, OECD, Singapore MOE, AI4K12)", Inches(3.4))
    ]
    
    table = doc.add_table(rows=len(data_lop1) + 1, cols=5)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)

    # Header row
    hdr_cells = table.rows[0].cells
    for idx, (h_text, w) in enumerate(headers):
        hdr_cells[idx].width = w
        set_cell_margins(hdr_cells[idx], top=120, bottom=120, left=100, right=100)
        set_cell_shading(hdr_cells[idx], "1B365D")
        p = hdr_cells[idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h_text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    # Make header repeat on every page
    header_tr = table.rows[0]._tr.get_or_add_trPr()
    header_tr.append(OxmlElement('w:tblHeader'))

    for row_idx, it in enumerate(data_lop1, start=1):
        row_cells = table.rows[row_idx].cells
        bg_color = "F7F9FC" if row_idx % 2 == 0 else "FFFFFF"

        for idx, (_, w) in enumerate(headers):
            row_cells[idx].width = w
            set_cell_margins(row_cells[idx], top=80, bottom=80, left=90, right=90)
            set_cell_shading(row_cells[idx], bg_color)

        # STT
        p0 = row_cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(str(it["stt"]))
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(9.5)
        r0.font.bold = True

        # Mã
        p1 = row_cells[1].paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r1 = p1.add_run(it["code"])
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(9.5)
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(0, 32, 96)

        # Mạch & Chủ đề con
        p2 = row_cells[2].paragraphs[0]
        p2.paragraph_format.line_spacing = 1.15
        p2.paragraph_format.space_after = Pt(2)
        r2_a = p2.add_run(it["strand"] + "\n")
        r2_a.font.name = "Times New Roman"
        r2_a.font.size = Pt(9)
        r2_a.font.bold = True
        r2_b = p2.add_run("• " + it["subtopic"])
        r2_b.font.name = "Times New Roman"
        r2_b.font.size = Pt(8.5)
        r2_b.font.italic = True
        r2_b.font.color.rgb = RGBColor(60, 60, 60)

        # YCCĐ VN
        p3 = row_cells[3].paragraphs[0]
        p3.paragraph_format.line_spacing = 1.15
        r3 = p3.add_run(it["yccd_vn"])
        r3.font.name = "Times New Roman"
        r3.font.size = Pt(9)

        # Chuẩn đầu ra Quốc tế
        p4 = row_cells[4].paragraphs[0]
        p4.paragraph_format.line_spacing = 1.15
        lines_intl = it["intl_full"].split("\n")
        for l_idx, line_txt in enumerate(lines_intl):
            if l_idx > 0:
                p4 = row_cells[4].add_paragraph()
                p4.paragraph_format.line_spacing = 1.15
                p4.paragraph_format.space_after = Pt(2)
            # format bullets
            parts = line_txt.split(":", 1)
            if len(parts) == 2:
                r_bold = p4.add_run(parts[0] + ":")
                r_bold.font.name = "Times New Roman"
                r_bold.font.size = Pt(8.5)
                r_bold.font.bold = True
                r_bold.font.color.rgb = RGBColor(0, 51, 102)
                r_norm = p4.add_run(parts[1])
                r_norm.font.name = "Times New Roman"
                r_norm.font.size = Pt(8.5)
            else:
                r_all = p4.add_run(line_txt)
                r_all.font.name = "Times New Roman"
                r_all.font.size = Pt(8.5)

    doc.save(output_path)
    print(f"Exported DOCX full: {output_path}")

def generate_docx_rut_gon(output_path):
    doc = docx.Document()
    # Portrait orientation for 4-column table
    for section in doc.sections:
        section.orientation = WD_ORIENT.PORTRAIT
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.7)
        section.right_margin = Inches(0.7)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("KHUNG NỘI DUNG GIÁO DỤC TRÍ TUỆ NHÂN TẠO – LỚP 1")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(14)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 32, 96)
    p_title.paragraph_format.space_after = Pt(2)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("(Bản rút gọn chuẩn hóa: Mạch năng lực, Chủ đề con và Yêu cầu cần đạt đầu ra)")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(10)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(80, 80, 80)
    p_sub.paragraph_format.space_after = Pt(12)

    # Table 4 columns
    headers = [
        ("STT", Inches(0.6)),
        ("Mạch năng lực", Inches(1.8)),
        ("Chủ đề con", Inches(2.0)),
        ("YCCĐ", Inches(2.5))
    ]
    
    table = doc.add_table(rows=len(data_lop1) + 1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)

    # Header row
    hdr_cells = table.rows[0].cells
    for idx, (h_text, w) in enumerate(headers):
        hdr_cells[idx].width = w
        set_cell_margins(hdr_cells[idx], top=120, bottom=120, left=100, right=100)
        set_cell_shading(hdr_cells[idx], "1B365D")
        p = hdr_cells[idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h_text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    header_tr = table.rows[0]._tr.get_or_add_trPr()
    header_tr.append(OxmlElement('w:tblHeader'))

    for row_idx, it in enumerate(data_lop1, start=1):
        row_cells = table.rows[row_idx].cells
        bg_color = "F7F9FC" if row_idx % 2 == 0 else "FFFFFF"

        for idx, (_, w) in enumerate(headers):
            row_cells[idx].width = w
            set_cell_margins(row_cells[idx], top=80, bottom=80, left=90, right=90)
            set_cell_shading(row_cells[idx], bg_color)

        # STT
        p0 = row_cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(str(it["stt"]))
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(9.5)
        r0.font.bold = True

        # Mạch năng lực
        p1 = row_cells[1].paragraphs[0]
        p1.paragraph_format.line_spacing = 1.15
        r1 = p1.add_run(it["strand"])
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(9.5)
        r1.font.bold = True

        # Chủ đề con
        p2 = row_cells[2].paragraphs[0]
        p2.paragraph_format.line_spacing = 1.15
        r2 = p2.add_run(it["subtopic"])
        r2.font.name = "Times New Roman"
        r2.font.size = Pt(9.5)

        # YCCĐ (Compact International Outcome text)
        p3 = row_cells[3].paragraphs[0]
        p3.paragraph_format.line_spacing = 1.15
        r3 = p3.add_run(it["intl_compact"])
        r3.font.name = "Times New Roman"
        r3.font.size = Pt(9.5)

    doc.save(output_path)
    print(f"Exported DOCX compact: {output_path}")

def generate_markdown_rut_gon(output_path):
    lines = [
        "# KHUNG NỘI DUNG GIÁO DỤC TRÍ TUỆ NHÂN TẠO – LỚP 1",
        "*(Bản rút gọn chuẩn hóa: Mạch năng lực, Chủ đề con và Yêu cầu cần đạt đầu ra)*",
        "",
        "> **Căn cứ pháp lý:** Quyết định số 2422/QĐ-BGDĐT của Bộ Giáo dục và Đào tạo.  ",
        "> **Đặc điểm:** Tinh gọn các chú giải nguồn, diễn đạt thành các Chuẩn đầu ra năng lực (Exit Competencies) liền mạch, súc tích, phục vụ trực tiếp việc xây dựng kế hoạch dạy học và giảng dạy thực tế.",
        "",
        "---",
        "",
        "| STT | Mạch năng lực | Chủ đề con | YCCĐ (Chuẩn đầu ra năng lực) |",
        "| :---: | :--- | :--- | :--- |"
    ]
    for it in data_lop1:
        row = f"| **{it['stt']}** | **{it['strand']}** | {it['subtopic']} | {it['intl_compact']} |"
        lines.append(row)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Exported MD compact: {output_path}")

if __name__ == "__main__":
    out_dir = r"c:\Users\USER\Desktop\AI-vibe-code\KhungNLĐTAI\03_San_Pham_Chinh_Thuc"
    
    md_day_du = os.path.join(out_dir, "SP1_Khung_YCCD_AI_Lop1_Day_Du.md")
    docx_day_du = os.path.join(out_dir, "SP1_Khung_YCCD_AI_Lop1_Day_Du.docx")
    md_rut_gon = os.path.join(out_dir, "SP1_Khung_YCCD_AI_Lop1_Rut_Gon.md")
    docx_rut_gon = os.path.join(out_dir, "SP1_Khung_YCCD_AI_Lop1_Rut_Gon.docx")
    
    generate_markdown_day_du(md_day_du)
    generate_docx_day_du(docx_day_du)
    generate_markdown_rut_gon(md_rut_gon)
    generate_docx_rut_gon(docx_rut_gon)
    print("SUCCESS: All 4 files for Lop 1 generated successfully!")
