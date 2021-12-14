from math import cos, pi

def get_units(n):
    return [cos(pi * (2 * k - 1) / (2 * n)) for k in range(1, n + 1)]

def get_coefficients(n):
    return [pi / n] * n

def meler_qf(f, n):
    units = get_units(n)
    coefficients = get_coefficients(n)
    return sum([coefficients[i] * f(units[i]) for i in range(n)])
