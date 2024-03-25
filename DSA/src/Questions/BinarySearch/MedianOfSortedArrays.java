package Questions.BinarySearch;

public class MedianOfSortedArrays {
    // Method to find the median of two sorted arrays
    public static double median(int[] a, int[] b) {
        int n1 = a.length, n2 = b.length;
        // If the first array is bigger than the second, swap the arrays
        if (n1 > n2)
            return median(b, a);

        int n = n1 + n2; // Total length of the two arrays
        int left = (n1 + n2 + 1) / 2; // Length of the left half of the combined array

        // Apply binary search on the smaller array
        int low = 0, high = n1;
        while (low <= high) {
            int mid1 = (low + high) / 2; // Middle index of the first array
            int mid2 = left - mid1; // Middle index of the second array

            // Calculate l1, l2, r1 and r2
            // If we find nothing then just help the comparison by setting them to min and max
            int l1 = (mid1 > 0) ? a[mid1 - 1] : Integer.MIN_VALUE; // Biggest Element in the first array left part
            int l2 = (mid2 > 0) ? b[mid2 - 1] : Integer.MIN_VALUE; // Biggest Element in the second array left part
            int r1 = (mid1 < n1) ? a[mid1] : Integer.MAX_VALUE; // Smallest Element in the first array right part
            int r2 = (mid2 < n2) ? b[mid2] : Integer.MAX_VALUE; // Smallest Element in the second array right part

            // If the elements just before the middle in both arrays are less than or equal
            // to the middle elements
            if (l1 <= r2 && l2 <= r1) {
                // If the total length of the combined array is odd, return the maximum of the
                // elements just before the middle
                if (n % 2 == 1) {
                    return Math.max(l1, l2);
                } else {
                    // If the total length is even, return the average of the maximum of the
                    // elements just before the middle and the minimum of the middle elements
                    return ((double) (Math.max(l1, l2) + Math.min(r1, r2))) / 2.0;
                }
            } else if (l1 > r2) {
                // If the element just before the middle in the first array is greater than the
                // middle element in the second array, search in the lower half of the first
                // array
                high = mid1 - 1;
            } else {
                // If the element just before the middle in the second array is greater than the
                // middle element in the first array, search in the upper half of the first
                // array
                low = mid1 + 1;
            }
        }
        return 0; // Dummy statement
    }

    // Main method
    public static void main(String[] args) {
        int[] a = { 1, 4, 7, 10, 12 };
        int[] b = { 2, 3, 6, 15 };
        // Find the median of the two sorted arrays
        System.out.println("The median of two sorted arrays is " + median(a, b));
    }
}