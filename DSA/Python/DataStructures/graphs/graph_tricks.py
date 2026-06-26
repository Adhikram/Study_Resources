"""
Core graph patterns for coding interviews — runnable & self-testing.

Every pattern below is a real, callable function/class (not a stub) with its
time and space complexity, the edge cases it handles, and inline `assert` tests.
Run `python3 graph_tricks.py`; a clean exit means all patterns passed.

Graphs are passed as adjacency lists: Dict[node, List[neighbour]] (or List[(nbr,
weight)] for weighted). See `adjacency_list.py` for an OO Graph class wrapping
these same ideas; this file isolates each algorithm.

Patterns:
    1.  BFS traversal + shortest path (unweighted) with distances
    2.  DFS — recursive and iterative
    3.  Connected components (count)
    4.  Cycle detection — directed (colours / rec-stack) AND undirected (parent)
    5.  Topological sort — Kahn's BFS AND DFS-based
    6.  Dijkstra — shortest path on a weighted graph (heapq)
    7.  Bipartite check — 2-colouring via BFS
    8.  Number of islands — grid DFS/BFS
    9.  Union-Find / DSU — path compression + union by rank (+ component count)
"""

import heapq
from collections import defaultdict, deque
from typing import Dict, List, Optional, Tuple


# ===========================================================================
# 1. BFS — level-order traversal + shortest path on an UNWEIGHTED graph
# ===========================================================================
def bfs_order(adj: Dict[int, List[int]], start: int) -> List[int]:
    """Vertices in BFS (level) order from `start`. Time O(V + E), Space O(V).
    Mark visited WHEN ENQUEUEING (not when dequeueing) to avoid double-adds."""
    visited = {start}
    order: List[int] = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for nbr in adj[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    return order


def bfs_shortest_path(adj: Dict[int, List[int]], start: int) -> Dict[int, int]:
    """Fewest edges from `start` to every reachable vertex. Time O(V + E).
    BFS gives shortest paths on UNWEIGHTED graphs because it explores in order
    of increasing distance. Unreachable vertices are simply absent from the map."""
    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nbr in adj[node]:
            if nbr not in dist:               # first time seen == shortest distance
                dist[nbr] = dist[node] + 1
                queue.append(nbr)
    return dist


# ===========================================================================
# 2. DFS — recursive and iterative
# ===========================================================================
def dfs_recursive(adj: Dict[int, List[int]], start: int) -> List[int]:
    """DFS preorder via recursion. Time O(V + E), Space O(V) (call stack).
    Risk: deep graphs can hit Python's recursion limit -> use the iterative form."""
    visited: set = set()
    order: List[int] = []

    def visit(node: int) -> None:
        visited.add(node)
        order.append(node)
        for nbr in adj[node]:
            if nbr not in visited:
                visit(nbr)

    visit(start)
    return order


def dfs_iterative(adj: Dict[int, List[int]], start: int) -> List[int]:
    """DFS using an explicit stack. Time O(V + E), Space O(V).
    Mark visited WHEN POPPING (a node can be pushed multiple times before it's
    first popped, so check-on-pop keeps the order correct)."""
    visited: set = set()
    order: List[int] = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # push reversed so the first neighbour is processed first (matches recursion)
        for nbr in reversed(adj[node]):
            if nbr not in visited:
                stack.append(nbr)
    return order


# ===========================================================================
# 3. CONNECTED COMPONENTS — count islands of an UNDIRECTED graph
# ===========================================================================
def count_components(n: int, edges: List[Tuple[int, int]]) -> int:
    """Number of connected components over vertices 0..n-1. Time O(V + E).
    Run a flood-fill from every unvisited vertex; each fill is one component."""
    adj: Dict[int, List[int]] = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited: set = set()

    def flood(start: int) -> None:
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            stack.extend(adj[node])

    components = 0
    for v in range(n):
        if v not in visited:
            components += 1            # a brand-new component
            flood(v)
    return components


# ===========================================================================
# 4. CYCLE DETECTION
# ===========================================================================
def has_cycle_directed(adj: Dict[int, List[int]], n_vertices: List[int]) -> bool:
    """Cycle detection in a DIRECTED graph via 3-colour DFS.
    Time O(V + E). WHITE=unseen, GREY=on the current DFS path, BLACK=finished.
    An edge to a GREY node = a back edge = a cycle. (A back edge to a BLACK node
    is fine — that subtree is already fully explored.)"""
    WHITE, GREY, BLACK = 0, 1, 2
    color = {v: WHITE for v in n_vertices}

    def visit(node: int) -> bool:
        color[node] = GREY
        for nbr in adj[node]:
            if color.get(nbr, WHITE) == GREY:
                return True            # back edge into the active path -> cycle
            if color.get(nbr, WHITE) == WHITE and visit(nbr):
                return True
        color[node] = BLACK
        return False

    return any(color[v] == WHITE and visit(v) for v in n_vertices)


def has_cycle_undirected(n: int, edges: List[Tuple[int, int]]) -> bool:
    """Cycle detection in an UNDIRECTED graph via DFS with a PARENT check.
    Time O(V + E). Going back to the node you just came from is NOT a cycle;
    reaching any OTHER already-visited node IS. (Self-loop counts as a cycle.)"""
    adj: Dict[int, List[int]] = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited: set = set()

    def visit(node: int, parent: int) -> bool:
        visited.add(node)
        for nbr in adj[node]:
            if nbr == node:
                return True            # self-loop
            if nbr not in visited:
                if visit(nbr, node):
                    return True
            elif nbr != parent:        # visited & not where we came from -> cycle
                return True
        return False

    return any(v not in visited and visit(v, -1) for v in range(n))


# ===========================================================================
# 5. TOPOLOGICAL SORT — only valid on a DAG (directed acyclic graph)
# ===========================================================================
def topo_sort_kahn(n: int, edges: List[Tuple[int, int]]) -> Optional[List[int]]:
    """Kahn's algorithm (BFS on in-degrees). Time O(V + E).
    Repeatedly emit a vertex with in-degree 0. If we can't emit all V vertices,
    a cycle exists -> return None (no valid ordering)."""
    adj: Dict[int, List[int]] = defaultdict(list)
    in_deg = [0] * n
    for u, v in edges:
        adj[u].append(v)
        in_deg[v] += 1

    queue = deque(v for v in range(n) if in_deg[v] == 0)
    order: List[int] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nbr in adj[node]:
            in_deg[nbr] -= 1           # "remove" node's outgoing edges
            if in_deg[nbr] == 0:
                queue.append(nbr)

    return order if len(order) == n else None   # short order => cycle


def topo_sort_dfs(n: int, edges: List[Tuple[int, int]]) -> Optional[List[int]]:
    """DFS-based topological sort. Time O(V + E).
    A vertex is pushed onto the output AFTER all its descendants finish; reverse
    that post-order. Uses 3-colour cycle detection to return None on a cycle."""
    adj: Dict[int, List[int]] = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    WHITE, GREY, BLACK = 0, 1, 2
    color = [WHITE] * n
    order: List[int] = []

    def visit(node: int) -> bool:
        color[node] = GREY
        for nbr in adj[node]:
            if color[nbr] == GREY:
                return False           # cycle
            if color[nbr] == WHITE and not visit(nbr):
                return False
        color[node] = BLACK
        order.append(node)             # finished -> safe to append (reverse later)
        return True

    for v in range(n):
        if color[v] == WHITE and not visit(v):
            return None
    return order[::-1]                 # reverse post-order = topological order


# ===========================================================================
# 6. DIJKSTRA — shortest path on a NON-NEGATIVE weighted graph (heapq)
# ===========================================================================
def dijkstra(adj: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """Shortest distances from `start` over edges (neighbour, weight) >= 0.
    Time O((V + E) log V) with a binary heap. Space O(V).
    Lazy deletion: we push improved distances and skip stale heap entries when
    popped. Negative weights would break this — use Bellman-Ford instead."""
    dist = {start: 0}
    heap: List[Tuple[int, int]] = [(0, start)]   # (distance, vertex)
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float("inf")):
            continue                   # stale entry — a better distance was found
        for nbr, w in adj[node]:
            nd = d + w
            if nd < dist.get(nbr, float("inf")):
                dist[nbr] = nd
                heapq.heappush(heap, (nd, nbr))
    return dist


# ===========================================================================
# 7. BIPARTITE CHECK — 2-colour the graph with BFS
# ===========================================================================
def is_bipartite(n: int, edges: List[Tuple[int, int]]) -> bool:
    """True if the UNDIRECTED graph can be 2-coloured (no edge joins same colour).
    Time O(V + E). BFS each component, colouring neighbours the opposite colour;
    a neighbour already coloured the SAME colour means an odd cycle -> not bipartite."""
    adj: Dict[int, List[int]] = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    color: Dict[int, int] = {}
    for start in range(n):
        if start in color:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for nbr in adj[node]:
                if nbr not in color:
                    color[nbr] = color[node] ^ 1   # flip 0<->1
                    queue.append(nbr)
                elif color[nbr] == color[node]:
                    return False        # same colour on both ends -> odd cycle
    return True


# ===========================================================================
# 8. NUMBER OF ISLANDS — grid as an implicit graph (DFS flood fill)
# ===========================================================================
def num_islands(grid: List[List[str]]) -> int:
    """Count connected groups of '1's (4-directionally) in a grid. Time O(rows*cols).
    Each cell is a vertex; edges connect orthogonal neighbours. Sink each island
    by flipping visited land to '0' so it isn't counted twice."""
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])

    def sink(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"               # mark visited in place
        sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                sink(r, c)
    return islands


# ===========================================================================
# 9. UNION-FIND / DSU — path compression + union by rank
# ===========================================================================
class UnionFind:
    """Disjoint Set Union. find/union are near-O(1) amortized (inverse Ackermann
    α(n)) thanks to path compression + union by rank. Space O(V).
    Great for: connected components, cycle detection in undirected graphs,
    Kruskal's MST, "redundant connection"."""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))   # each node starts as its own root
        self.rank = [0] * n            # tree height upper bound
        self.count = n                 # number of disjoint sets

    def find(self, x: int) -> int:
        """Root of x's set, compressing the path on the way up. ~O(α(n))."""
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:  # path compression: point everyone at root
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a: int, b: int) -> bool:
        """Merge the sets of a and b. Returns False if they were ALREADY joined
        (i.e. this edge would create a cycle). Attaches the shorter tree under
        the taller one (union by rank) to keep trees flat."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False               # already connected -> redundant edge
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True


def redundant_connection(n: int, edges: List[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
    """First edge that closes a cycle in an undirected graph (vertices 1..n), via
    DSU. Time ~O(E·α). Returns None if the graph stays a forest."""
    uf = UnionFind(n + 1)              # +1 so we can index by 1..n directly
    for u, v in edges:
        if not uf.union(u, v):         # union failed -> u,v already connected
            return (u, v)
    return None


# ===========================================================================
# TESTS — run via main(); cover normal + edge cases
# ===========================================================================
def _test() -> None:
    # Shared sample (undirected) graph:  1-2, 1-3, 2-4, 3-4
    und: Dict[int, List[int]] = defaultdict(list)
    for u, v in [(1, 2), (1, 3), (2, 4), (3, 4)]:
        und[u].append(v)
        und[v].append(u)

    # 1. BFS order + shortest path
    assert bfs_order(und, 1)[0] == 1
    assert set(bfs_order(und, 1)) == {1, 2, 3, 4}
    d = bfs_shortest_path(und, 1)
    assert d == {1: 0, 2: 1, 3: 1, 4: 2}
    assert bfs_shortest_path({1: [2], 2: [], 3: []}, 1) == {1: 0, 2: 1}   # 3 unreachable

    # 2. DFS recursive == iterative (set of nodes); preorder starts at root
    assert dfs_recursive(und, 1)[0] == 1
    assert set(dfs_recursive(und, 1)) == {1, 2, 3, 4}
    assert set(dfs_iterative(und, 1)) == {1, 2, 3, 4}

    # 3. connected components
    assert count_components(5, [(0, 1), (1, 2), (3, 4)]) == 2     # {0,1,2} {3,4}
    assert count_components(3, []) == 3                          # all isolated
    assert count_components(1, []) == 1

    # 4. cycle detection
    dag = {1: [2], 2: [3], 3: []}
    assert has_cycle_directed(dag, [1, 2, 3]) is False
    cyc = {1: [2], 2: [3], 3: [1]}
    assert has_cycle_directed(cyc, [1, 2, 3]) is True
    assert has_cycle_undirected(3, [(0, 1), (1, 2), (2, 0)]) is True
    assert has_cycle_undirected(3, [(0, 1), (1, 2)]) is False     # tree, no cycle
    assert has_cycle_undirected(1, [(0, 0)]) is True              # self-loop

    # 5. topological sort (both methods); cycle => None
    edges_dag = [(0, 1), (0, 2), (1, 3), (2, 3)]
    for topo in (topo_sort_kahn(4, edges_dag), topo_sort_dfs(4, edges_dag)):
        assert topo is not None
        pos = {v: i for i, v in enumerate(topo)}
        for u, v in edges_dag:                # u must precede v in the order
            assert pos[u] < pos[v]
    assert topo_sort_kahn(2, [(0, 1), (1, 0)]) is None            # cycle
    assert topo_sort_dfs(2, [(0, 1), (1, 0)]) is None

    # 6. Dijkstra (weighted)
    w: Dict[int, List[Tuple[int, int]]] = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [],
    }
    assert dijkstra(w, 0) == {0: 0, 2: 1, 1: 3, 3: 4}            # 0->2->1->3 = 4
    assert dijkstra({0: [], 1: []}, 0) == {0: 0}                 # isolated start

    # 7. bipartite
    assert is_bipartite(4, [(0, 1), (1, 2), (2, 3), (3, 0)]) is True     # even cycle
    assert is_bipartite(3, [(0, 1), (1, 2), (2, 0)]) is False            # odd cycle
    assert is_bipartite(2, []) is True                                   # no edges

    # 8. number of islands
    grid = [
        ["1", "1", "0", "0"],
        ["1", "0", "0", "1"],
        ["0", "0", "0", "1"],
        ["1", "0", "0", "0"],
    ]
    # islands: {(0,0),(0,1),(1,0)}, {(1,3),(2,3)}, {(3,0)} -> 3
    assert num_islands(grid) == 3
    assert num_islands([]) == 0
    assert num_islands([["0", "0"], ["0", "0"]]) == 0

    # 9. union-find / DSU
    uf = UnionFind(5)
    uf.union(0, 1); uf.union(1, 2); uf.union(3, 4)
    assert uf.find(0) == uf.find(2)
    assert uf.find(0) != uf.find(3)
    assert uf.count == 2                          # two components remain
    assert uf.union(0, 2) is False                # already joined
    assert redundant_connection(3, [(1, 2), (2, 3), (1, 3)]) == (1, 3)
    assert redundant_connection(3, [(1, 2), (2, 3)]) is None


def main() -> None:
    _test()
    print("graph_tricks.py: all 9 patterns verified ✔")


if __name__ == "__main__":
    main()
