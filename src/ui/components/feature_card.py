import customtkinter as ctk
import tkinter as tk
import math

from src.ui.themes.theme import COLORS, FONTS, CARD


class FeatureCard(ctk.CTkFrame):
    """Card hiển thị một tính năng PDF với icon, tiêu đề, mô tả."""

    def __init__(self, master, title, description, icon_color, icon_draw_func, command=None, **kwargs):
        super().__init__(
            master,
            fg_color=COLORS["bg_secondary"],
            corner_radius=CARD["corner_radius"],
            border_width=1,
            border_color=COLORS["border"],
            **kwargs,
        )

        self._command = command
        self._icon_color = icon_color
        self._is_hovered = False

        self.configure(cursor="hand2")

        # Layout nội bộ
        self.grid_columnconfigure(0, weight=1)

        # Icon container
        icon_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            height=CARD["icon_size"] + 16,
        )
        icon_frame.grid(row=0, column=0, padx=20, pady=(20, 8), sticky="w")

        # Vẽ icon bằng Canvas
        self._icon_canvas = tk.Canvas(
            icon_frame,
            width=CARD["icon_size"],
            height=CARD["icon_size"],
            bg=self._hex_to_rgba(icon_color, 0.15),
            highlightthickness=0,
            bd=0,
        )
        self._icon_canvas.pack()
        self._draw_rounded_rect(self._icon_canvas, 0, 0, CARD["icon_size"], CARD["icon_size"], 10,
                                fill=self._hex_to_rgba(icon_color, 0.15), outline="")
        icon_draw_func(self._icon_canvas, CARD["icon_size"], icon_color)

        # Tiêu đề
        self._title_label = ctk.CTkLabel(
            self,
            text=title,
            font=FONTS["heading_sm"],
            text_color=COLORS["text_primary"],
            anchor="w",
        )
        self._title_label.grid(row=1, column=0, padx=20, pady=(4, 4), sticky="w")

        # Mô tả
        self._desc_label = ctk.CTkLabel(
            self,
            text=description,
            font=FONTS["body_sm"],
            text_color=COLORS["text_secondary"],
            anchor="w",
            justify="left",
            wraplength=200,
        )
        self._desc_label.grid(row=2, column=0, padx=20, pady=(0, 8), sticky="w")

        # Arrow button
        self._arrow_label = ctk.CTkLabel(
            self,
            text="→",
            font=("Segoe UI", 16),
            text_color=COLORS["text_muted"],
            anchor="w",
        )
        self._arrow_label.grid(row=3, column=0, padx=20, pady=(0, 16), sticky="w")

        # Bind events cho tất cả widget con
        self._bind_hover_events(self)
        self._bind_hover_events(icon_frame)
        self._bind_hover_events(self._icon_canvas)
        self._bind_hover_events(self._title_label)
        self._bind_hover_events(self._desc_label)
        self._bind_hover_events(self._arrow_label)

    def _bind_hover_events(self, widget):
        widget.bind("<Enter>", self._on_enter)
        widget.bind("<Leave>", self._on_leave)
        widget.bind("<Button-1>", self._on_click)

    def _on_enter(self, event):
        if not self._is_hovered:
            self._is_hovered = True
            self.configure(
                fg_color=COLORS["bg_tertiary"],
                border_color=COLORS["border_hover"],
            )
            self._arrow_label.configure(text_color=self._icon_color)

    def _on_leave(self, event):
        # Kiểm tra chuột có thực sự rời khỏi card
        x, y = self.winfo_pointerxy()
        widget_x = self.winfo_rootx()
        widget_y = self.winfo_rooty()
        widget_w = self.winfo_width()
        widget_h = self.winfo_height()

        if not (widget_x <= x <= widget_x + widget_w and widget_y <= y <= widget_y + widget_h):
            self._is_hovered = False
            self.configure(
                fg_color=COLORS["bg_secondary"],
                border_color=COLORS["border"],
            )
            self._arrow_label.configure(text_color=COLORS["text_muted"])

    def _on_click(self, event):
        if self._command:
            self._command()

    @staticmethod
    def _hex_to_rgba(hex_color, alpha):
        """Chuyển hex color sang dạng có alpha (tạo màu nhạt hơn trộn với nền tối)."""
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        bg_r, bg_g, bg_b = 26, 27, 46  # bg_secondary

        new_r = int(r * alpha + bg_r * (1 - alpha))
        new_g = int(g * alpha + bg_g * (1 - alpha))
        new_b = int(b * alpha + bg_b * (1 - alpha))

        return f"#{new_r:02x}{new_g:02x}{new_b:02x}"

    @staticmethod
    def _draw_rounded_rect(canvas, x1, y1, x2, y2, radius, **kwargs):
        """Vẽ hình chữ nhật bo góc trên Canvas."""
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1,
        ]
        canvas.create_polygon(points, smooth=True, **kwargs)
