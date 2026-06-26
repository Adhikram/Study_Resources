# Complexity — the *why* behind the Big-O (graphs)

The number (`O(V + E)`, `O((V+E) log V)`, ...) is the answer. This file is the
**reasoning trick** that produces it — the mental model that lets you derive the
complexity in an interview instead of memorizing it. Each entry names the trick,
then proves it.

Two reasoning tools cover almost everything here:

1. **Charging / aggregate argument** — "each vertex is processed once and each
   edge is examined a constant number of times *total*, so summing the work over
   the whole run gives V + E, not V·E." Used for BFS, DFS, topological sort.
2. **Amortized analysis** — "an individual operation is occasionally expensive,
   but averaged (or with the right auxiliary structure) it's cheap." Used for
   union-find's near-constant operations.

If you can spot which applies, you can derive the bound yourself.

> Notation: **V** = number of vertices, **E** = number of edges. "Sparse" means
> E ≈ V; "dense" means E ≈ V². The runnable algorithms these bounds describe live
> in `graph_tricks.py` and `adjacency_list.py`.

---

## 1. BFS / DFS are O(V + E) — the charging argument

Both traversals do the same accounting; only the order differs (queue vs stack).

**Trick — charge the work to vertices and edges separately, then add.**

- **Each vertex is enqueued/pushed and dequeued/popped exactly once.** The
  `visited` set guarantees a vertex is never processed twice. That's `V` units
  of "per-vertex" work.
- **Each edge is examined exactly once** (directed) or **twice** (undirected,
  once from each endpoint). When we pop a vertex `u` we scan its whole adjacency
  list — and across the entire run, the sum of all adjacency-list lengths is
  exactly the number of edge-endpoints = `E` (or `2E` undirected). That's the
  "per-edge" work.

Add them: `O(V) + O(E) = O(V + E)`.

### Why V + E and NOT V·E
The tempting wrong analysis: "for each of V vertices we scan up to V neighbours →
V·V = V²." That over-counts. A vertex `u` doesn't have V neighbours — it has
`deg(u)` neighbours, and **the degrees sum to 2E, not V²** (handshake lemma). You
only do work proportional to edges that actually exist. So the cost is tied to
`E` (the real edges), giving `V + E`. On a dense graph where `E ≈ V²` the two
*coincide* (`V + E ≈ V²`), which is exactly why the adjacency-matrix version,
forced to scan all V potential neighbours per vertex, is `O(V²)` regardless of
how few edges exist.

> The `V` term matters on its own: you must touch isolated vertices and separate
> components too, so even an edgeless graph is `O(V)`.

---

## 2. Adjacency list O(V + E) space vs matrix O(V²) — and when each wins

- **Adjacency list** stores, per vertex, only its actual neighbours. Total
  storage = V vertex entries + one slot per edge-endpoint = `O(V + E)`.
- **Adjacency matrix** is a V×V grid of 0/1 (or weights). It reserves a cell for
  *every possible* edge whether or not it exists → `O(V²)` always.

**When each wins:**

| | Adjacency list | Adjacency matrix |
|---|---|---|
| Space | O(V + E) — great when sparse | O(V²) — wasteful when sparse |
| "Is there an edge u→v?" | O(deg(u)) scan | **O(1)** direct lookup |
| Iterate neighbours of u | O(deg(u)) — only real ones | O(V) — must scan a whole row |
| Best for | sparse graphs (most interview graphs) | dense graphs, or constant-time edge queries |

**Trick to decide:** if `E ≪ V²` (sparse — roads, social graphs, trees) use a
list; if the graph is dense or you do many "edge exists?" probes, the matrix's
O(1) lookup earns its O(V²) space.

---

## 3. Dijkstra with a binary heap is O((V + E) log V)

Dijkstra repeatedly pulls the *closest* unsettled vertex, then relaxes its edges.
The heap is what makes "find the closest" cheap. Account for both heap operations:

- **Pops:** each vertex is settled once, so we pop it once. With lazy deletion we
  may push a vertex several times, but the heap holds at most `O(E)` entries, and
  each `heappop` is `O(log(heap size)) = O(log V)` (since the number of distinct
  vertices is V, `log E ≤ log V² = 2 log V = O(log V)`). Total pops:
  `O((V + E) log V)`.
