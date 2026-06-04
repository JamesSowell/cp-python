class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i):  # sum [0..i]
        i += 1
        res = 0
        while i:
            res += self.bit[i]
            i -= i & -i
        return res

    def range_sum(self, l, r):
        return self.sum(r) - (self.sum(l - 1) if l else 0)