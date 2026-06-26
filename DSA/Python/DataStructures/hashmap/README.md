# Hash Map / Hash Set — Complete Interview Prep Guide

A single place to revise everything about hash maps and hash sets (`dict` and
`set`) in Python for coding interviews: how they work, what every operation
costs, the edge cases that break solutions, and the core patterns with runnable,
tested code.

> All `.py` files here are **runnable and self-testing**. Run any of them
> directly (`python3 fundamentals.py`) — they execute `assert`-based tests and
> print a short demo. If a file runs without raising, every example passed.

---

## Files in this folder

| File | What it covers |
|------|----------------|
| `fundamentals.py` | Every `dict` & `set` operation + its Big-O, `Counter`/`defaultdict`, hashability, common gotchas |
| `hashmap_tricks.py` | The 10 core hashmap/set patterns, each runnable with inline `assert` tests |
| `edge_cases.py`   | A concrete, runnable edge-case checklist (missing key/None value/unhashable/...) |
| `COMPLEXITY.md`   | The *why* behind every Big-O here — why get/put is O(1) average, O(n) worst |
| `README.md`       | This guide — fundamentals, complexity tables, checklists, pattern index |

---

## 1. What is a hash table (in Python)?

A Python `dict` is a **hash table**: it stores key→value entries in an array of
slots ("buckets"). To find a key it computes `hash(key)`, maps that to a slot,
and looks there — so lookups don't scan, they jump. That's what makes
get/put/delete **O(1) on average**.

- **CPython uses open addressing** (not separate chaining). Each entry lives in
  one slot; if the target slot is taken by a *different* key (a **collision**),
  the table **probes** other slots by a deterministic sequence until it finds the
  key or an empty slot. (CPython also keeps a compact insertion-ordered entries
  array plus a sparse index array — this is why dicts preserve order.)
- **Hashing** turns a key into an integer (`hash(key)`); equal keys must hash
  equal. Only **hashable** (effectively immutable) objects can be keys.
- **Load factor** = entries / slots. CPython keeps it below ~2/3. When it's
  exceeded, the table **resizes** (allocates a bigger slot array and re-inserts
  everything). This keeps collisions rare so probing stays short.
- **Resize is amortized O(1)** per insert — the same geometric-growth argument as
  a dynamic array's `append` (see `COMPLEXITY.md`).

A `set` is the **same hash-table machinery with keys only** (no values). It
exists for one job: **O(1) membership** (`x in s`), versus **O(n)** for a list.

> Use a `dict` when you need key→value; a `set` when you only care "have I seen
> this / is this present / what's unique".

---

## 2. `dict` vs `set` — when to use which

| Need | Use | Why |
|------|-----|-----|
| Map keys to values | `dict` | `d[k] = v`, O(1) avg lookup |
| Count occurrences | `Counter` / `dict` | value = count |
| Group items by a key | `defaultdict(list)` / `setdefault` | value = bucket |
| "Have I seen this?" / dedup | `set` | O(1) membership, no values needed |
| Set algebra (∪ ∩ − △) | `set` | built-in operators |
| Immutable / nestable set | `frozenset` | hashable -> can be a dict key or set element |

---

## 3. Operation complexity (memorize this table)

Average is the case you quote in interviews; worst case (every key collides) is
the caveat you mention.

| Operation | Example | Average | Worst | Notes |
|-----------|---------|---------|-------|-------|
| Insert / update | `d[k] = v` | O(1) | O(n) | amortized over resizes |
| Get | `d[k]`, `d.get(k)` | O(1) | O(n) | `d[k]` raises `KeyError` if absent |
| Delete | `del d[k]`, `d.pop(k)` | O(1) | O(n) | `KeyError` if absent (use `pop(k, default)`) |
| Membership | `k in d`, `x in s` | O(1) | O(n) | the headline win over a list |
| `setdefault` / `defaultdict` access | `d.setdefault(k, v)` | O(1) | O(n) | get-or-insert in one step |
| Length | `len(d)` | O(1) | O(1) | stored, not counted |
| Iterate keys/values/items | `for k in d` | O(n) | O(n) | insertion order (3.7+) |
| Copy | `d.copy()`, `dict(d)` | O(n) | O(n) | **shallow** |
| `Counter(iterable)` | build a freq map | O(n) | O(n) | |
| Set union / intersection / diff | `a \| b`, `a & b`, `a - b` | O(len a + len b) | — | intersection iterates the smaller |
| `values()` membership | `v in d.values()` | **O(n)** | O(n) | NOT hashed — it's a scan |

**Space:** a dict/set of n entries is O(n). Building a `set`/`Counter` to get
O(1) lookups is the classic **space-for-time trade** — call it out when asked
about O(1) space.

