import random
import numpy as np
from random import randint
import sys
import math

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''


def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx


def generate_keypair():
    # Generate primes
    primes = PrimeGen(100)
    p = q = 2
    # Select two primes
    while p == q:
        q = primes[randint(0, len(primes)-1)]
        p = primes[randint(0, len(primes)-1)]
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    try:
        plain = [chr(pow(char, key) % n) for char in ciphertext]
    except:
        pass
    # Return the array of bytes as a string
    return ''.join(plain)


def PrimeGen(n=10000):
    primes = []
    chk = 2
    while len(primes) < n:
        ptest = [chk for i in range(2, chk) if chk % i == 0]
        primes += [] if ptest else [chk]
        chk += 1
    return primes


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv) < 2:
            print("usage: python rsa.py \"<message>\"")
            sys.exit(1)

        message = sys.argv[1]

        public, private = generate_keypair()

        print("Public key: ", public)
        print("Private key: ", private)

        encrypted_msg = encrypt(public, message)
        print("Your encrypted message is: ")
        print(''.join(map(lambda x: str(x) + " ", encrypted_msg)))
        print("Your message is:")
        print(decrypt(private, encrypted_msg))
    else:
        # Public key: (29815, 100127)
        # Private key: (x, 100127)

        n = 100127
        nRoot = math.sqrt(n)
        primesN = PrimeGen(nRoot)
        p = 0
        q = 0
        for i in primesN:
            for k in primesN:
                if (i*k == n):
                    p = i
                    q = k

        phi = (p-1) * (q-1)

        pkey = multiplicative_inverse(29815, phi)
        m = decrypt((pkey, 100127), [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327,
                                     92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121])

        print(m)
