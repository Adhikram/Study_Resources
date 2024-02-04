package Questions.LinkedList;

public class AddTwoNumbers {
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

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode head = new ListNode(0);
        ListNode result = head;
        while (l1 != null || l2 != null) {
            int l1_val = 0;
            int l2_val = 0;
            if (l1 != null) {
                l1_val = l1.val;
            }
            if (l2 != null) {
                l2_val = l2.val;
            }
            int sum = l1_val + l2_val + carry;
            if (sum > 9) {
                carry = 1;
            } else {
                carry = 0;
            }
            head.next = new ListNode(sum % 10);
            head = head.next;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        if (carry > 0) {
            head.next = new ListNode(carry);
        }
        return result.next;
    }

    public static void main(String[] args) {
        AddTwoNumbers addTwoNumbers = new AddTwoNumbers();
        ListNode l1 = addTwoNumbers.new ListNode(2);
        l1.next = addTwoNumbers.new ListNode(4);
        l1.next.next = addTwoNumbers.new ListNode(3);
        ListNode l2 = addTwoNumbers.new ListNode(5);
        l2.next = addTwoNumbers.new ListNode(6);
        l2.next.next = addTwoNumbers.new ListNode(4);
        ListNode result = addTwoNumbers.addTwoNumbers(l1, l2);
        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }
}
