import gaussqf
from math import cos, pi

def polynom_str(polynom):
    polynom_with_x = [str(k) + "*x^" + str(deg) for deg, k in enumerate(polynom)]
    return " + ".join(polynom_with_x)

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
print("Коэффициенты и узлы КФ Гаусса")
for n in range(1, 9):
    print("N = {}:".format(n))
    units = gaussqf.get_units(n)
    coefficients = gaussqf.get_coefficients(units)
    number_len = max([len(str(unit)) + 1 for unit in units])
    for i in range(len(units)):
        print("\t{}".format(units[i]).ljust(number_len), "<-> {}".format(coefficients[i]))

print("Проверка точности КФ Гаусса на многочленах наивысшей степени")
N_UNITS = (3, 4, 5)
a = []
n_test = 1
for n in N_UNITS:
    print("{})".format(n_test), end="")
    n_test += 1
    print("\tКоличество узлов: {}".format(n))
    print("\tНаивысшая степень многочлена: {}".format(2 * n - 1))
    polynom = test_polynom_deg(2 * n - 1)
    print("\tМногочлен:", polynom_str(polynom))
    actual_integral = polynom_integral(polynom, -1, 0.1)
    print("\tИнтеграл:", actual_integral)
    gauss_integral = gaussqf.gauss_qf(lambda x: gaussqf.compute_polynom(polynom, x), -1, 0.1, n)
    print("\tИнтеграл по КФ Гаусса:", gauss_integral)
    print("\tАбсолютная фактическая погрешность:", abs(gauss_integral - actual_integral))