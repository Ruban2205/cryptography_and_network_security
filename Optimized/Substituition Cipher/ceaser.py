def caesar_cipher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        x = ord(char) - ord('a')
        cipher_char = chr((x + shift) % 26 + ord('a'))
        cipher_text += cipher_char
    return cipher_text

def caesar_decipher(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        x = ord(char) - ord('a')
        plain_char = chr((x - shift + 26) % 26 + ord('a'))
        plain_text += plain_char
    return plain_text

if __name__ == "__main__":
    plain_text = input("Enter plain text: ")
    shift = int(input("Enter shift value: "))

    cipher_text = caesar_cipher(plain_text, shift)

    print(f"Cipher text: {cipher_text}")
    print(f"Decrypted plain text: {caesar_decipher(cipher_text, shift)}")