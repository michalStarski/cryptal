from cryptal.bin_pow import bin_pow

def euler_theorem(a, p):
    return bin_pow(a, ((p + 1) // 4), p)


def sqrt():
    p, a = map(int, input('p, a: ').split())

    if p % 4 != 3:
        raise Exception('p must be a valid prime that equals 3 (mod 4)')

    b = euler_theorem(a, p)

    return p - b