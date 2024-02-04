package Questions.LinkedList;

public class GetIntersection {
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

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode aPointer = headA;
        ListNode bPointer = headB;
        while (aPointer != null || bPointer != null) {
            if (aPointer == null) {
                aPointer = headB;
            } else {
                aPointer = aPointer.next;
            }
            if (bPointer == null) {
                bPointer = headA;
            } else {
                bPointer = bPointer.next;
            }
        }
        return bPointer;
    }

    public static void main(String[] args) {
        GetIntersection getIntersection = new GetIntersection();
        ListNode headA = getIntersection.new ListNode(4);
        headA.next = getIntersection.new ListNode(1);
        headA.next.next = getIntersection.new ListNode(8);
        headA.next.next.next = getIntersection.new ListNode(4);
        headA.next.next.next.next = getIntersection.new ListNode(5);
        ListNode headB = getIntersection.new ListNode(5);
        headB.next = getIntersection.new ListNode(0);
        headB.next.next = getIntersection.new ListNode(1);
        headB.next.next.next = headA.next.next;
        headB.next.next.next.next = headA.next.next.next;
        headB.next.next.next.next.next = headA.next.next.next.next;
        System.out.println(getIntersection.getIntersectionNode(headA, headB).val);
    }
}
