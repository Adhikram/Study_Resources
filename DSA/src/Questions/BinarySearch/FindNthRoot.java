package Questions.BinarySearch;

/**
 * This class provides a method to calculate the nth root of a given number.
 */
public class FindNthRoot {

    /**
     * This method checks if the nth power of mid is equal to, less than, or greater
     * than m.
     *
     * @param mid The number to be raised to the power n.
     * @param n   The power to which mid is to be raised.
     * @param m   The number to be compared with the nth power of mid.
     * @return 1 if the nth power of mid is equal to m, 0 if it is less than m, and
     *         2 if it is greater than m.
     */
    public static int func(int mid, int n, int m) {
        long ans = 1;
        for (int i = 1; i <= n; i++) {
            ans = ans * mid;
            if (ans > m)
                return 2;
        }
        if (ans == m)
            return 1;
        return 0;
    }

    /**
     * This method calculates the nth root of a given number using binary search.
     *
     * @param n The root to be calculated.
     * @param m The number for which the nth root is to be calculated.
     * @return The nth root of the given number, or -1 if it does not exist.
     */
    public static int NthRoot(int n, int m) {
        // Use binary search on the answer space:
        int low = 1, high = m;
        while (low <= high) {
            int mid = (low + high) / 2;
            int midN = func(mid, n, m);
            if (midN == 1) {
                return mid;
            } else if (midN == 0) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }
    /*
     * Time Complexity: O(logM)
     */
    public static void main(String[] args) {
        int n = 2, m = 16;
        int ans = NthRoot(n, m);
        if (ans != -1) {
            System.out.println("The " + n + "th root of " + m + " is: " + ans);
        } else {
            System.out.println("No " + n + "th root found for " + m);
        }
    }
}