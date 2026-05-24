# PDF PRO - Cấu Hình Dự Án

## Thông Tin Chung
- **Tên dự án:** PDF PRO
- **Mô tả:** Bộ công cụ chỉnh sửa PDF chuyên nghiệp
- **Ngôn ngữ:** Python
- **GUI Framework:** CustomTkinter
- **Tác giả:** HOA QUANG THANG
- **Năm:** 2026

## Cấu Trúc Thư Mục
```
PDF-PRO/
├── .rules/              # Quy định dự án
├── docs/                # Tài liệu & cấu hình
├── src/                 # Mã nguồn chính
│   ├── assets/          # Tài nguyên (icon SVG, hình ảnh)
│   │   └── icons/       # Icon SVG cho các tính năng
│   ├── ui/              # Giao diện người dùng
│   │   ├── components/  # Các component tái sử dụng
│   │   ├── pages/       # Các trang tính năng
│   │   └── themes/      # Cấu hình theme
│   ├── core/            # Logic xử lý PDF
│   └── utils/           # Tiện ích
├── main.py              # Entry point
└── requirements.txt     # Thư viện cần thiết
```

## Danh Sách Tính Năng
| STT | Tính Năng          | Trạng Thái |
|-----|--------------------|------------|
| 1   | Ghép File PDF      | Đã phát triển |
| 2   | Sắp Xếp Trang     | Đã phát triển |
| 3   | Chỉnh Sửa & Ký Tên | Đã phát triển |
| 4   | Tách Trang PDF     | Đã phát triển |
| 5   | Trích Xuất Văn Bản | Chưa phát triển |
| 6   | Xuất Ảnh Từ PDF    | Chưa phát triển |
| 7   | Xuất PDF Sang Excel | Chưa phát triển |
| 8   | Nén File PDF       | Chưa phát triển |

## Thư Viện Sử Dụng
| Thư Viện       | Phiên Bản | Mục Đích           |
|----------------|-----------|---------------------|
| customtkinter  | 5.2.2     | GUI Framework       |
| Pillow         | 11.2.1    | Xử lý hình ảnh     |
| pypdf          | 5.4.0     | Ghép & sắp xếp PDF |
| PyMuPDF        | 1.25.5    | Chỉnh sửa & ký tên |

## Ghi Chú Phát Triển
- **23/05/2026:** Khởi tạo dự án, xây dựng giao diện ban đầu (khung UI)
- **24/05/2026:** Phát triển tính năng Chỉnh Sửa & Ký Tên (EditPage + SignatureDialog + pdf_edit.py)
