import random
import math


def generate_polynomial():
    while True:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)

        # Ensure non-zero values for a and c to avoid trivial cases where constants are 0
        if a == 0 or c == 0:
            continue

        # Ensure a and c are both positive if they are both negative
        if a < 0 and c < 0:
            a = -a
            c = -c

        # Coefficients of the quadratic polynomial
        A = a * c
        B = a * d + b * c
        C = b * d

        # Avoid case where A is 1
        if A == 1:
            continue

        # Formatted polynomial
        polynomial = f"{A}x^2 {format_sign(B)} {abs(B)}x {format_sign(C)} {abs(C)}"
        factored_form = f"({a}x {format_sign(b)} {abs(b)})({c}x {format_sign(d)} {abs(d)})"

        # Check if gcd(a, b) == 1 and gcd(c, d) == 1
        if math.gcd(a, b) == 1 and math.gcd(c, d) == 1:
            return polynomial, factored_form


def format_sign(value):
    """Return the appropriate sign for the formatted string."""
    return "+" if value >= 0 else "-"


def generate_card():
    poly, factored_poly = generate_polynomial()
    front = f"Factor: {poly}"
    back = factored_poly
    return front, back
