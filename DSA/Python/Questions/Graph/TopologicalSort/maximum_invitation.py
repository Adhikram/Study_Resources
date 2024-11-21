"""
# Question: Maximum Employees to Be Invited to a Meeting
# Link: https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

# Problem Statement:
# Given a list of n employees where favorite[i] denotes the favorite person of ith employee.
# Find the maximum number of employees that can be invited to a circular table meeting where
# each employee must sit next to their favorite person.

# Example:
# Input: favorite = [2,2,1,2]
# Output: 3
# Explanation: Employees 0, 1, and 2 can be invited to form a valid seating arrangement.
"""

from typing import List
from collections import deque

# Main Solution
"""
Algorithm:
1. Calculate in-degrees for each node
2. Process nodes with zero in-degree first
3. Track longest chains and cycle sizes
4. Handle two-length cycles specially
5. Return maximum of cycle size or sum of chains

Time Complexity: O(N)
Space Complexity: O(N)
"""


def maximum_invitations(favorite: List[int]) -> int:
    n = len(favorite)
    in_degree = [0] * n

    # Calculate in-degrees
    for f in favorite:
        in_degree[f] += 1

    # Initialize data structures
    queue = deque()
    longest_chain = [0] * n
    visited = [False] * n

    # Add nodes with zero in-degree
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    # Process nodes in topological order
    while queue:
        node = queue.popleft()
        visited[node] = True
        fav = favorite[node]

        # Update longest chain
        longest_chain[fav] = max(longest_chain[fav], longest_chain[node] + 1)

        in_degree[fav] -= 1
        if in_degree[fav] == 0:
            queue.append(fav)

    # Handle cycles
    max_cycle_size = 0
    sum_of_chains = 0

    for i in range(n):
        if not visited[i]:
            cycle_length = 0
            chain_length1 = chain_length2 = 0
            node = i

            # Find cycle
            while not visited[node]:
                visited[node] = True
                cycle_length += 1
                node = favorite[node]

            # Handle two-length cycles
            if cycle_length == 2:
                chain_length1 = longest_chain[i]
                chain_length2 = longest_chain[favorite[i]]
                sum_of_chains += chain_length1 + chain_length2 + cycle_length
            else:
                max_cycle_size = max(max_cycle_size, cycle_length)

    return max(max_cycle_size, sum_of_chains)


def main():
    test_cases = [[2, 2, 1, 2], [1, 2, 0], [3, 0, 1, 4, 1], [1, 2, 3, 4, 5, 0]]

    for i, favorite in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Favorite array: {favorite}")
        print(f"Maximum employees that can be invited: {maximum_invitations(favorite)}")


if __name__ == "__main__":
    main()
