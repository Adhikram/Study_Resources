# Graphs — Complete Interview Prep Guide

A single place to revise everything about graphs for coding interviews: how they
work, the three ways to represent them, what every operation costs, the edge
cases that break solutions, and the core patterns with runnable, tested code.

> All `.py` files here are **runnable and self-testing**. Run any of them
> directly (`python3 graph_tricks.py`) — they execute `assert`-based tests and
> print a short demo. If a file runs without raising, every example passed.

---

## Files in this folder

| File | What it covers |
|------|----------------|
| `adjacency_list.py` | A complete, runnable `Graph` class (directed/undirected): add/remove, BFS, DFS, path-finding, cycle detection |
| `fundamentals.py`   | Build adjacency list/matrix/edge-list, convert between them, degree counting, neighbour iteration, gotchas |
| `graph_tricks.py`   | The 9 core graph patterns, each runnable with inline `assert` tests |
| `edge_cases.py`     | A concrete, runnable edge-case checklist (empty/disconnected/self-loop/cycle-vs-DAG/...) |
| `COMPLEXITY.md`     | The *why* behind every Big-O here — the reasoning/trick that derives it |
| `README.md`         | This guide — fundamentals, complexity tables, checklists, pattern index |

---

## 1. What is a graph?

A **graph** `G = (V, E)` is a set of **vertices** (nodes) `V` connected by
**edges** `E`. It models *relationships*: roads between cities, friendships,
task dependencies, web links.

### Flavours
- **Undirected** — edge `u — v` goes both ways (friendship). Stored both ways.
- **Directed (digraph)** — edge `u → v` is one-way (a Twitter follow, a task
  dependency). The reverse edge is separate and may not exist.
- **Weighted** — each edge carries a cost/distance (road length, latency).
- **Unweighted** — every edge is "1 hop".

### Terminology (memorize)
- **Vertex / node** — a point in the graph.
- **Edge** — a connection between two vertices.
- **Degree** — number of edges incident to a vertex. Directed graphs split this
  into **in-degree** (edges pointing in) and **out-degree** (edges pointing out).
  A **self-loop** counts twice toward an undirected degree.
- **Path** — a sequence of vertices connected by edges. **Simple path** repeats
  no vertex.
- **Cycle** — a path that starts and ends at the same vertex.
- **Connected** — (undirected) every vertex is reachable from every other. A
  maximal connected piece is a **connected component**.
- **DAG** — Directed Acyclic Graph: directed with no cycles. The *only* kind of
  directed graph that has a valid **topological ordering**.
- **Tree** — a connected, acyclic undirected graph with exactly `V − 1` edges.

See `adjacency_list.py` for an OO `Graph` you can instantiate and play with.

---

## 2. The three representations

| Representation | Stores | Space | "Edge u→v exists?" | Iterate neighbours of u |
|----------------|--------|-------|--------------------|--------------------------|
| **Adjacency list** | per vertex, a collection of its neighbours | **O(V + E)** | O(deg(u)) | **O(deg(u))** (only real ones) |
| **Adjacency matrix** | a V×V grid, `M[u][v]=1` if edge | **O(V²)** | **O(1)** | O(V) (scan a whole row) |
| **Edge list** | a flat list of `(u, v)` pairs | O(E) | O(E) | O(E) |

```python
# Adjacency list (the interview default — sparse-friendly, fast neighbour scans)
adj = {0: [1, 2], 1: [2], 2: []}

# Adjacency matrix (dense graphs, or O(1) edge-existence checks)
mat = [[0, 1, 1],
       [0, 0, 1],
       [0, 0, 0]]

# Edge list (simplest input format; feed it to Kruskal's / union-find directly)
edges = [(0, 1), (0, 2), (1, 2)]
```

**Tradeoff in one line:** use an **adjacency list** by default (most graphs are
sparse, `E ≪ V²`); reach for the **matrix** only when the graph is dense or you
need O(1) "is there an edge?" lookups; the **edge list** is the natural input
form and what union-find / Kruskal's consume.

`fundamentals.py` builds all three and converts between them.

---

## 3. Operation complexity (memorize this table)

Bounds assume an **adjacency list** unless noted. `V` = vertices, `E` = edges.

| Operation | Time | Notes |
|-----------|------|-------|
| Add vertex | O(1) | |
| Add edge | O(1) | append to a list (undirected: two appends) |
| Remove edge | O(deg) or O(1) | O(1) with a set adjacency (`adjacency_list.py`) |
| Remove vertex | O(V + E) | must scrub it from every neighbour list |
| "Edge u→v exists?" | O(deg(u)) list / **O(1)** matrix or set | |
| Iterate neighbours of u | O(deg(u)) | |
| **BFS / DFS** (full traversal) | **O(V + E)** | each vertex once, each edge once |
| Connected components | O(V + E) | flood-fill from each unvisited vertex |
| Cycle detection | O(V + E) | colours (directed) / parent (undirected) |
| **Topological sort** | O(V + E) | Kahn's BFS or DFS post-order |
| **Dijkstra** (binary heap) | **O((V + E) log V)** | non-negative weights only |
| Bipartite check | O(V + E) | BFS 2-colouring |
| Union-Find `find` / `union` | **~O(α(n)) ≈ O(1)** | amortized; path compression + rank |

**Space:** adjacency list O(V + E); adjacency matrix O(V²); BFS/DFS use O(V)
auxiliary (visited set + queue/stack/recursion).

