package Questions.LinkedList;

public class FindPalindrom {
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

    public boolean isPalindrome(ListNode head) {
        ListNode head1 = head;
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        // Reverse the second half
        ListNode prev = slow;
        slow = slow.next;
        prev.next = null;
        ListNode nextElem = null;
        while (slow != null) {
            nextElem = slow.next;
            slow.next = prev;
            prev = slow;
            slow = nextElem;
        }

        fast = head;
        slow = prev;
        while (slow != null && fast != null) {
            if (slow.val != fast.val) {
                return false;
            }
            slow = slow.next;
            fast = fast.next;
        }
        return true;
    }

    public static void main(String[] args) {
        FindPalindrom palindrom = new FindPalindrom();
        ListNode head = palindrom.new ListNode(1);
        head.next = palindrom.new ListNode(2);
        head.next.next = palindrom.new ListNode(3);
        head.next.next.next = palindrom.new ListNode(4);
        head.next.next.next.next = palindrom.new ListNode(3);
        head.next.next.next.next.next = palindrom.new ListNode(2);
        head.next.next.next.next.next.next = palindrom.new ListNode(1);
        System.out.println(palindrom.isPalindrome(head));
    }
}
