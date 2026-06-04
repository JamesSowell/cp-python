class SegmentTreeIterative:
    def __init__(self, data):
        self.n = len(data)
        # Store tree in an array of size 2 * n
        self.tree = [float('-inf')] * self.n + data
        self._build()

    def _build(self):
        # Build the tree from leaves up to the root
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def update(self, idx, value):
        """Update element at position idx (0-indexed) with a new value."""
        pos = idx + self.n
        self.tree[pos] = value
        # Move up and update parents
        while pos > 1:
            pos >>= 1
            self.tree[pos] = max(self.tree[pos << 1], self.tree[pos << 1 | 1])

    def query(self, l, r):
        """Query maximum in range [l, r) - inclusive left, exclusive right."""
        res = float('-inf')
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res
