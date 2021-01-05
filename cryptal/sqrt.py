from cryptal.bin_pow import bin_pow


def legendre(a, p):
    symbol = bin_pow(a, ((p - 1) // 2), p)
    return symbol if symbol == 1 or symbol == 0 else -1


def sqrt(a, p):
    if p % 4 != 3:
        raise Exception("p must be a valid prime that equals 3 (mod 4)")

    b = bin_pow(a, ((p + 1) // 4), p)

    return p - b
