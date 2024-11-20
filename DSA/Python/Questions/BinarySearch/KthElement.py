"""
# Question: Kth Element of Two Sorted Arrays
# Find kth element in two sorted arrays

# Time Complexity: O(log(min(m,n)))
# Space Complexity: O(1)

# Algorithm:
# 1. Binary search on smaller array
# 2. Calculate partition points
# 3. Find kth element
"""


class KthElement:
    def find_kth_element(self, arr1: list[int], arr2: list[int], k: int) -> int:
        if len(arr1) > len(arr2):
            return self.find_kth_element(arr2, arr1, k)

        n1, n2 = len(arr1), len(arr2)
        left, right = max(0, k - n2), min(k, n1)

        while left <= right:
            cut1 = (left + right) >> 1
            cut2 = k - cut1

            left1 = float("-inf") if cut1 == 0 else arr1[cut1 - 1]
            left2 = float("-inf") if cut2 == 0 else arr2[cut2 - 1]
            right1 = float("inf") if cut1 == n1 else arr1[cut1]
            right2 = float("inf") if cut2 == n2 else arr2[cut2]

            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)
            elif left1 > right2:
                right = cut1 - 1
            else:
                left = cut1 + 1

        return -1


def main():
    solution = KthElement()
    arr1 = [2, 3, 6, 7, 9]
    arr2 = [1, 4, 8, 10]
    k = 5
    print(solution.find_kth_element(arr1, arr2, k))  # Expected: 6


if __name__ == "__main__":
    main()
