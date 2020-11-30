# calculate (x^k) % n
def bin_pow(x, k, n):
    # slice 0b part of the notation and reverse the binary string
    k_bin = bin(k)[2:][::-1]

    y = 1
    i = len(k_bin) - 1

    while i >= 0:
        y = (y * y) % n

        bit = k_bin[i]

        if bit == "1":
            y = (y * x) % n
        i = i - 1

    return y
