package Questions.Array;

public class KadensAlgo {
    static int kadensAlgo(int[] arr) {
        int maxSum = Integer.MIN_VALUE;
        int currSum = 0;
        for (int i : arr) {
            currSum += i;
            maxSum = Math.max(maxSum, currSum);
            currSum = Math.max(currSum, 0);
        }
        return maxSum;
    }
    public static void main(String[] args) {
        int[] arr = {1, -2, 3, -9, 5};
        System.out.println(kadensAlgo(arr));
    }
}
