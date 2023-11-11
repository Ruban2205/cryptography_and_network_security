# <center> Substituition Ciphers <center>

1. Ceasar Cipher - `Mono Alphabetic`
2. Affine Cipher - `Mono Alphabetic`
3. Vignere Cipher - `Poly Alphabetic`
4. Vernam Cipher - `One Time Pad`

## 1. Ceaser Cipher

Works by shifting the character by n charaters

    E(x) = (x + n) mod 26

where n is the number of characters to be shifted and x is the character to be encrypted.

That is:

    A -> C    if    shift == 2
    B -> E    if    shift == 3

## 2. Affine Cipher

Works by shifting the character by n charaters using a linear function of the form:

    E(x) = (ax + b) mod 26

where a and b are the keys of the cipher and x is the character to be encrypted.

####  Conditions to be satisfied for a and b:
- `a`
    - gcd(a, 26) = 1
    - 1 <= a <= 25
- `b`
    - 0 <= b <= 25   

## 3. Vignere Cipher

`Polyalphabetic cipher` which works by shifting the character by n charaters using a linear function of the form:

    E(x) = (x + k) mod 26

where k is the key of the cipher and x is the character to be encrypted.

> NOTE: Both the plain text and key should be only in lowercase alphabets

## 4. Vernam Cipher

`One time pad` which works by shifting the character by n charaters using a linear function of the form:

    E(x) = Xi XOR Ki

where k is the key of the cipher and X`i` is the character to be encrypted.