from cryptal.rand import random
from cryptal.bin_pow import bin_pow


def is_prime(x):
    if x == 1:
        return False

    if x == 2 or x == 3:
        return True

    for _ in range(0, 32):
        # The a values 1 and n-1 are not used as the equality holds for
        # all n and all odd n respectively, hence testing them
        # adds no value.
        if x > 4:
            a = random(2, x - 2)
        else:
            a = random(2, x)
        if bin_pow(a, x - 1, x) != 1:
            return False

    return True
