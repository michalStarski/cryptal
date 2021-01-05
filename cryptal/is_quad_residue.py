from cryptal.sqrt import legendre


# Calculate if b is quadratic remainder in Z*_p group
def is_quad_residue(p, b):
    euler_value = legendre(b, p)
    return True if euler_value == 1 else False
