class DSU:
    def __init__(self, n):
        # Parent pointer, initialized to itself
        self.parent = list(range(n))

        # Rank for union-by-rank optimization
        self.rank = [0] * n

        # Tracks total number of connected components
        self.num_sets = n

    def find(self, i):
        # Path compression
        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j

            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i

            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1

            # Decrease the number of sets when a merge occurs
            self.num_sets -= 1
            return True

        return False