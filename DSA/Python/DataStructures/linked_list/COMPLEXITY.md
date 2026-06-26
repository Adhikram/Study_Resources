# Complexity — the *why* behind the Big-O

The number (`O(n)`, `O(1)`, ...) is the answer. This file is the **reasoning
trick** that produces it — the mental model that lets you derive the complexity
in an interview instead of memorizing it. Each entry names the trick, then
proves it.

One idea underlies almost everything about linked lists:

> **A linked list has pointers, not indices.** You get O(1) only at a node you
> already hold a reference to; reaching any *other* node costs one hop per link.

From that single fact the whole table falls out. Two secondary reasoning tools
appear in the pointer patterns:

1. **Charging / "pointers only move forward"** — a loop with two pointers looks
   like it could be O(n²), but each pointer advances at most n times *total*, so
   it's O(n). Used by fast/slow, two-pointer-gap, intersection.
2. **In-place rewiring** — you can reorder a linked list by changing pointers
   alone, with no copy, which is what buys **O(1) space** for reverse, merge,
   palindrome, and reorder.

---

## 1. Access / search is O(n) — no contiguity, so no random access

An array stores elements in one contiguous block, so the address of element `k`
is `base + k × size` — a single multiply-add → **O(1)**. A linked list stores
each node wherever the allocator put it, joined only by `next` pointers. There is
**no formula** for "the address of node k"; the *only* way to find it is to start
at the head and follow `next` k times.

```
head → [a] → [b] → [c] → [d] → None
              ↑ to reach c you MUST pass through a and b
```

k hops, each O(1) → **O(k), worst case O(n).** Search by value is the same walk
with a comparison at each node → O(n). This is the price you pay for the cheap
splicing in the next entry: you trade away random access to gain O(1) structural
edits.

---

## 2. Insert/delete at a KNOWN node is O(1) — rewire, don't shift

This is the linked list's superpower and the mirror image of entry 1. If you
already hold the node before the gap, inserting or deleting is **just a couple of
pointer assignments — no elements move.**

```
insert x after p:        delete the node after p:
  new.next = p.next        p.next = p.next.next
  p.next   = new           (the unlinked node is now unreachable)
```

Each is a fixed number of pointer writes → **O(1)**, regardless of list length.
Contrast an array: inserting/deleting in the middle forces **every later element
to shift one slot** to keep indices contiguous → O(n). The catch is the
qualifier *"known node"*: if you must first *find* the node by value or index,
that search is O(n) (entry 1), and only the structural edit itself is O(1). So
"delete value v" is **O(n) find + O(1) unlink = O(n)** overall, but "delete the
node this pointer references" is genuinely O(1).

> Why a **dummy/sentinel node** matters here: deleting the head has no
> predecessor `p`. Prepending `dummy → head` gives *every* real node a
> predecessor, so the single `p.next = p.next.next` rewrite covers the head,
> middle, and tail with no special case — keeping the code O(1) per edit *and*
> branch-free.

---

## 3. Reversal is O(n) time, O(1) space — flip one pointer per node

```python
prev, cur = None, head
while cur:
    nxt = cur.next     # 1. remember the rest
    cur.next = prev    # 2. flip this link backwards
    prev = cur         # 3. advance prev
    cur = nxt          # 4. advance cur
return prev            # old tail = new head
```

You visit each node exactly **once** and do O(1) work (four assignments) per
node → **O(n) time.** Crucially you reverse the list by **mutating the existing
pointers in place** — no new nodes, no copy, just the three tracking variables
`prev/cur/nxt` → **O(1) space.** The one non-obvious line is stashing `nxt`
*before* overwriting `cur.next`; skip it and you've severed the rest of the list
and can't advance.

**Recursive** reversal is also O(n) time but **O(n) space**: the recursion
descends to the tail before doing any rewiring, so n stack frames are live at
once. Same time, worse space — mention this trade-off if asked for O(1) space.

---

## 4. Fast/slow (find middle) is O(n), O(1) — one walker laps the other

`slow` advances 1 node per step, `fast` advances 2. When `fast` reaches the end,
it has covered the whole list while `slow` covered exactly half — so `slow` sits
at the **middle**.

```
step:   0      1      2
slow:   ●      ●→     ●→→
fast:   ●      ●→→    ●→→→→ (off the end)
```

The loop runs while `fast` can take two steps, i.e. ⌈n/2⌉ iterations of O(1) work
→ **O(n) time.** Two pointers, nothing copied → **O(1) space.** This is the
charging argument in its simplest form: `fast` moves forward 2 each step and
never backtracks, so it terminates in ~n/2 steps and drags `slow` to the
midpoint for free.

