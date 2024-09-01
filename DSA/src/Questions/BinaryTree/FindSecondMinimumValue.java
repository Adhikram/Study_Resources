package Questions.BinaryTree;

public class FindSecondMinimumValue {

    public int findSecondMinimumValue(TreeNode root) {
        if (root == null)
            return -1;
        if (root.left == null && root.right == null)
            return -1;

        assert root.left != null;
        int left = root.left.val;
        int right = root.right.val;

        if (root.left.val == root.val) {
            left = findSecondMinimumValue(root.left);
        }

        if (root.right.val == root.val) {
            right = findSecondMinimumValue(root.right);
        }

        if (left != -1 && right != -1) {
            return Math.min(left, right);
        } else if (left != -1) {
            return left;
        } else {
            return right;
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(2);
        TreeNode left = new TreeNode(2);
        TreeNode right = new TreeNode(5);
        TreeNode rightLeft = new TreeNode(5);
        TreeNode rightRight = new TreeNode(7);
        root.left = left;
        root.right = right;
        right.left = rightLeft;
        right.right = rightRight;
        FindSecondMinimumValue findSecondMinimumValue = new FindSecondMinimumValue();
        int result = findSecondMinimumValue.findSecondMinimumValue(root);
        System.out.println("Result: " + result);
    }
}
