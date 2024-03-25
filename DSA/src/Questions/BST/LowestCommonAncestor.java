package Questions.BST;

import Questions.BinaryTree.TreeNode;

public class LowestCommonAncestor {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || p == root || q == root) {
            return root;
        }

        // Go to Left and Right
        TreeNode a = lowestCommonAncestor(root.left, p, q);
        TreeNode b = lowestCommonAncestor(root.right, p, q);

        if (a != null && b != null) {
            return root;
        }
        return (b == null) ? a : b;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        TreeNode left = new TreeNode(5);
        TreeNode right = new TreeNode(1);
        TreeNode leftLeft = new TreeNode(6);
        TreeNode leftRight = new TreeNode(2);
        TreeNode rightLeft = new TreeNode(0);
        TreeNode rightRight = new TreeNode(8);
        TreeNode leftRightLeft = new TreeNode(7);
        TreeNode leftRightRight = new TreeNode(4);
        root.left = left;
        root.right = right;
        left.left = leftLeft;
        left.right = leftRight;
        right.left = rightLeft;
        right.right = rightRight;
        leftRight.left = leftRightLeft;
        leftRight.right = leftRightRight;
        LowestCommonAncestor lowestCommonAncestor = new LowestCommonAncestor();
        TreeNode result = lowestCommonAncestor.lowestCommonAncestor(root, left, right);
        System.out.println("Lowest Common Ancestor: " + result.val);
    }
}
