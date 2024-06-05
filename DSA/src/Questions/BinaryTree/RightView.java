package Questions.BinaryTree;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class RightView {

    public List<Integer> rightSideView(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int elem = 0; elem < size; elem++) {
                TreeNode curr = q.poll();
                assert curr != null;
                if (elem == size - 1) {
                    result.add(curr.val);
                }

                if (curr.left != null) {
                    q.add(curr.left);
                }
                ;
                if (curr.right != null) {
                    q.add(curr.right);
                }
                ;

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
        RightView rightView = new RightView();
        List<Integer> result = rightView.rightSideView(root);
        System.out.println("Right View: " + result);
    }
}
