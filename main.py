from src.factor_polynomial_sum_difference_of_cubes import generate_polynomial

for i in range(10):
    polynomial, factored_polynomial = generate_polynomial()
    print()
    print(polynomial)
    print(factored_polynomial)
