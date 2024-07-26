package Questions.Graph;

/*
https://leetcode.com/problems/validate-binary-tree-nodes/description/
 You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:


Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
 

Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1
Time complexity: O(n)
Space complexity: O(n)
 */
public class ValidateBInaryNodes {
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        int[] inDegree = new int[n];
        int root = -1;
        for (int child : leftChild) {
            if (child != -1 && ++inDegree[child] == 2) {
                return false;
            }
        }
        for (int child : rightChild) {
            if (child != -1 && ++inDegree[child] == 2) {
                return false;
            }
        }
        for (int i = 0; i < n; ++i) {
            if (inDegree[i] == 0) {
                if (root == -1) {
                    root = i;
                } else {
                    return false;
                }
            }
        }
        if (root == -1) {
            return false;
        }
        return countNodes(root, leftChild, rightChild) == n;
    }

    private int countNodes(int root, int[] leftChild, int[] rightChild) {
        if (root == -1 || leftChild[root] == root || rightChild[root] == root) {
            return 0;
        }
        return 1 + countNodes(leftChild[root], leftChild, rightChild) +
                countNodes(rightChild[root], leftChild, rightChild);
    }
    public static void main(String[] args) {
        ValidateBInaryNodes validateBInaryNodes = new ValidateBInaryNodes();
        System.out.println(validateBInaryNodes.validateBinaryTreeNodes(4, new int[] { 1, -1, 3, -1 }, new int[] { 2, -1, -1, -1 })); // true
        System.out.println(validateBInaryNodes.validateBinaryTreeNodes(4, new int[] { 1, -1, 3, -1 }, new int[] { 2, 3, -1, -1 })); // false
        System.out.println(validateBInaryNodes.validateBinaryTreeNodes(2, new int[] { 1, 0 }, new int[] { -1, -1 })); // false
    }
}
