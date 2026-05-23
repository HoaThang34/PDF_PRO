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
        "title": "Ghep File PDF",
        "description": "Ket hop nhieu tep PDF lai voi nhau theo thu tu mong muon mot cach de dang.",
        "color": COLORS["accent_purple"],
        "icon_func": draw_merge_icon,
    },
    {
        "title": "Sap Xep Trang",
        "description": "Xem truoc trang, keo tha sap xep lai, xoay goc hoac xoa cac trang khong mong muon.",
        "color": COLORS["accent_blue"],
        "icon_func": draw_sort_icon,
    },
    {
        "title": "Chinh Sua & Ky Ten",
        "description": "Ve tu do, chen chu, dong dau va ky ten truc tiep len tai lieu PDF cua ban.",
        "color": COLORS["accent_green"],
        "icon_func": draw_edit_icon,
    },
    {
        "title": "Tach Trang PDF",
        "description": "Trich xuat cac trang cu the hoac chia nho tai lieu thanh nhieu tep moi.",
        "color": COLORS["accent_teal"],
        "icon_func": draw_split_icon,
    },
    {
        "title": "Trich Xuat Van Ban",
        "description": "Chuyen doi PDF sang van ban co the chinh sua voi cong nghe OCR.",
        "color": COLORS["accent_orange"],
        "icon_func": draw_extract_text_icon,
    },
    {
        "title": "Xuat Anh Tu PDF",
        "description": "Chuyen doi moi trang PDF thanh mot tep hinh anh chat luong cao.",
        "color": COLORS["accent_pink"],
        "icon_func": draw_extract_image_icon,
    },
    {
        "title": "Xuat PDF Sang Excel",
        "description": "Tu dong trich xuat bang bieu tu PDF sang bang tinh Excel.",
        "color": COLORS["accent_emerald"],
        "icon_func": draw_to_excel_icon,
    },
    {
        "title": "Nen File PDF",
        "description": "Giam dung luong tep PDF ma van giu nguyen chat luong hien thi.",
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
            text="Xu Ly PDF",
            font=("Segoe UI", 36, "bold"),
            text_color=COLORS["gradient_start"],
        )
        title_line1.grid(row=0, column=0, pady=(0, 0))

        title_line2 = ctk.CTkLabel(
            hero_frame,
            text="Nhanh Chong & Bao Mat",
            font=("Segoe UI", 36, "bold"),
            text_color=COLORS["gradient_end"],
        )
        title_line2.grid(row=1, column=0, pady=(0, 16))

        # Mô tả phụ
        subtitle = ctk.CTkLabel(
            hero_frame,
            text="Moi thao tac thuc hien truc tiep tren may tinh cua ban.\n"
                 "Tep tin khong bao gio duoc gui len bat ky may chu nao.",
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
