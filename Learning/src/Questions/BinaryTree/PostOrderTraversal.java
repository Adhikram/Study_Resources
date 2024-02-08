package Questions.BinaryTree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class PostOrderTraversal {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }

    }

    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> st = new Stack<>();
        TreeNode lastVisited = null;

        while (root != null || !st.isEmpty()) {
            while (root != null) {
                st.push(root);
                root = root.left;
            }

            TreeNode current = st.peek();

            // If the right subtree is null or already visited, process the current node
            if (current.right == null || current.right == lastVisited) {
                result.add(current.val);
                st.pop();
                lastVisited = current;
            } else {
                // Move to the right subtree
                root = current.right;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        TreeNode right = new TreeNode(2);
        TreeNode rightLeft = new TreeNode(3);
        root.right = right;
        right.left = rightLeft;
        PostOrderTraversal postOrderTraversal = new PostOrderTraversal();
        List<Integer> result = postOrderTraversal.postorderTraversal(root);
        System.out.println("PostOrder Traversal: " + result);
    }
}
