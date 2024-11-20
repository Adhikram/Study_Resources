"""
# Question: Number of Operations to Make Network Connected
# Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/

# Time Complexity: O(N + E * α(N))
# Space Complexity: O(N)

# Algorithm:
# 1. Count redundant connections
# 2. Find number of disconnected components
# 3. Check if enough cables available
"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
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
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True


class MakeNetworkConnected:
    def make_connected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        dsu = DisjointSet(n)
        redundant = 0

        for u, v in connections:
            if not dsu.union(u, v):
                redundant += 1

        return dsu.components - 1


def main():
    solution = MakeNetworkConnected()
    connections = [[0, 1], [0, 2], [1, 2]]
    print(solution.make_connected(4, connections))


if __name__ == "__main__":
    main()
