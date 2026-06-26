"""
Graph fundamentals for interviews — representations & basic operations.

Covers the three ways to store a graph (adjacency list, adjacency matrix, edge
list), how to build them for directed AND undirected graphs, how to convert
between them, and how to count degrees / iterate neighbours. Each section is
runnable and verified with `assert`s. Run `python3 fundamentals.py` — if it
exits cleanly, every example behaved as documented.

A GRAPH is a set of vertices (nodes) connected by edges. Edges may be:
- DIRECTED (u -> v, one way) or UNDIRECTED (u -- v, both ways),
- WEIGHTED (each edge carries a cost) or unweighted.

The adjacency LIST (vertex -> collection of neighbours) is the default for
interviews: O(V + E) space and O(1) neighbour iteration on sparse graphs. See
the full runnable Graph class in `adjacency_list.py`; this file shows the raw
building blocks behind it.
"""

from collections import defaultdict
from typing import Dict, List, Set, Tuple


# ---------------------------------------------------------------------------
# 1. Build an adjacency list (defaultdict) — UNDIRECTED
#    Space O(V + E). The #1 gotcha: an undirected edge must be added BOTH ways.
# ---------------------------------------------------------------------------
def build_undirected_adjacency(edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    """vertex -> list of neighbours, for an undirected graph.
    Time O(E), Space O(V + E). GOTCHA: add u->v AND v->u, else half the graph
    is invisible when you traverse from the other endpoint."""
    adj: Dict[int, List[int]] = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)          # both directions — this is the undirected part
    return adj


# ---------------------------------------------------------------------------
# 2. Build an adjacency list — DIRECTED
#    Only add u -> v. Reverse edge is a different (maybe absent) edge.
# ---------------------------------------------------------------------------
def build_directed_adjacency(edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    """vertex -> list of out-neighbours, for a directed graph.
    Time O(E), Space O(V + E). Only one direction is stored."""
    adj: Dict[int, List[int]] = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)          # one way only
    return adj


# ---------------------------------------------------------------------------
# 3. Build a WEIGHTED adjacency list — neighbour is (vertex, weight)
# ---------------------------------------------------------------------------
def build_weighted_adjacency(
    edges: List[Tuple[int, int, int]], directed: bool = False
) -> Dict[int, List[Tuple[int, int]]]:
    """vertex -> list of (neighbour, weight). Time O(E), Space O(V + E).
    For undirected, store the weight on BOTH directions."""
    adj: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))
    return adj


# ---------------------------------------------------------------------------
# 4. Build an adjacency MATRIX — n x n grid, matrix[u][v] = 1 if edge u->v
#    Space O(V^2). O(1) edge lookup, but wasteful & slow neighbour scan on
#    sparse graphs. Vertices must be 0..n-1 (or mapped to indices).
# ---------------------------------------------------------------------------
def build_adjacency_matrix(
    n: int, edges: List[Tuple[int, int]], directed: bool = False
) -> List[List[int]]:
    """n x n 0/1 matrix. Time O(V^2 + E), Space O(V^2).
    Edge existence check is O(1): matrix[u][v]. GOTCHA: undirected sets both
    matrix[u][v] AND matrix[v][u]."""
    matrix = [[0] * n for _ in range(n)]   # comprehension, NOT [[0]*n]*n (shared rows!)
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix


# ---------------------------------------------------------------------------
# 5. CONVERT  edge list  ->  adjacency list   (and back)
# ---------------------------------------------------------------------------
def edge_list_to_adjacency(
    edges: List[Tuple[int, int]], directed: bool = False
) -> Dict[int, List[int]]:
    """Edge list -> adjacency list. Time O(E), Space O(V + E)."""
    adj: Dict[int, List[int]] = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def adjacency_to_edge_list(
    adj: Dict[int, List[int]], directed: bool = False
) -> List[Tuple[int, int]]:
    """Adjacency list -> edge list. Time O(V + E).
    For UNDIRECTED, emit each edge once by keeping only u <= v, otherwise every
    edge appears twice (once from each endpoint)."""
    edges: List[Tuple[int, int]] = []
    for u in adj:
        for v in adj[u]:
            if directed or u <= v:    # dedupe the mirrored undirected entry
                edges.append((u, v))
    return edges


# ---------------------------------------------------------------------------
# 6. DEGREE counting
#    Undirected: degree(v) = number of incident edges (a self-loop counts twice).
#    Directed:   in-degree (edges INTO v) and out-degree (edges OUT of v).
# ---------------------------------------------------------------------------
def undirected_degrees(adj: Dict[int, List[int]]) -> Dict[int, int]:
    """vertex -> degree for an undirected adjacency list. Time O(V + E)."""
    return {v: len(adj[v]) for v in adj}


def directed_in_out_degrees(
    adj: Dict[int, List[int]]
) -> Tuple[Dict[int, int], Dict[int, int]]:
    """(in_degree, out_degree) maps for a directed adjacency list. Time O(V + E).
    out-degree is just len(adj[v]); in-degree is counted by scanning all edges."""
    out_deg: Dict[int, int] = {v: len(adj[v]) for v in adj}
    in_deg: Dict[int, int] = defaultdict(int)
    for u in adj:
        in_deg.setdefault(u, 0)        # ensure source vertices appear
        for v in adj[u]:
            in_deg[v] += 1
    return dict(in_deg), out_deg


