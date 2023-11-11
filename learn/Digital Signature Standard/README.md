# <center> DSS Implementation:

## Packages involed:
- random

## Steps involed:

1. Get the integer values p and q 

2. Compute g using p, q, and h

3. Get the hashed message - M

4. Generte random encryption key - k `Conditions Applied`

5. Get the private key - x `Conditions Applied`

6. Compute the public key - y 

7. Compute r and s

8. Compute w, u1, u2, v

9. Compare r and v

10. If r == v, then the signature is verified


## Conditions to be noted:

1. Random key - k
    - 1 < k < q

2. Private key - x
    - 1 < x < q