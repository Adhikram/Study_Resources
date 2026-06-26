"""
Binary tree / BST fundamentals for interviews.

Covers the node structure, every traversal (recursive AND iterative), level-order
BFS, the structural queries (height, count), and the four BST operations
(insert / search / delete / validate). Each section is runnable and verified with
`assert`s. Run `python3 fundamentals.py` — if it exits cleanly, every example
behaved as documented.

A BINARY TREE is a set of nodes where each node holds a value and up to two child
pointers (`left`, `right`). A BINARY SEARCH TREE (BST) adds an ordering invariant:
for every node, ALL values in its left subtree are smaller and ALL values in its
right subtree are larger. That invariant is what turns search/insert/delete into
O(h) operations — but only the WHOLE-SUBTREE range, not just the parent, is what
must hold (see `validate_bst` and the boundary gotcha in `edge_cases.py`).

Terminology used throughout:
    height(node)  = edges on the longest path from node DOWN to a leaf (leaf = 0)
    depth(node)   = edges from the root DOWN to that node (root = 0)
    leaf          = node with no children
    h             = height of the tree; O(log n) if balanced, O(n) if skewed
"""

from collections import deque
from typing import List, Optional


# ---------------------------------------------------------------------------
# 1. The node + a build helper
# ---------------------------------------------------------------------------
class TreeNode:
    """A binary-tree node. `val` plus two child pointers; `None` means absent."""

    def __init__(self, val: int = 0,
                 left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a level-order (BFS) list where `None` marks a missing
    child — the same compact format LeetCode uses, e.g. [1, 2, 3, None, 4].
    Time O(n), Space O(n). Edge case: [] or [None] -> None (empty tree)."""
    if not level_order or level_order[0] is None:
        return None
    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1
    return root


# ---------------------------------------------------------------------------
# 2. Depth-first traversals — RECURSIVE
#    Same three lines, reordered. The position of "visit node" names the order.
#    Time O(n) (each node visited once); Space O(h) for the recursion stack.
# ---------------------------------------------------------------------------
def preorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """Node -> Left -> Right. Used to copy/serialize a tree top-down."""
    out: List[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        out.append(node.val)     # visit BEFORE children
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return out


def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """Left -> Node -> Right. On a BST this yields values in SORTED order."""
    out: List[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)
        out.append(node.val)     # visit BETWEEN children
        dfs(node.right)

    dfs(root)
    return out


def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """Left -> Right -> Node. Children before parent — used to free/delete a tree."""
    out: List[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        out.append(node.val)     # visit AFTER children

    dfs(root)
    return out


# ---------------------------------------------------------------------------
# 3. Depth-first traversals — ITERATIVE (explicit stack)
#    Why bother? Recursion blows the stack on a skewed tree of ~1000s of nodes
#    (Python's default recursion limit is ~1000). An explicit stack is O(h) heap
#    space, which is much larger than the call stack.
# ---------------------------------------------------------------------------
def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Push root; pop -> visit -> push RIGHT then LEFT (so left is popped first).
    Time O(n), Space O(h)."""
    if not root:
        return []
    out: List[int] = []
    stack = [root]
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right:
            stack.append(node.right)   # right pushed first => popped last
        if node.left:
            stack.append(node.left)
    return out


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Walk all the way left pushing nodes, then pop+visit+go right.
    Time O(n), Space O(h)."""
    out: List[int] = []
    stack: List[TreeNode] = []
    curr = root
    while stack or curr:
        while curr:                    # dive to the leftmost node
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()             # leftmost unvisited
        out.append(curr.val)
        curr = curr.right              # then explore its right subtree
    return out


def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Trick: do a modified preorder (Node -> Right -> Left), then REVERSE it.
    That reversed order is exactly Left -> Right -> Node. Time O(n), Space O(h)."""
    if not root:
        return []
    out: List[int] = []
    stack = [root]
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.left:
            stack.append(node.left)    # left first => popped before right
        if node.right:
            stack.append(node.right)
    out.reverse()                      # Node,Right,Left reversed = Left,Right,Node
    return out


# ---------------------------------------------------------------------------
# 4. Breadth-first traversal — LEVEL ORDER (queue / deque)
# ---------------------------------------------------------------------------
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Group node values level by level, top to bottom, left to right.
    Time O(n), Space O(w) where w is the maximum width (the widest level).
    Snapshot the queue length per level so each pass handles exactly one level."""
    if not root:
        return []
    out: List[List[int]] = []
    queue = deque([root])
    while queue:
        level_size = len(queue)        # nodes currently on this level
        level: List[int] = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        out.append(level)
    return out


# ---------------------------------------------------------------------------
# 5. Structural queries
# ---------------------------------------------------------------------------
def height(root: Optional[TreeNode]) -> int:
    """Height in EDGES (single node -> 0, empty -> -1). Time O(n), Space O(h).
    Returning -1 for empty makes `1 + max(left, right)` compose cleanly."""
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))


def count_nodes(root: Optional[TreeNode]) -> int:
    """Total number of nodes. Time O(n), Space O(h)."""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# ---------------------------------------------------------------------------
# 6. BST operations — each is O(h): O(log n) balanced, O(n) skewed.
#    DUPLICATE CONVENTION: this implementation REJECTS duplicates on insert
#    (a no-op). Common alternatives: keep a count per node, or always send equal
#    keys to one side. ALWAYS clarify the convention with the interviewer.
# ---------------------------------------------------------------------------
def bst_insert(root: Optional[TreeNode], val: int) -> TreeNode:
    """Insert val into a BST, returning the (possibly new) root. Time O(h).
    Duplicates are ignored. Returns the root so the caller can reassign:
    `root = bst_insert(root, x)` — this is how the empty-tree case works."""
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    elif val > root.val:
        root.right = bst_insert(root.right, val)
    # val == root.val -> duplicate, ignore
    return root


def bst_search(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Return the node holding val, or None. Time O(h), Space O(1) (iterative).
    Each comparison discards a whole subtree — that's the BST payoff."""
    curr = root
    while curr:
        if val == curr.val:
            return curr
        curr = curr.left if val < curr.val else curr.right
    return None


def bst_delete(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Delete val from a BST, returning the new root. Time O(h).
    Three cases for the node to remove:
      - leaf / one child : splice the (possibly None) child up
      - two children     : replace value with the INORDER SUCCESSOR (smallest in
                           the right subtree), then delete that successor.
    Using the successor preserves the BST ordering invariant."""
    if not root:
        return None
    if val < root.val:
        root.left = bst_delete(root.left, val)
    elif val > root.val:
        root.right = bst_delete(root.right, val)
    else:                              # found the node to delete
        if not root.left:
            return root.right          # 0 or 1 (right) child
        if not root.right:
            return root.left           # 1 (left) child
        succ = root.right              # two children: find inorder successor
        while succ.left:
            succ = succ.left
        root.val = succ.val            # copy successor value up
        root.right = bst_delete(root.right, succ.val)   # remove the successor
    return root


def validate_bst(root: Optional[TreeNode]) -> bool:
    """True iff the tree obeys the BST invariant. Time O(n), Space O(h).
    GOTCHA: comparing only against the immediate parent is WRONG — a node deep in
    the left subtree can still be larger than an ancestor. Carry an OPEN (low,
    high) RANGE that tightens as you descend (see COMPLEXITY.md and edge_cases.py)."""
    def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (valid(node.left, low, node.val) and
                valid(node.right, node.val, high))

    return valid(root, float("-inf"), float("inf"))


# ===========================================================================
# TESTS
# ===========================================================================
def _test() -> None:
    # Shared sample tree (NOT a BST), level-order:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    t = build_tree([1, 2, 3, 4, 5, None, 6])

    # 2/3. DFS recursive vs iterative must agree
    assert preorder_recursive(t) == [1, 2, 4, 5, 3, 6]
    assert preorder_iterative(t) == [1, 2, 4, 5, 3, 6]
    assert inorder_recursive(t) == [4, 2, 5, 1, 3, 6]
    assert inorder_iterative(t) == [4, 2, 5, 1, 3, 6]
    assert postorder_recursive(t) == [4, 5, 2, 6, 3, 1]
    assert postorder_iterative(t) == [4, 5, 2, 6, 3, 1]

    # empty / single-node traversals
    assert preorder_recursive(None) == [] and inorder_iterative(None) == []
    single = TreeNode(42)
    assert level_order(single) == [[42]] and height(single) == 0

    # 4. level order
    assert level_order(t) == [[1], [2, 3], [4, 5, 6]]
    assert level_order(None) == []

    # 5. structural queries (height in EDGES, empty -> -1)
    assert height(t) == 2
    assert height(None) == -1
    assert count_nodes(t) == 6 and count_nodes(None) == 0

    # 6. BST insert/search — build one by repeated insertion
    bst: Optional[TreeNode] = None
    for v in [5, 3, 8, 1, 4, 7, 9]:
        bst = bst_insert(bst, v)
    assert inorder_recursive(bst) == [1, 3, 4, 5, 7, 8, 9]   # sorted!
    assert validate_bst(bst) is True
    assert bst_search(bst, 7) is not None
    assert bst_search(bst, 6) is None
    bst = bst_insert(bst, 5)                                  # duplicate ignored
    assert inorder_recursive(bst) == [1, 3, 4, 5, 7, 8, 9]

    # delete: leaf (1), one-child (8 after removing 9 leaves only 7), two-children (3)
    bst = bst_delete(bst, 1)
    assert inorder_recursive(bst) == [3, 4, 5, 7, 8, 9]
    bst = bst_delete(bst, 8)                                  # 8 has child 9 (one side)
    assert inorder_recursive(bst) == [3, 4, 5, 7, 9]
    bst = bst_delete(bst, 5)                                  # 5 (root) has two children
    assert inorder_recursive(bst) == [3, 4, 7, 9]
    assert validate_bst(bst) is True                          # still a valid BST
    bst = bst_delete(bst, 100)                                # absent -> no-op
    assert inorder_recursive(bst) == [3, 4, 7, 9]

    # validate_bst boundary gotcha: parent-only comparison would wrongly accept this.
    #        5
    #       / \
    #      3   8
    #         /
    #        4        <- 4 < 5, so it violates the BST property despite 4 < 8
    bad = TreeNode(5, TreeNode(3), TreeNode(8, TreeNode(4)))
    assert validate_bst(bad) is False


def main() -> None:
    _test()
    print("fundamentals.py: all examples verified ✔")


if __name__ == "__main__":
    main()
