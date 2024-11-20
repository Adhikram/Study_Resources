"""
# Question: Maximum Number of Achievable Transfer Requests
# Link: https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

# Find maximum number of achievable transfer requests

# Time Complexity: O(2^m) where m is number of requests
# Space Complexity: O(n) where n is number of buildings

# Algorithm:
# 1. Use backtracking to try all request combinations
# 2. Track building transfer balance using indegree array
# 3. Check if current combination is valid
# 4. Return maximum achievable requests

# Key Components:
# - maximum_requests(): Main implementation
# - helper(): Backtracking function for request combinations
# - Balance tracking with indegree array
"""


class MaximumNumberOfTransferRequests:
    def maximum_requests(self, n: int, requests: list[list[int]]) -> int:
        indegree = [0] * n

        def helper(
            start: int,
            requests: list[list[int]],
            indegree: list[int],
            n: int,
            count: int,
        ) -> int:
            # Base case: check if all buildings have zero net transfer
            if start == len(requests):
                return count if all(deg == 0 for deg in indegree) else 0

            # Take current request
            indegree[requests[start][0]] -= 1
            indegree[requests[start][1]] += 1
            take = helper(start + 1, requests, indegree, n, count + 1)

            # Backtrack
            indegree[requests[start][0]] += 1
            indegree[requests[start][1]] -= 1

            # Don't take current request
            not_take = helper(start + 1, requests, indegree, n, count)

            return max(take, not_take)

        return helper(0, requests, indegree, n, 0)


def main():
    solution = MaximumNumberOfTransferRequests()
    requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
    print(solution.maximum_requests(5, requests))  # Expected output: 5


if __name__ == "__main__":
    main()
