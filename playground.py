from cryptal.rand import random
from cryptal.ec import (
    generate_ec,
    rand_ec_point,
    multiply_point,
    sum_ec_points,
    message_to_point,
    opposite_point,
    point_to_message,
)
from math import sqrt


def generate_keys(ec):
    A, B, p = ec
    point = rand_ec_point(ec)

    # Hasse's theorem
    x = random(0, p + 1 - (int(2 * sqrt(p))))

    Q = multiply_point(point, x, ec)

    return {"pub": [ec, p, point, Q], "priv": [ec, p, point, Q, x]}


def encrypt(public_key, M):
    ec, p, point, Q = public_key
    Pm = message_to_point(M, ec)

    y = random(0, p + 1 - (int(2 * sqrt(p))))

    C1 = multiply_point(point, y, ec)
    C2 = sum_ec_points(Pm, multiply_point(Q, y, ec), ec)

    return [C1, C2]


def decrypt(C, private_key):
    ec, p, point, Q, x = private_key
    C1, C2 = C
    Pm = sum_ec_points(C2, opposite_point(multiply_point(C1, x, ec), p), ec)
    M = point_to_message(Pm)

    return M


ec = generate_ec()
keys = generate_keys(ec)

C = encrypt(
    keys["pub"], 133739201832091382019328103291832109381039218091839028309183019
)
M = decrypt(C, keys["priv"])

print(M)
