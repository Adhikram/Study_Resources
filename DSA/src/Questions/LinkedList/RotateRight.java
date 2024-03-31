package Questions.LinkedList;

public class RotateRight {
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

    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) {
            return null;
        }
        ListNode last = head;
        int length = 1;
        while (last.next != null) {
            last = last.next;
            length++;
        }
        k = length - (k % length) - 1;
        System.out.println(k);
        last.next = head;
        while (k-- > 0) {
            head = head.next;
        }
        ListNode result = head.next;
        head.next = null;
        return result;
    }

    public static void main(String[] args) {
        RotateRight rotateRight = new RotateRight();
        ListNode head = rotateRight.new ListNode(1);
        head.next = rotateRight.new ListNode(2);
        head.next.next = rotateRight.new ListNode(3);
        head.next.next.next = rotateRight.new ListNode(4);
        head.next.next.next.next = rotateRight.new ListNode(5);
        ListNode result = rotateRight.rotateRight(head, 2);
        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }
}
