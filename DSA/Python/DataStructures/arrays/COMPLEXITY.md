# Complexity — the *why* behind the Big-O

The number (`O(n)`, `O(log n)`, ...) is the answer. This file is the **reasoning
trick** that produces it — the mental model that lets you derive the complexity
in an interview instead of memorizing it. Each entry names the trick, then
proves it.

Two reasoning tools cover almost everything here:

1. **Amortized analysis** — "this *one* operation is occasionally expensive, but
   averaged over many operations it's cheap." Used for `append`.
2. **Aggregate / charging argument** — "this loop looks like it could be O(n²),
   but a pointer/variable only ever moves forward n times *total*, so it's O(n)."
   Used for two pointers, sliding window, Dutch flag, cyclic sort, matrix search.

If you can spot which of these applies, you can derive the bound yourself.

---

## 1. `append` is amortized O(1) — the doubling trick

A list is a contiguous buffer with spare capacity. When it fills, Python
allocates a **bigger** buffer (growth factor ~1.125, conceptually "doubling")
and copies everything over. That copy is O(n) — so how is append O(1)?

**Trick — the cost of the expensive copies is paid for by the cheap appends
before it.** Suppose capacity doubles. To reach n elements you copy:

```
1 + 2 + 4 + 8 + ... + n  ≈  2n   (a geometric series sums to ~2×its last term)
```

So *all* resizes across n appends cost ~2n total = O(n) total, spread over n
appends = **O(1) per append, amortized.** The key is geometric growth: if the
buffer grew by a *fixed +k* each time instead, you'd copy 1+2+3+...+n ≈ n²/2 →
O(n) per append. Doubling is what makes it constant.

> Same trick explains why building a list with n `append`s is O(n) total, not O(n²).

---

## 2. `insert(0, x)` / `pop(0)` / `remove(v)` are O(n) — no trick, just shifting

A list stores elements contiguously by index. Removing or inserting at the
front means **every later element must shift one slot** to keep indices
contiguous. n shifts → O(n). There is no clever workaround *for a list* — if you
need O(1) at both ends, that's what `collections.deque` is for.

**Interview tell:** `for x in a: a.pop(0)` is a hidden O(n²). Reverse-iterate,
use a deque, or use two pointers instead.

---

## 3. Two pointers — O(n) by the "pointers only move forward" argument

```python
left, right = 0, len(arr) - 1
while left < right:
    ... left += 1   # or
    ... right -= 1
```

It looks like a nested search, but **`left` only ever increases and `right` only
ever decreases**, and they stop when they meet. Across the *entire* run, the two
pointers take at most `n` steps combined. Each step is O(1) work → **O(n) total**,
O(1) space. The trick is recognizing the pointers can't backtrack, so there's no
n² blowup even though it's one `while` loop doing a lot.

---

## 4. Sliding window — O(n) because each element enters and leaves once

```python
for right in range(n):     # right advances n times
    while invalid:         # left advances...
        left += 1          # ...but only forward, total ≤ n times
```

The inner `while` makes people guess O(n²). It isn't: **`left` advances at most n
times across the whole loop**, independent of how many times the outer loop
spins. So total pointer movement ≤ 2n. Charge each element O(1) for entering the
window (right) and O(1) for leaving it (left) → **O(n) total.** This "each
element is added once and removed once" is the canonical amortized window
argument.

---

## 5. Kadane's — O(n) because it's 1-D DP with O(1) state

At each index the answer to "best subarray ending *here*" depends only on the
*previous* such answer: `cur = max(x, cur + x)`. One pass, constant state kept
(`cur`, `best`), no recomputation → **O(n) time, O(1) space.** The trick is the
realization that you never need to look back further than one step, which
collapses an O(n²) "try every subarray" into a single sweep.

---

## 6. Prefix sum — O(n) build buys O(1)-per-query range sums

`sum(arr[l..r])` naively is O(n) *per query*; q queries → O(nq).

**Trick — precompute once, subtract.** With `prefix[i] = arr[0]+...+arr[i-1]`:

```
sum(l..r) = prefix[r+1] - prefix[l]      # one subtraction
```

Build is O(n) (one pass). Every query is then O(1). q queries → **O(n + q)**
instead of O(nq). You trade O(n) space for turning repeated range work into a
constant-time lookup.

---

## 7. `subarray_sum_equals_k` — O(n) via prefix sums + a hashmap

Brute force checks every subarray: O(n²). The trick combines prefix sums with a
**complement lookup** (the same idea as Two Sum):

