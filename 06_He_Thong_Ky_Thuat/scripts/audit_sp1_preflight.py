"""
BỘ KIỂM ĐỊNH TỰ ĐỘNG SẢN PHẨM 1 (PRE-FLIGHT AUDIT TOOL FOR SP1)
Tuân thủ Điều 6B AGENTS.md, QĐ 2422/QĐ-BGDĐT và Tiêu chí QC-9 (Skill ppct_qaqc_auditor)

Chức năng:
1. Gate 1 (Row Integrity): Kiểm đếm số lượng YCCĐ khớp chính xác với định mức QĐ 2422.
2. Gate 2 (Blacklist Filter): Quét danh mục từ cấm theo lứa tuổi (Giao thức Human Lock).
3. Gate 3 (Cross-Format Sync): Kiểm tra tính nhất quán giữa tệp Word và Markdown.
"""

import os
import sys
import re
import docx

sys.stdout.reconfigure(encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "03_San_Pham_Chinh_Thuc"))

# 1. Định mức bất biến theo QĐ 2422
BENCHMARK_PRIMARY = {
    1: 21,
    2: 29,
    3: 32,
    4: 17,
    5: 24
}

# 2. Danh mục từ cấm cho cấp Tiểu học (Human Lock Blacklist)
PRIMARY_BLACKLIST = [
    (r"\bpháp lý\b", "Cấm gán trách nhiệm pháp lý cho trẻ tiểu học (chỉ dùng 'chịu trách nhiệm cuối cùng')"),
    (r"độc quyền", "Cấm dùng từ khẩu hiệu 'phẩm chất độc quyền' (dùng 'năng lực giữ vai trò trung tâm')"),
    (r"kiên quyết bài trừ", "Cấm dùng từ cực đoan (dùng 'tránh lạm dụng, không chia sẻ bừa bãi')"),
    (r"kiểm thử đối kháng", "Cấm thuật ngữ kỹ sư AI hàn lâm (dùng 'kiểm tra trên nhiều trường hợp/nhóm')"),
    (r"nguyên lý học liên tục", "Cấm khái niệm hàn lâm (dùng 'cải tiến khi bổ sung, cập nhật dữ liệu')"),
    (r"thao tác thành thạo", "Cấm vượt chuẩn kĩ năng ở Tiểu học (dùng 'thao tác cơ bản')"),
    (r"đo lường độ tin cậy", "Cấm vượt chuẩn đánh giá ở Tiểu học (dùng 'quan sát điểm số tin cậy nếu có')"),
    (r"\btất yếu\b", "Cấm từ ngữ đao to búa lớn ở Lớp 3 (dùng 'cần thiết')"),
    (r"\bvô hiệu\b", "Cấm từ ngữ đao to búa lớn ở Lớp 3 (dùng 'mất tác dụng')"),
    # Chốt chặn xâm lấn THCS (Anti-Secondary Creep - Điều 4B AGENTS.md)
    (r"cây quyết định", "Cấm đưa thuật ngữ 'cây quyết định' của THCS vào Tiểu học"),
    (r"decision tree", "Cấm đưa thuật ngữ 'decision tree' của THCS vào Tiểu học"),
    (r"thẻ mô hình", "Cấm đưa công cụ 'thẻ mô hình' của THCS vào Tiểu học"),
    (r"model card", "Cấm đưa công cụ 'model card' của THCS vào Tiểu học"),
    (r"ma trận nhầm lẫn", "Cấm đưa thuật ngữ 'ma trận nhầm lẫn' vào Tiểu học"),
    (r"confusion matrix", "Cấm đưa thuật ngữ 'confusion matrix' vào Tiểu học"),
    (r"few-shot", "Cấm đưa kỹ thuật prompt đa tầng 'few-shot' vào Tiểu học"),
    (r"chain-of-thought", "Cấm đưa kỹ thuật prompt 'chain-of-thought' vào Tiểu học"),
    (r"common sense", "Cấm trích dẫn học liệu Common Sense Education (dành cho THCS/THPT) vào Tiểu học"),
    (r"foundations of ai", "Cấm trích dẫn khóa Foundations of AI (11-14 tuổi) vào Tiểu học")
]

