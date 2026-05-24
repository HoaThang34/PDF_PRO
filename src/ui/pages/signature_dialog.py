import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageDraw

from src.ui.themes.theme import COLORS, FONTS


class SignatureDialog(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Ve Chu Ky")
        self.geometry("500x350")
        self.resizable(False, False)
        self.configure(fg_color=COLORS["bg_primary"])

        self.transient(master)
        self.grab_set()
        self._center_on_parent(master)

        self._result_image = None
        self._points = []

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
        ctk.CTkLabel(
            self, text="Ve chu ky cua ban bang chuot",
            font=FONTS["heading_sm"],
            text_color=COLORS["text_primary"],
        ).pack(pady=(16, 4))

        ctk.CTkLabel(
            self, text="Nhan giu va keo chuot de ve",
            font=FONTS["body_sm"],
            text_color=COLORS["text_muted"],
        ).pack(pady=(0, 10))

        canvas_frame = ctk.CTkFrame(self, fg_color=COLORS["bg_secondary"], corner_radius=8)
        canvas_frame.pack(padx=24, fill="both", expand=True)

        self._canvas = tk.Canvas(
            canvas_frame,
            bg="#FFFFFF",
            highlightthickness=0,
            bd=0,
            cursor="crosshair",
        )
        self._canvas.pack(fill="both", expand=True, padx=2, pady=2)

        self._canvas.bind("<Button-1>", self._on_press)
        self._canvas.bind("<B1-Motion>", self._on_move)
        self._canvas.bind("<ButtonRelease-1>", self._on_release)

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=(10, 16))

        ctk.CTkButton(
            btn_frame, text="Xoa",
            font=FONTS["body"],
            fg_color=COLORS["bg_tertiary"],
            text_color=COLORS["text_primary"],
            hover_color=COLORS["border_hover"],
            width=80, height=34, corner_radius=8,
            command=self._clear,
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            btn_frame, text="Dong",
            font=FONTS["body"],
            fg_color=COLORS["bg_tertiary"],
            text_color=COLORS["text_secondary"],
            hover_color=COLORS["border_hover"],
            width=80, height=34, corner_radius=8,
            command=self.destroy,
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            btn_frame, text="Xac Nhan",
            font=FONTS["heading_sm"],
            text_color="#FFFFFF",
            fg_color=COLORS["accent_green"],
            hover_color="#059669",
            width=100, height=34, corner_radius=8,
            command=self._confirm,
        ).pack(side="left", padx=(8, 0))

    def _on_press(self, event):
        self._current_stroke = [(event.x, event.y)]
        self._canvas.create_oval(
            event.x - 1, event.y - 1, event.x + 1, event.y + 1,
            fill="#000000", outline="", tags="sig",
        )

    def _on_move(self, event):
        if self._current_stroke is None:
            return
        last_x, last_y = self._current_stroke[-1]
        self._current_stroke.append((event.x, event.y))
        self._canvas.create_line(
            last_x, last_y, event.x, event.y,
            fill="#000000", width=3, capstyle="round", smooth=True, tags="sig",
        )

    def _on_release(self, event):
        if self._current_stroke:
            self._points.append(self._current_stroke)
            self._current_stroke = None

    def _clear(self):
        self._canvas.delete("sig")
        self._points.clear()
        self._current_stroke = None

    def _confirm(self):
        if not self._points:
            self.destroy()
            return
        img = Image.new("RGBA", (450, 200), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        for stroke in self._points:
            if len(stroke) < 2:
                continue
            for i in range(len(stroke) - 1):
                draw.line(
                    [stroke[i], stroke[i + 1]],
                    fill=(0, 0, 0, 255), width=5,
                )
        self._result_image = img
        self.destroy()

    def get_image(self):
        return self._result_image
