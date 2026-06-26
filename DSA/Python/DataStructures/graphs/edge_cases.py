"""
Graph edge cases — the inputs that break naive solutions, with runnable proof.

Each function demonstrates ONE edge-case category: a naive approach that fails
(or a subtle wrong assumption) and the robust version that doesn't. Run
`python3 edge_cases.py`; a clean exit means every "robust" version handled its
edge case as documented.

Use this as a pre-submission checklist: walk your graph solution through each
case before you say "done".
"""

from collections import defaultdict, deque
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# 1. EMPTY GRAPH — no vertices, no edges. Traversals/counts must not crash and
#    should return the empty/zero answer, not raise.
# ---------------------------------------------------------------------------
def empty_graph() -> None:
    def bfs(adj: Dict[int, List[int]], start: Optional[int]) -> List[int]:
        if start is None or start not in adj:
            return []                  # nothing to traverse
        visited = {start}
        q = deque([start])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nbr in adj[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        return order

    empty: Dict[int, List[int]] = {}
    assert bfs(empty, None) == []
    assert bfs(empty, 1) == []         # start absent -> empty, not KeyError


# ---------------------------------------------------------------------------
# 2. SINGLE VERTEX, NO EDGES — traversal returns just that vertex; degree 0.
# ---------------------------------------------------------------------------
def single_vertex() -> None:
    def reachable(adj: Dict[int, List[int]], start: int) -> List[int]:
        visited = {start}
        order, stack = [], [start]
        while stack:
            node = stack.pop()
            order.append(node)
            for nbr in adj[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    stack.append(nbr)
        return order

    adj: Dict[int, List[int]] = {0: []}
    assert reachable(adj, 0) == [0]    # lone vertex is reachable from itself
    assert len(adj[0]) == 0            # degree 0


# ---------------------------------------------------------------------------
# 3. DISCONNECTED GRAPH — BFS/DFS from ONE node misses other components. To
#    cover everything you must loop over ALL vertices, not start from one.
# ---------------------------------------------------------------------------
def disconnected_graph() -> None:
    adj: Dict[int, List[int]] = {0: [1], 1: [0], 2: [3], 3: [2]}   # {0,1} and {2,3}

    def bfs_from(start: int) -> set:
        visited = {start}
        q = deque([start])
        while q:
            node = q.popleft()
            for nbr in adj[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        return visited

    naive = bfs_from(0)                # only the first component
    assert naive == {0, 1}
    assert 2 not in naive and 3 not in naive   # the bug: other component missed

    def visit_all() -> int:            # robust: count components over ALL vertices
        seen: set = set()
        comps = 0
        for v in adj:
            if v not in seen:
                comps += 1
                seen |= bfs_from(v)
        return comps

    assert visit_all() == 2            # both components found


# ---------------------------------------------------------------------------
# 4. SELF-LOOP (v -- v) — must not loop forever, and it counts as a cycle.
# ---------------------------------------------------------------------------
def self_loop() -> None:
    adj: Dict[int, List[int]] = defaultdict(list)
    adj[0].append(0)                   # self-loop

    def reachable(start: int) -> set:  # visited set prevents infinite recursion
        visited: set = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue               # the self-loop is absorbed here
            visited.add(node)
            stack.extend(adj[node])
        return visited

    assert reachable(0) == {0}         # terminates despite the loop

    def has_self_loop() -> bool:
        return any(v in adj[v] for v in adj)

    assert has_self_loop() is True     # a self-loop IS a cycle


# ---------------------------------------------------------------------------
# 5. PARALLEL / DUPLICATE EDGES — a list adjacency keeps them (inflates degree
#    and BFS revisits), a set adjacency dedupes. Pick the right structure.
# ---------------------------------------------------------------------------
def parallel_edges() -> None:
    list_adj: Dict[int, List[int]] = defaultdict(list)
    for u, v in [(0, 1), (0, 1)]:      # same edge twice
        list_adj[u].append(v)
        list_adj[v].append(u)
    assert list_adj[0] == [1, 1]       # duplicate kept -> degree 2 (often wrong)

    set_adj: Dict[int, set] = defaultdict(set)
    for u, v in [(0, 1), (0, 1)]:
        set_adj[u].add(v)
        set_adj[v].add(u)
    assert set_adj[0] == {1}           # collapsed -> simple graph degree 1


# ---------------------------------------------------------------------------
# 6. CYCLE vs DAG for TOPOLOGICAL SORT — a cycle has NO valid ordering. Kahn's
#    must detect "couldn't place every vertex" and report it (None), not return
#    a partial order as if it were valid.
# ---------------------------------------------------------------------------
def cycle_breaks_topo() -> None:
    def topo(n: int, edges: List[Tuple[int, int]]) -> Optional[List[int]]:
        adj: Dict[int, List[int]] = defaultdict(list)
        indeg = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1
        q = deque(i for i in range(n) if indeg[i] == 0)
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nbr in adj[node]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0:
                    q.append(nbr)
        return order if len(order) == n else None

    assert topo(3, [(0, 1), (1, 2)]) == [0, 1, 2]   # DAG -> valid order
    assert topo(3, [(0, 1), (1, 2), (2, 0)]) is None  # cycle -> no order at all


# ---------------------------------------------------------------------------
# 7. DIRECTED vs UNDIRECTED cycle detection — the rules DIFFER. In undirected
#    you must ignore the edge back to your parent; applying the directed rule
#    (any visited neighbour = cycle) gives a FALSE positive on a simple tree.
# ---------------------------------------------------------------------------
def directed_vs_undirected_cycle() -> None:
    # Undirected edge 0-1 stored both ways. From 1, neighbour 0 is "visited" but
    # it's just our parent — NOT a cycle.
    adj: Dict[int, List[int]] = {0: [1], 1: [0]}

    def naive_cycle(start: int) -> bool:        # WRONG for undirected: no parent check
        visited: set = set()

        def visit(node: int) -> bool:
            visited.add(node)
            for nbr in adj[node]:
                if nbr in visited:
                    return True                 # falsely fires on the parent edge
                if visit(nbr):
                    return True
            return False

        return visit(start)

    def robust_cycle(start: int) -> bool:       # correct: skip the parent
        visited: set = set()

        def visit(node: int, parent: int) -> bool:
            visited.add(node)
            for nbr in adj[node]:
                if nbr not in visited:
                    if visit(nbr, node):
                        return True
                elif nbr != parent:
                    return True
            return False

        return visit(start, -1)

    assert naive_cycle(0) is True       # false positive — the bug
    assert robust_cycle(0) is False     # correct: 0-1 is just an edge, no cycle


# ---------------------------------------------------------------------------
# 8. UNREACHABLE TARGET — there may be NO path. Return a clear sentinel
#    (None / -1 / inf), never a wrong number or an exception.
# ---------------------------------------------------------------------------
def unreachable_target() -> None:
    adj: Dict[int, List[int]] = {0: [1], 1: [], 2: [3], 3: []}   # 2,3 separate

    def shortest(start: int, target: int) -> int:
        dist = {start: 0}
        q = deque([start])
        while q:
            node = q.popleft()
            if node == target:
                return dist[node]
            for nbr in adj[node]:
                if nbr not in dist:
                    dist[nbr] = dist[node] + 1
                    q.append(nbr)
        return -1                       # sentinel: target not reachable

    assert shortest(0, 1) == 1
    assert shortest(0, 3) == -1         # different component -> unreachable
    assert shortest(0, 0) == 0          # start == target


def main() -> None:
    empty_graph()
    single_vertex()
    disconnected_graph()
    self_loop()
    parallel_edges()
    cycle_breaks_topo()
    directed_vs_undirected_cycle()
    unreachable_target()
    print("edge_cases.py: all 8 edge-case categories verified ✔")


if __name__ == "__main__":
    main()
