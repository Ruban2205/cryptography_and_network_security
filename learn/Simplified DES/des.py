from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    cipher_text = cipher.encrypt(pad(plain_text, DES.block_size))
    return cipher_text

def des_decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plain_text = unpad(cipher.decrypt(cipher_text), DES.block_size)
    return plain_text



key = get_random_bytes(8)  # DES key - 8 bytes

plain_text = b"Hello, World!"
cipher_text = des_encrypt(plain_text, key)

print("Cipher text:", cipher_text)
print("Decrypted text:", des_decrypt(cipher_text, key))