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

def moment(n, x):
    if n == 0:
        return math.exp(x)
    return math.exp(x) * x ** n - n * moment(n - 1, x)

print("Лабораторная работа №6")
print("Приближенное вычисление интегралов при помощи КФ НАСТ")
print("Вариант №8")
print("ro(x) = exp(x)")
print("f(x) = sin(x)")
print("Приближенное вычисление интегралов при помощи СКФ Гаусса")
status = "y"
while status == "y":
    a, b = map(float, input("Введите пределы интегрирования [a, b]: ").split(","))
    n = int(input("Введите число узлов КФ (n): "))
    m = int(input("Введите число отрезков деления [{}, {}] (m): ".format(a, b)))
    h = (b - a) / m
    print("Узлы и коэффициенты исходной КФ Гаусса:")
    units = compoundgaussqf.get_units(n)
    coefficients = compoundgaussqf.get_coefficients(units)
    number_len = max([len(str(unit)) + 1 for unit in units])
    for i in range(len(units)):
        print("\t{}".format(units[i]).ljust(number_len), "<-> {}".format(coefficients[i]))
    res = compoundgaussqf.gauss_qf(fi, a, b, n, m)
    print("Результат СКФ Гаусса для функции exp(x) * sin(x): {:.12f}".format(res))
    print("Абсолютная фактическая погрешность: {}".format(abs(fi_integral(a, b) - res)))
    status = input("Хотите продолжить? y/[n] ")

print("Приближенное вычисление интегралов при помощи КФ типа Гаусса")
status = "y"
while status == "y":
    a, b = map(float, input("Введите пределы интегрирования [a, b]: ").split(","))
    n = int(input("Введите количество узлов: "))
    print("Проверка формулы на полиноме x^3:")
    res = gausslikeqf.gauss_qf2(pol_deg3, a, b, n, moment)
    print("\tРезультат: {:.12f}".format(res))
    print("\tАбсолютная фактическая погрешность:", abs(res - (moment(3, b) - moment(3, a))))
    print("Вычисление интеграла exp(x) * sin(x)")
    res = gausslikeqf.gauss_qf2(f, a, b, n, moment)
    print("Результат: {:.12f}".format(res))
    print("Абсолютная фактическая погрешнось:", abs(fi_integral(a, b) - res))
    status = input("Хотите продолжить? y/[n] ")
