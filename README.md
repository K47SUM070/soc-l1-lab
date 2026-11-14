# SOC L1 Lab

Laboratorio educativo **en desarrollo** para practicar tareas iniciales de un analista SOC L1. El caso 001 contiene únicamente datos simulados. La IP `198.51.100.23` pertenece a TEST-NET-2, reservado para documentación; las cuentas, el host y las marcas de tiempo son ficticios. No hay sistemas reales involucrados.

## Estructura

- `index.html`: entrada del sitio estático.
- `mesa-de-trabajo/`: página de navegación.
- `casos/caso-001-ssh/`: instrucciones, registro sintético y ticket editable.
- `plantillas/`: plantilla reutilizable de ticket.
- `recursos/`: espacio para futuras notas públicas.

Los originales `.md` y `auth.log` permanecen en el proyecto para editarlos localmente. Las páginas `*-consulta.html` permiten leerlos con comodidad en el navegador. El sitio publicado **no guarda cambios** en los tickets.

## Empezar el caso 001

1. Abrí la mesa de trabajo.
2. Leé las instrucciones, consultá el registro y completá `casos/caso-001-ssh/ticket.md` en un editor local.
3. Separá hechos de hipótesis y justificá la severidad y el escalamiento.

## Ejecución local

Desde la raíz de este proyecto:

```sh
python3 -m http.server 8080 --bind 127.0.0.1 --directory .
```

Abrí `http://127.0.0.1:8080/mesa-de-trabajo/index.html`. Para detener el servidor, presioná `Ctrl+C` en la terminal donde se ejecuta. Si el puerto 8080 está ocupado, elegí otro libre en el comando y la URL. Python 3 es la única dependencia para servirlo localmente.

## Alojamiento estático

En Vercel o Cloudflare Pages, usá la raíz del repositorio como directorio de salida/publicación. No hay comando de compilación, framework ni backend. No hace falta conectar esos servicios para usar el laboratorio en localhost.
