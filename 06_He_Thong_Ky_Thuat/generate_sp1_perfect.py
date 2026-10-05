# -*- coding: utf-8 -*-
"""
Script tạo KHUNG CHƯƠNG TRÌNH HOÀN CHỈNH (SẢN PHẨM 1) - CỤM TIỂU HỌC KHỞI ĐẦU (LỚP 1 VÀ LỚP 2)
Đáp ứng 100% 6 yêu cầu sửa đổi của Hội đồng kiểm định:
- Cấu trúc đầy đủ 8 phần của một Khung chương trình chuẩn mực
- Bổ sung Hàng rào an toàn số, bảo vệ dữ liệu học sinh
- Phân định rõ 12 tiết cốt lõi và 24 tiết mở rộng
- Viết lại YCCĐ bằng ngôn ngữ vừa sức học sinh 6-8 tuổi (bỏ từ ngữ hàn lâm)
- Tách riêng: YCCĐ hành vi | Diễn giải sư phạm chuẩn xác | Minh chứng quan sát K-S-A
- Sửa đổi 8 điểm khoa học theo góp ý của Chuyên gia AI
"""
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

# Dữ liệu 50 YCCĐ đã được tinh chỉnh toàn diện theo chuẩn Hội đồng
items_l1 = [
    # Mạch A - Lớp 1
    {
        "stt": 1, "track": "Cốt lõi (12T)", "code": "1.A1.1", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A1. Tính chủ động của con người – Con người có cảm xúc, AI thì không",
        "yccd": "Nêu được ví dụ về các cảm xúc quen thuộc của bản thân (vui, buồn, tức giận, sợ hãi) và nhận ra rằng con người cảm thấy vui buồn thật sự, còn máy móc thì không.",
        "explanation": "Giúp trẻ phân biệt trạng thái cảm xúc tự nhiên của con người với các tín hiệu mô phỏng của máy; máy móc hoạt động dựa trên chương trình do con người tạo ra.",
        "evidence": "K (Hiểu): Chỉ ra bạn nhỏ có cảm xúc thật, robot đồ chơi không biết buồn/vui.<br>S (Kỹ năng): Chọn đúng thẻ mặt cười/mặt mếu cho người và biểu tượng máy tính.<br>A (Thái độ): Biết yêu thương, đồng cảm với bạn bè xung quanh."
    },
    {
        "stt": 2, "track": "Cốt lõi (12T)", "code": "1.A1.2", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A1. Tính chủ động của con người – Con người có cảm xúc, AI thì không",
        "yccd": "Nêu được rằng máy thông minh chỉ bắt chước hoặc nhận biết nét mặt của con người, chứ không có cảm xúc như con người.",
        "explanation": "Khắc phục quan niệm sai lầm rằng máy có cảm xúc thật. Máy nhận diện hình ảnh khuôn mặt qua camera dựa trên thuật toán, không phải do có trái tim hay tâm hồn.",
        "evidence": "K: Nêu được robot cười là do được thiết kế để bắt chước.<br>S: Nhìn tranh và nói câu: 'Robot chỉ bắt chước nụ cười của bạn nhỏ'.<br>A: Tỉnh táo, không coi máy móc là một con người thật."
    },
    {
        "stt": 3, "track": "Cốt lõi (12T)", "code": "1.A1.3", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A1. Tính chủ động của con người – AI thể hiện cảm xúc do con người lập trình",
        "yccd": "Nêu được rằng việc AI thể hiện cảm xúc (như hình mặt cười, giọng nói vui vẻ) là do con người tạo ra hoặc lập trình từ trước.",
        "explanation": "Đính chính khoa học: Cảm xúc của AI (dù qua kịch bản lập trình hay qua mô hình học máy sinh lời) đều bắt nguồn từ sự thiết kế, lựa chọn dữ liệu và huấn luyện của con người.",
        "evidence": "K: Nói được câu: 'Hình mặt cười trên màn hình là do các cô chú kỹ sư vẽ ra và cài vào máy'.<br>S: Ghép đúng thẻ 'Con người tạo ra' với hình robot đang cười.<br>A: Tôn trọng sản phẩm công nghệ do con người sáng tạo."
    },
    {
        "stt": 4, "track": "Cốt lõi (12T)", "code": "1.A1.4", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A1. Tính chủ động của con người – AI thể hiện cảm xúc do con người lập trình",
        "yccd": "Nêu được ví dụ khi máy phát ra câu chào hoặc cười theo mẫu do con người thiết kế (ví dụ: loa thông minh nói 'Chào bạn, tôi có thể giúp gì?').",
        "explanation": "Liên hệ thực tế: Máy móc phản hồi theo mô hình hoặc kịch bản đã được huấn luyện, giúp học sinh không thần thánh hóa câu trả lời của máy.",
        "evidence": "K: Kể lại một câu nói quen thuộc của thiết bị thông minh.<br>S: Đóng vai người dùng chào loa và giải thích vì sao loa biết chào lại.<br>A: Lịch sự khi sử dụng thiết bị nhưng giữ tính độc lập."
    },
    {
        "stt": 5, "track": "Cốt lõi (12T)", "code": "1.A2.1", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A2. AI vì sự tiến bộ của con người – Ý nghĩa cảm xúc mà AI thể hiện",
        "yccd": "Chỉ ra được các cách máy thông minh thể hiện cảm xúc (như nháy đèn, hiện mặt cười, đổi giọng nói nhẹ nhàng).",
        "explanation": "Giúp học sinh nhận biết các giao diện thân thiện (hình ảnh, âm thanh) mà người thiết kế tạo ra để giao tiếp với người dùng.",
        "evidence": "K: Gọi tên được 2 cách máy thể hiện (hình vẽ trên màn hình, giọng nói).<br>S: Vẽ hoặc chọn đúng biểu tượng mặt cười mà máy hay dùng.<br>A: Cảm thấy vui vẻ, thoải mái khi học với thiết bị học tập."
    },
    {
        "stt": 6, "track": "Mở rộng (24T)", "code": "1.A2.MR1", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A2. AI vì sự tiến bộ của con người – Ý nghĩa cảm xúc mà AI thể hiện",
        "yccd": "Nêu được rằng giọng nói thân thiện và hình ảnh dễ thương giúp con người cảm thấy gần gũi, dễ chịu khi nhờ máy giúp đỡ.",
        "explanation": "Giới thiệu khái niệm trải nghiệm người dùng ở mức sơ khai: Thiết kế thân thiện giúp con người và công nghệ hợp tác tốt hơn.",
        "evidence": "K: Trả lời câu hỏi: 'Vì sao loa thông minh lại nói giọng nhẹ nhàng?'.<br>S: So sánh cảm giác khi nghe loa nói giọng gắt gỏng và giọng vui vẻ.<br>A: Yêu thích cái đẹp và sự lịch sự trong giao tiếp."
    },
    {
        "stt": 7, "track": "Cốt lõi (12T)", "code": "1.A2.2", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A2. AI vì sự tiến bộ của con người – Nhận diện AI trong cuộc sống",
        "yccd": "Kể tên được một số đồ dùng thông minh quen thuộc có thể tự thực hiện việc đơn giản (như robot hút bụi, camera nhận mặt, loa nghe lệnh).",
        "explanation": "Nhận biết các ứng dụng AI gần gũi trong đời sống, phân biệt với các đồ điện gia dụng thông thường.",
        "evidence": "K: Kể tên được 2-3 đồ dùng thông minh trong nhà hoặc trường học.<br>S: Phân loại đúng tranh ảnh đồ dùng thông minh và đồ dùng cơ thông thường.<br>A: Hứng thú khám phá thế giới xung quanh."
    },
    {
        "stt": 8, "track": "Cốt lõi (12T)", "code": "1.A2.3", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A2. AI vì sự tiến bộ của con người – Nhận diện AI trong cuộc sống",
        "yccd": "Nói được việc làm có ích của từng đồ dùng thông minh (như robot hút bụi giúp quét nhà sạch sẽ, loa giúp mở nhạc theo lời nói).",
        "explanation": "Giúp học sinh hiểu máy móc được tạo ra với mục đích phục vụ và hỗ trợ con người giải quyết công việc hàng ngày.",
        "evidence": "K: Nêu được công dụng của robot hút bụi hoặc loa thông minh.<br>S: Nối đúng hình ảnh thiết bị với công việc mà thiết bị đó giúp con người.<br>A: Biết ơn sức lao động và sự tiến bộ của khoa học."
    },

    # Mạch B - Lớp 1
    {
        "stt": 9, "track": "Cốt lõi (12T)", "code": "1.B1.1", "strand": "B. Đạo đức AI",
        "subtopic": "B1. Các khía cạnh đạo đức của AI – Việc làm tốt và việc làm xấu",
        "yccd": "Nêu được một vài việc không nên làm khi dùng thiết bị thông minh (như bật tiếng quá to làm phiền mọi người, dùng máy trêu chọc bạn).",
        "explanation": "Giáo dục hành vi an toàn và đúng mực ban đầu, hình thành ý thức tôn trọng những người xung quanh khi tiếp xúc công nghệ.",
        "evidence": "K: Nhận ra hành vi trêu bạn bằng máy là không đúng.<br>S: Giơ thẻ ĐỎ cho hành vi xấu và thẻ XANH cho hành vi tốt trong tranh tình huống.<br>A: Có ý thức giữ trật tự và tôn trọng bạn bè."
    },
    {
        "stt": 10, "track": "Cốt lõi (12T)", "code": "1.B3.1", "strand": "B. Đạo đức AI",
        "subtopic": "B3. Nguyên tắc đạo đức và trách nhiệm xã hội – Máy thông minh làm việc tốt",
        "yccd": "Biết và nhắc lại được quy tắc: Không được dùng máy móc thông minh để làm hại hoặc làm đau người khác.",
        "explanation": "Nguyên tắc đạo đức bất biến: Công nghệ phải hướng thiện, bảo đảm an toàn thân thể và tinh thần cho con người.",
        "evidence": "K: Nhắc lại được nguyên tắc 'Máy móc để giúp đỡ, không để làm hại'.<br>S: Tự nhắc bạn khi thấy bạn có hành vi bấm nghịch làm hại đồ vật.<br>A: Tôn trọng sự an toàn và hòa đồng."
    },
    {
        "stt": 11, "track": "Cốt lõi (12T)", "code": "1.B3.2", "strand": "B. Đạo đức AI",
        "subtopic": "B3. Nguyên tắc đạo đức và trách nhiệm xã hội – Máy thông minh làm việc tốt",
        "yccd": "Nêu được việc làm tốt đẹp mà con người sử dụng máy thông minh để thực hiện (như gọi giúp đỡ khi khẩn cấp, học nghe phát âm tiếng Anh).",
        "explanation": "Khích lệ học sinh noi theo những tấm gương sử dụng công nghệ vì mục đích học tập và giúp đỡ cộng đồng.",
        "evidence": "K: Nêu được một ví dụ dùng máy làm việc có ích.<br>S: Đóng vai dùng loa thông minh để nhờ mở bài học thể dục buổi sáng.<br>A: Tinh thần chăm chỉ học tập và giúp đỡ gia đình."
    },

    # Mạch C - Lớp 1
    {
        "stt": 12, "track": "Cốt lõi (12T)", "code": "1.C1.1", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C1. Đặc điểm chính của AI – Nhận biết AI và ứng dụng AI",
        "yccd": "Chỉ ra được sự khác biệt đơn giản giữa quạt máy thông thường (bật nút là quay) và quạt thông minh (tự quay khi có người đến gần).",
        "explanation": "Khắc họa đặc điểm cơ bản của hệ thống thông minh: Có khả năng nhận biết môi trường xung quanh để tự điều chỉnh hành vi phù hợp.",
        "evidence": "K: Nói được điểm khác biệt: Quạt thông minh biết tự quay khi có người.<br>S: Chọn đúng tranh đồ dùng thông minh trong bộ thẻ bài trực quan.<br>A: Tò mò, hứng thú tìm hiểu khoa học."
    },
    {
        "stt": 13, "track": "Cốt lõi (12T)", "code": "1.C1.2", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C1. Đặc điểm chính của AI – Nhận biết AI và ứng dụng AI",
        "yccd": "Nhận biết được hình ảnh biểu tượng trợ lí giọng nói (micro) hoặc ô vuông nhận diện khuôn mặt trên màn hình điện thoại do cô giáo chỉ.",
        "explanation": "Làm quen với các dấu hiệu trực quan của tính năng AI quen thuộc trên thiết bị dưới sự hướng dẫn của giáo viên.",
        "evidence": "K: Chỉ đúng biểu tượng micro dùng để nói chuyện với máy.<br>S: Khoanh tròn đúng biểu tượng trên tranh vẽ màn hình điện thoại.<br>A: Tự tin khi nhận biết biểu tượng số."
    },
    {
        "stt": 14, "track": "Cốt lõi (12T)", "code": "1.C1.3", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C1. Đặc điểm chính của AI – Chức năng và công cụ AI",
        "yccd": "Nhận biết được camera giống như 'mắt nhìn' và micro giống như 'tai nghe' của thiết bị thông minh.",
        "explanation": "Ẩn dụ trực quan sư phạm: Cảm biến camera và micro là bộ phận thu nhận tín hiệu đầu vào từ môi trường để máy xử lý.",
        "evidence": "K: Nêu được: Camera để máy nhìn, micro để máy nghe.<br>S: Chỉ đúng vị trí camera và micro trên mô hình tranh vẽ máy tính bảng.<br>A: Hiểu cơ chế hoạt động của các bộ phận trên máy."
    },
    {
        "stt": 15, "track": "Cốt lõi (12T)", "code": "1.C1.4", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C1. Đặc điểm chính của AI – Chức năng và công cụ AI",
        "yccd": "Nêu được rằng máy thông minh có thể hiểu được một số câu nói ngắn, rõ ràng của con người và trả lời lại theo cách con người đã dạy.",
        "explanation": "Đính chính khoa học: AI có khả năng nhận dạng giọng nói và sinh phản hồi dựa trên mô hình ngôn ngữ đã được học, không chỉ là các câu lệnh cứng.",
        "evidence": "K: Nêu được máy chỉ hiểu khi ta nói to, rõ ràng và đúng câu lệnh.<br>S: Nói mẫu một câu lệnh đơn giản: 'Bật đèn phòng khách'.<br>A: Nói năng mạch lạc, rõ ràng khi giao tiếp."
    },
    {
        "stt": 16, "track": "Mở rộng (24T)", "code": "1.C1.MR1", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C1. Đặc điểm chính của AI – Chức năng và công cụ AI",
        "yccd": "Quan sát và nhận biết được hình ảnh camera của máy đóng khung xung quanh quả táo hoặc chú mèo trên màn hình.",
        "explanation": "Làm quen với khái niệm thị giác máy tính ở dạng trực quan: Máy nhận dạng và phân biệt hình bóng đồ vật.",
        "evidence": "K: Nêu được máy đang nhận ra đồ vật nào trong tranh.<br>S: Vẽ khung vuông bao quanh đồ vật trên phiếu bài tập mô phỏng camera.<br>A: Tập trung chú ý quan sát chi tiết."
    },
    {
        "stt": 17, "track": "Mở rộng (24T)", "code": "1.C1.MR2", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C1. Đặc điểm chính của AI – Chức năng và công cụ AI",
        "yccd": "Quan sát được máy thông minh phản ứng khác nhau khi nghe tiếng vỗ tay so với khi nghe tiếng nói của con người.",
        "explanation": "Nhận thức cơ bản về xử lý âm thanh: Máy thông minh có thể phân biệt được các dạng âm thanh khác nhau dựa trên mẫu học.",
        "evidence": "K: Nêu được máy nhận ra tiếng vỗ tay hay tiếng người nói.<br>S: Vỗ tay để thử xem chuông có reo theo hướng dẫn giáo viên.<br>A: Hào hứng tham gia hoạt động trải nghiệm."
    },

    # Mạch D - Lớp 1
    {
        "stt": 18, "track": "Cốt lõi (12T)", "code": "1.D1.1", "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "D1. Nhận diện và hình thành giải pháp – Máy thông minh học từ ví dụ",
        "yccd": "Nêu được ví dụ về việc con người cho máy xem nhiều bức tranh con mèo để máy biết nhận ra con mèo.",
        "explanation": "Bản chất máy học: AI không tự nhiên biết mọi thứ, mà cần con người cung cấp các ví dụ mẫu (tranh ảnh, âm thanh) để học hỏi.",
        "evidence": "K: Giải thích được máy biết con mèo là nhờ xem nhiều tranh mẫu.<br>S: Xếp 3 bức tranh con mèo vào hộp mẫu 'dạy máy học con mèo'.<br>A: Hiểu rằng muốn giỏi giang cần phải chăm chỉ học hỏi."
    },
    {
        "stt": 19, "track": "Mở rộng (24T)", "code": "1.D1.MR1", "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "D1. Nhận diện và hình thành giải pháp – Máy thông minh học từ ví dụ",
        "yccd": "Giải thích được rằng nếu chỉ đưa 1 bức tranh thì máy dễ đoán sai; máy cần xem nhiều bức tranh khác nhau để học đúng.",
        "explanation": "Nguyên lý đa dạng của dữ liệu: Mẫu học cần phong phú về màu sắc, góc chụp để hệ thống nhận diện chính xác hơn.",
        "evidence": "K: Nói được: 'Cần nhiều tranh con mèo màu vàng, màu trắng để máy không nhầm'.<br>S: Chọn thêm 2 bức ảnh mèo khác nhau để bổ sung cho bộ tranh học.<br>A: Cẩn thận, chu đáo khi làm việc."
    },
    {
        "stt": 20, "track": "Cốt lõi (12T)", "code": "1.D2.1", "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "D2. Cấu trúc và tương tác, cải tiến hệ thống – Nhiều loại máy thông minh",
        "yccd": "Nhận biết được có đồ dùng chỉ làm được một việc riêng (như cân điện tử), có đồ dùng làm được nhiều việc (như điện thoại vừa nghe, vừa chụp ảnh).",
        "explanation": "Đính chính khoa học: Phân loại theo phạm vi nhiệm vụ của thiết bị (chuyên trách hay đa năng), giúp học sinh hiểu sự đa dạng của công nghệ.",
        "evidence": "K: Nêu tên 1 máy làm một việc và 1 máy làm nhiều việc.<br>S: Nói được công việc của từng loại máy qua tranh vẽ.<br>A: Tôn trọng công năng của từng đồ vật."
    },
    {
        "stt": 21, "track": "Cốt lõi (12T)", "code": "1.D2.2", "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "D2. Cấu trúc và tương tác, cải tiến hệ thống – Nhiều loại máy thông minh",
        "yccd": "Xếp được các thẻ tranh đồ dùng thông minh vào 2 nhóm: nhóm chỉ làm 1 việc và nhóm làm được nhiều việc khác nhau.",
        "explanation": "Rèn luyện tư duy phân loại và logic học máy thông qua trò chơi sắp xếp thẻ tranh không dùng máy tính (Unplugged).",
        "evidence": "K: Giải thích được vì sao xếp thẻ tranh vào nhóm đó.<br>S: Thao tác xếp đúng ít nhất 4 thẻ tranh vào 2 rổ tương ứng.<br>A: Hợp tác tốt với bạn khi chơi nhóm."
    }
]

