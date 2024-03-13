package Questions.LinkedList;

public class FindMiddleElement {
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

    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            System.out.println(slow.val + " " + fast.val);
            fast = fast.next.next;
            if(fast == null){
                return slow;
            }
            slow = slow.next;
        }
        return slow;
    }

    public static void main(String[] args) {
        FindMiddleElement findMiddleElement = new FindMiddleElement();
        ListNode head = findMiddleElement.new ListNode(1);
        head.next = findMiddleElement.new ListNode(2);
        head.next.next = findMiddleElement.new ListNode(3);
        head.next.next.next = findMiddleElement.new ListNode(4);
        head.next.next.next.next = findMiddleElement.new ListNode(5);
        // head.next.next.next.next.next = findMiddleElement.new ListNode(6);
        System.out.println(findMiddleElement.middleNode(head).val);
    }
}
