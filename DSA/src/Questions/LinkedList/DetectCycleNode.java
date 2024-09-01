package Questions.LinkedList;
/*
 https://leetcode.com/problems/linked-list-cycle-ii/description/
 */
public class DetectCycleNode {
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

    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                break;
            }
        }
        if (fast == null || fast.next == null)
            return null;
        while (head != slow) {
            slow = slow.next;
            head = head.next;
        }
        return head;

    }

    public static void main(String[] args) {
        DetectCycleNode detectCycleNode = new DetectCycleNode();
        ListNode head = detectCycleNode.new ListNode(1);
        head.next = detectCycleNode.new ListNode(2);
        head.next.next = detectCycleNode.new ListNode(3);
        head.next.next.next = detectCycleNode.new ListNode(4);
        head.next.next.next.next = detectCycleNode.new ListNode(5);
        head.next.next.next.next.next = detectCycleNode.new ListNode(6);
        head.next.next.next.next.next.next = head.next.next;
        ListNode cycleNode = detectCycleNode.detectCycle(head);
        System.out.println(cycleNode.val);
    }
}
