"""
Core hash map / hash set patterns for coding interviews — runnable & self-testing.

Every pattern below is a real, callable function (not a stub) with its time and
space complexity, the edge cases it handles, and inline `assert` tests. Run
`python3 hashmap_tricks.py`; a clean exit means all patterns passed their tests.

The unifying idea: a hashmap trades O(n) SPACE for turning an O(n) scan
("have I seen X?", "how many X?", "what maps to X?") into an O(1) lookup. Most
of these patterns collapse a brute-force O(n^2) double loop into one O(n) pass.

Patterns:
    1.  Two sum               — complement map, one pass
    2.  Frequency count       — Counter / dict of counts
    3.  Group anagrams        — sorted-string OR char-tuple key
    4.  Seen-set dedup        — first duplicate / contains duplicate
    5.  Subarray sum == k     — running prefix sum + count map
    6.  Longest unique window — sliding window + last-seen index map
    7.  First unique char     — count then re-scan for the first count==1
    8.  Intersection of arrays— set intersection
    9.  LRU cache             — dict (ordered) with O(1) get/put
    10. Composite keys        — frozenset / tuple as a dict key
"""

from collections import Counter, OrderedDict, defaultdict
from typing import Dict, List, Optional


# ===========================================================================
# 1. TWO SUM — complement map (the canonical hashmap trick)
# ===========================================================================
def two_sum(nums: List[int], target: int) -> List[int]:
    """Indices of the pair summing to target (assume exactly one), else [].
    Time O(n), Space O(n). One pass: for each x, ask "have I already seen
    target - x?" — an O(1) lookup instead of an O(n) inner scan.
    Edge cases: empty/single -> no pair -> []; duplicates fine (we store indices)."""
    seen: Dict[int, int] = {}            # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i                      # store AFTER the check (no self-pairing)
    return []


# ===========================================================================
# 2. FREQUENCY COUNT — the workhorse of hashmap problems
# ===========================================================================
def frequency(items: List[str]) -> Dict[str, int]:
    """Count occurrences of each item. Time O(n), Space O(k) distinct keys.
    Edge case: empty -> {}. Counter is the idiomatic one-liner."""
    return dict(Counter(items))


# ===========================================================================
# 3. GROUP ANAGRAMS — canonical key maps anagrams to the same bucket
# ===========================================================================
def group_anagrams(words: List[str]) -> List[List[str]]:
    """Group words that are anagrams of each other. Time O(n * k log k) using a
    SORTED-string key (k = word length), Space O(n*k).
    The trick: anagrams share a canonical form (sorted letters), so that form is
    the bucket key. A char-count tuple key gives O(n*k) and avoids the sort.
    Edge case: empty -> []. Insertion order of first appearance is preserved."""
    buckets: Dict[str, List[str]] = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))         # canonical anagram signature
        buckets[key].append(w)
    return list(buckets.values())


def group_anagrams_tuple_key(words: List[str]) -> List[List[str]]:
    """Same result, but key on a 26-count tuple -> O(n*k) total (no per-word sort).
    Demonstrates a TUPLE as a composite, hashable dict key."""
    buckets: Dict[tuple, List[str]] = defaultdict(list)
    for w in words:
        counts = [0] * 26
        for ch in w:
            counts[ord(ch) - ord("a")] += 1
        buckets[tuple(counts)].append(w)   # list isn't hashable; tuple is
    return list(buckets.values())


# ===========================================================================
# 4. SEEN-SET DEDUP — membership in a set is O(1)
# ===========================================================================
def has_duplicate(nums: List[int]) -> bool:
    """True if any value appears more than once. Time O(n), Space O(n).
    Short-circuits on the first repeat. Edge case: empty/single -> False."""
    seen = set()
    for x in nums:
        if x in seen:                    # O(1) membership
            return True
        seen.add(x)
    return False


def first_duplicate(nums: List[int]) -> Optional[int]:
    """Return the first value that repeats (by 2nd occurrence), else None.
    Time O(n), Space O(n)."""
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
    return None


# ===========================================================================
# 5. SUBARRAY SUM EQUALS K — prefix sum + count map (handles negatives)
# ===========================================================================
def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """Count contiguous subarrays summing to k. Works with negatives & zeros.
    Time O(n), Space O(n). A subarray (i, j] sums to k iff
    prefix[j] - prefix[i] = k, i.e. prefix[i] = running - k. So as we sweep,
    we ask the map how many earlier prefixes equal `running - k` — O(1).
    Edge case: seed {0: 1} so a prefix that itself equals k is counted."""
    count = 0
    running = 0
    seen: Dict[int, int] = {0: 1}        # one empty prefix has sum 0
    for x in nums:
        running += x
        count += seen.get(running - k, 0)
        seen[running] = seen.get(running, 0) + 1
    return count


# ===========================================================================
# 6. LONGEST SUBSTRING WITHOUT REPEATING CHARS — window + last-seen map
# ===========================================================================
def longest_unique_substring(s: str) -> int:
    """Length of the longest substring with all-distinct chars.
    Time O(n), Space O(min(n, charset)). Map char -> last index; when we hit a
    repeat that's inside the window, jump `start` past it. Edge case: '' -> 0."""
    last: Dict[str, int] = {}            # char -> most recent index
    start = 0
    best = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1         # shrink window past the duplicate
        last[ch] = i
        best = max(best, i - start + 1)
    return best


