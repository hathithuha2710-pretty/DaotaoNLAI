# -*- coding: utf-8 -*-
"""
Module chứa toàn bộ dữ liệu Phân phối chương trình Giáo dục AI Cấp Tiểu học (Lớp 1 - 5)
Tuân thủ 100% Quyết định 2422/QĐ-BGDĐT, Công văn 5588/BGDĐT-GDPT và Bảng ma trận 46 kỹ năng v2.0.
"""

GRADES_CONFIG = {
    1: {
        "title": "LỚP 1",
        "duration": "30–35 phút/tiết",
        "core_count": 17,
        "mr_count": 4,
        "total_yccd": 21,
        "pedagogy": "Trực quan – Cảm xúc Người và Máy – Đóng vai & Thẻ tranh Unplugged (100% không dùng máy tính cá nhân)",
        "assessment": "Đánh giá quá trình thường xuyên qua quan sát, nhận xét sự tiến bộ; hồ sơ học tập (tranh vẽ, mô hình robot giấy); không thi, không cho điểm."
    },
    2: {
        "title": "LỚP 2",
        "duration": "30–35 phút/tiết",
        "core_count": 17,
        "mr_count": 12,
        "total_yccd": 29,
        "pedagogy": "Trực quan – Nhận thức AI Gia đình – Dữ liệu mẫu & Phân loại trực quan – Trò chơi có luật Unplugged & Demo giáo viên",
        "assessment": "Đánh giá quá trình qua bảng kiểm hành vi (Checklist), quan sát thao tác thẻ dữ liệu, nhận xét sản phẩm mô hình ý tưởng."
    },
    3: {
        "title": "LỚP 3",
        "duration": "35 phút/tiết",
        "core_count": 21,
        "mr_count": 11,
        "total_yccd": 32,
        "pedagogy": "Trực quan sang Tư duy logic – AI Trường học – Khám phá Dữ liệu & Học máy sơ khai – Bắt đầu thực hành có hướng dẫn trên phòng máy",
        "assessment": "Đánh giá quá trình qua phiếu học tập, kết quả kiểm chứng thông tin AI, nhật ký câu lệnh cơ bản, sản phẩm dự án Teachable Machine."
    },
    4: {
        "title": "LỚP 4",
        "duration": "35 phút/tiết",
        "core_count": 10,
        "mr_count": 7,
        "total_yccd": 17,
        "pedagogy": "Khám phá Khoa học – Ứng dụng AI Đời sống & Sáng tạo – Vận hành 4 bước học máy – Thực hành phòng máy và giải quyết vấn đề thực tế",
        "assessment": "Đánh giá quá trình qua hồ sơ số (Digital Portfolio), sản phẩm sáng tạo cùng AI (tranh vẽ AutoDraw, ý tưởng giải pháp), rubric đánh giá đồng đẳng."
    },
    5: {
        "title": "LỚP 5",
        "duration": "35 phút/tiết",
        "core_count": 15,
        "mr_count": 9,
        "total_yccd": 24,
        "pedagogy": "Tư duy Thiết kế Hệ thống – Đạo đức & Trách nhiệm giải trình – Huấn luyện & Tinh chỉnh mô hình học máy – Dự án liên môn vì cộng đồng",
        "assessment": "Đánh giá quá trình qua báo cáo dự án học máy hoàn chỉnh (Model Card), thuyết trình giải pháp vì cộng đồng, đánh giá năng lực thích ứng số chuẩn bị lên THCS."
    }
}
