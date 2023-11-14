# Implement the Diffie Hellman Cipher

import random

p=int(input())
a=int(input())

xa=random.randint(1,p-1)
xb=random.randint(1,p-1)

y_a=(a**xa)%p
y_b=(a**xb)%p

KA=(y_b**xa)%p
KB=(y_a**xb)%p

if(KA==KB):
    print("Successfull")
else:
    print("Failed")