import re

file_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Section I heading
content = content.replace(
    "## I.  QUAN ĐIỂM XÂY DỰNG KHUNG NỘI DUNG GIÁO DỤC TRÍ TUỆ\n\nNHÂN TẠO Trong bối cảnh",
    "## I. QUAN ĐIỂM XÂY DỰNG KHUNG NỘI DUNG GIÁO DỤC TRÍ TUỆ NHÂN TẠO\n\nTrong bối cảnh"
)
content = content.replace(
    "## I.  QUAN ĐIỂM XÂY DỰNG KHUNG NỘI DUNG GIÁO DỤC TRÍ TUỆ",
    "## I. QUAN ĐIỂM XÂY DỰNG KHUNG NỘI DUNG GIÁO DỤC TRÍ TUỆ NHÂN TẠO"
)
content = content.replace(
    "NHÂN TẠO Trong bối cảnh",
    "Trong bối cảnh"
)

# Fix heading 3 in Section V
content = content.replace(
    "### 3. Định hướng phương pháp và hình thức tổ chức dạy học đặc thù trong\n\ngiáo dục AI",
    "### 3. Định hướng phương pháp và hình thức tổ chức dạy học đặc thù trong giáo dục AI"
)
content = content.replace(
    "### 3. Định hướng phương pháp và hình thức tổ chức dạy học đặc thù trong",
    "### 3. Định hướng phương pháp và hình thức tổ chức dạy học đặc thù trong giáo dục AI"
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed headings in QD2422 md")
