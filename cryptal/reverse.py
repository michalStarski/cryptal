from cryptal.multiply import multiply

# calculate such (u, v, d) that xu + vn = d and (x,n) = d
# we search for inverted x in fi(n) -> `u` in the formula above


def reverse(x, n):
    B = x
    A = n
    U = 0
    V = 1

    while True:
        q = A // B

        A, B = multiply([[0, 1], [1, -1 * q]], [[A], [B]])

        A = A[0]
        B = B[0]

        U, V = multiply([[0, 1], [1, -1 * q]], [[U], [V]])

        U = U[0]
        V = V[0]

        if B == 0:
            break

    u = U
    d = A
    # v = (d - x * u) / n

    if d != 1:
        raise Exception("Invalid data")

    return u
