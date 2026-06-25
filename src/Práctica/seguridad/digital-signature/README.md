# Firma Digital (optimizada)

**Python** con la librería [`cryptography`](https://cryptography.io/) — implementar RSA a mano es exactamente el tipo de cosa que **nunca** se debe hacer manualmente en producción, un error sutil en la implementación es gravísimo. Acá el código se enfoca en el flujo conceptual, no en reinventar la criptografía.

## El esquema (de `seguridad.md`)

La firma digital "ingenua" (encriptar el dato completo con la clave privada) es **muy costosa** con criptografía asimétrica. La versión optimizada:

1. Generar un **hash** del dato (SHA-256).
2. **Firmar el hash** con la clave privada del firmante (no el dato completo). Eso es la firma.
3. Adjuntarla al dato.

Para verificar: se recalcula el hash del dato recibido y se valida la firma contra la clave **pública** del firmante. Usamos RSA-PSS (el esquema moderno recomendado), no el viejo PKCS1v1.5.

## Cómo correr

```bash
pip install -r requirements.txt
python3 digital_signature.py
```

## Qué muestra

1. **Caso normal**: Alice firma, Bob verifica con la clave pública de Alice → válida.
2. **Documento modificado**: alguien cambia el monto de la transferencia después de firmada → la firma (la misma) ya **no es válida**, porque el hash del documento modificado no coincide con el que se firmó. Esto demuestra **integridad**.
3. **Impostor**: alguien sin la clave privada de Alice intenta firmar en su nombre → la verificación contra la clave pública de Alice falla. Esto demuestra **autenticidad** — solo la clave privada de Alice produce firmas válidas contra su clave pública correspondiente.

## Relación con la teoría

Esto es exactamente la combinación que `seguridad.md` remarca como necesaria: *"autenticación e integridad deben ir juntos — no le sirve de nada a Bob saber que un mensaje vino de Alice si no se puede asegurar que no fue modificado."* La firma cubre ambas al mismo tiempo: el **caso 3** prueba autenticidad, el **caso 2** prueba integridad.
