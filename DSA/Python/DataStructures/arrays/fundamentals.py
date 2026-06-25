"""
Array / list fundamentals for interviews — Python `list`.

Covers every operation you are likely to use, its time complexity, and the
gotchas that cause real interview bugs. Each section is runnable and verified
with `assert`s. Run `python3 fundamentals.py` — if it exits cleanly, every
example behaved as documented.

A Python `list` is a DYNAMIC ARRAY: a contiguous block of object pointers that
over-allocates so that `append` is amortized O(1). It is mutable and passed by
reference.
"""

from typing import List


# ---------------------------------------------------------------------------
# 1. Creation & initialization
# ---------------------------------------------------------------------------
def creation() -> None:
    empty = []                       # O(1)
    zeros = [0] * 5                  # O(n) -> [0, 0, 0, 0, 0]
    nums = [1, 2, 3]                 # literal
    squares = [x * x for x in range(5)]   # comprehension -> [0,1,4,9,16]

    # 2D grid: ALWAYS use a comprehension, never [[0]*n]*m  (see gotchas!)
    grid = [[0] * 3 for _ in range(2)]    # 2 rows, 3 cols

    assert zeros == [0, 0, 0, 0, 0]
    assert squares == [0, 1, 4, 9, 16]
    assert grid == [[0, 0, 0], [0, 0, 0]]
    assert len(empty) == 0 and len(nums) == 3


# ---------------------------------------------------------------------------
# 2. Access & update  — all O(1)
# ---------------------------------------------------------------------------
def access() -> None:
    a = [10, 20, 30, 40, 50]
    assert a[0] == 10          # first
    assert a[-1] == 50         # last (negative indexing)
    assert a[-2] == 40         # second to last
    a[1] = 99                  # update in place, O(1)
    assert a == [10, 99, 30, 40, 50]


# ---------------------------------------------------------------------------
# 3. Slicing — O(k), creates a COPY
# ---------------------------------------------------------------------------
def slicing() -> None:
    a = [0, 1, 2, 3, 4, 5]
    assert a[1:4] == [1, 2, 3]     # [start:stop)  stop exclusive
    assert a[:3] == [0, 1, 2]      # from start
    assert a[3:] == [3, 4, 5]      # to end
    assert a[::2] == [0, 2, 4]     # every 2nd
    assert a[::-1] == [5, 4, 3, 2, 1, 0]   # reversed copy
    assert a[-2:] == [4, 5]        # last two

    # Slicing is a SHALLOW COPY — independent top-level list...
    b = a[:]
    b[0] = 100
    assert a[0] == 0               # original untouched

    # Slice assignment can resize the list in place
    c = [1, 2, 3, 4]
    c[1:3] = [9, 9, 9]             # replace 2 elements with 3
    assert c == [1, 9, 9, 9, 4]


# ---------------------------------------------------------------------------
# 4. Adding elements
# ---------------------------------------------------------------------------
def adding() -> None:
    a = [1, 2, 3]
    a.append(4)                    # O(1) amortized -> [1,2,3,4]
    a.extend([5, 6])               # O(k) -> [1,2,3,4,5,6]
    a.insert(0, 0)                 # O(n) shift -> [0,1,2,3,4,5,6]  AVOID in hot loops
    assert a == [0, 1, 2, 3, 4, 5, 6]

    # append vs extend — classic confusion:
    x = [1, 2]
    x.append([3, 4])               # nests -> [1, 2, [3, 4]]
    assert x == [1, 2, [3, 4]]
    y = [1, 2]
    y.extend([3, 4])               # flattens -> [1, 2, 3, 4]
    assert y == [1, 2, 3, 4]

    assert [1, 2] + [3, 4] == [1, 2, 3, 4]   # concat -> new list, O(n+m)


# ---------------------------------------------------------------------------
# 5. Removing elements
# ---------------------------------------------------------------------------
def removing() -> None:
    a = [10, 20, 30, 20, 40]
    assert a.pop() == 40           # remove & return last, O(1) -> [10,20,30,20]
    assert a.pop(0) == 10          # remove & return index 0, O(n) -> [20,30,20]
    a.remove(20)                   # remove FIRST occurrence of value, O(n) -> [30,20]
    assert a == [30, 20]
    del a[0]                       # delete by index -> [20]
    assert a == [20]
    a.clear()                      # empty it
    assert a == []

    # Remove all occurrences of a value -> filter into a new list, O(n)
    b = [1, 2, 2, 3, 2, 4]
    b = [x for x in b if x != 2]
    assert b == [1, 3, 4]


