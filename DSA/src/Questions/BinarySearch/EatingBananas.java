package Questions.BinarySearch;

public class EatingBananas {
    // Method to find the maximum value in an array
    public static int findMax(int[] v) {
        int maxi = Integer.MIN_VALUE;
        int n = v.length;
        // Loop through the array to find the maximum value
        for (int i = 0; i < n; i++) {
            maxi = Math.max(maxi, v[i]);
        }
        return maxi;
    }

    // Method to calculate the total hours needed to eat all bananas at a given rate
    public static int calculateTotalHours(int[] v, int hourly) {
        int totalH = 0;
        int n = v.length;
        // Loop through the array and add the hours needed to eat each pile of bananas
        for (int i = 0; i < n; i++) {
            totalH += Math.ceil((double) (v[i]) / (double) (hourly));
        }
        return totalH;
    }

    // Method to find the minimum rate at which all bananas can be eaten within a
    // given number of hours
    public static int minimumRateToEatBananas(int[] v, int h) {
        int low = 1, high = findMax(v);

        // Apply binary search to find the minimum rate
        while (low <= high) {
            int mid = (low + high) / 2;
            int totalH = calculateTotalHours(v, mid);
            // If the total hours needed at the current rate is less than or equal to the
            // given hours, search in the lower half
            if (totalH <= h) {
                high = mid - 1;
            } else { // Else, search in the upper half
                low = mid + 1;
            }
        }
        return low;
    }

    // Main method
    public static void main(String[] args) {
        int[] v = { 7, 15, 6, 3 };
        int h = 8;
        // Find the minimum rate at which Koko can eat all bananas within 8 hours
        int ans = minimumRateToEatBananas(v, h);
        // Print the result
        System.out.println("Koko should eat at least " + ans + " bananas/hr.");
    }
}