import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import os
import io
from threading import Thread

from src.ui.themes.theme import COLORS, FONTS, SPACING
from src.core.pdf_edit import (
    open_pdf, render_page, get_page_size, apply_edits_to_pdf,
)
from src.ui.pages.signature_dialog import SignatureDialog


COLOR_SWATCHES = [
    "#000000", "#FFFFFF", "#EF4444", "#F59E0B",
    "#10B981", "#3B82F6", "#8B5CF6", "#EC4899",
]
PEN_WIDTHS = [1, 2, 4, 6, 10]


class EditPage(ctk.CTkFrame):

    def __init__(self, master, on_back=None):
        super().__init__(master, fg_color=COLORS["bg_primary"])

        self._on_back = on_back
        self._pdf_path = None
        self._page_count = 0
        self._current_page = 0
        self._page_width = 612
        self._page_height = 792
        self._zoom = 1.0
        self._fit_zoom = 1.0

        self._all_edits = {}
        self._current_stroke = None
        self._edit_counter = 0

        self._active_tool = "pen"
        self._pen_color = "#000000"
        self._pen_width = 3
        self._zoom = 0

        self._signature_image = None
        self._signature_photos = {}
        self._page_photo = None
        self._thumb_photos = {}
        self._is_saving = False

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self._build_content()
        self._build_bottom_bar()

    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color="transparent", height=50)
        header.grid(row=0, column=0, padx=SPACING["lg"], pady=(SPACING["lg"], 0), sticky="ew")
        header.grid_propagate(False)
        header.grid_columnconfigure(1, weight=1)

        back_btn = ctk.CTkButton(
            header, text="\u2190 Quay L\u1ea1i",
            font=FONTS["body"],
            text_color=COLORS["text_secondary"],
            fg_color="transparent", hover_color=COLORS["bg_tertiary"],
            width=100, height=36, corner_radius=8, command=self._on_back,
        )
        back_btn.grid(row=0, column=0, sticky="w")

        title = ctk.CTkLabel(
            header, text="Ch\u1ec9nh S\u1eeda & K\u00fd T\u00ean",
            font=FONTS["heading_lg"], text_color=COLORS["accent_green"],
        )
        title.grid(row=0, column=1)

        btn_frame = ctk.CTkFrame(header, fg_color="transparent")
        btn_frame.grid(row=0, column=2, sticky="e")

        self._open_btn = ctk.CTkButton(
            btn_frame, text="+ M\u1edf PDF",
            font=FONTS["heading_sm"], text_color="#FFFFFF",
            fg_color=COLORS["accent_green"], hover_color="#059669",
            height=36, corner_radius=8, command=self._open_pdf,
        )
        self._open_btn.pack(side="left", padx=(0, 8))

        self._save_btn = ctk.CTkButton(
            btn_frame, text="L\u01b0u PDF",
            font=FONTS["heading_sm"], text_color="#FFFFFF",
            fg_color=COLORS["accent_blue"], hover_color="#2563EB",
            height=36, corner_radius=8, state="disabled", command=self._start_save,
        )
        self._save_btn.pack(side="left")

    def _build_content(self):
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=1, column=0, padx=SPACING["lg"], pady=SPACING["md"], sticky="nsew")
        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(1, weight=1)

        self._build_toolbar(content)
        self._build_canvas_area(content)
        self._show_placeholder()

    def _build_toolbar(self, parent):
        toolbar = ctk.CTkScrollableFrame(
            parent, fg_color=COLORS["bg_secondary"],
            corner_radius=12, width=160,
        )
        toolbar.grid(row=0, column=0, sticky="ns", padx=(0, SPACING["md"]))

        ctk.CTkLabel(
            toolbar, text="C\u00f4ng C\u1ee5",
            font=FONTS["heading_sm"], text_color=COLORS["text_muted"],
        ).grid(row=0, column=0, padx=12, pady=(14, 8), sticky="w")

        self._tool_pen = ctk.CTkButton(
            toolbar, text="\u270e B\u00fat",
            font=FONTS["body"],
            text_color="#FFFFFF", fg_color=COLORS["accent_green"],
            hover_color="#059669", height=34, corner_radius=8,
            command=lambda: self._set_tool("pen"),
        )
        self._tool_pen.grid(row=1, column=0, padx=12, pady=3, sticky="ew")

        self._tool_text = ctk.CTkButton(
            toolbar, text="T Ch\u1eef",
            font=FONTS["body"],
            text_color=COLORS["text_primary"], fg_color=COLORS["bg_tertiary"],
            hover_color=COLORS["border_hover"], height=34, corner_radius=8,
            command=lambda: self._set_tool("text"),
        )
        self._tool_text.grid(row=2, column=0, padx=12, pady=3, sticky="ew")

        self._tool_sig = ctk.CTkButton(
            toolbar, text="\u270d K\u00fd",
            font=FONTS["body"],
            text_color=COLORS["text_primary"], fg_color=COLORS["bg_tertiary"],
            hover_color=COLORS["border_hover"], height=34, corner_radius=8,
            command=self._activate_signature,
        )
        self._tool_sig.grid(row=3, column=0, padx=12, pady=3, sticky="ew")

        sep = ctk.CTkFrame(toolbar, fg_color=COLORS["border"], height=1)
        sep.grid(row=4, column=0, padx=12, pady=(12, 8), sticky="ew")

        ctk.CTkLabel(
            toolbar, text="M\u00e0u S\u1eafc",
            font=FONTS["body_sm"], text_color=COLORS["text_muted"],
        ).grid(row=5, column=0, padx=12, pady=(0, 6), sticky="w")

        self._color_btns = []
        color_frame = ctk.CTkFrame(toolbar, fg_color="transparent")
        color_frame.grid(row=6, column=0, padx=8, pady=(0, 8), sticky="ew")
        for ci, col in enumerate(COLOR_SWATCHES):
            r, c = ci // 4, ci % 4
            btn = tk.Canvas(
                color_frame, width=22, height=22,
                bg=COLORS["bg_secondary"], highlightthickness=0, bd=0, cursor="hand2",
            )
            btn.grid(row=r, column=c, padx=2, pady=2)
            border = "#FFFFFF" if col == "#000000" else COLORS["border"]
            btn.create_oval(2, 2, 20, 20, fill=col, outline=border, width=1)
            btn.bind("<Button-1>", lambda e, c=col: self._set_color(c))
            self._color_btns.append(btn)

        sep2 = ctk.CTkFrame(toolbar, fg_color=COLORS["border"], height=1)
        sep2.grid(row=7, column=0, padx=12, pady=(8, 8), sticky="ew")

        ctk.CTkLabel(
            toolbar, text="\u0110\u1ed9 D\u00e0y",
            font=FONTS["body_sm"], text_color=COLORS["text_muted"],
        ).grid(row=8, column=0, padx=12, pady=(0, 4), sticky="w")

        self._size_var = tk.IntVar(value=3)
        self._size_slider = ctk.CTkSlider(
            toolbar, from_=1, to=5, number_of_steps=4,
            variable=self._size_var, command=self._on_size_change,
            fg_color=COLORS["bg_tertiary"], progress_color=COLORS["accent_green"],
            height=16,
        )
        self._size_slider.grid(row=9, column=0, padx=12, pady=(0, 4), sticky="ew")

        self._size_label = ctk.CTkLabel(
            toolbar, text="3px",
            font=FONTS["body_sm"], text_color=COLORS["text_secondary"],
        )
        self._size_label.grid(row=10, column=0, padx=12, sticky="w")

        sep3 = ctk.CTkFrame(toolbar, fg_color=COLORS["border"], height=1)
        sep3.grid(row=11, column=0, padx=12, pady=(12, 8), sticky="ew")

        self._undo_btn = ctk.CTkButton(
            toolbar, text="\u21a9 Ho\u00e0n T\u00e1c",
            font=FONTS["body"],
            text_color=COLORS["text_primary"], fg_color=COLORS["bg_tertiary"],
            hover_color=COLORS["border_hover"], height=34, corner_radius=8,
            state="disabled", command=self._undo,
        )
        self._undo_btn.grid(row=12, column=0, padx=12, pady=3, sticky="ew")

        self._clear_page_btn = ctk.CTkButton(
            toolbar, text="\u2716 X\u00f3a Trang",
            font=FONTS["body"],
            text_color=COLORS["text_muted"], fg_color="transparent",
            hover_color=COLORS["bg_tertiary"], height=34, corner_radius=8,
            state="disabled", command=self._clear_page,
        )
        self._clear_page_btn.grid(row=13, column=0, padx=12, pady=3, sticky="ew")

    def _build_canvas_area(self, parent):
        canvas_container = ctk.CTkFrame(parent, fg_color=COLORS["bg_secondary"], corner_radius=12)
        canvas_container.grid(row=0, column=1, sticky="nsew")
        canvas_container.grid_rowconfigure(0, weight=1)
        canvas_container.grid_columnconfigure(0, weight=1)

        self._canvas = tk.Canvas(
            canvas_container,
            bg=COLORS["bg_secondary"],
            highlightthickness=0, bd=0,
            cursor="crosshair",
        )
        self._canvas.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        self._canvas.bind("<Button-1>", self._on_canvas_press)
        self._canvas.bind("<B1-Motion>", self._on_canvas_move)
        self._canvas.bind("<ButtonRelease-1>", self._on_canvas_release)

        self._canvas_container = canvas_container
        self._canvas.bind("<Configure>", lambda e: self._on_canvas_resize())

    def _on_canvas_resize(self):
        if self._pdf_path:
            self._load_and_render()

    def _build_bottom_bar(self):
        bottom = ctk.CTkFrame(self, fg_color="transparent")
        bottom.grid(row=2, column=0, padx=SPACING["lg"], pady=(0, SPACING["lg"]), sticky="ew")
        bottom.grid_columnconfigure(0, weight=1)

        self._thumb_frame = ctk.CTkScrollableFrame(
            bottom, fg_color=COLORS["bg_secondary"],
            corner_radius=8, height=100, orientation="horizontal",
        )
        self._thumb_frame.grid(row=0, column=0, padx=(0, 12), sticky="ew")
        self._thumb_frame.grid_columnconfigure(0, weight=1)

        right_frame = ctk.CTkFrame(bottom, fg_color="transparent")
        right_frame.grid(row=0, column=1, sticky="e")

        self._page_label = ctk.CTkLabel(
            right_frame,
            text="Ch\u01b0a m\u1edf t\u1ec7p",
            font=FONTS["body_sm"], text_color=COLORS["text_muted"],
        )
        self._page_label.pack(side="left", padx=(0, 8))

        self._zoom_out_btn = ctk.CTkButton(
            right_frame, text="\u2212", width=32, height=28,
            fg_color=COLORS["bg_tertiary"], text_color=COLORS["text_primary"],
            hover_color=COLORS["border_hover"], corner_radius=6,
            command=self._zoom_out,
        )
        self._zoom_out_btn.pack(side="left", padx=2)

        self._zoom_label = ctk.CTkLabel(
            right_frame, text="100%",
            font=FONTS["body_sm"], text_color=COLORS["text_secondary"],
            width=44,
        )
        self._zoom_label.pack(side="left", padx=2)

        self._zoom_in_btn = ctk.CTkButton(
            right_frame, text="+", width=32, height=28,
            fg_color=COLORS["bg_tertiary"], text_color=COLORS["text_primary"],
            hover_color=COLORS["border_hover"], corner_radius=6,
            command=self._zoom_in,
        )
        self._zoom_in_btn.pack(side="left", padx=2)

    def _show_placeholder(self):
        self._canvas.delete("all")
        cw = self._canvas.winfo_width() or 600
        ch = self._canvas.winfo_height() or 400
        cx, cy = cw / 2, ch / 2

        self._canvas.create_text(
            cx, cy - 20,
            text="Ch\u01b0a c\u00f3 t\u1ec7p PDF n\u00e0o",
            fill=COLORS["text_muted"],
            font=("Segoe UI", 16),
            tags="placeholder",
        )
        self._canvas.create_text(
            cx, cy + 16,
            text="Nh\u1ea5n '+ M\u1edf PDF' \u0111\u1ec3 b\u1eaft \u0111\u1ea7u",
            fill=COLORS["text_secondary"],
            font=("Segoe UI", 12),
            tags="placeholder",
        )

    def _set_tool(self, tool):
        self._active_tool = tool
        normal_cfg = {"text_color": COLORS["text_primary"], "fg_color": COLORS["bg_tertiary"]}
        active_cfg = {"text_color": "#FFFFFF", "fg_color": COLORS["accent_green"]}
        self._tool_pen.configure(**active_cfg if tool == "pen" else normal_cfg)
        self._tool_text.configure(**active_cfg if tool == "text" else normal_cfg)
        self._tool_sig.configure(**active_cfg if tool == "signature" else normal_cfg)
        cursor = "crosshair" if tool == "pen" else "xterm" if tool == "text" else "target"
        self._canvas.configure(cursor=cursor)

    def _set_color(self, color):
        self._pen_color = color

    def _on_size_change(self, val):
        idx = max(0, min(int(round(val)) - 1, len(PEN_WIDTHS) - 1))
        self._pen_width = PEN_WIDTHS[idx]
        self._size_label.configure(text=f"{self._pen_width}px")

    def _activate_signature(self):
        self._set_tool("signature")
        if self._signature_image is None:
            dlg = SignatureDialog(self)
            self.wait_window(dlg)
            self._signature_image = dlg.get_image()
            if self._signature_image is None:
                self._set_tool("pen")

    def _open_pdf(self):
        path = filedialog.askopenfilename(
            title="Ch\u1ecdn file PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if not path:
            return

        try:
            info = open_pdf(path)
            self._pdf_path = path
            self._page_count = info["page_count"]
            self._current_page = 0
            self._all_edits.clear()
            self._signature_photos.clear()
            self._edit_counter = 0
            self._current_stroke = None

            pw, ph = get_page_size(path, 0)
            self._page_width = pw
            self._page_height = ph

            self._save_btn.configure(state="normal" if self._page_count > 0 else "disabled")
            self._load_and_render()
            self._build_thumbnails()
        except Exception as e:
            messagebox.showerror("L\u1ed7i", f"Kh\u00f4ng th\u1ec3 m\u1edf file PDF:\n\n{str(e)}")

    def _load_and_render(self):
        if not self._pdf_path:
            return

        cw = self._canvas.winfo_width() or 600
        ch = self._canvas.winfo_height() or 400
        margin = 20
        avail_w = cw - margin * 2
        avail_h = ch - margin * 2

        fit_zoom = min(avail_w / self._page_width, avail_h / self._page_height, 2.0)
        if self._zoom <= 0 or self._zoom > 2.0:
            self._zoom = fit_zoom
        self._fit_zoom = fit_zoom

        zoom = self._zoom
        img = render_page(self._pdf_path, self._current_page, zoom)
        self._page_photo = ImageTk.PhotoImage(img)

        self._canvas.delete("all")
        img_w, img_h = img.width, img.height
        ox = (cw - img_w) / 2
        oy = (ch - img_h) / 2
        self._canvas.create_image(ox, oy, image=self._page_photo, anchor="nw", tags="bg")
        self._canvas.create_rectangle(
            ox, oy, ox + img_w, oy + img_h,
            outline=COLORS["border"], tags="border",
        )
        self._draw_edits(ox, oy, zoom)

        self._page_label.configure(
            text=f"Trang {self._current_page + 1}/{self._page_count}"
        )
        self._zoom_label.configure(text=f"{int(self._zoom * 100)}%")
        self._update_tool_controls()

    def _draw_edits(self, ox, oy, zoom):
        page_edits = self._all_edits.get(self._current_page, [])
        for edit in page_edits:
            if edit["type"] == "ink":
                pts = edit["points"]
                if len(pts) < 2:
                    continue
                display_pts = []
                for px, py in pts:
                    dx = ox + px * zoom
                    dy = oy + (self._page_height - py) * zoom
                    display_pts.extend([dx, dy])
                self._canvas.create_line(
                    *display_pts,
                    fill=edit["color"],
                    width=max(edit["width"] * zoom, 1),
                    capstyle="round", joinstyle="round",
                    tags="edit_item",
                )

            elif edit["type"] == "text":
                dx = ox + edit["x"] * zoom
                dy = oy + (self._page_height - edit["y"]) * zoom
                font_size = max(edit["font_size"] * zoom * 0.75, 6)
                self._canvas.create_text(
                    dx, dy, text=edit["text"],
                    fill=edit["color"],
                    font=("Segoe UI", int(font_size)),
                    anchor="sw", tags="edit_item",
                )

            elif edit["type"] == "image":
                dx = ox + edit["x"] * zoom
                dy = oy + (self._page_height - edit["y"] - edit["height"]) * zoom
                dw = edit["width"] * zoom
                dh = edit["height"] * zoom
                img_data = edit["image_data"]
                pil_img = Image.open(io.BytesIO(img_data))
                if dw > 0 and dh > 0:
                    resized = pil_img.resize((int(dw), int(dh)), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(resized)
                    key = f"sig_{edit['id']}"
                    self._signature_photos[key] = photo
                    self._canvas.create_image(
                        dx, dy, image=photo, anchor="nw", tags="edit_item",
                    )

    def _on_canvas_press(self, event):
        if not self._pdf_path:
            return

        cw = self._canvas.winfo_width()
        ch = self._canvas.winfo_height()
        img_w = self._page_width * self._zoom
        img_h = self._page_height * self._zoom
        ox = (cw - img_w) / 2
        oy = (ch - img_h) / 2

        pdf_x = (event.x - ox) / self._zoom
        pdf_y = self._page_height - (event.y - oy) / self._zoom

        if pdf_x < 0 or pdf_y < 0 or pdf_x > self._page_width or pdf_y > self._page_height:
            return

        if self._active_tool == "pen":
            self._current_stroke = {
                "type": "ink",
                "points": [(pdf_x, pdf_y)],
                "color": self._pen_color,
                "width": self._pen_width,
            }

        elif self._active_tool == "text":
            result = simpledialog.askstring(
                "Them chu", "Nhap noi dung:",
                parent=self, initialvalue=""
            )
            if result:
                edit = {
                    "id": self._edit_counter,
                    "type": "text",
                    "x": pdf_x,
                    "y": pdf_y,
                    "text": result,
                    "font_size": self._pen_width * 2,
                    "color": self._pen_color,
                }
                self._edit_counter += 1
                self._all_edits.setdefault(self._current_page, []).append(edit)
                self._load_and_render()

        elif self._active_tool == "signature":
            if self._signature_image is None:
                return
            sig_w = 120
            sig_h = int(sig_w * self._signature_image.height / self._signature_image.width)
            buf = io.BytesIO()
            self._signature_image.save(buf, format="PNG")
            img_data = buf.getvalue()
            edit = {
                "id": self._edit_counter,
                "type": "image",
                "x": pdf_x,
                "y": pdf_y,
                "width": sig_w,
                "height": sig_h,
                "image_data": img_data,
            }
            self._edit_counter += 1
            self._all_edits.setdefault(self._current_page, []).append(edit)
            self._load_and_render()

    def _on_canvas_move(self, event):
        if self._active_tool != "pen" or self._current_stroke is None:
            return

        cw = self._canvas.winfo_width()
        ch = self._canvas.winfo_height()
        img_w = self._page_width * self._zoom
        img_h = self._page_height * self._zoom
        ox = (cw - img_w) / 2
        oy = (ch - img_h) / 2

        pdf_x = (event.x - ox) / self._zoom
        pdf_y = self._page_height - (event.y - oy) / self._zoom
        if pdf_x < 0 or pdf_y < 0 or pdf_x > self._page_width or pdf_y > self._page_height:
            return

        self._current_stroke["points"].append((pdf_x, pdf_y))

        pts = self._current_stroke["points"]
        if len(pts) >= 2:
            prev_x, prev_y = pts[-2]
            dx1 = ox + prev_x * self._zoom
            dy1 = oy + (self._page_height - prev_y) * self._zoom
            dx2 = ox + pdf_x * self._zoom
            dy2 = oy + (self._page_height - pdf_y) * self._zoom
            self._canvas.create_line(
                dx1, dy1, dx2, dy2,
                fill=self._pen_color,
                width=max(self._pen_width * self._zoom, 1),
                capstyle="round", joinstyle="round",
                tags="temp_stroke",
            )

    def _on_canvas_release(self, event):
        if self._active_tool == "pen" and self._current_stroke:
            if len(self._current_stroke["points"]) >= 2:
                edit = self._current_stroke
                edit["id"] = self._edit_counter
                self._edit_counter += 1
                self._all_edits.setdefault(self._current_page, []).append(edit)
            self._current_stroke = None
            self._load_and_render()

    def _undo(self):
        page_edits = self._all_edits.get(self._current_page, [])
        if not page_edits:
            return
        self._all_edits[self._current_page] = page_edits[:-1]
        self._load_and_render()

    def _clear_page(self):
        page_edits = self._all_edits.get(self._current_page, [])
        if not page_edits:
            return
        self._all_edits[self._current_page] = []
        self._load_and_render()

    def _update_tool_controls(self):
        page_edits = self._all_edits.get(self._current_page, [])
        has_edits = len(page_edits) > 0
        self._undo_btn.configure(state="normal" if has_edits else "disabled")
        self._clear_page_btn.configure(state="normal" if has_edits else "disabled")

    def _zoom_in(self):
        if not self._pdf_path:
            return
        self._zoom = min(self._zoom * 1.25, 3.0)
        self._load_and_render()

    def _zoom_out(self):
        if not self._pdf_path:
            return
        self._zoom = max(self._zoom / 1.25, 0.25)
        self._load_and_render()

    def _go_to_page(self, page_idx):
        if page_idx < 0 or page_idx >= self._page_count:
            return
        if self._current_stroke:
            self._current_stroke = None
        self._current_page = page_idx
        self._load_and_render()
        self._build_thumbnails()

    def _build_thumbnails(self):
        for w in self._thumb_frame.winfo_children():
            w.destroy()
        self._thumb_photos.clear()

        if not self._pdf_path:
            return

        thumb_zoom = 0.12
        container = ctk.CTkFrame(self._thumb_frame, fg_color="transparent")
        container.pack(pady=6)

        for i in range(self._page_count):
            frame = ctk.CTkFrame(
                container, fg_color=COLORS["accent_green"] if i == self._current_page else COLORS["bg_tertiary"],
                corner_radius=6, cursor="hand2",
            )
            frame.pack(side="left", padx=3)

            try:
                pil_img = render_page(self._pdf_path, i, thumb_zoom)
                ctk_img = ctk.CTkImage(pil_img, size=(pil_img.width, pil_img.height))
                self._thumb_photos[i] = ctk_img
                label = ctk.CTkLabel(frame, image=ctk_img, text="")
                label.pack(padx=3, pady=3)
            except Exception:
                label = ctk.CTkLabel(
                    frame, text=f"{i + 1}",
                    font=FONTS["caption"], text_color=COLORS["text_secondary"],
                    width=40, height=50,
                )
                label.pack(padx=3, pady=3)

            label.bind("<Button-1>", lambda e, idx=i: self._go_to_page(idx), add="+")
            frame.bind("<Button-1>", lambda e, idx=i: self._go_to_page(idx), add="+")

    def _start_save(self):
        if self._is_saving or not self._pdf_path:
            return

        if not any(self._all_edits.values()):
            messagebox.showinfo(
                "Thong bao",
                "Chua co chinh sua nao de luu."
            )
            return

        output_path = filedialog.asksaveasfilename(
            title="Luu file PDF da chinh sua",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if not output_path:
            return

        self._is_saving = True
        self._set_controls_enabled(False)
        self._save_btn.configure(text="Dang luu...")

        Thread(target=self._do_save, args=(output_path,), daemon=True).start()

    def _do_save(self, output_path):
        try:
            edits_by_page = {}
            for page_idx, page_edits in self._all_edits.items():
                if page_edits:
                    edits_by_page[page_idx] = page_edits

            def progress(val):
                self.after(0, lambda: self._save_btn.configure(
                    text=f"Dang luu... {val}%"
                ))

            apply_edits_to_pdf(self._pdf_path, output_path, edits_by_page, progress)
            self.after(0, self._on_save_success, output_path)
        except Exception as e:
            self.after(0, self._on_save_error, str(e))

    def _on_save_success(self, output_path):
        self._is_saving = False
        self._save_btn.configure(text="Luu PDF", state="normal")
        self._set_controls_enabled(True)
        messagebox.showinfo(
            "Thanh cong",
            f"Da luu file PDF da chinh sua thanh cong!\n\n"
            f"Tep luu tai:\n{output_path}"
        )

    def _on_save_error(self, error_msg):
        self._is_saving = False
        self._save_btn.configure(text="Luu PDF", state="normal")
        self._set_controls_enabled(True)
        messagebox.showerror("Loi", f"Khong the luu PDF:\n\n{error_msg}")

    def _set_controls_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        self._open_btn.configure(state=state)
