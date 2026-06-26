# Complexity — the *why* behind the Big-O

The number (`O(1)`, `O(n)`, ...) is the answer. This file is the **reasoning
trick** that produces it — the mental model that lets you derive (and defend) the
complexity in an interview instead of memorizing it. Each entry names the trick,
then proves it.

Three reasoning tools cover everything here:

1. **Hashing → direct addressing** — "instead of searching for a key, compute
   *where* it lives and go straight there." Turns O(n) search into O(1).
2. **Amortized analysis** — "this *one* operation is occasionally expensive
   (a resize), but averaged over many operations it's cheap." Used for insert.
3. **Worst-case adversary** — "if every key collides, the structure degrades to a
   linear scan." This is why we say O(1) *average*, O(n) *worst*.

If you can state which of these applies, you can derive the bound yourself.

---

## 1. `d[k]` get/put is O(1) AVERAGE — hash → bucket → done

A list answers "is `x` here?" by scanning: O(n). A dict answers it by
**computing the location** instead of searching for it:

```
slot = hash(key) mod (number of slots)      # one arithmetic step
look at table[slot]                          # one memory access
```

No scan — you jump straight to where the key *must* be. Computing `hash(key)`
and indexing the slot array are both O(1) (for fixed-size keys like ints and
short strings). **Trick: replace "search the data" with "compute the address."**

This holds **on average** only if keys are spread evenly across slots, which
depends on a good hash function and a low load factor (next sections explain why
both are maintained).

---

## 2. Why it's O(n) WORST case — everything collides into one chain

Two distinct keys can hash to the **same slot** — a **collision**. CPython
resolves it with **open addressing**: probe a deterministic sequence of other
slots until the key or an empty slot is found.

If an adversary (or a pathological hash) makes *every* key collide into the same
probe sequence, a lookup must walk past all the others before finding its key —
that's a linear scan of k entries. With n entries that's **O(n) per operation**.

```
ideal:    h(a)=0  h(b)=1  h(c)=2     → one probe each       → O(1)
worst:    h(a)=h(b)=h(c)=0            → probe 0,1,2,...      → O(n)
```

**Trick to remember the distinction:** O(1) is the *expected* cost under good
distribution; O(n) is the cost when the distribution collapses. In practice
Python's hashing + resizing keep us in the average case, so we *quote* O(1) but
*acknowledge* O(n).

---

## 3. Insert is AMORTIZED O(1) — resize + load factor (the doubling trick)

The table has a fixed number of slots. As you insert, the **load factor**
(entries ÷ slots) rises. Past a threshold (~2/3 in CPython) collisions become
frequent and probing slows down — so the dict **resizes**: it allocates a bigger
slot array (~doubling) and **re-inserts every existing entry** into it. That
rehash is O(n). So how is insert O(1)?

**Trick — the rare O(n) rehash is paid for by the many cheap inserts before it**,
exactly like a dynamic array's `append`. To grow to n entries the rehashes copy:

```
1 + 2 + 4 + 8 + ... + n  ≈  2n      (geometric series ≈ 2× its last term)
```

So *all* resizes across n inserts cost ~2n total = O(n), spread over n inserts =
**O(1) per insert, amortized.** Geometric (doubling) growth is what makes it
constant; growing by a fixed +k each time would give 1+2+...+n ≈ n²/2 → O(n) per
insert. Keeping the load factor low is *also* what keeps probe chains short,
preserving the O(1) average lookup from section 1.

> Same trick, two payoffs: amortizes the rehash cost AND bounds collisions.

---

## 4. Membership in a `set` is O(1) vs O(n) in a `list`

```python
x in some_list     # O(n): compare x against each element until found
x in some_set      # O(1) average: hash x, jump to its slot, check
```

A list has no idea *where* `x` would be, so it checks every position — O(n). A
set computes `hash(x)` and looks **only** in the slot `x` would occupy — O(1)
average (O(n) worst, per section 2). **Trick: the set pre-arranges elements by
their hash so "is it here?" becomes "is it in *this one* slot?"** This single
difference is why converting a list to a set before repeated `in` checks turns an
O(n·q) loop into O(n + q).

