# SOC L1 Lab

Laboratorio educativo con tres casos de análisis SOC L1/L2. Todos los datos son simulados: IP de los rangos TEST-NET, dominios `.example`, cuentas, hosts y tiempos ficticios. No hay sistemas reales involucrados.

## Estructura

- `index.html`: entrada del sitio estático.
- `mesa-de-trabajo/`: página de navegación.
- `casos/caso-001-ssh/`: práctica guiada completada; registro y ticket resuelto preservados.
- `casos/caso-002-correo/`: triage L1 de correo, pendiente.
- `casos/caso-003-investigacion-ssh/`: continuación L2 del caso 001, pendiente.
- `generar_html.py`: genera las páginas de consulta a partir de los originales.
- `plantillas/`: plantilla reutilizable de ticket.
- `recursos/`: espacio para futuras notas públicas.

Los originales `.md`, `.log`, `.csv`, `.txt` y `.eml` permanecen en el proyecto. Cada página `*-consulta.html` muestra contenido escapado y permite descargar el original. El sitio publicado **no guarda progreso ni cambios** en los tickets. Editá los tickets pendientes con un editor local.

## Uso

1. Abrí la mesa de trabajo.
2. Usá el caso 001 como práctica guiada y referencia de ticket resuelto.
3. Elegí el caso 002 o 003, leé sus instrucciones y evidencias y completá su `ticket.md` localmente.

## Regenerar HTML

Desde la raíz del repo, ejecutá `python3 generar_html.py`. El generador usa solo la biblioteca estándar, escapa el contenido y lee también el ticket 001 tal como está; no modifica los originales. `python3 generar_html.py --check` verifica que las páginas estén actualizadas. Regenerá antes de publicar si editaste cualquier original.

## Ejecución local

Desde la raíz de este proyecto:

```sh
python3 -m http.server 8080 --bind 127.0.0.1 --directory .
```

Abrí `http://127.0.0.1:8080/mesa-de-trabajo/index.html`. Para detener el servidor, presioná `Ctrl+C` en la terminal donde se ejecuta. Si el puerto 8080 está ocupado, elegí otro libre en el comando y la URL. Python 3 es la única dependencia para servirlo localmente.

## Alojamiento estático

En Vercel o Cloudflare Pages, usá la raíz del repositorio como directorio de salida/publicación. Ejecutá el generador localmente antes de subir los archivos estáticos; no hay backend ni almacenamiento de progreso. No hace falta conectar esos servicios para usar el laboratorio en localhost.
