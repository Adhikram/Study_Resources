package Questions.Array;

public class MaxPrimeDifference {
    public int[] getPrimeHash(int n) {
        int[] prime = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            prime[i] = 1;
        }
        for (int i = 2; i * i <= n; i++) {
            if (prime[i] == 1) {
                for (int j = i * i; j <= n; j += i) {
                    prime[j] = 0;
                }
            }
        }
        return prime;
    }
    public int maximumPrimeDifference(int[] nums) {
        int result = 0;
        int start = 0;
        int end = nums.length - 1;
        int[] prime = getPrimeHash(100);
        while(start < end){
            if( prime[nums[start]] == 1 &&  prime[nums[start]] ==  prime[nums[end]]){
                result = Math.max(result, end - start);
                break;
            }else if(prime[nums[start]] == 1){
                end--;
            }else{
                start++;
            }
        }
        return Math.max(result, end - start);
    }
}
