"""
Core binary-tree / BST patterns for coding interviews — runnable & self-testing.

Every pattern below is a real, callable function (not a nested stub) with its time
and space complexity, the edge cases it handles, and inline `assert` tests in
`_test()`. Run `python3 tree_tricks.py`; a clean exit means all patterns passed.

Almost every tree problem is one of two shapes:
    - DFS recursion that returns a value UP the tree (depth, balance, LCA, path sum)
    - a single traversal that threads STATE through (serialize, path-sum-III map)
Spotting which shape a problem is the whole game.

Patterns:
    1.  Max depth (height in nodes)
    2.  Diameter (longest path, may not pass through root)
    3.  Invert / mirror
    4.  Is-balanced (height-balanced in one pass)
    5.  LCA — lowest common ancestor (binary tree + BST variants)
    6.  Path sum I (root-to-leaf) + III (any downward path, prefix-sum map)
    7.  Serialize / deserialize (preorder with null markers)
    8.  Build tree from preorder + inorder
    9.  Morris inorder traversal (O(1) space)
"""

from collections import deque
from typing import Dict, List, Optional, Tuple


class TreeNode:
    """A binary-tree node; `None` means an absent child."""

    def __init__(self, val: int = 0,
                 left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a LeetCode-style level-order list (`None` = missing child).
    Used by the tests below. Time O(n), Space O(n)."""
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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Locate the first node with a given value (test helper for LCA). O(n)."""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


# ===========================================================================
# 1. MAX DEPTH — height counted in NODES (LeetCode's definition)
# ===========================================================================
def max_depth(root: Optional[TreeNode]) -> int:
    """Number of nodes on the longest root-to-leaf path (empty -> 0, leaf -> 1).
    Time O(n), Space O(h). The canonical "return a value up the tree" recursion."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# ===========================================================================
# 2. DIAMETER — longest path (in edges) between ANY two nodes
# ===========================================================================
def diameter(root: Optional[TreeNode]) -> int:
    """Longest path measured in EDGES; the path need NOT pass through the root.
    Time O(n), Space O(h). Trick: at each node the best path THROUGH it is
    left_height + right_height; track the global max while returning height up."""
    best = 0

    def depth(node: Optional[TreeNode]) -> int:
        nonlocal best
        if not node:
            return 0                          # height in nodes of empty = 0
        left = depth(node.left)
        right = depth(node.right)
        best = max(best, left + right)        # edges through this node
        return 1 + max(left, right)

    depth(root)
    return best


# ===========================================================================
# 3. INVERT / MIRROR — swap every node's children
# ===========================================================================
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Mirror the tree in place and return the root. Time O(n), Space O(h).
    Edge case: None -> None (recursion bottoms out cleanly)."""
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


# ===========================================================================
# 4. IS-BALANCED — every node's subtree heights differ by at most 1
# ===========================================================================
def is_balanced(root: Optional[TreeNode]) -> bool:
    """Height-balanced check in a SINGLE O(n) pass (Space O(h)).
    Trick: a helper returns the height, but returns the sentinel -1 the moment
    any subtree is unbalanced, short-circuiting the rest. The naive approach
    (call height() at every node) is O(n^2) on a skewed tree."""
    def check(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1                          # unbalanced -> poison upward
        return 1 + max(left, right)

    return check(root) != -1


# ===========================================================================
# 5. LCA — lowest common ancestor
# ===========================================================================
def lca_binary_tree(root: Optional[TreeNode],
                    p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """LCA in a GENERAL binary tree (no ordering). Time O(n), Space O(h).
    Returns the node where p and q's subtrees split: if one target is found in
    the left subtree and the other in the right, THIS node is the LCA.
    Assumes both p and q exist in the tree."""
    if not root or root is p or root is q:
        return root
    left = lca_binary_tree(root.left, p, q)
    right = lca_binary_tree(root.right, p, q)
    if left and right:
        return root                            # split here -> this is the LCA
    return left if left else right             # both targets on one side


def lca_bst(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """LCA exploiting the BST property — O(h) time, O(1) space (iterative).
    Walk down: if both targets are smaller go left, if both larger go right; the
    first node where they DIVERGE (or equals one of them) is the split = the LCA."""
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr                        # diverge here
    return None


# ===========================================================================
# 6. PATH SUM — I (root-to-leaf exact) and III (any downward path)
# ===========================================================================
def has_path_sum(root: Optional[TreeNode], target: int) -> bool:
    """True iff some ROOT-TO-LEAF path sums to target. Time O(n), Space O(h).
    GOTCHA: the check must happen AT A LEAF, not when the remainder hits 0 — a
    partial path that reaches the target mid-tree does not count. Negatives are
    fine because we never prune early."""
    if not root:
        return False
    if not root.left and not root.right:       # leaf
        return root.val == target
    remaining = target - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))


def path_sum_iii(root: Optional[TreeNode], target: int) -> int:
    """Count paths summing to target. Paths go DOWNWARD (parent->child) and may
    start/end at any node. Time O(n), Space O(h).
    Trick: the array 'subarray-sum-equals-k' idea on a root-to-node path. Keep a
    running sum and a map of prefix-sum frequencies seen on the CURRENT path; a
    valid path ending here exists for every earlier prefix equal to (running -
    target). Decrement the map on the way back up (backtracking) so sibling
    subtrees don't see each other's prefixes."""
    prefix: Dict[int, int] = {0: 1}            # empty prefix has sum 0

    def dfs(node: Optional[TreeNode], running: int) -> int:
        if not node:
            return 0
        running += node.val
        count = prefix.get(running - target, 0)
        prefix[running] = prefix.get(running, 0) + 1
        count += dfs(node.left, running)
        count += dfs(node.right, running)
        prefix[running] -= 1                   # backtrack: leave this path
        return count

    return dfs(root, 0)


# ===========================================================================
# 7. SERIALIZE / DESERIALIZE — preorder with explicit null markers
# ===========================================================================
def serialize(root: Optional[TreeNode]) -> str:
    """Encode any binary tree to a string (preorder, '#' marks a None child).
    Time O(n), Space O(n). Null markers are what make the encoding unambiguous —
    without them you cannot reconstruct the exact shape."""
    parts: List[str] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            parts.append("#")
            return
        parts.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(parts)


def deserialize(data: str) -> Optional[TreeNode]:
    """Inverse of serialize(). Time O(n), Space O(n).
    Consume tokens in preorder order from a single shared iterator — the same
    order they were produced, so each '#' rebuilds a None and stops that branch."""
    tokens = iter(data.split(","))

    def build() -> Optional[TreeNode]:
        val = next(tokens)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = build()                    # preorder: left subtree first
        node.right = build()
        return node

    return build()


# ===========================================================================
# 8. BUILD TREE FROM PREORDER + INORDER
# ===========================================================================
def build_from_preorder_inorder(preorder: List[int],
                                 inorder: List[int]) -> Optional[TreeNode]:
    """Reconstruct a tree from its preorder and inorder traversals (distinct
    values assumed). Time O(n), Space O(n).
    Insight: preorder[0] is always the root. Its position in inorder splits the
    inorder list into (left subtree | root | right subtree); the left part's
    length tells us how much of preorder is the left subtree. We use an index map
    for O(1) splits and a moving preorder pointer to stay O(n) overall (slicing
    preorder[1:] every call would be O(n^2))."""
    index = {val: i for i, val in enumerate(inorder)}   # value -> inorder index
    pre_idx = 0

    def build(in_left: int, in_right: int) -> Optional[TreeNode]:
        nonlocal pre_idx
        if in_left > in_right:
            return None
        root_val = preorder[pre_idx]
        pre_idx += 1
        node = TreeNode(root_val)
        mid = index[root_val]
        node.left = build(in_left, mid - 1)     # left subtree BEFORE right
        node.right = build(mid + 1, in_right)
        return node

    return build(0, len(inorder) - 1)


# ===========================================================================
# 9. MORRIS INORDER — O(1) extra space via threading
# ===========================================================================
def morris_inorder(root: Optional[TreeNode]) -> List[int]:
    """Inorder traversal in O(n) time and O(1) EXTRA space (no stack/recursion).
    Trick: temporarily thread each node's inorder PREDECESSOR's spare right
    pointer back to the node, walk left, and follow the thread back up when
    done — then UNDO the thread to restore the tree. The null right pointers of
    rightmost nodes are the free scratch space that replaces the call stack."""
    out: List[int] = []
    curr = root
    while curr:
        if not curr.left:
            out.append(curr.val)               # no left subtree -> visit, go right
            curr = curr.right
        else:
            pred = curr.left                   # rightmost node of left subtree
            while pred.right and pred.right is not curr:
                pred = pred.right
            if not pred.right:
                pred.right = curr              # create thread back to curr
                curr = curr.left
            else:
                pred.right = None              # thread already there -> remove it
                out.append(curr.val)           # left subtree done -> visit curr
                curr = curr.right
    return out


# ===========================================================================
# TESTS
# ===========================================================================
def _test() -> None:
    #         3
    #        / \
    #       9  20
    #         /  \
    #        15   7
    t = build_tree([3, 9, 20, None, None, 15, 7])

    # 1. max depth
    assert max_depth(t) == 3
    assert max_depth(None) == 0
    assert max_depth(TreeNode(1)) == 1

    # 2. diameter (edges). For [1,2,3,4,5]: path 4-2-5 or 4-2-1-3 => 3 edges
    d = build_tree([1, 2, 3, 4, 5])
    assert diameter(d) == 3
    assert diameter(None) == 0
    assert diameter(TreeNode(1)) == 0          # single node -> 0 edges

    # 3. invert
    inv = build_tree([1, 2, 3, 4, 5, 6, 7])
    invert_tree(inv)
    assert _inorder(inv) == [7, 3, 6, 1, 5, 2, 4]
    assert invert_tree(None) is None

    # 4. is-balanced
    assert is_balanced(build_tree([3, 9, 20, None, None, 15, 7])) is True
    assert is_balanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])) is False
    assert is_balanced(None) is True           # empty is balanced
    # skewed chain 1->2->3 is NOT balanced
    assert is_balanced(build_tree([1, 2, None, 3])) is False

    # 5. LCA — general binary tree
    bt = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p, q = find_node(bt, 5), find_node(bt, 1)
    assert lca_binary_tree(bt, p, q).val == 3
    p, q = find_node(bt, 5), find_node(bt, 4)
    assert lca_binary_tree(bt, p, q).val == 5  # an ancestor can be the LCA itself
    #    LCA — BST variant
    #         6
    #        / \
    #       2   8
    #      / \  / \
    #     0  4 7  9
    bst = build_tree([6, 2, 8, 0, 4, 7, 9])
    p, q = find_node(bst, 2), find_node(bst, 8)
    assert lca_bst(bst, p, q).val == 6
    p, q = find_node(bst, 2), find_node(bst, 4)
    assert lca_bst(bst, p, q).val == 2

    # 6. path sum I (root-to-leaf) and III (any downward path)
    #         5
    #        / \
    #       4   8
    #      /   / \
    #     11  13  4
    #    / \       \
    #   7   2       1
    ps = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    assert has_path_sum(ps, 22) is True        # 5->4->11->2
    assert has_path_sum(ps, 100) is False
    assert has_path_sum(None, 0) is False      # empty has no root-to-leaf path
    # path sum III with negatives; LeetCode example tree
    ps3 = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    assert path_sum_iii(ps3, 8) == 3
    assert path_sum_iii(None, 0) == 0

    # 7. serialize / deserialize round-trips (shape preserved)
    for spec in ([1, 2, 3, None, None, 4, 5], [], [42], [1, None, 2, None, 3]):
        original = build_tree(spec)
        assert serialize(deserialize(serialize(original))) == serialize(original)
    assert serialize(None) == "#"

    # 8. build from preorder + inorder
    built = build_from_preorder_inorder([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert _preorder(built) == [3, 9, 20, 15, 7]
    assert _inorder(built) == [9, 3, 15, 20, 7]
    assert build_from_preorder_inorder([], []) is None

    # 9. Morris inorder == recursive inorder, and the tree is RESTORED afterwards
    m = build_tree([1, 2, 3, 4, 5, None, 6])
    assert morris_inorder(m) == _inorder(m)
    assert _preorder(m) == [1, 2, 4, 5, 3, 6]  # structure intact (threads undone)
    assert morris_inorder(None) == []


# small local recursive references (kept private to this test module)
def _inorder(root: Optional[TreeNode]) -> List[int]:
    return (_inorder(root.left) + [root.val] + _inorder(root.right)) if root else []


def _preorder(root: Optional[TreeNode]) -> List[int]:
    return ([root.val] + _preorder(root.left) + _preorder(root.right)) if root else []


def main() -> None:
    _test()
    print("tree_tricks.py: all 9 patterns verified ✔")


if __name__ == "__main__":
    main()
