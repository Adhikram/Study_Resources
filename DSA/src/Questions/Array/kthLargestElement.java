package Questions.Array;

import java.util.PriorityQueue;

public class kthLargestElement {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int num: nums){
            pq.add(num);
            if(pq.size() > k){
                // We need to remove the top element
                pq.poll();
            }

        }

        return pq.peek();
    }
    public static void main(String[] args) {
        kthLargestElement kthLargestElement = new kthLargestElement();
        int[] nums = {3,2,1,5,6,4};
        int k = 2;
        System.out.println(kthLargestElement.findKthLargest(nums, k)); 
    }
}
