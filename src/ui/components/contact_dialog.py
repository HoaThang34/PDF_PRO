import webbrowser
import tkinter as tk
import customtkinter as ctk

from src.ui.themes.theme import COLORS, FONTS


class ContactDialog(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Liên Hệ")
        self.geometry("420x380")
        self.resizable(False, False)
        self.configure(fg_color=COLORS["bg_primary"])

        self.transient(master)
        self.grab_set()
        self._center_on_parent(master)

        self._build_ui()

    def _center_on_parent(self, master):
        self.update_idletasks()
        mx = master.winfo_rootx()
        my = master.winfo_rooty()
        mw = master.winfo_width()
        mh = master.winfo_height()
        dw = self.winfo_width()
        dh = self.winfo_height()
        x = mx + (mw - dw) // 2
        y = my + (mh - dh) // 2
        self.geometry(f"+{x}+{y}")

    def _build_ui(self):
        title = ctk.CTkLabel(
            self,
            text="Liên Hệ",
            font=("Segoe UI", 22, "bold"),
            text_color=COLORS["text_primary"],
        )
        title.pack(pady=(24, 20))

        contacts = [
            ("Facebook", "facebook.com/ThGThanG.734", "https://www.facebook.com/ThGThanG.734", COLORS["accent_blue"], True),
            ("GitHub", "github.com/HoaThang34", "https://github.com/HoaThang34", COLORS["text_primary"], True),
            ("Zalo", "0389823083", None, COLORS["accent_cyan"], False),
        ]

        for label, value, url, color, is_link in contacts:
            frame = ctk.CTkFrame(self, fg_color=COLORS["bg_secondary"], corner_radius=8)
            frame.pack(fill="x", padx=32, pady=6)

            name = ctk.CTkLabel(
                frame,
                text=label,
                font=("Segoe UI", 13, "bold"),
                text_color=color,
            )
            name.pack(side="left", padx=(16, 12), pady=14)

            if is_link and url:
                link = ctk.CTkLabel(
                    frame,
                    text=value,
                    font=("Segoe UI", 12),
                    text_color=COLORS["text_secondary"],
                    cursor="hand2",
                )
                link.pack(side="left", pady=14)
                link.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))
                link.bind("<Enter>", lambda e, l=link: l.configure(text_color=COLORS["text_primary"]))
                link.bind("<Leave>", lambda e, l=link: l.configure(text_color=COLORS["text_secondary"]))
            else:
                phone_frame = ctk.CTkFrame(frame, fg_color="transparent")
                phone_frame.pack(side="left", fill="x", expand=True, pady=14)

                phone_label = ctk.CTkLabel(
                    phone_frame,
                    text=value,
                    font=("Segoe UI", 12),
                    text_color=COLORS["text_secondary"],
                )
                phone_label.pack(side="left")

                copy_btn = ctk.CTkButton(
                    phone_frame,
                    text="Sao chép",
                    font=("Segoe UI", 10),
                    text_color=COLORS["text_primary"],
                    fg_color=COLORS["bg_tertiary"],
                    hover_color=COLORS["border_hover"],
                    width=70,
                    height=24,
                    corner_radius=4,
                    command=lambda v=value: self._copy_text(v),
                )
                copy_btn.pack(side="right", padx=(0, 12))

        close_btn = ctk.CTkButton(
            self,
            text="Đóng",
            font=("Segoe UI", 13),
            fg_color=COLORS["btn_primary"],
            hover_color=COLORS["btn_hover"],
            command=self.destroy,
            width=120,
            height=36,
            corner_radius=8,
        )
        close_btn.pack(pady=(12, 20))

    def _copy_text(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
