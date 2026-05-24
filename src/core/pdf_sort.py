import os
from pypdf import PdfReader, PdfWriter


def get_pages_from_files(file_paths):
    all_pages = []
    for file_idx, path in enumerate(file_paths):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Không tìm thấy tệp: {path}")
        reader = PdfReader(path)
        filename = os.path.basename(path)
        for page_idx, page in enumerate(reader.pages):
            all_pages.append({
                "file_index": file_idx,
                "page_index": page_idx,
                "file_path": path,
                "filename": filename,
                "width": float(page.mediabox.width),
                "height": float(page.mediabox.height),
            })
    return all_pages


def reorder_from_files(file_paths, output_path, page_order, progress_callback=None):
    if not file_paths:
        raise ValueError("Không có tệp PDF nào để xử lý.")

    readers = {}
    for path in file_paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Không tìm thấy tệp: {path}")
        readers[path] = PdfReader(path)

    writer = PdfWriter()
    total = len(page_order)
    for i, (file_idx, page_idx) in enumerate(page_order):
        path = file_paths[file_idx]
        writer.add_page(readers[path].pages[page_idx])
        if progress_callback:
            progress_callback(int((i + 1) / total * 100))

    writer.write(output_path)
    writer.close()

    for r in readers.values():
        r.close()

    return output_path


def get_page_thumbnail(pdf_path, page_num, max_size=(120, 160)):
    try:
        import fitz
    except ImportError:
        return None

    doc = fitz.open(pdf_path)
    try:
        page = doc.load_page(page_num)
        zoom_x = max_size[0] / page.rect.width
        zoom_y = max_size[1] / page.rect.height
        zoom = min(zoom_x, zoom_y, 1.0)

        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        from PIL import Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return img
    finally:
        doc.close()
