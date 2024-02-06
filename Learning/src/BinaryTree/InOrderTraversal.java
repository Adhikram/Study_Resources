package BinaryTree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import javax.swing.tree.TreeNode;

public class InOrderTraversal {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }

    }

    

    public List<Integer> inOrderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> st = new Stack<>();
        while (root != null || st.size() != 0) {
            while (root != null) {
                st.push(root);
                root = root.left;
            }

            root = st.peek();
            st.pop();
            result.add(root.val);
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
        InOrderTraversal inOrderTraversal = new InOrderTraversal();
        List<Integer> result = inOrderTraversal.inOrderTraversal(root);
        System.out.println("InOrder Traversal: " + result);
    }
}