> A subarray `(i, j]` sums to `k` ⟺ `prefix[j] - prefix[i] = k` ⟺
> `prefix[i] = prefix[j] - k`.

So as you sweep and maintain a running prefix sum, you ask a hashmap "how many
earlier prefixes equal `running - k`?" — an O(1) lookup. One pass, O(1) work per
element → **O(n) time, O(n) space.** This is why it handles negatives/zeros that
a sliding window cannot: it doesn't rely on the sum being monotonic.

---

## 8. Binary search — O(log n) because the search space halves

Each comparison discards **half** the remaining candidates. Starting from n, the
sizes go `n → n/2 → n/4 → ... → 1`. The number of halvings to reach 1 is
`log₂(n)` → **O(log n).** The only requirement is a sorted (or otherwise
monotonic) search space; the "trick" in rotated-array search is that even when
rotated, *one half is always sorted*, so you can still decide which half to
discard.

---

## 9. Dutch national flag — O(n) single pass, three pointers converge

`low`, `mid`, `high` partition the array into `<region | =region | unprocessed |
>region`. Every iteration either advances `mid` or retreats `high`, and the loop
ends when `mid > high`. The unprocessed gap `high - mid` **shrinks by one every
step**, so there are ≤ n steps → **O(n), O(1) space.** Same charging argument as
two pointers: the pointers only move toward each other.

---

## 10. Cyclic sort — O(n) despite a `while` with swaps inside

```python
while i < n:
    if misplaced: swap arr[i] into its correct slot   # don't advance i
    else: i += 1
```

It feels like it could loop forever or be O(n²). The trick: **every swap places
at least one element at its final correct index, permanently.** There are only n
elements, so there are at most n "productive" swaps total, plus at most n `i += 1`
steps → **O(n) time, O(1) space.** Charge each swap to the element it correctly
seats; each element is seated once.

---

## 11. Rotation by triple reversal — O(n), O(1) space

Rotating right by k = reverse all, then reverse the first k, then reverse the
rest. Three reversals, each O(n) over its slice → O(n) total. The trick is purely
*space*: reversal is in place, so you rotate **without** the O(n) extra array a
naive "copy to shifted positions" would need. `k %= n` first so `k>n`, `k==n`,
and `k<0` all collapse to the real shift.

---

## 12. Matrix staircase search — O(m+n) by eliminating a row OR a column per step

Start at the top-right corner of a row- and column-sorted matrix. Each
comparison with the target lets you discard an **entire row or an entire
column**:

- current > target → everything below in this column is bigger → drop the column (`col -= 1`)
- current < target → everything left in this row is smaller → drop the row (`row += 1`)

You can drop at most m rows and n columns before the pointers run off the grid →
**O(m + n)**, far better than O(m·n) scanning or O(m log n) per-row binary search.

---

## 13. Product except self — O(n), O(1) extra space, no division

The obvious approach is `total_product / arr[i]` — but that's O(n) and **breaks
on zeros**. The trick is two directional passes: `res[i] = (product of everything
to the left of i) × (product of everything to the right of i)`. First pass fills
left-products; second pass multiplies in right-products using a single rolling
variable. Two O(n) passes, the output array reused as scratch → **O(n) time, O(1)
extra space**, and zeros just fall out naturally.

---

## 14. Boyer–Moore majority vote — O(n), O(1) via cancellation

To find an element appearing **more than n/2 times** without a hashmap: keep a
`candidate` and a `count`. A matching vote increments, a differing vote
decrements; at 0 you adopt the next element as candidate. **Trick — pairing off
one majority element against one non-majority element cancels both. Since the
majority strictly exceeds half, it can't be fully cancelled and survives as the
final candidate.** One pass, two variables → **O(n) time, O(1) space.**

---

## Cheat-sheet: which trick gives which bound

| Bound | Trick that produces it |
|-------|------------------------|
| Amortized O(1) | geometric (doubling) growth spreads rare O(n) copies over many ops |
| O(n) from a loop-with-inner-loop | a pointer/index only moves forward ≤ n times *total* (charging) |
| O(n) DP | each element's answer depends only on O(1) prior state |
| O(1) query after O(n) build | precompute + subtract / hashmap complement lookup |
| O(log n) | each step halves the remaining search space |
| O(m+n) on a sorted grid | each step eliminates a whole row or column |
| O(1) space rearrangement | in-place reversal / swapping instead of a copy |
