package Questions.LinkedList;

import java.util.HashMap;

public class CopyRandomList {
    public Node copyRandomList(Node head) {
        if (head == null)
            return head;
        Node newHead = new Node(head.val);
        Node tail = newHead, temp = head.next;
        HashMap<Node, Node> map = new HashMap<>();
        // Add the original node and the new node to the map
        map.put(head, newHead);
        while (temp != null) {
            Node x = new Node(temp.val);
            tail.next = x;
            tail = x;
            map.put(temp, x);
            temp = temp.next;
        }
        Node t = newHead;
        while (head != null) {
            if (head.random != null) {
                t.random = map.get(head.random);
            }
            t = t.next;
            head = head.next;
        }
        return newHead;
    }
    public Node copyRanNode(Node head) {
        if (head == null)
            return head;
        Node temp = head;
        // Adding new nodes in between the original nodes
        while (temp != null) {
            Node x = new Node(temp.val);
            x.next = temp.next;
            temp.next = x;
            temp = x.next;
        }
        temp = head;
        // Assigning random pointers to the new nodes
        while (temp != null) {
            if (temp.random != null) {
                temp.next.random = temp.random.next;
            }
            temp = temp.next.next;
        }
        // Separating the new nodes from the original nodes
        Node newHead = head.next;
        Node newTemp = newHead;
        temp = head;
        // Restoring the original list
        while (temp != null) {
            temp.next = newTemp.next;
            if (newTemp.next != null) {
                newTemp.next = newTemp.next.next;
            }
            temp = temp.next;
            newTemp = newTemp.next;
        }
        return newHead;
    }

    public static void main(String[] args) {
        Node head = new Node(7);
        head.next = new Node(13);
        head.next.next = new Node(11);
        head.next.next.next = new Node(10);
        head.next.next.next.next = new Node(1);
        head.next.random = head;
        head.next.next.random = head.next.next.next.next;
        head.next.next.next.random = head.next.next;
        head.next.next.next.next.random = head;
        head.next.child = new Node(3);
        head.next.child.next = new Node(8);
        head.next.child.next.next = new Node(4);
        head.next.child.next.random = head.next;
        head.next.child.next.next.random = head.next.next.next;
        Node newHead = new CopyRandomList().copyRandomList(head);
        while (newHead != null) {
            System.out.print(newHead.val + " ");
            if (newHead.random != null)
                System.out.print(newHead.random.val + " ");
            newHead = newHead.next;
            System.out.println();
        }
        Node newHead2 = new CopyRandomList().copyRanNode(head);
        while (newHead2 != null) {
            System.out.print(newHead2.val + " ");
            if (newHead2.random != null)
                System.out.print(newHead2.random.val + " ");
            newHead2 = newHead2.next;
            System.out.println();
        }
    }
}