> Want the *reasoning* behind these numbers (why get/put is O(1) average but O(n)
> worst, why it's amortized under growth, why membership in a set beats a list)?
> See **`COMPLEXITY.md`** — it derives each bound from the trick that produces it.

---

## 4. Edge-case checklist (run through this for EVERY hashmap/set problem)

Before coding, ask / handle:

- [ ] **Missing key** — `d[k]` raises `KeyError`; use `d.get(k, default)` or `defaultdict`.
- [ ] **`None` as a real value** — `d.get(k)` returns `None` for *both* "value is None" and "key absent". Use `k in d` to disambiguate.
- [ ] **Unhashable key** — a `list`/`dict`/`set` key raises `TypeError`. Convert to a `tuple`/`frozenset`.
- [ ] **Duplicate keys** — last assignment silently overwrites; `1`, `1.0`, `True` are the *same* key.
- [ ] **Empty dict / set** — `popitem()` on empty raises; guard `max`/`min` with `default=`.
- [ ] **Mutating size during iteration** — `del d[k]` mid-loop raises `RuntimeError`; iterate `list(d)`.
- [ ] **Default-mutable value** — `m.setdefault(k, []).append(...)` or `defaultdict(list)`, never `m[k].append` on a fresh key.
- [ ] **Reading a `defaultdict` missing key inserts it** — use `.get` if you must not mutate.
- [ ] **Order assumptions** — dict preserves *insertion* order, NOT sorted order.
- [ ] **`set` discards duplicates** — `len(set(arr))` ≠ `len(arr)` if there are dups.
- [ ] **Memory** — building a map is O(n) space; flag it when O(1) space is required.

### Clarifying questions to ask the interviewer
- Are keys/values guaranteed present? What to return on a miss?
- Can values be `None`? Are duplicate keys possible?
- Is extra O(n) space acceptable, or must this be in place?
- Do you need insertion order, sorted order, or no order?

---

## 5. Pattern index (see `hashmap_tricks.py`)

| Pattern | When to reach for it | Typical complexity |
|---------|----------------------|--------------------|
| **Complement map (Two Sum)** | "find a pair / does X's partner exist" | O(n) time, O(n) space |
| **Frequency count** | counts, anagrams, top-k, majority | O(n) |
| **Group anagrams** | bucket items by a canonical key (sorted string / count tuple) | O(n·k log k) or O(n·k) |
| **Seen-set dedup** | contains-duplicate, first repeat, visited tracking | O(n) |
| **Prefix sum + count map** | subarray-sum-equals-k (handles negatives) | O(n) |
| **Sliding window + last-seen map** | longest substring without repeats | O(n) |
| **Count then re-scan** | first unique character | O(n) |
| **Set intersection / union / diff** | common/unique elements across collections | O(n+m) |
| **LRU cache (ordered dict)** | O(1) get/put with eviction | O(1) per op |
| **Composite key (tuple / frozenset)** | key on a pair/position/unordered set | O(1) per op |

---

## 6. Decision guide — "when does a hashmap beat sorting / an array?"

```
Do you need value-by-key lookup, counting, or "have I seen X"?
├── Yes → hashmap / set  (O(1) avg lookup beats O(n) scan and O(n log n) sort)
└── No
    ├── Need a pair/complement (two-sum style)?      → complement map, O(n)
    ├── Need to group/bucket by a derived key?       → dict of lists / defaultdict
    ├── Only membership / dedup matters?             → set, O(1) vs O(n) in a list
    ├── Need ORDER (sorted output, kth smallest)?    → sort or heap, NOT a hashmap
    ├── Need range queries / nearest element?        → sorted array + binary search
    └── Keys are a small dense range 0..n?           → a plain array/list indexes faster

Hashmap WINS when: lookups dominate, order doesn't matter, O(n) space is fine.
Hashmap LOSES when: you need sorted order, range/nearest queries, or O(1) space.
```

A hashmap turns the inner loop of a brute-force O(n²) ("for each element, scan
the rest") into an O(1) lookup, giving O(n) — *if* you can afford O(n) space and
don't need ordering.

---

## 7. Python idioms worth knowing (interview-friendly)

```python
d.get(k, default)                     # safe lookup, no KeyError
d.setdefault(k, []).append(x)         # get-or-create a list bucket
d.pop(k, None)                        # safe delete
from collections import Counter
Counter(iterable)                     # frequency map
Counter(a) == Counter(b)              # anagram check
Counter(s).most_common(k)             # top-k by count
from collections import defaultdict
g = defaultdict(list); g[k].append(x) # auto-init missing key
g = defaultdict(int);  g[k] += 1      # auto-init counter
{k: v for k, v in pairs}              # dict comprehension
{x for x in items}                    # set comprehension
a | b, a & b, a - b, a ^ b            # union / intersection / diff / symmetric
set(arr)                              # dedup; len(set(arr)) = #distinct
frozenset(pair)                       # hashable, order-insensitive composite key
list(d)                               # snapshot keys before mutating in a loop
```

See `fundamentals.py` for the full, runnable list of operations and gotchas.
