package Questions.LinkedList;

public class MergeTwoSortedList {
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

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        if (list1.val < list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }

    public static void main(String[] args) {
        MergeTwoSortedList mergeTwoSortedList = new MergeTwoSortedList();
        ListNode list1 = mergeTwoSortedList.new ListNode(1);
        list1.next = mergeTwoSortedList.new ListNode(2);
        list1.next.next = mergeTwoSortedList.new ListNode(4);
        ListNode list2 = mergeTwoSortedList.new ListNode(1);
        list2.next = mergeTwoSortedList.new ListNode(3);
        list2.next.next = mergeTwoSortedList.new ListNode(4);
        ListNode merged = mergeTwoSortedList.mergeTwoLists(list1, list2);
        while (merged != null) {
            System.out.println(merged.val);
            merged = merged.next;
        }
    }
}
