# Caso 002 — correo sospechoso (L1)

Datos simulados: dominios `.example`, IP de documentación y enlace desactivado (`hxxps`, `[.]`). No abras enlaces ni respondas al remitente.

Leé `evidencias/mensaje.eml`, `alerta.txt` y `declaracion.txt`; completá `ticket.md`.

1. Extraé From, Reply-To, Return-Path, IP de entrega, asunto y URL desactivada, con citas de evidencia.
2. Leé `Received` de abajo hacia arriba. Separá afirmaciones del emisor y observaciones del receptor.
3. Interpretá SPF, DKIM y DMARC y la alineación de dominios. Un fallo de autenticación no prueba phishing.
4. Contrastá la alerta y la declaración. Separá recepción, lectura, clic, entrega de credenciales e impacto confirmado o desconocido.
5. Justificá clasificación, severidad, confianza, escalamiento y datos faltantes.

Comandos locales opcionales, desde la raíz: `sed -n '1,45p' casos/caso-002-correo/evidencias/mensaje.eml` muestra cabeceras y cuerpo; `rg -n '^(From|Reply-To|Return-Path|Received|Authentication-Results):' casos/caso-002-correo/evidencias/mensaje.eml` localiza campos; `sha256sum casos/caso-002-correo/evidencias/*` calcula huellas para preservación, sin probar autenticidad.

Ayuda opcional: SPF evalúa el envelope sender; DMARC requiere alineación con el From visible mediante SPF o DKIM. Una declaración no reemplaza la telemetría de clic.
