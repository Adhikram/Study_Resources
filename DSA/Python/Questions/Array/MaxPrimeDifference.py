"""
# Question: Maximum Prime Difference
# Find maximum distance between two prime numbers in array

# Time Complexity: O(n) for array traversal, O(sqrt(n)) for prime sieve
# Space Complexity: O(n) for prime sieve array

# Algorithm:
# 1. Generate prime sieve up to maximum possible value
# 2. Use two pointers to find max distance between primes
# 3. Move pointers based on prime status of elements

# Key Components:
# - get_prime_hash(): Implements Sieve of Eratosthenes
# - maximum_prime_difference(): Two pointer approach
"""

from typing import List


class MaxPrimeDifference:
    def get_prime_hash(self, n: int) -> List[int]:
        prime = [1] * (n + 1)
        prime[0] = prime[1] = 0

        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i * i, n + 1, i):
                    prime[j] = 0

        return prime

    def maximum_prime_difference(self, nums: List[int]) -> int:
        result = 0
        start = 0
        end = len(nums) - 1
        prime = self.get_prime_hash(100)

        while start < end:
            if prime[nums[start]] and prime[nums[start]] == prime[nums[end]]:
                result = max(result, end - start)
                break
            elif prime[nums[start]]:
                end -= 1
            else:
                start += 1

        return max(result, end - start)


def main():
    solution = MaxPrimeDifference()
    nums = [3, 4, 5, 7, 11, 13]
    result = solution.maximum_prime_difference(nums)
    print(result)


if __name__ == "__main__":
    main()
