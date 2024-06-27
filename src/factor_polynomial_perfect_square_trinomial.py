import random


def generate_polynomial():
    a = random.randint(2, 14)
    b = random.randint(2, 14)

    sign = random.choice(["+", "-"])

    # Construct the polynomial and its factored form
    polynomial = f"{a**2}x^2 {sign} {2*b*a}x + {b**2}"
    factored_polynomial = f"({a}x {sign} {b})^2"

    return polynomial, factored_polynomial


def generate_card():
    poly, factored_poly = generate_polynomial()
    front = f"Factor: {poly}"
    back = factored_poly
    return front, back
