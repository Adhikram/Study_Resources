"""
Common Tree Tricks and Patterns for Coding Interviews

This file contains popular tree manipulation techniques and patterns
that frequently appear in coding interviews.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_traversal_patterns():
    """
    Tree Traversal Patterns:
    1. DFS (Preorder, Inorder, Postorder)
    2. BFS (Level Order)
    3. Morris Traversal (O(1) space)
    """
    def inorder_recursive(root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            print(node.val)  # Process node
            dfs(node.right)
        dfs(root)
    
    def inorder_iterative(root):
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            print(curr.val)  # Process node
            curr = curr.right
    
    def morris_traversal(root):
        """
        O(1) space complexity traversal
        This method modifies the tree structure temporarily
        to achieve in-order traversal without using stack or recursion.
        After processing, it restores the tree structure.
        Time Complexity: O(n)
        Space Complexity: O(1)

        first we mark the left subtree of the current node as visited by
        connecting the rightmost node of the left subtree to the current node.
        Then we move to the left subtree.
        When we reach a node that has already been visited (i.e., its right child is the current node),
        we remove the thread and move to the right subtree.
        """
        curr = root
        while curr:
            if not curr.left:
                print(curr.val)  # Process node
                curr = curr.right
            else:
                # Find the inorder predecessor
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if not pred.right:
                    pred.right = curr  # Create thread
                    curr = curr.left
                else:
                    pred.right = None  # Remove thread
                    print(curr.val)  # Process node
                    curr = curr.right

def tree_construction():
    """
    Tree Construction Techniques:
    1. From inorder and preorder/postorder
    2. From level order
    3. From string representation
    """
    def build_tree_from_inorder_preorder(preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = build_tree_from_inorder_preorder(
            preorder[1:mid+1],
            inorder[:mid]
        )
        root.right = build_tree_from_inorder_preorder(
            preorder[mid+1:],
            inorder[mid+1:]
        )
        
        return root

def lowest_common_ancestor():
    """
    Lowest Common Ancestor (LCA) Patterns:
    1. Binary Tree LCA
    2. Binary Search Tree LCA
    3. N-ary Tree LCA
    """
    def lca_binary_tree(root, p, q):
        if not root or root == p or root == q:
            return root
        
        left = lca_binary_tree(root.left, p, q)
        right = lca_binary_tree(root.right, p, q)
        
        if left and right:
            return root
        return left if left else right
    
    def lca_bst(root, p, q):
        """More efficient for BST
        As we traverse the tree, we can determine if both p and q are
        in the left or right subtree. If one is on the left and the other
        is on the right, then the current node is the LCA.
        Time Complexity: O(h) where h is the height of the tree
        Space Complexity: O(1)
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

def path_sum_patterns():
    """
    Path Sum Related Patterns:
    1. Path Sum (root to leaf)
    2. Path Sum II (all paths)
    3. Path Sum III (any path)
    """
    def has_path_sum(root, target):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == target
        return (has_path_sum(root.left, target - root.val) or
                has_path_sum(root.right, target - root.val))
    
    def path_sum_iii(root, target):
        """Count paths that sum to target (can start and end anywhere)"""
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix_sums.get(curr_sum - target, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            prefix_sums[curr_sum] -= 1
            return count
        
        prefix_sums = {0: 1}
        return dfs(root, 0)

def tree_serialization():
    """
    Tree Serialization Patterns:
    1. Level-order serialization
    2. Preorder serialization
    3. Parentheses representation
    """
    def serialize(root):
        """Level-order serialization"""
        if not root:
            return "[]"
        
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        while result[-1] == "null":
            result.pop()
        
        return "[" + ",".join(result) + "]"

def tree_modification():
    """
    Tree Modification Patterns:
    1. Flatten tree to linked list
    2. Convert BST to greater tree
    3. Balance BST
    """
    def flatten_to_linked_list(root):
        """Flatten binary tree to linked list in-place"""
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node in left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Rearrange pointers
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right

def binary_search_tree_tricks():
    """
    Binary Search Tree Tricks:
    1. Validation
    2. Insertion/Deletion
    3. Balancing
    """
    def is_valid_bst(root):
        def validate(node, min_val, max_val):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))

# Interview Tips:
"""
1. Tree Problem Patterns:
   - Traversal (DFS vs BFS)
   - Construction
   - Path finding
   - Tree modification
   - Subtree problems
   - Binary Search Tree properties

2. Common Edge Cases:
   - Empty tree
   - Single node
   - Unbalanced tree
   - Complete binary tree
   - Full binary tree
   - Perfect binary tree

3. Optimization Tips:
   - Use BST properties when possible
   - Consider iterative vs recursive
   - Use level order for breadth-first tasks
   - Use Morris traversal for O(1) space
   - Cache results in global variables

4. Problem-Solving Strategies:
   - Draw the tree
   - Try simple examples
   - Consider all traversal orders
   - Use helper functions for recursion
   - Track parent/path information
   - Use level-by-level processing

5. Time/Space Complexity:
   - Most tree operations: O(n) time
   - Balanced BST operations: O(log n)
   - Recursive space: O(h) where h is height
   - Level order space: O(w) where w is max width
""" 