"""
Binary tree / BST edge cases — the inputs that break naive solutions, with proof.

Each function demonstrates ONE edge-case category: where it matters, a naive
approach that fails (or would), and the robust version that doesn't. Run
`python3 edge_cases.py`; a clean exit means every "robust" version handled its
edge case as documented.

Use this as a pre-submission checklist: walk your tree solution through each case.
"""

import sys
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


# ---------------------------------------------------------------------------
# 1. EMPTY TREE (root is None) — the #1 crash. Any recursion or BFS must hit a
#    base case for None BEFORE touching node.val / node.left.
# ---------------------------------------------------------------------------
def empty_tree() -> None:
    def naive_max_depth(node):        # crashes on None: node.left / node.right
        return 1 + max(naive_max_depth(node.left), naive_max_depth(node.right))

    def robust_max_depth(node):       # base case guards the None
        if not node:
            return 0
        return 1 + max(robust_max_depth(node.left), robust_max_depth(node.right))

    assert robust_max_depth(None) == 0
    assert robust_max_depth(TreeNode(1)) == 1
    try:
        naive_max_depth(None)
        assert False
    except AttributeError:
        pass                          # 'NoneType' has no attribute 'left' — the bug


# ---------------------------------------------------------------------------
# 2. SINGLE NODE — leaf and root at once. Leaf-based logic (path sum, leaf
#    counting) must treat "no children" correctly.
# ---------------------------------------------------------------------------
def single_node() -> None:
    def has_path_sum(node, target):
        if not node:
            return False
        if not node.left and not node.right:   # leaf check, true for a single node
            return node.val == target
        rem = target - node.val
        return has_path_sum(node.left, rem) or has_path_sum(node.right, rem)

    root = TreeNode(7)
    assert has_path_sum(root, 7) is True       # the node itself is the only path
    assert has_path_sum(root, 5) is False
    assert has_path_sum(None, 0) is False      # empty: no root-to-leaf path exists


# ---------------------------------------------------------------------------
# 3. COMPLETELY SKEWED TREE — a degenerate linked list. Height == n, so deep
#    recursion can hit Python's recursion limit (~1000). Iterative traversal
#    uses O(h) HEAP space and survives.
# ---------------------------------------------------------------------------
def skewed_tree() -> None:
    # Build a right-skewed chain of 2000 nodes: 0 -> 1 -> 2 -> ... (all .right)
    n = 2000
    root = TreeNode(0)
    curr = root
    for v in range(1, n):
        curr.right = TreeNode(v)
        curr = curr.right

    def naive_count(node):            # O(h) recursion depth -> RecursionError at h~1000
        if not node:
            return 0
        return 1 + naive_count(node.left) + naive_count(node.right)

    def robust_count(node):           # iterative: explicit stack on the heap
        stack = [node]
        total = 0
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            total += 1
            stack.append(cur.left)
            stack.append(cur.right)
        return total

    assert robust_count(root) == n
    raised = False
    try:
        naive_count(root)             # depth 2000 exceeds the default limit
    except RecursionError:
        raised = True
    assert raised, "expected RecursionError on a 2000-deep skewed tree"
    # (You could also raise sys.setrecursionlimit, but that risks a real stack
    #  overflow / segfault; the iterative form is the safe interview answer.)
    assert sys.getrecursionlimit() < n   # confirm the default limit is below n


# ---------------------------------------------------------------------------
# 4. DUPLICATE VALUES — comparing NODES by value is wrong when values repeat;
#    compare by identity (`is`). BST insert needs a stated duplicate convention.
# ---------------------------------------------------------------------------
def duplicate_values() -> None:
    # Two distinct nodes share value 2. LCA must use identity, not value equality.
    #        2
    #       / \
    #      1   2     <- duplicate value 2
    a = TreeNode(2)
    a.left = TreeNode(1)
    a.right = TreeNode(2)
    p = a.right                       # the deeper "2"

    def lca(root, target):            # robust: identity check `is`
        if not root or root is target:
            return root
        left = lca(root.left, target)
        right = lca(root.right, target)
        return root if (left and right) else (left or right)

    found = lca(a, p)
    assert found is p and found is not a   # found the RIGHT "2", not the root "2"

    # BST insert with a "duplicates go right" convention stays a valid (multi)set.
    def bst_insert(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = bst_insert(root.left, val)
        else:                         # >= sends duplicates consistently right
            root.right = bst_insert(root.right, val)
        return root

    r = None
    for v in [5, 3, 5, 5]:
        r = bst_insert(r, v)
    # inorder is non-decreasing with the duplicates preserved
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    assert inorder(r) == [3, 5, 5, 5]


# ---------------------------------------------------------------------------
# 5. UNBALANCED vs BALANCED HEIGHT — calling height() at every node is O(n^2)
#    on a skewed tree; the bottom-up single pass is O(n).
# ---------------------------------------------------------------------------
def unbalanced_vs_balanced() -> None:
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def is_balanced_robust(node):     # single O(n) pass, -1 = "unbalanced" sentinel
        def check(n):
            if not n:
                return 0
            lh = check(n.left)
            if lh == -1:
                return -1
            rh = check(n.right)
            if rh == -1:
                return -1
            return -1 if abs(lh - rh) > 1 else 1 + max(lh, rh)
        return check(node) != -1

    # Balanced: full tree of height 2
    balanced = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                           TreeNode(3))
    assert is_balanced_robust(balanced) is True
    assert height(balanced) == 3

    # Unbalanced: left chain only -> heights 2 vs 0 at the root
    unbalanced = TreeNode(1, TreeNode(2, TreeNode(3)), None)
    assert is_balanced_robust(unbalanced) is False
    assert is_balanced_robust(None) is True   # empty tree is balanced


# ---------------------------------------------------------------------------
# 6. BST VALIDATION BOUNDARY — the classic trap: validating against the PARENT
#    only. A node must respect the range imposed by ALL its ancestors, not just
#    its immediate parent. Use an open (low, high) range that tightens on descent.
# ---------------------------------------------------------------------------
def bst_boundary() -> None:
    #        5
    #       / \
    #      1   7
    #         / \
    #        4   8       <- 4 is in 7's LEFT subtree but 4 < 5: violates the BST!
    root = TreeNode(5, TreeNode(1), TreeNode(7, TreeNode(4), TreeNode(8)))

    def naive_valid(node):            # WRONG: only checks immediate parent ordering
        if not node:
            return True
        if node.left and node.left.val >= node.val:
            return False
        if node.right and node.right.val <= node.val:
            return False
        return naive_valid(node.left) and naive_valid(node.right)

    def robust_valid(node, low=float("-inf"), high=float("inf")):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (robust_valid(node.left, low, node.val) and
                robust_valid(node.right, node.val, high))

    assert naive_valid(root) is True      # the BUG: parent-only check accepts it
    assert robust_valid(root) is False    # range check correctly rejects it
    # a genuinely valid BST passes both
    good = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)),
                       TreeNode(8, TreeNode(7), TreeNode(9)))
    assert naive_valid(good) is True and robust_valid(good) is True


def main() -> None:
    empty_tree()
    single_node()
    skewed_tree()
    duplicate_values()
    unbalanced_vs_balanced()
    bst_boundary()
    print("edge_cases.py: all 6 edge-case categories verified ✔")


if __name__ == "__main__":
    main()
