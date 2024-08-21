package Questions.Array;

public class KadensAlgo {
    static int kadensAlgo(int[] arr) {
        int maxSum = Integer.MIN_VALUE;
        int curSum = 0;
        for (int i : arr) {
            curSum += i;
            maxSum = Math.max(maxSum, curSum);
            curSum = Math.max(curSum, 0);
        }
        return maxSum;
    }
    public static void main(String[] args) {
        int[] arr = {1, -2, 3, -9, 5};
        System.out.println(kadensAlgo(arr));
    }
}
