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


from collections import defaultdict


class MinimumWindowSubstring:
    def min_window(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Create frequency map for target string
        target_freq = {}
        for char in t:
            target_freq[char] = target_freq.get(char, 0) + 1

        # Initialize variables
        window_freq = defaultdict(int)
        required = len(target_freq)
        formed = 0
        left = 0
        min_length = float("inf")
        min_left = 0

        # Sliding window
        for right, char in enumerate(s):
            # Expand window by adding current character
            window_freq[char] += 1

            # Check if current character satisfies the frequency requirement
            if char in target_freq and window_freq[char] == target_freq[char]:
                formed += 1

            # Contract window until it ceases to be 'desirable'
            while left <= right and formed == required:
                # Update minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left

                # Remove the leftmost character from the window
                window_freq[s[left]] -= 1
                if s[left] in target_freq and window_freq[s[left]] < target_freq[s[left]]:
                    formed -= 1
                left += 1

        # Return the minimum window or an empty string if no valid window is found
        return "" if min_length == float("inf") else s[min_left:min_left + min_length]

def main():
    solution = MinimumWindowSubstring()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solution.min_window(s, t))  # Expected: "BANC"


if __name__ == "__main__":
    main()