---

## 5. Floyd's tortoise & hare — WHY they meet, and why it's O(n)/O(1)

**Detection.** In a list *with* a cycle, once both pointers are inside the loop
the hare gains **one node per step** on the tortoise (it moves 2, the tortoise
moves 1, net +1). The gap between them therefore shrinks by exactly 1 each step,
so it must hit 0 — i.e. they **collide** — within at most (cycle length) steps.
If there's no cycle, the hare simply runs off the end (`fast`/`fast.next` is
`None`) and the loop stops. Either way the hare traverses O(n) nodes → **O(n)
time, O(1) space.**

**Finding the cycle start.** Let the tail-before-loop have length `a` (head to the
entry node), and let the meeting point be `b` nodes into a cycle of length `c`.
When they meet:

```
tortoise distance = a + b
hare distance      = a + b + (some whole number of laps) k·c
hare went twice as far:  2(a + b) = a + b + k·c
                    ⟹    a + b = k·c
                    ⟹    a = k·c − b
```

So `a` (head → entry) equals `k·c − b`, which is **the distance from the meeting
point back around to the entry**. Therefore: reset one pointer to the head, leave
the other at the meeting point, and advance **both one step at a time** — after
exactly `a` steps they land together **on the cycle's entry node**. Another O(n)
walk → still **O(n) time, O(1) space**, and no hash set needed.

---

## 6. Two-pointer gap (remove Nth from end) — O(n), O(1), single pass

Naively you'd find the length (one pass) then walk to `length − N` (second pass).
The trick collapses it to **one** pass by fixing a constant **gap** between two
pointers:

```
advance `fast` N steps first:   slow ●            fast ●  (N apart)
then move both together until fast hits the tail:
                                       slow ●      fast ● (END)
```

Because the gap is always exactly N, when `fast` reaches the last node `slow` is
sitting `N` nodes from the end — i.e. **just before** the target. Total movement
is N + (n − N) = **n steps → O(n)**, two pointers → **O(1) space.** A dummy before
the head means even "remove the head" (N == length) leaves `slow` on the dummy
with a valid `slow.next` to unlink.

---

## 7. Merge two sorted lists — O(n+m), O(1), splice don't copy

Walk both lists with a pointer each; repeatedly append the smaller front node to
the result and advance that list. Each node from either list is **looked at and
linked exactly once**, so the work is proportional to the total node count →
**O(n + m) time.** And you **relink existing nodes** rather than allocating new
ones, so it's **O(1) extra space.** The dummy head removes the "is this the first
node appended?" branch — `tail.next = …` is always valid — and `<=` (rather than
`<`) keeps equal elements in their original relative order, i.e. the merge is
**stable**.

---

## 8. Intersection by switching walkers — O(n+m), O(1)

Two lists that share a tail have **different lead-in lengths**. Walk `p` along
list A and `q` along list B; when either runs off the end, **redirect it to the
*other* list's head.** After the switch, both pointers have traversed exactly
`len(A) + len(B)` nodes when they reach the shared region, so they **arrive at the
intersection node simultaneously** (or both hit `None` together if there's no
intersection). One combined pass of n + m steps → **O(n + m) time, O(1) space** —
the length difference is cancelled out automatically, with no counting and no hash
set. (Comparison is by identity `is`, not value `==`: it's the *same node* that's
shared, not merely an equal value.)

---

## Cheat-sheet: which trick gives which bound

| Bound | Trick that produces it |
|-------|------------------------|
| O(n) access/search | no contiguity → no index formula → must hop link by link |
| **O(1)** insert/delete at a known node | rewire 1–2 pointers; nothing shifts (unlike an array) |
| O(1) regardless of where in the list | hold a dummy/sentinel so the head is never a special case |
| O(n) time, **O(1) space** reverse | flip each node's pointer in place; only 3 tracking vars |
| O(n) time, O(n) space reverse | recursion keeps n stack frames live to the tail |
| O(n) find-middle / detect-cycle | fast lapses slow by +1 per step → meet/terminate in ~n |
| O(n) find cycle **start** | algebra `a = k·c − b` ⇒ head-walk meets meeting-point-walk at entry |
| O(n) remove-Nth-from-end, one pass | fix a constant N-gap between two pointers |
| O(n+m) merge / intersection | touch each node once; switch-walkers cancels length diff |
| O(1) space rearrangement | splice/relink existing nodes instead of copying |
