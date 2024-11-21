"""
# Question: Sort Integers by The Power Value
# Link: https://leetcode.com/problems/sort-integers-by-the-power-value/

# Problem Statement:
# The power of an integer x is defined as the number of steps needed to transform x into 1 using:
# - If x is even, x = x / 2
# - If x is odd, x = 3 * x + 1
# Return the kth integer in the range [low, high] sorted by the power value.

# Example:
# Input: low = 12, high = 15, k = 2
# Output: 13
# Explanation: Powers are: 12->9->28->14->7->22->11->34->17->52->26->13->40->20->10->5->16->8->4->2->1 (9 steps)
"""

from typing import List

# Global DP array for memoization
dp = [0] * 1000000

# Power Calculation with Memoization
"""
Algorithm:
1. Base cases: return 0 for x = 1 or x = 0
2. If result cached in dp, return it
3. Calculate next step based on even/odd
4. Store and return result

Time Complexity: O(logN) per calculation
Space Complexity: O(N) for dp array
"""


def power(x: int) -> int:
    if x == 1 or x == 0:
        return 0

    if dp[x] != 0:
        return dp[x]

    if x % 2 == 0:
        dp[x] = 1 + power(x // 2)
    else:
        dp[x] = 1 + power(3 * x + 1)

    return dp[x]


# Main Function
"""
Algorithm:
1. Create array of [number, power] pairs
2. Calculate power for each number in range
3. Sort array by power values
4. Return kth number

Time Complexity: O(NlogN) where N = high-low+1
Space Complexity: O(N)
"""


def get_kth(low: int, high: int, k: int) -> int:
    # Create array of [number, power] pairs
    ans = []
    for num in range(low, high + 1):
        ans.append([num, power(num)])

    # Sort by power value
    ans.sort(key=lambda x: x[1])

    # Return kth number
    return ans[k - 1][0]


def main():
    # Test cases
    test_cases = [
        {"low": 12, "high": 15, "k": 2},  # Regular case
        {"low": 1, "high": 1, "k": 1},  # Single number
        {"low": 7, "high": 11, "k": 4},  # Multiple numbers
        {"low": 10, "high": 20, "k": 5},  # Larger range
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Low: {test['low']}, High: {test['high']}, k: {test['k']}")
        print(f"Result: {get_kth(test['low'], test['high'], test['k'])}")


if __name__ == "__main__":
    main()
