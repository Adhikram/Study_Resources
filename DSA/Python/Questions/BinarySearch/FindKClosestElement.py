"""
# Question: Find K Closest Elements
# Link: https://leetcode.com/problems/find-k-closest-elements/

# Time Complexity: O(log(n-k))
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search for starting position
# 2. Compare window differences
# 3. Return k closest elements
"""


class FindKClosestElement:
    def find_closest_elements(self, arr: list[int], k: int, x: int) -> list[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) >> 1

            # Compare distances from x
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]


def main():
    solution = FindKClosestElement()
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    print(solution.find_closest_elements(arr, k, x))  # Expected: [1,2,3,4]


if __name__ == "__main__":
    main()
