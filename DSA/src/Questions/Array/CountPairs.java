package Questions.Array;

import java.util.HashMap;

public class CountPairs {
    public static int countPairsOP(int[] a, int[] b) {
        int result = 0;
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < a.length; i++){
            int diff = a[i] + b[i];
            map.put(diff, map.getOrDefault(diff, 0) + 1);
            result += map.get(diff);
        }

        return result;
    }

    public static void main(String[] args) {
        int[] a = {2, -2, 5, 3};
        int[] b = {1, 5, -1, 1};
        System.out.println(countPairsOP(a, b)); // Output should be 6
    }
}
