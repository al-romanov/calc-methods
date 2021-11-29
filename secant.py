class Segment:
    def __init__(self, begin, end) -> None:
        self.begin = begin
        self.end = end

def separation(f, a, b, n):
    segments = []
    h = (b - a) / n
    for i in range(n + 1):
        if f(a) * f(a + h) <= 0:
            segments.append(Segment(a, a + h))
        a += h
    return segments

def secant(f, a, b, n, accuracy):
    segments = separation(f, a, b, n)
    roots = []
    for seg in segments:
        x0 = (seg.begin + seg.end) / 2
        x1 = x0 + (seg.end - seg.begin) / 5
        x = x1 - (x1 - x0) * f(x1) / (f(x1) - f(x0))
        while abs(x - x1) > 2 * accuracy:
            x0 = x1
            x1 = x
            x = x1 - (x1 - x0) * f(x1) / (f(x1) - f(x0))
        roots.append(x)
    return roots
