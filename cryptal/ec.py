from cryptal.rand import randkbits, random
from cryptal.is_prime import is_prime
from cryptal.is_sqrt_remainder import is_sqrt_remainder
from cryptal.bin_pow import bin_pow
from cryptal.reverse import reverse


def ec_delta(A, B, p):
    return (4 * bin_pow(A, 3, p) + 27 * bin_pow(B, 2, p)) % p


def calc_ec(curve, x):
    A, B, p = curve
    return (bin_pow(x, 3, p) + A * x + B) % p


def generate_ec():
    P_BIT_NUM = 300

    while True:
        k = randkbits(P_BIT_NUM)
        p = 4 * k + 3
        if is_prime(p):
            break

    while True:
        A = random(0, p)
        B = random(0, p)

        delta = ec_delta(A, B, p)

        if delta != 0:
            return (A, B, p)


def rand_ec_point(curve):
    A, B, p = curve

    if ec_delta(*curve) == 0:
        raise Exception("Invalid input")

    while True:
        x = random(0, p)
        f = calc_ec(curve, x)

        if is_sqrt_remainder(p, f):
            break

    y = bin_pow(f, 2, p)
    return (x, y)


def check_ec_point(point, curve):
    x, y = point
    A, B, p = curve

    if ec_delta(*curve) == 0:
        raise Exception("Invalid input")

    L = (y * y) % p
    P = ((x * x * x) + A * x + B) % p

    return L == P


def opposite_point(point, p):
    x, y = point
    x = x % p
    y = y % p

    return (x, p - y)


def sum_ec_points(p1, p2, curve):
    A, B, p = curve
    x1, y1 = p1
    x2, y2 = p2

    if p1 == p2:
        l = ((3 * bin_pow(x1, 2, p) + A) * reverse(2 * y1, p)) % p
        x3 = (bin_pow(l, 2, p) - 2 * x1) % p
        y3 = (l * (x1 - x3) - y1) % p

    else:
        l = ((y2 - y1) * reverse(x2 - x1, p)) % p
        x3 = (bin_pow(l, 2, p) - x1 - x2) % p
        y3 = (l * (x1 - x3) - y1) % p

    return (x3, y3)
