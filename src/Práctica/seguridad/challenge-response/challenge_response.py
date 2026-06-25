"""
Challenge-Response (desafío) con clave simétrica compartida, en la versión
simplificada de 3 pasos que describe `seguridad.md`:

1. Alice le manda a Bob "soy Alice" + un challenge (nonce aleatorio).
2. Bob le manda a Alice: la firma de SU challenge + un nuevo challenge propio.
3. Alice le manda a Bob la firma del challenge que recibió.

"Firmar" con clave simétrica es, en rigor, un HMAC (Hash-based Message
Authentication Code): probás que conocés la clave compartida sin revelarla,
porque solo alguien con la clave puede producir ese HMAC para ese mensaje.

Cómo correr:
    python3 challenge_response.py
"""
import hmac
import os
import secrets


SHARED_KEY = os.urandom(32)  # solo Alice y Bob la conocen


def sign(key: bytes, challenge: bytes) -> bytes:
    """El 'firmado' del challenge: HMAC-SHA256 con la clave compartida."""
    return hmac.new(key, challenge, "sha256").digest()


def verify(key: bytes, challenge: bytes, signature: bytes) -> bool:
    expected = sign(key, challenge)
    return hmac.compare_digest(expected, signature)  # constante en tiempo: evita timing attacks


def handshake(alice_key: bytes, bob_key: bytes) -> bool:
    print("1. Alice -> Bob: 'soy Alice', challenge_A")
    challenge_a = secrets.token_bytes(16)

    print("2. Bob -> Alice: firma(challenge_A), challenge_B")
    signature_b = sign(bob_key, challenge_a)
    challenge_b = secrets.token_bytes(16)

    if not verify(alice_key, challenge_a, signature_b):
        print("   Alice: la firma de 'Bob' NO coincide. Podría ser un impostor sin la clave. ABORTA.")
        return False
    print("   Alice: verifica la firma de Bob. Coincide, confía en que es Bob.")

    print("3. Alice -> Bob: firma(challenge_B)")
    signature_a = sign(alice_key, challenge_b)

    if not verify(bob_key, challenge_b, signature_a):
        print("   Bob: la firma de 'Alice' NO coincide. ABORTA.")
        return False
    print("   Bob: verifica la firma de Alice. Coincide, confía en que es Alice.")

    return True


def main():
    print("=== Caso 1: Alice y Bob comparten la clave real ===")
    ok = handshake(alice_key=SHARED_KEY, bob_key=SHARED_KEY)
    print(f"Resultado: autenticación {'EXITOSA' if ok else 'FALLIDA'}\n")

    print("=" * 60 + "\n")

    print("=== Caso 2: un atacante intenta hacerse pasar por Bob sin la clave ===")
    attacker_key = os.urandom(32)  # el atacante no conoce SHARED_KEY
    ok = handshake(alice_key=SHARED_KEY, bob_key=attacker_key)
    print(f"Resultado: autenticación {'EXITOSA' if ok else 'FALLIDA'}")
    print("(Alice detecta que la firma no coincide con SU clave compartida real con Bob)")


if __name__ == "__main__":
    main()