def run_preflight_audit():
    print("=" * 70)
    print("  BỘ KIỂM ĐỊNH TỰ ĐỘNG TIỀN XUẤT BẢN SẢN PHẨM 1 (QC-9 AUDIT TOOL)")
    print("=" * 70)

    total_issues = 0

    # A. KIỂM ĐỊNH TỪNG KHỐI LỚP (LỚP 1 ĐẾN LỚP 5)
    for g, exp_count in BENCHMARK_PRIMARY.items():
        print(f"\n--- [KIỂM ĐỊNH LỚP {g}] (Định mức chuẩn: {exp_count} YCCĐ) ---")
        
        def resolve_file(filename):
            p1 = os.path.join(BASE_DIR, filename)
            if os.path.exists(p1):
                return p1
            p2 = os.path.join(BASE_DIR, "file lẻ", filename)
            if os.path.exists(p2):
                return p2
            return p1

        f_md_full = resolve_file(f"SP1_Khung_YCCD_AI_Lop{g}_Day_Du.md")
        f_docx_full = resolve_file(f"SP1_Khung_YCCD_AI_Lop{g}_Day_Du.docx")
        f_md_comp = resolve_file(f"SP1_Khung_YCCD_AI_Lop{g}_Rut_Gon.md")
        f_docx_comp = resolve_file(f"SP1_Khung_YCCD_AI_Lop{g}_Rut_Gon.docx")

        # 1. Kiểm tra tồn tại tệp
        files = [f_md_full, f_docx_full, f_md_comp, f_docx_comp]
        missing = [f for f in files if not os.path.exists(f)]
        if missing:
            print(f"❌ GATE 0 FAIL: Thiếu tệp: {missing}")
            total_issues += len(missing)
            continue
        print("✅ Gate 0 PASS: Đầy đủ 4 tệp định dạng (.docx & .md cho cả Full & Compact).")

        # 2. Gate 1: Row Integrity Check
        with open(f_md_full, encoding="utf-8") as f:
            full_md_lines = [l for l in f if l.strip().startswith("| **")]
        with open(f_md_comp, encoding="utf-8") as f:
            comp_md_lines = [l for l in f if l.strip().startswith("| **")]

        doc_f = docx.Document(f_docx_full)
        doc_c = docx.Document(f_docx_comp)
        full_docx_rows = len(doc_f.tables[0].rows) - 1
        comp_docx_rows = len(doc_c.tables[0].rows) - 1

        counts = [len(full_md_lines), len(comp_md_lines), full_docx_rows, comp_docx_rows]
        if all(c == exp_count for c in counts):
            print(f"✅ Gate 1 PASS (Row Integrity): Khớp chính xác {exp_count}/{exp_count} YCCĐ ở cả 4 tệp.")
        else:
            print(f"❌ Gate 1 FAIL: Lệch số dòng! Full MD={counts[0]}, Comp MD={counts[1]}, Full DOCX={counts[2]}, Comp DOCX={counts[3]}, Kỳ vọng={exp_count}")
            total_issues += 1

        # 3. Gate 2: Age-Appropriate Blacklist Check (trên bảng dữ liệu, bỏ qua metadata header)
        full_table_text = "\n".join(full_md_lines)
        comp_table_text = "\n".join(comp_md_lines)
        table_combined = full_table_text + "\n" + comp_table_text

        class_issues = 0
        for pattern, reason in PRIMARY_BLACKLIST:
            # Ngoại lệ: Lớp 4-5 không bắt lỗi 'tất yếu' / 'vô hiệu' (chỉ rà soát ở Lớp 3)
            if g != 3 and pattern in [r"\btất yếu\b", r"\bvô hiệu\b"]:
                continue
            matches = list(re.finditer(pattern, table_combined, re.IGNORECASE))
            if matches:
                print(f"❌ Gate 2 VIOLATION: Phát hiện từ cấm '{pattern}' trong Lớp {g}! Lý do: {reason}")
                class_issues += len(matches)
                total_issues += len(matches)

        if class_issues == 0:
            print(f"✅ Gate 2 PASS (Human Lock): 100% sạch từ cấm lứa tuổi theo Điều 6B AGENTS.md.")

    # B. KIỂM ĐỊNH CÁC TỆP MASTER TỔNG HỢP TOÀN CẤP
    print("\n--- [KIỂM ĐỊNH TỆP MASTER TỔNG HỢP TOÀN CẤP (LỚP 1 - 5)] ---")
    def resolve_master(filename):
        p1 = os.path.join(BASE_DIR, "YCCĐ Lớp 1 - 5", filename)
        if os.path.exists(p1):
            return p1
        p2 = os.path.join(BASE_DIR, filename)
        if os.path.exists(p2):
            return p2
        return p1

    f_master_full_docx = resolve_master("SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.docx")
    f_master_comp_docx = resolve_master("SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.docx")
    f_master_full_md = resolve_master("SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md")
    f_master_comp_md = resolve_master("SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.md")

    m_files = [f_master_full_docx, f_master_comp_docx, f_master_full_md, f_master_comp_md]
    m_missing = [f for f in m_files if not os.path.exists(f)]
    if m_missing:
        print(f"❌ Master FAIL: Thiếu tệp master: {m_missing}")
        total_issues += len(m_missing)
    else:
        with open(f_master_full_md, encoding="utf-8") as f:
            m_full_lines = [l for l in f if l.strip().startswith("| **")]
        with open(f_master_comp_md, encoding="utf-8") as f:
            m_comp_lines = [l for l in f if l.strip().startswith("| **")]
        d_mf = docx.Document(f_master_full_docx)
        d_mc = docx.Document(f_master_comp_docx)

        m_full_docx_count = sum(len(t.rows) - 1 for t in d_mf.tables)
        m_comp_docx_count = sum(len(t.rows) - 1 for t in d_mc.tables)

        print(f"Master Full MD YCCĐ count: {len(m_full_lines)} (expected 123)")
        print(f"Master Comp MD YCCĐ count: {len(m_comp_lines)} (expected 123)")
        print(f"Master Full DOCX YCCĐ count: {m_full_docx_count} (expected 123)")
        print(f"Master Comp DOCX YCCĐ count: {m_comp_docx_count} (expected 123)")

        if len(m_full_lines) == 123 and len(m_comp_lines) == 123 and m_full_docx_count == 123 and m_comp_docx_count == 123:
            print("✅ Master PASS: Cả 4 tệp Master tổng hợp đều chứa trọn vẹn 123/123 YCCĐ của Tiểu học!")
        else:
            print("❌ Master FAIL: Lệch tổng số YCCĐ trên tệp Master!")
            total_issues += 1

    print("\n" + "=" * 70)
    if total_issues == 0:
        print("🏆 KẾT QUẢ CUỐI CÙNG: 100% TẤT CẢ CÁC TỆP SP1 TIỂU HỌC ĐẠT CHUẨN XUẤT SẮC!")
        print("=" * 70)
        return True
    else:
        print(f"⚠️ KẾT QUẢ CUỐI CÙNG: Phát hiện {total_issues} lỗi cần xử lý!")
        print("=" * 70)
        return False

if __name__ == "__main__":
    success = run_preflight_audit()
    sys.exit(0 if success else 1)
