class Line:
    def __init__(self, m, c):
        self.m = m  # slope
        self.c = c  # intercept

    def val(self, x):
        return self.m * x + self.c


class CHTMax:
    def __init__(self):
        self.lines = []
        self.ptr = 0

    def bad(self, l1, l2, l3):
        # For max hull with slopes added monotonically.
        # Remove l2 if intersection(l1,l2) >= intersection(l2,l3)
        return (l3.c - l1.c) * (l1.m - l2.m) >= (l2.c - l1.c) * (l1.m - l3.m)

    def add(self, m, c):
        line = Line(m, c)

        while len(self.lines) >= 2 and self.bad(self.lines[-2], self.lines[-1], line):
            self.lines.pop()

        self.lines.append(line)

    def query(self, x):
        while self.ptr + 1 < len(self.lines) and self.lines[self.ptr + 1].val(x) >= self.lines[self.ptr].val(x):
            self.ptr += 1

        return self.lines[self.ptr].val(x)