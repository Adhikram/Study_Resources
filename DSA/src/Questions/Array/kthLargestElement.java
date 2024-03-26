package Questions.Array;

import java.util.PriorityQueue;

public class kthLargestElement {
    public int quickSelect(int[] nums, int k, int left, int right) {
        int pivot = nums[right];
        int i = left;
        // We will place all the elements smaller than pivot to the left of pivot
        for (int j = left; j < right; j++) {
            if (nums[j] < pivot) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
            }
        }
        // Swap the pivot element with the element at i
        int temp = nums[i];
        nums[i] = nums[right];
        nums[right] = temp;

        if (i == k) {
            return nums[i];
        } else if (i < k) {
            return quickSelect(nums, k, i + 1, right);
        } else {
            return quickSelect(nums, k, left, i - 1);
        }
    }
    /*
     * Time complexity: O(n) Space complexity: O(n)
     */

    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num : nums) {
            pq.add(num);
            if (pq.size() > k) {
                // We need to remove the top element
                pq.poll();
            }

        }

        return pq.peek();
    }
    /*
     * Time complexity: O(nlogk) Space complexity: O(k)
     */

    public static void main(String[] args) {
        kthLargestElement kthLargestElement = new kthLargestElement();
        int[] nums = { 3, 2, 1, 5, 6, 4 };
        int k = 2;
        System.out.println(kthLargestElement.findKthLargest(nums, k));
        System.out.println(kthLargestElement.quickSelect(nums, nums.length - k, 0, nums.length - 1));
    }
}
