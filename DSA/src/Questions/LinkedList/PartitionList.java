package Questions.LinkedList;
/*
https://leetcode.com/problems/partition-list/description/
 Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
Time Complexity: O(N)
Space Complexity: O(1)
 */
public class PartitionList {
    public Node partition(Node head, int x) {
        Node lessHead = new Node(0); // Dummy head for the 'less than x' list
        Node greaterHead = new Node(0); // Dummy head for the 'greater than or equal to x' list
        Node less = lessHead; // Pointer for the 'less than x' list
        Node greater = greaterHead; // Pointer for the 'greater than or equal to x' list

        while (head != null) {
            if (head.val < x) {
                less.next = head; // Add to 'less' list
                less = less.next;
            } else {
                greater.next = head; // Add to 'greater' list
                greater = greater.next;
            }
            head = head.next;
        }

        greater.next = null; // End the 'greater' list
        less.next = greaterHead.next; // Concatenate 'less' list with 'greater' list

        return lessHead.next; // Return the concatenated list, skipping the dummy head

    }
    public static void main(String[] args) {
        
    }
}
