"""
# Question: Maximum Product Subarray
# Link: https://leetcode.com/problems/maximum-product-subarray/

# Problem Statement:
# Given an array that contains both negative and positive integers,
# find the maximum product subarray.

# Example:
# Input: arr = [6, -3, -10, 0, 2]
# Output: 180
# Explanation: Subarray [6, -3, -10] gives maximum product
"""

from typing import List


def max_product_subarray(arr: List[int]) -> int:
    """
    Find maximum product subarray using optimized approach

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Initialize variables with first element
    max_prod = min_prod = result = arr[0]

    # Process rest of the array
    for i in range(1, len(arr)):
        # Store current max_prod for min calculation
        temp = max(
            arr[i],  # Current number alone
            max_prod * arr[i],  # Product with previous max
            min_prod * arr[i],  # Product with previous min
        )

        # Update min_prod for next iteration
        min_prod = min(
            arr[i],  # Current number alone
            max_prod * arr[i],  # Product with previous max
            min_prod * arr[i],  # Product with previous min
        )

        # Update max_prod
        max_prod = temp

        # Update global maximum
        result = max(result, max_prod)

    return result


def main():
    # Test cases
    test_cases = [
        [6, -3, -10, 0, 2],  # Mixed positive/negative with zero
        [2, 3, -2, 4],  # Simple case
        [-2, 0, -1],  # Negative numbers with zero
        [1, -2, -3, 0, 7, -8, -2],  # Complex case
        [1, 2, 3, 4],  # All positive
        [-1, -2, -3, -4],  # All negative
    ]

    for i, arr in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {arr}")
        print(f"Maximum Product: {max_product_subarray(arr)}")


if __name__ == "__main__":
    main()
