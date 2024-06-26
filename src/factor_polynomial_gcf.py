import random
import math


def generate_polynomial():
    # Choose a random GCF greater than 1
    gcf = random.randint(2, 16)

    # Generate coefficients that are multiples of the GCF
    a = gcf * random.randint(1, 10)
    b = gcf * random.randint(1, 10)
    c = gcf * random.randint(1, 10)

    # Ensure the trinomial is prime (cannot be factored further over integers)
    discriminant = b**2 - 4*a*c
    while discriminant >= 0 and is_perfect_square(discriminant):
        a = gcf * random.randint(1, 10)
        b = gcf * random.randint(1, 10)
        c = gcf * random.randint(1, 10)
        discriminant = b**2 - 4*a*c

    # Construct the polynomial and its factored form
    polynomial = f"{a}x^2 + {b}x + {c}"
    a_gcf = a // gcf
    b_gcf = b // gcf
    c_gcf = c // gcf
    factored_polynomial = f"{gcf}({a_gcf}x^2 + {b_gcf}x + {c_gcf})"

    return polynomial, factored_polynomial


def is_perfect_square(n):
    return n == math.isqrt(n) ** 2


poly, factored_poly = generate_polynomial()


def generate_front():
    return f"Factor: {poly}"


def generate_back():
    return factored_poly
