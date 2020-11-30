from cryptal.generate_prime import generate_prime
from cryptal.is_prime import is_prime
from cryptal.rand import random
from cryptal.reverse import reverse
from cryptal.bin_pow import bin_pow


def generate_keys():
    p = generate_prime()
    q = None
    e = None
    while True:
        q = generate_prime()
        if p != q:
            break

    n = p * q
    fi = (p - 1) * (q - 1)
    l = max(p - 1, q - 1)

    while True:
        e = random(l + 1, fi)
        if is_prime(e):
            break

    d = reverse(e, fi)

    return {"public": (n, e), "private": (n, d)}


def encrypt(pub_k, M):
    n, e = pub_k
    if 0 > M or M > n:
        raise Exception("Invalid message. Message must be 0 <= M < n")

    return bin_pow(M, e, n)


def decrypt(priv_k, C):
    n, d = priv_k

    return bin_pow(C, d, n)
