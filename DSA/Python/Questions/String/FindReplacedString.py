"""
# Question: Find and Replace in String
# Link: https://leetcode.com/problems/find-and-replace-in-string/

# Time Complexity: O(n * m)
# Space Complexity: O(n)

# Algorithm:
# 1. Sort replacements by index
# 2. Process replacements from right to left
# 3. Validate and apply replacements
# 4. Return modified string

# Key Components:
# - find_replace_string(): Main implementation
# - Replacement validation
# - String manipulation
"""


class FindReplacedString:
    def find_replace_string(
        self, s: str, indices: list[int], sources: list[str], targets: list[str]
    ) -> str:
        # Create list of valid replacements
        replacements = []
        for i in range(len(indices)):
            if s.startswith(sources[i], indices[i]):
                replacements.append([indices[i], i])

        # Sort replacements by index in descending order
        replacements.sort(reverse=True)

        # Convert string to list for easier manipulation
        s_list = list(s)

        # Apply replacements
        for index, i in replacements:
            s_list[index : index + len(sources[i])] = targets[i]

        return "".join(s_list)


def main():
    solution = FindReplacedString()
    s = "abcd"
    indices = [0, 2]
    sources = ["a", "cd"]
    targets = ["eee", "ffff"]
    print(solution.find_replace_string(s, indices, sources, targets))


if __name__ == "__main__":
    main()
