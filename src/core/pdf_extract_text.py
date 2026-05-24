import os
import fitz
from PIL import Image


def get_text_page_info(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Khong tim thay tep: {file_path}")

    doc = fitz.open(file_path)
    pages = []
    filename = os.path.basename(file_path)

    for i in range(len(doc)):
        page = doc.load_page(i)
        pages.append({
            "index": i,
            "page_num": i + 1,
            "width": float(page.rect.width),
            "height": float(page.rect.height),
            "file_path": file_path,
            "filename": filename,
        })

    doc.close()
    return pages


def get_text_thumbnail(pdf_path, page_num, max_size=(120, 160)):
    doc = fitz.open(pdf_path)
    try:
        page = doc.load_page(page_num)
        zoom_x = max_size[0] / page.rect.width
        zoom_y = max_size[1] / page.rect.height
        zoom = min(zoom_x, zoom_y, 1.0)
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return img
    finally:
        doc.close()


def get_page_text_preview(file_path, page_index, max_chars=300):
    doc = fitz.open(file_path)
    try:
        page = doc.load_page(page_index)
        text = page.get_text()
        text = text.strip()
        if len(text) > max_chars:
            text = text[:max_chars] + "..."
        return text if text else "(Trang nay khong co van ban)"
    finally:
        doc.close()


def extract_text_to_files(input_path, page_indices, output_dir, base_name=None, combine=False, progress_callback=None):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Khong tim thay tep: {input_path}")

    doc = fitz.open(input_path)
    total = len(page_indices)

    if total == 0:
        doc.close()
        raise ValueError("Khong co trang nao de trich xuat.")

    if base_name is None:
        base_name = os.path.splitext(os.path.basename(input_path))[0]

    output_files = []

    if combine:
        all_text = []
        for i, page_idx in enumerate(page_indices):
            page = doc.load_page(page_idx)
            text = page.get_text()
            header = f"--- Trang {page_idx + 1} ---\n"
            all_text.append(header + text.strip() + "\n\n")
            if progress_callback:
                progress_callback(int((i + 1) / total * 100))

        output_path = os.path.join(output_dir, f"{base_name}_ToanBoVanBan.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.writelines(all_text)
        output_files.append(output_path)
    else:
        for i, page_idx in enumerate(page_indices):
            page = doc.load_page(page_idx)
            text = page.get_text()
            output_path = os.path.join(output_dir, f"{base_name}_Trang_{page_idx + 1}.txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text.strip())
            output_files.append(output_path)
            if progress_callback:
                progress_callback(int((i + 1) / total * 100))

    doc.close()
    return output_files
