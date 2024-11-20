"""
# Question: Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Use hashmap to track numbers
# 2. Find sequence start points
# 3. Count sequence lengths
# 4. Return maximum sequence length

# Key Components:
# - longest_consecutive(): Main implementation
# - longest_consecutive_optimized(): Optimized version
# - traverse(): Helper for sequence counting
"""


class LongestSubsequentSequence:
    def traverse(self, hash_map: dict, num: int, op: int) -> int:
        count = 0
        while hash_map.get(num, False):
            hash_map[num] = False
            num = num + op
            count += 1
        return count

    def longest_consecutive(self, nums: list[int]) -> int:
        hash_map = {num: True for num in nums}
        result = 0

        for num in nums:
            cur_result = self.traverse(hash_map, num + 1, 1) + self.traverse(
                hash_map, num, -1
            )
            result = max(result, cur_result)

        return result

    def longest_consecutive_optimized(self, nums: list[int]) -> int:
        hash_map = {num: True for num in nums}
        result = 0

        for num in nums:
            if not hash_map.get(num - 1, False):
                cur_result = self.traverse(hash_map, num + 1, 1)
                result = max(result, cur_result + 1)

        return result


def main():
    solution = LongestSubsequentSequence()
    nums = [100, 4, 200, 1, 3, 2]
    print(solution.longest_consecutive(nums))
    print(solution.longest_consecutive_optimized(nums))


if __name__ == "__main__":
    main()
