import os
import fitz
from PIL import Image


def get_split_page_info(file_path):
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


def get_split_thumbnail(pdf_path, page_num, max_size=(120, 160)):
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


def split_all_pages(input_path, output_dir, base_name=None, progress_callback=None):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Khong tim thay tep: {input_path}")

    doc = fitz.open(input_path)
    total = len(doc)

    if total == 0:
        doc.close()
        raise ValueError("PDF khong co trang nao.")

    if base_name is None:
        base_name = os.path.splitext(os.path.basename(input_path))[0]

    output_files = []
    for i in range(total):
        new_doc = fitz.open()
        new_doc.insert_pdf(doc, from_page=i, to_page=i)
        output_path = os.path.join(output_dir, f"{base_name}_Trang_{i+1}.pdf")
        new_doc.save(output_path, garbage=4, deflate=True)
        new_doc.close()
        output_files.append(output_path)
        if progress_callback:
            progress_callback(int((i + 1) / total * 100))

    doc.close()
    return output_files


def extract_selected_pages(input_path, output_dir, page_indices, base_name=None, progress_callback=None):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Khong tim thay tep: {input_path}")

    doc = fitz.open(input_path)
    total_pages = len(doc)

    valid_indices = sorted([i for i in page_indices if 0 <= i < total_pages])
    if not valid_indices:
        doc.close()
        raise ValueError("Khong co trang hop le nao de trich xuat.")

    total = len(valid_indices)

    if base_name is None:
        base_name = os.path.splitext(os.path.basename(input_path))[0]

    output_files = []
    for i, page_idx in enumerate(valid_indices):
        new_doc = fitz.open()
        new_doc.insert_pdf(doc, from_page=page_idx, to_page=page_idx)
        output_path = os.path.join(output_dir, f"{base_name}_Trang_{page_idx+1}.pdf")
        new_doc.save(output_path, garbage=4, deflate=True)
        new_doc.close()
        output_files.append(output_path)
        if progress_callback:
            progress_callback(int((i + 1) / total * 100))

    doc.close()
    return output_files
