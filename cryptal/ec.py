from cryptal.rand import randkbits, random
from cryptal.is_prime import is_prime
from cryptal.bin_pow import bin_pow
from cryptal.reverse import reverse
from cryptal.sqrt import legendre, sqrt


def ec_delta(A, B, p):
    return (4 * bin_pow(A, 3, p) + 27 * bin_pow(B, 2, p)) % p


def calc_ec(curve, x):
    A, B, p = curve
    return (x * x * x + A * x + B) % p


def generate_ec(p=None):
    if p is None:
        BIT_NUM = 300

        while True:
            k = randkbits(BIT_NUM)
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

        if legendre(f, p) != -1:
            break

    y = sqrt(f, p)
    return (x, y)


def check_ec_point(point, curve):
    x, y = point
    A, B, p = curve

    if ec_delta(*curve) == 0:
        raise Exception("Invalid input")

    L = (y * y) % p
    P = calc_ec(curve, x)

    return L == P


def opposite_point(point, p):
    x, y = point
    x = x % p
    y = y % p

    return (x, p - y)


def sum_ec_points(p1, p2, curve):
    # None acts like a neutral element
    if p1 is None:
        return p2

    if p2 is None:
        return p1

    A, B, p = curve
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2 and y1 == (p - y2):
        # neutral element
        return None

    elif p1 == p2:
        l = ((3 * bin_pow(x1, 2, p) + A) * reverse(2 * y1, p)) % p
        x3 = (bin_pow(l, 2, p) - 2 * x1) % p
        y3 = (l * (x1 - x3) - y1) % p

    else:
        l = ((y2 - y1) * reverse(x2 - x1, p)) % p
        x3 = (bin_pow(l, 2, p) - x1 - x2) % p
        y3 = (l * (x1 - x3) - y1) % p

    return (x3, y3)


# Multiply given point by n
def multiply_point(point, n, curve):
    Q = point
    R = None

    while n > 0:
        if n % 2 == 1:
            if R or Q:
                if R is None:
                    R = Q
                else:
                    R = R
            else:
                R = sum_ec_points(R, Q, curve)

            n -= 1

        Q = sum_ec_points(Q, Q, curve)
        n = n // 2
    return R


def message_to_point(M, curve):
    global u

    A, B, p = curve
    u = random(30, 51)

    for j in range(1, u + 1):
        x = (M * u + j) % p
        f = (x * x * x + A * x + B) % p

        if legendre(f, p) == 1:
            y = sqrt(f, p)
            return (x, y)


def point_to_message(point):
    x, y = point
    M = (x - 1) // u
    return M
