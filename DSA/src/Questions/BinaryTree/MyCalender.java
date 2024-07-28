package Questions.BinaryTree;
/*
https://leetcode.com/problems/my-calendar-i/description/
 You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
Time Complexity: O(logn)
Space Complexity: O(n)
 */
class MyCalendar {
    class Node {
        int start, end;
        Node left;
        Node right;

        public Node(int start, int end) {
            this.start = start;
            this.end = end;
            left = null;
            right = null;
        }
    }

    Node root;

    public MyCalendar() {
        this.root = null;
    }

    public boolean insert(Node root, int first, int last) {
        if (root.start >= last) {
            if (root.left == null) {
                root.left = new Node(first, last);
                return true;
            } else {
                return insert(root.left, first, last);
            }
        } else if (root.end <= first) {
            if (root.right == null) {
                root.right = new Node(first, last);
                return true;
            } else {
                return insert(root.right, first, last);
            }
        }
        return false;
    }

    public boolean book(int start, int end) {
        if (root == null) {
            root = new Node(start, end);
            return true;
        } else {
            return insert(root, start, end);
        }
    }
    public static void main(String[] args) {
        MyCalendar myCalendar = new MyCalendar();
        System.out.println(myCalendar.book(10, 20));
        System.out.println(myCalendar.book(15, 25));
        System.out.println(myCalendar.book(20, 30));
    }
}