# ===========================================================================
# 7. FIRST UNIQUE CHARACTER — count, then re-scan in order
# ===========================================================================
def first_unique_char(s: str) -> int:
    """Index of the first non-repeating character, else -1. Time O(n), Space O(k).
    Two passes: count all, then return the first whose count is 1 (insertion
    order makes the re-scan trivial). Edge case: '' or all-repeat -> -1."""
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1


# ===========================================================================
# 8. INTERSECTION OF TWO ARRAYS — set intersection
# ===========================================================================
def intersection(a: List[int], b: List[int]) -> List[int]:
    """Distinct values present in BOTH arrays. Time O(n+m), Space O(n+m).
    Sets dedup and give O(1) membership, so the intersection is one operation.
    Edge case: either empty -> []. (Order not guaranteed; sort if needed.)"""
    return list(set(a) & set(b))


# ===========================================================================
# 9. LRU CACHE — O(1) get & put using an ordered dict
# ===========================================================================
class LRUCache:
    """Least-Recently-Used cache with O(1) get and put.
    A dict preserves insertion order; OrderedDict.move_to_end / popitem make
    "touch this key" and "evict the oldest" both O(1). On capacity overflow we
    evict the least-recently-used (front) entry.
    Edge cases: capacity 0 stores nothing; get on a miss returns -1; updating an
    existing key refreshes its recency without growing size."""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.store: "OrderedDict[int, int]" = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.store.move_to_end(key)          # mark most-recently-used, O(1)
        return self.store[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.store:
            self.store.move_to_end(key)      # refresh recency
        self.store[key] = value
        if len(self.store) > self.capacity:
            self.store.popitem(last=False)   # evict least-recently-used (front)


# ===========================================================================
# 10. COMPOSITE KEYS — frozenset / tuple as a dict key
# ===========================================================================
def count_unordered_pairs(pairs: List[List[int]]) -> Dict[frozenset, int]:
    """Count pairs treating (a, b) and (b, a) as the SAME pair.
    A frozenset is hashable and order-insensitive -> ideal composite key.
    Time O(n), Space O(n). Edge case: empty -> {}."""
    counts: Dict[frozenset, int] = defaultdict(int)
    for a, b in pairs:
        counts[frozenset((a, b))] += 1
    return dict(counts)


def grid_visited(moves: List[tuple]) -> int:
    """Count DISTINCT cells visited, using a (row, col) TUPLE key in a set.
    Demonstrates an ordered composite key (position matters). Time O(n)."""
    seen = set()
    for cell in moves:
        seen.add(cell)                       # tuple is hashable
    return len(seen)


# ===========================================================================
# TESTS — run via main(); cover normal + edge cases
# ===========================================================================
def _test() -> None:
    # 1. two sum
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 3], 6) == [0, 1]              # duplicates
    assert two_sum([], 5) == [] and two_sum([5], 5) == []

    # 2. frequency
    assert frequency(["a", "b", "a", "c", "a"]) == {"a": 3, "b": 1, "c": 1}
    assert frequency([]) == {}

    # 3. group anagrams (both implementations agree on grouping)
    def normalize(groups):
        return sorted(sorted(g) for g in groups)
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert normalize(group_anagrams(words)) == expected
    assert normalize(group_anagrams_tuple_key(words)) == expected
    assert group_anagrams([]) == []

    # 4. dedup / first duplicate
    assert has_duplicate([1, 2, 3, 1]) is True
    assert has_duplicate([1, 2, 3]) is False
    assert has_duplicate([]) is False
    assert first_duplicate([5, 1, 5, 2]) == 5
    assert first_duplicate([1, 2, 3]) is None

    # 5. subarray sum == k (incl. negatives & zeros)
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2
    assert subarray_sum_equals_k([1, -1, 0], 0) == 3
    assert subarray_sum_equals_k([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4

    # 6. longest unique substring
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("bbbb") == 1
    assert longest_unique_substring("pwwkew") == 3

    # 7. first unique char
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert first_unique_char("") == -1

    # 8. intersection
    assert sorted(intersection([1, 2, 2, 1], [2, 2])) == [2]
    assert sorted(intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
    assert intersection([], [1, 2]) == []

    # 9. LRU cache (the classic LeetCode trace)
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1                           # 1 now most-recent
    lru.put(3, 3)                                    # evicts key 2 (LRU)
    assert lru.get(2) == -1                          # 2 gone
    lru.put(4, 4)                                    # evicts key 1
    assert lru.get(1) == -1
    assert lru.get(3) == 3 and lru.get(4) == 4
    zero = LRUCache(0)                               # capacity 0 stores nothing
    zero.put(1, 1)
    assert zero.get(1) == -1

    # 10. composite keys
    assert count_unordered_pairs([[1, 2], [2, 1], [3, 4]]) == {
        frozenset((1, 2)): 2,
        frozenset((3, 4)): 1,
    }
    assert grid_visited([(0, 0), (0, 1), (0, 0)]) == 2


def main() -> None:
    _test()
    print("hashmap_tricks.py: all 10 patterns verified ✔")


if __name__ == "__main__":
    main()
