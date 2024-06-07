package Questions.BinarySearch;

public class KthElement {
    // Method to find the kth element in the union of two sorted arrays
    static int solve(int[] array1, int[] array2, int m, int n, int k) {
        int p1 = 0, p2 = 0, counter = 0, answer = 0;

        // Traverse both arrays
        while (p1 < m && p2 < n) {
            // If we have found k elements, break
            if (counter == k)
                break;
                // If current element of array1 is smaller, increment p1
            else if (array1[p1] < array2[p2]) {
                answer = array1[p1];
                ++p1;
            }
            // If current element of array2 is smaller, increment p2
            else {
                answer = array2[p2];
                ++p2;
            }
            // Increment the count of total elements
            ++counter;
        }
        // If we have not found k elements, check the remaining elements in the array
        // which has not been fully traversed
        if (counter != k) {
            if (p1 != m - 1)
                answer = array1[k - counter];
            else
                answer = array2[k - counter];
        }
        // Return the kth element
        return answer;
    }

    // Method to find the kth element in the union of two sorted arrays using binary
    // search
    static int BinarySearch(int[] arr1, int[] arr2, int m, int n, int k) {
        // If the size of the first array is greater than the second one, swap them
        if (m > n) {
            return BinarySearch(arr2, arr1, n, m, k);
        }

        int low = 0, high = Math.min(k, n);
        if (k > n) {
            high = m + n;
        }

        while (low <= high) {
            int cut1 = (low + high) >> 1;
            // Calculate the cut position in the second array
            int cut2 = k - cut1;
//            System.out.println("Low: " + low + " High: " + high + " Cut1: " + cut1 + " Cut2: " + cut2);
            int l1 = cut1 == 0 ? Integer.MIN_VALUE : (cut1 >= m) ? arr1[m - 1] : arr1[cut1 - 1];
            int l2 = cut2 == 0 ? Integer.MIN_VALUE : (cut2 >= n) ? arr2[n - 1] : arr2[cut2 - 1];
            int r1 = cut1 >= m ? Integer.MAX_VALUE : arr1[cut1];
            int r2 = cut2 >= n ? Integer.MAX_VALUE : arr2[cut2];
//            System.out.println("Values: L1 " + l1 + " L2 " + l2 + " R1 " + r1 + " R2 " + r2);

            // If the elements at the cut positions in both arrays are in the correct order,
            // return the maximum of them
            if (l1 <= r2 && l2 <= r1) {
                return Math.max(l1, l2);
            }
            // If the element at the cut position in the first array is greater, move
            // towards left in the first array
            else if (l1 > r2) {
                high = cut1 - 1;
            }
            // If the element at the cut position in the second array is greater, move
            // towards right in the first array
            else {
                low = cut1 + 1;
            }
        }
        // If no element is found, return -1
        return -1;
    }

    /*
     * Time Complexity : log(min(m,n)) Space Complexity : O(1)
     */
    // Main method
    public static void main(String[] args) {
        int[] array1 = {2, 3, 6, 7, 9};
        int[] array2 = {1, 4, 8, 10};
        int m = array1.length;
        int n = array2.length;
        int k = 10;
        // Find the kth element in the union of the two sorted arrays
        System.out.println(solve(array1, array2, m, n, k));
        // Find the kth element in the union of the two sorted arrays using binary
        // search
        System.out.println(BinarySearch(array1, array2, m, n, k));
    }
}