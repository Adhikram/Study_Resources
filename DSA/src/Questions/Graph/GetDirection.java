package Questions.Graph;
/*
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
 You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
Time Complexity: O(n)
Space Complexity: O(n)
 */
public class GetDirection {
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

        private boolean find(TreeNode n, int val, StringBuilder sb) {
            if (n.val == val)
                return true;
            if (n.left != null && find(n.left, val, sb))
                sb.append("L");
            else if (n.right != null && find(n.right, val, sb))
                sb.append("R");
            return sb.length() > 0;
        }

        public String getDirections(TreeNode root, int startValue, int destValue) {
            StringBuilder s = new StringBuilder(), d = new StringBuilder();
            find(root, startValue, s);
            find(root, destValue, d);
            // To Find the LCS
            int i = 0, max_i = Math.min(d.length(), s.length());
            while (i < max_i && s.charAt(s.length() - i - 1) == d.charAt(d.length() - i - 1))
                ++i;
            return "U".repeat(s.length() - i) + d.reverse().toString().substring(i);
        }
        
    }
    public static void main(String[] args) {
        GetDirection getDirection = new GetDirection();
        TreeNode root = getDirection.new TreeNode(5);
        root.left = getDirection.new TreeNode(1);
        root.right = getDirection.new TreeNode(2);
        root.left.left = getDirection.new TreeNode(3);
        root.right.right = getDirection.new TreeNode(6);
        root.right.left = getDirection.new TreeNode(4);
        System.out.println(root.getDirections(root, 3, 6));
    }
}
