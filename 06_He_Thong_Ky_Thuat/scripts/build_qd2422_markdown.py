import sys, io, re
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber
import pymupdf

pdf_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.pdf"
out_path = r"01_Van_Ban_Phap_Ly\2422_QD_BGDDT_PL_kem_theo_QD_-_Khung_ND_GD_AI_tu_____2026-2027.signed_1d10d.md"

doc_fitz = pymupdf.open(pdf_path)
pdf_plumber = pdfplumber.open(pdf_path)

def clean_paragraph_text(text):
    lines = [l.strip() for l in text.split('\n')]
    clean_lines = []
    for l in lines:
        if not l:
            continue
        if re.match(r'^\d+$', l):
            continue
        if re.match(r'^(?:2422|18|08)$', l):
            continue
        clean_lines.append(l)
    return clean_lines

def format_text_lines_to_md(lines):
    md_blocks = []
    curr_para = []
    
    for l in lines:
        if re.match(r'^[I|V|X]+\.\s+', l):
            if curr_para:
                md_blocks.append(" ".join(curr_para))
                curr_para = []
            md_blocks.append(f"\n## {l}\n")
        elif re.match(r'^\d+\.\s+[A-ZÀ-Ỹ]', l) and len(l) < 120:
            if curr_para:
                md_blocks.append(" ".join(curr_para))
                curr_para = []
            md_blocks.append(f"\n### {l}\n")
        elif re.match(r'^[a-z]\)\s+[A-ZÀ-Ỹ]', l) and len(l) < 120:
            if curr_para:
                md_blocks.append(" ".join(curr_para))
                curr_para = []
            md_blocks.append(f"\n#### {l}\n")
        elif l.startswith(('-', '•', '+')):
            if curr_para:
                md_blocks.append(" ".join(curr_para))
                curr_para = []
            clean_b = l.lstrip('-•+ ').strip()
            md_blocks.append(f"- {clean_b}")
        else:
            if md_blocks and md_blocks[-1].startswith('- ') and not l.startswith(('1.', '2.', '3.', '4.', '5.', 'I.', 'II.', 'III.', 'IV.', 'V.', 'VI.')) and not curr_para:
                md_blocks[-1] += " " + l
            else:
                curr_para.append(l)
                
    if curr_para:
        md_blocks.append(" ".join(curr_para))
        
    return "\n\n".join(md_blocks)

def clean_cell_text(text):
    """
    Cleans table cell text by properly joining lines broken by PDF wrapping.
    Only introduces <br> between distinct bullet points or distinct list items.
    """
    if not text:
        return ""
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if not lines:
        return ""
    
    items = []
    curr = []
    for l in lines:
        # Check if line starts a new bullet item
        if l.startswith(('-', '•', '+')) or re.match(r'^\d+[\.\)]\s+', l):
            if curr:
                items.append(" ".join(curr))
            curr = [l]
        else:
            if curr:
                curr.append(l)
            else:
                curr = [l]
    if curr:
        items.append(" ".join(curr))
        
    return "<br>".join(items).replace('|', '\\|')

def format_yccd_cell(text):
    """
    Formats the YCCĐ column: joins wrapped text lines within each YCCĐ code,
    and formats multiple codes cleanly with double <br> and bold code tags.
    """
    if not text:
        return ""
    # First reassemble wrapped lines
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    unified_text = " ".join(lines)
    
    parts = re.split(r'(\b\d+\.[A-D]\d*(?:\.MR\d+|\.\d+)?\.\s*)', unified_text)
    if len(parts) <= 1:
        return unified_text.replace('|', '\\|')
    
    formatted = []
    if parts[0].strip():
        formatted.append(parts[0].strip().replace('|', '\\|'))
        
    i = 1
    while i < len(parts):
        code = parts[i].strip()
        desc = parts[i+1].strip() if i+1 < len(parts) else ""
        desc = desc.replace('|', '\\|')
        formatted.append(f"**{code}** {desc}")
        i += 2
        
    return "<br><br>".join(formatted)

md_sections = []

# Header
md_sections.append("""# BỘ GIÁO DỤC VÀ ĐÀO TẠO

# KHUNG NỘI DUNG GIÁO DỤC TRÍ TUỆ NHÂN TẠO CHO HỌC SINH PHỔ THÔNG
*(Kèm theo Quyết định số 2422/QĐ-BGDĐT ngày 18 tháng 8 năm 2026 của Bộ trưởng Bộ Giáo dục và Đào tạo)*

---
""")

