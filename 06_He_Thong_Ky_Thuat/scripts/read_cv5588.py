import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import fitz

doc = fitz.open('cong-van-5588-bgddt-gdpt.pdf')
print(f'So trang: {doc.page_count}')

all_text = []
for i, page in enumerate(doc):
    text = page.get_text()
    if text.strip():
        all_text.append(f'--- TRANG {i+1} ---\n{text}')
        print(f'--- TRANG {i+1} ---')
        print(text)
    else:
        # PDF dạng ảnh scan, thử lấy metadata
        print(f'Trang {i+1}: Không có text (có thể là scan ảnh)')
        # Thử extract via rawdict
        rawdict = page.get_text('rawdict')
        nblocks = len(rawdict.get('blocks', []))
        print(f'  -> {nblocks} image blocks')

doc.close()
