package Questions.BinaryTree;

public class Diameter {

    public int maxDepth(TreeNode root, int[] d) {
        if (root == null) {
            return 0;
        }
        int ld = maxDepth(root.left, d);
        int rd = maxDepth(root.right, d);
        d[0] = Math.max(d[0], (ld + rd));
        return 1 + Math.max(ld, rd);
    }

    public int diameterOfBinaryTree(TreeNode root) {
        int[] d = new int[1];
        maxDepth(root, d);
        return d[0];
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        TreeNode right = new TreeNode(2);
        TreeNode rightLeft = new TreeNode(3);
        root.right = right;
        right.left = rightLeft;
        Diameter diameter = new Diameter();
        int result = diameter.diameterOfBinaryTree(root);
        System.out.println("Diameter of the tree: " + result);
    }
}
