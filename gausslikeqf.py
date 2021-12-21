import math
import numpy
from typing import List, Any, Callable
from scipy.integrate import quad

def calculate_moments(f: Callable, degree: int, a: float, b: float) -> List[float]:
    return [quad(lambda x: f(x) * x ** i, a, b, epsabs=1.49e-10, epsrel=1.49e-10)[0] for i in range(0, degree + 1)]

def gauss_qf2(f, ro, a, b, n):
    moments = calculate_moments(ro, 2 * n - 1, a, b)
    print("Моменты весовой функции:")
    for i in range(len(moments)):
        print("\tMu{} = {}".format(i, moments[i]))
    ys = [-mu for mu in moments[n:]]
    xs = [[moments[j + i] for j in range(n - 1, -1, -1)] for i in range(0, n)]
    ort_pol_coefs = numpy.linalg.solve(xs, ys)
    print("Коэффициенты ортогонального многочлена:")
    for i, coef in enumerate(ort_pol_coefs):
        print("\ta{} = {}".format(i + 1, coef))
    nodes = numpy.roots([1.0, *ort_pol_coefs])
    nodes = [float(i) for i in nodes if i.imag == 0 and float(i) > a and float(i) < b]
    print("Узлы КФ:")
    for i, node in enumerate(nodes):
        print("\tx{} = {}".format(i + 1, node))
    if len(nodes) != n:
        print("Некоторые узлы оказались не вещественными или не лежат внутри [{}, {}]".format(a, b))
    n = len(nodes)
    eq_lvalues = [[node ** i for node in nodes] for i in range(n)]
    eq_rvalues = [moments[i] for i in range(n)]
    coefs = numpy.linalg.solve(eq_lvalues, eq_rvalues)
    print("Коэффициенты КФ:")
    for i, coef in enumerate(coefs):
        print("\tA{} = {}".format(i + 1, coef))
    return sum([coefs[i] * f(nodes[i]) for i in range(len(nodes))])

