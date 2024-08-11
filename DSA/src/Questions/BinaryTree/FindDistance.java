package Questions.BinaryTree;

/*
https://leetcode.com/problems/find-distance-in-a-binary-tree/description/
 Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

The distance between two nodes is the number of edges on the path from one to the other.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
Output: 3
Explanation: There are 3 edges between 5 and 0: 5-3-1-0.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
Output: 2
Explanation: There are 2 edges between 5 and 7: 5-2-7.
Example 3:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
Output: 0
Explanation: The distance between a node and itself is 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
All Node.val are unique.
p and q are values in the tree.
Explanation:
findLCA Method: This method recursively searches for the LCA of nodes p and q. If either p or q matches the current root, it returns the root.
 If both p and q are found in the left and right subtrees, the current root is the LCA.

findLevel Method: This method calculates the distance from the LCA to the given node by counting the levels down to that node.

findDistance Method: This is the main method that first finds the LCA and then calculates the total distance as the sum of distances 
from the LCA to p and q.

Time Complexity:
The time complexity of this approach is O(N), where N is the number of nodes in the tree, 
since we may potentially visit every node twice (once for finding the LCA and once for calculating the distance).

Space Complexity:
The space complexity is O(H), where H is the height of the tree, which corresponds to the maximum depth of the recursion stack.

 */
public class FindDistance {
    public int findDistance(TreeNode root, int p, int q) {
        TreeNode lca = findLCA(root, p, q);
        int distanceP = findLevel(lca, p, 0);
        int distanceQ = findLevel(lca, q, 0);
        return distanceP + distanceQ;
    }

    // Helper method to find the Lowest Common Ancestor (LCA)
    private TreeNode findLCA(TreeNode root, int p, int q) {
        if (root == null)
            return null;
        if (root.val == p || root.val == q)
            return root;

        TreeNode left = findLCA(root.left, p, q);
        TreeNode right = findLCA(root.right, p, q);

        if (left != null && right != null)
            return root;
        return (left != null) ? left : right;
    }

    // Helper method to find the distance from the LCA to a given node
    private int findLevel(TreeNode root, int val, int level) {
        if (root == null)
            return -1;
        if (root.val == val)
            return level;

        int left = findLevel(root.left, val, level + 1);
        if (left == -1) {
            return findLevel(root.right, val, level + 1);
        }
        return left;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(5);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(6);
        root.left.right = new TreeNode(2);
        root.right.left = new TreeNode(0);
        root.right.right = new TreeNode(8);
        root.left.right.left = new TreeNode(7);
        root.left.right.right = new TreeNode(4);

        FindDistance findDistance = new FindDistance();
        System.out.println(findDistance.findDistance(root, 5, 0)); // Output: 3
        System.out.println(findDistance.findDistance(root, 5, 7)); // Output: 2
        System.out.println(findDistance.findDistance(root, 5, 5)); // Output: 0
    }
}
