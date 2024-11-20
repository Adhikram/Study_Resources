"""
# Question: Longest Absolute File Path
# Link: https://leetcode.com/problems/longest-absolute-file-path/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Split input by newlines
# 2. Track directory levels using stack
# 3. Calculate path lengths
# 4. Return longest valid file path

# Key Components:
# - length_longest_path(): Main implementation
# - Level tracking using array
# - File extension detection
"""


class LongestAbsoluteFilePath:
    def length_longest_path(self, input_str: str) -> int:
        paths = input_str.split("\n")
        stack = [0] * (len(paths) + 1)
        max_len = 0

        for path in paths:
            # Get directory level from tab count
            level = path.rstrip().count("\t") + 1

            # Calculate current path length
            curr_len = len(path.replace("\t", ""))

            # Previous levels sum + current length + 1 for '/'
            stack[level] = stack[level - 1] + curr_len + 1

            # Update max length if current path is a file
            if "." in path:
                max_len = max(max_len, stack[level] - 1)

        return max_len


def main():
    solution = LongestAbsoluteFilePath()
    input_str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(solution.length_longest_path(input_str))  # Expected: 32


if __name__ == "__main__":
    main()
