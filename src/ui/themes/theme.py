# Theme configuration cho PDF PRO

# Bảng màu chính - Dark Theme
COLORS = {
    # Nền
    "bg_primary": "#0F1117",       # Nền chính (rất tối)
    "bg_secondary": "#1A1B2E",     # Nền card/panel
    "bg_tertiary": "#232438",      # Nền hover/active
    "bg_header": "#0F1117",        # Nền header
    "bg_footer": "#0A0B10",        # Nền footer

    # Văn bản
    "text_primary": "#FFFFFF",     # Trắng chính
    "text_secondary": "#A0A3B1",   # Xám nhạt
    "text_muted": "#6B6F80",       # Xám đậm

    # Accent - Màu icon cho từng tính năng
    "accent_purple": "#8B5CF6",    # Ghép File PDF
    "accent_blue": "#3B82F6",      # Sắp Xếp Trang
    "accent_green": "#10B981",     # Chỉnh Sửa & Ký Tên
    "accent_teal": "#14B8A6",      # Tách Trang PDF
    "accent_orange": "#F59E0B",    # Trích Xuất Văn Bản
    "accent_pink": "#EC4899",      # Xuất Ảnh Từ PDF
    "accent_emerald": "#34D399",   # Xuất PDF Sang Excel
    "accent_cyan": "#06B6D4",      # Nén File PDF

    # Gradient
    "gradient_start": "#8B5CF6",   # Tím
    "gradient_end": "#EC4899",     # Hồng

    # Border
    "border": "#2A2B3D",
    "border_hover": "#3D3F56",

    # Button
    "btn_primary": "#8B5CF6",
    "btn_hover": "#7C3AED",
}

# Typography
FONTS = {
    "family": "Segoe UI",
    "heading_xl": ("Segoe UI", 32, "bold"),
    "heading_lg": ("Segoe UI", 24, "bold"),
    "heading_md": ("Segoe UI", 18, "bold"),
    "heading_sm": ("Segoe UI", 14, "bold"),
    "body": ("Segoe UI", 13),
    "body_sm": ("Segoe UI", 11),
    "caption": ("Segoe UI", 10),
}

# Spacing (4px grid)
SPACING = {
    "xs": 4,
    "sm": 8,
    "md": 16,
    "lg": 24,
    "xl": 32,
    "xxl": 48,
}

# Kích thước cửa sổ
WINDOW = {
    "width": 1100,
    "height": 750,
    "min_width": 900,
    "min_height": 650,
}

# Kích thước card
CARD = {
    "width": 230,
    "height": 180,
    "corner_radius": 12,
    "icon_size": 44,
}
