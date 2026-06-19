from collections import deque

class BinaryLift:
    def __init__(self, n, adj, root=0):
        self.n = n
        self.LOG = n.bit_length()

        self.depth = [0] * n
        self.root_dist = [0] * n

        self.up = [[-1] * self.LOG for _ in range(n)]

        self._build(adj, root)

    def _build(self, adj, root):
        q = deque([root])

        parent = [-1] * self.n

        while q:
            u = q.popleft()

            for v, w in adj[u]:
                if v == parent[u]:
                    continue

                parent[v] = u

                self.depth[v] = self.depth[u] + 1
                self.root_dist[v] = self.root_dist[u] + w

                self.up[v][0] = u

                q.append(v)

        for j in range(1, self.LOG):
            for u in range(self.n):
                p = self.up[u][j - 1]

                if p != -1:
                    self.up[u][j] = self.up[p][j - 1]

    def kth_ancestor(self, u, k):
        for j in range(self.LOG):
            if k & (1 << j):
                u = self.up[u][j]

                if u == -1:
                    return -1

        return u

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]
        u = self.kth_ancestor(u, diff)

        if u == v:
            return u

        for j in range(self.LOG - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]

        return self.up[u][0]

    def dist(self, u, v):
        """
        number of edges
        """
        a = self.lca(u, v)

        return (
            self.depth[u]
            + self.depth[v]
            - 2 * self.depth[a]
        )

    def weighted_dist(self, u, v):
        """
        sum of edge weights
        """
        a = self.lca(u, v)

        return (
            self.root_dist[u]
            + self.root_dist[v]
            - 2 * self.root_dist[a]
        )