- **Pushes (relaxations):** every edge can trigger at most one improving push,
  and each `heappush` is `O(log V)`. Across all `E` edges: `O(E log V)`.

Add them: **`O((V + E) log V)`**.

**Trick:** the `log V` factor is *entirely* the heap's price for ordering by
distance. Replace the binary heap with a Fibonacci heap and relaxations become
amortized O(1), giving `O(E + V log V)`; replace it with a plain array scan for
the min and you get `O(V²)` (better than the heap on dense graphs!). The data
structure picks the bound. Note Dijkstra requires **non-negative weights** — the
"settle each vertex once" assumption breaks otherwise (use Bellman-Ford, `O(VE)`).

---

## 4. Topological sort is O(V + E) — it's just a guided traversal

Both algorithms visit each vertex and edge a constant number of times.

- **Kahn's (BFS on in-degrees):** computing all in-degrees scans every edge once
  → `O(E)`. Then each vertex is enqueued once (when its in-degree hits 0) and, on
  dequeue, we decrement once per outgoing edge — again every edge touched once →
  `O(V + E)`.
- **DFS-based:** it *is* a DFS (`O(V + E)`) with an O(1) append on each vertex's
  finish; reversing the finish-order list is `O(V)`.

**Trick:** topo sort doesn't add any new dominant work on top of a traversal —
the ordering falls out of the order vertices are *finished* (DFS) or *freed*
(Kahn). Same charging argument as §1 → `O(V + E)`. The "cycle ⇒ no ordering"
check is free: Kahn notices it emitted fewer than V vertices; DFS notices a back
edge to a GREY node.

---

## 5. Union-Find is near-O(1) amortized — α(n), the inverse Ackermann

A naive DSU where `find` walks to the root and `union` links arbitrarily can
build a tall chain, making `find` O(n). Two optimizations together flatten it:

- **Union by rank** — always attach the *shorter* tree under the *taller* one.
  Alone, this caps tree height at `O(log n)` (rank only increases when two equal
  ranks merge, so rank r needs ≥ 2ʳ nodes).
- **Path compression** — during `find`, re-point every node on the path directly
  at the root. This permanently shortens future lookups for those nodes.

**Trick — combined, the amortized cost per operation is `O(α(n))`**, where α is
the *inverse Ackermann* function. α grows so slowly that `α(n) ≤ 4` for any `n`
that fits in the observable universe, so each `find`/`union` is **effectively
constant**. The intuition: union-by-rank keeps trees from getting tall, and path
compression "pays forward" by amortizing the cost of one deep walk across all the
nodes it just hoisted to the root — no single later operation re-pays that cost.

So `m` operations over `n` elements cost `O(m · α(n)) ≈ O(m)`. That's why DSU is
the go-to for connected-components, undirected cycle detection, Kruskal's MST,
and "redundant connection".

---

## 6. Grid problems (number of islands) — O(rows × cols)

A grid is an *implicit* graph: each cell is a vertex, edges join the ≤4
orthogonal neighbours. So `V = rows·cols` and `E ≤ 4V` (a constant per cell).
Plugging into the BFS/DFS bound `O(V + E) = O(V + 4V) = O(V)` = **O(rows·cols)**:
every cell is visited once (then sunk/marked so it isn't revisited), and each
visit looks at a constant 4 neighbours. The "graph algorithm in disguise" trick:
recognize the grid as a graph and the `O(V + E)` charging argument applies
directly.

---

## Cheat-sheet: which trick gives which bound

| Bound | Trick that produces it |
|-------|------------------------|
| O(V + E) BFS/DFS | each vertex processed once + each edge scanned once → V + E (not V·E) |
| O(V) (edgeless / per-vertex) | must still touch every vertex & component |
| O(V²) matrix space / matrix traversal | a cell per *possible* edge; scan whole row for neighbours |
| O(V + E) space (list) | store only real edges; degrees sum to 2E |
| O((V + E) log V) Dijkstra | heap orders by distance: V+E ops × O(log V) per heap op |
| O(V + E) topological sort | a traversal in disguise; order falls out of finish/free order |
| ~O(1) amortized union-find | union by rank caps height + path compression amortizes → α(n) ≤ 4 |
| O(rows·cols) grid flood fill | implicit graph, V = cells, E = O(V) → O(V) |
