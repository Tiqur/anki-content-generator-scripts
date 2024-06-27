import random


def get_sign(b):
    return "+" if b else "-"


def generate_polynomial():
    b = random.randint(2, 6)

    sign_bool = random.choice([True, False])
    sign = get_sign(sign_bool)

    polynomial = f"x^3 {sign} {b**3}"
    factored_polynomial = f"(x {sign} {b})(x^2 {
        get_sign(not sign_bool)} {b}x + {b**2})"

    return polynomial, factored_polynomial


def generate_card():
    poly, factored_poly = generate_polynomial()
    front = f"Factor: {poly}"
    back = factored_poly
    return front, back
