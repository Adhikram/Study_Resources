package Questions.BinaryTree;

public class NextRightPointers {
    public static class Node {
        int val;
        Node left;
        Node right;
        Node next;

        public Node() {
        }

        public Node(int val) {
            this.val = val;
        }

        public Node(int val, Node left, Node right, Node next) {
            this.val = val;
            this.left = left;
            this.right = right;
            this.next = next;
        }
    }
    public Node connect(Node root) {
        // System.out.println("root: " + root.val);
        if (root == null) return null;

        Node currentLevelStart = root; // Start with the root of the tree

        while (currentLevelStart.left != null) { // While there's a next level
            Node current = currentLevelStart;

            while (current != null) { // Traverse the current level
                current.left.next = current.right; // Connect left child to right child

                if (current.next != null) { // Connect right child to next node's left child
                    current.right.next = current.next.left;
                }

                current = current.next; // Move to the next node in the current level
            }

            currentLevelStart = currentLevelStart.left; // Move down to the next level
        }

        System.out.println("root: " + root.val);
        return root; // Return the modified tree
    }
    public static void main(String[] args) {
        NextRightPointers nextRightPointers = new NextRightPointers();
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);
        // Tree
        //      1
        //    /  \
        //   2    3
        //  / \  / \
        // 4   5 6  7
        Node result = nextRightPointers.connect(root);
        // Traverse through the tree and print the next pointers
        while (result != null) {
            Node current = result;
            while (current != null) {
                System.out.print(current.val + " -> ");
                current = current.next;
            }
            System.out.println("null");
            result = result.left;
        }

    }
}
