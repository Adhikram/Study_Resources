package Questions.LinkedList;

public class Reverse {

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

    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }
        return prev;
    }

    public static void main(String[] args) {
        Reverse reverse = new Reverse();
        ListNode head = reverse.new ListNode(1);
        head.next = reverse.new ListNode(2);
        head.next.next = reverse.new ListNode(3);
        head.next.next.next = reverse.new ListNode(4);
        head.next.next.next.next = reverse.new ListNode(5);
        head.next.next.next.next.next = reverse.new ListNode(6);
        ListNode reversed = reverse.reverseList(head);
        while (reversed != null) {
            System.out.println(reversed.val);
            reversed = reversed.next;
        }
    }
}
