"""
# Question: Reorganize String
# Link: https://leetcode.com/problems/reorganize-string/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Count character frequencies
# 2. Find maximum frequency character
# 3. Place characters alternately
# 4. Return reorganized string

# Key Components:
# - reorganize_string(): Main implementation
# - Character frequency tracking
# - Alternate placement strategy
"""


class RecognizeString:
    def reorganize_string(self, s: str) -> str:
        # Track character frequencies
        freq = [0] * 26
        max_freq = 0
        letter = 0

        # Count frequencies and find max
        for char in s:
            index = ord(char) - ord("a")
            freq[index] += 1
            if freq[index] > max_freq:
                max_freq = freq[index]
                letter = index

        # Check if reorganization is possible
        if max_freq > (len(s) + 1) // 2:
            return ""

        # Place characters alternately
        result = [""] * len(s)
        idx = 0

        # Place most frequent character
        while freq[letter] > 0:
            result[idx] = chr(letter + ord("a"))
            idx += 2
            freq[letter] -= 1

        # Place remaining characters
        for i in range(26):
            while freq[i] > 0:
                if idx >= len(s):
                    idx = 1
                result[idx] = chr(i + ord("a"))
                idx += 2
                freq[i] -= 1

        return "".join(result)


def main():
    solution = RecognizeString()
    print(solution.reorganize_string("aab"))  # Expected: "aba"
    print(solution.reorganize_string("aaab"))  # Expected: ""


if __name__ == "__main__":
    main()
