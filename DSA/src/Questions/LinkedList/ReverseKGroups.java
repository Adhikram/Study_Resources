package Questions.LinkedList;

public class ReverseKGroups {
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

    public ListNode reverseKGroup(ListNode head, int k) {
        // Check if K elements are present
        ListNode curr = head;
        for (int i = 0; i < k; i++) {
            if (curr == null) {
                return head;
            }
            curr = curr.next;
        }
        // Reverse K nodes
        curr = head;
        ListNode prev = null;
        ListNode temp = null;
        int count = 0;
        while (curr != null && count < k) {
            temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
            count++;
        }
        // If next element Presents then attach it to the head
        if (curr != null) {
            head.next = reverseKGroup(curr, k);
        }
        return prev;

    }

    public static void main(String[] args) {
        ReverseKGroups reverse = new ReverseKGroups();
        ListNode head = reverse.new ListNode(1);
        head.next = reverse.new ListNode(2);
        head.next.next = reverse.new ListNode(3);
        head.next.next.next = reverse.new ListNode(4);
        head.next.next.next.next = reverse.new ListNode(5);
        head.next.next.next.next.next = reverse.new ListNode(6);
        ListNode reversed = reverse.reverseKGroup(head, 2);
        while (reversed != null) {
            System.out.println(reversed.val);
            reversed = reversed.next;
        }
    }
}
