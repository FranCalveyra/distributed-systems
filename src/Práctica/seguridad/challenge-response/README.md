# Challenge-Response con Clave Simétrica

**Python**, usando el módulo estándar `hmac`. Implementa la versión **simplificada de 3 pasos** que describe `seguridad.md`:

1. Alice → Bob: "soy Alice" + `challenge_A` (nonce aleatorio)
2. Bob → Alice: firma de `challenge_A` + `challenge_B` (su propio challenge)
3. Alice → Bob: firma de `challenge_B`

## Qué es "firmar" con clave simétrica

En rigor, es un **HMAC** (Hash-based Message Authentication Code): `HMAC(clave_compartida, challenge)`. Solo quien conoce la clave puede producir ese valor para ese challenge específico — probás que la conocés sin revelarla.

## Cómo correr

```bash
python3 challenge_response.py
```

## Qué muestra

- **Caso 1**: Alice y Bob comparten la clave real → el handshake completo de 3 pasos termina en autenticación mutua exitosa.
- **Caso 2**: un atacante intenta responder en nombre de Bob **sin conocer la clave compartida real** → Alice verifica con `hmac.compare_digest` (comparación en tiempo constante, evita timing attacks) y la firma no coincide. Aborta.

## Sobre la vulnerabilidad a MITM que menciona la teórica

La teórica dice que este protocolo *"es muy propenso a ataques de Man In The Middle"* y que *"si el atacante escucha el canal, puede deducir fácilmente la firma"*. Con HMAC-SHA256 (lo que usamos acá) eso ya no es tan trivial — esa observación aplica más a esquemas de cifrado simétrico débiles o reversibles, no a un MAC criptográfico moderno.

El problema real de fondo es otro: el protocolo **no autentica el canal en sí**, solo a las partes. Un atacante que se interponga desde el principio (antes de que se establezca cualquier confianza) puede *relayar* mensajes entre Alice y Bob sin que ninguno note la diferencia — porque cada uno sigue hablando con la clave real del otro lado, solo que a través del atacante. Eso es justamente lo que resuelve después la criptografía de clave pública con certificados: atar la clave a una identidad verificada por un tercero de confianza.
