import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from threading import Thread

from src.ui.themes.theme import COLORS, FONTS, SPACING
from src.core.pdf_compress import (
    get_compress_page_info,
    get_compress_thumbnail,
    get_file_info,
    get_file_size_str,
    compress_pdf,
)


class CompressPage(ctk.CTkFrame):

    def __init__(self, master, on_back=None):
        super().__init__(master, fg_color=COLORS["bg_primary"])

        self._on_back = on_back
        self._pdf_path = None
        self._file_info = None
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
            text="N\u00e9n File PDF",
            font=FONTS["heading_lg"],
            text_color=COLORS["accent_cyan"],
        )
        title.grid(row=0, column=1)

        btn_frame = ctk.CTkFrame(header, fg_color="transparent")
        btn_frame.grid(row=0, column=2, sticky="e")

        self._add_btn = ctk.CTkButton(
            btn_frame,
            text="+ Ch\u1ecdn File PDF",
            font=FONTS["heading_sm"],
            text_color="#FFFFFF",
            fg_color=COLORS["accent_cyan"],
            hover_color="#0891B2",
            height=36, corner_radius=8,
            command=self._add_file,
        )
        self._add_btn.pack(side="left")

    def _build_content_area(self):
        self.grid_rowconfigure(1, weight=1)

        main = ctk.CTkFrame(self, fg_color="transparent")
        main.grid(row=1, column=0, padx=SPACING["lg"], pady=SPACING["md"], sticky="nsew")
        main.grid_columnconfigure(0, weight=1)
        main.grid_rowconfigure(0, weight=1)

        self._info_card = ctk.CTkFrame(
            main,
            fg_color=COLORS["bg_secondary"],
            corner_radius=12,
            border_width=1,
            border_color=COLORS["border"],
        )
        self._info_card.grid(row=0, column=0, pady=(0, SPACING["md"]), sticky="nsew")
        self._info_card.grid_columnconfigure(0, weight=1)

        self._placeholder_frame = ctk.CTkFrame(self._info_card, fg_color="transparent")
        self._placeholder_frame.grid(row=0, column=0, pady=60, sticky="ew")
        self._placeholder_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self._placeholder_frame,
            text="Ch\u01b0a c\u00f3 t\u1ec7p n\u00e0o \u0111\u01b0\u1ee3c ch\u1ecdn.\n"
                 "Nh\u1ea5n 'Ch\u1ecdn File PDF' \u0111\u1ec3 m\u1edf t\u00e0i li\u1ec7u v\u00e0 n\u00e9n.",
            font=FONTS["body"],
            text_color=COLORS["text_muted"],
            justify="center",
        ).grid(row=0, column=0)

        self._file_info_frame = ctk.CTkFrame(self._info_card, fg_color="transparent")
        self._file_info_frame.grid(row=0, column=0, padx=SPACING["lg"], pady=SPACING["lg"], sticky="nsew")
        self._file_info_frame.grid_columnconfigure(1, weight=1)
        self._file_info_frame.grid_remove()

        rows = [
            ("T\u00ean t\u1ec7p:", "file_name"),
            ("K\u00edch th\u01b0\u1edbc:", "file_size"),
            ("S\u1ed1 trang:", "file_pages"),
            ("Ch\u1ee9a \u1ea3nh:", "file_images"),
        ]
        self._info_labels = {}
        for i, (label_text, key) in enumerate(rows):
            ctk.CTkLabel(
                self._file_info_frame,
                text=label_text,
                font=FONTS["heading_sm"],
                text_color=COLORS["text_secondary"],
                anchor="w",
            ).grid(row=i, column=0, padx=(0, 24), pady=6, sticky="w")

            self._info_labels[key] = ctk.CTkLabel(
                self._file_info_frame,
                text="",
                font=FONTS["body"],
                text_color=COLORS["text_primary"],
                anchor="w",
            )
            self._info_labels[key].grid(row=i, column=1, pady=6, sticky="w")

        self._quality_frame = ctk.CTkFrame(self._info_card, fg_color="transparent")
        self._quality_frame.grid(row=1, column=0, padx=SPACING["lg"], pady=(0, SPACING["lg"]), sticky="ew")
        self._quality_frame.grid_columnconfigure(1, weight=1)
        self._quality_frame.grid_remove()

        ctk.CTkLabel(
            self._quality_frame,
            text="M\u1ee9c \u0111\u1ed9 n\u00e9n:",
            font=FONTS["heading_sm"],
            text_color=COLORS["text_secondary"],
            anchor="w",
        ).grid(row=0, column=0, padx=(0, 16), sticky="w")

        self._quality_var = ctk.StringVar(value="medium")
        quality_options = [
            ("Th\u1ea5p (ch\u1ea5t l\u01b0\u1ee3ng cao)", "high"),
            ("Trung b\u00ecnh (c\u00e2n b\u1eb1ng)", "medium"),
            ("Cao (gi\u1ea3m t\u1ed1i \u0111a)", "low"),
        ]

        quality_btn_frame = ctk.CTkFrame(self._quality_frame, fg_color="transparent")
        quality_btn_frame.grid(row=0, column=1, sticky="w")

        self._quality_buttons = {}
        for i, (text, val) in enumerate(quality_options):
            btn = ctk.CTkButton(
                quality_btn_frame,
                text=text,
                font=FONTS["body_sm"],
                text_color=COLORS["text_primary"],
                fg_color=COLORS["accent_cyan"] if val == "medium" else COLORS["bg_tertiary"],
                hover_color="#0891B2",
                height=32, corner_radius=8,
                width=180,
                command=lambda v=val: self._select_quality(v),
            )
            btn.grid(row=0, column=i, padx=(0, 8))
            self._quality_buttons[val] = btn

        self._compress_btn_frame = ctk.CTkFrame(self._info_card, fg_color="transparent")
        self._compress_btn_frame.grid(row=2, column=0, padx=SPACING["lg"], pady=(0, SPACING["lg"]), sticky="e")
        self._compress_btn_frame.grid_remove()

        self._compress_btn = ctk.CTkButton(
            self._compress_btn_frame,
            text="N\u00e9n File PDF",
            font=FONTS["heading_sm"],
            text_color="#FFFFFF",
            fg_color=COLORS["accent_cyan"],
            hover_color="#0891B2",
            height=40, corner_radius=8,
            command=self._start_compress,
        )
        self._compress_btn.pack(side="left")

    def _select_quality(self, val):
        self._quality_var.set(val)
        for v, btn in self._quality_buttons.items():
            btn.configure(
                fg_color=COLORS["accent_cyan"] if v == val else COLORS["bg_tertiary"],
                hover_color="#0891B2",
            )

    def _show_file_info(self):
        self._placeholder_frame.grid_remove()
        self._file_info_frame.grid()
        self._quality_frame.grid()
        self._compress_btn_frame.grid()

        info = self._file_info
        self._info_labels["file_name"].configure(text=info["filename"])
        self._info_labels["file_size"].configure(text=info["size_str"])
        self._info_labels["file_pages"].configure(text=str(info["page_count"]))
        self._info_labels["file_images"].configure(
            text="C\u00f3" if info["has_images"] else "Kh\u00f4ng"
        )

    def _build_bottom_bar(self):
        bottom = ctk.CTkFrame(self, fg_color="transparent")
        bottom.grid(row=2, column=0, padx=SPACING["lg"], pady=(0, SPACING["lg"]), sticky="ew")
        bottom.grid_columnconfigure(0, weight=1)

        right_frame = ctk.CTkFrame(bottom, fg_color="transparent")
        right_frame.grid(row=0, column=1, sticky="e")

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
            progress_color=COLORS["accent_cyan"],
            corner_radius=4,
        )
        self._progress_bar.pack(side="left", padx=(0, 12))
        self._progress_bar.set(0)

    def _add_file(self):
        path = filedialog.askopenfilename(
            title="Ch\u1ecdn file PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if not path:
            return

        self._pdf_path = path
        self._status_label.configure(text="\u0110ang \u0111\u1ecdc th\u00f4ng tin...")
        Thread(target=self._load_file_info, daemon=True).start()

    def _load_file_info(self):
        try:
            info = get_file_info(self._pdf_path)
            self._file_info = info
            self.after(0, self._on_load_success)
        except Exception as e:
            self.after(0, lambda: self._on_load_error(str(e)))

    def _on_load_success(self):
        self._status_label.configure(
            text=f"{self._file_info['filename']} - {self._file_info['size_str']}"
        )
        self._show_file_info()
        self._progress_bar.set(0)

    def _on_load_error(self, msg):
        self._pdf_path = None
        self._status_label.configure(text="L\u1ed7i")
        messagebox.showerror("L\u1ed7i", f"Kh\u00f4ng th\u1ec3 \u0111\u1ecdc file PDF:\n\n{msg}")

    def _start_compress(self):
        if self._is_processing or not self._pdf_path:
            return

        output_path = filedialog.asksaveasfilename(
            title="L\u01b0u file PDF \u0111\u00e3 n\u00e9n",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if not output_path:
            return

        if output_path == self._pdf_path:
            messagebox.showerror("L\u1ed7i", "Vui l\u00f2ng ch\u1ecdn t\u00ean file kh\u00e1c v\u1edbi file g\u1ed1c.")
            return

        self._is_processing = True
        self._compress_btn.configure(state="disabled", text="\u0110ang n\u00e9n...")
        self._add_btn.configure(state="disabled")
        self._progress_bar.set(0)
        self._status_label.configure(text="\u0110ang n\u00e9n file PDF...")

        quality = self._quality_var.get()
        Thread(target=self._do_compress, args=(output_path, quality), daemon=True).start()

    def _do_compress(self, output_path, quality):
        try:
            def progress(val):
                self.after(0, lambda: self._progress_bar.set(val / 100))

            old_size = self._file_info["size"]
            compress_pdf(self._pdf_path, output_path, quality=quality, progress_callback=progress)
            new_size = os.path.getsize(output_path)
            self.after(0, self._on_compress_success, output_path, old_size, new_size)
        except Exception as e:
            self.after(0, self._on_compress_error, str(e))

    def _on_compress_success(self, output_path, old_size, new_size):
        self._is_processing = False
        self._progress_bar.set(1)
        reduction = ((old_size - new_size) / old_size * 100) if old_size > 0 else 0
        self._status_label.configure(text="Ho\u00e0n t\u1ea5t!")
        self._compress_btn.configure(state="normal", text="N\u00e9n File PDF")
        self._add_btn.configure(state="normal")

        messagebox.showinfo(
            "Th\u00e0nh c\u00f4ng",
            f"\u0110\u00e3 n\u00e9n file PDF th\u00e0nh c\u00f4ng!\n\n"
            f"K\u00edch th\u01b0\u1edbc g\u1ed1c: {get_file_size_str(old_size)}\n"
            f"K\u00edch th\u01b0\u1edbc sau n\u00e9n: {get_file_size_str(new_size)}\n"
            f"Gi\u1ea3m: {reduction:.1f}%\n\n"
            f"File l\u01b0u t\u1ea1i:\n{output_path}"
        )
        self._progress_bar.set(0)
        self._status_label.configure(
            text=f"{self._file_info['filename']} - {self._file_info['size_str']}"
        )

    def _on_compress_error(self, error_msg):
        self._is_processing = False
        self._compress_btn.configure(state="normal", text="N\u00e9n File PDF")
        self._add_btn.configure(state="normal")
        self._progress_bar.set(0)
        self._status_label.configure(text="L\u1ed7i")
        messagebox.showerror("L\u1ed7i", f"Kh\u00f4ng th\u1ec3 n\u00e9n PDF:\n\n{error_msg}")
