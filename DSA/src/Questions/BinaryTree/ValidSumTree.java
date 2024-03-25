package Questions.BinaryTree;

public class ValidSumTree {
    public static boolean checkTree(TreeNode root) {
        if (root == null)
            return true;
        boolean left = checkTree(root.left);
        if (!left)
            return false;
        boolean right = checkTree(root.right);
        if (!right)
            return false;
        int leftSum = root.left == null ? 0 : root.left.val;
        int rightSum = root.right == null ? 0 : root.right.val;
        return root.val == leftSum + rightSum;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(26);
        TreeNode left = new TreeNode(10);
        TreeNode right = new TreeNode(3);
        TreeNode leftLeft = new TreeNode(4);
        TreeNode leftRight = new TreeNode(6);
        TreeNode rightRight = new TreeNode(3);
        root.left = left;
        root.right = right;
        left.left = leftLeft;
        left.right = leftRight;
        right.right = rightRight;
        boolean result = checkTree(root);
        System.out.println("Is the tree a valid sum tree: " + result);
    }
}