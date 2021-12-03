import gaussqf
from math import cos, pi

def print_polynom(polynom):
    polynom_with_x = polynom
    for deg, k in enumerate(polynom):

def test_polynom_deg(deg):
    return [i + 1 for i in range(deg + 1)]

def polynom_integral(polynom, a, b):
    polynom_integral = polynom
    integral_a = 0
    integral_b = 0
    for deg in range(len(polynom_integral)):
        integral_a += a ** (deg + 1) * polynom_integral[deg] / (deg + 1)
        integral_b += b ** (deg + 1) * polynom_integral[deg] / (deg + 1)
    return integral_b - integral_a


def gauss_f(x):
    return cos(x * x)

print("Лабораторная работа №5")
print("Вычисление интегралов при помощи КФ Гаусса")
print("Проверка точности КФ Гаусса на многочленах наивысшей степени")
N_UNITS = (3, 6, 7, 8)
a = []
for n in N_UNITS:
    print("\tКоличество узлов: {}".format(n))
    print("\tНаивысшая степень многочлена: {}".format(2 * n - 1))
    polynom = test_polynom_deg(2 * n - 1)
    print(gaussqf.gauss_qf(lambda x: gaussqf.compute_polynom(polynom, x), -1, 1, n))
    print(polynom_integral(polynom, -1, 1))
