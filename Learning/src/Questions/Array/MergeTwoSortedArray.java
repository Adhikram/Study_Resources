package Questions.Array;

public class MergeTwoSortedArray {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int final_size = nums1.length - 1;
        m--;
        n--;
        while (m > -1 && n > -1) {
            if (nums1[m] < nums2[n]) {
                int temp = nums1[final_size];
                nums1[final_size--] = nums2[n];
                nums2[n--] = temp;
            } else {
                int temp = nums1[final_size];
                nums1[final_size--] = nums1[m];
                nums1[m--] = temp;
            }
        }
        for (int k = 0; k < nums1.length; k++) {
            System.out.print(nums1[k] + " ");
        }
        System.out.println("");
        for (int k = 0; k < nums2.length; k++) {
            System.out.print(nums2[k] + " ");
        }
        while (n > -1) {
            int temp = nums1[final_size];
            nums1[final_size--] = nums2[n];
            nums2[n--] = temp;
        }
    }

    public static void main(String[] args) {
        int[] nums1 = new int[] { 1, 2, 3, 0, 0, 0 };
        int[] nums2 = new int[] { 2, 5, 6 };
        merge(nums1, 3, nums2, 3);
    }
}
