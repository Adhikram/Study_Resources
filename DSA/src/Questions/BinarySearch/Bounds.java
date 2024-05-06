package Questions.BinarySearch;

public class Bounds {
    public static int lowerBound(int []arr, int n, int x) {
        int low = 0, high = n - 1;
        int ans = n;

        while (low <= high) {
            int mid = (low + high) / 2;
            // maybe an answer
            if (arr[mid] >= x) {
                ans = mid;
                //look for smaller index on the left
                high = mid - 1;
            } else {
                low = mid + 1; // look on the right
            }
        }
        return high + 1; // ans
    }
    public static int upperBound(int[] arr, int x, int n) {
        int low = 0, high = n - 1;
        int ans = n;

        while (low <= high) {
            int mid = (low + high) / 2;
            // maybe an answer
            if (arr[mid] <= x) {
                ans = mid;
                //look for smaller index on the left
                low = mid + 1; // look on the right
            } else {
                high = mid - 1;
            }
        }
        return low - 1; // ans
    }
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 3, 3, 5, 5, 5, 5, 5, 7};
        int n = arr.length;
        int x = 5;
        System.out.println(lowerBound(arr, n, x));
        System.out.println(upperBound(arr, x, n));
    }
}
