import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('03_San_Pham_Chinh_Thuc/Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_v2.0.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the 4 missing codes and see where they should be mapped:
# Missing codes: '1.C1.MR2', '2.B3.1', '3.A2.2', '4.A1.1'

# 1.C1.MR2: Quan sát được máy thông minh phản ứng khác nhau khi nghe tiếng vỗ tay so với khi nghe tiếng nói của con người.
# -> Best fit: Skill 2 (Phát âm câu lệnh chuẩn xác) or Skill 27 (Mô tả chức năng cảm biến máy tính).

# 2.B3.1: Phân biệt được sản phẩm do mình tự làm ra (như bức tranh tự vẽ) với sản phẩm do máy thông minh tạo ra.
# -> Best fit: Skill 14 (Minh bạch tác quyền AI (Attribution)) or Skill 15 (Thực hành liêm chính học thuật).

# 3.A2.2: Nêu được mục đích của AI trong trường học: hỗ trợ thầy cô và học sinh, cá nhân hoá việc học theo năng lực và kích hoạt hứng thú học tập.
# -> Best fit: Skill 3 (Khai thác AI hỗ trợ học tập) or Skill 17 (Xây dựng giải pháp AI bao trùm).

# 4.A1.1: Trình bày được một số lĩnh vực hoặc công việc cụ thể mà AI có thể hỗ trợ con người (nông nghiệp, y tế, giao thông...).
# -> Best fit: Skill 36 (Xác định bài toán thực tiễn) or Skill 38 (Đề xuất giải pháp AI theo ngữ cảnh).

print("Check analysis completed.")