# ---------------------------------------------------------------------------
# 6. Searching & counting — O(n)
# ---------------------------------------------------------------------------
def searching() -> None:
    a = [5, 3, 8, 3, 9]
    assert (8 in a) is True        # membership, O(n)
    assert a.index(3) == 1         # first index of value (raises ValueError if absent)
    assert a.count(3) == 2         # occurrences

    # Safe index lookup without exceptions:
    target = 100
    idx = a.index(target) if target in a else -1
    assert idx == -1


# ---------------------------------------------------------------------------
# 7. Sorting & reversing
# ---------------------------------------------------------------------------
def sorting() -> None:
    a = [3, 1, 2]
    a.sort()                       # in place, O(n log n), stable Timsort
    assert a == [1, 2, 3]
    a.sort(reverse=True)
    assert a == [3, 2, 1]

    b = sorted([3, 1, 2])          # returns NEW list, original untouched
    assert b == [1, 2, 3]

    # Custom / multi-key sort (stable): by 2nd field, tie-break by 1st
    pairs = [(1, 3), (2, 1), (3, 1)]
    pairs.sort(key=lambda p: (p[1], p[0]))
    assert pairs == [(2, 1), (3, 1), (1, 3)]

    c = [1, 2, 3]
    c.reverse()                    # in place, O(n)
    assert c == [3, 2, 1]


# ---------------------------------------------------------------------------
# 8. Aggregates & utilities
# ---------------------------------------------------------------------------
def aggregates() -> None:
    a = [4, 1, 7, 3]
    assert sum(a) == 15
    assert min(a) == 1 and max(a) == 7
    assert len(a) == 4
    assert min(a, key=lambda x: abs(x - 5)) == 4   # closest to 5
    assert sorted(a) == [1, 3, 4, 7]
    assert list(enumerate(["a", "b"])) == [(0, "a"), (1, "b")]
    assert list(zip([1, 2], ["a", "b"])) == [(1, "a"), (2, "b")]


# ---------------------------------------------------------------------------
# 9. GOTCHAS — the bugs that cost interviews
# ---------------------------------------------------------------------------
def gotchas() -> None:
    # (a) Aliasing: assignment does NOT copy. Both names point to one list.
    a = [1, 2, 3]
    b = a
    b.append(4)
    assert a == [1, 2, 3, 4]       # 'a' changed too! Use a.copy()/a[:] to clone.

    # (b) Shallow copy: top level is independent, nested objects are SHARED.
    nested = [[1, 2], [3, 4]]
    shallow = nested[:]            # or nested.copy()
    shallow[0].append(99)
    assert nested[0] == [1, 2, 99]   # inner list shared! Use copy.deepcopy for full clone.

    # (c) The [[0]*n]*m trap: all rows are the SAME object.
    bad = [[0] * 3] * 2
    bad[0][0] = 1
    assert bad == [[1, 0, 0], [1, 0, 0]]   # both rows mutated — almost never what you want
    good = [[0] * 3 for _ in range(2)]
    good[0][0] = 1
    assert good == [[1, 0, 0], [0, 0, 0]]  # correct: independent rows

    # (d) Mutating a list while iterating over it -> skipped/duplicated elements.
    #     Iterate over a copy, or build a new list instead.
    data = [1, 2, 3, 4]
    data = [x for x in data if x % 2 == 0]   # safe: new list
    assert data == [2, 4]

    # (e) Mutable default argument is created ONCE and shared across calls.
    def buggy(item, bucket=[]):        # DON'T do this
        bucket.append(item)
        return bucket
    buggy(1)
    assert buggy(2) == [1, 2]          # leaked state from the previous call!

    def fixed(item, bucket=None):      # correct idiom
        if bucket is None:
            bucket = []
        bucket.append(item)
        return bucket
    assert fixed(1) == [1] and fixed(2) == [2]

    # (f) Passing a list to a function lets the function mutate the caller's data.
    def append_in_place(lst: List[int]) -> None:
        lst.append(0)
    mine = [1, 2]
    append_in_place(mine)
    assert mine == [1, 2, 0]           # mutated by callee — pass mine[:] to protect it.


def main() -> None:
    creation()
    access()
    slicing()
    adding()
    removing()
    searching()
    sorting()
    aggregates()
    gotchas()
    print("fundamentals.py: all examples verified ✔")


if __name__ == "__main__":
    main()
