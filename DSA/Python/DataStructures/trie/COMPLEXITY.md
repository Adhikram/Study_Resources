# Complexity — the *why* behind the Big-O

The number (`O(m)`, `O(p)`, ...) is the answer. This file is the **reasoning
trick** that produces it — the mental model that lets you derive trie complexity
in an interview instead of memorizing it. Each entry names the trick, then
proves it.

Notation used throughout:

- `m` = length of the word being inserted/searched.
- `p` = length of a prefix being queried.
- `N` = number of words stored.
- `M` = length of the longest word.
- `ALPHABET` = number of distinct characters possible at a node (26 for `a–z`).

The one idea that unlocks almost everything here: **a trie indexes by character
position, so work is proportional to the LENGTH of the string you touch, never
to how many strings are stored.** Hold onto that and the bounds fall out.

---

## 1. `insert` / `search` / `starts_with` are O(m) — one step per character

To insert or look up a word you walk the trie **one node per character**: at
each step you do an O(1) dict lookup/insert on `node.children[ch]` and move down.
A word of length `m` is therefore exactly `m` steps of O(1) work → **O(m)**.

**The key advantage — and the thing to say out loud in an interview:** this cost
is *independent of `N`*, the number of words already stored. A hash set's lookup
is O(m) too (you must hash the whole string), but the trie buys you something the
hash set cannot: every *prefix* of that walk is also answered for free. Searching
"apple" already visited the nodes for "a", "ap", "app", "appl" — so prefix
queries are essentially free side effects of the same walk.

`search` vs `starts_with` cost the *same* (both O(m)); they differ only in the
final check: `search` additionally requires `node.is_end` to be set, while
`starts_with` only requires the node to *exist*. That single boolean is the
difference between "this is a stored word" and "this is merely a prefix of one."

---

## 2. Prefix queries are O(p) — and that's why a trie beats scanning N words

"How many / which stored words start with `pre`?" In a flat list/array you must
examine **every** word and test `word.startswith(pre)`: that's `N` comparisons of
up to `p` characters → **O(N·M)**. In a trie you walk straight to the prefix node
in **O(p)**, and everything in that node's subtree is exactly the set of words
with that prefix — no scanning of unrelated words at all.

**Trick — the structure pre-groups words by shared prefix.** Words that share a
prefix share the *same path of nodes*, so reaching the prefix node already
isolates the answer set. If you also cache a `count` on each node (incremented on
every insert that passes through), `count_words_with_prefix` becomes a single
O(p) walk with **no subtree traversal at all** — the answer is sitting on the
node. This O(p)-vs-O(N·M) gap is the entire reason tries exist for autocomplete,
dictionaries, and "words with prefix" problems.

---

## 3. Space is O(ALPHABET · N · M) worst case — and prefix sharing shrinks it

The worst case stores `N` words of length up to `M` with **no shared prefixes**:
every word is its own root-to-leaf chain, so you have up to `N·M` nodes, and each
node's children map can hold up to `ALPHABET` entries → **O(ALPHABET · N · M)**.

**Trick — sharing prefixes collapses the front of every chain into one path.**
The moment words overlap ("car", "card", "care", "cart" all share "car"), those
shared characters cost *one* set of nodes instead of one per word. So the more
your dataset clusters around common prefixes (English words, URLs, file paths),
the further real usage drops below the worst case. A dict-based `children` (used
in this folder) also avoids reserving `ALPHABET` empty slots per node — you only
pay for children that actually exist, so practical space tracks the number of
*distinct edges*, not `ALPHABET · nodes`.

---

## 4. Wildcard search is O(b^w · m) — every '.' forks the DFS

In `WordDictionary.search`, a literal character follows exactly one child (O(1)
per level → O(m) total, same as a normal search). A `.` wildcard, however, must
try **every** child, turning the walk into a DFS.

**Trick — count the branching.** Each `.` multiplies the number of live search
paths by the branching factor `b` at that node (up to `ALPHABET`). With `w`
wildcards the DFS explores up to `b^w` paths, each of length `m` → **O(b^w · m)**.
A query of all wildcards (`"...."`) is the worst case: it visits every node at
that depth. With zero wildcards it collapses back to plain **O(m)**. This is why
"how many wildcards?" is the question that determines the bound.

---

## 5. Word Search II — trie turns "search W words" into one shared grid DFS

Searching each of `W` words on an `R×C` board independently is
`O(W · R · C · 4^L)`. Building a trie of the words and DFS-ing the board **once**,
walking the trie in lockstep, shares all the common prefixes across words.

**Trick — prune the instant no word can extend the path.** At each grid step you
descend `node.children[cell]`; if that child doesn't exist, **no dictionary word
starts with the current path**, so you abandon the branch immediately instead of
exploring it for every word separately. The board DFS is the cost
(`O(R · C · 4^maxlen)` worst case) and the trie is the filter that keeps you from
walking dead branches — the `W` factor disappears because all words are tested
simultaneously by one traversal.

---

## 6. Binary trie XOR — exactly 32 steps, so O(n), not O(n²)

Maximum-XOR-of-two-numbers brute force tries every pair → **O(n²)**. The binary
trie stores each number as its fixed-width bit string (MSB→LSB) and, for each
number, **greedily walks the opposite bit** at every level to maximize the
running XOR.

**Trick — fixed width makes depth a constant, not a variable.** A 32-bit integer
is *always* a path of exactly 32 nodes, so insert is 32 steps and each query is
32 steps — both O(1) in `n` terms. Inserting `n` numbers is `O(32·n)` and
querying all `n` is `O(32·n)` → **O(n) overall.** At each bit, taking the
opposite branch (if it exists) sets that bit in the XOR — the highest bit you can
flip dominates, which is why greedy MSB-first is optimal. The "constant" 32 is
the whole reason an O(n²) pairwise problem becomes linear.

---

## Cheat-sheet: which trick gives which bound

| Bound | Trick that produces it |
|-------|------------------------|
| `insert/search/starts_with` = O(m) | one O(1) node step per character; cost is independent of N |
| prefix query = O(p), beats O(N·M) scan | shared-prefix paths pre-group words; cached `count` answers without traversal |
| space = O(ALPHABET·N·M) worst case | one chain per word with no sharing; dict children + prefix sharing shrink it in practice |
| wildcard search = O(b^w · m) | each '.' forks the DFS into every child (branching factor `b`, `w` times) |
| Word Search II shared DFS | trie prunes a grid branch the instant no word extends it — drops the per-word factor |
| binary-trie XOR = O(n) | every number is a fixed 32-step path; greedy opposite-bit walk replaces O(n²) pairing |
