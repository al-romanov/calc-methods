import gaussqf
import math

def f(x):
    return math.exp(x)

def ro(x):
    return math.sin(x)

def fi(x):
    return ro(x) * f(x)

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
    for
    res = 0
    for i in range(m):
        z1 = a + i * h
        z2 = a + (i + 1) * h
        res += gaussqf.gauss_qf(fi, z1, z2, n)
    print("Результат СКФ Гаусса: {:.12f}".format(res))
    status = input("Хотите продолжить? y/[n] ")