---

## 5. Why hashing requires immutability (hashable = effectively immutable)

A key's slot is `hash(key) mod slots`. The dict files the entry under that slot
**at insert time**. If the key later *mutated*, its hash would change, so it
would now belong in a *different* slot — but it's still physically sitting in the
old one. Lookups would compute the new slot, find nothing, and report the key as
absent even though it's in the table. The structure would be silently corrupt.

**Trick — to keep "where I filed it" equal to "where I look for it," the key's
hash must never change.** Python enforces this by only allowing **hashable**
objects (those with a stable `__hash__`) as keys/elements: `int`, `str`, `float`,
`bool`, `tuple` (of hashables), `frozenset`, `None`. Mutable containers (`list`,
`dict`, `set`) are unhashable → `TypeError`. Contract: **`a == b` ⇒
`hash(a) == hash(b)`**, and the hash is constant for the object's lifetime.

> Corollary: `1 == 1.0 == True` and they share a hash, so they are the **same**
> dict key — inserting all three leaves one entry.

---

## 6. Set algebra — O(size of inputs), iterate the smaller side

`a & b` (intersection) iterates the **smaller** set and tests each element for
membership in the larger — each test is O(1) average — giving **O(min(|a|,|b|))**.
`a | b` (union) and `a - b` touch every relevant element once → **O(|a|+|b|)**.
**Trick: set algebra is just membership tests in a loop**, and membership is O(1),
so the total is linear in the elements examined — never the O(|a|·|b|) a naive
nested-loop comparison would cost.

---

## 7. Why the hashmap patterns are O(n) — the complement/seen trick

The brute force for two-sum, dedup, subarray-sum, etc. is a double loop: "for
each element, scan the others" → O(n²). Each pattern replaces that inner scan
with an **O(1) hashmap lookup**:

> "Have I seen the complement / this value / this prefix sum before?"

One outer pass (n iterations) × O(1) work each → **O(n) time, O(n) space**. The
space is the price of the lookup table; the trick is recognizing that the inner
loop was only ever asking a membership/lookup question, which a hashmap answers
in O(1). This is also why `subarray_sum_equals_k` beats a sliding window on
arrays with negatives: it relies on equality lookups, not on the sum being
monotonic.

---

## 8. LRU cache — O(1) get & put via an ordered dict

A naive LRU scans for the least-recently-used entry on each eviction: O(n). Using
an **insertion-ordered dict** (CPython dicts, or `OrderedDict`):

- `get`/`put` find the entry by key in O(1) (it's a hashmap).
- "mark as most-recently-used" = `move_to_end(key)` — O(1).
- "evict the oldest" = `popitem(last=False)` (remove the front) — O(1).

**Trick: order + hashing together** give random access *and* O(1) reordering at
the ends, so both operations stay constant. No scan is ever needed.

---

## Cheat-sheet: which trick gives which bound

| Bound | Trick that produces it |
|-------|------------------------|
| O(1) average get/put/membership | hash the key → jump to its slot (compute the address, don't search) |
| O(n) worst case | all keys collide → probing degrades to a linear scan |
| Amortized O(1) insert | geometric (doubling) resize spreads the rare O(n) rehash over many inserts |
| Low load factor maintained | resize before it fills → probe chains stay short → average stays O(1) |
| set membership O(1) vs list O(n) | set pre-files elements by hash; list has no location info |
| set algebra O(\|a\|+\|b\|) | it's just O(1) membership tests over the elements, smaller side driven |
| O(n) hashmap patterns | replace the inner O(n) scan with an O(1) "have I seen it?" lookup |
| O(1) LRU get/put | ordered dict = hashing (random access) + O(1) reorder at the ends |
| hashable ⇒ immutable | the slot is fixed at insert time; a changing hash would lose the key |
