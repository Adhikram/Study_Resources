package Questions.LinkedList;

public class RemoveNthNode {
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

    public ListNode ref(ListNode head, int[] n) {
        if (head == null) {
            return null;
        }
        head.next = ref(head.next, n);
        n[0]--;
        if (n[0] == 0) {
            return head.next;
        }
        return head;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        return ref(head, new int[] { n });
    }

    public static void main(String[] args) {
        RemoveNthNode removeNthNode = new RemoveNthNode();
        ListNode head = removeNthNode.new ListNode(1);
        head.next = removeNthNode.new ListNode(2);
        head.next.next = removeNthNode.new ListNode(3);
        head.next.next.next = removeNthNode.new ListNode(4);
        head.next.next.next.next = removeNthNode.new ListNode(5);
        ListNode result = removeNthNode.removeNthFromEnd(head, 2);
        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }
}
