# Trie (Prefix Tree) — Complete Interview Prep Guide

A single place to revise everything about tries in Python for coding interviews:
how they work, what every operation costs, the edge cases that break solutions,
and the core patterns with runnable, tested code.

> All `.py` files here are **runnable and self-testing**. Run any of them
> directly (`python3 fundamentals.py`) — they execute `assert`-based tests and
> print a short demo. If a file runs without raising, every example passed.

---

## Files in this folder

| File | What it covers |
|------|----------------|
| `fundamentals.py` | A clean `Trie`/`TrieNode` class: insert, search, starts_with, delete, count_words_with_prefix + gotchas |
| `trie_tricks.py`  | The 5 core trie patterns, each runnable with inline `assert` tests |
| `edge_cases.py`   | A concrete, runnable edge-case checklist (empty/single/dup/prefix/wildcard/...) |
| `COMPLEXITY.md`   | The *why* behind every Big-O here — the reasoning/trick that derives it |
| `README.md`       | This guide — fundamentals, complexity tables, checklists, pattern index |

---

## 1. What is a trie?

A **trie** (prefix tree) is a **character-indexed tree**. Instead of storing a
whole key in one node, it spreads the key across a *path*: one node per
character, walking down from the root.

Each node holds:

- a **`children` map** (`char -> child node`) — the edges out of this node, and
- an **`is_end` flag** — a sentinel marking "a complete word terminates here."

```
insert("cat"), insert("car"), insert("card"):

        (root)
          |c
        (·)
          |a
        (·)
       t/  \r
    (cat*) (·)          * = is_end (a stored word ends here)
            |d
          (card*)        "car" is_end on the 'r' node; "card" continues to 'd'
```

- **Shared prefixes share nodes.** "cat", "car", "card" all reuse the `c -> a`
  path; only where they diverge do new branches appear. That sharing is the
  entire point — it makes prefix work cheap.
- The **`is_end` flag is load-bearing.** Reaching the end of a path does *not*
  mean you found a word — the node must have `is_end` set. This distinguishes a
  stored word ("car") from a mere prefix of one ("ca").

### When to use a trie (and why it beats a hash set)

Reach for a trie when the problem is about **prefixes**:

- prefix queries / "does any word start with X?",
- autocomplete / type-ahead,
- dictionary & spell-check operations,
- wildcard or pattern matching over a word set,
- bitwise problems (binary trie for max-XOR / range queries).

A **hash set** answers "is this *exact* word present?" in O(m) — same as a trie —
but it stores keys opaquely, so it **cannot answer prefix questions** without
scanning every key (O(N·M)). A trie walks straight to the prefix node in O(p) and
has the entire matching set sitting in that subtree. **Prefix work is where a
trie wins; exact-membership-only work is where a hash set is simpler.**

---

## 2. Operation complexity (memorize this table)

`m` = word length, `p` = prefix length, `N` = number of words, `M` = longest
word, `ALPHABET` = distinct chars per node.

| Operation | Example | Time | Notes |
|-----------|---------|------|-------|
| Insert | `t.insert("cat")` | **O(m)** | one node per char; independent of N |
| Search (full word) | `t.search("cat")` | **O(m)** | walk + require `is_end` |
| Starts-with (prefix) | `t.starts_with("ca")` | **O(p)** | walk only; `is_end` irrelevant |
| Delete | `t.delete("cat")` | **O(m)** | prune only nodes no other word needs |
| Count words with prefix | `t.count_words_with_prefix("ca")` | **O(p)** | with a cached per-node counter |
| Wildcard search (`.`) | `wd.search("c.t")` | O(b^w·m) | each `.` forks DFS; b = branching, w = #wildcards |
| Binary-trie insert/query | max-XOR | O(32) = O(1) | fixed 32-bit depth per number |

**Space:** O(ALPHABET · N · M) worst case (no shared prefixes). In practice,
shared prefixes and a dict-based `children` (pay only for edges that exist)
shrink this substantially.

