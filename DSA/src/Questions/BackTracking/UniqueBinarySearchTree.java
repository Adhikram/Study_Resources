package Questions.BackTracking;

import java.util.LinkedList;
import java.util.List;

/*
https://leetcode.com/problems/unique-binary-search-trees-ii/
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.


Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 8
Time Complexity: O(4^n)
Space Complexity: O(4^n)

Recursive Approach:
Use a recursive function generateSubtrees to generate all possible subtrees for a given range of values [s, e].
For each value i in the range, consider it as the root and recursively generate all possible left subtrees from [s, i-1] 
and right subtrees from [i+1, e].
Combine each left subtree with each right subtree to form the full tree with i as the root.

Base Case for Recursion:
If s > e, return a list containing null to represent an empty tree.

Combining Subtrees:
For each value i in the range, generate all possible left and right subtrees.
Combine each left subtree with each right subtree to form the full tree and add it to the result list.

Handling Edge Cases:
If n is 0, return an empty list as there are no trees to generate.
 */
public class UniqueBinarySearchTree {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<TreeNode> generateTrees(int n) {
        return generateSubtrees(1, n);
    }

    private List<TreeNode> generateSubtrees(int s, int e) {
        List<TreeNode> res = new LinkedList<TreeNode>();
        if (s > e) {
            res.add(null); // empty tree
            return res;
        }

        for (int i = s; i <= e; ++i) {
            List<TreeNode> leftSubtrees = generateSubtrees(s, i - 1);
            List<TreeNode> rightSubtrees = generateSubtrees(i + 1, e);

            for (TreeNode left : leftSubtrees) {
                for (TreeNode right : rightSubtrees) {
                    TreeNode root = new TreeNode(i, left, right);
                    res.add(root);
                }
            }
        }
        return res;
    }
    public static void main(String[] args) {
        UniqueBinarySearchTree uniqueBinarySearchTree = new UniqueBinarySearchTree();
        List<TreeNode> result = uniqueBinarySearchTree.generateTrees(3);
        System.out.println(result.size());
    }
}
