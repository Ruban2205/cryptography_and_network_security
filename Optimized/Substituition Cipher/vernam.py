def vernam_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return ciphertext

def vernam_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    ciphertext = vernam_encrypt(plaintext, key)

    print(f"Ciphertext: {list(ciphertext)}")
    print(f"Decrypted plaintext: {vernam_decrypt(ciphertext, key)}")