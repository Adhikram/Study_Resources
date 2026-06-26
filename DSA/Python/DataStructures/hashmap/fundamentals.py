"""
Hash map / hash set fundamentals for interviews — Python `dict` & `set`.

Covers every operation you are likely to use, its time complexity, and the
gotchas that cause real interview bugs. Each section is runnable and verified
with `assert`s. Run `python3 fundamentals.py` — if it exits cleanly, every
example behaved as documented.

A Python `dict` is a HASH TABLE: keys are hashed to find a bucket (slot) via
open addressing, giving O(1) AVERAGE get/put/delete. It is mutable, preserves
INSERTION ORDER (guaranteed 3.7+), and requires keys to be HASHABLE (immutable).
A `set` is the same machinery with keys only (no values) — O(1) membership.
"""

from collections import Counter, defaultdict
from typing import Dict, List, Set


# ---------------------------------------------------------------------------
# 1. Creation & initialization
# ---------------------------------------------------------------------------
def creation() -> None:
    empty_d: Dict = {}                          # O(1) empty dict
    empty_s: Set = set()                        # O(1) empty set ({} is a DICT!)
    literal = {"a": 1, "b": 2}                  # dict literal
    from_pairs = dict([("x", 1), ("y", 2)])     # from (key, value) pairs, O(n)
    from_kwargs = dict(p=1, q=2)                # from keyword args
    comp = {k: k * k for k in range(4)}         # dict comprehension -> {0:0,1:1,2:4,3:9}
    s_literal = {1, 2, 3}                        # set literal (non-empty braces)
    s_comp = {x % 3 for x in range(6)}           # set comprehension -> {0, 1, 2}
    s_from_iter = set([1, 1, 2, 3])              # dedups -> {1, 2, 3}

    assert empty_d == {} and empty_s == set()
    assert type(empty_s) is set                  # {} is an empty DICT, not a set
    assert literal == {"a": 1, "b": 2}
    assert from_pairs == {"x": 1, "y": 2}
    assert from_kwargs == {"p": 1, "q": 2}
    assert comp == {0: 0, 1: 1, 2: 4, 3: 9}
    assert s_literal == {1, 2, 3}
    assert s_comp == {0, 1, 2}
    assert s_from_iter == {1, 2, 3}


# ---------------------------------------------------------------------------
# 2. Insert / get / update / delete — all O(1) AVERAGE
# ---------------------------------------------------------------------------
def insert_get_update_delete() -> None:
    d = {}
    d["one"] = 1                    # insert, O(1) avg
    d["two"] = 2
    assert d["one"] == 1            # get by key, O(1) avg (KeyError if absent!)
    d["one"] = 11                   # update existing key in place, O(1) avg
    assert d["one"] == 11

    del d["two"]                    # delete by key, O(1) avg (KeyError if absent!)
    assert "two" not in d

    # pop(key) removes & returns; pop(key, default) is the safe form.
    d["three"] = 3
    assert d.pop("three") == 3
    assert d.pop("missing", -1) == -1          # default avoids KeyError
    assert d.popitem() == ("one", 11)          # removes & returns LAST inserted pair

    # update() merges another mapping / iterable of pairs in place, O(k).
    d = {"a": 1}
    d.update({"b": 2, "a": 9})                 # adds b, overwrites a
    assert d == {"a": 9, "b": 2}


# ---------------------------------------------------------------------------
# 3. Get with default & setdefault — avoid KeyError
# ---------------------------------------------------------------------------
def get_with_default() -> None:
    d = {"a": 1}
    assert d.get("a") == 1                      # present
    assert d.get("z") is None                   # absent -> None (NO KeyError)
    assert d.get("z", 0) == 0                   # absent -> supplied default
    assert "z" not in d                         # .get does NOT insert the key

    # setdefault: return existing value, OR insert default and return it.
    cfg = {"timeout": 30}
    assert cfg.setdefault("timeout", 99) == 30  # present -> existing kept
    assert cfg.setdefault("retries", 3) == 3    # absent -> inserted
    assert cfg == {"timeout": 30, "retries": 3}

    # Classic group-by idiom with setdefault (one line, no import):
    groups: Dict[str, List[int]] = {}
    for n in [1, 2, 3, 4]:
        groups.setdefault("even" if n % 2 == 0 else "odd", []).append(n)
    assert groups == {"odd": [1, 3], "even": [2, 4]}


