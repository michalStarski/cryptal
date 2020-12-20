from cryptal.generate_prime import generate_prime
from cryptal.is_prime import is_prime
from cryptal.rand import random
from cryptal.reverse import reverse
from cryptal.bin_pow import bin_pow
from cryptal.gcd import gcd


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


def factorize_n(pub_k, priv_k):
    n, d = priv_k
    _, e = pub_k

    tmp = e * d - 1
    s = 0
    t = None
    while True:
        if tmp % 2 == 0:
            tmp = tmp // 2
            s += 1
        else:
            t = tmp
            break

    a = random(2, n)

    if gcd(a, n) > 1:
        return a

    v = bin_pow(a, t, n)
    if v == 1:
        return None

    while v % n != 1:
        v0 = v % n
        v = bin_pow(v, 2, n)

    if v0 % n == -1:
        return None
    else:
        return gcd(v0 + 1, n)