# Dữ liệu Lớp 2 (29 YCCĐ)
items_l2 = [
    # Mạch A - Lớp 2
    {
        "stt": 22, "track": "Cốt lõi (12T)", "code": "2.A1.1", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A1. Tính chủ động của con người – Khi nào nên và không nên dùng AI",
        "yccd": "Nêu được một số việc máy thông minh giúp con người làm nhanh hơn (như tìm đường đi, tìm một bài hát yêu thích, dịch một câu chào tiếng nước ngoài).",
        "explanation": "Nhận biết tính hữu ích của công cụ AI trong đời sống thực tế, giúp tiết kiệm thời gian và công sức cho con người.",
        "evidence": "K: Kể được 2 tình huống máy giúp đỡ người lớn hoặc học sinh.<br>S: Chọn đúng công cụ máy móc phù hợp với việc cần làm trong tranh.<br>A: Tích cực, chủ động tìm kiếm sự trợ giúp đúng lúc."
    },
    {
        "stt": 23, "track": "Cốt lõi (12T)", "code": "2.A1.2", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A1. Tính chủ động của con người – Khi nào nên và không nên dùng AI",
        "yccd": "Nêu được tình huống không nên dùng máy thông minh (như không nói địa chỉ nhà, tên bố mẹ cho máy; không để máy làm hết bài tập về nhà của mình).",
        "explanation": "Rèn luyện ý thức bảo vệ thông tin cá nhân cơ bản và chống ỷ lại vào công nghệ, giữ gìn thói quen tự suy nghĩ.",
        "evidence": "K: Nêu được lý do không chia sẻ bí mật gia đình cho máy.<br>S: Nói 'KHÔNG' khi bạn rủ nhờ máy làm hộ bài tập viết chữ.<br>A: Trung thực và tự giác trong học tập."
    },
    {
        "stt": 24, "track": "Cốt lõi (12T)", "code": "2.A1.3", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A1. Tính chủ động của con người – AI làm việc, con người kiểm soát",
        "yccd": "Nêu được ví dụ con người luôn cần để mắt kiểm tra máy khi máy làm việc (như người lái xe vẫn phải nhìn đường khi xe tự chạy, bác sĩ kiểm tra lại lời máy gợi ý).",
        "explanation": "Nguyên lý con người làm chủ: AI chỉ là công cụ hỗ trợ, con người phải luôn theo dõi, giám sát và chịu trách nhiệm về kết quả cuối cùng.",
        "evidence": "K: Giải thích vì sao người lái xe không được ngủ gật khi bật xe tự lái.<br>S: Đóng vai người kiểm tra, chấm lại đáp án máy đưa ra.<br>A: Tinh thần trách nhiệm và cẩn thận."
    },
    {
        "stt": 25, "track": "Cốt lõi (12T)", "code": "2.A1.4", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A1. Tính chủ động của con người – AI làm việc, con người kiểm soát",
        "yccd": "Thể hiện được thái độ đúng đắn: Biết dùng máy để học hỏi nhưng luôn tự suy nghĩ và kiểm tra lại chứ không tin tưởng hoàn toàn vào máy.",
        "explanation": "Xây dựng thái độ tự chủ, tỉnh táo trước công nghệ; hiểu rằng máy móc có thể nhầm lẫn nên cần sự kiểm tra của con người.",
        "evidence": "K: Trả lời được câu hỏi: 'Nếu máy trả lời một điều rất lạ, em sẽ làm gì?'.<br>S: Biết hỏi lại cô giáo hoặc cha mẹ khi thấy kết quả của máy chưa đúng.<br>A: Tự tin vào khả năng suy nghĩ của chính mình."
    },
    {
        "stt": 26, "track": "Cốt lõi (12T)", "code": "2.A2.1", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A2. AI vì sự tiến bộ của con người – AI trong gia đình",
        "yccd": "Kể tên được một số thiết bị thông minh dùng trong gia đình (như robot quét nhà, điều hòa tự chỉnh nhiệt độ, tivi gợi ý phim hoạt hình em thích).",
        "explanation": "Nhận biết các điểm ứng dụng công nghệ trong không gian gia đình, liên kết bài học với môi trường sống hàng ngày.",
        "evidence": "K: Kể tên được 2 đồ dùng thông minh có trong gia đình hoặc nhà người quen.<br>S: Nối đúng đồ dùng với phòng chức năng trong ngôi nhà trên tranh vẽ.<br>A: Ý thức giữ gìn và bảo quản đồ dùng gia đình."
    },
    {
        "stt": 27, "track": "Mở rộng (24T)", "code": "2.A2.MR1", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A2. AI vì sự tiến bộ của con người – AI trong gia đình",
        "yccd": "Thực hành thử nói một câu lệnh nhờ máy giúp dưới sự cho phép và quan sát của thầy cô giáo.",
        "explanation": "Trải nghiệm thực hành an toàn có kiểm soát: Học sinh làm quen với thao tác ra lệnh mẫu trong môi trường học đường an toàn.",
        "evidence": "K: Biết các bước xin phép trước khi chạm vào máy.<br>S: Nói to, rõ câu lệnh: 'Xin mở bài hát thiếu nhi' dưới sự hướng dẫn của cô.<br>A: Lễ phép, tuân thủ hướng dẫn của giáo viên."
    },
    {
        "stt": 28, "track": "Mở rộng (24T)", "code": "2.A2.MR2", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A2. AI vì sự tiến bộ của con người – AI trong gia đình",
        "yccd": "Nhắc lại và làm theo quy tắc: Chỉ sử dụng đồ dùng thông minh khi có sự đồng ý và trông chừng của người lớn.",
        "explanation": "Quy tắc an toàn số sống còn cho lứa tuổi 7 tuổi: Tránh việc trẻ tự ý tiếp xúc với thiết bị kết nối mạng mà không có người bảo trợ.",
        "evidence": "K: Nhắc lại được: 'Em luôn hỏi xin phép bố mẹ trước khi dùng máy tính/điện thoại'.<br>S: Thể hiện hành động xin phép bố mẹ trong tình huống đóng vai.<br>A: Vâng lời người lớn, có ý thức tự bảo vệ bản thân."
    },
    {
        "stt": 29, "track": "Cốt lõi (12T)", "code": "2.A2.2", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A2. AI vì sự tiến bộ của con người – AI hỗ trợ mọi người",
        "yccd": "Kể được các thành viên trong nhà mà máy thông minh có thể giúp đỡ (như nhắc bà uống thuốc, giúp mẹ lau sàn nhà, giúp bố hẹn giờ làm việc).",
        "explanation": "Gắn kết công nghệ với tình cảm gia đình, giáo dục học sinh thấy được giá trị của việc công nghệ phục vụ con người.",
        "evidence": "K: Nêu được công việc máy giúp cho từng người trong nhà.<br>S: Ghép đúng thẻ thiết bị với thành viên gia đình được hỗ trợ.<br>A: Yêu thương, quan tâm chăm sóc ông bà, cha mẹ."
    },
    {
        "stt": 30, "track": "Mở rộng (24T)", "code": "2.A2.MR3", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A2. AI vì sự tiến bộ của con người – AI hỗ trợ mọi người",
        "yccd": "Nêu được rằng khi máy giúp làm bớt việc nhà, cả nhà sẽ có nhiều thời gian vui chơi, trò chuyện cùng nhau hơn.",
        "explanation": "Ý nghĩa nhân văn cốt lõi: Mục tiêu của công nghệ là giải phóng sức lao động để con người sống hạnh phúc, gắn kết bên nhau hơn.",
        "evidence": "K: Nêu được lợi ích: Nhà có nhiều thời gian cùng nhau ăn cơm, đọc sách.<br>S: Vẽ bức tranh gia đình sum vầy khi việc nhà đã được dọn sạch.<br>A: Trân trọng thời gian ở bên gia đình."
    },
    {
        "stt": 31, "track": "Cốt lõi (12T)", "code": "2.A3.1", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A3. Công dân trong kỉ nguyên AI – Con người dạy AI qua tương tác",
        "yccd": "Nhận biết được rằng những câu hỏi, lựa chọn của con người có thể được hệ thống lưu lại để làm ví dụ giúp máy học và cải tiến cách trả lời.",
        "explanation": "Đính chính khoa học: Không phải mọi tương tác đều khiến máy 'học suy nghĩ', mà dữ liệu tương tác được lưu lại để nhà sản xuất tinh chỉnh mô hình máy học.",
        "evidence": "K: Hiểu rằng khi ta chọn xem nhiều video hoạt hình, máy sẽ gợi ý thêm phim hoạt hình.<br>S: Chỉ ra trên tranh tình huống: Lựa chọn của bạn nhỏ được máy ghi nhận.<br>A: Thận trọng với những gì mình tìm kiếm trên mạng."
    },
    {
        "stt": 32, "track": "Mở rộng (24T)", "code": "2.A3.MR1", "strand": "A. Tư duy lấy con người làm trung tâm",
        "subtopic": "A3. Công dân trong kỉ nguyên AI – Con người dạy AI qua tương tác",
        "yccd": "Nêu được rằng khi con người dùng lời nói lịch sự, đúng đắn thì sẽ cung cấp những ví dụ tốt cho máy; nếu nói lời thô tục hoặc thông tin sai thì máy có thể bị dạy sai.",
        "explanation": "Đính chính khoa học: Nhấn mạnh trách nhiệm của người sử dụng trong việc giữ gìn môi trường dữ liệu trong sạch, văn minh.",
        "evidence": "K: Nêu được vì sao cần nói năng lịch sự khi tương tác với thiết bị số.<br>S: Chọn câu nói lịch sự, văn minh để làm ví dụ tốt cho máy học.<br>A: Lịch thiệp, giữ gìn sự trong sáng của lời nói."
    },

    # Mạch B - Lớp 2
    {
        "stt": 33, "track": "Cốt lõi (12T)", "code": "2.B1.1", "strand": "B. Đạo đức AI",
        "subtopic": "B1. Các khía cạnh đạo đức của AI – Sự đối xử không công bằng",
        "yccd": "Nhận biết được rằng máy thông minh đôi khi có thể phân biệt hoặc đối xử không công bằng giữa những người khác nhau.",
        "explanation": "Làm quen với khái niệm thiên lệch thuật toán ở mức trực quan đơn giản: Máy móc có thể thiên vị nếu không được dạy cẩn thận.",
        "evidence": "K: Nêu được ví dụ máy chỉ nghe được giọng người lớn mà không nghe được giọng trẻ con.<br>S: Chỉ ra điểm chưa công bằng trong tình huống truyện kể.<br>A: Mong muốn mọi người đều được đối xử bình đẳng."
    },
    {
        "stt": 34, "track": "Mở rộng (24T)", "code": "2.B1.MR1", "strand": "B. Đạo đức AI",
        "subtopic": "B1. Các khía cạnh đạo đức của AI – Sự đối xử không công bằng",
        "yccd": "Kể lại một tình huống máy nhận diện không công bằng (như máy nhận diện giọng nói chỉ hiểu giọng bạn miền Bắc mà không hiểu bạn miền Trung hay miền Nam).",
        "explanation": "Minh họa cụ thể thiên lệch trong thực tế lứa tuổi học đường, giúp học sinh thấu hiểu qua câu chuyện gần gũi.",
        "evidence": "K: Kể lại đúng chi tiết câu chuyện về bạn nhỏ bị máy nghe nhầm giọng nói.<br>S: Diễn tả lại phản ứng của bạn nhỏ và đề xuất cách giúp bạn.<br>A: Tôn trọng sự đa dạng ngôn ngữ và văn hóa vùng miền."
    },
    {
        "stt": 35, "track": "Mở rộng (24T)", "code": "2.B1.MR2", "strand": "B. Đạo đức AI",
        "subtopic": "B1. Các khía cạnh đạo đức của AI – Sự đối xử không công bằng",
        "yccd": "Giải thích được rằng nếu lúc dạy máy, con người chỉ đưa ví dụ của một nhóm người thì máy sẽ không nhận biết tốt những người khác.",
        "explanation": "Nguyên nhân của thiên lệch: Dữ liệu huấn luyện bị thiếu hụt, không đồng đều sẽ dẫn đến việc mô hình thiên vị một phía.",
        "evidence": "K: Giải thích được: 'Vì chỉ cho máy nghe giọng người lớn nên máy chưa quen giọng trẻ em'.<br>S: Đề xuất bổ sung thêm giọng trẻ con vào bài học cho máy.<br>A: Công bằng và bao dung trong suy nghĩ."
    },
    {
        "stt": 36, "track": "Cốt lõi (12T)", "code": "2.B3.1", "strand": "B. Đạo đức AI",
        "subtopic": "B3. Nguyên tắc đạo đức và trách nhiệm xã hội – Của bạn và của tớ",
        "yccd": "Phân biệt được đồ dùng, tranh vẽ của riêng em với đồ dùng, tranh vẽ của bạn khác trong lớp học.",
        "explanation": "Xác lập ranh giới quyền sở hữu đồ vật và tác phẩm cá nhân trong thực tế đời sống hàng ngày của trẻ lên 7.",
        "evidence": "K: Chỉ đúng hộp bút, quyển vở là của mình; đồ của bạn là của bạn.<br>S: Tự sắp xếp đồ dùng của mình gọn gàng, không cầm nhầm đồ của bạn.<br>A: Tôn trọng tài sản cá nhân của người khác."
    },
    {
        "stt": 37, "track": "Cốt lõi (12T)", "code": "2.B3.2", "strand": "B. Đạo đức AI",
        "subtopic": "B3. Nguyên tắc đạo đức và trách nhiệm xã hội – Của bạn và của tớ",
        "yccd": "Nêu được ví dụ về việc bức tranh do em tự vẽ là của em, còn bức tranh do máy tạo ra thì phải ghi rõ là máy tạo ra, không nhận là do mình tự vẽ.",
        "explanation": "Bước đầu hình thành liêm chính học thuật và bản quyền sơ khai: Tôn trọng công sức thật sự, không gian dối nhận vơ sản phẩm của AI.",
        "evidence": "K: Hiểu rằng tranh do máy vẽ không phải là do em tự cầm bút vẽ.<br>S: Ghi dòng chữ nhỏ 'Tranh do máy vẽ' dưới bức ảnh in từ máy tính.<br>A: Trung thực, thẳng thắn trong học tập."
    },
    {
        "stt": 38, "track": "Mở rộng (24T)", "code": "2.B3.MR1", "strand": "B. Đạo đức AI",
        "subtopic": "B3. Nguyên tắc đạo đức và trách nhiệm xã hội – Của bạn và của tớ",
        "yccd": "Phân biệt được trong tình huống cụ thể đồ vật nào được phép dùng và đồ vật nào phải hỏi trước khi chạm vào.",
        "explanation": "Kỹ năng xử lý tình huống sở hữu trên thực tế trường lớp, tạo nền tảng cho việc tôn trọng quyền riêng tư dữ liệu sau này.",
        "evidence": "K: Xác định được đồ dùng chung của lớp và đồ dùng cá nhân của bạn.<br>S: Khoanh đúng vào đồ vật cần xin phép trước khi mượn trên phiếu bài tập.<br>A: Tự giác và lịch thiệp."
    },
    {
        "stt": 39, "track": "Mở rộng (24T)", "code": "2.B3.MR2", "strand": "B. Đạo đức AI",
        "subtopic": "B3. Nguyên tắc đạo đức và trách nhiệm xã hội – Của bạn và của tớ",
        "yccd": "Thực hành nói lời xin phép lịch sự trước khi mượn đồ dùng hoặc mượn xem bức tranh của bạn.",
        "explanation": "Nguyên tắc Đồng thuận (Consent) sơ khai: Luôn hỏi ý kiến và được sự đồng ý của chủ sở hữu trước khi sử dụng.",
        "evidence": "K: Nhớ câu nói xin phép: 'Bạn cho mình mượn... có được không?'.<br>S: Thực hành đóng vai hỏi mượn đồ lịch sự và chờ bạn gật đầu đồng ý.<br>A: Tôn trọng quyền tự quyết của người khác."
    },

    # Mạch C - Lớp 2
    {
        "stt": 40, "track": "Cốt lõi (12T)", "code": "2.C1.1", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C1. Đặc điểm chính của AI – Cách AI học và học liệu của AI",
        "yccd": "Nêu được rằng 'dữ liệu' chính là các hình ảnh, âm thanh mẫu mà con người gom lại để dạy cho máy học.",
        "explanation": "Định nghĩa khoa học dữ liệu ở mức độ trực quan, gần gũi: Dữ liệu là tập hợp các bức ảnh, tiếng động được chuẩn bị để máy nhận biết.",
        "evidence": "K: Trả lời được câu hỏi: 'Dữ liệu của máy học con mèo gồm những gì?' (gồm nhiều tranh ảnh con mèo).<br>S: Chỉ đúng xấp ảnh mẫu là 'dữ liệu để dạy máy'.<br>A: Coi trọng việc thu thập ví dụ chính xác."
    },
    {
        "stt": 41, "track": "Mở rộng (24T)", "code": "2.C1.MR1", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C1. Đặc điểm chính của AI – Cách AI học và học liệu của AI",
        "yccd": "Nêu được điểm khác nhau đơn giản: Con người học bằng cách nhìn, chơi đùa và trải nghiệm thật; còn máy học bằng cách xem qua các bức ảnh hoặc âm thanh mẫu.",
        "explanation": "Đính chính khoa học: So sánh phương thức nhận thức sinh học (trải nghiệm đa giác quan) và máy học (xử lý dữ liệu số), không thần thánh hóa máy.",
        "evidence": "K: Nêu được: Em sờ vào con mèo thật để biết lông mềm; máy chỉ xem ảnh trên màn hình.<br>S: Nối đúng cách học của người và cách học của máy trên bảng phân loại.<br>A: Tự hào về trí thông minh kỳ diệu của con người."
    },
    {
        "stt": 42, "track": "Cốt lõi (12T)", "code": "2.C3.1", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C3. Công nghệ AI – Sơ lược cách AI phân loại đồ vật",
        "yccd": "Nhận biết được rằng máy thông minh có thể giúp con người chia đồ vật thành các nhóm khác nhau (như chia nhóm quả cam và quả chuối).",
        "explanation": "Nhiệm vụ phân loại (Classification): Một trong những chức năng phổ biến nhất của công nghệ thị giác máy tính và học máy.",
        "evidence": "K: Nêu được máy có thể tự chia quả thành nhóm quả tròn và quả dài.<br>S: Chỉ vào màn hình mô phỏng thấy máy tự chia rổ hoa quả thành 2 bên.<br>A: Hào hứng với sự nhanh nhẹn của máy."
    },
    {
        "stt": 43, "track": "Cốt lõi (12T)", "code": "2.C3.2", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C3. Công nghệ AI – Sơ lược cách AI phân loại đồ vật",
        "yccd": "Nêu được ví dụ máy thông minh có thể đoán nhầm khi đồ vật nhìn quá giống nhau (như nhầm quả bóng màu cam với quả cam).",
        "explanation": "Giới hạn của mô hình: AI không hoàn hảo và có thể mắc sai sót khi dữ liệu có đặc điểm bên ngoài tương tự nhau.",
        "evidence": "K: Chỉ ra được tình huống máy nhầm quả bóng tròn màu cam là quả cam thật.<br>S: Giải thích được vì sao máy lại nhầm (do cả hai đều tròn và có màu cam).<br>A: Hiểu rằng không được tin tưởng máy tuyệt đối."
    },
    {
        "stt": 44, "track": "Mở rộng (24T)", "code": "2.C3.MR1", "strand": "C. Các kĩ thuật và ứng dụng AI",
        "subtopic": "C3. Công nghệ AI – Sơ lược cách AI phân loại đồ vật",
        "yccd": "Quan sát cô giáo làm mẫu trên phần mềm mô phỏng và nói được: Con người nhận ra đồ vật nhanh hơn máy khi đồ vật bị che khuất một phần.",
        "explanation": "Đính chính khoa học: So sánh trực quan khả năng nhận diện hình ảnh giữa mắt người và mô hình máy tính khi gặp vật cản.",
        "evidence": "K: Nói được mắt người vẫn nhận ra quả táo dù bị chiếc lá che một nửa.<br>S: Quan sát thí nghiệm che đồ vật và nêu nhận xét đúng/sai.<br>A: Nhận ra trí tuệ con người vượt trội hơn máy ở sự suy luận linh hoạt."
    },

    # Mạch D - Lớp 2
    {
        "stt": 45, "track": "Cốt lõi (12T)", "code": "2.D1.1", "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "D1. Nhận diện và hình thành giải pháp – Máy thông minh giúp giải quyết vấn đề quanh em",
        "yccd": "Nêu được một việc vất vả trong lớp hoặc ở nhà mà em ước có một chú robot thông minh đến giúp đỡ (như lau bảng trên cao, nhặt rác dưới gầm bàn).",
        "explanation": "Khởi đầu tư duy giải quyết vấn đề: Xác định nhu cầu thực tế của con người trước khi nghĩ đến công cụ công nghệ.",
        "evidence": "K: Nêu được việc khó khăn cần giúp đỡ trong lớp học.<br>S: Mô tả bài toán bằng lời nói rõ ràng trước nhóm bạn.<br>A: Có tinh thần giúp đỡ thầy cô và bạn bè."
    },
    {
        "stt": 46, "track": "Cốt lõi (12T)", "code": "2.D1.2", "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "D1. Nhận diện và hình thành giải pháp – Ý tưởng máy thông minh",
        "yccd": "Vẽ tranh hoặc kể tên một chú robot mơ ước do em tưởng tượng ra để giúp đỡ mọi người.",
        "explanation": "Kích thích trí tưởng tượng và sáng tạo công nghệ nhân văn: Thiết kế ý tưởng robot phục vụ cuộc sống.",
        "evidence": "K: Trình bày được tên và nhiệm vụ chính của chú robot em vẽ.<br>S: Vẽ hoàn chỉnh bức tranh chú robot mơ ước có các bộ phận giúp việc.<br>A: Yêu thích sáng tạo và khoa học kỹ thuật."
    },
    {
        "stt": 47, "track": "Mở rộng (24T)", "code": "2.D1.MR1", "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "D1. Nhận diện và hình thành giải pháp – Ý tưởng máy thông minh",
        "yccd": "Chọn được một số tấm thẻ hình ảnh đúng để chuẩn bị làm 'bài học mẫu' dạy cho chú robot của em nhận biết đồ vật.",
        "explanation": "Đóng vai người thiết kế dữ liệu: Tự tay lựa chọn các mẫu ví dụ phù hợp để chuẩn bị dạy cho mô hình AI.",
        "evidence": "K: Giải thích vì sao chọn các thẻ tranh này mà không chọn thẻ tranh khác.<br>S: Nhặt đúng 3-5 tấm thẻ tranh quả táo rõ nét cho vào hộp dữ liệu của robot.<br>A: Làm việc có mục đích và chọn lọc."
    },
    {
        "stt": 48, "track": "Cốt lõi (12T)", "code": "2.D2.1", "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "D2. Cấu trúc và tương tác, cải tiến hệ thống – Vai trò của dữ liệu",
        "yccd": "Nêu được rằng máy thông minh cần có các ví dụ mẫu do con người chuẩn bị thì mới có thể học và làm việc được.",
        "explanation": "Đính chính khoa học: Tuyệt đối tránh ẩn dụ 'dữ liệu là thức ăn giúp AI lớn lên' (gây nhân cách hóa máy). Thay bằng: Dữ liệu là các bài học mẫu, ví dụ mẫu mà con người cung cấp cho máy.",
        "evidence": "K: Nhắc lại được: 'Nếu không có ví dụ mẫu thì máy không biết làm bài'.<br>S: Nói đúng câu kết luận khi quan sát máy không có dữ liệu đầu vào.<br>A: Ý thức được vai trò chuẩn bị chu đáo của con người."
    },
    {
        "stt": 49, "track": "Cốt lõi (12T)", "code": "2.D2.2", "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "D2. Cấu trúc và tương tác, cải tiến hệ thống – Vai trò của dữ liệu",
        "yccd": "Giải thích được rằng nếu đưa cho máy những bức ảnh bị mờ, chụp tối hoặc sai tên thì máy sẽ học sai và đưa ra kết quả sai.",
        "explanation": "Khái niệm chất lượng dữ liệu: Dữ liệu mẫu phải rõ ràng, chính xác thì mô hình mới đưa ra kết quả tin cậy.",
        "evidence": "K: Chỉ ra bức ảnh bị mờ, nhòe và nói: 'Ảnh này máy không nhìn rõ, dễ đoán sai'.<br>S: Nhặt bỏ bức ảnh mờ ra khỏi bộ dữ liệu mẫu dạy máy.<br>A: Cẩn thận, tỉ mỉ và chính xác."
    },
    {
        "stt": 50, "track": "Mở rộng (24T)", "code": "2.D2.MR1", "strand": "D. Thiết kế hệ thống AI",
        "subtopic": "D2. Cấu trúc và tương tác, cải tiến hệ thống – Vai trò của dữ liệu",
        "yccd": "Thực hành thu thập và sắp xếp 5-10 bức tranh rõ nét từ sách báo cũ để tạo thành bộ ví dụ mẫu dạy máy nhận diện đồ vật.",
        "explanation": "Hoạt động thực hành Unplugged: Học sinh trải nghiệm toàn bộ quy trình thu thập và chuẩn bị dữ liệu học máy thủ công.",
        "evidence": "K: Giải thích vì sao bộ tranh của nhóm mình là bộ dữ liệu tốt.<br>S: Cắt/dán ngay ngắn các hình ảnh hoa quả rõ nét vào bảng bìa nhóm.<br>A: Hợp tác vui vẻ, khéo léo và biết chia sẻ công việc với bạn."
    }
]

