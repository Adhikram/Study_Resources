package Questions.BinaryTree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class PreOrderTraversal {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }

    }
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> st = new Stack<>();

        while (root != null || !st.isEmpty()) {
            while (root != null) {
                result.add(root.val);  // Process the current node
                st.push(root);
                root = root.left;
            }

            root = st.pop();
            root = root.right;
        }

        return result;
    }
    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        TreeNode right = new TreeNode(2);
        TreeNode rightLeft = new TreeNode(3);
        root.right = right;
        right.left = rightLeft;
        PreOrderTraversal preOrderTracersal = new PreOrderTraversal();
        List<Integer> result = preOrderTracersal.preorderTraversal(root);
        System.out.println("PreOrder Traversal: " + result);
    }
}
