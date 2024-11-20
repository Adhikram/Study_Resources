"""
# Question: Topological Sort Implementation
# Sorts vertices in directed acyclic graph

# Time Complexity: O(V + E)
# Space Complexity: O(V)

# Algorithm:
# 1. DFS-based implementation
# 2. Track visited vertices
# 3. Build sorted order
"""

from collections import defaultdict


class TopologicalSort:
    def topological_sort(self, n: int, edges: list[list[int]]) -> list[int]:
        # Build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        visited = set()
        temp = set()
        order = []

        def dfs(vertex: int) -> bool:
            if vertex in temp:
                return False
            if vertex in visited:
                return True

            temp.add(vertex)
            for neighbor in graph[vertex]:
                if not dfs(neighbor):
                    return False
            temp.remove(vertex)
            visited.add(vertex)
            order.append(vertex)
            return True

        for vertex in range(n):
            if vertex not in visited:
                if not dfs(vertex):
                    return []

        return order[::-1]


def main():
    solution = TopologicalSort()
    edges = [[0, 1], [1, 2], [2, 3]]
    print(solution.topological_sort(4, edges))


if __name__ == "__main__":
    main()