# Section I, II, III, IV introductory text (Pages 1 to 9)
p1_9_lines = []
for p_idx in range(9):
    txt = doc_fitz[p_idx].get_text()
    lines = clean_paragraph_text(txt)
    if p_idx == 0:
        header_skipped = []
        skip = True
        for l in lines:
            if 'I.  QUAN ĐIỂM' in l or 'I. QUAN ĐIỂM' in l:
                skip = False
            if not skip:
                header_skipped.append(l)
        lines = header_skipped
    p1_9_lines.extend(lines)

# Rejoin split headings like "I. QUAN ĐIỂM..." + "NHÂN TẠO"
fixed_lines = []
skip_next = False
for i, l in enumerate(p1_9_lines):
    if skip_next:
        skip_next = False
        continue
    if 'I.  QUAN ĐIỂM XÂY DỰNG KHUNG NỘI DUNG GIÁO DỤC TRÍ TUỆ' in l and i + 1 < len(p1_9_lines) and p1_9_lines[i+1] == 'NHÂN TẠO':
        fixed_lines.append("I. QUAN ĐIỂM XÂY DỰNG KHUNG NỘI DUNG GIÁO DỤC TRÍ TUỆ NHÂN TẠO")
        skip_next = True
    else:
        fixed_lines.append(l)

sec1_3_md = format_text_lines_to_md(fixed_lines)
md_sections.append(sec1_3_md)

# Section IV Overview Tables (Pages 10 to 13)
md_sections.append("\n\n### BẢNG TỔNG THỂ MẠCH NỘI DUNG GIÁO DỤC AI\n")

# Overview Table 1: Tiểu học (Lớp 1-5, Page 10)
md_sections.append("#### 1. Cấp Tiểu học (Lớp 1 – Lớp 5)\n")
p10_t = pdf_plumber.pages[9].extract_tables()[0]
ov1_header = [clean_cell_text(c) for c in p10_t[0]]
md_sections.append("| " + " | ".join(ov1_header) + " |")
md_sections.append("| " + " | ".join(["---"] * len(ov1_header)) + " |")
for row in p10_t[1:]:
    clean_r = [clean_cell_text(c) for c in row]
    while len(clean_r) < len(ov1_header): clean_r.append("")
    md_sections.append("| " + " | ".join(clean_r[:len(ov1_header)]) + " |")

# Overview Table 2: THCS (Lớp 6-9, Page 11 & Page 12 Table 0)
md_sections.append("\n\n#### 2. Cấp Trung học cơ sở (Lớp 6 – Lớp 9)\n")
p11_t = pdf_plumber.pages[10].extract_tables()[0]
p12_t0 = pdf_plumber.pages[11].extract_tables()[0]
ov2_header = [clean_cell_text(c) for c in p11_t[0]]
md_sections.append("| " + " | ".join(ov2_header) + " |")
md_sections.append("| " + " | ".join(["---"] * len(ov2_header)) + " |")
for row in p11_t[1:] + p12_t0[1:]:
    clean_r = [clean_cell_text(c) for c in row]
    while len(clean_r) < len(ov2_header): clean_r.append("")
    md_sections.append("| " + " | ".join(clean_r[:len(ov2_header)]) + " |")

# Overview Table 3: THPT (Lớp 10-12, Page 12 Table 1 & Page 13 Table 0)
md_sections.append("\n\n#### 3. Cấp Trung học phổ thông (Lớp 10 – Lớp 12)\n")
p12_t1 = pdf_plumber.pages[11].extract_tables()[1]
p13_t0 = pdf_plumber.pages[12].extract_tables()[0]
ov3_header = [clean_cell_text(c) for c in p12_t1[0]]
md_sections.append("| " + " | ".join(ov3_header) + " |")
md_sections.append("| " + " | ".join(["---"] * len(ov3_header)) + " |")
for row in p12_t1[1:] + p13_t0[1:]:
    clean_r = [clean_cell_text(c) for c in row]
    while len(clean_r) < len(ov3_header): clean_r.append("")
    md_sections.append("| " + " | ".join(clean_r[:len(ov3_header)]) + " |")

# Detailed Grade Tables (Lớp 1 to Lớp 12, Pages 14 to 43)
grades_def = [
    ("LỚP 1", 14, 16),
    ("LỚP 2", 16, 18),
    ("LỚP 3", 18, 21),
    ("LỚP 4", 21, 23),
    ("LỚP 5", 23, 26),
    ("LỚP 6", 26, 29),
    ("LỚP 7", 29, 31),
    ("LỚP 8", 32, 34),
    ("LỚP 9", 34, 37),
    ("LỚP 10", 37, 39),
    ("LỚP 11", 39, 41),
    ("LỚP 12", 41, 43),
]

