import gaussqf
from math import cos, pi

def test_polynom_deg(x, deg):
    res = 0
    for i in range(deg):
        res += (i + 1) * x ** i
    return res

def gauss_f(x):
    return cos(x * x)

print("Лабораторная работа №5")
print("Вычисление интегралов при помощи КФ Гаусса")
print(test_polynom_deg(0, 4))
N_UNITS = (3, 6, 7, 8)
for n in N_UNITS:
    print(gaussqf.gauss_qf(lambda x: test_polynom_deg(x, 2 * n - 1), 0, 3, n))
