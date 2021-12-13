import gaussqf
from math import cos, pi, exp, sin

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

def meler_f(x):
    return exp(x) * sin(x * x)

print("Лабораторная работа №5")
print("Вычисление интегралов при помощи КФ Гаусса")
print("Лабораторная работа №8")
print("Коэффициенты и узлы КФ Гаусса")
for n in range(1, 9):
    print("N = {}:".format(n))
    units = gaussqf.get_units(n)
    coefficients = gaussqf.get_coefficients(units)
    number_len = max([len(str(unit)) + 1 for unit in units])
    for i in range(len(units)):
        print("\t{}".format(units[i]).ljust(number_len), "<-> {}".format(coefficients[i]))

print("Проверка точности КФ Гаусса на многочленах наивысшей степени")
a = []
n_test = 1
for n in (3, 4, 5):
    print("{})".format(n_test), end="")
    n_test += 1
    print("\tКоличество узлов: {}".format(n))
    print("\tНаивысшая степень многочлена: {}".format(2 * n - 1))
    polynom = test_polynom_deg(2 * n - 1)
    print("\tМногочлен:", polynom_str(polynom))
    actual_integral = polynom_integral(polynom, -1, 1)
    print("\tИнтеграл:", actual_integral)
    gauss_integral = gaussqf.gauss_qf(lambda x: gaussqf.compute_polynom(polynom, x), -1, 1, n)
    print("\tИнтеграл по КФ Гаусса:", gauss_integral)
    print("\tАбсолютная фактическая погрешность:", abs(gauss_integral - actual_integral))

print("Вычисление интеграла функции f(x) = cos(x^2) при помощи КФ Гаусса")
n_test = 1
status = "y"
while status == "y":
    a, b = map(float, input("Введите пределы интегрирования [a, b]: ").split(","))
    for n in (3, 6, 7, 8):
        print("{})".format(n_test), end="")

        n_test += 1
        print("\tКоличество узлов: {}".format(n))
        units = gaussqf.get_units(n)
        coefficients = gaussqf.get_coefficients(units)
        units = [a + (b - a) / 2 * (x_k + 1) for x_k in units]
        coefficients = [coef * (b - a) / 2 for coef in coefficients]
        number_len = max([len(str(unit)) + 1 for unit in units])
        print("\tУзлы и коэффициенты:")
        for i in range(len(units)):
            print("\t{}".format(units[i]).ljust(number_len), "<-> {}".format(coefficients[i]))
        print("Результат:", gaussqf.gauss_qf(gauss_f, a, b, n))
    status = input("Вы хотите продолжить? [y/N]:")

print("Вычисление интеграла функции exp(x) * sin(x^2) / sqrt(1 - x^2) при помощи КФ Мелера")
print("Вес ro(x) = 1 / sqrt(1 - x^2)")
print("f(x) =  exp(x) * sin(x^2)")

