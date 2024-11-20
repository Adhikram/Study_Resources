"""
# Question: Alien Dictionary
# Link: https://leetcode.com/problems/alien-dictionary/

# Time Complexity: O(C) where C is total length of all words
# Space Complexity: O(1) since alphabet size is fixed

# Algorithm:
# 1. Build graph from adjacent words
# 2. Detect cycles in character ordering
# 3. Return topological sort order
"""

from collections import defaultdict, deque


class AlienDictionary:
    def alien_order(self, words: list[str]) -> str:
        # Build graph
        graph = defaultdict(set)
        in_degree = defaultdict(int)

        # Add all characters to in_degree
        for word in words:
            for c in word:
                in_degree[c] = 0

        # Build edges from adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # Check invalid case
            if len(w1) > len(w2) and w1[: len(w2)] == w2:
                return ""

            # Find first different character
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        in_degree[c2] += 1
                    break

        # Topological sort using BFS
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        result = []

        while queue:
            c = queue.popleft()
            result.append(c)
            for next_c in graph[c]:
                in_degree[next_c] -= 1
                if in_degree[next_c] == 0:
                    queue.append(next_c)

        return "".join(result) if len(result) == len(in_degree) else ""


def main():
    solution = AlienDictionary()
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(solution.alien_order(words))


if __name__ == "__main__":
    main()
