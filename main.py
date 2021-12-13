import gausslikeqf
import compoundgaussqf
import math

from gausslikeqf import gauss_qf2

def f(x):
    return math.sin(x)
def ro(x):
    return math.exp(x)

def pol_deg3(x):
    return x ** 3

def fi(x):
    return ro(x) * f(x)

def fi_integral(a, b):
    return 1 / 2 * (math.sin(b) * math.exp(b) - math.cos(b) * math.exp(b) - math.sin(a) * math.exp(a) + math.cos(a) * math.exp(a))

MOMENTS = [lambda x: math.exp(x),
        lambda x: (x - 1) * math.exp(x),
        lambda x: (x ** 2 - 2 * x + 2) * math.exp(x),
        lambda x: (x ** 3 - 3 * x ** 2 + 6 * x - 6) * math.exp(x)]

print("Лабораторная работа №5")
print("Приближенное вычисление интегралов при помощи КФ НАСТ")
print("Вариант №8")
print("Вес: ro(x) = exp(x)")
print("Функция: f(x) = sin(x)")
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

print("Приближенное вычисление интегралов при помощи КФ типа Гаусса")
status = "y"
while status == "y":
    a, b = map(float, input("Введите пределы интегрирования [a, b]: ").split(","))
    print("Проверка формулы на полиноме x^3:")
    res = gausslikeqf.gauss_qf2(pol_deg3, a, b, MOMENTS)
    print("\tРезультат: {:.12f}".format(res))
    print("\tАбсолютная фактическая погрешность:", abs(res - (MOMENTS[3](b) - MOMENTS[3](a))))
    print("Вычисление интеграла ro(x)*f(x)")
    res = gausslikeqf.gauss_qf2(f, a, b, MOMENTS)
    print("Результат: {:.12f}".format(res))
    print("Абсолютная фактическая погрешнось:", abs(fi_integral(a, b) - res))
    status = input("Хотите продолжить? y/[n] ")
