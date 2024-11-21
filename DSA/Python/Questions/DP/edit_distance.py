"""
# Question: Edit Distance
# Link: https://leetcode.com/problems/edit-distance/

# Problem Statement:
# Given two strings str1 and str2, return the minimum number of operations
# required to convert str1 to str2. The allowed operations are:
# 1. Insert a character
# 2. Delete a character
# 3. Replace a character

# Example:
# Input: str1 = "horse", str2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Key Insights:
# - Each position can have three possible operations
# - Need to track minimum operations at each step
# - Characters matching means no operation needed
"""

# 1. Recursive Solution with Memoization
"""
Algorithm:
1. Compare characters from end of both strings
2. If characters match, no operation needed
3. If different, try all three operations:
   - Replace current character
   - Delete character from str1
   - Insert character from str2
4. Use memoization to store results

Time Complexity: O(n*m)
Space Complexity: O(n*m) + O(n+m) recursion stack
"""


def edit_distance_recursive(str1: str, str2: str) -> int:
    n, m = len(str1), len(str2)
    # Initialize dp array for memoization
    dp = [[-1] * m for _ in range(n)]

    def solve(i: int, j: int) -> int:
        # Base cases: if either string is exhausted
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        # Return memoized result if available
        if dp[i][j] != -1:
            return dp[i][j]

        # If characters match, no operation needed
        if str1[i] == str2[j]:
            dp[i][j] = solve(i - 1, j - 1)
            return dp[i][j]

        # Try all three operations and take minimum
        replace = solve(i - 1, j - 1)
        delete = solve(i - 1, j)
        insert = solve(i, j - 1)

        # Store minimum operations needed
        dp[i][j] = 1 + min(replace, delete, insert)
        return dp[i][j]

    return solve(n - 1, m - 1)


# 2. Tabulation Solution
"""
Algorithm:
1. Create 2D dp array of size (n+1)*(m+1)
2. Initialize base cases for empty strings
3. Fill dp table using bottom-up approach
4. For each position, calculate minimum operations

Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""


def edit_distance_tabulation(str1: str, str2: str) -> int:
    n, m = len(str1), len(str2)
    # Create dp array with base cases
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize first row and column
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If characters match
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Take minimum of three operations
                dp[i][j] = 1 + min(
                    dp[i - 1][j - 1],  # replace
                    dp[i - 1][j],  # delete
                    dp[i][j - 1],  # insert
                )

    return dp[n][m]


# 3. Space Optimized Solution
"""
Algorithm:
1. Use two arrays instead of 2D array
2. Previous row and current row sufficient
3. Update arrays in alternating fashion

Time Complexity: O(n*m)
Space Complexity: O(m)
"""


def edit_distance_optimized(str1: str, str2: str) -> int:
    n, m = len(str1), len(str2)
    # Initialize previous row
    prev = [j for j in range(m + 1)]

    # Process each character of str1
    for i in range(1, n + 1):
        # Current row array
        curr = [0] * (m + 1)
        curr[0] = i  # Base case

        # Fill current row
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    prev[j - 1], prev[j], curr[j - 1]  # replace  # delete  # insert
                )

        # Update previous row
        prev = curr[:]

    return prev[m]


def main():
    # Test cases
    test_cases = [
        ("horse", "ros"),  # Regular case
        ("intention", "execution"),  # Multiple operations
        ("", "abc"),  # Empty string
        ("abc", ""),  # Empty target
        ("sunday", "saturday"),  # Complex transformations
    ]

    for i, (str1, str2) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: str1 = '{str1}', str2 = '{str2}'")
        print(f"Recursive Solution: {edit_distance_recursive(str1, str2)}")
        print(f"Tabulation Solution: {edit_distance_tabulation(str1, str2)}")
        print(f"Optimized Solution: {edit_distance_optimized(str1, str2)}")


if __name__ == "__main__":
    main()
