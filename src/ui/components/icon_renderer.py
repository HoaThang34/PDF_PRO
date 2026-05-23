"""Module vẽ icon SVG-style trên tkinter Canvas cho từng tính năng."""
import math


def draw_merge_icon(canvas, size, color):
    """Icon Ghép File PDF - biểu tượng file kết hợp."""
    pad = size * 0.22
    cx, cy = size / 2, size / 2

    # File phía sau
    canvas.create_rectangle(
        pad + 2, pad, size - pad + 2, size - pad,
        outline=color, width=1.5, fill=""
    )
    # File phía trước
    canvas.create_rectangle(
        pad - 2, pad + 3, size - pad - 2, size - pad + 3,
        outline=color, width=1.5, fill=""
    )
    # Mũi tên xuống ở giữa
    canvas.create_line(cx, cy - 4, cx, cy + 6, fill=color, width=2)
    canvas.create_line(cx - 4, cy + 2, cx, cy + 6, fill=color, width=2)
    canvas.create_line(cx + 4, cy + 2, cx, cy + 6, fill=color, width=2)


def draw_sort_icon(canvas, size, color):
    """Icon Sắp Xếp Trang - lưới 2x2."""
    pad = size * 0.2
    gap = 3
    cell_w = (size - 2 * pad - gap) / 2
    cell_h = (size - 2 * pad - gap) / 2

    for row in range(2):
        for col in range(2):
            x1 = pad + col * (cell_w + gap)
            y1 = pad + row * (cell_h + gap)
            canvas.create_rectangle(
                x1, y1, x1 + cell_w, y1 + cell_h,
                outline=color, width=1.5, fill=""
            )


def draw_edit_icon(canvas, size, color):
    """Icon Chỉnh Sửa & Ký Tên - bút chỉnh sửa."""
    pad = size * 0.2

    # Khung giấy
    canvas.create_rectangle(
        pad, pad + 2, size * 0.6, size - pad,
        outline=color, width=1.5, fill=""
    )
    # Bút
    canvas.create_line(
        size * 0.5, size * 0.25,
        size - pad, size * 0.65,
        fill=color, width=2
    )
    canvas.create_line(
        size * 0.55, size * 0.3,
        size - pad + 2, size * 0.7,
        fill=color, width=2
    )


def draw_split_icon(canvas, size, color):
    """Icon Tách Trang PDF - file với đường cắt."""
    pad = size * 0.22
    cx = size / 2

    # File
    canvas.create_rectangle(
        pad, pad, size - pad, size - pad,
        outline=color, width=1.5, fill=""
    )
    # Đường cắt ngang
    dash_y = size / 2
    canvas.create_line(
        pad - 2, dash_y, size - pad + 2, dash_y,
        fill=color, width=1.5, dash=(4, 3)
    )
    # Mũi tên lên
    canvas.create_line(cx, dash_y - 3, cx, pad + 4, fill=color, width=1.5)
    canvas.create_line(cx - 3, pad + 7, cx, pad + 4, fill=color, width=1.5)
    canvas.create_line(cx + 3, pad + 7, cx, pad + 4, fill=color, width=1.5)
    # Mũi tên xuống
    canvas.create_line(cx, dash_y + 3, cx, size - pad - 4, fill=color, width=1.5)
    canvas.create_line(cx - 3, size - pad - 7, cx, size - pad - 4, fill=color, width=1.5)
    canvas.create_line(cx + 3, size - pad - 7, cx, size - pad - 4, fill=color, width=1.5)


def draw_extract_text_icon(canvas, size, color):
    """Icon Trích Xuất Văn Bản - file với dòng text."""
    pad = size * 0.22

    # File
    canvas.create_rectangle(
        pad, pad, size - pad, size - pad,
        outline=color, width=1.5, fill=""
    )
    # Các dòng text
    line_pad = pad + 5
    for i, w_ratio in enumerate([0.65, 0.5, 0.55]):
        y = pad + 8 + i * 6
        canvas.create_line(
            line_pad, y, line_pad + (size - 2 * pad - 10) * w_ratio, y,
            fill=color, width=1.5
        )


def draw_extract_image_icon(canvas, size, color):
    """Icon Xuất Ảnh Từ PDF - khung ảnh với núi."""
    pad = size * 0.2

    # Khung ảnh
    canvas.create_rectangle(
        pad, pad, size - pad, size - pad,
        outline=color, width=1.5, fill=""
    )
    # Mặt trời
    canvas.create_oval(
        pad + 5, pad + 5, pad + 12, pad + 12,
        outline=color, width=1.5, fill=""
    )
    # Núi
    canvas.create_line(
        pad + 2, size - pad - 3,
        size * 0.45, size * 0.5,
        size - pad - 2, size - pad - 3,
        fill=color, width=1.5
    )


def draw_to_excel_icon(canvas, size, color):
    """Icon Xuất PDF Sang Excel - bảng lưới."""
    pad = size * 0.2
    w = size - 2 * pad
    h = size - 2 * pad

    # Khung ngoài
    canvas.create_rectangle(
        pad, pad, size - pad, size - pad,
        outline=color, width=1.5, fill=""
    )
    # Đường dọc
    canvas.create_line(pad + w / 3, pad, pad + w / 3, size - pad, fill=color, width=1)
    canvas.create_line(pad + 2 * w / 3, pad, pad + 2 * w / 3, size - pad, fill=color, width=1)
    # Đường ngang
    canvas.create_line(pad, pad + h / 3, size - pad, pad + h / 3, fill=color, width=1)
    canvas.create_line(pad, pad + 2 * h / 3, size - pad, pad + 2 * h / 3, fill=color, width=1)


def draw_compress_icon(canvas, size, color):
    """Icon Nén File PDF - mũi tên thu nhỏ."""
    pad = size * 0.2
    cx, cy = size / 2, size / 2

    # Mũi tên từ góc trên-phải vào giữa
    canvas.create_line(size - pad, pad, cx + 2, cy - 2, fill=color, width=2, arrow="last")
    # Mũi tên từ góc dưới-trái vào giữa
    canvas.create_line(pad, size - pad, cx - 2, cy + 2, fill=color, width=2, arrow="last")
    # Đường gạch ở góc
    canvas.create_line(size - pad, pad, size - pad - 6, pad, fill=color, width=1.5)
    canvas.create_line(size - pad, pad, size - pad, pad + 6, fill=color, width=1.5)
    canvas.create_line(pad, size - pad, pad + 6, size - pad, fill=color, width=1.5)
    canvas.create_line(pad, size - pad, pad, size - pad - 6, fill=color, width=1.5)
