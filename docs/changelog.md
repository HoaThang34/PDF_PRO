# PDF PRO - Nhật Ký Phát Triển

## 24/05/2026 - Xây dựng Landing Page + cập nhật tài liệu

### Công việc đã thực hiện
- Tạo `landing-page/` với Vite + React 18 (thư mục riêng, không trùng source code tool)
- 12 sections: Header, Hero, Tools Grid, Features, Demo/Showcase, How It Works, Advanced Features, Security, Performance, Testimonials, FAQ, Final CTA, Footer
- Thiết kế dark theme, responsive, có sẵn file `vercel.json` deploy zero-config lên Vercel
- Sử dụng icon SVG thay vì emoji — file `src/icons.jsx` chứa 30+ component icon
- Tích hợp hình ảnh thực tế: ảnh chụp giao diện (`image/homepage.png`), chân dung tác giả (`image/hoaquangthang.png`), logo (`logo.png`)
- Hiệu ứng animation cho 3 bước xử lý, badge floating
- Before/After so sánh chất lượng trước-sau khi xử lý (AI-generated content)
- Thông tin tác giả: Hoà Quang Thắng, Facebook, GitHub, Email, SĐT
- Cập nhật `docs/project_config.md`: thêm mô tả landing page và thư mục `image/`, `landing-page/`
- Cập nhật `README.md`: sử dụng ảnh thực tế, thêm landing page section
- Cập nhật `AGENTS.md`: hướng dẫn landing page



## 24/05/2026 - Phat trien 3 tinh nang con lai

### Cong viec da thuc hien

#### Tinh nang 6: Xuat Anh Tu PDF
- Tao `src/core/pdf_extract_image.py`: logic xuat trang PDF thanh anh PNG/JPEG
- Tao `src/ui/pages/extract_image_page.py`: giao dien chon trang, xem truoc anh, tuy chon dinh dang (PNG/JPEG) va DPI (150-600)
- Cap nhat `main.py`: routing tinh nang moi

#### Tinh nang 7: Xuat PDF Sang Excel
- Them `openpyxl==3.1.5` vao `requirements.txt`
- Tao `src/core/pdf_to_excel.py`: trich xuat van ban tu PDF, phan tich dong/cot, xuat file Excel co dinh dang
- Tao `src/ui/pages/to_excel_page.py`: giao dien chon trang, xem truoc, tuy chon gop thanh 1 file
- Cap nhat `main.py`: routing tinh nang moi

#### Tinh nang 8: Nen File PDF
- Tao `src/core/pdf_compress.py`: nen PDF bang cach toi uu hinh anh, gom rac, deflate
- Tao `src/ui/pages/compress_page.py`: giao dien chon file, hien thi thong tin, tuy chon muc do nen (Thap/Trung binh/Cao)
- Cap nhat `main.py`: routing tinh nang moi

### Cap nhat tai lieu
- `docs/project_config.md`: danh dau 3 tinh nang da phat trien, them openpyxl vao danh sach thu vien

## 24/05/2026 - Phat trien tinh nang Chinh Sua & Ky Ten

### Cong viec da thuc hien
- Tao `src/core/pdf_edit.py`: logic xu ly PDF (doc, render, ap dung chinh sua) bang PyMuPDF
- Tao `src/ui/pages/edit_page.py`: giao dien chinh tinh nang gom toolbar + canvas + thumbnails
- Tao `src/ui/pages/signature_dialog.py`: dialog ve chu ky bang chuot
- Cap nhat `main.py`: routing tinh nang moi

### Chuc nang ho tro
- **But ve**: Ve tu do len PDF voi nhieu mau sac va do day
- **Them chu**: Nhap van ban truc tiep tai vi tri click
- **Ky ten**: Ve chu ky bang chuot va dat len file PDF
- **Dieu chinh**: Zoom in/out (25%-300%), hoan tac, xoa chinh sua theo trang
- **Danh sach trang**: Xem thumbnails, chuyen trang nhanh
- **Luu**: Xuat file PDF da chinh sua voi hieu ung day du

### Bug fix
- `CTkScrollableFrame.grid_propagate(False)` crash vi CTkScrollableFrame khong ho tro tham so boolean
- `UserWarning` khi dung `ImageTk.PhotoImage` voi `CTkLabel` -> chuyen sang `CTkImage`

## 23/05/2026 - Khoi tao du an

### Cong viec da thuc hien
- Tao cau truc thu muc du an
- Xay dung giao dien ban dau (khung UI) voi CustomTkinter
- Cai dat thu vien: customtkinter 5.2.2, Pillow 11.2.1

### Cau truc file da tao (tinh nang Chinh Sua & Ky Ten)
```
src/core/pdf_edit.py              # Core PDF editing logic
src/ui/pages/edit_page.py         # Trang chinh sua & ky ten
src/ui/pages/signature_dialog.py  # Dialog ve chu ky
```

### Bo sung vao file co san
- `main.py`: Them import va routing cho EditPage

### Giao dien ban dau
- Header: Logo PDF PRO + navigation "All Tools"
- Hero section: Tieu de "Xu Ly PDF Nhanh Chong & Bao Mat"
- 8 card tinh nang: Ghep, Sap Xep, Chinh Sua, Tach, Trich Xuat Van Ban, Xuat Anh, Xuat Excel, Nen
- Footer: Ban quyen + links
- Dark theme chuyen nghiep voi hieu ung hover

### Ghi chu
- Chua phat trien logic xu ly PDF (chi giao dien)
- Cac trang con tinh nang chua xay dung
- San sang cho buoc tiep theo: phat trien tung tinh nang