def build_comprehensive_docx(output_path):
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(0.7)
        s.bottom_margin = Inches(0.7)
        s.left_margin = Inches(0.7)
        s.right_margin = Inches(0.7)
        
    def add_p(text="", style=None, align=WD_ALIGN_PARAGRAPH.LEFT, bold=False, italic=False, size=11, color=None, space_after=6):
        p = doc.add_paragraph(style=style)
        p.alignment = align
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if text:
            r = p.add_run(text)
            r.font.name = "Times New Roman"
            r.font.size = Pt(size)
            r.font.bold = bold
            r.font.italic = italic
            if color:
                r.font.color.rgb = color
        return p

    # HEADER BỘ
    add_p("BỘ GIÁO DỤC VÀ ĐÀO TẠO", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=11)
    add_p("DỰ ÁN XÂY DỰNG CHƯƠNG TRÌNH GIÁO DỤC TRÍ TUỆ NHÂN TẠO PHỔ THÔNG", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=12, color=RGBColor(0, 32, 96))
    add_p("────────────────────────", align=WD_ALIGN_PARAGRAPH.CENTER, size=10, color=RGBColor(128, 128, 128))
    
    # TIÊU ĐỀ CHÍNH
    add_p("KHUNG CHƯƠNG TRÌNH GIÁO DỤC TRÍ TUỆ NHÂN TẠO (AI)", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=16, color=RGBColor(192, 0, 0))
    add_p("CỤM TIỂU HỌC KHỞI ĐẦU: LỚP 1 VÀ LỚP 2", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=14, color=RGBColor(0, 32, 96))
    add_p("(Bản hoàn chỉnh tích hợp 8 phần chuẩn mực theo thẩm định của Hội đồng chuyên môn\nTuân thủ Quyết định 2422/QĐ-BGDĐT và Công văn 5588/BGDĐT-GDPT)", align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, size=10)
    
    doc.add_paragraph() # space
    
    # I. QUAN ĐIỂM XÂY DỰNG CHƯƠNG TRÌNH
    add_p("I. QUAN ĐIỂM XÂY DỰNG CHƯƠNG TRÌNH", bold=True, size=13, color=RGBColor(0, 32, 96))
    add_p("1. Pháp lý và chuẩn mực tối cao: Tuân thủ tuyệt đối Quyết định số 2422/QĐ-BGDĐT (Single Source of Truth) và Công văn số 5588/BGDĐT-GDPT của Bộ GD&ĐT; bảo đảm tính thống nhất với Chương trình GDPT 2018 môn Tin học.", size=10.5)
    add_p("2. Lấy con người làm trung tâm (UNESCO AI Framework 2024): Đặt sự phát triển tâm sinh lý, an toàn và lợi ích của trẻ em làm ưu tiên số một. AI chỉ là công cụ hỗ trợ, con người giữ vai trò kiểm soát và làm chủ.", size=10.5)
    add_p("3. Trực quan – Trải nghiệm ban đầu – Vừa sức (AI4K12 Big Ideas 1–5): Chuyển hóa các khái niệm công nghệ trừu tượng thành các hoạt động trải nghiệm gần gũi, sử dụng thẻ tranh, đóng vai, kể chuyện; kiên quyết loại bỏ ngôn ngữ hàn lâm, đao to búa lớn đối với học sinh 6–8 tuổi.", size=10.5)
    add_p("4. Công bằng tiếp cận và 100% Unplugged Fallback: Không phân biệt điều kiện kinh tế gia đình. 100% bài học cốt lõi đều được thiết kế phương án dự phòng không cần máy tính hoặc Internet.", size=10.5)

    # II. MỤC TIÊU GIÁO DỤC
    add_p("II. MỤC TIÊU GIÁO DỤC CỤM TIỂU HỌC KHỞI ĐẦU", bold=True, size=13, color=RGBColor(0, 32, 96))
    add_p("1. Mục tiêu chung: Giúp học sinh bước đầu làm quen với sự hiện diện của AI trong đời sống; phân biệt được cảm xúc thật của con người với sự mô phỏng của máy; hình thành ý thức an toàn, tự bảo vệ bản thân và biết tôn trọng quyền sở hữu của bạn bè.", size=10.5)
    add_p("2. Mục tiêu cụ thể Lớp 1 (Nhận biết & Cảm xúc): Nhận diện đồ dùng thông minh; nhận biết máy móc do con người lập trình; hiểu camera là 'mắt' và micro là 'tai' của máy; biết máy học từ các tranh ảnh mẫu do con người cung cấp.", size=10.5)
    add_p("3. Mục tiêu cụ thể Lớp 2 (Trải nghiệm có hướng dẫn & Tự chủ sơ khai): Nhận biết AI hỗ trợ gia đình; biết xin phép người lớn trước khi dùng máy; biết máy có thể đoán nhầm hoặc thiên vị nếu thiếu ví dụ mẫu; bước đầu có ý tưởng sáng tạo robot giúp đỡ mọi người.", size=10.5)

    # III. CẤU TRÚC THỜI LƯỢNG & PHÂN ĐỊNH 2 LUỒNG
    add_p("III. CẤU TRÚC THỜI LƯỢNG & PHÂN ĐỊNH 2 LUỒNG NỘI DUNG", bold=True, size=13, color=RGBColor(0, 32, 96))
    add_p("Căn cứ Mục II Công văn 5588/BGDĐT-GDPT, chương trình phân định rõ ràng giữa 2 luồng nội dung:", size=10.5)
    add_p("• Luồng 1 – Nội dung cốt lõi bắt buộc (12 tiết/lớp/năm học): Bố trí trong kế hoạch dạy học 2 buổi/ngày. Phủ đủ 100% YCCĐ cốt lõi của QĐ 2422 (17 mã Lớp 1 và 17 mã Lớp 2). Đây là căn cứ duy nhất nếu đánh giá diện rộng.", size=10.5)
    add_p("• Luồng 2 – Nội dung mở rộng linh hoạt (24 tiết/lớp/năm học): Tổ chức dưới hình thức câu lạc bộ, dự án sáng tạo, hoạt động trải nghiệm theo nhu cầu. Phủ đủ 100% mã MR của QĐ 2422 (4 mã Lớp 1 và 12 mã Lớp 2). Không dùng nội dung mở rộng để đánh giá bắt buộc đối với mọi học sinh.", size=10.5)
    add_p("• Chuẩn thời lượng tiết dạy: Mỗi tiết học kéo dài từ 30 đến 35 phút, bảo đảm phù hợp với năng lượng tập trung của học sinh Lớp 1 và Lớp 2.", size=10.5)

    # IV. HÀNG RÀO AN TOÀN SỐ & BẢO VỆ DỮ LIỆU HỌC SINH (CV 5588)
    add_p("IV. HÀNG RÀO AN TOÀN SỐ VÀ BẢO VỆ DỮ LIỆU HỌC SINH (CV 5588)", bold=True, size=13, color=RGBColor(192, 0, 0))
    add_p("Để bảo vệ tối đa trẻ em 6–8 tuổi trên không gian số theo Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và CV 5588, Khung chương trình xác lập 7 NGUYÊN TẮC AN TOÀN BẤT BIẾN:", size=10.5, italic=True)
    add_p("1. CẤM tự do sử dụng GenAI thương mại: Học sinh Lớp 1–2 tuyệt đối không được tự do tạo lệnh trên các chatbot AI tạo sinh công cộng (như ChatGPT, Claude, Gemini...).", size=10)
    add_p("2. KHÔNG tạo tài khoản cá nhân: Tuyệt đối không yêu cầu học sinh hoặc phụ huynh tạo tài khoản cá nhân để phục vụ các bài học AI.", size=10)
    add_p("3. KHÔNG nhập dữ liệu cá nhân thật: Tuyệt đối không cho học sinh nhập họ tên thật, ngày sinh, địa chỉ nhà, trường lớp, số điện thoại hoặc dữ liệu nhạy cảm vào bất kỳ phần mềm nào.", size=10)
    add_p("4. KHÔNG quét khuôn mặt thật của học sinh: Các hoạt động thị giác máy tính chỉ sử dụng tranh vẽ đồ vật, hoa quả hoặc thẻ mẫu nhân vật hoạt hình; cấm dùng camera quét khuôn mặt thật của học sinh trong lớp.", size=10)
    add_p("5. Giám sát 100% của giáo viên: Mọi thao tác trên máy (nếu có) phải do giáo viên trực tiếp trình chiếu trên màn hình chung hoặc giám sát chặt chẽ trong môi trường cục bộ đã duyệt.", size=10)
    add_p("6. Ưu tiên học liệu Unplugged: Sử dụng tối đa thẻ tranh giấy, đồ dùng trực quan, trò chơi vận động; dữ liệu học máy phải được giáo viên chuẩn bị sẵn và rà soát nội dung an toàn.", size=10)
    add_p("7. Quy trình xử lý sự cố tức thì: Nhà trường và giáo viên phải có phương án dừng ngay thiết bị khi phát hiện nội dung hoặc phản hồi không phù hợp với lứa tuổi tiểu học.", size=10)

    # V. PHƯƠNG PHÁP & ĐÁNH GIÁ
    add_p("V. PHƯƠNG PHÁP DẠY HỌC VÀ ĐỊNH HƯỚNG ĐÁNH GIÁ (CV 2345 & MỤC VI QĐ 2422)", bold=True, size=13, color=RGBColor(0, 32, 96))
    add_p("1. Tiến trình sư phạm: Vận hành theo Chu trình học tập trải nghiệm David Kolb (4 pha: CE – Trải nghiệm cụ thể ➔ RO – Quan sát phản tư ➔ AC – Khái quát hóa ➔ AE – Thử nghiệm vận dụng) gói gọn trong 30–35 phút.", size=10.5)
    add_p("2. Nguyên tắc đánh giá: Đánh giá quá trình giữ vai trò chủ đạo, tuyệt đối KHÔNG cho điểm số, KHÔNG tổ chức bài kiểm tra hay bài thi riêng. Đánh giá hoàn toàn bằng nhận xét dựa trên quan sát thái độ, lời nói, sản phẩm tranh vẽ hoặc thao tác xếp thẻ của học sinh.", size=10.5)
    add_p("3. Đa dạng hóa minh chứng: Đánh giá dựa trên ma trận Kiến thức – Kỹ năng – Phẩm chất (K–S–A), không đánh giá dựa trên mức độ sở hữu thiết bị thông minh của gia đình học sinh.", size=10.5)

    # VI. BẢNG KHUNG NỘI DUNG & YCCĐ
    add_p("VI. BẢNG CHI TIẾT KHUNG NỘI DUNG, YCCĐ VÀ MA TRẬN ĐÁNH GIÁ", bold=True, size=13, color=RGBColor(0, 32, 96))
    add_p("(Đã chuẩn hóa ngôn ngữ vừa sức 6–8 tuổi, tách bạch YCCĐ hành vi, Diễn giải sư phạm chuẩn xác và Minh chứng quan sát)", italic=True, size=10)

    # Function add table for a list of items
    def add_grade_table(items, grade_title):
        add_p(f"BẢNG YCCĐ {grade_title.upper()}", bold=True, size=11, color=RGBColor(192, 0, 0))
        tbl = doc.add_table(rows=1, cols=6)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        
        widths = [Inches(0.4), Inches(0.8), Inches(0.6), Inches(1.3), Inches(2.2), Inches(1.9)]
        hdrs = ["STT", "Luồng", "Mã", "Mạch / Chủ đề", "Yêu cầu cần đạt chuẩn hóa\n(Ngôn ngữ vừa sức học sinh)", "Diễn giải sư phạm & Minh chứng K-S-A"]
        
        h_row = tbl.rows[0].cells
        for idx, h in enumerate(hdrs):
            h_row[idx].text = h
            set_cell_margins(h_row[idx], top=100, bottom=100, left=100, right=100)
            set_cell_shading(h_row[idx], "1F4E79")
            h_row[idx].width = widths[idx]
            p = h_row[idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(8.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                
        for it in items:
            row = tbl.add_row().cells
            for idx in range(6):
                row[idx].width = widths[idx]
                set_cell_margins(row[idx], top=70, bottom=70, left=90, right=90)
                
            if it["stt"] % 2 == 0:
                for c in row:
                    set_cell_shading(c, "F2F5F9")
                    
            # 0: STT
            p0 = row[0].paragraphs[0]
            p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r0 = p0.add_run(str(it["stt"]))
            r0.font.name = "Times New Roman"; r0.font.size = Pt(8.5); r0.font.bold = True
            
            # 1: Luồng
            p1 = row[1].paragraphs[0]
            p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r1 = p1.add_run(it["track"])
            r1.font.name = "Times New Roman"; r1.font.size = Pt(8)
            if "Cốt lõi" in it["track"]:
                r1.font.bold = True; r1.font.color.rgb = RGBColor(0, 32, 96)
            else:
                r1.font.italic = True; r1.font.color.rgb = RGBColor(192, 0, 0)
                
            # 2: Mã
            p2 = row[2].paragraphs[0]
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r2 = p2.add_run(it["code"])
            r2.font.name = "Times New Roman"; r2.font.size = Pt(8.5); r2.font.bold = True
            
            # 3: Mạch / Chủ đề
            p3 = row[3].paragraphs[0]
            r3 = p3.add_run(it["subtopic"])
            r3.font.name = "Times New Roman"; r3.font.size = Pt(8)
            
            # 4: YCCĐ chuẩn hóa
            p4 = row[4].paragraphs[0]
            r4 = p4.add_run(it["yccd"])
            r4.font.name = "Times New Roman"; r4.font.size = Pt(8.5); r4.font.bold = True
            
            # 5: Diễn giải & Minh chứng
            p5 = row[5].paragraphs[0]
            r5_exp = p5.add_run("💡 Diễn giải: " + it["explanation"] + "\n\n")
            r5_exp.font.name = "Times New Roman"; r5_exp.font.size = Pt(8); r5_exp.font.italic = True
            r5_exp.font.color.rgb = RGBColor(80, 80, 80)
            
            r5_ev_hdr = p5.add_run("📋 Minh chứng K-S-A:\n")
            r5_ev_hdr.font.name = "Times New Roman"; r5_ev_hdr.font.size = Pt(8); r5_ev_hdr.font.bold = True
            r5_ev_hdr.font.color.rgb = RGBColor(0, 102, 204)
            
            # clean html tags for word
            ev_clean = it["evidence"].replace("<br>", "\n")
            r5_ev = p5.add_run(ev_clean)
            r5_ev.font.name = "Times New Roman"; r5_ev.font.size = Pt(8)
            
        doc.add_paragraph() # space

    add_grade_table(items_l1, "Lớp 1 (21 YCCĐ: 17 Cốt lõi – 4 Mở rộng)")
    add_grade_table(items_l2, "Lớp 2 (29 YCCĐ: 17 Cốt lõi – 12 Mở rộng)")

    doc.save(output_path)
    print("DOCX saved successfully.")

def build_comprehensive_md(output_path):
    lines = []
    lines.append("# KHUNG CHƯƠNG TRÌNH GIÁO DỤC TRÍ TUỆ NHÂN TẠO (AI)")
    lines.append("## CỤM TIỂU HỌC KHỞI ĐẦU: LỚP 1 VÀ LỚP 2")
    lines.append("*(Bản hoàn chỉnh tích hợp 8 phần chuẩn mực theo thẩm định của Hội đồng chuyên môn – Tuân thủ QĐ 2422/QĐ-BGDĐT và CV 5588/BGDĐT-GDPT)*\n")
    
    lines.append("### I. QUAN ĐIỂM XÂY DỰNG CHƯƠNG TRÌNH")
    lines.append("1. **Pháp lý tối cao (QĐ 2422 & CV 5588):** Chương trình bám sát tuyệt đối mục tiêu, 4 mạch nội dung và hệ thống YCCĐ của Bộ GD&ĐT; kế thừa liên thông môn Tin học và CT GDPT 2018.")
    lines.append("2. **Lấy con người làm trung tâm (UNESCO 2024):** Công nghệ AI chỉ là công cụ hỗ trợ phát triển cá nhân và học tập; con người luôn giữ vai trò kiểm soát, tự chủ và chịu trách nhiệm.")
    lines.append("3. **Vừa sức – Trực quan – Không đao to búa lớn:** Tuyệt đối loại bỏ các thuật ngữ chuyên môn hàn lâm dành cho người lớn. YCCĐ được viết bằng ngôn ngữ hành vi học sinh 6–8 tuổi hiểu được, làm được.")
    lines.append("4. **Công bằng tiếp cận & 100% Unplugged Fallback:** Không lệ thuộc thiết bị hay đường truyền; 100% bài học cốt lõi có phương án dạy bằng thẻ tranh, trò chơi đóng vai khi thiếu phòng máy.\n")
    
    lines.append("### II. MỤC TIÊU GIÁO DỤC CỤM TIỂU HỌC KHỞI ĐẦU")
    lines.append("- **Mục tiêu chung:** Hình thành nhận thức ban đầu về AI; phân biệt được cảm xúc thật của con người với sự mô phỏng của máy móc; rèn luyện thói quen an toàn, hỏi người lớn trước khi dùng thiết bị thông minh; tôn trọng sản phẩm của người khác.")
    lines.append("- **Mục tiêu Lớp 1 (Nhận biết & Cảm xúc):** Nhận diện thiết bị thông minh; hiểu cảm xúc của máy là do người tạo ra; nhận biết camera là 'mắt' và micro là 'tai' của máy; máy học từ các tranh ảnh mẫu do con người cung cấp.")
    lines.append("- **Mục tiêu Lớp 2 (Trải nghiệm có hướng dẫn & Tự chủ sơ khai):** Nêu được AI giúp ích gì trong gia đình; biết khi nào nên và không nên dùng AI; nhận thức máy có thể đoán nhầm hoặc thiên vị nếu thiếu ví dụ; khởi tạo ý tưởng robot giúp đỡ mọi người.\n")
    
    lines.append("### III. KHUNG THỜI LƯỢNG & PHÂN ĐỊNH 2 LUỒNG NỘI DUNG (CV 5588)")
    lines.append("| Luồng nội dung | Thời lượng chuẩn | Quy mô triển khai | Mục tiêu & Phạm vi đánh giá |")
    lines.append("|---|:---:|---|---|")
    lines.append("| **Nội dung Cốt lõi (Core)** | **12 tiết/lớp/năm** | Bắt buộc 100% học sinh (bố trí trong kế hoạch 2 buổi/ngày) | Đạt 100% YCCĐ cốt lõi QĐ 2422 (17 mã L1, 17 mã L2). Là căn cứ duy nhất nếu đánh giá diện rộng. |")
    lines.append("| **Nội dung Mở rộng (MR)** | **24 tiết/lớp/năm** | Tự nguyện, linh hoạt (CLB, dự án, trải nghiệm) | Đạt 100% YCCĐ mở rộng QĐ 2422 (4 mã L1, 12 mã L2). Không dùng làm căn cứ đánh giá bắt buộc đối với mọi học sinh. |")
    lines.append("| **Thời lượng tiết học** | **30 – 35 phút/tiết** | Cấp Tiểu học (Lớp 1 và Lớp 2) | Tuân thủ đặc điểm tâm sinh lý lứa tuổi theo Thông tư số 28/2020/TT-BGDĐT. |\n")
    
    lines.append("### IV. HÀNG RÀO AN TOÀN SỐ VÀ BẢO VỆ DỮ LIỆU HỌC SINH (CV 5588)")
    lines.append("Thực hiện nghiêm túc Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và CV 5588, chương trình xác lập **7 Nguyên tắc An toàn Cấp Bách**:")
    lines.append("1. **CẤM học sinh tự do dùng GenAI thương mại:** Không cho trẻ 6–8 tuổi tự gõ lệnh trên ChatGPT, Claude, Gemini...")
    lines.append("2. **KHÔNG tạo tài khoản cá nhân cho học sinh:** Tuyệt đối không yêu cầu học sinh hay phụ huynh đăng ký tài khoản.")
    lines.append("3. **KHÔNG nhập dữ liệu cá nhân thật:** Cấm nhập tên thật, địa chỉ nhà, số điện thoại, giọng nói hay ảnh chụp gia đình vào phần mềm.")
    lines.append("4. **KHÔNG quét khuôn mặt thật của học sinh:** Trải nghiệm thị giác máy tính chỉ thực hiện trên tranh thẻ hoa quả, đồ vật hoặc nhân vật hoạt hình.")
    lines.append("5. **Giám sát 100% của giáo viên:** Mọi thao tác công nghệ đều được giáo viên trình chiếu trên màn hình chung có kiểm duyệt.")
    lines.append("6. **Ưu tiên hoạt động Unplugged không máy tính:** 100% bài cốt lõi phải sẵn sàng dạy bằng thẻ tranh giấy, đóng vai khi mất mạng/mất điện.")
    lines.append("7. **Quy trình xử lý sự cố tức thì:** Giáo viên dừng ngay thiết bị khi phát hiện nội dung lạ và báo cáo ban giám hiệu nhà trường.\n")
    
    lines.append("### V. PHƯƠNG PHÁP DẠY HỌC & ĐỊNH HƯỚNG ĐÁNH GIÁ")
    lines.append("- **Tiến trình sư phạm Kolb (30–35 phút):** Pha 1: Trải nghiệm kích hoạt (CE: 5–6p) ➔ Pha 2: Quan sát phản tư (RO: 5–7p) ➔ Pha 3: Khái quát bài học (AC: 7–8p) ➔ Pha 4: Thử nghiệm vận dụng (AE: 8–10p).")
    lines.append("- **Định hướng đánh giá:** Đánh giá quá trình bằng quan sát hành vi, tranh vẽ, câu trả lời; tuyệt đối **KHÔNG CHO ĐIỂM SỐ**, không tổ chức bài thi riêng; không đánh giá dựa trên điều kiện thiết bị của gia đình học sinh.\n")
    
    lines.append("### VI. BẢNG CHI TIẾT KHUNG NỘI DUNG, YCCĐ VÀ MA TRẬN ĐÁNH GIÁ (LỚP 1 VÀ LỚP 2)\n")
    
    def add_md_table(items, title):
        lines.append(f"#### {title}")
        lines.append("| STT | Luồng | Mã | Mạch / Chủ đề | Yêu cầu cần đạt chuẩn hóa (Ngôn ngữ vừa sức 6–8 tuổi) | Diễn giải sư phạm & Minh chứng K-S-A |")
        lines.append("|:---:|:---:|:---:|:---|:---|:---|")
        for it in items:
            stt = it["stt"]
            track = f"**{it['track']}**" if "Cốt lõi" in it["track"] else f"*{it['track']}*"
            code = f"`{it['code']}`"
            subtopic = it["subtopic"].replace("|", "/")
            yccd = it["yccd"].replace("|", "/")
            explanation = it["explanation"].replace("|", "/")
            evidence = it["evidence"].replace("|", "/")
            
            detail = f"💡 *Diễn giải:* {explanation}<br><br>📋 **Minh chứng K-S-A:**<br>{evidence}"
            lines.append(f"| {stt} | {track} | {code} | {subtopic} | **{yccd}** | {detail} |")
        lines.append("\n")

    add_md_table(items_l1, "BẢNG YCCĐ LỚP 1 (21 YCCĐ: 17 CỐT LÕI – 4 MỞ RỘNG)")
    add_md_table(items_l2, "BẢNG YCCĐ LỚP 2 (29 YCCĐ: 17 CỐT LÕI – 12 MỞ RỘNG)")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("MD saved successfully.")

if __name__ == "__main__":
    out_dir = r"c:\Users\USER\Desktop\AI-vibe-code\KhungNLĐTAI\03_San_Pham_Chinh_Thuc"
    docx_file = os.path.join(out_dir, "SP1_Khung_Chuong_Trinh_AI_Lop1_Lop2_Hoan_Chinh.docx")
    md_file = os.path.join(out_dir, "SP1_Khung_Chuong_Trinh_AI_Lop1_Lop2_Hoan_Chinh.md")
    build_comprehensive_docx(docx_file)
    build_comprehensive_md(md_file)
    print("All tasks completed.")
