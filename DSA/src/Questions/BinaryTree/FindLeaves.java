package Questions.BinaryTree;

import java.util.ArrayList;
import java.util.List;

/*
https://leetcode.com/problems/find-leaves-of-binary-tree/description/
 Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
Time Complexity: O(N)
Space Complexity: O(N)
 */
public class FindLeaves {
    public static List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        height(root, res);
        return res;
    }

    private static int height(TreeNode node, List<List<Integer>> res) {
        if (null == node)
            return -1;
        int level = 1 + Math.max(height(node.left, res), height(node.right, res));
        if (res.size() < level + 1)
            res.add(new ArrayList<>());
        res.get(level).add(node.val);
        return level;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(6);
        List<List<Integer>> result = findLeaves(root);
        for (List<Integer> list : result) {
            for (int num : list) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
