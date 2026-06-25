"""
Firma digital optimizada, tal como la describe `seguridad.md`:

1. Generar un HASH del dato (no se firma el dato completo: sería muy
   costoso con criptografía asimétrica).
2. ENCRIPTAR ese hash con la clave PRIVADA del firmante. Eso ES la firma.
3. Adjuntar la firma al dato (o certificado).

Para verificar, del otro lado:
- Se recalcula el hash del dato recibido.
- Se "desencripta" la firma con la clave PÚBLICA del firmante (en la práctica,
  RSA con PSS hace esto de forma más prolija, pero el concepto es ese).
- Si el hash recalculado coincide con el que salió de la firma, el dato es
  íntegro y viene de quien dice ser.

Usamos la librería `cryptography` porque implementar RSA a mano sería
reinventar la rueda en un terreno donde un error sutil es gravísimo (justo
el tipo de cosa que en la vida real NUNCA se debe hacer manualmente).

Cómo correr:
    pip install -r requirements.txt
    python3 digital_signature.py
"""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_keypair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()


def sign(private_key, data: bytes) -> bytes:
    """Internamente: hashea `data` con SHA-256 y firma el hash con la
    clave privada (RSA-PSS, el esquema moderno recomendado sobre RSA-PKCS1v1.5)."""
    return private_key.sign(
        data,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )


def verify(public_key, data: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )
        return True
    except Exception:
        return False


def main():
    alice_private, alice_public = generate_keypair()

    documento = b"Transferir $1000 de Alice a Bob"
    print(f"Documento original: {documento!r}")

    firma = sign(alice_private, documento)
    print(f"Firma (primeros 16 bytes en hex): {firma[:16].hex()}...")

    print("\n=== Caso 1: Bob verifica el documento sin modificar ===")
    print(f"¿Firma válida? {verify(alice_public, documento, firma)}")

    print("\n=== Caso 2: alguien interceptó y modificó el documento ===")
    documento_modificado = b"Transferir $9000 de Alice a Bob"
    print(f"Documento modificado: {documento_modificado!r}")
    print(f"¿Firma (la misma) sigue siendo válida? {verify(alice_public, documento_modificado, firma)}")
    print("(el hash del documento modificado no coincide con el que se firmó: detectado)")

    print("\n=== Caso 3: alguien intenta firmar haciéndose pasar por Alice ===")
    impostor_private, _ = generate_keypair()
    firma_falsa = sign(impostor_private, documento)
    print(f"¿La firma del impostor es válida contra la clave PÚBLICA de Alice? "
          f"{verify(alice_public, documento, firma_falsa)}")
    print("(solo la clave privada de Alice produce firmas válidas contra su clave pública)")


if __name__ == "__main__":
    main()
