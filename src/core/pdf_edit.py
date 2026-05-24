import os
from PIL import Image
import fitz


def open_pdf(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Khong tim thay tep: {file_path}")
    doc = fitz.open(file_path)
    info = {
        "file_path": file_path,
        "page_count": len(doc),
        "title": doc.metadata.get("title", ""),
    }
    doc.close()
    return info


def render_page(file_path, page_num, zoom=1.0):
    doc = fitz.open(file_path)
    page = doc.load_page(page_num)
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    doc.close()
    return img


def get_page_size(file_path, page_num):
    doc = fitz.open(file_path)
    page = doc.load_page(page_num)
    w, h = page.rect.width, page.rect.height
    doc.close()
    return w, h


def _hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def apply_edits_to_pdf(input_path, output_path, edits_by_page, progress_callback=None):
    doc = fitz.open(input_path)
    total_pages = len(edits_by_page)
    processed = 0

    for page_num, page_edits in edits_by_page.items():
        if not page_edits:
            processed += 1
            continue

        page = doc.load_page(page_num)
        page_height = page.rect.height

        for edit in page_edits:
            if edit["type"] == "ink":
                annot = page.add_ink_annot([edit["points"]])
                annot.set_border(width=edit["width"])
                r, g, b = _hex_to_rgb(edit["color"])
                annot.set_colors(stroke=(r / 255, g / 255, b / 255))
                annot.update()

            elif edit["type"] == "text":
                fs = edit["font_size"]
                rect = fitz.Rect(edit["x"], edit["y"] - fs * 1.2, edit["x"] + 500, edit["y"])
                r, g, b = _hex_to_rgb(edit["color"])
                page.add_freetext_annot(
                    rect, text=edit["text"],
                    fontsize=fs, fontname="helv",
                    text_color=(r / 255, g / 255, b / 255),
                    fill_color=(1, 1, 1), border_width=0,
                )

            elif edit["type"] == "image":
                rect = fitz.Rect(
                    edit["x"], edit["y"] - edit["height"],
                    edit["x"] + edit["width"], edit["y"],
                )
                page.insert_image(rect, stream=edit["image_data"])

        processed += 1
        if progress_callback:
            progress_callback(int(processed / total_pages * 100))

    doc.save(output_path, garbage=4, deflate=True)
    doc.close()
    return output_path
