# <center> RSA Implementation:

## Packages involed:
- math
- random
- sympy ( might need to be installed ) [!pip install sympy]

## Steps involed:

1. Get the prime number p and q from user.

2. Find n and z

> NOTE: Here z is the phi of n

3. Generate random encryption key - e `Conditions Applied`

4. Compute decryption key - d

5. Get the message from user - m `Conditions Applied`

6. Encrypt and Decrypt the text to verify RSA

## Conditions to be noted:

1. Encryption Key Generation
    - 1 < e < z
    - prime

2. Getting message 
    - gcd of meessage and n == 1