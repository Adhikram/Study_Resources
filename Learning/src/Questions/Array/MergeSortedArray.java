package Questions.Array;

public class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0;
        int j = 0;
        if (m == 0) {
            nums1 = nums2;
        }
        while (i < m && j < n) {
            // System.out.println(nums1[i] + " " + i + " " + j + " " + nums2[j]);
            // for (int k = 0; k < nums1.length; k++) {
            //     System.out.print(nums1[k] + " ");
            // }
            // System.out.println("");
            // for (int k = 0; k < nums2.length; k++) {
            //     System.out.print(nums2[k] + " ");
            // }
            // System.out.println("");
            // System.out.println(nums1.toString());
            // System.out.println(nums2.toString());
            if (nums1[i] == 0) {
                nums1[i] = nums2[j];
                j++;
                i++;
            } else {
                if (nums1[i] > nums2[j]) {
                    int temp = nums1[i];
                    nums1[i] = nums2[j];
                    nums2[j] = temp;
                }
                i++;
            }
        }
    }
}
