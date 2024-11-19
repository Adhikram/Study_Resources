"""
# Question: Beautiful Pairs
# Link: https://leetcode.com/problems/beautiful-pairs/

# Given two arrays nums1 and nums2 of equal length n, find the pair of indices (i,j)
# such that the Manhattan distance between the elements at those indices is minimized.
# The Manhattan distance between two points (x1,y1) and (x2,y2) is |x1-x2| + |y1-y2|.

# Time Complexity: O(n log n) where n is the length of input arrays
# Space Complexity: O(n) for storing points list

# Algorithm:
# 1. Convert array elements into points with coordinates (nums1[i], nums2[i])
# 2. Use divide and conquer approach to find minimum Manhattan distance:
#    - Divide points into left and right halves
#    - Recursively find minimum distances in both halves
#    - Combine results by checking points near the dividing line
# 3. For points near dividing line:
#    - Sort by y-coordinate
#    - Compare each point with nearby points
#    - Update minimum distance if smaller distance found

# Key Components:
# - dist(): Calculates Manhattan distance between two points
# - dfs(): Implements divide and conquer strategy
# - beautiful_pair(): Main function that processes input arrays

# Data Structures:
# - self.points: List of tuples storing (x, y, index) for each point
# - Return format: [distance, index1, index2] where indices form the beautiful pair
"""

# Import List type from typing module
from typing import List


# Define BeautifulPairs class
class BeautifulPairs:
    # Initialize class with empty points list
    def __init__(self):
        # List to store points
        self.points = []

    # Calculate Manhattan distance between two points
    def dist(self, x1: int, y1: int, x2: int, y2: int) -> int:
        # Return absolute difference of x coordinates plus absolute difference of y coordinates
        return abs(x1 - x2) + abs(y1 - y2)

    # Recursive divide and conquer function
    def dfs(self, l: int, r: int) -> List[int]:
        # Base case: if left >= right, return max value and invalid indices
        if l >= r:
            return [1 << 30, -1, -1]

        # Calculate middle point
        m = (l + r) >> 1
        # Get x coordinate of middle point
        x = self.points[m][0]

        # Recursively process left half
        t1 = self.dfs(l, m)
        # Recursively process right half
        t2 = self.dfs(m + 1, r)

        # Compare results from both halves and take the better one
        if t1[0] > t2[0] or (
            t1[0] == t2[0] and (t1[1] > t2[1] or (t1[1] == t2[1] and t1[2] > t2[2]))
        ):
            t1 = t2

        # Create list for points near dividing line
        t = []
        # Collect points that are within current minimum distance of dividing line
        for i in range(l, r + 1):
            if abs(self.points[i][0] - x) <= t1[0]:
                t.append(self.points[i])

        # Sort points by y coordinate
        t.sort(key=lambda x: x[1])

        # Compare each point with nearby points
        for i in range(len(t)):
            for j in range(i + 1, len(t)):
                # Break if y distance exceeds current minimum
                if t[j][1] - t[i][1] > t1[0]:
                    break
                # Get indices in sorted order
                pi = min(t[i][2], t[j][2])
                pj = max(t[i][2], t[j][2])
                # Calculate distance between points
                d = self.dist(t[i][0], t[i][1], t[j][0], t[j][1])
                # Update result if better distance found
                if d < t1[0] or (
                    d == t1[0] and (pi < t1[1] or (pi == t1[1] and pj < t1[2]))
                ):
                    t1 = [d, pi, pj]
        # Return best result
        return t1

    # Main function to find beautiful pair
    def beautiful_pair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Get length of input arrays
        n = len(nums1)
        # Reset points list
        self.points = []
        # Create points from input arrays
        for i in range(n):
            self.points.append([nums1[i], nums2[i], i])
        # Sort points by x coordinate
        self.points.sort()
        # Get result from divide and conquer
        result = self.dfs(0, n - 1)
        # Return indices of beautiful pair
        return [result[1], result[2]]


# Main function for testing
def main():
    # Create instance of BeautifulPairs
    beautiful_pairs = BeautifulPairs()
    # Test input arrays
    nums1 = [1, 2, 3, 2, 4]
    nums2 = [2, 3, 1, 2, 3]
    # Get result
    result = beautiful_pairs.beautiful_pair(nums1, nums2)
    # Print result
    print(f"{result[0]} {result[1]}")


# Execute main function if script is run directly
if __name__ == "__main__":
    main()
