import customtkinter as ctk
import tkinter as tk

from src.ui.themes.theme import COLORS, FONTS
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


FEATURES = [
    {"title": "Ghép File PDF",    "desc": "Kết hợp nhiều tệp PDF lại với nhau.",                       "color": COLORS["accent_purple"],  "icon_func": draw_merge_icon},
    {"title": "Sắp Xếp Trang",    "desc": "Xem trước, kéo thả sắp xếp lại các trang.",                "color": COLORS["accent_blue"],    "icon_func": draw_sort_icon},
    {"title": "Chỉnh Sửa & Ký Tên","desc": "Vẽ, chèn chữ, đóng dấu và ký tên trực tiếp lên PDF.",    "color": COLORS["accent_green"],   "icon_func": draw_edit_icon},
    {"title": "Tách Trang PDF",    "desc": "Trích xuất trang cụ thể hoặc chia nhỏ tài liệu.",         "color": COLORS["accent_teal"],    "icon_func": draw_split_icon},
    {"title": "Trích Xuất Văn Bản","desc": "Chuyển đổi PDF sang văn bản có thể chỉnh sửa.",           "color": COLORS["accent_orange"],  "icon_func": draw_extract_text_icon},
    {"title": "Xuất Ảnh Từ PDF",  "desc": "Chuyển đổi mỗi trang PDF thành hình ảnh chất lượng cao.",  "color": COLORS["accent_pink"],    "icon_func": draw_extract_image_icon},
    {"title": "Xuất PDF Sang Excel","desc": "Trích xuất bảng biểu từ PDF sang bảng tính Excel.",      "color": COLORS["accent_emerald"], "icon_func": draw_to_excel_icon},
    {"title": "Nén File PDF",      "desc": "Giảm dung lượng PDF mà vẫn giữ nguyên chất lượng.",        "color": COLORS["accent_cyan"],    "icon_func": draw_compress_icon},
]


class HomePage(ctk.CTkFrame):

    def __init__(self, master, on_feature_click=None, **kwargs):
        super().__init__(master, fg_color=COLORS["bg_primary"], **kwargs)
        self._on_feature_click = on_feature_click

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._scroll = ctk.CTkScrollableFrame(
            self, fg_color=COLORS["bg_primary"],
            scrollbar_button_color=COLORS["bg_tertiary"],
            scrollbar_button_hover_color=COLORS["border_hover"],
        )
        self._scroll.grid(row=0, column=0, sticky="nsew")
        self._scroll.grid_columnconfigure(0, weight=1)

        self._build_hero()
        self._build_section_label()
        self._build_tools()

    def _build_hero(self):
        hero = ctk.CTkFrame(self._scroll, fg_color="transparent")
        hero.grid(row=0, column=0, pady=(48, 0), sticky="ew")
        hero.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            hero, text="PDF PRO",
            font=("Segoe UI", 40, "bold"),
            text_color=COLORS["text_primary"],
        ).grid(row=0, column=0)

        ctk.CTkLabel(
            hero, text="Bộ công cụ chỉnh sửa PDF chuyên nghiệp — mọi thao tác đều chạy hoàn toàn trên máy của bạn.",
            font=FONTS["body"],
            text_color=COLORS["text_secondary"],
            justify="center",
        ).grid(row=1, column=0, pady=(8, 0))

    def _build_section_label(self):
        label = ctk.CTkLabel(
            self._scroll, text="Danh Sách Công Cụ",
            font=("Segoe UI", 13, "bold"),
            text_color=COLORS["text_muted"],
            anchor="w",
        )
        label.grid(row=2, column=0, padx=44, pady=(36, 12), sticky="w")

    def _build_tools(self):
        container = ctk.CTkFrame(self._scroll, fg_color="transparent")
        container.grid(row=3, column=0, padx=40, pady=(0, 48), sticky="ew")
        for col in range(4):
            container.grid_columnconfigure(col, weight=1, uniform="tool")

        for i, feat in enumerate(FEATURES):
            self._build_tool_item(container, i, feat)

    def _build_tool_item(self, parent, idx, feat):
        r, c = idx // 4, idx % 4
        is_merge = feat["title"] == "Ghép File PDF"

        card = ctk.CTkFrame(
            parent,
            fg_color=COLORS["bg_secondary"],
            corner_radius=14,
            border_width=2 if is_merge else 1,
            border_color=feat["color"] if is_merge else COLORS["border"],
            cursor="hand2",
        )
        card.grid(row=r, column=c, padx=6, pady=6, sticky="nsew")
        card.grid_columnconfigure(0, weight=1)

        icon_frame = ctk.CTkFrame(card, fg_color="transparent", height=64)
        icon_frame.grid(row=0, column=0, pady=(16, 0), sticky="ew")
        icon_frame.grid_propagate(False)

        icon_s = 36
        cv = tk.Canvas(
            icon_frame, width=icon_s, height=icon_s,
            bg=COLORS["bg_secondary"], highlightthickness=0, bd=0,
        )
        cv.pack()
        self._draw_icon_bg(cv, icon_s, feat["color"], 0.12)
        feat["icon_func"](cv, icon_s, feat["color"])

        title_label = ctk.CTkLabel(
            card, text=feat["title"],
            font=("Segoe UI", 14, "bold"),
            text_color=COLORS["text_primary"],
        )
        title_label.grid(row=1, column=0, pady=(10, 4))

        desc_label = ctk.CTkLabel(
            card, text=feat["desc"],
            font=("Segoe UI", 11),
            text_color=COLORS["text_secondary"],
            justify="center",
            wraplength=200,
        )
        desc_label.grid(row=2, column=0, padx=16, pady=(0, 16))

        def on_enter(e):
            card.configure(fg_color=COLORS["bg_tertiary"], border_color=feat["color"])
        def on_leave(e):
            card.configure(
                fg_color=COLORS["bg_secondary"],
                border_color=feat["color"] if is_merge else COLORS["border"],
            )
        def on_click(e):
            if self._on_feature_click:
                self._on_feature_click(feat["title"])

        for w in (card, cv, icon_frame, title_label, desc_label):
            w.bind("<Enter>", on_enter)
            w.bind("<Leave>", on_leave)
            w.bind("<Button-1>", on_click)

    def _draw_icon_bg(self, canvas, size, color, alpha):
        r = int(color[1:3], 16); g = int(color[3:5], 16); b = int(color[5:7], 16)
        br, bg, bb = 26, 27, 46
        nr = int(r * alpha + br * (1 - alpha))
        ng = int(g * alpha + bg * (1 - alpha))
        nb = int(b * alpha + bb * (1 - alpha))
        bg_hex = f"#{nr:02x}{ng:02x}{nb:02x}"
        pad2 = 2
        canvas.create_rectangle(pad2, pad2, size - pad2, size - pad2, fill=bg_hex, outline="", width=0)
