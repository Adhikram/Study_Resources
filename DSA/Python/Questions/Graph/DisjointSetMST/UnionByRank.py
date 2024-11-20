"""
# Implementation of Union-Find with Union by Rank optimization
# Provides efficient operations for disjoint set data structure

# Time Complexity:
# - Find: O(α(N))
# - Union: O(α(N))
# where α is the inverse Ackermann function

# Features:
# 1. Union by rank optimization
# 2. Path compression in find
# 3. Component size tracking
"""


class UnionByRank:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        self.components -= 1
        return True

    def get_size(self, x):
        return self.size[self.find(x)]

    def get_components(self):
        return self.components


def main():
    uf = UnionByRank(5)
    uf.union(0, 1)
    uf.union(2, 3)
    print(uf.get_components())  # 3
    print(uf.get_size(0))  # 2


if __name__ == "__main__":
    main()
