import math
import numpy

def gauss_qf2(f, a, b, n, moment):
    ms = [moment(i, b) - moment(i, a) for i in range(2 * n)]
    print("Моменты весовой функции:")
    for i in range(len(ms)):
        print("\tMu{} = {}".format(i, ms[i]))
    eq_lvalues = [[ms[i + n - 1 - j] for j in range(n)] for i in range(n)]
    eq_rvalues = [-ms[n + i] for i in range(n)]
    ort_pol_coefs = numpy.linalg.solve(eq_lvalues, eq_rvalues)
    print("Коэффициенты ортогонального многочлена:")
    for i, coef in enumerate(ort_pol_coefs):
        print("\ta{} = {}".format(i + 1, coef))
    print([1, *ort_pol_coefs])
    nodes = numpy.roots([1, *ort_pol_coefs])

    print("Узлы КФ:")
    for i, node in enumerate(nodes):
        print("\tx{} = {}".format(i + 1, node))
    ro = lambda x: moment(0, x)
    eq_lvalues = [[node ** i for node in nodes] for i in range(n)]
    eq_rvalues = [moment(i, b) - moment(i, a) for i in range(n)]
    coefs = numpy.linalg.solve(eq_lvalues, eq_rvalues)
    print("Коэффициенты КФ:")
    for i, coef in enumerate(coefs):
        print("\tA{} = {}".format(i + 1, coef))
    return sum([coefs[i] * f(nodes[i]) for i in range(n)])

