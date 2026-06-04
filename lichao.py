class LiChaoTree:
    def __init__(self, min_x, max_x, minimize=True):
        self.min_x = min_x
        self.max_x = max_x
        self.minimize = minimize
        self.tree = {} # Use dict for sparse tree if range is large

    def _eval(self, line, x):
        return line[0] * x + line[1]

    def add_line(self, m, c, node_l=None, node_r=None, idx=1):
        if node_l is None: node_l, node_r = self.min_x, self.max_x
        new_line = (m, c)
        if idx not in self.tree:
            self.tree[idx] = new_line
            return

        curr_line = self.tree[idx]
        mid = (node_l + node_r) // 2
        
        # Compare at midpoint
        better_at_mid = self._eval(new_line, mid) < self._eval(curr_line, mid) if self.minimize else \
                        self._eval(new_line, mid) > self._eval(curr_line, mid)
        
        if better_at_mid:
            self.tree[idx], new_line = new_line, curr_line
            
        if node_l == node_r: return
        
        # Check intersections to push the "loser" line to children
        better_at_l = self._eval(new_line, node_l) < self._eval(curr_line, node_l) if self.minimize else \
                      self._eval(new_line, node_l) > self._eval(curr_line, node_l)
                      
        if better_at_l:
            self.add_line(*new_line, node_l, mid, 2 * idx)
        else:
            self.add_line(*new_line, mid + 1, node_r, 2 * idx + 1)

    def query(self, x, node_l=None, node_r=None, idx=1):
        if node_l is None: node_l, node_r = self.min_x, self.max_x
        if idx not in self.tree: return float('inf') if self.minimize else float('-inf')
        
        res = self._eval(self.tree[idx], x)
        if node_l == node_r: return res
        
        mid = (node_l + node_r) // 2
        if x <= mid:
            child_res = self.query(x, node_l, mid, 2 * idx)
        else:
            child_res = self.query(x, mid + 1, node_r, 2 * idx + 1)
            
        return min(res, child_res) if self.minimize else max(res, child_res)