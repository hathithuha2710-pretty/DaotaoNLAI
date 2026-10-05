import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import pymupdf
import base64, json

doc = pymupdf.open('cong-van-5588-bgddt-gdpt.pdf')
print(f'So trang: {doc.page_count}')

# Render each page as PNG and save
for i, page in enumerate(doc):
    mat = pymupdf.Matrix(2, 2)  # 2x zoom for better OCR quality
    pix = page.get_pixmap(matrix=mat)
    out_path = f'cv5588_page_{i+1}.png'
    pix.save(out_path)
    print(f'Saved: {out_path} ({pix.width}x{pix.height})')

doc.close()
print('Done rendering pages')
