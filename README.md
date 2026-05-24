<div align="center">
  <img src="logo.png" alt="PDF PRO Logo" width="80" height="80">
  <h1>PDF PRO</h1>
  <p><strong>Bộ Công Cụ Chỉnh Sửa PDF Chuyên Nghiệp</strong></p>
  <p>Ứng dụng desktop giao diện thiết kế hiện đại, hỗ trợ 8 tính năng xử lý PDF mạnh mẽ.</p>

  <!-- Nút tải xuống một cú nhấp chuột -->
  <a href="https://github.com/HoaThang34/PDF_PRO/releases/download/v1.0.0/PDF-PRO.exe">
    <img src="https://img.shields.io/badge/T%E1%BA%A3i%20xu%E1%BB%91ng%20PDF%20PRO%20v1.0-1a1b2e?style=for-the-badge&logo=windows&logoColor=white&labelColor=%233b82f6" alt="Tải xuống">
  </a>

  <br>

  <a href="https://github.com/HoaThang34/PDF_PRO/releases">
    <img src="https://img.shields.io/github/v/release/HoaThang34/PDF_PRO?style=flat-square&label=Phi%C3%AAn%20b%E1%BA%A3n%20m%E1%BB%9Bi%20nh%E1%BA%A5t&color=%233b82f6" alt="Release">
  </a>
  <a href="https://github.com/HoaThang34/PDF_PRO">
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/Gi%E1%BA%A5y%20ph%C3%A9p-MIT-blue?style=flat-square" alt="License">
  </a>
</div>

---

## Giao Diện Ứng Dụng

<div align="center">
  <img src="image/homepage.png" alt="Giao diện chính PDF PRO" width="80%" style="border-radius: 12px; border: 1px solid #333;">
  <p><em>Giao diện chính với dark theme và các card tính năng</em></p>
</div>

<br>

<div align="center">
  <img src="image/tinhnang.png" alt="Tính năng chỉnh sửa PDF" width="80%" style="border-radius: 12px; border: 1px solid #333;">
  <p><em>Tính năng ghép file PDF</em></p>
</div>

<br>

<div align="center">
  <img src="image/contact.png" alt="Thông tin liên hệ" width="80%" style="border-radius: 12px; border: 1px solid #333;">
  <p><em>Trang thông tin liên hệ và thông tin ứng dụng</em></p>
</div>

---

## Landing Page

Truy cập landing page trực tuyến tại: [pdf-pro.vercel.app](https://pdf-pro.vercel.app) (nếu đã deploy)

Landing page được xây dựng với **Vite + React 18**, thiết kế dark theme chuyên nghiệp, đầy đủ thông tin sản phẩm và liên hệ tác giả.

```bash
cd landing-page
npm install
npm run dev      # Chạy local
npm run build    # Build production
npx vercel --prod  # Deploy lên Vercel
```

---

## Tính Năng

| STT | Tính Năng | Mô Tả |
|-----|-----------|-------|
| 1 | **Ghép File PDF** | Gộp nhiều file PDF thành một file duy nhất |
| 2 | **Sắp Xếp Trang** | Sắp xếp, xoay, xoá trang PDF theo ý muốn |
| 3 | **Chỉnh Sửa & Ký Tên** | Vẽ, thêm văn bản, ký tên trực tiếp lên PDF |
| 4 | **Tách Trang PDF** | Tách toàn bộ hoặc trích xuất trang theo lựa chọn |
| 5 | **Trích Xuất Văn Bản** | Trích xuất nội dung văn bản từ file PDF |
| 6 | **Xuất Ảnh Từ PDF** | Xuất hình ảnh từ các trang PDF |
| 7 | **Xuất PDF Sang Excel** | Chuyển đổi bảng biểu trong PDF sang file Excel |
| 8 | **Nén File PDF** | Giảm kích thước file PDF mà vẫn giữ chất lượng |

## Yêu Cầu Hệ Thống

- **Hệ điều hành:** Windows 10 / 11 (64-bit)
- **Dung lượng:** ~80 MB ổ đĩa cứng

## Cài Đặt

### Cách 1: Tải file chạy (Khuyến nghị)

Nhấn nút **Tải xuống PDF PRO** ở trên, mở file `.exe` và sử dụng ngay. Không cần cài đặt.

### Cách 2: Chạy từ mã nguồn

```bash
git clone https://github.com/HoaThang34/PDF_PRO.git
cd PDF-PRO
pip install -r requirements.txt
python main.py
```

## Công Nghệ Sử Dụng

| Công Nghệ | Mục Đích |
|-----------|----------|
| **Python** | Ngôn ngữ lập trình chính |
| **CustomTkinter** | GUI Framework (giao diện desktop hiện đại) |
| **PyMuPDF (fitz)** | Xử lý PDF (chỉnh sửa, ký, tách, trích xuất) |
| **pypdf** | Ghép và sắp xếp trang PDF |
| **Pillow** | Xử lý hình ảnh |
| **openpyxl** | Xuất dữ liệu PDF sang Excel |
| **PyInstaller** | Đóng gói thành file .exe |

## Giấy Phép

Dự án này được phân phối dưới giấy phép [MIT](LICENSE).

## Tác Giả

**HOA QUANG THANG** &copy; 2026

<div align="center">
  <img src="image/hoaquangthang.png" alt="Hoà Quang Thắng" width="120" height="120" style="border-radius: 50%;">
  <br>
  <strong>Hoà Quang Thắng</strong>
  <br>
  <a href="https://www.facebook.com/ThGThanG.734">Facebook</a> ·
  <a href="https://github.com/HoaThang34">GitHub</a> ·
  <a href="mailto:hoathang34.09@gmail.com">Email</a>
</div>
