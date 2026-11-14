# Caso 001 — actividad SSH

**Datos simulados.** Todos los eventos, identidades y tiempos son ficticios; la IP pertenece a un rango reservado para documentación. No hay sistemas reales involucrados.

## Tu tarea como analista SOC L1

Leé `evidencias/auth.log` y registrá tus hallazgos en `ticket.md`.

1. Identificá la IP de origen, el host de destino y todas las cuentas mencionadas. Indicá qué registro respalda cada dato.
2. Contá los intentos fallidos de autenticación. Separá, si corresponde, los fallos por cuenta.
3. Construí una cronología con horas, acciones y resultado. Conservá el orden de los eventos.
4. Evaluá el acceso exitoso posterior: ¿qué relación temporal y de origen tiene con los fallos? ¿Qué se puede afirmar y qué requiere más evidencia?
5. Examiná la entrada de `sudo` y explicá qué demuestra exactamente.
6. Separá en el ticket los **hechos observados** de las **hipótesis**. Indicá la confianza de tus conclusiones.
7. Proponé severidad y decidí si corresponde escalar. Justificá ambas decisiones e indicá qué información falta para confirmarlas.

No ejecutes acciones sobre sistemas reales. Este ejercicio se resuelve con la evidencia local.
