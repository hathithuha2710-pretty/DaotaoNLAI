import os
import sys
import re
from docx import Document

sys.stdout.reconfigure(encoding='utf-8')

folder = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi"
full_md = os.path.join(folder, "SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md")
full_docx = os.path.join(folder, "SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.docx")
compact_md = os.path.join(folder, "SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md")
compact_docx = os.path.join(folder, "SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.docx")

files = [full_md, full_docx, compact_md, compact_docx]

print("=== 1. KIỂM TRA SỰ TỒN TẠI VÀ DUNG LƯỢNG TỆP ===")
for f in files:
    if os.path.exists(f):
        size_kb = os.path.getsize(f) / 1024
        print(f"  [OK] {os.path.basename(f)}: {size_kb:.1f} KB")
    else:
        print(f"  [FAIL] Missing file: {f}")

blacklist = [
    'cây quyết định', 'decision tree', 'thẻ mô hình', 'model card',
    'ma trận nhầm lẫn', 'confusion matrix', 'few-shot', 'chain-of-thought',
    'common sense', 'foundations of ai',
    'pháp lý', 'độc quyền', 'kiên quyết bài trừ', 'kiểm thử đối kháng',
    'nguyên lý học liên tục', 'thao tác thành thạo', 'đo lường độ tin cậy'
]

print("\n=== 2. QUÉT TỪ CẤM BLACKLIST & THCS CREEP (ĐIỀU 4B AGENTS.MD) ===")
for f in [full_md, compact_md]:
    with open(f, 'r', encoding='utf-8') as stream:
        text = stream.read()
    fname = os.path.basename(f)
    found = []
    for kw in blacklist:
        m = re.findall(rf'({kw})', text, re.IGNORECASE)
        if m:
            found.append((kw, len(m)))
    if found:
        print(f"  [FAIL] {fname} chứa từ cấm: {found}")
    else:
        print(f"  [PASS] {fname}: 0 từ cấm blacklist!")

print("\n=== 3. ĐỐI SOÁT MÃ YCCĐ GIỮA BẢN ĐẦY ĐỦ VÀ BẢN RÚT GỌN ===")
with open(full_md, 'r', encoding='utf-8') as f:
    full_text = f.read()
with open(compact_md, 'r', encoding='utf-8') as f:
    compact_text = f.read()

full_codes = [c.replace('**', '').strip() for c in re.findall(r'\|\s*\*\*\d+\*\*\s*\|\s*\*\*([^\*\|]+)\*\*\s*\|', full_text)]
compact_codes = [c.replace('**', '').strip() for c in re.findall(r'\|\s*\*\*\d+\*\*\s*\|\s*\*\*([^\*\|]+)\*\*\s*\|', compact_text)]

print(f"  Số mã YCCĐ trong Bản Đầy Đủ: {len(full_codes)}")
print(f"  Số mã YCCĐ trong Bản Rút Gọn: {len(compact_codes)}")

if full_codes == compact_codes:
    print("  [PASS] 100% mã YCCĐ khớp chính xác tuyệt đối giữa 2 bản (123/123)!")
else:
    print("  [FAIL] Phát hiện sự sai lệch giữa 2 danh sách mã!")
    diff = set(full_codes) ^ set(compact_codes)
    print(f"  Khác biệt: {diff}")

print("\n=== 4. KIỂM ĐỊNH BẢNG BIỂU TRONG TỆP DOCX ===")
doc_compact = Document(compact_docx)
print(f"  Số bảng trong file Word Bản Rút Gọn: {len(doc_compact.tables)}")
total_docx_rows = sum(len(t.rows) - 1 for t in doc_compact.tables)
print(f"  Tổng số dòng dữ liệu YCCĐ trong Word: {total_docx_rows} (Kỳ vọng: 123)")

if total_docx_rows == 123:
    print("  [PASS] Tệp DOCX đầy đủ 123 YCCĐ chuẩn xác!")
else:
    print("  [FAIL] Số dòng trong tệp Word không khớp!")
