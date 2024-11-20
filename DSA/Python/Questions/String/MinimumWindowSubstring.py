"""
# Question: Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/

# Time Complexity: O(n + m)
# Space Complexity: O(k) where k is charset size

# Algorithm:
# 1. Use sliding window approach
# 2. Track character frequencies
# 3. Maintain window with required characters
# 4. Find minimum valid window

# Key Components:
# - min_window(): Main implementation
# - Character frequency tracking
# - Window size optimization
"""


class MinimumWindowSubstring:
    def min_window(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Create frequency map for target string
        target_freq = {}
        for char in t:
            target_freq[char] = target_freq.get(char, 0) + 1

        # Initialize variables
        window_freq = [0] * 256
        required = len(target_freq)
        formed = 0
        left = right = 0
        min_length = float("inf")
        min_left = min_right = 0

        # Sliding window
        while right < len(s):
            # Expand window
            char = s[right]
            window_freq[ord(char)] += 1

            if char in target_freq and window_freq[ord(char)] == target_freq[char]:
                formed += 1

            # Contract window
            while formed == required:
                # Update minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                    min_right = right

                char = s[left]
                window_freq[ord(char)] -= 1

                if char in target_freq and window_freq[ord(char)] < target_freq[char]:
                    formed -= 1

                left += 1

            right += 1

        return "" if min_length == float("inf") else s[min_left : min_right + 1]


def main():
    solution = MinimumWindowSubstring()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solution.min_window(s, t))  # Expected: "BANC"


if __name__ == "__main__":
    main()
