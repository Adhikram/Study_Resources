package Questions.BinaryTree;

public class KthSmallestElement {
    public int inOrder(TreeNode root, int[] k) {
        if (root == null)
            return -1;
        int left = inOrder(root.left, k);
        k[0]--;
        if (k[0] == 0)
            return root.val;
        int right = inOrder(root.right, k);
        if (left != -1) {
            return left;
        } else {
            return right;
        }

    }

    public int kthSmallest(TreeNode root, int k) {
        return inOrder(root, new int[] { k });
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        TreeNode left = new TreeNode(1);
        TreeNode right = new TreeNode(4);
        TreeNode leftRight = new TreeNode(2);
        root.left = left;
        root.right = right;
        left.right = leftRight;
        KthSmallestElement kthSmallestElement = new KthSmallestElement();
        int result = kthSmallestElement.kthSmallest(root, 1);
        System.out.println("Result: " + result);
    }
}
