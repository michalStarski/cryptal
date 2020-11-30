from cryptal.sqrt import euler_theorem


# Calculate if b is quadratic remainder in Z*_p group
def is_sqrt_remainder(p, b):
    euler_value = euler_theorem(b, p)
    return True if euler_value == 1 else False