> Want the *reasoning* behind these numbers (why BFS is O(V + E) not O(V·E), why
> Dijkstra carries a `log V`, why union-find is effectively O(1))? See
> **`COMPLEXITY.md`** — it derives each bound from the trick that produces it.

---

## 4. Edge-case checklist (run through this for EVERY graph problem)

Before coding, ask / handle (`edge_cases.py` proves each one):

- [ ] **Empty graph** — no vertices/edges; traversal should return empty, not crash.
- [ ] **Single vertex, no edges** — reachable set is just itself; degree 0.
- [ ] **Disconnected graph** — BFS/DFS from one node MISSES other components; to
      cover all, loop over every vertex.
- [ ] **Self-loop** (`v — v`) — must not loop forever (visited set); counts as a cycle.
- [ ] **Parallel / duplicate edges** — a list adjacency keeps them (inflates degree
      & revisits); a set adjacency dedupes. Pick deliberately.
- [ ] **Cycle vs DAG for topological sort** — a cycle has NO valid order; detect
      "fewer than V emitted" and return `None`.
- [ ] **Directed vs undirected cycle detection** — different rules! Undirected
      must ignore the edge back to the *parent*, or it false-positives on a tree.
- [ ] **Unreachable target** — there may be no path; return a sentinel (`-1`/`None`/`inf`).
- [ ] **Negative edge weights** — break Dijkstra; use Bellman-Ford.
- [ ] **Disconnected components in topo sort / bipartite** — start from every vertex.
- [ ] **Vertex labels** — are they `0..n-1` integers (matrix-friendly) or arbitrary
      (strings) needing a `dict`/index map?
- [ ] **Deep / large graph** — recursion may hit Python's limit; use iterative BFS/DFS.

### Clarifying questions to ask the interviewer
- Directed or undirected? Weighted? Can weights be negative?
- Are there self-loops or parallel edges? Is the graph connected?
- How are vertices labelled (`0..n-1` or arbitrary)? How big is V and E?
- What do I return when there's no path / no valid ordering?
- May I mutate the input (e.g. sink cells in "number of islands")?

---

## 5. Pattern index (see `graph_tricks.py`)

| Pattern | When to reach for it | Typical complexity |
|---------|----------------------|--------------------|
| **BFS traversal + shortest path** | level order; fewest-edges path on UNWEIGHTED graph | O(V + E) |
| **DFS (recursive / iterative)** | explore deep, path existence, backtracking, post-order | O(V + E) |
| **Connected components** | count islands of an undirected graph | O(V + E) |
| **Cycle detection (directed)** | "does this digraph have a cycle?", deadlock detection | O(V + E) |
| **Cycle detection (undirected)** | "does this graph contain a loop?" (parent-aware) | O(V + E) |
| **Topological sort** | order tasks with dependencies; only on a DAG | O(V + E) |
| **Dijkstra** | shortest path with NON-NEGATIVE weights | O((V + E) log V) |
| **Bipartite check (2-colour)** | "can nodes split into two conflict-free groups?" | O(V + E) |
| **Number of islands (grid)** | connected regions in a 2-D grid | O(rows·cols) |
| **Union-Find / DSU** | dynamic connectivity, undirected cycle, Kruskal's MST | ~O(α(n)) per op |

---

## 6. Decision guide — "which algorithm?"

```
What are you asked for?
├── Shortest path / fewest hops?
│   ├── Unweighted (or all weights equal)?   → BFS  (O(V + E))
│   ├── Weighted, all weights ≥ 0?           → Dijkstra  (O((V+E) log V))
│   └── Weighted, negative edges?            → Bellman-Ford  (O(V·E))
├── Just need to visit / reach / path-exists? → DFS or BFS
├── Order tasks with dependencies?           → Topological sort (DAG only)
├── Count / merge groups, dynamic "are u,v connected?" → Union-Find (DSU)
├── Detect a cycle?
│   ├── Directed graph?                        → DFS 3-colour / rec-stack
│   └── Undirected graph?                      → DFS with parent, or Union-Find
├── Two-group / conflict partition?           → Bipartite 2-colouring (BFS)
└── Connected regions in a grid?              → DFS/BFS flood fill
```

**BFS vs DFS in one line:** BFS finds the *shortest unweighted path* and explores
by levels (queue); DFS goes *deep first* (stack/recursion) and is natural for
cycle detection, topological order, and connectivity.

---

## 7. Python idioms worth knowing (interview-friendly)

```python
from collections import defaultdict, deque
import heapq

adj = defaultdict(list)            # auto-creates [] for a new key — no KeyError
for u, v in edges:                 # build an undirected adjacency list
    adj[u].append(v)
    adj[v].append(u)               # BOTH ways — the classic undirected gotcha

visited = set()                    # the loop-breaker: each vertex processed once
queue = deque([start])             # BFS frontier; popleft() is O(1) (a list isn't!)
node = queue.popleft()
queue.append(nbr)

stack = [start]                    # iterative DFS — avoids recursion-limit crashes
node = stack.pop()

heap = [(0, start)]                # Dijkstra: (distance, vertex) min-heap
d, node = heapq.heappop(heap)
heapq.heappush(heap, (nd, nbr))

color[nbr] = color[node] ^ 1       # bipartite: flip 0<->1
float('inf')                       # sentinel for "no path yet" distances
```

See `fundamentals.py` for the full, runnable set of build/convert/degree
operations and gotchas, and `graph_tricks.py` for every pattern above as tested,
callable code.
