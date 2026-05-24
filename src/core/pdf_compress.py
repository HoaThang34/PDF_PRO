import os
import fitz
from PIL import Image


def get_compress_page_info(file_path):
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


def get_compress_thumbnail(pdf_path, page_num, max_size=(120, 160)):
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


def get_file_size_str(file_path):
    if isinstance(file_path, (int, float)):
        size = file_path
    else:
        size = os.path.getsize(file_path)
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"
    else:
        return f"{size / (1024 * 1024):.1f} MB"


def get_file_info(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Khong tim thay tep: {file_path}")

    doc = fitz.open(file_path)
    page_count = len(doc)
    has_images = False
    for i in range(min(page_count, 5)):
        page = doc.load_page(i)
        images = page.get_images()
        if images:
            has_images = True
            break
    doc.close()

    return {
        "filename": os.path.basename(file_path),
        "size": os.path.getsize(file_path),
        "size_str": get_file_size_str(file_path),
        "page_count": page_count,
        "has_images": has_images,
    }


def compress_pdf(input_path, output_path, quality="medium", progress_callback=None):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Khong tim thay tep: {input_path}")

    quality_configs = {
        "low": {"garbage": 4, "deflate": True, "ascii": False, "linear": False, "image_quality": 50},
        "medium": {"garbage": 4, "deflate": True, "ascii": False, "linear": True, "image_quality": 75},
        "high": {"garbage": 3, "deflate": True, "ascii": False, "linear": False, "image_quality": 90},
    }

    config = quality_configs.get(quality, quality_configs["medium"])

    doc = fitz.open(input_path)
    total = len(doc)

    if total == 0:
        doc.close()
        raise ValueError("PDF khong co trang nao.")

    for i in range(total):
        page = doc.load_page(i)
        images = page.get_images(full=True)
        for img_info in images:
            xref = img_info[0]
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha > 3:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                img_bytes = pix.tobytes("jpeg", quality=config["image_quality"])
                page.replace_image(xref, stream=img_bytes)
                pix = None
            except Exception:
                pass
        if progress_callback:
            progress_callback(int((i + 1) / total * 50))

    doc.save(
        output_path,
        garbage=config["garbage"],
        deflate=config["deflate"],
        ascii=config["ascii"],
        linear=config["linear"],
        clean=True,
    )
    doc.close()

    if progress_callback:
        progress_callback(100)

    return output_path
