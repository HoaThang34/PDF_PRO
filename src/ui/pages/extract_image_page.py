import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from threading import Thread

from src.ui.themes.theme import COLORS, FONTS, SPACING
from src.core.pdf_extract_image import (
    get_image_page_info,
    get_image_thumbnail,
    get_page_render_preview,
    extract_pages_to_images,
)
from customtkinter import CTkImage
from PIL import Image


class ExtractImagePage(ctk.CTkFrame):

    def __init__(self, master, on_back=None):
        super().__init__(master, fg_color=COLORS["bg_primary"])

        self._on_back = on_back
        self._pdf_path = None
        self._pages = []
        self._selected_indices = set()
        self._thumbnails = {}
        self._preview_img = None
        self._preview_ctk_img = None
        self._is_processing = False

        self.grid_columnconfigure(0, weight=1)

        self._build_header()
        self._build_content_area()
        self._build_bottom_bar()

    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color="transparent", height=50)
        header.grid(row=0, column=0, padx=SPACING["lg"], pady=(SPACING["lg"], 0), sticky="ew")
        header.grid_propagate(False)
        header.grid_columnconfigure(1, weight=1)

        back_btn = ctk.CTkButton(
            header,
            text="\u2190 Quay L\u1ea1i",
            font=FONTS["body"],
            text_color=COLORS["text_secondary"],
            fg_color="transparent",
            hover_color=COLORS["bg_tertiary"],
            width=100, height=36, corner_radius=8,
            command=self._on_back,
        )
        back_btn.grid(row=0, column=0, sticky="w")

        title = ctk.CTkLabel(
            header,
            text="Xu\u1ea5t \u1ea2nh T\u1eeb PDF",
            font=FONTS["heading_lg"],
            text_color=COLORS["accent_pink"],
        )
        title.grid(row=0, column=1)

        btn_frame = ctk.CTkFrame(header, fg_color="transparent")
        btn_frame.grid(row=0, column=2, sticky="e")

        self._add_btn = ctk.CTkButton(
            btn_frame,
            text="+ Th\u00eam T\u1ec7p PDF",
            font=FONTS["heading_sm"],
            text_color="#FFFFFF",
            fg_color=COLORS["accent_pink"],
            hover_color="#DB2777",
            height=36, corner_radius=8,
            command=self._add_file,
        )
        self._add_btn.pack(side="left")

        self._clear_btn = ctk.CTkButton(
            btn_frame,
            text="X\u00f3a T\u1ea5t C\u1ea3",
            font=FONTS["body"],
            text_color=COLORS["text_muted"],
            fg_color="transparent",
            hover_color=COLORS["bg_tertiary"],
            height=36, corner_radius=8,
            state="disabled",
            command=self._clear_all,
        )
        self._clear_btn.pack(side="left", padx=(8, 0))

    def _build_content_area(self):
        self.grid_rowconfigure(1, weight=3)
        self.grid_rowconfigure(2, weight=2)

        self._pages_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=COLORS["bg_secondary"],
            corner_radius=12,
            border_width=1,
            border_color=COLORS["border"],
        )
        self._pages_frame.grid(row=1, column=0, padx=SPACING["lg"], pady=(SPACING["md"], 6), sticky="nsew")
        self._pages_frame.grid_columnconfigure(0, weight=1)

        self._preview_frame = ctk.CTkFrame(
            self,
            fg_color=COLORS["bg_secondary"],
            corner_radius=12,
            border_width=1,
            border_color=COLORS["border"],
        )
        self._preview_frame.grid(row=2, column=0, padx=SPACING["lg"], pady=(6, SPACING["md"]), sticky="nsew")
        self._preview_frame.grid_columnconfigure(0, weight=1)
        self._preview_frame.grid_rowconfigure(1, weight=1)

        preview_header = ctk.CTkFrame(self._preview_frame, fg_color="transparent", height=30)
        preview_header.grid(row=0, column=0, padx=12, pady=(8, 4), sticky="ew")
        preview_header.grid_propagate(False)
        preview_header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            preview_header,
            text="Xem tr\u01b0\u1edbc \u1ea3nh",
            font=FONTS["heading_sm"],
            text_color=COLORS["text_muted"],
            anchor="w",
        ).grid(row=0, column=0, sticky="w")

        self._preview_label = ctk.CTkLabel(
            self._preview_frame,
            text="Ch\u1ecdn m\u1ed9t trang \u0111\u1ec3 xem tr\u01b0\u1edbc \u1ea3nh.",
            font=FONTS["body"],
            text_color=COLORS["text_muted"],
        )
        self._preview_label.grid(row=1, column=0, pady=40)

        self._show_placeholder()

    def _show_placeholder(self):
        for w in self._pages_frame.winfo_children():
            w.destroy()
        ctk.CTkLabel(
            self._pages_frame,
            text="Ch\u01b0a c\u00f3 t\u1ec7p n\u00e0o \u0111\u01b0\u1ee3c ch\u1ecdn.\n"
                 "Nh\u1ea5n 'Th\u00eam T\u1ec7p PDF' \u0111\u1ec3 m\u1edf t\u00e0i li\u1ec7u v\u00e0 xu\u1ea5t \u1ea3nh.",
            font=FONTS["body"],
            text_color=COLORS["text_muted"],
            justify="center",
        ).grid(row=0, column=0, pady=80)

    def _build_bottom_bar(self):
        bottom = ctk.CTkFrame(self, fg_color="transparent")
        bottom.grid(row=3, column=0, padx=SPACING["lg"], pady=(0, SPACING["lg"]), sticky="ew")
        bottom.grid_columnconfigure(0, weight=1)

        btn_frame = ctk.CTkFrame(bottom, fg_color="transparent")
        btn_frame.grid(row=0, column=0, sticky="w")

        self._select_all_btn = ctk.CTkButton(
            btn_frame, text="\u2611 Ch\u1ecdn T\u1ea5t C\u1ea3", width=130, height=36,
            fg_color=COLORS["bg_tertiary"], text_color=COLORS["text_primary"],
            hover_color=COLORS["border_hover"], corner_radius=8,
            state="disabled", command=self._select_all,
        )
        self._select_all_btn.pack(side="left", padx=(0, 6))

        self._deselect_btn = ctk.CTkButton(
            btn_frame, text="B\u1ecf Ch\u1ecdn T\u1ea5t C\u1ea3", width=130, height=36,
            fg_color="transparent", text_color=COLORS["text_muted"],
            hover_color=COLORS["bg_tertiary"], corner_radius=8,
            state="disabled", command=self._deselect_all,
        )
        self._deselect_btn.pack(side="left")

        right_frame = ctk.CTkFrame(bottom, fg_color="transparent")
        right_frame.grid(row=0, column=1, sticky="e")

        ctk.CTkLabel(
            right_frame,
            text="\u0110\u1ecbnh d\u1ea1ng:",
            font=FONTS["body_sm"],
            text_color=COLORS["text_muted"],
        ).pack(side="left", padx=(0, 6))

        self._format_var = ctk.StringVar(value="PNG")
        self._format_menu = ctk.CTkOptionMenu(
            right_frame,
            values=["PNG", "JPEG"],
            variable=self._format_var,
            font=FONTS["body_sm"],
            text_color=COLORS["text_primary"],
            fg_color=COLORS["bg_tertiary"],
            button_color=COLORS["border_hover"],
            button_hover_color=COLORS["text_muted"],
            height=36, width=80, corner_radius=8,
            state="disabled",
        )
        self._format_menu.pack(side="left", padx=(0, 12))

        ctk.CTkLabel(
            right_frame,
            text="DPI:",
            font=FONTS["body_sm"],
            text_color=COLORS["text_muted"],
        ).pack(side="left", padx=(0, 6))

        self._dpi_var = ctk.StringVar(value="200")
        self._dpi_menu = ctk.CTkOptionMenu(
            right_frame,
            values=["150", "200", "300", "400", "600"],
            variable=self._dpi_var,
            font=FONTS["body_sm"],
            text_color=COLORS["text_primary"],
            fg_color=COLORS["bg_tertiary"],
            button_color=COLORS["border_hover"],
            button_hover_color=COLORS["text_muted"],
            height=36, width=70, corner_radius=8,
            state="disabled",
        )
        self._dpi_menu.pack(side="left", padx=(0, 12))

        self._status_label = ctk.CTkLabel(
            right_frame,
            text="Ch\u01b0a m\u1edf t\u1ec7p",
            font=FONTS["body_sm"],
            text_color=COLORS["text_muted"],
        )
        self._status_label.pack(side="left", padx=(0, 12))

        self._progress_bar = ctk.CTkProgressBar(
            right_frame,
            width=180, height=8,
            fg_color=COLORS["bg_tertiary"],
            progress_color=COLORS["accent_pink"],
            corner_radius=4,
        )
        self._progress_bar.pack(side="left", padx=(0, 12))
        self._progress_bar.set(0)

        self._extract_btn = ctk.CTkButton(
            right_frame,
            text="Xu\u1ea5t \u1ea2nh",
            font=FONTS["heading_sm"],
            text_color="#FFFFFF",
            fg_color=COLORS["accent_pink"],
            hover_color="#DB2777",
            height=40, corner_radius=8,
            state="disabled", command=self._start_extract_selected,
        )
        self._extract_btn.pack(side="left")

        self._update_controls()

    def _add_file(self):
        path = filedialog.askopenfilename(
            title="Ch\u1ecdn file PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if not path:
            return

        self._pdf_path = path
        self._selected_indices.clear()
        self._status_label.configure(text="\u0110ang \u0111\u1ecdc c\u00e1c trang...")
        Thread(target=self._load_all_pages, daemon=True).start()

    def _load_all_pages(self):
        try:
            pages = get_image_page_info(self._pdf_path)
            self._pages = pages

            self._thumbnails.clear()
            for p in pages:
                idx = p["index"]
                img = get_image_thumbnail(self._pdf_path, idx)
                if img:
                    self._thumbnails[idx] = CTkImage(img, size=(60, 80))

            total_pages = len(pages)
            self.after(0, lambda: self._on_load_success(total_pages))
        except Exception as e:
            self.after(0, lambda: self._on_load_error(str(e)))

    def _on_load_success(self, total_pages):
        self._status_label.configure(text=f"1 t\u1ec7p - {total_pages} trang - 0/{total_pages} \u0111\u00e3 ch\u1ecdn")
        self._refresh_page_list()
        self._update_controls()
        self._clear_preview()

    def _on_load_error(self, msg):
        self._pdf_path = None
        self._status_label.configure(text="L\u1ed7i")
        messagebox.showerror("L\u1ed7i", f"Kh\u00f4ng th\u1ec3 \u0111\u1ecdc file PDF:\n\n{msg}")
        self._show_placeholder()
        self._update_controls()

    def _refresh_page_list(self):
        for w in self._pages_frame.winfo_children():
            w.destroy()

        if not self._pages:
            self._show_placeholder()
            self._update_controls()
            return

        for page_info in self._pages:
            idx = page_info["index"]
            self._build_page_item(idx, page_info)

    def _build_page_item(self, index, page_info):
        selected = index in self._selected_indices

        row = ctk.CTkFrame(
            self._pages_frame,
            fg_color=COLORS["bg_tertiary"] if selected else "transparent",
            corner_radius=8,
            height=90,
        )
        row.grid(row=index, column=0, padx=8, pady=3, sticky="ew")
        row.grid_propagate(False)
        row.grid_columnconfigure(2, weight=1)

        check_canvas = tk.Canvas(
            row, width=24, height=24,
            bg=COLORS["bg_secondary"],
            highlightthickness=0, bd=0,
        )
        check_canvas.grid(row=0, column=0, padx=(10, 6))
        self._draw_checkbox(check_canvas, selected)

        thumb_frame = ctk.CTkFrame(row, fg_color="#FFFFFF", width=48, height=64, corner_radius=4)
        thumb_frame.grid(row=0, column=1, padx=(0, 12))
        thumb_frame.grid_propagate(False)

        if index in self._thumbnails:
            thumb_label = ctk.CTkLabel(thumb_frame, image=self._thumbnails[index], text="")
            thumb_label.grid(row=0, column=0)
        else:
            ctk.CTkLabel(
                thumb_frame,
                text=f"Trang\n{page_info['page_num']}",
                font=("Segoe UI", 9), text_color="#333333",
            ).grid(row=0, column=0)

        info_frame = ctk.CTkFrame(row, fg_color="transparent")
        info_frame.grid(row=0, column=2, sticky="w")

        ctk.CTkLabel(
            info_frame,
            text=f"Trang {page_info['page_num']} - {page_info['filename']}",
            font=FONTS["heading_sm"],
            text_color=COLORS["text_primary"],
            anchor="w",
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            info_frame,
            text=f"{page_info['width']:.0f} x {page_info['height']:.0f} pt",
            font=FONTS["body_sm"],
            text_color=COLORS["text_secondary"],
            anchor="w",
        ).grid(row=1, column=0, sticky="w", pady=(2, 0))

        for w in (row, check_canvas, thumb_frame, info_frame):
            w.bind("<Button-1>", lambda e, idx=index: self._toggle_page(idx), add="+")

        return row

    def _draw_checkbox(self, canvas, checked):
        canvas.delete("all")
        s = 24
        if checked:
            canvas.create_rectangle(2, 2, s - 2, s - 2, fill=COLORS["accent_pink"], outline=COLORS["accent_pink"], width=1)
            canvas.create_text(s / 2, s / 2, text="\u2713", fill="#FFFFFF", font=("Segoe UI", 14, "bold"))
        else:
            canvas.create_rectangle(2, 2, s - 2, s - 2, fill="", outline=COLORS["text_muted"], width=1.5)

    def _toggle_page(self, index):
        if index in self._selected_indices:
            self._selected_indices.discard(index)
        else:
            self._selected_indices.add(index)
        self._refresh_page_list()
        self._update_controls()
        if index in self._selected_indices:
            self._show_preview_for_page(index)
        else:
            self._clear_preview()

    def _show_preview_for_page(self, index):
        if not self._pdf_path:
            return
        self._preview_label.configure(text="\u0110ang t\u1ea3i \u1ea3nh...")
        self._preview_label.configure(image="")
        Thread(target=self._load_preview, args=(index,), daemon=True).start()

    def _load_preview(self, index):
        try:
            img = get_page_render_preview(self._pdf_path, index, dpi=120)
            max_w = 500
            max_h = 300
            w, h = img.size
            scale = min(max_w / w, max_h / h, 1.0)
            if scale < 1.0:
                new_w = int(w * scale)
                new_h = int(h * scale)
                img = img.resize((new_w, new_h), Image.LANCZOS)
            self._preview_img = img
            ctk_img = CTkImage(img, size=img.size)
            self._preview_ctk_img = ctk_img
            self.after(0, lambda: self._update_preview_image(ctk_img))
        except Exception as e:
            self.after(0, lambda: self._update_preview_error(str(e)))

    def _update_preview_image(self, ctk_img):
        self._preview_label.configure(image=ctk_img, text="")

    def _update_preview_error(self, msg):
        self._preview_label.configure(text=f"L\u1ed7i khi t\u1ea3i \u1ea3nh:\n{msg}", image="")

    def _clear_preview(self):
        self._preview_label.configure(image="", text="Ch\u1ecdn m\u1ed9t trang \u0111\u1ec3 xem tr\u01b0\u1edbc \u1ea3nh.")

    def _select_all(self):
        if not self._pages:
            return
        self._selected_indices = set(p["index"] for p in self._pages)
        self._refresh_page_list()
        self._update_controls()
        if self._selected_indices:
            idx = min(self._selected_indices)
            self._show_preview_for_page(idx)

    def _deselect_all(self):
        self._selected_indices.clear()
        self._refresh_page_list()
        self._update_controls()
        self._clear_preview()

    def _clear_all(self):
        if not self._pdf_path:
            return
        self._pdf_path = None
        self._pages.clear()
        self._selected_indices.clear()
        self._thumbnails.clear()
        self._preview_img = None
        self._preview_ctk_img = None
        self._status_label.configure(text="Ch\u01b0a m\u1edf t\u1ec7p")
        self._progress_bar.set(0)
        self._refresh_page_list()
        self._update_controls()
        self._clear_preview()

    def _update_controls(self):
        n = len(self._pages)
        has_pages = n > 0
        has_selection = len(self._selected_indices) > 0

        if self._is_processing:
            self._add_btn.configure(state="disabled")
            self._clear_btn.configure(state="disabled")
            self._select_all_btn.configure(state="disabled")
            self._deselect_btn.configure(state="disabled")
            self._extract_btn.configure(state="disabled")
            self._format_menu.configure(state="disabled")
            self._dpi_menu.configure(state="disabled")
            return

        self._add_btn.configure(state="normal")
        self._clear_btn.configure(state="normal" if has_pages else "disabled")
        self._select_all_btn.configure(state="normal" if has_pages else "disabled")
        self._deselect_btn.configure(state="normal" if has_selection else "disabled")
        self._extract_btn.configure(state="normal" if has_selection else "disabled")
        self._format_menu.configure(state="normal" if has_pages else "disabled")
        self._dpi_menu.configure(state="normal" if has_pages else "disabled")

        if has_pages:
            self._status_label.configure(
                text=f"1 t\u1ec7p - {n} trang - {len(self._selected_indices)}/{n} \u0111\u00e3 ch\u1ecdn"
            )

    def _start_extract_selected(self):
        if self._is_processing or not self._pdf_path or not self._selected_indices:
            return

        output_dir = filedialog.askdirectory(
            title="Ch\u1ecdn th\u01b0 m\u1ee5c l\u01b0u file \u1ea3nh"
        )
        if not output_dir:
            return

        self._is_processing = True
        self._set_controls_enabled(False)
        self._progress_bar.set(0)
        self._status_label.configure(text="\u0110ang xu\u1ea5t \u1ea3nh...")

        page_indices = sorted(self._selected_indices)
        image_format = self._format_var.get()
        dpi = int(self._dpi_var.get())
        Thread(target=self._do_extract, args=(output_dir, page_indices, image_format, dpi), daemon=True).start()

    def _do_extract(self, output_dir, page_indices, image_format, dpi):
        try:
            def progress(val):
                self.after(0, lambda: self._progress_bar.set(val / 100))

            extract_pages_to_images(
                self._pdf_path, page_indices, output_dir,
                image_format=image_format, dpi=dpi, progress_callback=progress,
            )
            self.after(0, self._on_extract_success, output_dir, len(page_indices))
        except Exception as e:
            self.after(0, self._on_extract_error, str(e))

    def _on_extract_success(self, output_dir, count):
        self._is_processing = False
        self._progress_bar.set(1)
        self._status_label.configure(text="Ho\u00e0n t\u1ea5t!")
        fmt = self._format_var.get()
        messagebox.showinfo(
            "Th\u00e0nh c\u00f4ng",
            f"\u0110\u00e3 xu\u1ea5t th\u00e0nh c\u00f4ng {count} trang sang \u0111\u1ecbnh d\u1ea1ng {fmt}!\n\n"
            f"C\u00e1c file \u1ea3nh \u0111\u01b0\u1ee3c l\u01b0u t\u1ea1i:\n{output_dir}"
        )
        self._set_controls_enabled(True)
        self._progress_bar.set(0)
        n = len(self._pages)
        sel = len(self._selected_indices)
        self._status_label.configure(text=f"1 t\u1ec7p - {n} trang - {sel}/{n} \u0111\u00e3 ch\u1ecdn")

    def _on_extract_error(self, error_msg):
        self._is_processing = False
        self._set_controls_enabled(True)
        self._progress_bar.set(0)
        self._status_label.configure(text="L\u1ed7i")
        messagebox.showerror("L\u1ed7i", f"Kh\u00f4ng th\u1ec3 xu\u1ea5t \u1ea3nh:\n\n{error_msg}")

    def _set_controls_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        self._add_btn.configure(state=state)
        self._clear_btn.configure(state=state)
        self._select_all_btn.configure(state=state)
        self._deselect_btn.configure(state=state)
        self._extract_btn.configure(
            state=state,
            text="\u0110ang x\u1eed l\u00fd..." if not enabled else "Xu\u1ea5t \u1ea2nh",
        )
        self._format_menu.configure(state=state)
        self._dpi_menu.configure(state=state)
        if enabled:
            self._update_controls()
