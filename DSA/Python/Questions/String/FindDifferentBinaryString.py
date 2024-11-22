"""
# Question: Find Different Binary String
# Link: https://leetcode.com/problems/find-unique-binary-string/

# Find a binary string that's different from all given strings

# Time Complexity: O(n)
# Space Complexity: O(1)

# Algorithm:
# 1. Use Cantor's diagonalization
# 2. Flip each bit at corresponding position
# 3. Build result string
# 4. Return unique binary string

# Key Components:
# - find_different_binary_string(): Main implementation
# - Bit flipping logic
# - String construction
"""


class FindDifferentBinaryString:
    def find_different_binary_string(self, nums: list[str]) -> str:
        result = []
        for i in range(len(nums)):
            # Flip the bit at diagonal position
            result.append("1" if nums[i][i] == "0" else "0")

        return "".join(result)


def main():
    solution = FindDifferentBinaryString()
    nums = ["01", "10"]
    print(solution.find_different_binary_string(nums))  # Expected: "11"

    nums = ["00", "01"]
    print(solution.find_different_binary_string(nums))  # Expected: "11"


if __name__ == "__main__":
    main()
