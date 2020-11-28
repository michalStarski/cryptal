# multiply 2 matrices
def multiply(m1, m2):
    # zip(*m2) -> column from the second matrix
    # zip(m1_r, m2_c) -> creates a tuple from m1 row and m2 column
    return [
        [sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*m2)] for m1_r in m1
    ]
