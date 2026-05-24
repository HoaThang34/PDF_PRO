import sys
import os
import customtkinter as ctk
import tkinter as tk
from PIL import Image

from src.ui.themes.theme import COLORS, FONTS, SPACING, WINDOW
from src.ui.pages.home_page import HomePage
from src.ui.pages.merge_page import MergePage
from src.ui.pages.sort_page import SortPage
from src.ui.pages.edit_page import EditPage
from src.ui.pages.split_page import SplitPage
from src.ui.pages.extract_text_page import ExtractTextPage
from src.ui.pages.extract_image_page import ExtractImagePage
from src.ui.pages.to_excel_page import ToExcelPage
from src.ui.pages.compress_page import CompressPage
from src.ui.components.contact_dialog import ContactDialog


class PDFProApp(ctk.CTk):
    """Cửa sổ chính của ứng dụng PDF PRO."""

    def __init__(self):
        super().__init__()

        # Cấu hình cửa sổ
        self.title("PDF PRO - Bộ Công Cụ Chỉnh Sửa PDF Chuyên Nghiệp")
        self.geometry(f"{WINDOW['width']}x{WINDOW['height']}")
        self.minsize(WINDOW["min_width"], WINDOW["min_height"])

        # Dark theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.configure(fg_color=COLORS["bg_primary"])

        # Layout chính
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)  # Content area mở rộng

        self._current_feature_frame = None

        self._build_header()
        self._build_content()
        self._build_footer()

        # Bind phím Escape để quay về trang chủ
        self.bind_all("<Escape>", self._on_esc_pressed)

        # Đặt cửa sổ ở giữa màn hình
        self._center_window()

    def _center_window(self):
        """Đặt cửa sổ ở giữa màn hình."""
        self.update_idletasks()
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w - WINDOW["width"]) // 2
        y = (screen_h - WINDOW["height"]) // 2
        self.geometry(f"{WINDOW['width']}x{WINDOW['height']}+{x}+{y}")

    def _build_header(self):
        """Xây dựng thanh header với logo và navigation."""
        header = ctk.CTkFrame(
            self,
            fg_color=COLORS["bg_header"],
            height=60,
            corner_radius=0,
        )
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)
        header.grid_columnconfigure(1, weight=1)

        # Logo section
        logo_frame = ctk.CTkFrame(header, fg_color="transparent")
        logo_frame.grid(row=0, column=0, padx=24, pady=12, sticky="w")

        # Logo image
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        logo_pil = Image.open(logo_path)
        logo_ctk = ctk.CTkImage(light_image=logo_pil, dark_image=logo_pil, size=(36, 36))
        logo_label = ctk.CTkLabel(logo_frame, image=logo_ctk, text="")
        logo_label.pack(side="left", padx=(0, 10))

        # Tên app
        logo_text_frame = ctk.CTkFrame(logo_frame, fg_color="transparent")
        logo_text_frame.pack(side="left")

        app_name = ctk.CTkLabel(
            logo_text_frame,
            text="PDF PRO",
            font=("Segoe UI", 18, "bold"),
            text_color=COLORS["text_primary"],
        )
        app_name.pack(anchor="w")

        app_desc = ctk.CTkLabel(
            logo_text_frame,
            text="BỘ CÔNG CỤ CHỈNH SỬA FILE PDF CHUYÊN NGHIỆP",
            font=("Segoe UI", 8),
            text_color=COLORS["text_muted"],
        )
        app_desc.pack(anchor="w")

        # Navigation
        nav_frame = ctk.CTkFrame(header, fg_color="transparent")
        nav_frame.grid(row=0, column=1, pady=12)

        self._all_tools_btn = ctk.CTkButton(
            nav_frame,
            text="Tất Cả Công Cụ",
            font=("Segoe UI", 14, "bold"),
            text_color=COLORS["text_primary"],
            fg_color="transparent",
            hover_color=COLORS["bg_tertiary"],
            width=100,
            height=36,
            corner_radius=8,
            command=self._show_home,
        )
        self._all_tools_btn.pack()

    def _build_content(self):
        """Xây dựng vùng nội dung chính."""
        self._home_page = HomePage(
            self,
            on_feature_click=self._on_feature_selected,
        )
        self._home_page.grid(row=1, column=0, sticky="nsew")

    def _build_footer(self):
        """Xây dựng footer với thông tin bản quyền."""
        footer = ctk.CTkFrame(
            self,
            fg_color=COLORS["bg_footer"],
            height=50,
            corner_radius=0,
        )
        footer.grid(row=2, column=0, sticky="ew")
        footer.grid_propagate(False)
        footer.grid_columnconfigure(0, weight=1)
        footer.grid_columnconfigure(1, weight=1)

        # Bên trái - Logo và copyright
        left_frame = ctk.CTkFrame(footer, fg_color="transparent")
        left_frame.grid(row=0, column=0, padx=24, pady=10, sticky="w")

        brand = ctk.CTkLabel(
            left_frame,
            text="PDF PRO",
            font=("Segoe UI", 13, "bold"),
            text_color=COLORS["text_primary"],
        )
        brand.pack(side="left", padx=(0, 16))

        copyright_text = ctk.CTkLabel(
            left_frame,
            text="(C) 2026 - HOA QUANG THANG",
            font=FONTS["caption"],
            text_color=COLORS["text_muted"],
        )
        copyright_text.pack(side="left")

        # Bên phải - Links
        right_frame = ctk.CTkFrame(footer, fg_color="transparent")
        right_frame.grid(row=0, column=1, padx=24, pady=10, sticky="e")

        links = ["Chính sách bảo mật", "Điều khoản dịch vụ", "Liên hệ"]
        for link_text in links:
            link = ctk.CTkLabel(
                right_frame,
                text=link_text,
                font=FONTS["caption"],
                text_color=COLORS["text_muted"],
                cursor="hand2",
            )
            link.pack(side="left", padx=(16, 0))
            link.bind("<Enter>", lambda e, l=link: l.configure(text_color=COLORS["text_secondary"]))
            link.bind("<Leave>", lambda e, l=link: l.configure(text_color=COLORS["text_muted"]))
            link.bind("<Button-1>", lambda e, t=link_text: self._on_footer_link_click(t))

    def _on_feature_selected(self, feature_name):
        """Xử lý khi chọn một tính năng - chuyển đến trang tính năng."""
        if feature_name == "Ghép File PDF":
            self._open_feature_page(MergePage)
        elif feature_name == "Sắp Xếp Trang":
            self._open_feature_page(SortPage)
        elif feature_name == "Chỉnh Sửa & Ký Tên":
            self._open_feature_page(EditPage)
        elif feature_name == "Tách Trang PDF":
            self._open_feature_page(SplitPage)
        elif feature_name == "Trích Xuất Văn Bản":
            self._open_feature_page(ExtractTextPage)
        elif feature_name == "Xuất Ảnh Từ PDF":
            self._open_feature_page(ExtractImagePage)
        elif feature_name == "Xuất PDF Sang Excel":
            self._open_feature_page(ToExcelPage)
        elif feature_name == "Nén File PDF":
            self._open_feature_page(CompressPage)

    def _open_feature_page(self, page_class):
        """Mở một trang tính năng mới."""
        if self._current_feature_frame:
            self._current_feature_frame.destroy()
            self._current_feature_frame = None
        self._home_page.grid_forget()
        self._current_feature_frame = page_class(self, on_back=self._show_home)
        self._current_feature_frame.grid(row=1, column=0, sticky="nsew")

    def _show_home(self):
        """Quay về trang chủ."""
        if self._current_feature_frame:
            self._current_feature_frame.destroy()
            self._current_feature_frame = None
        self._home_page.grid(row=1, column=0, sticky="nsew")

    def _on_esc_pressed(self, event=None):
        """Xử lý khi nhấn phím Escape - quay về trang chủ."""
        self._show_home()

    def _on_footer_link_click(self, link_text):
        """Xử lý khi nhấn vào link ở footer."""
        if link_text == "Liên hệ":
            ContactDialog(self)


def main():
    app = PDFProApp()
    app.mainloop()


if __name__ == "__main__":
    main()
