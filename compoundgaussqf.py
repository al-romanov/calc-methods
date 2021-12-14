from secant import secant

def get_legendre_polynom(n):
    polynom1 = [1]
    if n == 0:
        return polynom1
    polynom2 = [0, 1]
    for i in range(2, n + 1):
        k1 = -(i - 1) / i
        k2 = (2 * i - 1) / i
        polynom = [0] + polynom2
        polynom = [k2 * a for a in polynom]
        for i in range(min(len(polynom1), len(polynom2))):
            polynom[i] += k1 * polynom1[i]
        polynom1 = polynom2
        polynom2 = polynom
    return polynom2

def compute_polynom(polynom, x):
    res = 0;
    for deg, k in enumerate(polynom):
        res += k * x ** deg
    return res

def get_units(n):
    H = 0.001
    m = 1 + int(2 / H)
    polynom = get_legendre_polynom(n)
    return secant(lambda x: compute_polynom(polynom, x), -1, 1, m, 1e-12)

def get_coefficients(units):
    n = len(units)
    if n > 0:
        polynom = get_legendre_polynom(n - 1)
    return [2 * (1 - x_k * x_k) / (n * n * compute_polynom(polynom, x_k) ** 2) for x_k in units]

def gauss_qf(f, a, b, n, m):
    units = get_units(n)
    coefficients = get_coefficients(units)
    h = (b - a) / m
    s = 0.0
    for j in range(m):
        z1 = a + j * h
        z2 = a + (j + 1) * h
        units_j = [t_k * h / 2 + (z1 + z2) / 2 for t_k in units]
        s += sum([f(units_j[i]) * coefficients[i] for i in range(n)])
    return s * h / 2
