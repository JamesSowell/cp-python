
# st = SparseTable(A, min)

# st.query(1, 3)  # min(2, 7, 1) = 1
# st.query(0, 1)  # min(4, 2) = 2
# st.query(2, 2)  # min(7) = 7

class SparseTable:
    def __init__(self, arr, op=min):
        n = len(arr)
        self.op = op

        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        K = self.log[n] + 1
        self.st = [arr[:]]

        for j in range(1, K):
            half = 1 << (j - 1)
            length = 1 << j
            prev = self.st[j - 1]

            self.st.append([
                op(prev[i], prev[i + half])
                for i in range(n - length + 1)
            ])

    def query(self, l, r):
        """Inclusive range [l, r], O(1)."""
        j = self.log[r - l + 1]
        return self.op(
            self.st[j][l],
            self.st[j][r - (1 << j) + 1]
        )
