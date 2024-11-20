"""
# Question: Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/

# Time Complexity: O(n * k * log k)
# Space Complexity: O(n * k)

# Algorithm:
# 1. Sort each word's characters
# 2. Use sorted word as key in hashmap
# 3. Group anagrams together
# 4. Return list of grouped anagrams

# Key Components:
# - group_anagrams(): Main implementation
# - merge_sort(): Custom sorting implementation
# - Hashmap for grouping
"""

from collections import defaultdict


class GroupAnagrams:
    def merge_sort(self, arr: list, l: int, r: int) -> None:
        if l < r:
            m = l + (r - l) // 2
            self.merge_sort(arr, l, m)
            self.merge_sort(arr, m + 1, r)
            self.merge(arr, l, m, r)

    def merge(self, arr: list, l: int, m: int, r: int) -> None:
        n1, n2 = m - l + 1, r - m
        L = arr[l : l + n1]
        R = arr[m + 1 : m + 1 + n2]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            chars = list(word)
            self.merge_sort(chars, 0, len(chars) - 1)
            sorted_word = "".join(chars)
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())


def main():
    solution = GroupAnagrams()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.group_anagrams(strs))


if __name__ == "__main__":
    main()
