"""
# Question: Maximum Score Words Formed by Letters
# Link: https://leetcode.com/problems/maximum-score-words-formed-by-letters/

# Find maximum score possible using given letters to form words

# Time Complexity: O(2^N * M) where N is number of words, M is avg word length
# Space Complexity: O(N) for recursion stack

# Algorithm:
# 1. Count available letters
# 2. Try forming each word combination
# 3. Track letter usage and scores
# 4. Return maximum achievable score

# Key Components:
# - max_score_words(): Main scoring implementation
# - backtrack(): Recursive helper for word combinations
# - Letter counting and validation
"""


class MaxScoreWords:
    def max_score_words(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int:
        # Initialize letter count
        count = [0] * 26
        for ch in letters:
            count[ord(ch) - ord("a")] += 1

        def backtrack(
            words: list[str], count: list[int], score: list[int], index: int
        ) -> int:
            max_score = 0

            # Try each word starting from current index
            for i in range(index, len(words)):
                res = 0
                is_valid = True

                # Check if word can be formed and calculate score
                for ch in words[i]:
                    count[ord(ch) - ord("a")] -= 1
                    res += score[ord(ch) - ord("a")]
                    if count[ord(ch) - ord("a")] < 0:
                        is_valid = False

                # If word is valid, continue with recursion
                if is_valid:
                    res += backtrack(words, count, score, i + 1)
                    max_score = max(res, max_score)

                # Backtrack: restore letter counts
                for ch in words[i]:
                    count[ord(ch) - ord("a")] += 1

            return max_score

        return backtrack(words, count, score, 0)


def main():
    solution = MaxScoreWords()
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [
        1,
        0,
        9,
        5,
        0,
        0,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    print(solution.max_score_words(words, letters, score))  # Expected: 23


if __name__ == "__main__":
    main()
