"""
# Question: Satisfiability of Equality Equations
# Link: https://leetcode.com/problems/satisfiability-of-equality-equations/

# Problem Statement:
# Given an array of strings equations that represent relationships between variables where
# each string equations[i] is of length 4 and takes one of two forms: "xi==yi" or "xi!=yi".
# Return true if it is possible to assign integers to variable names to satisfy all equations.

# Example:
# Input: equations = ["a==b","b!=a"]
# Output: False
# Explanation: If we assign a = 1 and b = 1, then the first equation is satisfied, but not the second.
"""

from typing import List

# 1. Union Find Solution
"""
Algorithm:
1. Create disjoint sets for all characters
2. Process all equality equations first (==)
3. Union characters that should be equal
4. Check inequality equations (!=)
5. Return false if any inequality is violated

Time Complexity: O(N) where N is length of equations
Space Complexity: O(1) as we only need 26 characters
"""


class UnionFind:
    def __init__(self):
        self.parent = list(range(26))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        self.parent[self.find(x)] = self.find(y)


def equations_possible(equations: List[str]) -> bool:
    # Initialize Union-Find data structure
    uf = UnionFind()

    # Process equality equations
    for eq in equations:
        if eq[1] == "=":
            x = ord(eq[0]) - ord("a")
            y = ord(eq[3]) - ord("a")
            uf.union(x, y)

    # Check inequality equations
    for eq in equations:
        if eq[1] == "!":
            x = ord(eq[0]) - ord("a")
            y = ord(eq[3]) - ord("a")
            if uf.find(x) == uf.find(y):
                return False

    return True


# 2. Graph-based DFS Solution
"""
Algorithm:
1. Build graph of equality relationships
2. Use DFS to find connected components
3. Process inequality constraints
4. Check if any inequality violates component membership

Time Complexity: O(N + V) where V is number of variables
Space Complexity: O(V)
"""


def equations_possible_dfs(equations: List[str]) -> bool:
    # Build graph
    graph = [[] for _ in range(26)]
    for eq in equations:
        if eq[1] == "=":
            x = ord(eq[0]) - ord("a")
            y = ord(eq[3]) - ord("a")
            graph[x].append(y)
            graph[y].append(x)

    # DFS to mark components
    def dfs(node: int, component: int, components: List[int]):
        if components[node] == -1:
            components[node] = component
            for neighbor in graph[node]:
                dfs(neighbor, component, components)

    # Find connected components
    components = [-1] * 26
    component = 0
    for i in range(26):
        if components[i] == -1 and graph[i]:
            dfs(i, component, components)
            component += 1

    # Check inequalities
    for eq in equations:
        if eq[1] == "!":
            x = ord(eq[0]) - ord("a")
            y = ord(eq[3]) - ord("a")
            if x == y or (
                components[x] != -1
                and components[y] != -1
                and components[x] == components[y]
            ):
                return False

    return True


def main():
    test_cases = [
        ["a==b", "b!=a"],
        ["b==a", "a==b"],
        ["a==b", "b==c", "a!=c"],
        ["c==c", "b==d", "a!=a"],
        ["a==b", "b!=c", "c==a"],
    ]

    for i, equations in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Equations: {equations}")
        print(f"Union-Find Solution: {equations_possible(equations)}")
        print(f"DFS Solution: {equations_possible_dfs(equations)}")


if __name__ == "__main__":
    main()
