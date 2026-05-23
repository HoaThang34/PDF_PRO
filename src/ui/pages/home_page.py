import customtkinter as ctk
import tkinter as tk

from src.ui.themes.theme import COLORS, FONTS, SPACING, CARD
from src.ui.components.feature_card import FeatureCard
from src.ui.components.icon_renderer import (
    draw_merge_icon,
    draw_sort_icon,
    draw_edit_icon,
    draw_split_icon,
    draw_extract_text_icon,
    draw_extract_image_icon,
    draw_to_excel_icon,
    draw_compress_icon,
)


# Cấu hình 8 tính năng
FEATURES = [
    {
        "title": "Ghép File PDF",
        "description": "Kết hợp nhiều tệp PDF lại với nhau theo thứ tự mong muốn một cách dễ dàng.",
        "color": COLORS["accent_purple"],
        "icon_func": draw_merge_icon,
    },
    {
        "title": "Sắp Xếp Trang",
        "description": "Xem trước trang, kéo thả sắp xếp lại, xoay góc hoặc xóa các trang không mong muốn.",
        "color": COLORS["accent_blue"],
        "icon_func": draw_sort_icon,
    },
    {
        "title": "Chỉnh Sửa & Ký Tên",
        "description": "Vẽ tự do, chèn chữ, đóng dấu và ký tên trực tiếp lên tài liệu PDF của bạn.",
        "color": COLORS["accent_green"],
        "icon_func": draw_edit_icon,
    },
    {
        "title": "Tách Trang PDF",
        "description": "Trích xuất các trang cụ thể hoặc chia nhỏ tài liệu thành nhiều tệp mới.",
        "color": COLORS["accent_teal"],
        "icon_func": draw_split_icon,
    },
    {
        "title": "Trích Xuất Văn Bản",
        "description": "Chuyển đổi PDF sang văn bản có thể chỉnh sửa với công nghệ OCR.",
        "color": COLORS["accent_orange"],
        "icon_func": draw_extract_text_icon,
    },
    {
        "title": "Xuất Ảnh Từ PDF",
        "description": "Chuyển đổi mỗi trang PDF thành một tệp hình ảnh chất lượng cao.",
        "color": COLORS["accent_pink"],
        "icon_func": draw_extract_image_icon,
    },
    {
        "title": "Xuất PDF Sang Excel",
        "description": "Tự động trích xuất bảng biểu từ PDF sang bảng tính Excel.",
        "color": COLORS["accent_emerald"],
        "icon_func": draw_to_excel_icon,
    },
    {
        "title": "Nén File PDF",
        "description": "Giảm dung lượng tệp PDF mà vẫn giữ nguyên chất lượng hiển thị.",
        "color": COLORS["accent_cyan"],
        "icon_func": draw_compress_icon,
    },
]


class HomePage(ctk.CTkFrame):
    """Trang chủ hiển thị tất cả tính năng PDF PRO."""

    def __init__(self, master, on_feature_click=None, **kwargs):
        super().__init__(master, fg_color=COLORS["bg_primary"], **kwargs)

        self._on_feature_click = on_feature_click

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Scrollable content area
        self._scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=COLORS["bg_primary"],
            scrollbar_button_color=COLORS["bg_tertiary"],
            scrollbar_button_hover_color=COLORS["border_hover"],
        )
        self._scroll_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self._scroll_frame.grid_columnconfigure(0, weight=1)

        self._build_hero_section()
        self._build_features_grid()

    def _build_hero_section(self):
        """Xây dựng phần hero - tiêu đề và mô tả chính."""
        hero_frame = ctk.CTkFrame(self._scroll_frame, fg_color="transparent")
        hero_frame.grid(row=0, column=0, pady=(40, 30), sticky="ew")
        hero_frame.grid_columnconfigure(0, weight=1)

        # Tiêu đề chính với gradient text (dùng 2 label mô phỏng)
        title_line1 = ctk.CTkLabel(
            hero_frame,
            text="Xử Lý PDF",
            font=("Segoe UI", 36, "bold"),
            text_color=COLORS["gradient_start"],
        )
        title_line1.grid(row=0, column=0, pady=(0, 0))

        title_line2 = ctk.CTkLabel(
            hero_frame,
            text="Nhanh Chóng & Bảo Mật",
            font=("Segoe UI", 36, "bold"),
            text_color=COLORS["gradient_end"],
        )
        title_line2.grid(row=1, column=0, pady=(0, 16))

        # Mô tả phụ
        subtitle = ctk.CTkLabel(
            hero_frame,
            text="Mọi thao tác thực hiện trực tiếp trên máy tính của bạn.\n"
                 "Tệp tin không bao giờ được gửi lên bất kỳ máy chủ nào.",
            font=FONTS["body"],
            text_color=COLORS["text_secondary"],
            justify="center",
        )
        subtitle.grid(row=2, column=0, pady=(0, 0))

    def _build_features_grid(self):
        """Xây dựng lưới các card tính năng 4 cột."""
        grid_frame = ctk.CTkFrame(self._scroll_frame, fg_color="transparent")
        grid_frame.grid(row=1, column=0, padx=40, pady=(10, 40), sticky="ew")

        # Cấu hình 4 cột
        for col in range(4):
            grid_frame.grid_columnconfigure(col, weight=1, uniform="card")

        for idx, feature in enumerate(FEATURES):
            row = idx // 4
            col = idx % 4

            card = FeatureCard(
                master=grid_frame,
                title=feature["title"],
                description=feature["description"],
                icon_color=feature["color"],
                icon_draw_func=feature["icon_func"],
                command=lambda f=feature: self._handle_feature_click(f),
            )
            card.grid(
                row=row, column=col,
                padx=SPACING["sm"],
                pady=SPACING["sm"],
                sticky="nsew",
            )

    def _handle_feature_click(self, feature):
        """Xử lý khi nhấn vào một card tính năng."""
        if self._on_feature_click:
            self._on_feature_click(feature["title"])
