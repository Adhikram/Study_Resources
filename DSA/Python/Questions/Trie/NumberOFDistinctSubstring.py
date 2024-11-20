"""
# Question: Number of Distinct Substrings
# Link: https://leetcode.com/problems/number-of-distinct-substrings/

# Count distinct substrings in a string using Trie

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

# Algorithm:
# 1. Build Trie from all possible substrings
# 2. Track new nodes for distinct substrings
# 3. Count unique paths in Trie
# 4. Include empty string in final count

# Key Components:
# - TrieNode class implementation
# - count_distinct_substrings(): Main counter
# - Trie insertion and counting logic
"""


class TrieNode:
    def __init__(self):
        self.links = [None] * 26

    def contains_key(self, ch: str) -> bool:
        return self.links[ord(ch) - ord("a")] is not None

    def get(self, ch: str) -> "TrieNode":
        return self.links[ord(ch) - ord("a")]

    def put(self, ch: str, node: "TrieNode") -> None:
        self.links[ord(ch) - ord("a")] = node


def count_distinct_substrings(s: str) -> int:
    root = TrieNode()
    n = len(s)
    count = 0

    # Generate all substrings and insert into trie
    for i in range(n):
        node = root
        for j in range(i, n):
            if not node.contains_key(s[j]):
                node.put(s[j], TrieNode())
                count += 1
            node = node.get(s[j])

    # Add 1 for empty string
    return count + 1


def main():
    s1 = "ababa"
    print(
        f"Total number of distinct substrings for s1: {count_distinct_substrings(s1)}"
    )

    s2 = "ccfdf"
    print(
        f"Total number of distinct substrings for s2: {count_distinct_substrings(s2)}"
    )


if __name__ == "__main__":
    main()