# ---------------------------------------------------------------------------
# 4. Membership — O(1) AVERAGE (vs O(n) for a list!)
# ---------------------------------------------------------------------------
def membership() -> None:
    d = {"a": 1, "b": 2}
    assert ("a" in d) is True                   # checks KEYS, O(1) avg
    assert ("z" in d) is False
    assert (1 in d.values()) is True            # values() membership is O(n)!

    s = {10, 20, 30}
    assert (20 in s) is True                    # O(1) avg — the reason sets exist
    assert (99 in s) is False

    # Why this matters: list membership is O(n), set membership is O(1).
    big_list = list(range(1000))
    big_set = set(big_list)
    assert (999 in big_list) is True            # O(n) scan
    assert (999 in big_set) is True             # O(1) hash lookup


# ---------------------------------------------------------------------------
# 5. Iteration — keys / values / items (insertion order, 3.7+)
# ---------------------------------------------------------------------------
def iteration() -> None:
    d = {"a": 1, "b": 2, "c": 3}
    assert list(d) == ["a", "b", "c"]           # iterating a dict yields KEYS
    assert list(d.keys()) == ["a", "b", "c"]
    assert list(d.values()) == [1, 2, 3]
    assert list(d.items()) == [("a", 1), ("b", 2), ("c", 3)]

    # items() is the standard way to iterate pairs.
    total = 0
    for _key, val in d.items():
        total += val
    assert total == 6

    # Views are LIVE: they reflect later mutations of the dict.
    keys_view = d.keys()
    d["x"] = 9
    assert "x" in keys_view                     # view updated automatically
    del d["x"]


# ---------------------------------------------------------------------------
# 6. Counter — frequency map with batteries included
# ---------------------------------------------------------------------------
def counter_basics() -> None:
    c = Counter("mississippi")                  # counts each char
    assert c["s"] == 4 and c["i"] == 4 and c["p"] == 2
    assert c["z"] == 0                          # MISSING key -> 0, never KeyError

    assert c.most_common(2) == [("i", 4), ("s", 4)]   # top-2 by count

    # Counters add/subtract elementwise like multisets.
    a = Counter("aab")
    b = Counter("abc")
    assert a + b == Counter({"a": 3, "b": 2, "c": 1})
    assert (a - b) == Counter({"a": 1})          # subtract drops <=0 counts

    # Build from any iterable; great for "are these two anagrams?"
    assert Counter("listen") == Counter("silent")


# ---------------------------------------------------------------------------
# 7. defaultdict — auto-initialize missing keys
# ---------------------------------------------------------------------------
def defaultdict_basics() -> None:
    # int factory -> missing key starts at 0; perfect for counting.
    freq: Dict[str, int] = defaultdict(int)
    for ch in "banana":
        freq[ch] += 1                           # no KeyError on first touch
    assert freq == {"b": 1, "a": 3, "n": 2}

    # list factory -> missing key starts at []; perfect for grouping.
    groups: Dict[int, List[int]] = defaultdict(list)
    for n in [1, 2, 3, 4, 5]:
        groups[n % 2].append(n)
    assert groups[0] == [2, 4] and groups[1] == [1, 3, 5]

    # WARNING: merely READING a missing key INSERTS it (with the default).
    dd: Dict[str, int] = defaultdict(int)
    _ = dd["ghost"]                             # this creates "ghost": 0
    assert "ghost" in dd                        # side effect! use .get to avoid


