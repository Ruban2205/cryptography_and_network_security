from math import gcd

def affine_cipher_encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        char_index = ord(char.upper()) - 65
        transformed_index = (a * char_index + b) % 26
        transformed_char = chr(transformed_index + 65)
        ciphertext += transformed_char
    return ciphertext

def affine_cipher_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inverse = None

    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break

    for char in ciphertext:
        char_index = ord(char.upper()) - 65
        transformed_index = (a_inverse * (char_index - b)) % 26
        transformed_char = chr(transformed_index + 65)
        plaintext += transformed_char
    return plaintext

def check_alpha(a):
    if gcd(a, 26) == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    a = int(input("Enter value between 1 and 25 - a: "))

    while not check_alpha(a):
        a = int(input("Please try again\nEnter value between 1 and 25 - a: "))
    b = int(input("Enter value between 0 and 25 - b: "))

    ciphertext = affine_cipher_encrypt(plaintext, a, b)

    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted plaintext: {affine_cipher_decrypt(ciphertext, a, b)}")




    # Optional - formatting
    decryptedtext = affine_cipher_decrypt(ciphertext, a, b)
    trans_table = str.maketrans(decryptedtext, plaintext)
    print(decryptedtext.translate(trans_table))