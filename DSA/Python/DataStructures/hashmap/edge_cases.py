"""
Hash map / hash set edge cases — the inputs that break naive solutions, with
runnable proof.

Each function demonstrates ONE edge-case category: a naive approach that fails
and the robust version that doesn't. Run `python3 edge_cases.py`; a clean exit
means every "robust" version handled its edge case as documented.

Use this as a pre-submission checklist: walk your solution through each case.
"""

from collections import defaultdict
from typing import Dict, List


# ---------------------------------------------------------------------------
# 1. MISSING KEY — indexing raises KeyError; .get returns a default.
# ---------------------------------------------------------------------------
def missing_key() -> None:
    d = {"a": 1}

    def naive_lookup(m, key):     # crashes on absent key
        return m[key]

    def robust_lookup(m, key):    # explicit default, no exception
        return m.get(key, 0)

    assert robust_lookup(d, "a") == 1
    assert robust_lookup(d, "z") == 0
    try:
        naive_lookup(d, "z")
        assert False
    except KeyError:
        pass                      # exactly the bug we avoid


# ---------------------------------------------------------------------------
# 2. UNHASHABLE KEY — mutable containers (list/dict/set) can't be keys.
# ---------------------------------------------------------------------------
def unhashable_key() -> None:
    def naive_key(pair):          # uses a LIST as a key -> TypeError
        m = {}
        m[pair] = 1
        return m

    def robust_key(pair):         # convert to an immutable tuple first
        m = {}
        m[tuple(pair)] = 1
        return m

    assert robust_key([1, 2]) == {(1, 2): 1}
    try:
        naive_key([1, 2])
        assert False
    except TypeError:
        pass                      # "unhashable type: 'list'"

    # Same rule for set elements.
    try:
        {[1, 2]}                  # set of lists -> TypeError
        assert False
    except TypeError:
        pass
    assert {(1, 2)} == {(1, 2)}    # tuples are fine


# ---------------------------------------------------------------------------
# 3. NONE AS A LEGITIMATE VALUE — .get can't tell "None value" from "missing".
# ---------------------------------------------------------------------------
def none_value() -> None:
    d = {"present": None}

    def naive_has(m, key):        # WRONG: treats a real None value as "missing"
        return m.get(key) is not None

    def robust_has(m, key):       # correct: membership test
        return key in m

    assert naive_has(d, "present") is False    # the bug: it IS present
    assert robust_has(d, "present") is True    # correct
    assert robust_has(d, "absent") is False

    # If you need a default that None could collide with, use a unique sentinel.
    SENTINEL = object()
    assert d.get("absent", SENTINEL) is SENTINEL   # unambiguously "missing"
    assert d.get("present", SENTINEL) is None      # unambiguously "value is None"


# ---------------------------------------------------------------------------
# 4. DEFAULT-MUTABLE-VALUE PATTERN — build lists/sets per key safely.
# ---------------------------------------------------------------------------
def default_mutable_value() -> None:
    edges = [("a", 1), ("b", 2), ("a", 3)]

    def naive_group(pairs):       # crashes: m[k] doesn't exist yet to .append
        m = {}
        for k, v in pairs:
            m[k].append(v)        # KeyError on first touch of each key
        return m

    def robust_setdefault(pairs): # setdefault inserts [] then appends
        m: Dict[str, List[int]] = {}
        for k, v in pairs:
            m.setdefault(k, []).append(v)
        return m

    def robust_defaultdict(pairs):  # defaultdict(list) auto-creates []
        m: Dict[str, List[int]] = defaultdict(list)
        for k, v in pairs:
            m[k].append(v)
        return dict(m)

    expected = {"a": [1, 3], "b": [2]}
    assert robust_setdefault(edges) == expected
    assert robust_defaultdict(edges) == expected
    try:
        naive_group(edges)
        assert False
    except KeyError:
        pass


# ---------------------------------------------------------------------------
# 5. COLLISIONS / DUPLICATE KEYS — later assignment OVERWRITES the earlier.
# ---------------------------------------------------------------------------
def duplicate_keys_overwrite() -> None:
    # A dict literal with repeated keys keeps the LAST value silently.
    d = {"a": 1, "a": 2}          # noqa: F601 (intentional duplicate)
    assert d == {"a": 2}          # first value is lost — easy to miss in a bug

    # dict() from pairs behaves the same: last wins.
    built = dict([("k", 1), ("k", 9)])
    assert built == {"k": 9}

    # If you need to KEEP earlier values, accumulate instead of overwrite.
    def keep_all(pairs):
        m: Dict[str, List[int]] = defaultdict(list)
        for k, v in pairs:
            m[k].append(v)
        return dict(m)
    assert keep_all([("k", 1), ("k", 9)]) == {"k": [1, 9]}

    # Hash COLLISION (different keys, same bucket) is invisible & correct:
    # equality, not hash, decides identity, so both keys coexist.
    assert hash(1) == hash(1.0) == hash(True)      # all collide to the same hash
    collide = {}
    collide[1] = "int"
    collide[1.0] = "float"        # 1 == 1.0 -> SAME key, overwrites!
    assert collide == {1: "float"}                 # only ONE entry, value updated
    assert len(collide) == 1


# ---------------------------------------------------------------------------
# 6. EMPTY DICT / SET — operations must degrade gracefully.
# ---------------------------------------------------------------------------
def empty_collections() -> None:
    empty_d: Dict[str, int] = {}
    assert len(empty_d) == 0
    assert list(empty_d.items()) == []         # iteration yields nothing
    assert empty_d.get("x", 0) == 0
    assert ("x" in empty_d) is False
    try:
        empty_d.popitem()                       # pop from empty -> KeyError
        assert False
    except KeyError:
        pass

    empty_s: set = set()
    assert len(empty_s) == 0
    assert (empty_s & {1, 2}) == set()          # intersection with empty -> empty
    assert (empty_s | {1, 2}) == {1, 2}         # union with empty -> the other
    assert empty_s.isdisjoint({1, 2}) is True   # vacuously disjoint
    # max/min over empty must be guarded just like with lists.
    assert (max(empty_d, default=None)) is None


def main() -> None:
    missing_key()
    unhashable_key()
    none_value()
    default_mutable_value()
    duplicate_keys_overwrite()
    empty_collections()
    print("edge_cases.py: all 6 edge-case categories verified ✔")


if __name__ == "__main__":
    main()
