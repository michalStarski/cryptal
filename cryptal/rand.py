from random import randint, getrandbits

# pick a number from a to b - 1
def random(a, b):
    return randint(a, b - 1)

def randkbits(k):
    r = getrandbits(k)
    if r > 1:
        return r
    else:
        return randkbits(k)
