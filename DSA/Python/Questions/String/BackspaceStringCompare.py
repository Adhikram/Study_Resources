"""
# Question: Backspace String Compare
# Link: https://leetcode.com/problems/backspace-string-compare/

# Compare two strings with backspace characters

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Process strings from right to left
# 2. Skip characters based on backspaces
# 3. Compare valid characters
# 4. Return equality result

# Key Components:
# - backspace_compare(): Main implementation
# - get_next_valid_index(): Helper for character skipping
# - Two-pointer approach
"""


class BackspaceStringCompare:
    def backspace_compare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = self.get_next_valid_index(s, i)
            j = self.get_next_valid_index(t, j)

            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True

    def get_next_valid_index(self, s: str, index: int) -> int:
        skip = 0
        while index >= 0:
            if s[index] == "#":
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                break
            index -= 1
        return index


def main():
    solution = BackspaceStringCompare()
    s = "ab#c"
    t = "ad#c"
    print(solution.backspace_compare(s, t))  # Expected: True


if __name__ == "__main__":
    main()
