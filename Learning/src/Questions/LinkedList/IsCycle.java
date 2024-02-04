package Questions.LinkedList;

public class IsCycle {
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

    public boolean hasCycle(ListNode head) {

        if (head == null || head.next == null) {
            return false;
        }
        ListNode slow = head;
        ListNode fast = head.next;
        while (slow.next != null && fast.next != null) {
            slow = slow.next;
            if (fast.next.next == null) {
                break;
            }
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;

    }

    public static void main(String[] args) {
        IsCycle isCycle = new IsCycle();
        ListNode head = isCycle.new ListNode(3);
        head.next = isCycle.new ListNode(2);
        head.next.next = isCycle.new ListNode(0);
        head.next.next.next = isCycle.new ListNode(-4);
        head.next.next.next.next = head.next;
        System.out.println(isCycle.hasCycle(head));
    }

}
