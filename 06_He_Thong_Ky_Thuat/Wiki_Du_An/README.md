# Wiki Giáo dục AI Tiểu học

Website tra cứu 180 bài học theo Lớp 1–5, 46 kỹ năng thuộc 6 nhóm và 123 Yêu cầu cần đạt. Có danh sách và trang chi tiết bài học, kỹ năng, YCCĐ; tìm kiếm, bộ lọc và giao diện điện thoại. Phông Noto Sans đi kèm mã nguồn, hỗ trợ tiếng Việt và có giấy phép OFL.

Dữ liệu giáo dục trong `data/curriculum.json` được trích từ ba tài liệu Word SP1, SP2, SP3 đã chọn. Tên và mã bài giữ theo tài liệu nguồn. Website không chứa tài liệu Word/Markdown gốc hoặc ghi chú quá trình làm.

## Chạy website

Cần Node.js 22 trở lên. Không có thư viện JavaScript bên ngoài cần cài đặt.

```sh
cd 06_He_Thong_Ky_Thuat/Wiki_Du_An
npm run build
npm run check
python -m http.server 8891 --directory dist --bind 127.0.0.1
```

Mở http://127.0.0.1:8891/ trong trình duyệt. Python chỉ dùng để chạy máy chủ xem thử; việc build chỉ cần Node.js.

## Triển khai trên Vercel

Import repo `hathithuha2710-pretty/DaotaoNLAI` và chọn:

| Thiết lập | Giá trị |
| --- | --- |
| Production Branch | `main` |
| Root Directory | `06_He_Thong_Ky_Thuat/Wiki_Du_An` |
| Framework Preset | `Other` |
| Build Command | `npm run build` |
| Output Directory | `dist` |

`vercel.json` đã lưu cấu hình build và thư mục xuất bản. Chỉ `dist/` được phục vụ như website. Sau khi kết nối Vercel, commit mới trên nhánh production sẽ cập nhật bản online theo cấu hình Git của Vercel.

Tham khảo [cấu hình dự án Vercel](https://vercel.com/docs/project-configuration) và [Root Directory](https://vercel.com/docs/deployments/configure-a-build#root-directory).

## Cập nhật nội dung từ Word

Đây là bước chủ động khi có tài liệu nguồn mới, không chạy tự động trên Vercel. Cần ba file:

- `SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Rut_Gon.docx`
- `SP2_Bang_Ma_Tran_Ky_Nang_AI_Tieu_Hoc_Lop1_5_Moi.docx`
- `SP3_ Phan_phoi_Chuong_Trinh_AI_Lop_1_5_36_Bai.docx`

```sh
python -m pip install -r requirements.txt
python scripts/extract_word.py --input-dir "../../03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi"
npm run build
npm run check
```

Đối chiếu bản Word được chọn trước khi commit dữ liệu. Script chỉ đọc Word và ghi dữ liệu web; không sửa file nguồn. Bộ lọc nhóm kỹ năng dựa vào tham chiếu KN được ghi trực tiếp trong PPCT.

## Cấu trúc mã nguồn

- `web/`: HTML, JavaScript, CSS, biểu tượng và phông chữ.
- `data/curriculum.json`: nội dung giáo dục dùng trên website.
- `scripts/build.mjs`: đóng gói website vào `dist/`.
- `scripts/verify.mjs`: kiểm tra số lượng, định danh, liên kết kỹ năng và các tệp được xuất bản.
- `scripts/extract_word.py`: cập nhật dữ liệu từ ba tài liệu Word.

Các trang dùng địa chỉ hash; không cần cấu hình rewrite cho SPA. Có thể triển khai cùng gói `dist/` lên dịch vụ phục vụ website tĩnh khác.
