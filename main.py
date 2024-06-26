from src.factor_polynomial_grouping import generate_polynomial

for i in range(10):
    polynomial, factored_polynomial = generate_polynomial()
    print()
    print(polynomial)
    print(factored_polynomial)
