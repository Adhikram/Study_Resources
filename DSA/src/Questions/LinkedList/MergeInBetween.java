package Questions.LinkedList;

public class MergeInBetween {
    public static Node mergeInBetween(Node list1, int a, int b, Node list2) {
        Node start = list1, end = list1;
        int i = 1;
        while (i <= b) {
            if (i++ == a) start = end;
            end = end.next;
        }
        start.next = list2;
        while (list2.next != null) list2 = list2.next;
        list2.next = end.next;
        return list1;
    }

    public static void main(String[] args) {
        Node list1 = new Node(0);
        list1.next = new Node(1);
        list1.next.next = new Node(2);
        list1.next.next.next = new Node(3);
        list1.next.next.next.next = new Node(4);
        list1.next.next.next.next.next = new Node(5);
        Node list2 = new Node(1000000);
        list2.next = new Node(1000001);
        list2.next.next = new Node(1000002);
        Node res = mergeInBetween(list1, 3, 4, list2);
        while (res != null) {
            System.out.print(res.val + " ");
            res = res.next;
        }
    }
}
