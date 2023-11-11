# Implement Transposition Cipher. (Vignere Cipher)

def vigenere_cipher(plain_text, key):
    cipher_text = ""
    key = (key * (len(plain_text) // len(key) + 1))[:len(plain_text)]
    for idx, char in enumerate(plain_text):
        x = ord(char) - ord('a')
        k = ord(key[idx]) - ord('a')
        cipher_char = chr((x + k) % 26 + ord('a'))
        cipher_text += cipher_char
    return cipher_text

def vigenere_decipher(cipher_text, key):
    plain_text = ""
    key = (key * (len(cipher_text) // len(key) + 1))[:len(cipher_text)]
    for idx, char in enumerate(cipher_text):
        x = ord(char) - ord('a')
        k = ord(key[idx]) - ord('a')
        plain_char = chr((x - k + 26) % 26 + ord('a'))
        plain_text += plain_char
    return plain_text

if __name__ == "__main__":
    plain_text = input("Enter plain text: ")
    key = input("Enter key: ")

    cipher_text = vigenere_cipher(plain_text, key)

    print(f"Cipher text: {cipher_text}")
    print(f"Decrypted plain text: {vigenere_decipher(cipher_text, key)}")