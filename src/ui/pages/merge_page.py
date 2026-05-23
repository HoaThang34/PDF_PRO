import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from threading import Thread

from src.ui.themes.theme import COLORS, FONTS, SPACING
from src.core.pdf_merge import merge_pdfs


class MergePage(ctk.CTkFrame):
    """Trang ghep nhieu file PDF thanh mot."""

    def __init__(self, master, on_back=None):
        super().__init__(master, fg_color=COLORS["bg_primary"])

        self._on_back = on_back
        self._files = []
        self._selected_index = -1
        self._is_merging = False

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
            width=100,
            height=36,
            corner_radius=8,
            command=self._on_back,
        )
        back_btn.grid(row=0, column=0, sticky="w")

        title = ctk.CTkLabel(
            header,
            text="Gh\u00e9p File PDF",
            font=FONTS["heading_lg"],
            text_color=COLORS["accent_purple"],
        )
        title.grid(row=0, column=1)

        add_btn = ctk.CTkButton(
            header,
            text="+ Th\u00eam T\u1ec7p PDF",
            font=FONTS["heading_sm"],
            text_color="#FFFFFF",
            fg_color=COLORS["accent_purple"],
            hover_color=COLORS["btn_hover"],
            height=36,
            corner_radius=8,
            command=self._add_files,
        )
        add_btn.grid(row=0, column=2, sticky="e")

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
        self._placeholder = ctk.CTkLabel(
            self._content_frame,
            text="Ch\u01b0a c\u00f3 t\u1ec7p n\u00e0o \u0111\u01b0\u1ee3c ch\u1ecdn.\n"
                 "Nh\u1ea5n 'Th\u00eam T\u1ec7p PDF' \u0111\u1ec3 b\u1eaft \u0111\u1ea7u.",
            font=FONTS["body"],
            text_color=COLORS["text_muted"],
            justify="center",
        )
        self._placeholder.grid(row=0, column=0, pady=80)

    def _build_bottom_bar(self):
        bottom = ctk.CTkFrame(self, fg_color="transparent")
        bottom.grid(row=2, column=0, padx=SPACING["lg"], pady=(0, SPACING["lg"]), sticky="ew")
        bottom.grid_columnconfigure(0, weight=1)

        btn_frame = ctk.CTkFrame(bottom, fg_color="transparent")
        btn_frame.grid(row=0, column=0, sticky="w")

        self._up_btn = ctk.CTkButton(
            btn_frame, text="\u2191", width=40, height=36,
            fg_color=COLORS["bg_tertiary"], text_color=COLORS["text_primary"],
            hover_color=COLORS["border_hover"], corner_radius=8,
            command=self._move_up,
        )
        self._up_btn.pack(side="left", padx=(0, 6))

        self._down_btn = ctk.CTkButton(
            btn_frame, text="\u2193", width=40, height=36,
            fg_color=COLORS["bg_tertiary"], text_color=COLORS["text_primary"],
            hover_color=COLORS["border_hover"], corner_radius=8,
            command=self._move_down,
        )
        self._down_btn.pack(side="left", padx=(0, 6))

        self._remove_btn = ctk.CTkButton(
            btn_frame, text="X\u00f3a", width=80, height=36,
            fg_color=COLORS["bg_tertiary"], text_color=COLORS["text_primary"],
            hover_color="#DC2626", corner_radius=8,
            command=self._remove_selected,
        )
        self._remove_btn.pack(side="left", padx=(0, 6))

        self._clear_btn = ctk.CTkButton(
            btn_frame, text="X\u00f3a T\u1ea5t C\u1ea3", width=100, height=36,
            fg_color="transparent", text_color=COLORS["text_muted"],
            hover_color=COLORS["bg_tertiary"], corner_radius=8,
            command=self._clear_all,
        )
        self._clear_btn.pack(side="left")

        right_frame = ctk.CTkFrame(bottom, fg_color="transparent")
        right_frame.grid(row=0, column=1, sticky="e")

        self._status_label = ctk.CTkLabel(
            right_frame,
            text="0 t\u1ec7p",
            font=FONTS["body_sm"],
            text_color=COLORS["text_muted"],
        )
        self._status_label.pack(side="left", padx=(0, 12))

        self._progress_bar = ctk.CTkProgressBar(
            right_frame,
            width=180,
            height=8,
            fg_color=COLORS["bg_tertiary"],
            progress_color=COLORS["accent_purple"],
            corner_radius=4,
        )
        self._progress_bar.pack(side="left", padx=(0, 12))
        self._progress_bar.set(0)

        self._merge_btn = ctk.CTkButton(
            right_frame,
            text="Gh\u00e9p PDF",
            font=FONTS["heading_sm"],
            text_color="#FFFFFF",
            fg_color=COLORS["accent_purple"],
            hover_color=COLORS["btn_hover"],
            height=40,
            corner_radius=8,
            command=self._start_merge,
        )
        self._merge_btn.pack(side="left")

        self._update_controls()

    def _add_files(self):
        paths = filedialog.askopenfilenames(
            title="Ch\u1ecdn c\u00e1c t\u1ec7p PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if not paths:
            return
        existing = set(self._files)
        added = False
        for p in paths:
            if p not in existing:
                self._files.append(p)
                existing.add(p)
                added = True
        if added:
            self._selected_index = -1
            self._refresh_file_list()

    def _refresh_file_list(self):
        for w in self._content_frame.winfo_children():
            w.destroy()

        if not self._files:
            self._show_placeholder()
            self._update_controls()
            return

        for i, filepath in enumerate(self._files):
            self._build_file_item(i, filepath)
        self._update_controls()

    def _build_file_item(self, index, filepath):
        filename = os.path.basename(filepath)
        try:
            size_bytes = os.path.getsize(filepath)
            size_str = self._format_size(size_bytes)
        except OSError:
            size_str = "?"

        selected = index == self._selected_index

        row = ctk.CTkFrame(
            self._content_frame,
            fg_color=COLORS["bg_tertiary"] if selected else "transparent",
            corner_radius=8,
            height=40,
        )
        row.grid(row=index, column=0, padx=8, pady=3, sticky="ew")
        row.grid_propagate(False)
        row.grid_columnconfigure(1, weight=1)

        idx_label = ctk.CTkLabel(
            row, text=str(index + 1),
            font=FONTS["body_sm"], text_color=COLORS["text_muted"],
            width=28, anchor="center",
        )
        idx_label.grid(row=0, column=0, padx=(8, 4))

        name_label = ctk.CTkLabel(
            row, text=filename,
            font=FONTS["body"], text_color=COLORS["text_primary"],
            anchor="w",
        )
        name_label.grid(row=0, column=1, sticky="w")

        size_label = ctk.CTkLabel(
            row, text=size_str,
            font=FONTS["body_sm"], text_color=COLORS["text_secondary"],
            width=80, anchor="e",
        )
        size_label.grid(row=0, column=2, padx=(4, 12))

        clickables = [row, idx_label, name_label, size_label]
        for w in clickables:
            w.bind("<Button-1>", lambda e, idx=index: self._select_item(idx), add="+")

        return row

    def _select_item(self, index):
        if self._selected_index == index:
            self._selected_index = -1
        else:
            self._selected_index = index
        self._refresh_file_list()

    def _move_up(self):
        if self._selected_index <= 0:
            return
        idx = self._selected_index
        self._files[idx], self._files[idx - 1] = self._files[idx - 1], self._files[idx]
        self._selected_index = idx - 1
        self._refresh_file_list()

    def _move_down(self):
        if self._selected_index < 0 or self._selected_index >= len(self._files) - 1:
            return
        idx = self._selected_index
        self._files[idx], self._files[idx + 1] = self._files[idx + 1], self._files[idx]
        self._selected_index = idx + 1
        self._refresh_file_list()

    def _remove_selected(self):
        if self._selected_index < 0 or self._selected_index >= len(self._files):
            return
        del self._files[self._selected_index]
        self._selected_index = -1
        self._refresh_file_list()

    def _clear_all(self):
        if not self._files:
            return
        self._files.clear()
        self._selected_index = -1
        self._refresh_file_list()

    def _update_controls(self):
        n = len(self._files)
        has_selection = 0 <= self._selected_index < n

        self._status_label.configure(text=f"{n} t\u1ec7p")
        self._up_btn.configure(state="normal" if has_selection and self._selected_index > 0 else "disabled")
        self._down_btn.configure(
            state="normal" if has_selection and self._selected_index < n - 1 else "disabled"
        )
        self._remove_btn.configure(state="normal" if has_selection else "disabled")
        self._merge_btn.configure(state="normal" if n >= 2 else "disabled")

    def _start_merge(self):
        if self._is_merging:
            return
        if len(self._files) < 2:
            messagebox.showwarning(
                "C\u1ea3nh b\u00e1o",
                "Vui l\u00f2ng th\u00eam \u00edt nh\u1ea5t hai t\u1ec7p PDF \u0111\u1ec3 gh\u00e9p."
            )
            return

        output_path = filedialog.asksaveasfilename(
            title="L\u01b0u t\u1ec7p PDF \u0111\u00e3 gh\u00e9p",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if not output_path:
            return

        self._is_merging = True
        self._set_controls_enabled(False)
        self._progress_bar.set(0)
        self._status_label.configure(text="\u0110ang gh\u00e9p...")

        Thread(target=self._do_merge, args=(output_path,), daemon=True).start()

    def _do_merge(self, output_path):
        try:
            def progress(val):
                self.after(0, lambda: self._progress_bar.set(val / 100))

            merge_pdfs(list(self._files), output_path, progress_callback=progress)
            self.after(0, self._on_merge_success, output_path)
        except Exception as e:
            self.after(0, self._on_merge_error, str(e))

    def _on_merge_success(self, output_path):
        self._is_merging = False
        self._progress_bar.set(1)
        self._status_label.configure(text="Ho\u00e0n t\u1ea5t!")
        self._merge_btn.configure(text="Gh\u00e9p PDF")
        messagebox.showinfo(
            "Th\u00e0nh c\u00f4ng",
            f"\u0110\u00e3 gh\u00e9p {len(self._files)} t\u1ec7p PDF th\u00e0nh c\u00f4ng!\n\n"
            f"T\u1ec7p l\u01b0u t\u1ea1i:\n{output_path}"
        )
        self._files.clear()
        self._selected_index = -1
        self._refresh_file_list()
        self._set_controls_enabled(True)
        self._progress_bar.set(0)
        self._status_label.configure(text="0 t\u1ec7p")

    def _on_merge_error(self, error_msg):
        self._is_merging = False
        self._set_controls_enabled(True)
        self._progress_bar.set(0)
        self._status_label.configure(text="L\u1ed7i")
        self._merge_btn.configure(text="Gh\u00e9p PDF")
        messagebox.showerror("L\u1ed7i", f"Kh\u00f4ng th\u1ec3 gh\u00e9p PDF:\n\n{error_msg}")

    def _set_controls_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        self._merge_btn.configure(state=state, text="\u0110ang gh\u00e9p..." if not enabled else "Gh\u00e9p PDF")
        self._update_controls()

    @staticmethod
    def _format_size(bytes_val):
        if bytes_val < 1024:
            return f"{bytes_val} B"
        elif bytes_val < 1024 * 1024:
            return f"{bytes_val / 1024:.1f} KB"
        else:
            return f"{bytes_val / (1024 * 1024):.1f} MB"
