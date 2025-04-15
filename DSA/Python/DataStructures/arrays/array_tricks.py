"""
Common Array Tricks and Patterns for Coding Interviews

This file contains popular array manipulation techniques and patterns
that frequently appear in coding interviews.
"""

def two_pointer_technique():
    """
    Two Pointer Technique Examples:
    1. Finding pair with sum in sorted array
    2. Container with most water
    3. Three sum problem
    """
    # Example: Find pair with sum in sorted array
    def find_pair_with_sum(arr, target):
        left, right = 0, len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []

def sliding_window():
    """
    Sliding Window Technique Examples:
    1. Maximum sum subarray of size k
    2. Longest substring without repeating characters
    3. Minimum window substring
    """
    # Example: Maximum sum subarray of size k
    def max_sum_subarray(arr, k):
        if not arr or k > len(arr):
            return 0
        
        window_sum = sum(arr[:k])
        max_sum = window_sum
        
        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i-k] + arr[i]
            max_sum = max(max_sum, window_sum)
        
        return max_sum

def kadanes_algorithm():
    """
    Kadane's Algorithm for Maximum Subarray Sum
    Time Complexity: O(n)
    """
    def max_subarray_sum(arr):
        max_ending_here = max_so_far = arr[0]
        for num in arr[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

def dutch_national_flag():
    """
    Dutch National Flag Algorithm (Three-way partitioning)
    Used for sorting arrays with 3 distinct values (e.g., Sort Colors)
    """
    def sort_colors(arr):
        low = mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:  # arr[mid] == 2
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

def prefix_sum():
    """
    Prefix Sum Technique for Range Queries
    Useful for:
    1. Range sum queries
    2. Equilibrium index
    3. Maximum subarray sum
    """
    def build_prefix_sum(arr):
        prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] + arr[i]
        return prefix
    
    def range_sum(prefix, left, right):
        return prefix[right + 1] - prefix[left]

def array_rotation():
    """
    Array Rotation Techniques
    1. Using temporary array
    2. Juggling algorithm
    3. Reversal algorithm
    """
    def rotate_array(arr, k):
        n = len(arr)
        k = k % n
        
        # Reverse entire array
        arr.reverse()
        # Reverse first k elements
        arr[:k] = reversed(arr[:k])
        # Reverse remaining elements
        arr[k:] = reversed(arr[k:])

def binary_search_variations():
    """
    Binary Search Variations:
    1. First and last occurrence
    2. Search in rotated sorted array
    3. Peak element
    """
    def first_occurrence(arr, target):
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                right = mid - 1  # Continue searching left
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result

def cyclic_sort():
    """
    Cyclic Sort Pattern
    Useful for arrays containing numbers in range 1 to n
    """
    def cyclic_sort(arr):
        i = 0
        while i < len(arr):
            correct_pos = arr[i] - 1
            if arr[i] != arr[correct_pos]:
                arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
            else:
                i += 1

def matrix_tricks():
    """
    2D Array/Matrix Tricks:
    1. Spiral traversal
    2. Search in sorted matrix
    3. Rotate matrix
    """
    def search_sorted_matrix(matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False

# Interview Tips:
"""
1. Always clarify:
   - Array size constraints
   - Answer
   - Value range constraints
   - Are duplicates allowed?
   - Is the array sorted?
   - Memory constraints
   - Can we modify the input array?

2. Common Edge Cases:
   - Empty array
   - Array with one element
   - Array with duplicate elements
   - Array with negative numbers
   - Sorted vs unsorted array
   - Array size exactly equals k
   - All elements are same

3. Optimization Techniques:
   - Use hash tables for O(1) lookup
   - Sort array if order doesn't matter
   - Use two pointers for range/interval problems
   - Use sliding window for subarray problems
   - Use binary search on sorted arrays
   - Use prefix sum for range queries
""" 