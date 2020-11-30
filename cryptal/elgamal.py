from cryptal.rand import random, randkbits
from cryptal.bin_pow import bin_pow
from cryptal.is_prime import is_prime
from cryptal.reverse import reverse


def generate_keys():
    p = None
    q = None
    g = None

    while True:
        num = randkbits(1024)
        if is_prime(num) and is_prime(2 * num + 1):
            q = num
            p = 2 * num + 1

            print(q, p)

            while True:
                g = random(1, p - 1)
                x = bin_pow(g, q, p)
                if x != 1:
                    y = bin_pow(g, x, p)
                    return {"public": (p, g, y), "private": (x, p)}


def encrypt(pub_key, M):
    p, g, y = pub_key
    z = random(1, p - 1)
    c1 = bin_pow(g, z, p)

    c2 = M * bin_pow(y, z, p)

    C = [c1, c2]
    return C


def decrypt(priv_key, C):
    x, p = priv_key
    c1, c2 = C
    c1_rev = reverse(c1, p)
    c1_rev_x = bin_pow(c1_rev, x, p)

    return c2 * c1_rev_x % p
