"""
# Question: Implement Trie II (Prefix Tree)
# Link: https://leetcode.com/problems/implement-trie-ii-prefix-tree/

# Implement a trie with word count tracking

# Time Complexity:
# - insert: O(n)
# - countWordsEqualTo: O(n)
# - countWordsStartingWith: O(n)
# - erase: O(n)

# Space Complexity: O(n)

# Algorithm:
# 1. Use TrieNode with children array
# 2. Track word count and prefix count
# 3. Implement insert, count, and erase operations
# 4. Maintain accurate counts during operations

# Key Components:
# - TrieNode class implementation
# - Word and prefix count tracking
# - Search functionality
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0  # Count of words ending here
        self.prefix = 0  # Count of words using this prefix


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
            node.prefix += 1
        node.count += 1

    def count_words_equal_to(self, word: str) -> int:
        node = self._search(word)
        return node.count if node else 0

    def count_words_starting_with(self, prefix: str) -> int:
        node = self._search(prefix)
        return node.prefix if node else 0

    def erase(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            node = node.children[idx]
            node.prefix -= 1
        node.count -= 1

    def _search(self, s: str) -> TrieNode:
        node = self.root
        for c in s:
            idx = ord(c) - ord("a")
            if not node.children[idx]:
                return None
            node = node.children[idx]
        return node


def main():
    trie = Trie()
    trie.insert("apple")
    trie.insert("apple")
    print(trie.count_words_equal_to("apple"))
    print(trie.count_words_starting_with("app"))
    trie.erase("apple")
    print(trie.count_words_equal_to("apple"))


if __name__ == "__main__":
    main()
