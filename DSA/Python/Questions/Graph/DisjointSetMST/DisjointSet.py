"""
# Implementation of Disjoint Set Data Structure
# Supports Union and Find operations

# Time Complexity:
# - Find: O(α(N)) amortized
# - Union: O(α(N)) amortized
# where α is the inverse Ackermann function

# Features:
# 1. Path compression in find
# 2. Union by rank
# 3. Size tracking
"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        """Find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union by rank"""
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

    def get_size(self, x: int) -> int:
        """Get size of component containing x"""
        return self.size[self.find(x)]

    def is_connected(self, x: int, y: int) -> bool:
        """Check if two elements are in same component"""
        return self.find(x) == self.find(y)


def main():
    ds = DisjointSet(5)
    ds.union(0, 1)
    ds.union(2, 3)
    print(ds.is_connected(0, 1))  # True
    print(ds.is_connected(0, 2))  # False
    print(ds.get_size(0))  # 2


if __name__ == "__main__":
    main()