# ---------------------------------------------------------------------------
# 7. NEIGHBOUR iteration + a VISITED set to avoid infinite loops
#    Cycles mean naive recursion/queueing revisits nodes forever. A visited set
#    guarantees each vertex is processed once -> traversal is O(V + E).
# ---------------------------------------------------------------------------
def reachable_count(adj: Dict[int, List[int]], start: int) -> int:
    """How many vertices are reachable from `start` (inclusive). Time O(V + E).
    The `visited` set is what stops a cycle from looping forever."""
    visited: Set[int] = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue                  # already handled — the loop-breaker
        visited.add(node)
        for nbr in adj[node]:
            if nbr not in visited:
                stack.append(nbr)
    return len(visited)


# ---------------------------------------------------------------------------
# 8. GOTCHAS — the bugs that quietly corrupt a graph
# ---------------------------------------------------------------------------
def gotchas() -> None:
    # (a) Undirected edge added only one way -> the reverse traversal sees nothing.
    one_way: Dict[int, List[int]] = defaultdict(list)
    one_way[1].append(2)              # forgot one_way[2].append(1)
    assert 1 not in one_way[2]        # bug: from 2 you can't reach 1
    both_ways = build_undirected_adjacency([(1, 2)])
    assert 2 in both_ways[1] and 1 in both_ways[2]   # correct

    # (b) Self-loop (v -- v). In an undirected degree count it contributes TWICE.
    loop = build_undirected_adjacency([(1, 1)])
    assert loop[1].count(1) == 2      # appended for u and for v
    assert undirected_degrees(loop)[1] == 2

    # (c) Parallel / duplicate edges. A list-based adjacency KEEPS duplicates;
    #     a set-based one (like adjacency_list.py uses) silently dedupes them.
    dup_list = build_undirected_adjacency([(1, 2), (1, 2)])
    assert dup_list[1] == [2, 2]      # both kept -> degree 2
    dup_set: Set[int] = set()
    dup_set.add(2); dup_set.add(2)
    assert dup_set == {2}             # set collapses parallel edges

    # (d) Disconnected vertex: a node with no edges still exists. defaultdict
    #     returns an empty list for it, but it won't appear unless you add it.
    adj = build_directed_adjacency([(1, 2)])
    assert adj[99] == []              # access auto-creates an empty entry
    # ...so to track ALL vertices (incl. isolated ones), keep a separate set.

    # (e) Mutable-default adjacency: never `def f(adj=defaultdict(list))`. The
    #     default is created ONCE and shared across calls (same trap as [] / {}).
    def buggy(x: int, bucket=defaultdict(list)):   # DON'T
        bucket[0].append(x)
        return bucket
    buggy(1)
    assert buggy(2)[0] == [1, 2]      # leaked state from the previous call!

    def fixed(x: int, bucket=None):                # correct idiom
        if bucket is None:
            bucket = defaultdict(list)
        bucket[0].append(x)
        return bucket
    assert fixed(1)[0] == [1] and fixed(2)[0] == [2]


def main() -> None:
    # 1 & 2: directed vs undirected build
    und = build_undirected_adjacency([(1, 2), (2, 3)])
    assert sorted(und[2]) == [1, 3]                 # 2 sees both neighbours
    dir_ = build_directed_adjacency([(1, 2), (2, 3)])
    assert dir_[2] == [3] and dir_[3] == []         # 3 has no out-edges

    # 3: weighted
    w = build_weighted_adjacency([(1, 2, 5), (2, 3, 7)])
    assert (2, 5) in w[1] and (1, 5) in w[2]        # weight mirrored undirected

    # 4: adjacency matrix
    m = build_adjacency_matrix(3, [(0, 1), (1, 2)])
    assert m[0][1] == 1 and m[1][0] == 1            # undirected -> symmetric
    assert m[0][2] == 0

    # 5: conversions round-trip
    edges = [(1, 2), (2, 3), (1, 3)]
    a = edge_list_to_adjacency(edges)
    back = adjacency_to_edge_list(a)
    assert sorted(back) == [(1, 2), (1, 3), (2, 3)]  # each undirected edge once

    # 6: degrees
    assert undirected_degrees(a) == {1: 2, 2: 2, 3: 2}
    dadj = build_directed_adjacency([(1, 2), (1, 3), (2, 3)])
    dadj[3]                     # touch sink vertex so it has an entry (out-degree 0)
    din, dout = directed_in_out_degrees(dadj)
    assert dout == {1: 2, 2: 1, 3: 0} and din == {1: 0, 2: 1, 3: 2}

    # 7: neighbour iteration + visited set on a CYCLE (would loop forever w/o it)
    cyclic = build_undirected_adjacency([(1, 2), (2, 3), (3, 1)])
    assert reachable_count(cyclic, 1) == 3
    assert reachable_count(build_directed_adjacency([(1, 2), (3, 4)]), 1) == 2  # disconnected

    # 8: gotchas
    gotchas()

    print("fundamentals.py: all examples verified ✔")


if __name__ == "__main__":
    main()
