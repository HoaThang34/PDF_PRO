# PDF-PRO — Agent Guide

## Run

```powershell
python main.py
```

No tests, linters, or typecheckers configured. Edit `requirements.txt` when adding dependencies.

## Architecture

- **Entrypoint:** `main.py` → `PDFProApp(ctk.CTk)` (CustomTkinter)
- **3 implemented features** — `Merge` (pypdf), `Sort` (pypdf + PyMuPDF), `Edit & Sign` (PyMuPDF). The rest (Split, Extract Text, Extract Image, Export Excel, Compress) remain stubs.
- **Edit & Sign feature** uses `src/core/pdf_edit.py` (PyMuPDF). Coordinate system: stored in PDF space (y from bottom), converted to/from display space for canvas rendering. UI at `src/ui/pages/edit_page.py`, signature dialog at `src/ui/pages/signature_dialog.py`.
- **8 features** listed in `docs/project_config.md`, 3 implemented + 5 stubs
- **Themes:** `src/ui/themes/theme.py` — dark theme, Segoe UI fonts, 4px spacing scale

## Key Quirks

- **Dual icon system:** SVG constants in `src/assets/icons/icons.py` are **unused**. Active icons are Canvas-drawn functions in `src/ui/components/icon_renderer.py`.
- **No `pyproject.toml`**, no `.gitignore` — only `requirements.txt` governs deps.
- **Git remote:** `origin` points to `https://github.com/HoaThang34/PRD-PRO.git` (PRD, not PDF — likely a typo)
- **Color alpha blend:** `_hex_to_rgba()` in `feature_card.py` hardcodes `bg_rgb = (26, 27, 46)` as a tkinter Canvas workaround
- **CTkScrollableFrame:** `grid_propagate(False)` not supported (takes no args). Use `grid_propagate()` read-only.
- **CTkLabel images:** Must use `CTkImage`, not `ImageTk.PhotoImage`, to avoid UserWarning.
- **All UI strings in Vietnamese** (without diacritics)

## Config

- `.rules/` — 8 AI agent behavior files (agentic-coding, code-quality, coding, core-behavior, FIX_LANGUAGE, output-format, thinking-reasoning, tool-usage). These govern how code should be written.
