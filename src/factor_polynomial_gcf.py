import random
import math


def generate_polynomial():
    a, b, c, gcf = None, None, None, None

    # Choose a random GCF greater than 1
    gcf = random.randint(2, 8)

    # Generate coefficients that are multiples of the GCF
    a = random.randint(1, 10) * gcf
    b = random.randint(1, 10) * gcf
    c = random.randint(1, 10) * gcf

    # Get greatest common divisor ( gcf variable not guaranteed to be GCD )
    gcd = math.gcd(a, math.gcd(b, c))

    # Construct the polynomial and its factored form
    polynomial = f"{a}x^2 + {b}x + {c}"
    factored_polynomial = f"{gcd}({a//gcd}x^2 + {b//gcd}x + {c//gcd})"

    return polynomial, factored_polynomial


def generate_card():
    poly, factored_poly = generate_polynomial()
    front = f"Factor: {poly}"
    back = factored_poly
    return front, back
