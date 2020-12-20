def gcd(a, b):
    while b != 0:
        tmp_a = a
        tmp_b = b

        a = tmp_b
        b = tmp_a % tmp_b

    return a
