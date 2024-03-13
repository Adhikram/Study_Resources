package Questions.BST;

import java.util.HashMap;

public class FindTargetSum {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }

    }

    public boolean inOrder(TreeNode root, HashMap<Integer, Boolean> hash, int k) {
        if (root == null)
            return false;

        boolean left = inOrder(root.left, hash, k);
        if (left || hash.containsKey(k - root.val)) {
            return true;
        }
        hash.put(root.val, true);
        return inOrder(root.right, hash, k);
    }

    public boolean findTarget(TreeNode root, int k) {
        return inOrder(root, new HashMap<Integer, Boolean>(), k);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(5);
        TreeNode left = new TreeNode(3);
        TreeNode right = new TreeNode(6);
        TreeNode leftLeft = new TreeNode(2);
        TreeNode leftRight = new TreeNode(4);
        TreeNode rightRight = new TreeNode(7);
        root.left = left;
        root.right = right;
        left.left = leftLeft;
        left.right = leftRight;
        right.right = rightRight;
        FindTargetSum findTargetSum = new FindTargetSum();
        boolean result = findTargetSum.findTarget(root, 9);
        System.out.println("Result: " + result);
    }
}
