# -*- coding: utf-8 -*-
"""
Script tạo Bảng Ma trận Phân bổ 46 Kỹ năng AI Cấp Tiểu học (Lớp 1 - 5) - Phiên bản v2.0
Đồng bộ: Markdown (.md), Excel (.xlsx), Word (.docx)
Căn cứ: QĐ 2422/QĐ-BGDĐT, CV 5588/BGDĐT-GDPT, UNICEF 9 Requirements, Google BIA, Experience AI, AI4K12, UNESCO, OECD.
"""

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Dữ liệu 46 kỹ năng chi tiết v2.0
SKILLS_DATA = [
    # ==========================================
    # NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI (1 - 7)
    # ==========================================
    {
        "stt": 1,
        "name": "Nhận diện giao diện AI",
        "definition": "Nhận biết và chỉ đúng biểu tượng micro, camera, khung nhận diện khuôn mặt và các vùng điều khiển trên giao diện ứng dụng AI.",
        "group_id": 1,
        "group_name": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "domain": "NLc",
        "g1": {
            "level": "Mức 1: Quan sát / Nhận biết",
            "track": "VN-CORE",
            "yccd": "1.C1.2",
            "sources": "AI4K12 (Big Idea 1), UNESCO (Interface Literacy)",
            "points": [
                "Quan sát giáo viên demo trên máy chiếu, chỉ đúng biểu tượng micro của trợ lý giọng nói và ô vuông nhận diện khuôn mặt khi camera quét.",
                "Phân biệt tín hiệu thị giác: biểu tượng micro chuyển động khi đang 'lắng nghe' và khung viền đổi màu khi AI đã 'nhìn thấy' khuôn mặt.",
                "Thực hành không máy tính (Unplugged): Giơ thẻ bài biểu tượng tương ứng khi nghe cô giáo mô tả hành động của máy."
            ]
        },
        "g2": {
            "level": "Mức 1: Quan sát / Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.A2.1, 2.C1.1",
            "sources": "AI4K12 (Big Idea 1), Singapore MOE (Smart Nation)",
            "points": [
                "Nhận biết các nút chức năng kích hoạt tính năng AI trên giao diện màn hình thông minh gia đình (nút micro trên điều khiển tivi, camera giám sát nhà, loa thông minh).",
                "Phân biệt nút bấm cơ học thông thường vs nút kích hoạt chế độ nhận biết tự động của AI.",
                "Quan sát biểu tượng loa thông minh phát tín hiệu đèn LED báo hiệu hệ thống đã sẵn sàng nhận lệnh."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.2, 3.A1.MR1",
            "sources": "Google BIA (AI Literacy Guide), Experience AI",
            "points": [
                "Thao tác trên máy tính phòng máy: Nhấp chuột kích hoạt biểu tượng micro/camera trên phần mềm học tập tiếng Anh hoặc trợ lý số.",
                "Xác định đúng vùng nhập câu lệnh (prompt box) và vùng hiển thị câu trả lời (response area) trên màn hình ứng dụng.",
                "Thực hành cấp quyền truy cập micro/camera trên trình duyệt có sự kiểm soát của giáo viên."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-MR",
            "yccd": "4.C2.1, 4.C2.MR1",
            "sources": "Google Applied Digital Skills (AutoDraw, Quick Draw)",
            "points": [
                "Nhận diện đầy đủ các phân vùng chức năng trên giao diện AI tạo sinh tranh vẽ (AutoDraw) và văn bản: Thanh công cụ gợi ý nét vẽ thông minh, nút Tạo lại (Regenerate), bảng màu.",
                "Tự chủ điều hướng giữa giao diện nhập dữ liệu và bảng kết quả do AI đề xuất; chọn phương án tối ưu."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.C5.2",
            "sources": "Experience AI Foundations (Teachable Machine)",
            "points": [
                "Vận hành độc lập giao diện công cụ huấn luyện AI trực quan (Google Teachable Machine): Vùng lớp dữ liệu (Class), nút thu nạp qua Webcam/Tải tệp, nút Train Model, thanh tiến trình huấn luyện, bảng kiểm thử trực tiếp (Preview).",
                "Đọc hiểu thanh chỉ số tin cậy (Confidence Bar) theo thời gian thực trên giao diện đầu ra."
            ]
        }
    },
    {
        "stt": 2,
        "name": "Phát âm câu lệnh chuẩn xác",
        "definition": "Phát âm to, rõ ràng, đúng ngữ điệu và tốc độ trước micro để cảm biến âm thanh của hệ thống AI thu nhận tối ưu.",
        "group_id": 1,
        "group_name": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "domain": "NLc",
        "g1": {
            "level": "Mức 1: Quan sát / Bắt chước",
            "track": "VN-CORE",
            "yccd": "1.C1.4",
            "sources": "AI4K12 (Big Idea 4 - Natural Interaction)",
            "points": [
                "Nghe cô giáo làm mẫu và tập phát âm đồng thanh to, tròn vành rõ chữ 1-2 từ khoá đơn giản (như 'Xin chào', 'Bật đèn') trước micro lớp học.",
                "Nhận thức qua trải nghiệm: Nếu nói quá khẽ, nói lí nhí hoặc la hét thì máy tính sẽ không hiểu được hoặc báo lỗi âm thanh."
            ]
        },
        "g2": {
            "level": "Mức 1: Thực hành tập thể",
            "track": "VN-CORE",
            "yccd": "2.A2.MR1",
            "sources": "Singapore MOE (Primary Computing)",
            "points": [
                "Luyện phát âm câu lệnh ngắn hoàn chỉnh (3-5 từ) có cấu trúc mệnh lệnh rõ ràng: 'Mở bài hát thiếu nhi', 'Thời tiết hôm nay thế nào?' dưới sự giám sát của giáo viên.",
                "Rèn luyện tư thế đứng thẳng, giữ khoảng cách chuẩn (20-30 cm) trước micro để âm thanh không bị rè nhiễu."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.2, 3.A1.MR1",
            "sources": "UNESCO (Apply Level), Experience AI",
            "points": [
                "Tự phát âm câu lệnh trước micro tai nghe cá nhân trên phần mềm luyện tiếng Anh (Duolingo/LingoKids) để hệ thống AI đánh giá độ chuẩn xác ngữ âm.",
                "So sánh sóng âm và điểm đánh giá phát âm của máy; chủ động phát âm lại các âm tiết bị máy đánh dấu đỏ."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-MR",
            "yccd": "4.C2.MR1, 4.A1.MR1",
            "sources": "Google BIA (AI Literacy Guide)",
            "points": [
                "Tự điều chỉnh tốc độ nói, khoảng cách micro và giảm thiểu tạp âm môi trường xung quanh khi phần mềm nhận dạng giọng nói không phiên âm đúng.",
                "Thực hành thay đổi từ ngữ đồng nghĩa nếu AI liên tục gặp khó khăn khi nhận dạng một cụm từ địa phương."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-MR",
            "yccd": "5.A3.2, 5.C5.2",
            "sources": "Experience AI (Audio Models), UNICEF Requirement 4",
            "points": [
                "Phát âm câu lệnh song ngữ (tiếng Việt/tiếng Anh) với ngữ điệu tự nhiên, chuẩn xác, phục vụ điều khiển hệ thống AI hoặc thu nạp mẫu âm thanh cho mô hình phân loại giọng nói.",
                "Phân tích nguyên nhân kỹ thuật khi mô hình nhận diện sai các ngữ điệu vùng miền khác nhau (thiên lệch dữ liệu âm thanh)."
            ]
        }
    },
    {
        "stt": 3,
        "name": "Khai thác AI hỗ trợ học tập",
        "definition": "Sử dụng câu lệnh hợp lý để tra cứu từ vựng, giải thích hiện tượng khoa học, luyện phát âm và khơi gợi ý tưởng học tập.",
        "group_id": 1,
        "group_name": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "domain": "NLc",
        "g1": None,
        "g2": {
            "level": "Mức 1: Quan sát / Cảm thụ",
            "track": "VN-MR",
            "yccd": "2.A1.1",
            "sources": "UNESCO (AI for Humanity)",
            "points": [
                "Xem giáo viên thị phạm: Hỏi trợ lý ảo phát âm từ vựng tiếng Anh minh họa hoặc dịch một câu chào hỏi đơn giản giữa các quốc gia.",
                "Nhận biết AI là 'bạn trợ giảng thông minh' giúp lớp học sinh động và hỗ trợ việc tra cứu nhanh."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.1, 3.A1.2, 3.A1.MR1",
            "sources": "UNESCO (AI in Education), Singapore MOE EdTech",
            "points": [
                "Sử dụng trợ lý học tập thông minh và ứng dụng ngôn ngữ để tra nghĩa từ mới môn Tiếng Việt, kiểm tra lỗi chính tả và luyện nghe nói tiếng Anh.",
                "Áp dụng nguyên tắc: Chỉ dùng AI để giải nghĩa từ ngữ hoặc nghe phát âm mẫu, không để AI viết sẵn câu trả lời."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.A1.MR1, 4.C2.1, 4.C2.MR1",
            "sources": "Google Applied Digital Skills (Verse by Verse)",
            "points": [
                "Nhờ AI gợi ý ý tưởng làm bài tập làm văn (tìm 3 tính từ miêu tả cánh đồng lúa, gợi ý các loài động vật quý hiếm) và vẽ tranh minh họa.",
                "Sử dụng công cụ Verse by Verse hoặc AutoDraw để kích hoạt cảm hứng sáng tác thơ văn và mỹ thuật."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.1, 5.A2.1, 5.A3.1, 5.A3.2",
            "sources": "Experience AI (AI Study Buddy), OECD Learning Compass",
            "points": [
                "Chủ động sử dụng AI như 'Bạn cùng học' (AI Study Buddy): Yêu cầu AI đặt 3 câu hỏi trắc nghiệm ôn tập bài học Lịch sử - Địa lý; yêu cầu giải thích hiện tượng quang hợp bằng ví dụ dễ hiểu cho học sinh lớp 5.",
                "Tự lập dàn ý đề cương thuyết trình dự án môn Khoa học có sự gợi ý phản biện từ AI."
            ]
        }
    },
    {
        "stt": 4,
        "name": "Cấu trúc câu lệnh tường minh (Prompting)",
        "definition": "Thiết lập câu lệnh hoàn chỉnh, rõ ràng gồm: vai trò của AI, bối cảnh, nhiệm vụ cụ thể và giới hạn đầu ra.",
        "group_id": 1,
        "group_name": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "domain": "NLc",
        "g1": None,
        "g2": None,
        "g3": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-MR",
            "yccd": "3.A1.MR1, 3.C5.1",
            "sources": "Google BIA (Prompt Crafting)",
            "points": [
                "Nhận biết sự khác biệt qua ví dụ: Câu lệnh đủ ý ('Hãy kể 1 câu chuyện ngắn về chú mèo dũng cảm') giúp máy hiểu nhanh và đúng hơn câu nói cộc lốc ('Mèo').",
                "Làm quen với quy tắc 'Nói rõ việc cần làm' khi tương tác với phần mềm thông minh."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "4.C2.MR1, 4.A1.MR1",
            "sources": "Google BIA AI Literacy Guide",
            "points": [
                "Thực hành cấu trúc câu lệnh 3 thành phần trên phiếu bài tập và phần mềm: [Vai trò của AI] + [Nhiệm vụ cụ thể] + [Định dạng kết quả mong muốn].",
                "Ví dụ: 'Bạn là chuyên gia cây xanh (Vai trò), hãy nêu 3 lợi ích của rừng ngập mặn (Nhiệm vụ) dưới dạng danh sách gạch đầu dòng (Định dạng)'."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-MR",
            "yccd": "5.A3.2, 5.C5.2",
            "sources": "OECD/EU AILF, Google BIA Guide",
            "points": [
                "Thiết lập thành thạo cấu trúc câu lệnh 4 thành phần hoàn chỉnh: [Vai trò] + [Bối cảnh cụ thể] + [Nhiệm vụ chi tiết] + [Giới hạn đầu ra: số từ, phong cách văn phong, những từ cấm sử dụng].",
                "Đánh giá và so sánh chất lượng văn bản phản hồi giữa câu lệnh sơ sài vs câu lệnh cấu trúc chuẩn mực."
            ]
        }
    },
    {
        "stt": 5,
        "name": "Thiết kế câu lệnh kèm ví dụ (Few-shot)",
        "definition": "Cung cấp 1–2 mẫu chuẩn ngay trong câu lệnh để định hướng AI sinh kết quả đúng quy cách, thể loại và văn phong mong muốn.",
        "group_id": 1,
        "group_name": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "domain": "NLc",
        "g1": None,
        "g2": None,
        "g3": None,
        "g4": {
            "level": "Mức 1: Quan sát / So sánh",
            "track": "VN-MR",
            "yccd": "4.C2.MR1",
            "sources": "Google BIA AI Literacy Guide",
            "points": [
                "Quan sát so sánh hai màn hình kết quả: Câu lệnh yêu cầu chung chung vs Câu lệnh có kèm 1 ví dụ mẫu minh họa.",
                "Nhận ra rằng khi được con người 'mồi' trước một ví dụ mẫu (Few-shot), AI sẽ bắt chước định dạng và trả lời chính xác, sát ý hơn nhiều."
            ]
        },
        "g5": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "5.A3.2, 5.C5.2",
            "sources": "Experience AI, OECD/EU AILF",
            "points": [
                "Viết câu lệnh kèm 1-2 mẫu chuẩn để định hướng AI sáng tác: Cung cấp mẫu 1 khổ thơ 4 chữ về mùa thu để yêu cầu AI viết tiếp khổ thơ thứ hai đúng vần điệu.",
                "Cung cấp 1 cặp câu đố mẫu về con vật kèm câu trả lời để yêu cầu AI tạo ra 2 câu đố mới theo đúng cấu trúc đó."
            ]
        }
    },
    {
        "stt": 6,
        "name": "Tinh chỉnh câu lệnh đa vòng",
        "definition": "Đọc kết quả của AI và viết tiếp câu lệnh bổ sung để nắn chỉnh phản hồi cho đến khi đạt yêu cầu mong muốn.",
        "group_id": 1,
        "group_name": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "domain": "NLc",
        "g1": None,
        "g2": {
            "level": "Mức 1: Quan sát",
            "track": "VN-MR",
            "yccd": "2.A3.1, 2.A3.MR1",
            "sources": "Singapore MOE Cyber Wellness",
            "points": [
                "Quan sát cô giáo nói câu lệnh lần 2 chi tiết hơn khi trợ lý ảo chưa hiểu lệnh lần 1.",
                "Nhận biết con người đóng vai trò chủ động nắn chỉnh để máy móc phục vụ đúng ý mình."
            ]
        },
        "g3": {
            "level": "Mức 1: Quan sát / Thảo luận",
            "track": "VN-MR",
            "yccd": "3.A1.MR1, 3.A3.2",
            "sources": "Google BIA (AI Literacy Guide)",
            "points": [
                "Đọc câu trả lời ban đầu của AI trên màn hình máy chiếu và thảo luận nhóm xem cần yêu cầu thêm gì để máy trả lời chi tiết và đúng trọng tâm hơn.",
                "Nhận biết AI không thể đọc được suy nghĩ con người mà phải qua từng lượt hội thoại tương tác."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "4.C2.MR1, 4.D2.1",
            "sources": "Google Applied Digital Skills",
            "points": [
                "Thực hành nhập tiếp câu lệnh bổ sung vòng 2, vòng 3: 'Hãy viết ngắn gọn hơn trong 3 dòng', 'Hãy thêm 2 ví dụ về động vật ở Việt Nam', 'Đổi giọng văn hài hước hơn'.",
                "Ghi chép sự thay đổi của phản hồi qua từng vòng tinh chỉnh."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-MR",
            "yccd": "5.A3.2, 5.D2.1",
            "sources": "OECD AILF, Experience AI",
            "points": [
                "Tự chủ thực hiện phiên tương tác đa vòng (3-4 lượt) để phát triển một sản phẩm hoàn chỉnh: Vòng 1 (Khởi tạo ý tưởng) -> Vòng 2 (Lập dàn ý chi tiết) -> Vòng 3 (Soát lỗi từ ngữ và chỉnh sửa phong cách) -> Vòng 4 (Hoàn thiện sản phẩm cuối cùng).",
                "Rèn luyện tư duy đồng sáng tạo kiên trì, không chấp nhận ngay kết quả sơ sài ở vòng đầu tiên."
            ]
        }
    },
    {
        "stt": 7,
        "name": "Thực hành giao tiếp số văn minh",
        "definition": "Sử dụng ngôn từ lịch thiệp, tôn trọng và văn hóa khi tương tác với các hệ thống AI; xây dựng văn hóa ứng xử số lành mạnh.",
        "group_id": 1,
        "group_name": "NHÓM 1: KỸ NĂNG GIAO TIẾP & ĐIỀU KHIỂN AI",
        "domain": "NLb",
        "g1": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "1.B1.1, 1.C1.4",
            "sources": "Singapore MOE Cyber Wellness, UNESCO Ethics",
            "points": [
                "Hình thành thói quen nói lời lễ phép, rõ ràng ('Xin chào', 'Cảm ơn bạn'); không la hét, quát tháo hoặc đập phá thiết bị lớp học.",
                "Nhắc lại quy ước lớp học: Tôn trọng thiết bị thông minh cũng là tôn trọng cô giáo và các bạn cùng lớp."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.A3.MR1, 2.B1.1",
            "sources": "Google BIA (It's Cool to Be Kind)",
            "points": [
                "Nhận biết không dùng lời lẽ thô tục, xúc phạm hoặc quát mắng khi ra lệnh cho trợ lý ảo gia đình.",
                "Hiểu rằng cách mình nói chuyện với máy tính phản ánh tính cách và văn hóa của chính bản thân mình (Digital Civility)."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "3.A2.MR2, 3.B3.1",
            "sources": "UNESCO Ethics, Singapore MOE",
            "points": [
                "Thực hành gõ câu lệnh có chủ vị đầy đủ, lịch thiệp và đúng chuẩn mực ngôn ngữ học đường trên phần mềm học tập phòng máy.",
                "Thảo luận tình huống: Vì sao cần duy trì thói quen ngôn ngữ lịch sự ngay cả khi nói chuyện với một cỗ máy vô tri?"
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.A1.2, 4.B2.1",
            "sources": "Google BIA AI Literacy Guide",
            "points": [
                "Duy trì văn hóa giao tiếp tôn trọng, văn minh trên mọi ứng dụng và diễn đàn số có tích hợp AI.",
                "Tôn trọng công sức của các kỹ sư lập trình tạo ra ứng dụng; không thử thách máy bằng các câu nói khiếm nhã."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.B1.2",
            "sources": "UNICEF Requirement 2 (Child Well-being)",
            "points": [
                "Gương mẫu trong ứng xử số; chủ động nhắc nhở và ngăn chặn bạn bè trêu chọc, chửi bới AI hoặc dùng AI để phát tán ngôn từ kích động, thù ghét.",
                "Xây dựng môi trường không gian mạng học đường an toàn, tích cực và tôn trọng lẫn nhau."
            ]
        }
    },

    # ==========================================
    # NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ (8 - 17)
    # ==========================================
    {
        "stt": 8,
        "name": "Phân loại thông tin cá nhân cần bảo mật",
        "definition": "Nhận diện và giữ bí mật tuyệt đối họ tên, ngày sinh, địa chỉ nhà, trường lớp, mật khẩu, ảnh khuôn mặt trước các hệ thống AI.",
        "group_id": 2,
        "group_name": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "domain": "NLb",
        "g1": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "1.B1.1, 1.B3.1",
            "sources": "UNICEF Requirement 5, OECD Digital Safety",
            "points": [
                "Nhận biết qua tranh thẻ: Họ và tên thật, địa chỉ nhà, trường lớp học, số điện thoại của bố mẹ là những thông tin bí mật.",
                "Khẳng định quy tắc: Tuyệt đối không kể thông tin bí mật này cho đồ chơi thông minh, loa thông minh hoặc người lạ trên máy vi tính."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết qua phân loại",
            "track": "VN-CORE",
            "yccd": "2.A1.2, 2.B3.MR1",
            "sources": "Google BIA (Secure Your Secrets)",
            "points": [
                "Phân biệt rõ ràng 2 nhóm thông tin qua trò chơi thẻ bài: Thông tin chung có thể chia sẻ (món ăn ưa thích, con vật yêu, bài hát hay) vs Thông tin riêng tư cần bảo mật (mật khẩu, địa chỉ nhà, ảnh chụp trong phòng ngủ).",
                "Nhận biết nguy cơ khi đưa thông tin riêng tư lên các ứng dụng thông minh."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.4, 3.A1.MR3",
            "sources": "UNICEF Data Protection, Google BIA",
            "points": [
                "Thực hành nhận diện và gạch bỏ thông tin nhạy cảm (họ tên đầy đủ, ngày sinh, địa chỉ) trên phiếu tình huống mẫu trước khi nạp vào máy tính (khử nhận dạng sơ khai).",
                "Giải thích lý do vì sao máy tính không cần biết tên thật và số điện thoại của em để giải bài toán đố."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.B2.1, 4.B2.2",
            "sources": "QĐ 2422 (YCCĐ 4.B2.1, 4.B2.2), UNICEF Requirement 5",
            "points": [
                "Nêu được các loại thông tin cá nhân cần giữ bí mật: Mật khẩu tài khoản, số CCCD của bố mẹ, vị trí định vị thời gian thực, hình ảnh khuôn mặt mộc.",
                "Phân tích các hậu quả khôn lường khi thông tin cá nhân bị lộ hoặc bị AI lợi dụng: Bị kẻ xấu mạo danh lừa đảo, bị làm phiền bằng tin nhắn rác, mất an toàn cho gia đình."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.B2.MR1",
            "sources": "Experience AI Foundations, UNICEF Requirement 5",
            "points": [
                "Thiết lập bộ nguyên tắc bảo vệ danh tính số cho bản thân và nhóm dự án.",
                "Thực hành kỹ thuật 'Khử nhận dạng dữ liệu cá nhân' (Anonymization): Làm mờ khuôn mặt bạn bè, xoá biển số xe, ẩn tên trường lớp trên toàn bộ tập ảnh dữ liệu thu thập trước khi huấn luyện mô hình học máy."
            ]
        }
    },
    {
        "stt": 9,
        "name": "Thực hành từ chối chia sẻ dữ liệu",
        "definition": "Dứt khoát không nhập thông tin nhạy cảm vào các phần mềm hội thoại tự động hoặc trang mạng lạ khi chưa có sự đồng ý của cha mẹ/thầy cô.",
        "group_id": 2,
        "group_name": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "domain": "NLb",
        "g1": {
            "level": "Mức 1: Phản xạ hành vi",
            "track": "VN-CORE",
            "yccd": "1.B1.1",
            "sources": "UNICEF Safety, Google BIA",
            "points": [
                "Rèn luyện phản xạ hành vi tức thì: Dứt khoát khoanh tay nói 'KHÔNG' và chạy đi gọi người lớn khi robot hoặc màn hình gặng hỏi tên nhà, số điện thoại.",
                "Ghi nhớ câu thần chú an toàn: 'Máy hỏi chuyện riêng - Em liền gọi mẹ'."
            ]
        },
        "g2": {
            "level": "Mức 1: Đóng vai xử lý tình huống",
            "track": "VN-CORE",
            "yccd": "2.A1.2",
            "sources": "Google BIA (Don't Fall for Fake)",
            "points": [
                "Tham gia đóng vai xử lý tình huống: Ứng dụng trò chơi AI yêu cầu 'Nhập số điện thoại bố mẹ để nhận quà kim cương miễn phí'.",
                "Thực hành hành động dứt khoát: Nhấn nút Hủy bỏ (Cancel) và báo ngay cho bố mẹ kiểm tra."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.4, 3.A1.MR3",
            "sources": "Singapore MOE Cyber Wellness, UNICEF",
            "points": [
                "Thao tác trên phần mềm phòng máy: Bấm nút 'Từ chối' (Deny / Block) khi có thông báo trình duyệt đòi cấp quyền truy cập vị trí địa lý hoặc danh bạ không cần thiết.",
                "Giải thích nguyên tắc: Chỉ cấp quyền tối thiểu cần thiết để ứng dụng học tập hoạt động."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.B2.MR1",
            "sources": "QĐ 2422 (YCCĐ 4.B2.MR1), OECD Digital Safety",
            "points": [
                "Chủ động nhận diện và đóng ngay tab trang web/ứng dụng AI khi xuất hiện các biểu mẫu khảo sát yêu cầu thu thập thông tin gia đình bất thường.",
                "Thực hành xử lý tình huống giả định theo đúng quy trình 3 bước do giáo viên hướng dẫn."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.B2.1",
            "sources": "UNICEF Requirement 6 (Safety & Security)",
            "points": [
                "Phản biện và kiên quyết ngăn chặn các hành vi dụ dỗ đổi thông tin tài khoản, mật khẩu hoặc ảnh cá nhân lấy tài khoản game VIP có tích hợp AI.",
                "Tuyên truyền cho các bạn trong trường về quyền giữ bí mật dữ liệu cá nhân trên không gian mạng."
            ]
        }
    },
    {
        "stt": 10,
        "name": "Quản lý dấu chân kỹ thuật số",
        "definition": "Kiểm soát nội dung và lịch sử tương tác trên môi trường mạng để tránh bị thu thập, theo dõi và khai thác dữ liệu hành vi.",
        "group_id": 2,
        "group_name": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "domain": "NLb",
        "g1": None,
        "g2": None,
        "g3": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-MR",
            "yccd": "3.A1.4",
            "sources": "Common Sense Education (Digital Footprint)",
            "points": [
                "Làm quen với khái niệm 'Dấu chân kỹ thuật số' qua hình ảnh ẩn dụ: Mỗi lượt tìm kiếm, mỗi bức ảnh tải lên hay câu nói với AI đều để lại vết chân lưu mãi trên máy chủ.",
                "Hiểu rằng dấu chân số không tự biến mất khi mình tắt máy tính."
            ]
        },
        "g4": {
            "level": "Mức 1: Nhận biết / Thảo luận",
            "track": "VN-MR",
            "yccd": "4.B2.2, 4.B2.MR1",
            "sources": "OECD AILF, UNICEF Requirement 5",
            "points": [
                "Thảo luận trường hợp thực tế: Vì sao vừa tìm kiếm video về đồ chơi xếp hình thì các ứng dụng mạng xã hội và AI lập tức gợi ý toàn quảng cáo xếp hình?",
                "Nhận biết các thuật toán gợi ý của AI luôn âm thầm ghi nhận sở thích và thói quen của người dùng."
            ]
        },
        "g5": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "5.A1.2, 5.B2.1",
            "sources": "Google BIA AI Guide, Experience AI",
            "points": [
                "Thực hành kiểm tra lịch sử tìm kiếm và lịch sử hội thoại trên các nền tảng AI học tập.",
                "Thực hiện thao tác: Xóa lịch sử hội thoại (Clear chat history), tắt tính năng 'Cho phép dùng dữ liệu của tôi để huấn luyện mô hình' trong phần Cài đặt quyền riêng tư."
            ]
        }
    },
    {
        "stt": 11,
        "name": "Phát hiện nội dung giả mạo (Deepfake)",
        "definition": "Phân tích các dấu hiệu bất thường để nhận diện hình ảnh, video và âm thanh do AI làm giả mạo con người thực tế.",
        "group_id": 2,
        "group_name": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "domain": "NLb",
        "g1": None,
        "g2": {
            "level": "Mức 1: Nhận biết qua tranh ảnh",
            "track": "VN-MR",
            "yccd": "2.B1.1",
            "sources": "Google BIA (Don't Fall for Fake)",
            "points": [
                "Xem các bức ảnh so sánh: Ảnh thật của con vật vs Ảnh con vật có đặc điểm kỳ lạ do máy tính ghép (như mèo có 6 chân, chim có tai thỏ).",
                "Nhận biết máy tính có thể ghép và tạo ra những hình ảnh trông giống thật nhưng không có thật trong tự nhiên."
            ]
        },
        "g3": {
            "level": "Mức 1: Nhận biết hiện tượng",
            "track": "VN-MR",
            "yccd": "3.B2.1",
            "sources": "QĐ 2422 (YCCĐ 3.B2.1), Google BIA Guide",
            "points": [
                "Làm quen với thuật ngữ chuẩn: 'Nội dung giả mạo do AI tạo ra (deepfake)'.",
                "Nhận biết hiện tượng video ghép mặt người nổi tiếng hoặc giọng nói máy tính giả danh người quen trên mạng nhằm mục đích lừa gạt hoặc bôi nhọ danh dự."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "4.B2.2, 4.C2.1",
            "sources": "Google BIA AI Literacy Guide, UNICEF Protection",
            "points": [
                "Thực hành 'Soi 4 dấu hiệu vạch trần Deepfake' trên video bài tập: 1. Mắt không chớp tự nhiên; 2. Viền môi và viền tóc bị nhòe mờ khi chuyển động; 3. Ánh sáng và bóng đổ trên khuôn mặt không khớp với khung cảnh; 4. Giọng nói thiếu cảm xúc tự nhiên hoặc bị giật ngắt quãng.",
                "Ghi chép và khoanh tròn các điểm bất thường trên phiếu học tập."
            ]
        },
        "g5": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.B1.1",
            "sources": "OECD AILF, Experience AI Foundations",
            "points": [
                "Áp dụng quy tắc kiểm chứng tối thượng trước nghi vấn Deepfake: Tuyệt đối không chuyển tiền hoặc làm theo lời dặn trên video; thực hiện đối chứng trực tiếp với người thật bằng cuộc gọi điện thoại truyền thống hoặc câu hỏi bí mật của gia đình.",
                "Cảnh báo cho người thân trong gia đình về thủ đoạn lừa đảo tinh vi bằng video và giọng nói deepfake."
            ]
        }
    },
    {
        "stt": 12,
        "name": "Xử lý sự cố an toàn thông tin",
        "definition": "Dừng ngay ứng dụng, ngắt kết nối và báo cáo kịp thời cho cha mẹ/thầy cô khi gặp nguy cơ mất an toàn hoặc nội dung độc hại.",
        "group_id": 2,
        "group_name": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "domain": "NLb",
        "g1": {
            "level": "Mức 1: Phản xạ tức thì",
            "track": "VN-CORE",
            "yccd": "1.B1.1",
            "sources": "UNICEF Child Well-being, Singapore MOE",
            "points": [
                "Ngừng bấm máy ngay lập tức và giơ tay báo cáo cô giáo khi màn hình xuất hiện hình ảnh bạo lực, kinh dị, chữ lạ đáng sợ hoặc khi ứng dụng phát ra âm thanh lạ.",
                "Tuyệt đối không tò mò bấm tiếp vào các liên kết lạ nhấp nháy trên màn hình."
            ]
        },
        "g2": {
            "level": "Mức 1: Phản xạ tức thì",
            "track": "VN-CORE",
            "yccd": "2.A1.2",
            "sources": "Google BIA (When in Doubt, Talk It Out)",
            "points": [
                "Thực hành phản xạ: Tắt ngay màn hình thiết bị và kể lại trung thực cho bố mẹ/thầy cô khi nhận tin nhắn đe dọa, đòi tiền hoặc yêu cầu thực hiện hành vi xấu từ ứng dụng thông minh.",
                "Hiểu rằng báo cáo người lớn là hành động dũng cảm và thông minh, không bị phạt."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.4, 3.A1.MR3",
            "sources": "Google BIA, Singapore MOE Cyber Wellness",
            "points": [
                "Vận hành thuần thục quy trình an toàn 3 bước: Bước 1: Dừng thao tác -> Bước 2: Tắt kết nối mạng / Đóng tab phần mềm -> Bước 3: Báo cáo ngay cho người lớn tin cậy (thầy cô, bố mẹ).",
                "Diễn tập xử lý tình huống mất an toàn số trong giờ học Tin học."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.B2.MR1",
            "sources": "QĐ 2422 (YCCĐ 4.B2.MR1), OECD Digital Safety",
            "points": [
                "Biết chụp ảnh màn hình (Screenshot) để lưu giữ bằng chứng vi phạm của trang web/tài khoản lừa đảo.",
                "Ghi nhớ địa chỉ URL lạ và điền phiếu báo cáo sự cố an toàn thông tin cho giáo viên quản trị phòng máy."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.B2.1",
            "sources": "Experience AI, UNICEF Requirement 6",
            "points": [
                "Chủ động thực hiện các biện pháp khẩn cấp khi tài khoản bị lộ: Đổi mật khẩu ngay lập tức, đăng xuất khỏi tất cả các thiết bị lạ.",
                "Hướng dẫn và hỗ trợ bạn cùng lớp các bước xử lý khi phát hiện dữ liệu nhóm bị kẻ xấu chèn mã độc hoặc hình ảnh rác."
            ]
        }
    },
    {
        "stt": 13,
        "name": "Thực hành nguyên tắc đồng thuận",
        "definition": "Xác lập ranh giới dữ liệu cá nhân; hỏi xin phép và chỉ sử dụng hình ảnh, âm thanh, bài viết của người khác khi có sự đồng ý.",
        "group_id": 2,
        "group_name": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "domain": "NLb",
        "g1": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "1.B1.1",
            "sources": "Singapore MOE Cyber Wellness, UNESCO Ethics",
            "points": [
                "Hỏi xin phép bạn rõ ràng trước khi chạm tay vào đồ chơi thông minh hoặc bức tranh vẽ của bạn trong lớp học.",
                "Tôn trọng đồ dùng của bạn, chỉ chơi chung khi được bạn vui vẻ đồng ý."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết và thực hành lời nói",
            "track": "VN-CORE",
            "yccd": "2.B3.MR1, 2.B3.MR2",
            "sources": "QĐ 2422 (YCCĐ 2.B3.MR2), UNICEF Requirement 1",
            "points": [
                "Nhận biết quy định: Muốn dùng thứ của người khác (đồ dùng, tranh vẽ, ảnh chụp) thì phải hỏi và được người đó đồng ý.",
                "Thực hành nói câu xin phép lịch sự: 'Bạn có đồng ý cho mình chụp bức tranh này để làm bài tập không?' trước khi chụp ảnh."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "3.A2.MR2, 3.B3.1",
            "sources": "Experience AI, UNESCO Ethics",
            "points": [
                "Thực hành quy trình xin phép đồng thuận dữ liệu mẫu: Trước khi chụp ảnh hoặc ghi âm giọng nói của bạn để nạp dữ liệu cho AI, phải đưa 'Phiếu xin phép mini' để bạn ký đồng ý.",
                "Nếu bạn từ chối, vui vẻ chấp nhận và không được chụp lén."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.B2.1",
            "sources": "OECD AILF, Singapore MOE NDLP",
            "points": [
                "Tôn trọng ranh giới riêng tư số: Chỉ được tải dữ liệu, hình ảnh hoạt động nhóm lên mạng Internet khi tất cả các thành viên trong nhóm và giáo viên đều đồng thuận.",
                "Lập tức gỡ ảnh xuống nếu có một bạn trong nhóm cảm thấy không thoải mái."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.B2.MR1",
            "sources": "UNICEF Guidance on AI for Children (Req 5)",
            "points": [
                "Hiểu rằng quyền đồng thuận dữ liệu cá nhân là nguyên tắc pháp lý bất khả xâm phạm (theo Luật Trẻ em và Nghị định bảo vệ dữ liệu cá nhân).",
                "Thiết lập biên bản đồng thuận thu thập dữ liệu chính thức trong hồ sơ dự án AI của lớp."
            ]
        }
    },
    {
        "stt": 14,
        "name": "Minh bạch tác quyền AI (Attribution)",
        "definition": "Dán nhãn ghi rõ 'Tạo bởi AI' đối với sản phẩm tranh ảnh, văn bản do máy tạo ra; không mạo nhận là tác phẩm do bản thân tự sáng tác.",
        "group_id": 2,
        "group_name": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "domain": "NLb",
        "g1": None,
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-MR",
            "yccd": "2.B3.2",
            "sources": "QĐ 2422 (YCCĐ 2.B3.2), UNESCO Attribution",
            "points": [
                "Nêu được ví dụ: Bức tranh do em tự vẽ bằng sáp màu là của riêng em; bức tranh do máy tính gợi ý vẽ thì phải nói thật với cô giáo là máy tính tạo ra.",
                "Hình thành đức tính trung thực: Không nhận sản phẩm của máy là do mình tự làm."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "3.A2.MR2, 3.B2.1",
            "sources": "Common Sense Education (AI Attribution)",
            "points": [
                "Thực hành ghi chú thích nguồn gốc minh bạch ở góc dưới bài làm: 'Ý tưởng bài thơ được gợi ý từ phần mềm AI' hoặc 'Hình minh họa tạo bởi công cụ AutoDraw'.",
                "Hiểu rằng ghi rõ nguồn gốc AI là thể hiện sự hiểu biết văn minh và trung thực."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.A1.2, 4.C2.1",
            "sources": "UNESCO Ethics, OECD AILF",
            "points": [
                "Dán nhãn chuẩn hóa 'Tạo bởi AI (AI-generated)' cho mọi sản phẩm tranh ảnh, áp phích hoặc đoạn văn do công cụ AI sinh ra.",
                "Phân biệt rõ: Tác phẩm do con người hoàn toàn tự sáng tác vs Tác phẩm có sự trợ giúp của AI."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.A2.1",
            "sources": "UNESCO Academic Integrity in GenAI, Experience AI",
            "points": [
                "Báo cáo minh bạch cơ cấu đóng góp trong bài thu hoạch dự án: Phần nào do nhóm học sinh tự nghiên cứu, tư duy, viết lời; phần nào do AI hỗ trợ dịch thuật, gợi ý dữ liệu.",
                "Tuyên thệ không đạo văn (Plagiarism) và tôn trọng quyền sở hữu trí tuệ."
            ]
        }
    },
    {
        "stt": 15,
        "name": "Thực hành liêm chính học thuật",
        "definition": "Tự giác làm bài tập độc lập, không sử dụng công cụ AI làm thay toàn bộ để gian lận điểm số hay thi cử; bảo vệ năng lực thực chất.",
        "group_id": 2,
        "group_name": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "domain": "NLb",
        "g1": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "1.B1.1, 1.B3.1",
            "sources": "UNESCO Ethics, Singapore MOE",
            "points": [
                "Bé tự tay nắn nót viết từng nét chữ và tự làm bài toán của mình, không nhờ máy tính hay người lớn làm hộ để cô giáo chấm điểm thực chất.",
                "Nhận biết: Tự mình cố gắng thì mình mới mau tiến bộ và thông minh hơn."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.A1.2, 2.B3.2",
            "sources": "QĐ 2422 (YCCĐ 2.A1.2)",
            "points": [
                "Giải thích được lý do vì sao không nên để máy tính làm hết bài tập thay cho mình: Nếu máy làm hộ, não mình sẽ lười suy nghĩ, không học được kiến thức mới.",
                "Cam kết trung thực trong các bài kiểm tra định kỳ."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.3, 3.A1.MR2",
            "sources": "QĐ 2422 (YCCĐ 3.A1.3, 3.A1.MR2), OECD Agency",
            "points": [
                "Ký bản cam kết liêm chính học tập đầu năm: Tự mình làm bài tập về nhà; chỉ mở ứng dụng AI để kiểm tra lại sau khi đã tự suy nghĩ và viết lời giải ra vở.",
                "Nhận diện hành vi gian lận: Sao chép nguyên văn đáp án của AI vào vở bài tập."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.A1.2, 4.A1.MR1",
            "sources": "Common Sense Education, Google BIA",
            "points": [
                "Kiên quyết từ chối sao chép nguyên xi văn bản của AI; nếu có tham khảo ý tưởng của AI, phải tự diễn đạt lại bằng vốn từ và văn phong riêng của bản thân.",
                "Tự giác trung thực trong mọi bài tập thực hành trên phòng máy vi tính."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.A2.1",
            "sources": "UNESCO Ethics, OECD Future of Skills",
            "points": [
                "Tự hào về năng lực sáng tạo và trí tuệ thực chất của bản thân; kiên quyết tẩy chay mọi hành vi sử dụng AI để gian lận trong kiểm tra, đánh giá.",
                "Khẳng định triết lý học đường: Điểm số chỉ có giá trị khi phản ánh đúng năng lực tư duy thật sự của học sinh."
            ]
        }
    },
    {
        "stt": 16,
        "name": "Kiểm soát hành vi không gây hại",
        "definition": "Không sử dụng các công cụ AI để chế ảnh bôi nhọ, nhại giọng trêu chọc, bắt nạt trực tuyến hoặc làm tổn thương người khác.",
        "group_id": 2,
        "group_name": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "domain": "NLb",
        "g1": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "1.B1.1, 1.B3.1",
            "sources": "QĐ 2422 (YCCĐ 1.B1.1, 1.B3.1), UNESCO 'Do No Harm'",
            "points": [
                "Nhắc lại và chấp hành nghiêm quy tắc đạo đức cốt lõi: Tuyệt đối không dùng máy móc thông minh để làm hại hoặc làm đau người khác.",
                "Không dùng loa phát tiếng quá to làm phiền ông bà; không dùng đồ chơi robot để hù dọa các bạn nhỏ."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.B1.1",
            "sources": "Singapore MOE Cyber Wellness, UNICEF Well-being",
            "points": [
                "Nhận biết: Không được dùng các ứng dụng chỉnh ảnh để kéo méo mặt bạn, biến bạn thành hình thù xấu xí để trêu chọc làm bạn khóc.",
                "Rèn luyện lòng trắc ẩn: Biết nghĩ đến cảm xúc buồn tủi của bạn bè trước khi bấm chia sẻ."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.B3.1",
            "sources": "QĐ 2422 (YCCĐ 3.B3.1), CASEL Social Awareness",
            "points": [
                "Thảo luận chủ đề: 'Nụ cười của em có làm bạn tổn thương không?'. Nhận diện ranh giới giữa đùa vui lành mạnh và hành vi quấy rối bằng công nghệ.",
                "Cam kết không tạo ra hoặc sử dụng AI cho các mục đích xấu, trêu chọc bạn bè."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.A1.2, 4.B2.1",
            "sources": "Google BIA (It's Cool to Be Kind), UNICEF Req 6",
            "points": [
                "Nhận diện các biểu hiện của hành vi bắt nạt qua mạng (Cyberbullying) có sử dụng công nghệ AI (chế ảnh meme bêu xấu, nhại giọng giễu cợt).",
                "Dứt khoát không like, không bình luận xúc phạm và không lan truyền nội dung độc hại; báo ngay cho giáo viên chủ nhiệm."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.B1.2",
            "sources": "UNESCO Ethics of AI, UNICEF Requirement 2",
            "points": [
                "Ký cam kết văn hóa số: 'Sử dụng công nghệ AI vì điều tốt đẹp - Tuyệt đối không gây hại cho con người và xã hội'.",
                "Tham gia bảo vệ các bạn học sinh yếu thế trong trường khỏi nguy cơ bị bạo lực mạng."
            ]
        }
    },
    {
        "stt": 17,
        "name": "Xây dựng giải pháp AI bao trùm",
        "definition": "Hướng ý tưởng ứng dụng AI vào việc phục vụ bình đẳng xã hội, hỗ trợ người khuyết tật, người già và các nhóm yếu thế.",
        "group_id": 2,
        "group_name": "NHÓM 2: KỸ NĂNG AN TOÀN SỐ & ĐẠO ĐỨC CÔNG NGHỆ",
        "domain": "NLa",
        "g1": {
            "level": "Mức 1: Cảm thụ / Nghe chuyện",
            "track": "VN-MR",
            "yccd": "1.A2.MR1, 1.B3.2",
            "sources": "UNICEF Requirement 3 (Inclusion)",
            "points": [
                "Xem tranh và nghe câu chuyện xúc động về chú chó robot dẫn đường thông minh giúp người khiếm thị qua ngã tư an toàn.",
                "Cảm nhận vẻ đẹp nhân văn: Máy móc thông minh được tạo ra để chở che và giúp đỡ những người gặp khó khăn."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-MR",
            "yccd": "2.A2.2, 2.A2.MR3",
            "sources": "QĐ 2422 (YCCĐ 2.A2.2), UNESCO Social Good",
            "points": [
                "Kể tên những người trong gia đình và xã hội mà AI có thể giúp đỡ: Robot đọc sách to cho ông bà mắt mờ, ứng dụng nhận diện giọng nói cho người không thể gõ phím.",
                "Hiểu mục tiêu của AI trong gia đình là chăm sóc mọi thành viên an toàn và hạnh phúc hơn."
            ]
        },
        "g3": {
            "level": "Mức 1: Quan sát / Thảo luận",
            "track": "VN-MR",
            "yccd": "3.A2.3, 3.A2.MR3",
            "sources": "QĐ 2422 (YCCĐ 3.A2.3), OECD Inclusive Education",
            "points": [
                "Tìm hiểu công cụ AI hỗ trợ giáo dục hòa nhập: Ứng dụng chuyển giọng nói thành văn bản cho học sinh khiếm thính trong lớp học; công cụ đọc màn hình cho bạn khiếm thị.",
                "Nhận biết AI giúp đảm bảo quyền học tập bình đẳng cho tất cả mọi học sinh."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "4.A2.2, 4.D1.MR1",
            "sources": "QĐ 2422 (YCCĐ 4.A2.2), UNICEF Requirement 3",
            "points": [
                "Thực hành thiết kế poster ý tưởng: 'Trợ lý AI học tiếng Việt cho các bạn nhỏ vùng cao' hoặc 'Cây gậy thông minh cảnh báo vật cản cho người khiếm thị'.",
                "Trình bày giải pháp trước lớp, nêu bật tính bao trùm và giá trị nhân ái của công nghệ."
            ]
        },
        "g5": {
            "level": "Mức 3: Vận dụng / Dự án",
            "track": "VN-MR",
            "yccd": "5.A2.2, 5.A2.3, 5.A3.MR1",
            "sources": "UNESCO AI for SDGs, OECD Compass 2030",
            "points": [
                "Xây dựng đề án nhóm: Đề xuất giải pháp AI phục vụ lợi ích cộng đồng (AI phân loại rác bảo vệ môi trường biển, AI nhận diện cử chỉ tay hỗ trợ người câm điếc giao tiếp).",
                "Đánh giá tính bao trùm của giải pháp: Đảm bảo công nghệ dễ dùng, chi phí thấp và phục vụ bình đẳng mọi tầng lớp nhân dân."
            ]
        }
    },

    # ==========================================
    # NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG (18 - 26)
    # ==========================================
    {
        "stt": 18,
        "name": "Phân biệt cảm xúc người và máy",
        "definition": "Nhận diện cảm xúc chân thực của con người và phân biệt rạch ròi với các tín hiệu mô phỏng do AI lập trình; chống nhân hóa máy móc.",
        "group_id": 3,
        "group_name": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "domain": "NLa",
        "g1": {
            "level": "Mức 1: Nhận biết cốt lõi",
            "track": "VN-CORE",
            "yccd": "1.A1.1, 1.A1.2, 1.A1.3, 1.A1.4, 1.A2.1, 1.A2.MR1",
            "sources": "QĐ 2422 (YCCĐ 1.A1.1-4), UNESCO, Singapore MOE",
            "points": [
                "Nêu ví dụ về cảm xúc quen thuộc của bản thân (vui, buồn, sợ hãi) và nhận ra con người có cảm xúc thật từ trái tim, máy móc thì không.",
                "Nhận biết máy thông minh chỉ bắt chước hoặc nhận diện nét mặt; hình mặt cười, giọng nói vui vẻ của loa thông minh là do con người lập trình từ trước để tạo cảm giác gần gũi."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.A1.4",
            "sources": "Singapore MOE (Avoiding Anthropomorphism)",
            "points": [
                "Nhận biết giọng nói ngọt ngào, ân cần của trợ lý ảo chỉ là sóng âm toán học mô phỏng, máy móc là thiết bị nhân tạo, không biết buồn vui, không biết đau đớn.",
                "Tránh nhân hóa công nghệ (không coi robot là con người có tâm hồn)."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.3",
            "sources": "OECD Digital Well-being, UNICEF Req 2",
            "points": [
                "Phân tích tình huống: Tại sao robot hỏi thăm ân cần nhưng không thể thay thế vòng tay ấm áp của mẹ khi em ốm, không thể thay thế tình bạn thực tế ngoài đời?",
                "Khẳng định giá trị duy nhất của tình cảm gia đình và tình bạn con người."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.A1.2, 4.A2.1",
            "sources": "UNESCO Human Agency, OECD AILF",
            "points": [
                "Chống nhân hóa AI: Kiên quyết khẳng định máy tính là công cụ vô tri, không có ý thức, không có lương tri hay đạo đức tự thân; chỉ có con người mới có trách nhiệm đạo đức.",
                "Cảnh báo nguy cơ rơi vào bẫy cảm xúc giả tạo khi tâm sự quá mức với Chatbot."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A2.1, 5.A2.MR1",
            "sources": "QĐ 2422 (YCCĐ 5.A2.MR1), UNESCO Human Flourishing",
            "points": [
                "Biện luận sự khác biệt bản chất: Trí tuệ sinh học của con người gắn liền với cảm xúc, lòng trắc ẩn, trực giác và trải nghiệm sống; Trí tuệ nhân tạo chỉ là thuật toán tính toán thống kê dựa trên dữ liệu số.",
                "Thuyết trình khẳng định vị thế trung tâm và phẩm giá không thể thay thế của con người."
            ]
        }
    },
    {
        "stt": 19,
        "name": "Phân biệt thiết bị cơ học và thiết bị AI",
        "definition": "Chỉ ra sự khác biệt giữa đồ dùng cơ học thông thường (bấm nút cơ) và thiết bị thông minh ứng dụng AI (có cảm biến tự động nhận biết).",
        "group_id": 3,
        "group_name": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "domain": "NLc",
        "g1": {
            "level": "Mức 1: Nhận biết trực quan",
            "track": "VN-CORE",
            "yccd": "1.C1.1",
            "sources": "QĐ 2422 (YCCĐ 1.C1.1), AI4K12 Big Idea 1",
            "points": [
                "Chỉ ra sự khác biệt đơn giản: Quạt máy thông thường phải bấm nút cơ mới quay; quạt thông minh có 'mắt cảm biến' tự quay khi nhận biết có người lại gần.",
                "Nhận biết thiết bị thông minh có khả năng đón nhận tín hiệu xung quanh."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.A2.1",
            "sources": "AI4K12 (Big Idea 1), Singapore MOE Computing",
            "points": [
                "So sánh qua tranh ảnh thực tế: Thùng rác đạp chân cơ học vs Thùng rác cảm ứng tự mở nắp; Chổi quét nhà thông thường vs Robot hút bụi tự né bàn ghế.",
                "Nhận biết đồ dùng AI có bộ phận cảm biến và xử lý thông tin tự động."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A2.1, 3.C5.1",
            "sources": "AI4K12 (Big Idea 1), UNESCO Techniques",
            "points": [
                "Lập bảng so sánh 5 cặp đồ dùng thông thường và đồ dùng thông minh tương ứng trong trường học và gia đình.",
                "Chỉ ra thành phần cảm biến (Input) và bộ điều khiển (Process) tạo nên sự thông minh vượt trội của thiết bị AI."
            ]
        },
        "g4": None,
        "g5": None
    },
    {
        "stt": 20,
        "name": "Phân loại thiết bị đơn nhiệm và đa nhiệm",
        "definition": "Phân biệt đồ dùng chỉ làm được một việc chuyên dụng (đơn nhiệm) và thiết bị thông minh làm được nhiều việc khác nhau (đa nhiệm).",
        "group_id": 3,
        "group_name": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "domain": "NLd",
        "g1": {
            "level": "Mức 1: Nhận biết qua phân loại",
            "track": "VN-CORE",
            "yccd": "1.D2.1, 1.D2.2",
            "sources": "QĐ 2422 (YCCĐ 1.D2.1-2), Singapore MOE Systems",
            "points": [
                "Nhận biết qua ví dụ: Cân điện tử chỉ làm một việc là đo cân nặng; Điện thoại thông minh làm được nhiều việc: vừa nghe gọi, chụp ảnh, xem giờ, phát nhạc.",
                "Thực hành xếp thẻ tranh các đồ dùng thông minh vào 2 rổ: Nhóm chỉ làm 1 việc và Nhóm làm được nhiều việc khác nhau."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.A2.1",
            "sources": "AI4K12 (Big Idea 5)",
            "points": [
                "Xếp các thiết bị trong gia đình vào 2 nhóm: Thiết bị chuyên dụng (máy đo huyết áp điện tử, nhiệt kế điện tử) vs Thiết bị đa năng (máy tính bảng, loa thông minh điều khiển nhà).",
                "Nói được công dụng chính của từng thiết bị."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "3.A2.1",
            "sources": "Singapore MOE Computational Thinking",
            "points": [
                "Phân tích ưu điểm và nhược điểm: Thiết bị chuyên dụng hoạt động rất chính xác và bền bỉ vs Thiết bị đa nhiệm tiện lợi nhưng dễ gây mất tập trung.",
                "Vẽ sơ đồ tư duy phân loại các thiết bị thông minh trong trường học."
            ]
        },
        "g4": None,
        "g5": None
    },
    {
        "stt": 21,
        "name": "So sánh phương thức học tập",
        "definition": "So sánh cách con người học qua trải nghiệm sống và hiểu bản chất vs cách máy học bằng việc tính toán thống kê trên dữ liệu số.",
        "group_id": 3,
        "group_name": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "domain": "NLc",
        "g1": {
            "level": "Mức 1: Nhận biết qua ví dụ",
            "track": "VN-MR",
            "yccd": "1.D1.1, 1.D1.MR1",
            "sources": "AI4K12 (Big Idea 3 - Learning from Examples)",
            "points": [
                "Em học chữ và nhận biết con vật qua chơi đùa, trải nghiệm thật và nghe cô kể chuyện; máy tính học bằng cách con người cho xem nhiều bức tranh mẫu.",
                "Hiểu rằng máy tính cần con người chuẩn bị tranh mẫu thì mới học được."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết đối chiếu",
            "track": "VN-CORE",
            "yccd": "2.C1.MR1",
            "sources": "QĐ 2422 (YCCĐ 2.C1.MR1), UNESCO Human vs Machine",
            "points": [
                "So sánh: Con người học qua nhìn, chơi đùa và trải nghiệm thật trong cuộc sống (người ngã biết đau để cẩn thận); còn AI học bằng cách xem qua nhiều tranh ảnh, âm thanh mẫu do con người nạp vào.",
                "Nhận biết sự khác biệt giữa trải nghiệm sinh học và dữ liệu máy tính."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.C5.2",
            "sources": "AI4K12 Big Idea 3, Experience AI",
            "points": [
                "Lập bảng đối chiếu chi tiết: Não người học bằng cách hiểu ý nghĩa bản chất và liên tưởng phong phú vs Học máy (Machine Learning) học bằng cách tìm kiếm quy luật toán học trên tập dữ liệu số.",
                "Khẳng định đặc điểm chính của học máy: 'Học trên dữ liệu'."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.D1.1",
            "sources": "Experience AI (Discovering AI)",
            "points": [
                "Phân tích trường hợp kinh điển: Em bé chỉ cần nhìn thấy con voi 1 lần ở vườn thú là nhận ra mọi con voi khác; trong khi mô hình AI cần nạp hàng ngàn bức ảnh con voi ở đủ góc chụp, màu sắc, ánh sáng mới nhận ra.",
                "Giải thích nguyên nhân: Não người có khả năng khái quát hóa vượt trội."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A2.MR1, 5.C5.2",
            "sources": "UNESCO Human-Centred Mindset, OECD AILF",
            "points": [
                "Thuyết trình chuyên đề: 'Trí tuệ con người vs Trí tuệ nhân tạo'. Khẳng định máy móc chỉ sao chép mẫu dữ liệu quá khứ, không có khả năng sáng tạo đột phá hay linh cảm như bộ não con người.",
                "Cổ vũ niềm tin vào năng lực học tập suốt đời của bản thân."
            ]
        }
    },
    {
        "stt": 22,
        "name": "Phân tích nguyên nhân sai số của AI",
        "definition": "Mổ xẻ các lý do kỹ thuật khiến AI đưa ra kết quả sai lệch: hình ảnh bị mờ, vật bị che khuất, thiếu dữ liệu góc chụp, hai đối tượng quá giống nhau.",
        "group_id": 3,
        "group_name": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "domain": "NLc",
        "g1": {
            "level": "Mức 1: Quan sát trực quan",
            "track": "VN-CORE",
            "yccd": "1.C1.MR1, 1.D1.MR1",
            "sources": "AI4K12 (Big Idea 1 - Perception Limitations)",
            "points": [
                "Quan sát camera AI demo nhận nhầm quả bóng màu cam thành quả cam ăn được vì cùng hình tròn và màu cam.",
                "Nhận ra máy tính nhìn bề ngoài màu sắc, không ngửi được mùi hương hay nếm được vị như con người nên dễ đoán sai."
            ]
        },
        "g2": {
            "level": "Mức 1: Quan sát / So sánh",
            "track": "VN-CORE",
            "yccd": "2.C3.2, 2.C3.MR1, 2.D2.2",
            "sources": "QĐ 2422 (YCCĐ 2.C3.2, 2.C3.MR1, 2.D2.2)",
            "points": [
                "Nêu được AI có thể phân loại sai khi đồ vật nhìn quá giống nhau hoặc khi đồ vật bị che khuất một phần (Occlusion).",
                "So sánh: Con người tận dụng kinh nghiệm và ngữ cảnh thực tế để nhận ra, còn AI có thể gặp khó khăn hoặc phân loại nhầm."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A3.1, 3.D2.1",
            "sources": "QĐ 2422 (YCCĐ 3.A3.1), Experience AI",
            "points": [
                "Thử nghiệm đưa đồ vật vào webcam ở các góc chụp khó (ngược sáng, bị ngón tay che khuất, xoay nghiêng) xem mô hình Teachable Machine dự đoán nhầm.",
                "Chỉ ra nguyên nhân: Dữ liệu huấn luyện ban đầu bị thiếu góc chụp đó."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.D2.1",
            "sources": "Experience AI (Discovering AI 8-12)",
            "points": [
                "Phân loại 3 nhóm nguyên nhân sai số cốt lõi: 1. Dữ liệu đầu vào mờ/nhiễu; 2. Tập mẫu huấn luyện bị lệch, thiếu đa dạng; 3. Hai đối tượng có đặc trưng thị giác bên ngoài quá tương đồng.",
                "Lập bảng phân tích lỗi dự đoán của mô hình."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.C5.MR3, 5.D2.1",
            "sources": "QĐ 2422 (YCCĐ 5.C5.MR3), Experience AI Foundations",
            "points": [
                "Kiểm tra kết quả mô hình đưa ra, lập danh sách các trường hợp nhận diện sai hoặc độ tin cậy thấp.",
                "Đề xuất phương án kỹ thuật khắc phục triệt để: Chụp bổ sung ảnh góc nghiêng, cải thiện ánh sáng, cân bằng số lượng mẫu giữa các nhãn dữ liệu."
            ]
        }
    },
    {
        "stt": 23,
        "name": "Kiểm chứng thông tin (Chống ảo giác AI)",
        "definition": "Giữ thái độ nghi ngờ lành mạnh trước phản hồi của AI; nhận diện hiện tượng ảo giác AI và chủ động đối chiếu chéo với các nguồn tin cậy.",
        "group_id": 3,
        "group_name": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "domain": "NLb",
        "g1": None,
        "g2": {
            "level": "Mức 1: Nhận thức ban đầu",
            "track": "VN-MR",
            "yccd": "2.A1.4",
            "sources": "QĐ 2422 (YCCĐ 2.A1.4), Google BIA",
            "points": [
                "Biết rằng máy móc thông minh cũng có lúc nói sai, dịch nhầm hoặc trả lời nhầm lẫn; không được tin tưởng 100% vào mọi điều máy nói.",
                "Khi thấy thông tin lạ, luôn hỏi lại bố mẹ và thầy cô."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A3.1, 3.A3.2",
            "sources": "QĐ 2422 (YCCĐ 3.A3.1, 3.A3.2), Singapore MOE Critical",
            "points": [
                "Nêu ví dụ AI có thể sai (dịch sai ngữ nghĩa, nhận diện nhầm hình ảnh).",
                "Thực hành kiểm tra lại kết quả do AI cung cấp bằng cách mở sách giáo khoa trang tương ứng hoặc hỏi ý kiến thầy cô; không được tin ngay."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.A1.2, 4.A1.MR1",
            "sources": "Google BIA AI Literacy Guide",
            "points": [
                "Thực hiện quy tắc kiểm chứng 2 nguồn (Cross-checking): Luôn đối chiếu thông tin AI đưa ra với ít nhất 1 nguồn tài liệu chính thống (sách thư viện, từ điển, cổng thông tin giáo dục).",
                "Gạch chân các chi tiết nghi vấn trong câu trả lời của AI để thẩm định."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.A2.1",
            "sources": "OECD AILF, Experience AI Foundations",
            "points": [
                "Nhận diện và định nghĩa hiện tượng 'Ảo giác AI (hallucination)': AI tự tạo ra thông tin bịa đặt, sai sự thật nhưng trình bày với văn phong cực kỳ tự tin và thuyết phục.",
                "Thực hành phát hiện và lập biên bản 'Bắt lỗi ảo giác' đối với các câu trả lời sai lệch của AI về lịch sử hoặc địa lý Việt Nam."
            ]
        }
    },
    {
        "stt": 24,
        "name": "Phát hiện thiên lệch thuật toán (Bias)",
        "definition": "Nhận diện khi kết quả AI đưa ra bị thiếu công bằng do tập dữ liệu huấn luyện bị lệch mẫu, thiên vị một nhóm đối tượng.",
        "group_id": 3,
        "group_name": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "domain": "NLb",
        "g1": None,
        "g2": {
            "level": "Mức 1: Quan sát trực quan",
            "track": "VN-CORE",
            "yccd": "2.B1.1, 2.B1.MR1, 2.B1.MR2",
            "sources": "QĐ 2422 (YCCĐ 2.B1.1, 2.B1.MR1-2), Experience AI",
            "points": [
                "Nhận biết AI có thể thiên kiến (thiên lệch), tức là đối xử không công bằng với một số nhóm người.",
                "Nêu ví dụ: Máy nhận diện giọng nói chỉ hiểu giọng bạn miền Bắc mà chưa hiểu giọng bạn miền Trung/miền Nam.",
                "Giải thích: Do con người chỉ nạp dữ liệu một nhóm người thì máy sẽ nhận diện kém những người khác ('Bias in, bias out')."
            ]
        },
        "g3": {
            "level": "Mức 1: Quan sát / Nhận xét",
            "track": "VN-CORE",
            "yccd": "3.B3.MR1",
            "sources": "QĐ 2422 (YCCĐ 3.B3.MR1), UNICEF Requirement 4",
            "points": [
                "Giải thích: Con người cần cung cấp dữ liệu đúng và đa dạng để AI hoạt động chính xác và công bằng.",
                "Nhận biết: Nếu dữ liệu mẫu chỉ toàn quả chuối vàng thì máy sẽ không thể nhận ra quả chuối xanh."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.A2.2, 4.D2.1",
            "sources": "Experience AI (Lesson: Bias in, bias out)",
            "points": [
                "Làm thí nghiệm 'Thiên lệch dữ liệu' trên Teachable Machine: Cố tình nạp 20 ảnh tay người lớn và chỉ 1 ảnh tay trẻ em -> kiểm thử thấy máy không nhận ra tay học sinh.",
                "Rút ra kết luận: Mô hình phản ánh chính xác sự thiên vị có trong tập dữ liệu đầu vào."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.B1.1, 5.B1.2, 5.B2.1",
            "sources": "QĐ 2422 (YCCĐ 5.B1.1-2, 5.B2.1), UNICEF Requirement 4",
            "points": [
                "Nêu ví dụ về sự công bằng/không công bằng của AI trong đời sống; giải thích AI cần phục vụ con người công bằng, không phân biệt đối xử.",
                "Đề xuất các biện pháp giúp AI hoạt động công bằng hơn: Sử dụng dữ liệu đa dạng giới tính, độ tuổi, màu da, vùng miền; liên tục kiểm định thiên lệch."
            ]
        }
    },
    {
        "stt": 25,
        "name": "Đánh giá điểm số tin cậy mô hình",
        "definition": "Đọc hiểu chỉ số tin cậy (Confidence Score / Probability) để thẩm định mức độ chắc chắn của mô hình trước khi đưa ra quyết định.",
        "group_id": 3,
        "group_name": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "domain": "NLc",
        "g1": None,
        "g2": None,
        "g3": {
            "level": "Mức 1: Quan sát thanh đo",
            "track": "VN-MR",
            "yccd": "3.C5.4, 3.C5.MR2",
            "sources": "Experience AI Discovering AI",
            "points": [
                "Quan sát thanh đo xác suất trên màn hình demo: Thanh dài màu xanh = Máy rất tự tin và chắc chắn; Thanh ngắn rung rinh = Máy đang phân vân, không chắc chắn.",
                "Nhận biết máy tính đưa ra kết quả dưới dạng dự đoán xác suất."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "4.C5.MR1, 4.D2.1",
            "sources": "Teachable Machine, Google ADS",
            "points": [
                "Đọc hiểu chỉ số phần trăm trên phần mềm: 85% máy đoán là quả táo, 15% nghi ngờ là quả cà chua.",
                "Thử nghiệm đưa vật mẫu rõ nét (độ tin cậy tăng lên 98%) vs vật mẫu mờ tối (độ tin cậy giảm xuống 50%) để cảm nhận sự biến thiên."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.B3.1, 5.C5.MR3",
            "sources": "Experience AI Foundations, OECD AILF",
            "points": [
                "Thiết lập ngưỡng an toàn (Confidence Threshold): Chỉ chấp nhận quyết định tự động của mô hình khi độ tin cậy đạt từ 85% trở lên; nếu dưới 85%, hệ thống phải báo động để con người kiểm tra trực tiếp.",
                "Giải thích lý do không thể tin cậy vào kết quả khi điểm số tin cậy quá thấp."
            ]
        }
    },
    {
        "stt": 26,
        "name": "Đánh giá tính minh bạch của AI",
        "definition": "Giải thích lý do con người cần hiểu cách AI đưa ra quyết định để đảm bảo an toàn, trách nhiệm giải trình và niềm tin xã hội.",
        "group_id": 3,
        "group_name": "NHÓM 3: KỸ NĂNG TƯ DUY PHẢN BIỆN & KIỂM CHỨNG",
        "domain": "NLb",
        "g1": None,
        "g2": None,
        "g3": {
            "level": "Mức 1: Nhận thức",
            "track": "VN-MR",
            "yccd": "3.A1.5",
            "sources": "UNICEF Requirement 7 (Explainability)",
            "points": [
                "Nhận thức rằng con người cần biết lý do vì sao máy tính lại đưa ra kết quả đó thay vì chỉ chấp nhận thụ động.",
                "Đặt câu hỏi: 'Tại sao máy lại nghĩ đây là quả táo?'."
            ]
        },
        "g4": {
            "level": "Mức 1: Thảo luận",
            "track": "VN-MR",
            "yccd": "4.A1.2, 4.D2.1",
            "sources": "UNICEF Transparency, OECD AILF",
            "points": [
                "Thảo luận tình huống: Ứng dụng AI chấm điểm bài thi của học sinh phải giải thích rõ tiêu chí chấm (lỗi chính tả ở đâu, thiếu ý gì) thì học sinh mới tin phục.",
                "Nhận biết nguy cơ nếu hệ thống AI hoạt động như một 'hộp đen' bí ẩn không ai hiểu được."
            ]
        },
        "g5": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "5.B3.1",
            "sources": "QĐ 2422 (YCCĐ 5.B3.1), Experience AI Model Card",
            "points": [
                "Giải thích vì sao con người cần hiểu cách AI đưa ra quyết định, nhất là trong các lĩnh vực quan trọng như y tế, giao thông (để đảm bảo an toàn, tin cậy và có thể sửa chữa sai sót).",
                "Lập thẻ thông tin mô hình (Model Card đơn giản) cho sản phẩm AI của nhóm: Ghi rõ dữ liệu học từ đâu, độ chính xác bao nhiêu, những hạn chế chưa làm được."
            ]
        }
    },

    # ==========================================
    # NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY (27 - 35)
    # ==========================================
    {
        "stt": 27,
        "name": "Mô tả chức năng cảm biến máy tính",
        "definition": "Giải thích được Camera là 'mắt nhìn', Micro là 'tai nghe', Mạng cảm biến là 'xúc giác' giúp hệ thống AI tiếp nhận thông tin từ thế giới thực.",
        "group_id": 4,
        "group_name": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "domain": "NLc",
        "g1": {
            "level": "Mức 1: Ẩn dụ trực quan",
            "track": "VN-CORE",
            "yccd": "1.C1.2, 1.C1.3",
            "sources": "QĐ 2422 (YCCĐ 1.C1.2, 1.C1.3), AI4K12 Big Idea 1",
            "points": [
                "Nhận biết camera giống như 'mắt nhìn' và micro giống như 'tai nghe' của thiết bị thông minh.",
                "Chỉ đúng vị trí camera và micro trên máy tính bảng, điện thoại thông minh của cô giáo."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.A2.1",
            "sources": "AI4K12 (Big Idea 1 - Sensing)",
            "points": [
                "Nhận biết cảm biến chạm/khoảng cách ở mũi robot hút bụi giống như xúc giác, giúp robot biết quay đầu khi gặp chân bàn; cảm biến nhiệt độ trên điều hòa tự chỉnh độ mát.",
                "Phân biệt cảm biến thu tín hiệu vs cơ cấu phát hành động."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A2.1, 3.C4.1",
            "sources": "AI4K12 Big Idea 1, Singapore MOE",
            "points": [
                "Khám phá các loại cảm biến trên máy tính phòng máy và máy tính bảng: Webcam, micro, cảm biến ánh sáng màn hình, cảm biến con quay xoay ngang dọc.",
                "Giải thích vai trò của cảm biến trong việc thu thập dữ liệu đầu vào (Input) từ thế giới xung quanh để máy tính xử lý."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.C2.1, 4.D1.1",
            "sources": "OECD AILF, AI4K12 Big Idea 1",
            "points": [
                "Giải thích sơ đồ luồng dữ liệu số: Cảm biến thu tín hiệu tương tự (hình ảnh, âm thanh thực) -> Bộ chuyển đổi số hóa thành các điểm ảnh/sóng âm số -> Thuật toán AI phân tích và ra quyết định.",
                "Nhận diện các loại cảm biến dùng trong xe tự lái (Lidar, Radar, Camera đa góc)."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.C5.2, 5.D1.1",
            "sources": "AI4K12 Big Idea 1, Experience AI Foundations",
            "points": [
                "Sơ đồ hóa mối liên hệ giữa các loại cảm biến ngoại vi và thuật toán nhận dạng thông minh trong hệ thống AI hoàn chỉnh.",
                "Tự cấu hình và kiểm tra thông số kỹ thuật của cảm biến webcam/micro trên phần mềm huấn luyện học máy."
            ]
        }
    },
    {
        "stt": 28,
        "name": "Xác định vai trò của dữ liệu",
        "definition": "Giải thích mối quan hệ bản chất: Dữ liệu là 'thức ăn' của AI; máy tính học máy chỉ thông minh được khi có tập ví dụ mẫu do con người chuẩn bị.",
        "group_id": 4,
        "group_name": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "domain": "NLc",
        "g1": {
            "level": "Mức 1: Nhận biết qua mẫu",
            "track": "VN-CORE",
            "yccd": "1.D1.1, 1.D1.MR1",
            "sources": "QĐ 2422 (YCCĐ 1.D1.1, 1.D1.MR1), AI4K12 Big Idea 3",
            "points": [
                "Nêu ví dụ: Con người cho máy xem nhiều bức tranh con mèo để máy biết nhận ra con mèo.",
                "Giải thích: Nếu chỉ đưa 1 bức tranh thì máy dễ đoán sai; máy cần xem nhiều bức tranh khác nhau để học đúng."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.C1.1, 2.D2.1, 2.D2.2",
            "sources": "QĐ 2422 (YCCĐ 2.C1.1, 2.D2.1-2), Experience AI",
            "points": [
                "Giải thích được: 'Dữ liệu' là những ví dụ (hình ảnh, âm thanh) mà con người dùng để dạy cho AI.",
                "Đối với các hệ thống AI học máy, máy tính cần có tập ví dụ mẫu do con người chuẩn bị thì mới có thể học và nhận biết được; cần cung cấp dữ liệu chính xác, rõ ràng."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.C4.1, 3.C5.2",
            "sources": "QĐ 2422 (YCCĐ 3.C4.1, 3.C5.2), AI4K12 Big Idea 3",
            "points": [
                "Trình bày khái niệm dữ liệu thông qua ví dụ cụ thể (tập hợp hình ảnh các loài hoa, con số nhiệt độ hàng ngày, tệp ghi âm giọng nói).",
                "Khẳng định đặc điểm cốt tử: Học máy (Machine Learning) là quá trình học trên dữ liệu mẫu."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.D1.1, 4.D2.1",
            "sources": "Experience AI (Discovering AI)",
            "points": [
                "Khẳng định nguyên lý cốt lõi: 'Dữ liệu là thức ăn của AI' - Dữ liệu sạch, chuẩn thì mô hình thông minh; dữ liệu sai, rác thì mô hình sai hỏng (Garbage in, Garbage out).",
                "Chứng minh bằng số liệu: Số lượng mẫu càng lớn và đa dạng thì độ chính xác của mô hình càng cao."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.D1.1, 5.D2.1",
            "sources": "QĐ 2422 (YCCĐ 5.D1.1, 5.D2.1), Experience AI",
            "points": [
                "Phân tích tác động mang tính quyết định của chất lượng dữ liệu đối với hiệu năng và độ tin cậy của toàn bộ hệ thống AI.",
                "Giải thích vai trò của dữ liệu kiểm thử (Test Data) độc lập với dữ liệu huấn luyện (Training Data) để đánh giá trung thực mô hình."
            ]
        }
    },
    {
        "stt": 29,
        "name": "Thu thập và chọn lọc dữ liệu mẫu",
        "definition": "Tìm kiếm, chụp ảnh, ghi âm có chọn lọc các tập mẫu đạt chuẩn (sắc nét, đúng chủ đề, đủ số lượng) để chuẩn bị dạy máy học.",
        "group_id": 4,
        "group_name": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "domain": "NLc",
        "g1": {
            "level": "Mức 1: Hoạt động tập thể",
            "track": "VN-MR",
            "yccd": "1.D1.1, 1.D1.MR1",
            "sources": "AI4K12 Big Idea 3 Hands-on",
            "points": [
                "Cùng cô giáo nhặt các đồ vật thật trong lớp (cục tẩy, bút chì, thước kẻ) hoặc các tấm tranh rõ nét xếp vào góc lớp làm tập mẫu dạy máy.",
                "Học cách xếp gọn gàng theo từng loại đồ vật."
            ]
        },
        "g2": {
            "level": "Mức 1: Thu thập tranh ảnh",
            "track": "VN-MR",
            "yccd": "2.D1.MR1, 2.D2.MR1",
            "sources": "QĐ 2422 (YCCĐ 2.D1.MR1, 2.D2.MR1), MIT Day of AI",
            "points": [
                "Thực hành tìm kiếm và sắp xếp 5-10 bức tranh rõ nét từ sách báo cũ để tạo thành bộ ví dụ mẫu dạy máy nhận diện đồ vật (quả cam vs quả chuối).",
                "Chọn những bức tranh đẹp, không bị nhàu nát hay mất góc."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.C4.MR1, 3.D1.1",
            "sources": "QĐ 2422 (YCCĐ 3.C4.MR1, 3.D1.1), Teachable Machine",
            "points": [
                "Dùng webcam phòng máy chụp 10-15 ảnh đồ dùng học tập theo hướng dẫn của giáo viên.",
                "Xác định đặc trưng nhận dạng của bộ dữ liệu (màu sắc, hình dạng, hoa văn bề mặt) để phục vụ bước huấn luyện."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.C5.MR2, 4.D1.MR1",
            "sources": "QĐ 2422 (YCCĐ 4.C5.MR2), Experience AI",
            "points": [
                "Thu thập 2 bộ dữ liệu ảnh phân biệt đạt chuẩn (ví dụ: lá cây khỏe mạnh vs lá cây bị sâu bệnh, mỗi nhóm 20 ảnh).",
                "Đảm bảo các yêu cầu kỹ thuật: Ảnh rõ nét, đủ ánh sáng, vật thể nằm ở vị trí trung tâm khung hình."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.B2.MR1, 5.D1.MR1",
            "sources": "QĐ 2422 (YCCĐ 5.B2.MR1, 5.D1.MR1), Experience AI",
            "points": [
                "Tự thiết kế và thực thi kế hoạch thu thập dữ liệu phục vụ bài toán dự án AI của nhóm: Thu thập tối thiểu 30-40 mẫu cho mỗi nhãn.",
                "Tuân thủ nghiêm ngặt các quy tắc đạo đức: Xin phép đồng thuận, không chụp trộm, bảo vệ dữ liệu cá nhân."
            ]
        }
    },
    {
        "stt": 30,
        "name": "Gán nhãn dữ liệu (Data Labeling)",
        "definition": "Thiết lập hệ thống danh mục nhãn chuẩn xác và phân loại đúng từng mẫu vào nhóm tương ứng (Class Labeling).",
        "group_id": 4,
        "group_name": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "domain": "NLc",
        "g1": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-MR",
            "yccd": "1.D2.2",
            "sources": "Singapore MOE (Sorting & Labeling)",
            "points": [
                "Đọc tên nhãn dán trên rổ: Rổ 'Đồ dùng học tập', Rổ 'Đồ chơi' khi tham gia trò chơi phân loại.",
                "Nhận biết mỗi cái rổ có một cái tên riêng để không bị xếp lộn xộn."
            ]
        },
        "g2": {
            "level": "Mức 1: Dán nhãn giấy",
            "track": "VN-MR",
            "yccd": "2.C3.1, 2.D2.MR1",
            "sources": "Experience AI (Hands-on Classification)",
            "points": [
                "Thực hành dán sticker nhãn chữ (ví dụ: Nhãn 'Cam', Nhãn 'Táo') ngay ngắn dưới từng bức tranh mẫu trước khi đưa cho cô giáo nạp vào máy tính.",
                "Hiểu rằng nhãn chữ giúp máy tính biết bức tranh đó vẽ cái gì."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.D1.1, 3.D2.MR1",
            "sources": "QĐ 2422 (YCCĐ 3.D1.1, 3.D2.MR1), Teachable Machine",
            "points": [
                "Đặt tên nhãn phân loại (Class 1: 'Hop_but', Class 2: 'Vo_viet') trên phần mềm Teachable Machine.",
                "Thao tác kéo-thả hoặc chụp trực tiếp hình ảnh vào đúng ngăn nhãn tương ứng."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.C5.MR1, 4.C5.MR2",
            "sources": "QĐ 2422 (YCCĐ 4.C5.MR1-2), Experience AI",
            "points": [
                "Thực hiện thành thạo thao tác tạo mới nhãn, đổi tên nhãn và tổ chức cấu trúc thư mục dữ liệu nhãn trên phần mềm trải nghiệm AI trực quan.",
                "Đảm bảo tên nhãn ngắn gọn, không dấu tiếng Việt (đối với phần mềm quốc tế) hoặc đúng quy chuẩn kỹ thuật."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.C5.MR2, 5.D1.1",
            "sources": "Experience AI Foundations",
            "points": [
                "Xây dựng cây nhãn dữ liệu đa lớp chuẩn xác, không bị chồng chéo ngữ nghĩa cho bài toán phân loại phức tạp (ví dụ: 'Khau_trang_dung', 'Khau_trang_sai', 'Khong_khau_trang').",
                "Kiểm tra tính nhất quán trong quy ước gán nhãn của toàn bộ các thành viên trong nhóm."
            ]
        }
    },
    {
        "stt": 31,
        "name": "Làm sạch dữ liệu (Data Cleaning)",
        "definition": "Kiểm tra tập mẫu và loại bỏ các ảnh mờ, âm thanh tạp hoặc thẻ bị gán sai nhãn trước khi bấm nút huấn luyện mô hình.",
        "group_id": 4,
        "group_name": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "domain": "NLc",
        "g1": {
            "level": "Mức 1: Trò chơi nhặt rác dữ liệu",
            "track": "VN-MR",
            "yccd": "1.D1.MR1",
            "sources": "AI4K12 Big Idea 3 Unplugged",
            "points": [
                "Tham gia trò chơi Unplugged 'Bác làm vườn dọn rác': Nhặt bỏ các bức tranh bị rách, hình vẽ bậy hoặc hình vẽ không rõ nét ra khỏi rổ tranh mẫu dạy máy.",
                "Hiểu rằng tranh xấu sẽ làm máy học sai."
            ]
        },
        "g2": {
            "level": "Mức 1: Phát hiện ảnh lỗi",
            "track": "VN-MR",
            "yccd": "2.D2.2, 2.D2.MR1",
            "sources": "QĐ 2422 (YCCĐ 2.D2.2), Experience AI",
            "points": [
                "Quan sát tập tranh mẫu, chỉ ra bức tranh bị mờ nhòe, bị chụp tối đen hoặc bị ngón tay che khuất cần loại bỏ trước khi nạp cho cô giáo.",
                "Nêu lý do: Ảnh mờ làm máy nhận diện kém hoặc đưa ra kết quả sai."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.D2.2, 3.D2.MR1, 3.D2.3",
            "sources": "QĐ 2422 (YCCĐ 3.D2.MR1, 3.D2.3), Teachable Machine",
            "points": [
                "Thực hành kiểm tra một bộ thẻ dữ liệu mẫu trên phần mềm; phát hiện và bấm nút Xóa bỏ các thẻ bị gán sai nhãn (ví dụ: ảnh quả táo nằm nhầm trong nhãn quả cam) và thẻ bị mờ nhòe.",
                "Trình bày: Nếu dữ liệu sai thì AI sẽ không hoạt động hiệu quả."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.D2.1",
            "sources": "Experience AI (Discovering AI)",
            "points": [
                "Thực hiện quy trình rà soát và làm sạch dữ liệu chuẩn: 1. Soát lỗi gán nhãn nhầm; 2. Xóa các mẫu trùng lặp 100%; 3. Loại bỏ ảnh bị rung lắc khi chụp; 4. Cân bằng ánh sáng.",
                "Ghi chép số lượng mẫu bị loại bỏ vào bảng theo dõi."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.D1.1, 5.D2.MR1",
            "sources": "QĐ 2422 (YCCĐ 5.D2.MR1), Experience AI Foundations",
            "points": [
                "Tự chủ thực hiện quy trình tiền xử lý và làm sạch dữ liệu chuyên nghiệp trước khi bấm nút huấn luyện mô hình.",
                "Phân tích tác động trực tiếp của bước làm sạch dữ liệu đối với việc nâng cao điểm số tin cậy (Confidence score) của mô hình AI."
            ]
        }
    },
    {
        "stt": 32,
        "name": "Kiểm soát tính đa dạng của dữ liệu",
        "definition": "Thu thập mẫu từ nhiều góc độ, bối cảnh, màu sắc và kích thước khác nhau để mô hình nhận diện chính xác và công bằng.",
        "group_id": 4,
        "group_name": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "domain": "NLc",
        "g1": None,
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-MR",
            "yccd": "2.B1.MR2",
            "sources": "QĐ 2422 (YCCĐ 2.B1.MR2), Experience AI",
            "points": [
                "Nhận biết cần nạp cả ảnh mèo trắng, mèo đen, mèo vàng, mèo tam thể để máy có thể nhận ra mọi loại mèo trong thực tế.",
                "Hiểu rằng nếu chỉ nạp tranh mèo trắng thì gặp mèo đen máy sẽ không biết là con gì."
            ]
        },
        "g3": {
            "level": "Mức 1: Quan sát / Nhận xét",
            "track": "VN-CORE",
            "yccd": "3.B3.MR1, 3.D2.2",
            "sources": "QĐ 2422 (YCCĐ 3.B3.MR1, 3.D2.2), UNICEF Req 4",
            "points": [
                "Giải thích: Cần nạp dữ liệu đa dạng kích thước, màu sắc và góc chụp khác nhau để AI học hỏi toàn diện.",
                "Nêu yêu cầu cơ bản đối với dữ liệu huấn luyện AI: Đủ số lượng, chính xác về nhãn và đa dạng về mẫu mã."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.D1.MR1, 4.D2.1",
            "sources": "Experience AI (Dataset Diversity)",
            "points": [
                "Thực hành thu thập mẫu vật ở nhiều điều kiện môi trường khác nhau: Nền trắng, nền bàn gỗ, ánh sáng ban ngày, ánh sáng đèn học, nhìn thẳng, nhìn nghiêng.",
                "Đánh giá xem mô hình có nhận diện tốt khi vật mẫu đổi nền hay không."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.B2.1, 5.B2.MR1",
            "sources": "QĐ 2422 (YCCĐ 5.B2.1, 5.B2.MR1), UNICEF Req 4",
            "points": [
                "Đề xuất bảng quy tắc khi thu thập dữ liệu (Data Diversity Checklist) để có được bộ dữ liệu đa dạng, đầy đủ và công bằng: Đảm bảo cân bằng tỷ lệ mẫu giữa các biến số (giới tính, vùng miền, lứa tuổi, màu sắc).",
                "Đánh giá và loại trừ nguy cơ thiên lệch do thiếu hụt dữ liệu đại diện."
            ]
        }
    },
    {
        "stt": 33,
        "name": "Phân loại bài toán học máy",
        "definition": "Phân biệt bài toán Phân loại đối tượng (chia nhóm các đối tượng rời rạc) và bài toán Dự đoán xu hướng (dự báo con số hoặc xu thế tương lai).",
        "group_id": 4,
        "group_name": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "domain": "NLc",
        "g1": None,
        "g2": {
            "level": "Mức 1: Trò chơi chia nhóm",
            "track": "VN-MR",
            "yccd": "2.C3.1",
            "sources": "AI4K12 Big Idea 3 Unplugged",
            "points": [
                "Tham gia trò chơi xếp thẻ bài vào 2 loại: Bài toán 'Chia nhóm đồ vật' (phân loại cam và chuối) vs Bài toán 'Đoán xem ngày mai' (dự đoán thời tiết mưa hay nắng).",
                "Làm quen với ý niệm: Máy tính có thể giúp con người chia nhóm hoặc đoán trước tương lai."
            ]
        },
        "g3": {
            "level": "Mức 1: Nhận biết qua ví dụ",
            "track": "VN-CORE",
            "yccd": "3.C5.4, 3.C5.MR2",
            "sources": "QĐ 2422 (YCCĐ 3.C5.4, 3.C5.MR2), Experience AI",
            "points": [
                "Nhận biết và phân biệt được bài toán học máy phân loại và bài toán học máy dự đoán qua các ví dụ thực tế.",
                "Minh họa: Phân loại email rác vs email thường (Phân loại); Dự đoán nhiệt độ ngày mai dựa trên số liệu tuần qua (Dự đoán)."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.C2.1, 4.D1.1",
            "sources": "Experience AI (Discovering AI)",
            "points": [
                "Xác định đúng dạng bài toán học máy tương ứng với nhu cầu thực tiễn: Hệ thống nhận diện khuôn mặt điểm danh (Bài toán phân loại hình ảnh); Ứng dụng dự báo sản lượng lúa theo thời tiết (Bài toán dự đoán).",
                "Giải thích sự khác biệt về loại dữ liệu đầu ra của hai dạng bài toán."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.C5.2, 5.C5.MR2",
            "sources": "Experience AI Foundations",
            "points": [
                "Lựa chọn và cấu hình chính xác dạng bài toán học máy (Phân loại hình ảnh / Phân loại âm thanh / Phân loại tư thế cơ thể) tương thích với mục tiêu của dự án sáng tạo AI.",
                "Biện luận lý do lựa chọn mô hình phân loại cho bài toán nhận diện đồ dùng học tập."
            ]
        }
    },
    {
        "stt": 34,
        "name": "Vận hành quy trình 4 bước học máy",
        "definition": "Thực hiện thuần thục quy trình học máy chuẩn gồm 4 bước: Thu thập dữ liệu -> Chuẩn bị & gán nhãn dữ liệu -> Huấn luyện mô hình -> Đánh giá & kiểm thử.",
        "group_id": 4,
        "group_name": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "domain": "NLd",
        "g1": {
            "level": "Mức 1: Nghe kể chuyện 4 bước",
            "track": "VN-MR",
            "yccd": "1.D1.1",
            "sources": "AI4K12 Big Idea 3 Storytelling",
            "points": [
                "Nghe câu chuyện 4 bước dạy chú robot thông minh: 1. Đặt tên bạn -> 2. Cho bạn xem tranh mẫu -> 3. Bạn nhớ bài học -> 4. Đố vui kiểm tra bạn.",
                "Nhớ tên 4 bước qua bài đồng dao vui nhộn."
            ]
        },
        "g2": {
            "level": "Mức 1: Quan sát cô demo",
            "track": "VN-MR",
            "yccd": "2.D1.MR1, 2.D2.1",
            "sources": "Experience AI, MIT Day of AI",
            "points": [
                "Quan sát cô giáo thao tác đủ 4 bước trên phần mềm Teachable Machine chiếu trên bảng: 1. Tạo 2 nhãn -> 2. Chụp ảnh mẫu -> 3. Bấm Train Model -> 4. Đưa đồ vật thử nghiệm.",
                "Chỉ ra bước nào con người làm và bước nào máy tính tự tính toán."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.D1.1",
            "sources": "QĐ 2422 (YCCĐ 3.D1.1), Teachable Machine",
            "points": [
                "Trình bày và thực hiện quy trình đơn giản để huấn luyện AI gồm các bước: Thu thập dữ liệu -> Chuẩn bị dữ liệu -> Huấn luyện mô hình -> Đánh giá mô hình.",
                "Cùng nhóm thao tác từng bước dưới sự hướng dẫn trực tiếp của giáo viên phòng máy."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành cá nhân có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.C5.MR1, 4.C5.MR2",
            "sources": "QĐ 2422 (YCCĐ 4.C5.MR1-2), Experience AI",
            "points": [
                "Thực hiện lại theo từng bước các thao tác cơ bản với công cụ trải nghiệm AI trực quan.",
                "Lặp lại đầy đủ 4 bước trên với một nhóm dữ liệu tự chọn khác (ví dụ: phân biệt cử chỉ giơ tay số 1 và số 2) và báo cáo kết quả đánh giá mô hình trước lớp."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.C5.2, 5.C5.MR2, 5.D1.1",
            "sources": "QĐ 2422 (YCCĐ 5.D1.1), Experience AI Foundations",
            "points": [
                "Tự chủ vận hành trọn vẹn quy trình Mini AI Lifecycle: Xác định vấn đề -> Lập kế hoạch dữ liệu -> Thu thập & Gán nhãn -> Huấn luyện mô hình -> Kiểm thử & Tái huấn luyện -> Đóng gói Model Card.",
                "Quản lý hồ sơ dự án AI khoa học, bài bản."
            ]
        }
    },
    {
        "stt": 35,
        "name": "Tái huấn luyện mô hình (Retraining)",
        "definition": "Nạp bổ sung dữ liệu mới tại những điểm AI nhận diện kém và cho máy học lại (Retrain) để nâng cao độ chính xác và tính thích ứng.",
        "group_id": 4,
        "group_name": "NHÓM 4: KỸ NĂNG DỮ LIỆU & HỌC MÁY",
        "domain": "NLd",
        "g1": None,
        "g2": None,
        "g3": {
            "level": "Mức 1: Quan sát cô sửa sai cho máy",
            "track": "VN-MR",
            "yccd": "3.A3.2, 3.D2.3",
            "sources": "Experience AI, Teachable Machine",
            "points": [
                "Quan sát cô giáo nạp thêm 3 bức ảnh con mèo chụp nghiêng khi máy đoán sai, sau đó bấm nút Train Model để máy học lại.",
                "Chứng kiến máy tính đoán đúng và độ tự tin tăng lên sau khi được nạp thêm mẫu bổ sung."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.D2.1",
            "sources": "QĐ 2422 (YCCĐ 4.D2.1), Experience AI",
            "points": [
                "Trình bày được: Con người cần liên tục đánh giá và nâng cấp sản phẩm AI sau khi tạo ra.",
                "Thực hành: Phát hiện các mẫu ảnh bị máy đoán sai -> Bổ sung thêm 5-10 ảnh ở điều kiện ánh sáng/góc độ đó -> Bấm Train lại và kiểm chứng độ chính xác cải thiện."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.C5.MR3, 5.D2.1, 5.D2.MR1",
            "sources": "QĐ 2422 (YCCĐ 5.D2.1, 5.D2.MR1), Experience AI",
            "points": [
                "Giải thích bằng ví dụ rằng hệ thống AI có thể được cải tiến và hoàn thiện theo thời gian bằng cách học thêm từ dữ liệu mới.",
                "Thực hành cải tiến hệ thống AI bằng cách bổ sung dữ liệu; so sánh tỷ lệ chính xác (Accuracy) và điểm số tin cậy trước và sau khi tái huấn luyện; lập biểu đồ đối chứng."
            ]
        }
    },

    # ==========================================
    # NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ (36 - 41)
    # ==========================================
    {
        "stt": 36,
        "name": "Xác định bài toán thực tiễn",
        "definition": "Phát hiện các khó khăn, công việc vất vả trong học tập và đời sống (nhặt rác gầm bàn, lau bảng trên cao) có thể áp dụng AI để giải quyết.",
        "group_id": 5,
        "group_name": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "domain": "NLd",
        "g1": {
            "level": "Mức 1: Quan sát việc nhà",
            "track": "VN-CORE",
            "yccd": "1.A2.2, 1.A2.3",
            "sources": "QĐ 2422 (YCCĐ 1.A2.2, 1.A2.3), Stanford AI Quests",
            "points": [
                "Kể tên đồ dùng thông minh quen thuộc (robot hút bụi, camera nhận mặt, loa nghe lệnh) và nói được việc làm có ích của từng đồ dùng (giúp quét nhà sạch sẽ, phát nhạc).",
                "Thấy mẹ quét nhà vất vả -> mơ ước có robot hút bụi phụ giúp."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận diện việc trường lớp",
            "track": "VN-CORE",
            "yccd": "2.D1.1",
            "sources": "QĐ 2422 (YCCĐ 2.D1.1), UNESCO Human-Centred Problem",
            "points": [
                "Nêu được một số vấn đề đơn giản, gần gũi trong đời sống có thể áp dụng AI để giải quyết: Công việc vất vả trong lớp hoặc ở nhà mà em mong có máy thông minh giúp đỡ (lau bảng trên cao, nhặt rác gầm bàn).",
                "Đặt con người làm trung tâm khi tìm kiếm vấn đề."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A2.1, 3.C5.3",
            "sources": "QĐ 2422 (YCCĐ 3.C5.3), Experience AI",
            "points": [
                "Nêu được một số tình huống cụ thể trong trường học có thể áp dụng học máy: Phân loại rác tái chế ở sân trường, điểm danh học sinh tự động, nhắc nhở giữ yên lặng trong thư viện.",
                "Viết phiếu khảo sát nhu cầu cần hỗ trợ của các thầy cô và bạn bè."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.D1.1, 4.D1.MR1",
            "sources": "QĐ 2422 (YCCĐ 4.D1.1, 4.D1.MR1), MIT Day of AI",
            "points": [
                "Nêu ý tưởng ban đầu về cách AI có thể học hoặc giúp giải quyết vấn đề đơn giản quanh em (nhận diện đồ vật, trợ giúp tìm kiếm).",
                "Trình bày cách sử dụng AI để giải quyết vấn đề trong tình huống cụ thể vừa sức với lứa tuổi tiểu học."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A2.2, 5.A2.3, 5.D1.1",
            "sources": "QĐ 2422 (YCCĐ 5.A2.2-3, 5.D1.1), UNESCO SDGs",
            "points": [
                "Khảo sát và xác định vấn đề cấp thiết của trường học hoặc địa phương có thể áp dụng giải pháp AI phục vụ lợi ích chung (y tế, giáo dục, giao thông, bảo vệ môi trường).",
                "Viết bản thuyết minh vấn đề (Problem Statement) rõ ràng, nêu bật tính khả thi và tác động xã hội tích cực."
            ]
        }
    },
    {
        "stt": 37,
        "name": "Mô hình hóa ý tưởng giải pháp",
        "definition": "Vẽ tranh, viết kịch bản hoặc vẽ sơ đồ khối mô tả ý tưởng robot thông minh phục vụ cộng đồng theo tư duy thiết kế hệ thống.",
        "group_id": 5,
        "group_name": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "domain": "NLd",
        "g1": {
            "level": "Mức 1: Vẽ tranh robot mơ ước",
            "track": "VN-CORE",
            "yccd": "1.A2.3",
            "sources": "Stanford AI Quests, MIT Day of AI",
            "points": [
                "Vẽ tranh chú robot thông minh giúp mẹ rửa bát, dọn đồ chơi theo trí tưởng tượng của bé.",
                "Đặt tên cho chú robot và kể 1 việc tốt robot sẽ làm giúp đỡ gia đình."
            ]
        },
        "g2": {
            "level": "Mức 1: Kể chuyện theo tranh",
            "track": "VN-CORE",
            "yccd": "2.D1.2",
            "sources": "QĐ 2422 (YCCĐ 2.D1.2), Singapore MOE Design",
            "points": [
                "Nêu được ý tưởng máy thông minh qua vẽ tranh hoặc kể tên một chú robot mơ ước do em tưởng tượng ra để giúp đỡ mọi người.",
                "Mô tả các bộ phận chính: Mắt nhìn camera, tay gắp đồ vật, bánh xe di chuyển."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A2.MR1, 3.D1.1",
            "sources": "QĐ 2422 (YCCĐ 3.A2.MR1), AI4K12 Big Idea 2",
            "points": [
                "Mô tả trường học mong muốn trong tương lai có sự xuất hiện của AI hỗ trợ học sinh và giáo viên.",
                "Vẽ sơ đồ khối 3 phần mô tả hoạt động của robot: Cảm biến thu nhận gì -> Bộ não AI nghĩ gì -> Động cơ thực hiện hành động gì."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.D1.MR1",
            "sources": "QĐ 2422 (YCCĐ 4.D1.MR1), Experience AI",
            "points": [
                "Thiết kế poster dự án AI hoàn chỉnh trên giấy A3: Tên giải pháp, Cảm biến sử dụng, Bộ dữ liệu cần nạp, Lợi ích đem lại cho cộng đồng và Cảnh báo an toàn.",
                "Trình bày poster thuyết phục trước giáo viên và các nhóm bạn."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A3.MR1, 5.D1.1",
            "sources": "QĐ 2422 (YCCĐ 5.A3.MR1, 5.D1.1), UNESCO System Design",
            "points": [
                "Trình bày ý tưởng về một số tình huống trong tương lai mà AI hỗ trợ con người hiệu quả.",
                "Lập bản kiến trúc hệ thống AI hoàn chỉnh: Sơ đồ luồng dữ liệu, Loại mô hình học máy sử dụng, Giao diện tương tác người-máy (UI/UX) và Kịch bản kiểm thử thực tế."
            ]
        }
    },
    {
        "stt": 38,
        "name": "Đề xuất giải pháp AI theo ngữ cảnh",
        "definition": "Đưa ra ý tưởng ứng dụng AI giải quyết bài toán môi trường, văn hóa hoặc xã hội gắn liền với bối cảnh đặc thù tại Việt Nam.",
        "group_id": 5,
        "group_name": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "domain": "NLd",
        "g1": None,
        "g2": None,
        "g3": {
            "level": "Mức 1: Thảo luận ý tưởng",
            "track": "VN-MR",
            "yccd": "3.A2.MR1",
            "sources": "QĐ 2422 (YCCĐ 3.A2.MR1)",
            "points": [
                "Thảo luận ý tưởng giải pháp AI gắn với đời sống trường học Việt Nam: Hệ thống camera AI nhắc nhở các bạn nhỏ đội mũ bảo hiểm trước cổng trường.",
                "Nhận biết công nghệ phải gắn liền với nề nếp văn hóa học đường."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "4.A2.2, 4.D1.MR1",
            "sources": "QĐ 2422 (YCCĐ 4.A2.2), OECD AILF",
            "points": [
                "Đề xuất ý tưởng ứng dụng AI gắn với điều kiện tự nhiên Việt Nam: Mô hình AI cảnh báo sớm nguy cơ sạt lở đất lũ quét vùng núi, AI hỗ trợ bà con nông dân phát hiện bệnh trên lá lúa.",
                "Nêu rõ các đối tượng người dân được hưởng lợi từ giải pháp."
            ]
        },
        "g5": {
            "level": "Mức 3: Vận dụng sáng tạo",
            "track": "VN-MR",
            "yccd": "5.A2.3, 5.A3.MR1",
            "sources": "QĐ 2422 (YCCĐ 5.A2.3, 5.A3.MR1), UNESCO Heritage",
            "points": [
                "Xây dựng đề án nhóm: Ứng dụng AI nhận diện và quảng bá trang phục truyền thống của 54 dân tộc Việt Nam hoặc nhận diện các di tích lịch sử quốc gia.",
                "Tích hợp niềm tự hào dân tộc và ý thức bảo tồn di sản văn hóa vào giải pháp công nghệ số."
            ]
        }
    },
    {
        "stt": 39,
        "name": "Đồng sáng tạo sản phẩm cùng AI",
        "definition": "Kết hợp hài hòa gợi ý của AI tạo sinh với tư duy cá nhân để phát triển thành tác phẩm văn học, mỹ thuật số hoàn thiện.",
        "group_id": 5,
        "group_name": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "domain": "NLc",
        "g1": None,
        "g2": {
            "level": "Mức 1: Quan sát gợi ý nét vẽ",
            "track": "VN-MR",
            "yccd": "2.B3.2",
            "sources": "Google Applied Digital Skills (Quick, Draw!)",
            "points": [
                "Quan sát AI dự đoán và gợi ý nét vẽ hoàn chỉnh khi em vẽ phác thảo bông hoa hoặc ngôi nhà trên ứng dụng Quick, Draw!.",
                "Cảm nhận sự thú vị khi máy tính có thể nhận ra nét vẽ thô sơ của con người."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "3.B2.1",
            "sources": "Google Applied Digital Skills (AutoDraw)",
            "points": [
                "Sử dụng công cụ AutoDraw: Em tự tay vẽ phác thảo ý tưởng, chọn nét vẽ đẹp do AI đề xuất, sau đó tự tay phối màu và bổ sung chi tiết sáng tạo của riêng mình.",
                "Hiểu rằng AI chỉ gợi ý hình vẽ, sự sắp xếp bố cục và cảm xúc là của chính em."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.C2.1, 4.C2.MR1",
            "sources": "Google Applied Digital Skills (Verse by Verse)",
            "points": [
                "Thực hành trải nghiệm ứng dụng AI tạo sinh: Dùng Verse by Verse nhận gợi ý vần thơ, học sinh tự chọn lọc và chắp bút viết tiếp bài thơ 4 câu hoàn chỉnh về thầy cô, mái trường.",
                "Ghi rõ sự đồng sáng tạo: 'Thơ em sáng tác - AI gợi ý vần'."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A2.1, 5.C5.2",
            "sources": "Experience AI, UNESCO Human Agency",
            "points": [
                "Kết hợp linh hoạt các công cụ AI tạo ảnh và tư duy cá nhân để xuất bản một tập truyện tranh số ngắn (Digital Comic) hoặc cẩm nang an toàn học đường.",
                "Khẳng định vai trò tác giả chính của học sinh: AI chỉ là cây cọ thông minh, linh hồn câu chuyện thuộc về tác giả nhí."
            ]
        }
    },
    {
        "stt": 40,
        "name": "Lập trình phản hồi thông minh",
        "definition": "Ứng dụng cấu trúc logic 'Nếu … thì …' trên Scratch và kết nối mô hình học máy để lập trình nhân vật tương tác thông minh.",
        "group_id": 5,
        "group_name": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "domain": "NLd",
        "g1": None,
        "g2": None,
        "g3": {
            "level": "Mức 2: Thực hành khối lệnh cơ bản",
            "track": "VN-CORE",
            "yccd": "3.C5.1, 3.C5.MR1",
            "sources": "QĐ 2422 (YCCĐ 3.C5.1, 3.C5.MR1), Scratch AI",
            "points": [
                "Mô tả cấu trúc 'Nếu … thì …' trong giải quyết tình huống hàng ngày và trong công cụ AI.",
                "Thực hành lắp ghép khối lệnh trên Scratch: 'Nếu nhấn phím Cách thì nhân vật phát lời chào' hoặc 'Nếu nhận diện tiếng vỗ tay thì bật đèn'."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.C2.MR1, 4.D1.MR1",
            "sources": "AI4K12 Big Idea 4, Scratch AI Extension",
            "points": [
                "Lập trình logic tương tác phân nhánh: 'Nếu camera nhận diện khuôn mặt cười thì nhân vật Scratch nhảy múa; Nếu mặt buồn thì phát bản nhạc vui động viên'.",
                "Kiểm thử sự phản hồi của chương trình qua webcam phòng máy."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.C5.1, 5.C5.MR1",
            "sources": "QĐ 2422 (YCCĐ 5.C5.1, 5.C5.MR1), MIT RAISE",
            "points": [
                "Nêu cách sử dụng cấu trúc 'Nếu … thì …' trong lập trình AI đơn giản (ví dụ: gán nhãn cho các nhóm kết quả dựa trên điều kiện dữ liệu).",
                "Thực hành kết nối mô hình học máy Teachable Machine đã huấn luyện vào phần mềm Scratch để điều khiển nhân vật game bằng cử chỉ tay hoặc giọng nói."
            ]
        }
    },
    {
        "stt": 41,
        "name": "Xây dựng mô hình AI hoàn chỉnh",
        "definition": "Tự thu thập dữ liệu, dạy máy học trên phần mềm và thử nghiệm tạo ra một sản phẩm AI thực tế giải quyết bài toán nhỏ.",
        "group_id": 5,
        "group_name": "NHÓM 5: KỸ NĂNG SÁNG TẠO & GIẢI QUYẾT VẤN ĐỀ",
        "domain": "NLd",
        "g1": None,
        "g2": None,
        "g3": {
            "level": "Mức 1: Tham gia nạp ảnh",
            "track": "VN-MR",
            "yccd": "3.D1.1",
            "sources": "Experience AI, Teachable Machine",
            "points": [
                "Đóng góp 3 bức ảnh chân dung của bản thân cho mô hình AI phân loại chung của lớp học.",
                "Cùng cả lớp chứng kiến mô hình được huấn luyện và cùng kiểm thử khả năng nhận diện trên màn hình máy chiếu."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành theo nhóm",
            "track": "VN-CORE",
            "yccd": "4.C5.MR1, 4.C5.MR2",
            "sources": "QĐ 2422 (YCCĐ 4.C5.MR1-2), Experience AI",
            "points": [
                "Cùng nhóm hoàn thiện sản phẩm AI nhận diện đồ dùng học tập: Tự chuẩn bị 2 nhãn dữ liệu, tự huấn luyện mô hình và chạy thử nghiệm trước lớp.",
                "Ghi chép báo cáo kết quả nhận diện chính xác và những trường hợp đoán nhầm."
            ]
        },
        "g5": {
            "level": "Mức 3: Dự án thực tế độc lập",
            "track": "VN-CORE",
            "yccd": "5.C5.2, 5.C5.MR2, 5.D1.1, 5.D1.MR1",
            "sources": "QĐ 2422 (YCCĐ 5.C5.2, 5.D1.1, 5.D1.MR1), Experience AI",
            "points": [
                "Tự chủ xây dựng hoàn chỉnh một ứng dụng AI giải quyết bài toán thực tế (ví dụ: AI nhận diện rác tái chế / rác hữu cơ, AI cảnh báo tư thế ngồi học quá gần màn hình).",
                "Thực hiện đầy đủ các bước: Thu thập dữ liệu mẫu -> Huấn luyện mô hình -> Kiểm thử -> Báo cáo thuyết trình dự án."
            ]
        }
    },

    # ==========================================
    # NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH (42 - 46)
    # ==========================================
    {
        "stt": 42,
        "name": "Duy trì tư duy độc lập (Chống ỷ lại)",
        "definition": "Tự suy nghĩ và giải quyết vấn đề trước khi tham khảo gợi ý của AI; bảo vệ sự tự chủ nhận thức và bản lĩnh học tập cá nhân.",
        "group_id": 6,
        "group_name": "NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH",
        "domain": "NLa",
        "g1": {
            "level": "Mức 1: Nhận thức",
            "track": "VN-CORE",
            "yccd": "1.A1.1, 1.B1.1",
            "sources": "Singapore MOE Cyber Wellness (Resilience)",
            "points": [
                "Bé tự suy nghĩ cách xếp đồ chơi vào giỏ, không ngồi thụ động chờ đồ chơi tự di chuyển.",
                "Tự tìm đồ dùng học tập của mình trước khi hỏi mẹ hay cô giáo; rèn thói quen tự lập từ nhỏ."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận thức",
            "track": "VN-CORE",
            "yccd": "2.A1.2",
            "sources": "QĐ 2422 (YCCĐ 2.A1.2), Singapore MOE Anti-Dependency",
            "points": [
                "Tự mình tìm đường đi trong mê cung giấy và giải câu đố vui trước khi mở ứng dụng thông minh xem đáp án.",
                "Hiểu rằng tự mình tìm ra đáp án thì niềm vui chiến thắng mới thực sự trọn vẹn."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.3, 3.A1.MR2",
            "sources": "QĐ 2422 (YCCĐ 3.A1.3, 3.A1.MR2), OECD Agency",
            "points": [
                "Phân biệt giữa việc sử dụng AI như công cụ hỗ trợ (chủ động) và để AI làm thay toàn bộ (thụ động, ỷ lại).",
                "Nêu hậu quả việc phụ thuộc quá mức vào AI: Giảm khả năng tư duy độc lập và sáng tạo; mất dần kĩ năng giải quyết vấn đề; ảnh hưởng đến sự tự tin và bản lĩnh cá nhân.",
                "Thực hành: Luôn viết nháp ý tưởng của mình ra vở trước khi mở AI tra cứu."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.A1.2, 4.A3.1",
            "sources": "Singapore MOE NDLP, Google BIA",
            "points": [
                "Thực hiện nghiêm túc quy tắc '10 phút tự tư duy': Dành tối thiểu 10 phút tự đọc hiểu, tự phân tích và phác thảo hướng giải bài tập trước khi quyết định gõ câu lệnh hỏi AI.",
                "Kiên quyết không để công nghệ thay thế năng lực suy nghĩ cá nhân."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A2.1, 5.A2.MR1",
            "sources": "QĐ 2422 (YCCĐ 5.A2.MR1), UNESCO Human-Centred",
            "points": [
                "Trình bày: Dù AI làm được nhiều việc, nhưng chỉ con người mới có ý thức, cảm xúc, khả năng sáng tạo và trách nhiệm.",
                "Bảo vệ sự tự chủ nhận thức; phản biện các gợi ý của AI; kiên định với chính kiến cá nhân nếu gợi ý của máy tính thiếu cơ sở hoặc phi logic."
            ]
        }
    },
    {
        "stt": 43,
        "name": "Ra quyết định sử dụng có điều kiện",
        "definition": "Đưa ra quyết định độc lập: Chỉ sử dụng AI khi an toàn, có ích và có người lớn giám sát; dứt khoát từ chối dùng khi có nguy cơ rủi ro.",
        "group_id": 6,
        "group_name": "NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH",
        "domain": "NLa",
        "g1": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "1.B1.1, 1.B3.1",
            "sources": "OECD Digital Safety for Minors, UNICEF Safety",
            "points": [
                "Chỉ sử dụng máy tính, tivi thông minh, loa thông minh khi có sự đồng ý và có mặt giám sát của bố mẹ hoặc cô giáo.",
                "Không tự ý bật máy khi người lớn vắng nhà."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.A1.1, 2.A1.2, 2.A2.MR2",
            "sources": "QĐ 2422 (YCCĐ 2.A1.1-2, 2.A2.MR2)",
            "points": [
                "Trình bày tình huống nên dùng AI (tìm đường, dịch câu chào) vs Tình huống không nên/cần thận trọng (khi làm lộ thông tin cá nhân, không để máy làm hết bài tập).",
                "Khẳng định quy tắc: Không được sử dụng thiết bị hoặc ứng dụng có sử dụng AI mà không có sự giám sát của người lớn."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.4, 3.A1.5, 3.A1.MR3",
            "sources": "QĐ 2422 (YCCĐ 3.A1.4, 3.A1.5, 3.A1.MR3), Singapore MOE",
            "points": [
                "Nêu các tình huống có thể gây rủi ro khi dùng AI (kết quả sai lệch, lộ bí mật).",
                "Tự đặt và trả lời bộ câu hỏi trước khi quyết định dùng AI: 'Việc này có cần dùng AI không?', 'Nếu AI đưa ra kết quả sai thì điều gì có thể xảy ra?'.",
                "Giải thích: Việc suy nghĩ và kiểm tra trước khi dùng AI giúp phòng tránh rủi ro, bảo vệ an toàn và quyền riêng tư."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.A3.1, 4.A3.MR1",
            "sources": "QĐ 2422 (YCCĐ 4.A3.1, 4.A3.MR1), OECD AILF",
            "points": [
                "Trình bày: Việc quyết định có sử dụng AI hay không phụ thuộc vào mục đích, mức độ tin cậy và sự phù hợp trong từng hoàn cảnh cụ thể.",
                "Thực hành đưa quyết định dứt khoát 'NÊN DÙNG' hay 'KHÔNG NÊN DÙNG' trong 5 tình huống giả định và giải thích rõ lý do."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A3.2",
            "sources": "QĐ 2422 (YCCĐ 5.A3.2), UNICEF Requirement 1 & 2",
            "points": [
                "Trình bày: Việc sử dụng AI phải phù hợp với nhu cầu, khả năng và giới hạn cho phép (về độ tuổi, thời lượng, tính an toàn và quy định pháp luật).",
                "Xây dựng 'Bộ quy tắc sử dụng AI thông thái' cho gia đình và lớp học."
            ]
        }
    },
    {
        "stt": 44,
        "name": "Quản trị thời gian tương tác số",
        "definition": "Tự giác dừng và ngắt kết nối thiết bị khi hết giờ; cân bằng giữa hoạt động trên màn hình số và vận động thể chất, đời sống thực tế.",
        "group_id": 6,
        "group_name": "NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH",
        "domain": "NLa",
        "g1": {
            "level": "Mức 1: Tuân thủ",
            "track": "VN-CORE",
            "yccd": "1.B1.1",
            "sources": "OECD Digital Well-being, Singapore MOE",
            "points": [
                "Rời mắt khỏi màn hình máy chiếu/tivi ngay khi chuông reo báo hết giờ hoặc khi cô giáo ra hiệu lệnh.",
                "Tập bài tập thể dục chớp mắt và vươn vai nhẹ nhàng để bảo vệ thị lực và cột sống."
            ]
        },
        "g2": {
            "level": "Mức 1: Tuân thủ",
            "track": "VN-CORE",
            "yccd": "2.A2.MR3",
            "sources": "QĐ 2422 (YCCĐ 2.A2.MR3), UNICEF Well-being",
            "points": [
                "Tự giác hẹn giờ không quá 15-20 phút khi xem chương trình hoặc học tập trên máy tính bảng gia đình.",
                "Hiểu rằng AI giúp làm việc nhanh hơn để gia đình có nhiều thời gian trò chuyện và vui chơi cùng nhau."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-MR",
            "yccd": "3.A2.MR2",
            "sources": "Singapore MOE Cyber Wellness",
            "points": [
                "Viết 'Nhật ký thời gian số': Ghi lại số phút học tập và giải trí với máy tính mỗi ngày; cam kết không sử dụng quá 45 phút mỗi lần.",
                "Tích cực tham gia các trò chơi vận động ngoài trời cùng bạn bè giờ ra chơi."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.A1.2, 4.B2.1",
            "sources": "OECD Digital Well-being, CDC Guidelines",
            "points": [
                "Thực hiện nghiêm túc quy tắc 20-20-20: Cứ sau 20 phút nhìn màn hình máy tính, nhìn xa 20 feet (6 mét) trong vòng 20 giây để thư giãn mắt.",
                "Tự giác tắt máy vi tính phòng thực hành khi hết tiết học mà không cần thầy cô nhắc nhở."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.A3.2",
            "sources": "UNESCO Human Flourishing, OECD Compass 2030",
            "points": [
                "Tự chủ quản lý thời gian tương tác số; chủ động phòng tránh hội chứng nghiện màn hình hoặc lệ thuộc vào các ứng dụng trò chuyện AI.",
                "Cân bằng hài hòa giữa học tập số với hoạt động thể thao, đọc sách giấy và gắn kết tình cảm với gia đình."
            ]
        }
    },
    {
        "stt": 45,
        "name": "Giám sát và kiểm soát hệ thống AI",
        "definition": "Giữ vững quyền hạn kiểm tra, can thiệp và phê duyệt quyết định cuối cùng trong mọi việc có AI hỗ trợ (Human-in-the-loop).",
        "group_id": 6,
        "group_name": "NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH",
        "domain": "NLa",
        "g1": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "1.A1.3, 1.C1.1",
            "sources": "UNESCO Human Agency & Oversight",
            "points": [
                "Con người là chủ nhân sáng tạo ra máy móc; em có quyền bấm nút TẮT nguồn (OFF) khi đồ chơi hoặc loa thông minh hoạt động không đúng ý.",
                "Máy móc phải tuân lệnh con người, không được tự ý điều khiển con người."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận biết",
            "track": "VN-CORE",
            "yccd": "2.A1.3, 2.A1.4",
            "sources": "QĐ 2422 (YCCĐ 2.A1.3, 2.A1.4), UNESCO Oversight",
            "points": [
                "Nêu ví dụ về tình huống cần con người giám sát AI: Người lái xe vẫn cần quan sát và giữ vô lăng khi xe tự lái hoạt động; bác sĩ cần kiểm tra lại kết quả do AI gợi ý.",
                "Biết tin tưởng vào công nghệ ở mức hợp lý nhưng không tin tuyệt đối và luôn có sự kiểm tra của con người."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.3, 3.A3.2",
            "sources": "QĐ 2422 (YCCĐ 3.A1.3, 3.A3.2), Singapore MOE",
            "points": [
                "Luôn kiểm tra lại từng phép tính hoặc gợi ý do AI đưa ra trước khi nhấn nút nộp bài; bấm nút Dừng màu đỏ trên phần mềm Scratch khi nhân vật phản hồi sai kịch bản.",
                "Khẳng định: Học sinh là người kiểm soát và ra quyết định cuối cùng đối với bài tập của mình."
            ]
        },
        "g4": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "4.A1.2, 4.D2.1",
            "sources": "UNESCO Human-in-the-loop, OECD Trustworthy AI",
            "points": [
                "Thực hành vai trò 'Người giám sát công nghệ': Phê duyệt hoặc từ chối từng phương án do AI đề xuất.",
                "Tuyệt đối không cấp quyền cho phần mềm AI tự động thực hiện các thao tác quan trọng mà không có sự xác nhận của con người."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.MR1, 5.A2.1",
            "sources": "QĐ 2422 (YCCĐ 5.A1.MR1), UNESCO Ethics, UNICEF Req 1",
            "points": [
                "Xác lập nguyên tắc tối thượng: 'Con người luôn nắm quyền kiểm soát tối cao (Human-in-the-loop) trong mọi hệ thống AI'.",
                "Trình bày: Con người chịu trách nhiệm cuối cùng về mọi quyết định và hậu quả của việc sử dụng AI, dù có sử dụng hệ thống tự động hoàn toàn thì quyền can thiệp dừng khẩn cấp luôn thuộc về con người."
            ]
        }
    },
    {
        "stt": 46,
        "name": "Xác lập trách nhiệm giải trình (Accountability)",
        "definition": "Chịu trách nhiệm toàn diện 100% về mọi quyết định và sản phẩm do mình tạo ra có sự trợ giúp của AI; tuyệt đối không đổ lỗi cho máy tính.",
        "group_id": 6,
        "group_name": "NHÓM 6: KỸ NĂNG TỰ CHỦ & TRÁCH NHIỆM GIẢI TRÌNH",
        "domain": "NLa",
        "g1": {
            "level": "Mức 1: Nhận thức",
            "track": "VN-CORE",
            "yccd": "1.B1.1, 1.B3.1",
            "sources": "UNESCO Ethics, Singapore MOE Character Education",
            "points": [
                "Làm đổ vỡ đồ chơi là do tay em bấm nút, em dũng cảm nhận lỗi và dọn dẹp, không đổ lỗi cho chiếc xe điều khiển.",
                "Hình thành ý thức dám chịu trách nhiệm về hành động của bản thân."
            ]
        },
        "g2": {
            "level": "Mức 1: Nhận thức",
            "track": "VN-CORE",
            "yccd": "2.B3.2",
            "sources": "QĐ 2422 (YCCĐ 2.B3.2), Google BIA",
            "points": [
                "Khi bài vẽ hoặc bài làm bị điểm chưa tốt, không được thanh minh: 'Tại máy tính gợi ý xấu'.",
                "Hiểu rằng người bấm nút chọn kết quả đó là chính em, em phải chịu trách nhiệm về bài nộp của mình."
            ]
        },
        "g3": {
            "level": "Mức 2: Thực hành có hướng dẫn",
            "track": "VN-CORE",
            "yccd": "3.A1.3, 3.A2.MR2",
            "sources": "QĐ 2422 (YCCĐ 3.A1.3), Singapore MOE Cyber Wellness",
            "points": [
                "Tự chịu trách nhiệm hoàn toàn về nội dung bài làm và lỗi chính tả dù có dùng trợ lý AI hỗ trợ tra cứu; không thể đổ lỗi cho phần mềm khi bài làm sai.",
                "Rèn luyện tính tự giác và trung thực trong học tập."
            ]
        },
        "g4": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "4.A1.2, 4.A3.1",
            "sources": "OECD Responsible Stewardship, Google BIA Guide",
            "points": [
                "Thảo luận tình huống đạo đức: Nếu sử dụng AI tìm kiếm thông tin sai lệch dẫn đến kết quả bài tập nhóm bị sai, thì trách nhiệm thuộc về ai?",
                "Khẳng định mạnh mẽ: Người sử dụng chịu trách nhiệm toàn bộ, máy móc không thể gánh trách nhiệm pháp lý hay đạo đức."
            ]
        },
        "g5": {
            "level": "Mức 3: Thực hành độc lập",
            "track": "VN-CORE",
            "yccd": "5.A1.2, 5.A1.MR1",
            "sources": "QĐ 2422 (YCCĐ 5.A1.2, 5.A1.MR1), UNESCO Ethics, UNICEF Req 8",
            "points": [
                "Nêu ví dụ cụ thể về trách nhiệm của người tạo và sử dụng AI (ví dụ: trách nhiệm pháp lý khi xe tự lái gây tai nạn, trách nhiệm của kỹ sư khi thuật toán phân biệt đối xử).",
                "Trình bày được: Con người chịu trách nhiệm cuối cùng về mọi quyết định và hậu quả của việc sử dụng AI.",
                "Tuyên thệ trách nhiệm cá nhân: 'Em là tác giả - Em làm chủ công cụ - Em chịu trách nhiệm 100% về sản phẩm của mình'."
            ]
        }
    }
]

print(f"Tổng số kỹ năng: {len(SKILLS_DATA)}")

def format_cell_markdown(cell_data):
    if not cell_data:
        return "-"
    level = cell_data["level"]
    track = cell_data["track"]
    yccd = cell_data.get("yccd", "")
    sources = cell_data.get("sources", "")
    points = cell_data.get("points", [])
    
    track_str = f"**[{track}]**" if track == "VN-CORE" else f"*[{track}]*"
    res = f"**{level}**<br>{track_str}"
    if yccd:
        res += f"<br>*(Mã YCCĐ: {yccd})*"
    if sources:
        res += f"<br>*(Nguồn: {sources})*"
    for p in points:
        res += f"<br>• {p}"
    return res

def format_cell_excel(cell_data):
    if not cell_data:
        return "-"
    level = cell_data["level"]
    track = cell_data["track"]
    yccd = cell_data.get("yccd", "")
    sources = cell_data.get("sources", "")
    points = cell_data.get("points", [])
    
    lines = [f"{level} [{track}]"]
    if yccd:
        lines.append(f"Mã YCCĐ: {yccd}")
    if sources:
        lines.append(f"Nguồn: {sources}")
    for p in points:
        lines.append(f"• {p}")
    return "\n".join(lines)

def export_markdown(filepath):
    lines = []
    lines.append("# BẢNG MA TRẬN PHÂN BỔ 46 KỸ NĂNG GIÁO DỤC AI CẤP TIỂU HỌC (LỚP 1 – 5) — PHIÊN BẢN v2.0")
    lines.append("")
    lines.append("> **CĂN CỨ PHÁP LÝ & CHUẨN MỰC TỐI CAO:**")
    lines.append("> - **Quyết định số 2422/QĐ-BGDĐT** ngày 18/8/2026 của Bộ GD&ĐT ban hành *'Khung nội dung giáo dục Trí tuệ nhân tạo cho học sinh phổ thông'*: Chuẩn mực bắt buộc cao nhất (Single Source of Truth) — Phủ trọn vẹn 123 YCCĐ toàn cấp.")
    lines.append("> - **Công văn số 5588/BGDĐT-GDPT** ngày 19/8/2026 của Bộ GD&ĐT hướng dẫn triển khai thực tế từ năm học 2026-2027.")
    lines.append("> - **Kho học liệu tham chiếu quốc tế mới cập nhật (2024–2026):**")
    lines.append(">   + **UNICEF Policy Guidance on AI for Children (v2.0):** 9 yêu cầu bảo vệ quyền trẻ em, an toàn số và công bằng tiếp cận.")
    lines.append(">   + **Google Be Internet Awesome (BIA) AI Literacy Guide:** Chiến lược câu lệnh (prompting), chống ảo giác (hallucination), phát hiện thiên lệch (bias) và nội dung giả mạo (deepfake).")
    lines.append(">   + **Google Applied Digital Skills (Discover AI in Daily Life):** 10 modules trải nghiệm thực hành (Quick, Draw!, AutoDraw, Verse by Verse, Google Translate).")
    lines.append(">   + **Experience AI (Google DeepMind & Raspberry Pi Foundation):** Giáo trình Discovering AI (8–12 tuổi) & Foundations of AI (11–14 tuổi), bài lab 'Bias in, bias out', Model Card và vòng đời học máy.")
    lines.append(">   + **AI4K12 Five Big Ideas & UNESCO AI Competency Framework (2024):** 4 chiều năng lực, 3 mức độ thành thạo và 5 ý tưởng lớn về AI.")
    lines.append(">   + **OECD Learning Compass 2030 & Singapore MOE NDLP:** Năng lực tự chủ số, chống ỷ lại nhận thức công nghệ và văn hóa đồng thuận.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## I. QUY CHUẨN VẬN HÀNH MA TRẬN VÀ NGUYÊN TẮC RÀNG BUỘC")
    lines.append("")
    lines.append("### 1. Thang 3 Mức độ yêu cầu sư phạm:")
    lines.append("- **Mức 1: Quan sát / Nhận biết (Observation / Recognition):** Học sinh tiếp cận trực quan qua tranh thẻ, đồ vật thực tế, câu chuyện, trò chơi không cắm điện (Unplugged) hoặc xem giáo viên thị phạm qua máy chiếu.")
    lines.append("- **Mức 2: Thực hành có hướng dẫn (Guided Practice):** Học sinh thao tác theo nhóm hoặc cá nhân dưới sự hướng dẫn từng bước (Scaffolding) của giáo viên trên máy tính phòng thực hành môn Tin học.")
    lines.append("- **Mức 3: Thực hành độc lập / Vận dụng (Independent Practice / Application):** Học sinh tự chủ thao tác, tự thu thập dữ liệu, thẩm định kết quả, phản biện thông tin và hoàn thành sản phẩm/dự án học tập.")
    lines.append("")
    lines.append("### 2. Hai luồng thời lượng (36 tiết/lớp/năm học):")
    lines.append("- **`VN-CORE` (12 tiết Cốt lõi):** Bắt buộc 100% học sinh; bao phủ kín 100% Yêu cầu cần đạt cốt lõi của Bộ GD&ĐT theo QĐ 2422. Áp dụng triệt để phương pháp sư phạm trải nghiệm (Kolb) và Unplugged.")
    lines.append("- **`VN-MR` & `INT-ENRICH` (24 tiết Mở rộng):** Nội dung tăng cường, đào sâu kỹ năng, câu lạc bộ, dự án liên môn và làm giàu chuẩn quốc tế; bao phủ kín 100% YCCĐ mở rộng (mã `MR`) của QĐ 2422.")
    lines.append("")
    lines.append("### 3. Ràng buộc hạ tầng thiết bị tuyệt đối:")
    lines.append("- **Lớp 1 – Lớp 2:** Học sinh **100% KHÔNG thao tác máy tính cá nhân**. Mọi kỹ năng kỹ thuật (NLc) và thiết kế hệ thống (NLd) chỉ định vị ở **Mức 1 (Quan sát / Nhận biết)** qua hoạt động Unplugged hoặc giáo viên demo.")
    lines.append("- **Lớp 3 – Lớp 5:** Bắt đầu chuyển dịch lên **Mức 2 (Thực hành có hướng dẫn)** và **Mức 3 (Thực hành độc lập)** trên máy tính (sử dụng Teachable Machine, AutoDraw, Scratch AI).")
    lines.append("")
    lines.append("### 4. Chính sách từ vựng chuẩn (Zero-Deviation Policy):")
    lines.append("Tuân thủ nghiêm ngặt 26 thuật ngữ trong Phụ lục QĐ 2422: *Câu lệnh (prompt), Ảo giác AI (hallucination), Thiên lệch (bias), Nội dung giả mạo do AI tạo ra (deepfake), Chatbot, Tác nhân AI (AI agent), Khử nhận dạng dữ liệu cá nhân, Trách nhiệm giải trình (Accountability), Học máy (machine learning), v.v.*")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## II. BẢNG MA TRẬN CHI TIẾT 46 KỸ NĂNG × 5 KHỐI LỚP (BẢN v2.0)")
    lines.append("")

    current_group = 0
    for s in SKILLS_DATA:
        if s["group_id"] != current_group:
            current_group = s["group_id"]
            lines.append(f"### {s['group_name']}")
            lines.append("")
            lines.append("| STT | Tên kỹ năng & Định nghĩa chuẩn hóa | Mạch NL | Lớp 1 (30–35 phút) | Lớp 2 (30–35 phút) | Lớp 3 (35 phút) | Lớp 4 (35 phút) | Lớp 5 (35 phút) |")
            lines.append("| :---: | :--- | :---: | :--- | :--- | :--- | :--- | :--- |")
        
        row_str = f"| **{s['stt']}** | **{s['name']}**<br>*{s['definition']}* | `{s['domain']}` | "
        row_str += f"{format_cell_markdown(s['g1'])} | "
        row_str += f"{format_cell_markdown(s['g2'])} | "
        row_str += f"{format_cell_markdown(s['g3'])} | "
        row_str += f"{format_cell_markdown(s['g4'])} | "
        row_str += f"{format_cell_markdown(s['g5'])} |"
        lines.append(row_str)
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## III. BẢNG TỔNG HỢP THỐNG KÊ & MA TRẬN YCCĐ TOÀN CẤP")
    lines.append("")
    lines.append("| Chỉ số thống kê kỹ năng | Lớp 1 | Lớp 2 | Lớp 3 | Lớp 4 | Lớp 5 | Toàn cấp Tiểu học |")
    lines.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
    lines.append("| **Tổng số kỹ năng kích hoạt** | **28** | **37** | **45** | **44** | **44** | **46 kỹ năng** |")
    lines.append("| • Kỹ năng Cốt lõi (`VN-CORE`) | 22 | 24 | 27 | 33 | 36 | 142 lượt |")
    lines.append("| • Kỹ năng Mở rộng (`VN-MR`) | 6 | 13 | 18 | 11 | 8 | 56 lượt |")
    lines.append("| **Tổng số YCCĐ QĐ 2422 bao phủ** | **21 / 21** | **29 / 29** | **32 / 32** | **17 / 17** | **24 / 24** | **123 / 123 (100%)** |")
    lines.append("| • YCCĐ Cốt lõi của Bộ GD&ĐT | 16 | 17 | 25 | 11 | 18 | 87 YCCĐ |")
    lines.append("| • YCCĐ Mở rộng (`MR`) của Bộ | 5 | 12 | 7 | 6 | 6 | 36 YCCĐ |")
    lines.append("| **Thời lượng chương trình** | **36 tiết** | **36 tiết** | **36 tiết** | **36 tiết** | **36 tiết** | **180 tiết** |")
    lines.append("| • Luồng 1: Chuyên đề Cốt lõi bắt buộc | 12 tiết | 12 tiết | 12 tiết | 12 tiết | 12 tiết | 60 tiết |")
    lines.append("| • Luồng 2: Nội dung Mở rộng & Làm giàu | 24 tiết | 24 tiết | 24 tiết | 24 tiết | 24 tiết | 120 tiết |")
    lines.append("")
    lines.append("### Nhận định quy luật sư phạm và tiến trình kiến trúc:")
    lines.append("1. **Độ phủ 100% YCCĐ pháp lý:** Ma trận v2.0 đã đối chiếu và phủ kín trọn vẹn 123/123 YCCĐ của Bộ GD&ĐT từ Lớp 1 đến Lớp 5, đảm bảo tính hợp pháp và giải trình cao nhất.")
    lines.append("2. **Thẩm thấu tinh hoa quốc tế mới cập nhật:** Mỗi ô kỹ năng được tích hợp các bài lab, nguyên tắc đạo đức và bài tập thực tế từ Experience AI, Google BIA AI Literacy Guide, Google ADS, UNICEF 9 Requirements và AI4K12.")
    lines.append("3. **Ràng buộc hạ tầng nghiêm ngặt:** Lớp 1–2 giữ vững 100% không dùng máy tính cá nhân, học sinh tiếp cận thuần túy qua Unplugged và giáo viên demo. Lớp 3–5 phát triển thực hành có hướng dẫn và thực hành độc lập trên nền tảng Teachable Machine và Scratch AI.")
    lines.append("")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"-> Đã xuất tệp Markdown: {filepath}")

def export_excel(filepath):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Ma_Tran_46_Ky_Nang_v2.0"
    ws.views.sheetView[0].showGridLines = True

    # Palette màu chuyên nghiệp
    navy_header = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    group_header = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    core_tag_fill = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
    mr_tag_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
    
    font_title = Font(name="Calibri", size=16, bold=True, color="1F4E79")
    font_sub = Font(name="Calibri", size=10, italic=True, color="595959")
    font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    font_group = Font(name="Calibri", size=11, bold=True, color="1F4E79")
    font_bold = Font(name="Calibri", size=10, bold=True)
    font_normal = Font(name="Calibri", size=9)
    font_italic = Font(name="Calibri", size=9, italic=True)

    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )
    thick_bottom = Border(bottom=Side(style='medium', color='1F4E79'))

    # Title rows
    ws.merge_cells("A1:H1")
    ws["A1"] = "BẢNG MA TRẬN PHÂN BỔ 46 KỸ NĂNG GIÁO DỤC AI CẤP TIỂU HỌC (LỚP 1 - 5) — BẢN v2.0"
    ws["A1"].font = font_title
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 30

    ws.merge_cells("A2:H2")
    ws["A2"] = "Căn cứ: Quyết định 2422/QĐ-BGDĐT & CV 5588/BGDĐT-GDPT | Tham chiếu quốc tế: UNICEF, Google BIA, Experience AI, AI4K12, UNESCO, OECD"
    ws["A2"].font = font_sub
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 20

    # Header table
    headers = [
        "STT", 
        "Tên kỹ năng & Định nghĩa chuẩn hóa", 
        "Mạch NL", 
        "Lớp 1 (30–35 phút)\n100% Unplugged", 
        "Lớp 2 (30–35 phút)\n100% Unplugged", 
        "Lớp 3 (35 phút)\nGuided Practice", 
        "Lớp 4 (35 phút)\nIndependent/Guided", 
        "Lớp 5 (35 phút)\nIndependent Practice"
    ]
    
    ws.row_dimensions[4].height = 40
    for col_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col_idx, value=h)
        cell.fill = navy_header
        cell.font = font_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    current_row = 5
    current_group = 0

    for s in SKILLS_DATA:
        if s["group_id"] != current_group:
            current_group = s["group_id"]
            ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=8)
            g_cell = ws.cell(row=current_row, column=1, value=s["group_name"])
            g_cell.fill = group_header
            g_cell.font = font_group
            g_cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
            ws.row_dimensions[current_row].height = 25
            current_row += 1

        ws.row_dimensions[current_row].height = 140

        # Cột 1: STT
        c1 = ws.cell(row=current_row, column=1, value=s["stt"])
        c1.alignment = Alignment(horizontal="center", vertical="top")
        c1.font = font_bold
        c1.border = thin_border

        # Cột 2: Tên & Định nghĩa
        c2 = ws.cell(row=current_row, column=2, value=f"{s['name']}\n\n{s['definition']}")
        c2.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        c2.font = font_normal
        c2.border = thin_border

        # Cột 3: Mạch NL
        c3 = ws.cell(row=current_row, column=3, value=s["domain"])
        c3.alignment = Alignment(horizontal="center", vertical="top")
        c3.font = font_bold
        c3.border = thin_border

        # Cột 4 - 8: Lớp 1 - 5
        grades_data = [s["g1"], s["g2"], s["g3"], s["g4"], s["g5"]]
        for idx, g_data in enumerate(grades_data, 4):
            cell = ws.cell(row=current_row, column=idx, value=format_cell_excel(g_data))
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            cell.font = font_normal
            cell.border = thin_border
            if g_data:
                if g_data["track"] == "VN-CORE":
                    cell.fill = core_tag_fill
                elif g_data["track"] == "VN-MR":
                    cell.fill = mr_tag_fill

        current_row += 1

    # Column widths
    col_widths = {1: 6, 2: 32, 3: 10, 4: 35, 5: 35, 6: 35, 7: 35, 8: 35}
    for col_idx, width in col_widths.items():
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = width

    wb.save(filepath)
    print(f"-> Đã xuất tệp Excel: {filepath}")

def export_docx(filepath):
    doc = docx.Document()

    # Cấu hình khổ giấy A4 ngang (Landscape)
    section = doc.sections[0]
    section.page_width = Inches(11.69)
    section.page_height = Inches(8.27)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)

    # Tiêu đề
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(4)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_t = title_p.add_run("BẢNG MA TRẬN PHÂN BỔ 46 KỸ NĂNG GIÁO DỤC AI CẤP TIỂU HỌC (LỚP 1 – 5) — BẢN v2.0")
    run_t.font.name = "Calibri"
    run_t.font.size = Pt(15)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(31, 78, 121)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(10)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_s = sub_p.add_run("Căn cứ pháp lý: QĐ 2422/QĐ-BGDĐT & CV 5588/BGDĐT-GDPT | Tham chiếu: UNICEF, Google BIA, Experience AI, AI4K12, UNESCO, OECD")
    run_s.font.name = "Calibri"
    run_s.font.size = Pt(9.5)
    run_s.font.italic = True
    run_s.font.color.rgb = RGBColor(89, 89, 89)

    # Tạo bảng
    table = doc.add_table(rows=1, cols=8)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Độ rộng cột (Tổng cộng ~ 10.69 inches)
    col_widths = [Inches(0.4), Inches(2.0), Inches(0.5), Inches(1.55), Inches(1.55), Inches(1.55), Inches(1.55), Inches(1.55)]

    # Header row
    hdr_cells = table.rows[0].cells
    headers = [
        "STT", 
        "Tên kỹ năng &\nĐịnh nghĩa chuẩn hóa", 
        "Mạch", 
        "Lớp 1 (30–35p)\nUnplugged", 
        "Lớp 2 (30–35p)\nUnplugged", 
        "Lớp 3 (35p)\nGuided Practice", 
        "Lớp 4 (35p)\nIndependent", 
        "Lớp 5 (35p)\nIndependent"
    ]
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].width = col_widths[i]
        shd = parse_xml(r'<w:shd {} w:fill="1F4E79"/>'.format(nsdecls('w')))
        hdr_cells[i]._tc.get_or_add_tcPr().append(shd)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

    current_group = 0
    for s in SKILLS_DATA:
        if s["group_id"] != current_group:
            current_group = s["group_id"]
            # Row group header
            g_row = table.add_row()
            g_cell = g_row.cells[0]
            g_cell.text = s["group_name"]
            g_cell.width = sum(col_widths)
            # Merge across all 8 cols
            for c in g_row.cells[1:]:
                g_cell.merge(c)
            shd = parse_xml(r'<w:shd {} w:fill="D9E1F2"/>'.format(nsdecls('w')))
            g_cell._tc.get_or_add_tcPr().append(shd)
            p = g_cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = "Calibri"
                r.font.size = Pt(9.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(31, 78, 121)

        row = table.add_row()
        cells = row.cells
        for i, w in enumerate(col_widths):
            cells[i].width = w

        # STT
        cells[0].text = str(s["stt"])
        cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        cells[0].paragraphs[0].runs[0].font.bold = True
        cells[0].paragraphs[0].runs[0].font.size = Pt(8.5)

        # Tên & Định nghĩa
        p_name = cells[1].paragraphs[0]
        p_name.text = s["name"]
        p_name.runs[0].font.bold = True
        p_name.runs[0].font.size = Pt(8.5)
        p_def = cells[1].add_paragraph(s["definition"])
        p_def.runs[0].font.italic = True
        p_def.runs[0].font.size = Pt(7.5)

        # Mạch
        cells[2].text = s["domain"]
        cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        cells[2].paragraphs[0].runs[0].font.size = Pt(8.5)
        cells[2].paragraphs[0].runs[0].font.bold = True

        # Lớp 1 - 5
        grades_data = [s["g1"], s["g2"], s["g3"], s["g4"], s["g5"]]
        for idx, g_data in enumerate(grades_data, 3):
            cell = cells[idx]
            if not g_data:
                cell.text = "-"
                cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
                cell.paragraphs[0].runs[0].font.size = Pt(8.5)
            else:
                p_top = cell.paragraphs[0]
                p_top.text = f"{g_data['level']} [{g_data['track']}]"
                p_top.runs[0].font.bold = True
                p_top.runs[0].font.size = Pt(8)
                if g_data["track"] == "VN-CORE":
                    p_top.runs[0].font.color.rgb = RGBColor(56, 87, 35) # Dark Green
                    shd = parse_xml(r'<w:shd {} w:fill="F2F8F2"/>'.format(nsdecls('w')))
                    cell._tc.get_or_add_tcPr().append(shd)
                else:
                    p_top.runs[0].font.color.rgb = RGBColor(128, 96, 0) # Dark Gold
                    shd = parse_xml(r'<w:shd {} w:fill="FFFDF2"/>'.format(nsdecls('w')))
                    cell._tc.get_or_add_tcPr().append(shd)

                if g_data.get("yccd"):
                    p_yccd = cell.add_paragraph(f"Mã YCCĐ: {g_data['yccd']}")
                    p_yccd.runs[0].font.italic = True
                    p_yccd.runs[0].font.size = Pt(7.5)
                    p_yccd.runs[0].font.color.rgb = RGBColor(112, 48, 160) # Purple

                for pt in g_data.get("points", []):
                    p_pt = cell.add_paragraph(f"• {pt}")
                    p_pt.runs[0].font.size = Pt(7.5)

    doc.save(filepath)
    print(f"-> Đã xuất tệp Word: {filepath}")

if __name__ == "__main__":
    out_dir = r"03_San_Pham_Chinh_Thuc"
    os.makedirs(out_dir, exist_ok=True)
    
    md_path = os.path.join(out_dir, "Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_v2.0.md")
    xlsx_path = os.path.join(out_dir, "Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_v2.0.xlsx")
    docx_path = os.path.join(out_dir, "Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_v2.0.docx")

    export_markdown(md_path)
    export_excel(xlsx_path)
    export_docx(docx_path)
    print("=== HOÀN THÀNH ĐỒNG BỘ 3 ĐỊNH DẠNG v2.0 THÀNH CÔNG! ===")

