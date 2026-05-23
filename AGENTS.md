# PDF-PRO — Agent Guide

## Run

```powershell
python main.py
```

No tests, linters, or typecheckers configured. Edit `requirements.txt` when adding dependencies.

## Architecture

- **Entrypoint:** `main.py` → `PDFProApp(ctk.CTk)` (CustomTkinter)
- **UI shell only** — no PDF logic exists yet. `src/core/` and `src/utils/` are empty stubs.
- **8 features** listed in `docs/project_config.md`, all unimplemented
- **Themes:** `src/ui/themes/theme.py` — dark theme, Segoe UI fonts, 4px spacing scale

## Key Quirks

- **Dual icon system:** SVG constants in `src/assets/icons/icons.py` are **unused**. Active icons are Canvas-drawn functions in `src/ui/components/icon_renderer.py`.
- **No `pyproject.toml`**, no `.gitignore` — only `requirements.txt` governs deps.
- **Git remote:** `origin` points to `https://github.com/HoaThang34/PRD-PRO.git` (PRD, not PDF — likely a typo)
- **Color alpha blend:** `_hex_to_rgba()` in `feature_card.py` hardcodes `bg_rgb = (26, 27, 46)` as a tkinter Canvas workaround
- **All UI strings in Vietnamese** (without diacritics)

## Config

- `.rules/` — 8 AI agent behavior files (agentic-coding, code-quality, coding, core-behavior, FIX_LANGUAGE, output-format, thinking-reasoning, tool-usage). These govern how code should be written.