for g_name, start_p, end_p in grades_def:
    md_sections.append(f"\n\n## {g_name}\n")
    all_rows = []
    for p_idx in range(start_p - 1, end_p):
        p = pdf_plumber.pages[p_idx]
        tables = p.extract_tables()
        for t_idx, table in enumerate(tables):
            if p_idx == start_p - 1 and len(tables) > 1 and start_p > 14:
                if t_idx == 0:
                    continue
            if p_idx == end_p - 1 and len(tables) > 1 and end_p != 31 and end_p != 43:
                if t_idx > 0:
                    continue
            for r in table:
                clean_r = [c.strip() if c else '' for c in r]
                if clean_r == ['Chủ đề', 'Nội dung', 'Yêu cầu cần đạt']:
                    continue
                if not any(clean_r):
                    continue
                all_rows.append(clean_r)
                
    # Build markdown table
    md_sections.append("| Chủ đề | Nội dung | Yêu cầu cần đạt |")
    md_sections.append("| :--- | :--- | :--- |")
    
    for r in all_rows:
        col0_raw = r[0] if len(r) > 0 else ''
        col1_raw = r[1] if len(r) > 1 else ''
        col2_raw = r[2] if len(r) > 2 else ''
        
        col0 = clean_cell_text(col0_raw)
        col1 = clean_cell_text(col1_raw)
        
        # Check if strand header row
        if (col0.startswith(('A.', 'B.', 'C.', 'D.')) and ' ' in col0 and not col1 and not col2_raw) or (col0.startswith(('A.', 'B.', 'C.', 'D.')) and col1 == '' and col2_raw == ''):
            md_sections.append(f"| **{col0}** | | |")
            continue
            
        col2 = format_yccd_cell(col2_raw)
        md_sections.append(f"| {col0} | {col1} | {col2} |")

# Section V, VI (Pages 44 to 48)
p44_48_lines = []
for p_idx in range(43, 48):
    txt = doc_fitz[p_idx].get_text()
    lines = clean_paragraph_text(txt)
    if p_idx == 47:
        sec_lines = []
        for l in lines:
            if 'PHỤ LỤC' in l or 'GIẢI THÍCH THUẬT NGỮ' in l:
                break
            sec_lines.append(l)
        lines = sec_lines
    p44_48_lines.extend(lines)

# Rejoin multi-line headings in V and VI
fixed_v_vi_lines = []
skip_next = False
for i, l in enumerate(p44_48_lines):
    if skip_next:
        skip_next = False
        continue
    if l == '3. Định hướng phương pháp và hình thức tổ chức dạy học đặc thù trong' and i + 1 < len(p44_48_lines) and p44_48_lines[i+1] == 'giáo dục AI':
        fixed_v_vi_lines.append("3. Định hướng phương pháp và hình thức tổ chức dạy học đặc thù trong giáo dục AI")
        skip_next = True
    else:
        fixed_v_vi_lines.append(l)

sec5_6_md = format_text_lines_to_md(fixed_v_vi_lines)
md_sections.append("\n\n" + sec5_6_md)

# Glossary Section (Pages 48 to 51)
md_sections.append("\n\n## PHỤ LỤC: GIẢI THÍCH THUẬT NGỮ\n")

glossary_terms = []
for p_idx in [48, 49, 50]:
    tables = pdf_plumber.pages[p_idx].extract_tables()
    for t in tables:
        for row in t:
            non_empty = [c.strip().replace('\n', ' ') for c in row if c and c.strip()]
            if len(non_empty) >= 2:
                t_name, t_def = non_empty[0], non_empty[1]
                if t_name not in ['Thuật ngữ', '']:
                    glossary_terms.append((t_name, t_def))
            elif len(non_empty) == 1 and glossary_terms:
                prev_name, prev_def = glossary_terms[-1]
                glossary_terms[-1] = (prev_name, prev_def + " " + non_empty[0])

md_sections.append("| STT | Thuật ngữ | Giải thích |")
md_sections.append("| :---: | :--- | :--- |")
for idx, (t_name, t_def) in enumerate(glossary_terms):
    clean_name = t_name.replace('|', '\\|')
    clean_def = t_def.replace('|', '\\|')
    md_sections.append(f"| **{idx+1}** | **{clean_name}** | {clean_def} |")

final_content = "\n".join(md_sections)
final_content = re.sub(r'\n{3,}', '\n\n', final_content)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print(f"Generated {out_path} with {len(final_content)} characters and {len(glossary_terms)} glossary terms.")
