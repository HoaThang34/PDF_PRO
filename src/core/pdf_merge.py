import os
from pypdf import PdfWriter


def merge_pdfs(input_paths, output_path, progress_callback=None):
    if not input_paths:
        raise ValueError("Khong co tep PDF nao de ghep.")

    writer = PdfWriter()
    total = len(input_paths)

    for i, path in enumerate(input_paths):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Khong tim thay tep: {path}")
        writer.append(path)
        if progress_callback:
            progress_callback(int((i + 1) / total * 100))

    writer.write(output_path)
    writer.close()
    return output_path
