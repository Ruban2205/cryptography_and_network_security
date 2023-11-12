# Implement the Signature Scheme - Digital Signature Standard

from cryptography.hazmat.backends import default_backend # pip install cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

def generate_key_pair():
    private_key = dsa.generate_private_key(
        key_size=1024,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode('utf-8'),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False

if __name__ == "__main__":
    private_key, public_key = generate_key_pair()     # Generate key pair

    message = "Hello, this is a test message." # Message to be signed

    signature = sign_message(private_key, message) # Sign the message

    if verify_signature(public_key, message, signature): # Verify the signature
        print("Signature is valid.")
    else:
        print("Signature is not valid.")
