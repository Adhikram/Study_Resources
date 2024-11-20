"""
# Question: Find Close Friends in Social Network
# Find groups of closely connected friends using disjoint sets

# Time Complexity: O(N * α(N)) where α is the inverse Ackermann function
# Space Complexity: O(N)

# Algorithm:
# 1. Initialize disjoint set for all users
# 2. Union friends based on connections
# 3. Find groups of close friends
"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


class CloseFriends:
    def find_friend_groups(
        self, n: int, connections: list[list[int]]
    ) -> list[list[int]]:
        dsu = DisjointSet(n)

        for u, v in connections:
            dsu.union(u, v)

        groups = {}
        for i in range(n):
            parent = dsu.find(i)
            if parent not in groups:
                groups[parent] = []
            groups[parent].append(i)

        return list(groups.values())


def main():
    solution = CloseFriends()
    connections = [[0, 1], [1, 2], [3, 4]]
    print(solution.find_friend_groups(5, connections))


if __name__ == "__main__":
    main()