> Want the *reasoning* behind these numbers (why insert is O(m) regardless of N,
> why prefix queries beat scanning, the wildcard branching cost, the 32-step
> XOR)? See **`COMPLEXITY.md`** — it derives each bound from the trick that
> produces it.

---

## 3. Edge-case checklist (run through this for EVERY trie problem)

Before coding, ask / handle:

- [ ] **Empty string** `""` — a legitimate word stored on `root.is_end`; the
      empty prefix matches everything. Does your code handle it?
- [ ] **Single character** — the end node is a direct child of root.
- [ ] **Duplicate inserts** — must be idempotent for membership (or accumulate a
      frequency/count, if that's the intent).
- [ ] **Prefix that is NOT a full word** — the #1 trie bug. `is_end` must be set;
      "path exists" is not "word found."
- [ ] **Missing prefix / diverging path** — use `.get()` and short-circuit to
      False; don't `node.children[ch]` blindly (KeyError).
- [ ] **Case sensitivity** — `'A' != 'a'`. Normalize up front if needed.
- [ ] **Delete of a non-existent word** — must be a safe no-op.
- [ ] **Delete a word that is a prefix of another** — clear `is_end` only; do
      NOT remove the shared nodes a longer word still needs.
- [ ] **Wildcard matching nothing** — wrong length or diverging path returns
      False; the final node must still be `is_end`.
- [ ] **Very large dictionary** — is the O(ALPHABET·N·M) space acceptable?

### Clarifying questions to ask the interviewer
- Case-sensitive? Fixed alphabet (a–z) or arbitrary characters?
- Are duplicate inserts possible — track counts/frequency?
- Do I need delete? Wildcards? Top-k by frequency?
- What to return when a word/prefix is absent (`False`, `[]`, `-1`)?

---

## 4. Pattern index (see `trie_tricks.py`)

| Pattern | When to reach for it | Typical complexity |
|---------|----------------------|--------------------|
| **WordDictionary (`.` wildcard)** | add/search where queries contain single-char wildcards | O(m) literal, O(b^w·m) with wildcards |
| **Word Search II** | find all dictionary words on a grid | trie build + grid DFS, pruned per branch |
| **Autocomplete top-k** | prefix suggestions ranked by frequency | O(p + S log S), S = words under prefix |
| **Replace words** | swap each word for its shortest dictionary root | O(total text length) after O(Σroots) build |
| **Maximum XOR (binary trie)** | max XOR of any two numbers | O(32·n) = O(n) |

---

## 5. Decision guide — "trie vs hash set vs sorting?"

```
Do you need PREFIX queries (startsWith, autocomplete, "words beginning with X")?
├── Yes
│   ├── Also need order / range of strings?      → sort the words (binary-search the prefix range)
│   └── Need live insert/delete + prefix lookup? → TRIE  (O(p) prefix, O(m) insert/delete)
└── No  (only exact membership / counts)
    ├── O(1) exact lookup, no prefix work?        → HASH SET / dict (simplest, less memory)
    └── Bitwise max/min-XOR over a number set?    → BINARY TRIE (32-step paths)
```

- **Trie** — best when prefixes matter *and* the set changes; O(p) prefix work.
- **Hash set** — best for plain exact membership; simpler and lighter, but
  O(N·M) to answer any prefix question.
- **Sorting** — one-shot prefix ranges via binary search, but O(N log N) up front
  and awkward with frequent inserts/deletes.

---

## 6. Python idioms worth knowing (interview-friendly)

```python
# Dict children (only pay for edges that exist; no fixed 26-slot arrays):
node.children = {}
node = node.children.setdefault(ch, TrieNode())   # walk-or-create in one line

# Sentinel end-of-word flag — the difference between a word and a prefix:
node.is_end = True

# Safe walk that short-circuits on a missing branch (no KeyError):
nxt = node.children.get(ch)
if nxt is None:
    return False

# Cache a count on each node for O(p) "words with prefix":
node.count += 1            # on every insert that passes through

# Binary trie: iterate bits MSB -> LSB
for i in range(31, -1, -1):
    bit = (num >> i) & 1
```

See `fundamentals.py` for the full, runnable `Trie` class and gotchas.
