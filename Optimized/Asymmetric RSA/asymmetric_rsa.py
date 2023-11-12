# Implement Asymmetric Cipher. (RSA/EI Gamal)

import random
import math
from sympy import mod_inverse, isprime

def encrypt(message, e, n):
    return (message ** e) % n

def decrypt(cipher, d, n):
    return (cipher ** d) % n


p = int(input("Enter a prime number p: "))
q = int(input("Enter another prime number q: "))

n = p * q

z = (p - 1) * (q - 1)

e = random.randint(2, z - 1)

while not isprime(e):
    e = random.randint(2, z - 1)


d = mod_inverse(e, z)

message = int(input("Enter a message [Number] "))
print()

while math.gcd(message, n) != 1:
    print("Please choose another message.")
    message = int(input("Enter a message [Number] "))

cipher_text = encrypt(message, e, n)

decrypted_message = decrypt(cipher_text, d, n)

print(f"Original Message: {message}")
print(f"Cipher Text: {cipher_text}")
print(f"Decrypted Message: {decrypted_message}")