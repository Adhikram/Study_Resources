package Questions.LinkedList;

public class DeleteNodeSpecial {
    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }

    public static void main(String[] args) {
        DeleteNodeSpecial deleteNodeSpecial = new DeleteNodeSpecial();
        ListNode head = deleteNodeSpecial.new ListNode(1);
        head.next = deleteNodeSpecial.new ListNode(2);
        head.next.next = deleteNodeSpecial.new ListNode(3);
        head.next.next.next = deleteNodeSpecial.new ListNode(4);
        head.next.next.next.next = deleteNodeSpecial.new ListNode(5);
        deleteNodeSpecial.deleteNode(head.next.next);
        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }
}
