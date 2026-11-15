# Caso 003 — investigación SSH (L2)

Continuación simulada del caso 001. Su `auth.log` y ticket resuelto permanecen intactos. Los archivos nuevos usan fecha ISO completa y UTC.

## Normalización del original

El original solo registra `Nov 14 HH:MM:SS`, sin año ni zona. Para correlacionar, este ejercicio **supone** `2026-11-14` y UTC para esos eventos. No es un dato extraído del original. Conservá ambas formas y pedí confirmación de año, zona y reloj del host.

Compará el caso 001 con `evidencias/autenticacion.log`, `sudo.log`, `procesos.csv`, `conexiones.csv` y `contexto.md`. Completá `ticket.md`.

1. Armá cronología UTC con fuente y certeza; correlacioná PID, sesión, usuario, IP y tiempo.
2. Evaluá hipótesis de actividad autorizada, uso indebido de credenciales o actividad mixta. Indicá pruebas a favor, en contra y faltantes.
3. Delimitá alcance por cuentas, host, procesos y conexiones observadas; evitá inferir otros sistemas.
4. Analizá padre-hijo y sudo. Una línea o proceso no demuestra intención ni resultado final.
5. Documentá límites, preservación de originales y huellas, clasificación, severidad y escalamiento.
6. Proponé contención condicionada a validación y autorización, con efectos posibles. No ejecutes acciones reales.

Comandos locales opcionales: `rg -n '18080|50204|09:19:07' casos/caso-001-ssh/evidencias/auth.log casos/caso-003-investigacion-ssh/evidencias/*` correlaciona identificadores; `sha256sum casos/caso-001-ssh/evidencias/auth.log casos/caso-003-investigacion-ssh/evidencias/*` registra huellas, sin validar el origen de los eventos; `python3 -m csv casos/caso-003-investigacion-ssh/evidencias/procesos.csv` revisa CSV si el módulo está disponible.

Ayuda opcional: una aprobación de cambio no identifica automáticamente al operador de una sesión. ¿Qué confirmación independiente pedirías?
