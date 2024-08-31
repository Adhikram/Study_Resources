package Questions.Array;

import java.util.PriorityQueue;
import java.util.Random;

/*
 https://leetcode.com/problems/kth-largest-element-in-an-array/description/

 Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
 */
public class kthLargestElement {
    private Random rand = new Random();

    public int quickSelect(int[] nums, int k, int left, int right) {
        if (left == right) {
            return nums[left];
        }

        int pivotIndex = left + rand.nextInt(right - left + 1);
        pivotIndex = partition(nums, left, right, pivotIndex);

        if (k == pivotIndex) {
            return nums[k];
        } else if (k < pivotIndex) {
            return quickSelect(nums, k, left, pivotIndex - 1);
        } else {
            return quickSelect(nums, k, pivotIndex + 1, right);
        }
    }

    private int partition(int[] nums, int left, int right, int pivotIndex) {
        int pivot = nums[pivotIndex];
        swap(nums, pivotIndex, right);
        int storeIndex = left;

        for (int i = left; i < right; i++) {
            if (nums[i] < pivot) {
                swap(nums, storeIndex, i);
                storeIndex++;
            }
        }
        swap(nums, right, storeIndex);
        return storeIndex;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
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
