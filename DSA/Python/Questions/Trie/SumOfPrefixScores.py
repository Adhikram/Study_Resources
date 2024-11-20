"""
# Question: Sum of Prefix Scores of Strings
# Link: https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

# Calculate sum of prefix scores for each string

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)

# Algorithm:
# 1. Build Trie from all words
# 2. Track frequency at each node
# 3. Calculate prefix scores
# 4. Return array of scores

# Key Components:
# - TrieNode class with frequency tracking
# - sum_prefix_scores(): Main implementation
# - add_to_trie(): Helper for trie construction
"""


class TrieNode:
    def __init__(self):
        self.freq = 0
        self.children = [None] * 26


class SumOfPrefixScores:
    def sum_prefix_scores(self, words: list[str]) -> list[int]:
        root = TrieNode()

        # Build trie and track frequencies
        for word in words:
            self.add_to_trie(word, root)

        # Calculate scores for each word
        output = []
        for word in words:
            score = 0
            node = root
            for c in word:
                node = node.children[ord(c) - ord("a")]
                score += node.freq
            output.append(score)

        return output

    def add_to_trie(self, word: str, root: TrieNode) -> None:
        node = root
        for c in word:
            idx = ord(c) - ord("a")
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node.children[idx].freq += 1
            node = node.children[idx]


def main():
    solution = SumOfPrefixScores()
    words = ["abc", "ab", "bc", "b"]
    output = solution.sum_prefix_scores(words)
    print(" ".join(map(str, output)))


if __name__ == "__main__":
    main()