# ---------------------------------------------------------------------------
# 8. Set operations — union / intersection / difference / symmetric
# ---------------------------------------------------------------------------
def set_operations() -> None:
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    assert a | b == {1, 2, 3, 4, 5, 6}          # union (in either)
    assert a & b == {3, 4}                       # intersection (in both)
    assert a - b == {1, 2}                       # difference (in a, not b)
    assert a ^ b == {1, 2, 5, 6}                 # symmetric diff (in exactly one)

    # Method forms accept any iterable, operators require sets.
    assert a.union([7]) == {1, 2, 3, 4, 7}
    assert a.intersection([2, 3, 99]) == {2, 3}

    # Subset / superset / disjoint relations.
    assert {1, 2} <= a                           # subset
    assert a >= {1, 2}                           # superset
    assert {8, 9}.isdisjoint(a) is True          # no common elements

    # Add / discard / remove.
    s = {1, 2}
    s.add(3)
    s.discard(99)                                # discard: no error if absent
    assert s == {1, 2, 3}
    try:
        s.remove(99)                             # remove: KeyError if absent
        assert False
    except KeyError:
        pass


# ---------------------------------------------------------------------------
# 9. Hashability rules — what can be a key / set element
# ---------------------------------------------------------------------------
def hashability() -> None:
    # Hashable (immutable) types are valid keys: int, str, float, bool, tuple,
    # frozenset, None, and tuples OF hashable things.
    ok = {1: "int", "s": "str", (1, 2): "tuple", None: "none", frozenset({1}): "fs"}
    assert ok[(1, 2)] == "tuple"
    assert ok[None] == "none"

    # A tuple is hashable ONLY if all its members are hashable.
    assert hash((1, 2)) == hash((1, 2))          # deterministic within a run
    try:
        hash((1, [2]))                           # tuple containing a list
        assert False
    except TypeError:
        pass                                     # unhashable: contains a list

    # Sets can hold the same hashable types.
    valid_set = {1, "a", (2, 3), frozenset({9})}
    assert (2, 3) in valid_set


# ---------------------------------------------------------------------------
# 10. GOTCHAS — the bugs that cost interviews
# ---------------------------------------------------------------------------
def gotchas() -> None:
    # (a) KeyError vs .get: indexing a missing key RAISES; .get returns a default.
    d = {"a": 1}
    try:
        _ = d["missing"]                         # raises KeyError
        assert False
    except KeyError:
        pass
    assert d.get("missing", 0) == 0              # safe

    # (b) Mutable / unhashable keys: a list cannot be a key (it's mutable).
    try:
        bad = {[1, 2]: "x"}                       # TypeError: unhashable type: 'list'
        assert False
    except TypeError:
        pass
    good = {(1, 2): "x"}                          # use a tuple instead
    assert good[(1, 2)] == "x"

    # (c) None-value vs missing-key ambiguity: .get can't distinguish them.
    d = {"present": None}
    assert d.get("present") is None              # key EXISTS, value is None
    assert d.get("absent") is None               # key MISSING -> also None
    assert ("present" in d) is True              # use `in` to tell them apart
    assert ("absent" in d) is False

    # (d) Insertion order is preserved (guaranteed since Python 3.7).
    order = {}
    for k in ["z", "a", "m"]:
        order[k] = 1
    assert list(order) == ["z", "a", "m"]        # NOT sorted — insertion order
    order["z"] = 2                               # updating a key keeps its position
    assert list(order) == ["z", "a", "m"]

    # (e) Mutating a dict's size while iterating -> RuntimeError.
    d = {"a": 1, "b": 2, "c": 3}
    try:
        for key in d:
            if key == "a":
                del d[key]                        # changes size mid-iteration
        assert False
    except RuntimeError:
        pass
    # Fix: iterate over a snapshot of the keys.
    d = {"a": 1, "b": 2, "c": 3}
    for key in list(d):                          # list() snapshots the keys
        if key == "a":
            del d[key]
    assert d == {"b": 2, "c": 3}


def main() -> None:
    creation()
    insert_get_update_delete()
    get_with_default()
    membership()
    iteration()
    counter_basics()
    defaultdict_basics()
    set_operations()
    hashability()
    gotchas()
    print("fundamentals.py: all examples verified ✔")


if __name__ == "__main__":
    main()
