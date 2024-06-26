import random
import math


def generate_polynomial():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    polynomial = f"{a**2}x^2 - {b**2}"
    factored_polynomial = f"({a}x + {b})({a}x - {b})"

    return polynomial, factored_polynomial


def generate_card():
    poly, factored_poly = generate_polynomial()
    front = f"Factor: {poly}"
    back = factored_poly
    return front, back
