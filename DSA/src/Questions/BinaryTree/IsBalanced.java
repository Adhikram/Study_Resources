package Questions.BinaryTree;

public class IsBalanced {
    // Method to check if a binary tree is height-balanced
    public static boolean isBalanced(TreeNode root) {
        // A binary tree is height-balanced if the heights of the two subtrees of any
        // node never differ by more than 1
        // If dfsHeight returns -1, the binary tree is not height-balanced
        return dfsHeight(root) != -1;
    }

    // Method to find the height of a binary tree using depth-first search
    static int dfsHeight(TreeNode root) {
        // If the current node is null, return 0
        if (root == null)
            return 0;

        // Find the height of the left subtree
        int leftHeight = dfsHeight(root.left);
        // If the left subtree is not height-balanced, return -1
        if (leftHeight == -1)
            return -1;
        // Find the height of the right subtree
        int rightHeight = dfsHeight(root.right);
        // If the right subtree is not height-balanced, return -1
        if (rightHeight == -1)
            return -1;

        // If the heights of the left and right subtrees differ by more than 1, return
        // -1
        if (Math.abs(leftHeight - rightHeight) > 1)
            return -1;
        // Return the height of the binary tree
        return Math.max(leftHeight, rightHeight) + 1;
    }

    // Main method
    public static void main(String[] args) {
        // Create a binary tree
        TreeNode root = new TreeNode(1);
        TreeNode right = new TreeNode(2);
        TreeNode rightLeft = new TreeNode(3);
        root.right = right;
        right.left = rightLeft;
        // Check if the binary tree is height-balanced
        System.out.println("Is the tree balanced: " + isBalanced(root));
    }
}