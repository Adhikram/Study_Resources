"""
# Question: Remove Maximum Number of Edges to Keep Graph Fully Traversable
# Link: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

# Time Complexity: O(E * α(N))
# Space Complexity: O(N)

# Algorithm:
# 1. Process type 3 edges first (both Alice and Bob)
# 2. Process type 1 edges (Alice only)
# 3. Process type 2 edges (Bob only)
# 4. Count removable edges
"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n - 1

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


class MaximumEdgesToRemove:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        alice = DisjointSet(n + 1)
        bob = DisjointSet(n + 1)
        removable = 0

        # Process type 3 edges
        for t, u, v in edges:
            if t == 3:
                if not alice.union(u, v):
                    removable += 1
                bob.union(u, v)

        # Process type 1 and 2 edges
        for t, u, v in edges:
            if t == 1:
                if not alice.union(u, v):
                    removable += 1
            elif t == 2:
                if not bob.union(u, v):
                    removable += 1

        if alice.components == 0 and bob.components == 0:
            return removable
        return -1


def main():
    solution = MaximumEdgesToRemove()
    edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    print(solution.maxNumEdgesToRemove(4, edges))


if __name__ == "__main__":
    main()
