package Questions.StackQueue;

import java.util.LinkedList;
import java.util.Queue;

/*
 https://leetcode.com/problems/implement-stack-using-queues/description/
 Time Complexity:
Push: O(1) for adding an element to the stack.
Pop: O(1) for removing the top element from the stack.
Top: O(1) for getting the top element from the stack.
IsEmpty: O(1) for checking if the stack is empty.
IsFull: O(1) for checking if the stack is full.
Space Complexity: O(n) for storing the elements in the array, where n is the capacity of the stack.
 */
public class StackUsingQueue {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();

    public StackUsingQueue() {

    }

    public void push(int x) {
        while (q1.size() != 0) {
            q2.add(q1.poll());
        }
        q1.add(x);
        while (q2.size() != 0) {
            q1.add(q2.poll());
        }
    }

    public int pop() {
        return q1.poll();
    }

    public int top() {
        return q1.peek();
    }

    public boolean empty() {
        return q1.size() == 0;
    }

    public static void main(String[] args) {
        StackUsingQueue stack = new StackUsingQueue();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        System.out.println("Top element of the stack: " + stack.top());
    }
}
