package Questions.StackQueue;
import java.util.PriorityQueue;
/*
 https://leetcode.com/problems/find-median-from-data-stream/description/

 Time Complexity:
addNum: O(log n) for inserting a number into the heap.
findMedian: O(1) for retrieving the median.
Space Complexity: O(n) for storing the numbers in the heaps.

 */
public class FindMedianInaDataStream {
    PriorityQueue<Integer> maxHeap; // left half
    PriorityQueue<Integer> minHeap; // right half

    public FindMedianInaDataStream() {
        maxHeap = new PriorityQueue<>((a, b) -> b - a);
        minHeap = new PriorityQueue<>();
    }

    public void addNum(int num) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.add(num);
        } else {
            minHeap.add(num);
        }
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.add(maxHeap.poll());
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.add(minHeap.poll());
        }
    }

    public double findMedian() {
        if (!maxHeap.isEmpty() && maxHeap.size() == minHeap.size()) {
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
        return maxHeap.isEmpty()? 0 : maxHeap.peek();
    }

    public static void main(String[] args) {
        FindMedianInaDataStream obj = new FindMedianInaDataStream();
        System.out.println(obj.findMedian());
        obj.addNum(1);
        obj.addNum(2);
        System.out.println(obj.findMedian());
        obj.addNum(3);
        System.out.println(obj.findMedian());
    }

}
