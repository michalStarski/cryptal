from random import randint

# pick a number from a to b - 1
def random(a, b):
    max_bits = len(bin(b - 1)[2:])

    rand_num_bits = ''
    for _ in range(0, max_bits):
        rand_num_bits += str(randint(0, 1))

    rand_num = int(rand_num_bits, 2)
    return min(max(a, rand_num), b)

def randkbits(k):
    rand_num_bits = ''
    for _ in range(0, k + 1):
        rand_num_bits += str(randint(0, 1))

    return int(rand_num_bits, 2)
