from cryptal.rand import randkbits
from cryptal.is_prime import is_prime


def generate_prime(bit_num=256):
    while True:
        r = randkbits(bit_num)
        if is_prime(r):
            return r
