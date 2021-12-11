import compoundgaussqf
import math

def f(x):
    return math.exp(x)
def ro(x):
    return math.sin(x)

def fi(x):
    return ro(x) * f(x)

def fi_integral(a, b):
    return 1 / 2 * (math.sin(b) * math.exp(b) - math.cos(b) * math.exp(b) - math.sin(a) * math.exp(a) + math.cos(a) * math.exp(a))

print("Лабораторная работа №5")
print("Приближенное вычисление интегралов при помощи КФ НАСТ")
print("Вариант №8")
print("Вес: ro(x) = sin(x)")
print("Функция: f(x) = exp(x)")
status = "y"
while status == "y":
    a, b = map(float, input("Введите пределы интегрирования [a, b]: ").split(","))
    n = int(input("Введите число узлов КФ (n): "))
    m = int(input("Введите число отрезков деления [{}, {}] (m): ".format(a, b)))
    h = (b - a) / m
    print("Узлы и коэффициенты исходной КФ Гаусса:")
    units = compoundgaussqf.get_units(n)
    coefficients = compoundgaussqf.get_coefficients(units)
    units = [a + (b - a) / 2 * (x_k + 1) for x_k in units]
    coefficients = [coef * (b - a) / 2 for coef in coefficients]
    number_len = max([len(str(unit)) + 1 for unit in units])
    for i in range(len(units)):
        print("\t{}".format(units[i]).ljust(number_len), "<-> {}".format(coefficients[i]))
    res = compoundgaussqf.gauss_qf(fi, a, b, n, m)
    print("Результат СКФ Гаусса: {:.12f}".format(res))
    print("Абсолютная фактическая погрешность: {}".format(abs(fi_integral(a, b) - res)))
    status = input("Хотите продолжить? y/[n] ")
