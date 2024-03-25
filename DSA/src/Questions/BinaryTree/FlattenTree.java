package Questions.BinaryTree;

public class FlattenTree {
    static TreeNode prev = null;

    static void flatten(TreeNode root) {
        if (root == null)
            return;

        flatten(root.right);
        flatten(root.left);

        root.right = prev;
        root.left = null;
        prev = root;
    }

    public static void main(String args[]) {

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right = new TreeNode(5);
        root.right.right = new TreeNode(6);
        root.right.right.left = new TreeNode(7);
        flatten(root);
        while (root.right != null) {
            System.out.print(root.val + "->");
            root = root.right;
        }
        System.out.print(root.val);
    }
}
