package Questions.LinkedList;

import java.util.Stack;

public class Flatten {
    public Node flattenRecursive(Node head) {
        if (head == null) {
            return null;
        }

        Node current = head;
        while (current != null) {
            if (current.child != null) {
                Node nextNode = current.next;

                // Connect current node to the child list
                current.next = flattenRecursive(current.child);
                current.next.prev = current;
                current.child = null;

                // Find the tail of the child list
                Node tail = current.next;
                while (tail.next != null) {
                    tail = tail.next;
                }

                // Connect the tail of the child list to the next node
                tail.next = nextNode;
                if (nextNode != null) {
                    nextNode.prev = tail;
                }
            }

            current = current.next;
        }

        return head;
    }


    public Node flatten(Node head) {
        if (head == null) {
            return null;
        }

        Node current = head;
        Stack<Node> stack = new Stack<>();

        while (current != null) {
            if (current.child != null) {
                Node nextNode = current.next;

                // Connect current node to the child list
                current.next = current.child;
                current.child.prev = current;
                current.child = null;

                // Push the next node onto the stack for later processing
                if (nextNode != null) {
                    stack.push(nextNode);
                }
            } else if (current.next == null && !stack.isEmpty()) {
                // If there are no more nodes in the current level,
                // pop a node from the stack and connect it to the current node
                Node nextNode = stack.pop();
                current.next = nextNode;
                nextNode.prev = current;
            }

            current = current.next;
        }

        return head;
    }

    public static void main(String[] args) {
        Node head = new Node(1);
        Node second = new Node(2);
        Node third = new Node(3);
        Node fourth = new Node(4);
        Node fifth = new Node(5);
        Node sixth = new Node(6);
        Node seventh = new Node(7);
        Node eighth = new Node(8);
        Node ninth = new Node(9);
        Node tenth = new Node(10);
        Node eleventh = new Node(11);
        Node twelfth = new Node(12);

        head.next = second;
        second.prev = head;
        second.next = third;
        third.prev = second;
        third.next = fourth;
        fourth.prev = third;
        fourth.next = fifth;
        fifth.prev = fourth;
        fifth.next = sixth;
        sixth.prev = fifth;
        sixth.next = seventh;
        seventh.prev = sixth;
        third.child = eighth;
        eighth.next = ninth;
        ninth.prev = eighth;
        ninth.next = tenth;
        tenth.prev = ninth;
        tenth.next = eleventh;
        eleventh.prev = tenth;
        eleventh.next = twelfth;
        twelfth.prev = eleventh;

        Flatten flatten = new Flatten();
        Node result = flatten.flatten(head);
        Node resultRecursive = flatten.flattenRecursive(head);

        while (result != null) {
            System.out.print(result.val + " ");
            result = result.next;
        }
        System.out.println();
        while (resultRecursive != null) {
            System.out.print(resultRecursive.val + " ");
            resultRecursive = resultRecursive.next;
            
        }
    }
}
