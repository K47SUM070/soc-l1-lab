#!/usr/bin/env python3
"""Regenera páginas de consulta a partir de originales locales, sin dependencias."""

from __future__ import annotations

import argparse
import html
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CASES = {
    "caso-001-ssh": {"instrucciones.md": "Instrucciones", "ticket.md": "Ticket", "evidencias/auth.log": "Registro SSH"},
    "caso-002-correo": {"instrucciones.md": "Instrucciones", "ticket.md": "Ticket", "evidencias/mensaje.eml": "Mensaje", "evidencias/alerta.txt": "Alerta", "evidencias/declaracion.txt": "Declaración"},
    "caso-003-investigacion-ssh": {"instrucciones.md": "Instrucciones", "ticket.md": "Ticket", "evidencias/autenticacion.log": "Autenticación", "evidencias/sudo.log": "Sudo", "evidencias/procesos.csv": "Procesos", "evidencias/conexiones.csv": "Conexiones", "evidencias/contexto.md": "Contexto"},
}


def page(case: str, source: Path, title: str) -> str:
    relative = source.relative_to(ROOT / "casos" / case)
    nav = "../../../mesa-de-trabajo/index.html" if len(relative.parts) > 1 else "../../mesa-de-trabajo/index.html"
    raw = source.read_text(encoding="utf-8")
    safe_title = html.escape(f"{title} · {case}", quote=True)
    safe_name = html.escape(relative.name, quote=True)
    safe_raw = html.escape(raw, quote=False)
    return f'''<!doctype html>
<html lang="es">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{safe_title}</title>
<style>:root{{color-scheme:dark;font-family:system-ui,sans-serif;background:#0b1220;color:#e5edf8}}body{{max-width:1000px;margin:auto;padding:1.5rem;line-height:1.5}}a{{color:#9ee7d5}}.bar{{display:flex;gap:1.5rem;flex-wrap:wrap}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#162235;border:1px solid #32465f;border-radius:.6rem;padding:1.2rem;font:1rem/1.65 ui-monospace,monospace}}.note{{color:#bdccdf}}</style></head>
<body><nav class="bar"><a href="{nav}">← Mesa de trabajo</a><a href="{safe_name}" download>Descargar original</a></nav><h1>{safe_title}</h1><p class="note">Datos simulados. Consulta de solo lectura; la web no guarda progreso. Editá el ticket original en un editor local.</p><pre>{safe_raw}</pre></body></html>
'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Comprueba que los HTML coinciden con los originales")
    args = parser.parse_args()
    outdated = []
    for case, entries in CASES.items():
        for name, title in entries.items():
            source = ROOT / "casos" / case / name
            destination = source.with_name(source.stem + "-consulta.html")
            rendered = page(case, source, title)
            if args.check:
                if not destination.exists() or destination.read_text(encoding="utf-8") != rendered:
                    outdated.append(str(destination.relative_to(ROOT)))
            else:
                destination.write_text(rendered, encoding="utf-8")
    if outdated:
        print("HTML desactualizado:\n" + "\n".join(outdated))
        return 1
    print("HTML verificado" if args.check else "HTML generado")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
