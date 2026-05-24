import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from threading import Thread

from src.ui.themes.theme import COLORS, FONTS, SPACING
from src.core.pdf_sort import get_pages_from_files, reorder_from_files, get_page_thumbnail


class SortPage(ctk.CTkFrame):

    def __init__(self, master, on_back=None):
        super().__init__(master, fg_color=COLORS["bg_primary"])

        self._on_back = on_back
        self._file_paths = []
        self._pages = []
        self._page_order = []
        self._thumbnails = {}
        self._selected_index = -1
        self._is_processing = False

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

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
            text="S\u1eafp X\u1ebfp Trang",
            font=FONTS["heading_lg"],
            text_color=COLORS["accent_blue"],
        )
        title.grid(row=0, column=1)

        btn_frame = ctk.CTkFrame(header, fg_color="transparent")
        btn_frame.grid(row=0, column=2, sticky="e")

        self._add_btn = ctk.CTkButton(
            btn_frame,
            text="+ Th\u00eam T\u1ec7p PDF",
            font=FONTS["heading_sm"],
            text_color="#FFFFFF",
            fg_color=COLORS["accent_blue"],
            hover_color="#2563EB",
            height=36, corner_radius=8,
            command=self._add_files,
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
            command=self._clear_all,
        )
        self._clear_btn.pack(side="left", padx=(8, 0))

    def _build_content_area(self):
        self._content_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=COLORS["bg_secondary"],
            corner_radius=12,
            border_width=1,
            border_color=COLORS["border"],
        )
        self._content_frame.grid(row=1, column=0, padx=SPACING["lg"], pady=SPACING["md"], sticky="nsew")
        self._content_frame.grid_columnconfigure(0, weight=1)

        self._show_placeholder()

    def _show_placeholder(self):
        for w in self._content_frame.winfo_children():
            w.destroy()
        ctk.CTkLabel(
            self._content_frame,
            text="Ch\u01b0a c\u00f3 t\u1ec7p n\u00e0o \u0111\u01b0\u1ee3c ch\u1ecdn.\n"
                 "Nh\u1ea5n 'Th\u00eam T\u1ec7p PDF' \u0111\u1ec3 th\u00eam c\u00e1c t\u1ec7p v\u00e0 s\u1eafp x\u1ebfp trang.",
            font=FONTS["body"],
            text_color=COLORS["text_muted"],
            justify="center",
        ).grid(row=0, column=0, pady=80)

    def _build_bottom_bar(self):
        bottom = ctk.CTkFrame(self, fg_color="transparent")
        bottom.grid(row=2, column=0, padx=SPACING["lg"], pady=(0, SPACING["lg"]), sticky="ew")
        bottom.grid_columnconfigure(0, weight=1)

        btn_frame = ctk.CTkFrame(bottom, fg_color="transparent")
        btn_frame.grid(row=0, column=0, sticky="w")

        self._top_btn = ctk.CTkButton(
            btn_frame, text="\u2b06 \u0110\u1ea7u", width=70, height=36,
            fg_color=COLORS["bg_tertiary"], text_color=COLORS["text_primary"],
            hover_color=COLORS["border_hover"], corner_radius=8,
            command=self._move_top,
        )
        self._top_btn.pack(side="left", padx=(0, 4))

        self._up_btn = ctk.CTkButton(
            btn_frame, text="\u2191", width=40, height=36,
            fg_color=COLORS["bg_tertiary"], text_color=COLORS["text_primary"],
            hover_color=COLORS["border_hover"], corner_radius=8,
            command=self._move_up,
        )
        self._up_btn.pack(side="left", padx=(0, 4))

        self._down_btn = ctk.CTkButton(
            btn_frame, text="\u2193", width=40, height=36,
            fg_color=COLORS["bg_tertiary"], text_color=COLORS["text_primary"],
            hover_color=COLORS["border_hover"], corner_radius=8,
            command=self._move_down,
        )
        self._down_btn.pack(side="left", padx=(0, 4))

        self._bottom_btn = ctk.CTkButton(
            btn_frame, text="\u2b07 Cu\u1ed1i", width=70, height=36,
            fg_color=COLORS["bg_tertiary"], text_color=COLORS["text_primary"],
            hover_color=COLORS["border_hover"], corner_radius=8,
            command=self._move_bottom,
        )
        self._bottom_btn.pack(side="left", padx=(0, 12))

        self._reset_btn = ctk.CTkButton(
            btn_frame, text="\u0110\u1eb7t L\u1ea1i", width=80, height=36,
            fg_color="transparent", text_color=COLORS["text_muted"],
            hover_color=COLORS["bg_tertiary"], corner_radius=8,
            command=self._reset_order,
        )
        self._reset_btn.pack(side="left")

        right_frame = ctk.CTkFrame(bottom, fg_color="transparent")
        right_frame.grid(row=0, column=1, sticky="e")

        self._status_label = ctk.CTkLabel(
            right_frame,
            text="Ch\u01b0a c\u00f3 t\u1ec7p n\u00e0o",
            font=FONTS["body_sm"],
            text_color=COLORS["text_muted"],
        )
        self._status_label.pack(side="left", padx=(0, 12))

        self._progress_bar = ctk.CTkProgressBar(
            right_frame,
            width=180, height=8,
            fg_color=COLORS["bg_tertiary"],
            progress_color=COLORS["accent_blue"],
            corner_radius=4,
        )
        self._progress_bar.pack(side="left", padx=(0, 12))
        self._progress_bar.set(0)

        self._save_btn = ctk.CTkButton(
            right_frame,
            text="L\u01b0u PDF",
            font=FONTS["heading_sm"],
            text_color="#FFFFFF",
            fg_color=COLORS["accent_blue"],
            hover_color="#2563EB",
            height=40, corner_radius=8,
            command=self._start_save,
        )
        self._save_btn.pack(side="left")

        self._update_controls()

    def _add_files(self):
        paths = filedialog.askopenfilenames(
            title="Ch\u1ecdn c\u00e1c t\u1ec7p PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if not paths:
            return

        existing = set(self._file_paths)
        new_paths = [p for p in paths if p not in existing]
        if not new_paths:
            return

        self._file_paths.extend(new_paths)
        self._selected_index = -1
        self._status_label.configure(text="\u0110ang \u0111\u1ecdc c\u00e1c t\u1ec7p...")
        Thread(target=self._load_all_pdfs, daemon=True).start()

    def _load_all_pdfs(self):
        try:
            all_pages = get_pages_from_files(self._file_paths)
            self._pages = all_pages
            self._page_order = list(range(len(all_pages)))

            self._thumbnails.clear()
            for idx, p in enumerate(all_pages):
                img = get_page_thumbnail(p["file_path"], p["page_index"])
                if img:
                    from customtkinter import CTkImage
                    self._thumbnails[idx] = CTkImage(img, size=(60, 80))

            total_files = len(self._file_paths)
            total_pages = len(all_pages)
            self.after(0, lambda: self._on_load_success(total_files, total_pages))
        except Exception as e:
            self.after(0, lambda: self._on_load_error(str(e)))

    def _on_load_success(self, total_files, total_pages):
        self._status_label.configure(
            text=f"{total_files} t\u1ec7p - {total_pages} trang"
        )
        self._refresh_page_list()
        self._update_controls()

    def _on_load_error(self, msg):
        self._file_paths.clear()
        self._status_label.configure(text="L\u1ed7i")
        messagebox.showerror("L\u1ed7i", f"Kh\u00f4ng th\u1ec3 \u0111\u1ecdc file PDF:\n\n{msg}")
        self._show_placeholder()
        self._update_controls()

    def _refresh_page_list(self):
        for w in self._content_frame.winfo_children():
            w.destroy()

        if not self._page_order:
            self._show_placeholder()
            self._update_controls()
            return

        for pos, page_idx in enumerate(self._page_order):
            self._build_page_item(pos, page_idx)

    def _build_page_item(self, position, page_idx):
        info = self._pages[page_idx]
        selected = position == self._selected_index

        row = ctk.CTkFrame(
            self._content_frame,
            fg_color=COLORS["bg_tertiary"] if selected else "transparent",
            corner_radius=8,
            height=90,
        )
        row.grid(row=position, column=0, padx=8, pady=3, sticky="ew")
        row.grid_propagate(False)
        row.grid_columnconfigure(2, weight=1)

        pos_label = ctk.CTkLabel(
            row, text=str(position + 1),
            font=("Segoe UI", 13, "bold"),
            text_color=COLORS["accent_blue"],
            width=32, anchor="center",
        )
        pos_label.grid(row=0, column=0, padx=(10, 6))

        thumb_frame = ctk.CTkFrame(row, fg_color="#FFFFFF", width=48, height=64, corner_radius=4)
        thumb_frame.grid(row=0, column=1, padx=(0, 12))
        thumb_frame.grid_propagate(False)

        if page_idx in self._thumbnails:
            thumb_label = ctk.CTkLabel(thumb_frame, image=self._thumbnails[page_idx], text="")
            thumb_label.grid(row=0, column=0)
        else:
            ctk.CTkLabel(
                thumb_frame,
                text=f"Trang\n{info['page_index'] + 1}",
                font=("Segoe UI", 9), text_color="#333333",
            ).grid(row=0, column=0)

        info_frame = ctk.CTkFrame(row, fg_color="transparent")
        info_frame.grid(row=0, column=2, sticky="w")
        info_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            info_frame,
            text=f"Trang {info['page_index'] + 1} - {info['filename']}",
            font=FONTS["heading_sm"],
            text_color=COLORS["text_primary"],
            anchor="w",
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            info_frame,
            text=f"{info['width']:.0f} x {info['height']:.0f} pt",
            font=FONTS["body_sm"],
            text_color=COLORS["text_secondary"],
            anchor="w",
        ).grid(row=1, column=0, sticky="w", pady=(2, 0))

        handle = ctk.CTkLabel(
            row, text="\u2261",
            font=("Segoe UI", 20),
            text_color=COLORS["text_muted"],
            anchor="center", width=30,
        )
        handle.grid(row=0, column=3, padx=(0, 8))

        clickables = [row, pos_label, info_frame, thumb_frame]
        for w in clickables:
            w.bind("<Button-1>", lambda e, idx=position: self._select_item(idx), add="+")

        return row

    def _select_item(self, index):
        if self._selected_index == index:
            self._selected_index = -1
        else:
            self._selected_index = index
        self._refresh_page_list()
        self._update_controls()

    def _move_up(self):
        if self._selected_index <= 0:
            return
        idx = self._selected_index
        self._page_order[idx], self._page_order[idx - 1] = self._page_order[idx - 1], self._page_order[idx]
        self._selected_index = idx - 1
        self._refresh_page_list()

    def _move_down(self):
        if self._selected_index < 0 or self._selected_index >= len(self._page_order) - 1:
            return
        idx = self._selected_index
        self._page_order[idx], self._page_order[idx + 1] = self._page_order[idx + 1], self._page_order[idx]
        self._selected_index = idx + 1
        self._refresh_page_list()

    def _move_top(self):
        if self._selected_index <= 0:
            return
        val = self._page_order.pop(self._selected_index)
        self._page_order.insert(0, val)
        self._selected_index = 0
        self._refresh_page_list()

    def _move_bottom(self):
        n = len(self._page_order)
        if self._selected_index < 0 or self._selected_index >= n - 1:
            return
        val = self._page_order.pop(self._selected_index)
        self._page_order.append(val)
        self._selected_index = n - 1
        self._refresh_page_list()

    def _reset_order(self):
        if not self._pages:
            return
        self._page_order = list(range(len(self._pages)))
        self._selected_index = -1
        self._refresh_page_list()

    def _clear_all(self):
        if not self._file_paths:
            return
        self._file_paths.clear()
        self._pages.clear()
        self._page_order.clear()
        self._thumbnails.clear()
        self._selected_index = -1
        self._status_label.configure(text="Ch\u01b0a c\u00f3 t\u1ec7p n\u00e0o")
        self._refresh_page_list()
        self._update_controls()

    def _update_controls(self):
        n = len(self._page_order)
        has_selection = 0 <= self._selected_index < n

        self._top_btn.configure(state="normal" if has_selection and self._selected_index > 0 else "disabled")
        self._up_btn.configure(state="normal" if has_selection and self._selected_index > 0 else "disabled")
        self._down_btn.configure(state="normal" if has_selection and self._selected_index < n - 1 else "disabled")
        self._bottom_btn.configure(state="normal" if has_selection and self._selected_index < n - 1 else "disabled")
        self._reset_btn.configure(state="normal" if n > 0 else "disabled")
        self._save_btn.configure(state="normal" if n > 0 else "disabled")
        self._clear_btn.configure(state="normal" if n > 0 else "disabled")

    def _start_save(self):
        if self._is_processing:
            return
        if not self._file_paths or not self._page_order:
            return

        output_path = filedialog.asksaveasfilename(
            title="L\u01b0u file PDF \u0111\u00e3 s\u1eafp x\u1ebfp",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if not output_path:
            return

        self._is_processing = True
        self._set_controls_enabled(False)
        self._progress_bar.set(0)
        self._status_label.configure(text="\u0110ang x\u1eed l\u00fd...")

        page_order = list(self._page_order)
        file_paths = list(self._file_paths)

        Thread(target=self._do_save, args=(file_paths, output_path, page_order), daemon=True).start()

    def _do_save(self, file_paths, output_path, page_order):
        try:
            mappings = [(self._pages[i]["file_index"], self._pages[i]["page_index"]) for i in page_order]

            def progress(val):
                self.after(0, lambda: self._progress_bar.set(val / 100))

            reorder_from_files(file_paths, output_path, mappings, progress_callback=progress)
            self.after(0, self._on_save_success, output_path)
        except Exception as e:
            self.after(0, self._on_save_error, str(e))

    def _on_save_success(self, output_path):
        self._is_processing = False
        self._progress_bar.set(1)
        self._status_label.configure(text="Ho\u00e0n t\u1ea5t!")
        messagebox.showinfo(
            "Th\u00e0nh c\u00f4ng",
            f"\u0110\u00e3 s\u1eafp x\u1ebfp l\u1ea1i {len(self._page_order)} trang th\u00e0nh c\u00f4ng!\n\n"
            f"T\u1ec7p l\u01b0u t\u1ea1i:\n{output_path}"
        )
        self._set_controls_enabled(True)
        self._progress_bar.set(0)
        total_files = len(self._file_paths)
        total_pages = len(self._page_order)
        self._status_label.configure(text=f"{total_files} t\u1ec7p - {total_pages} trang")

    def _on_save_error(self, error_msg):
        self._is_processing = False
        self._set_controls_enabled(True)
        self._progress_bar.set(0)
        self._status_label.configure(text="L\u1ed7i")
        messagebox.showerror("L\u1ed7i", f"Kh\u00f4ng th\u1ec3 l\u01b0u PDF:\n\n{error_msg}")

    def _set_controls_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        self._save_btn.configure(state=state, text="\u0110ang x\u1eed l\u00fd..." if not enabled else "L\u01b0u PDF")
        self._add_btn.configure(state=state)
        self._clear_btn.configure(state=state)
