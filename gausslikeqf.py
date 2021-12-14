import math

def gauss_qf2(f, a, b, moments):
    ms = [abs(moment(b) - moment(a)) for moment in moments]
    print("Моменты весовой функции:")
    for i in range(len(ms)):
        print("\tMu{} = {}".format(i, ms[i]))
    a1 = (ms[0] * ms[3] - ms[2] * ms[1]) / (ms[1] * ms[1] - ms[2] * ms[0])
    a2 = (ms[2] * ms[2] - ms[3] * ms[1]) / (ms[1] * ms[1] - ms[2] * ms[0])
    print("Коэффициенты ортогонального многочлена:")
    print("\ta1 = {}\n\ta2 = {}".format(a1, a2))
    d = a1 * a1 - 4 * a2
    if d <= 0:
        print("Упс! Что-то пошло не так!")
        exit()
    x1 = (-a1 + math.sqrt(d)) / 2
    x2 = (-a1 - math.sqrt(d)) / 2
    print("Узлы КФ:")
    print("\tx1 = {}\n\tx2 = {}".format(x1, x2))
    coef1 = 1 / (x1 - x2) * (ms[1] - x2 * ms[0])
    coef2 = 1 / (x2 - x1) * (ms[1] - x1 * ms[0])
    print("Коэффициенты КФ:")
    print("\tA1 = {}\n\tA2 = {}".format(coef1, coef2))
    return coef1 * f(x1) + coef2 * f(x2)

