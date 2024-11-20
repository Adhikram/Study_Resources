"""
# Question: Merge Strings Alternately
# Link: https://leetcode.com/problems/merge-strings-alternately/

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

# Algorithm:
# 1. Alternate between strings
# 2. Track position in each string
# 3. Append remaining characters
# 4. Return merged string

# Key Components:
# - merge_alternately(): Main implementation
# - Two-pointer approach
# - String building
"""


class MergeAlternatively:
    def merge_alternately(self, word1: str, word2: str) -> str:
        merged = []
        i = j = 0

        # Merge alternately
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters
        merged.extend(word1[i:])
        merged.extend(word2[j:])

        return "".join(merged)


def main():
    solution = MergeAlternatively()
    word1 = "abc"
    word2 = "pqr"
    print(solution.merge_alternately(word1, word2))  # Expected: "apbqcr"


if __name__ == "__main__":
    main()
