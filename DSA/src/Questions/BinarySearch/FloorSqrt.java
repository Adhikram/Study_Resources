package Questions.BinarySearch;

import java.math.BigInteger;

public class FloorSqrt {
    public static int floorSqrt(int n) {
        int low = 1, high = n;
        //Binary search on the answers:
        while (low <= high) {
            long mid = (low + high) / 2;
            long val = mid * mid;
            if (val <= (long)(n)) {
                //eliminate the left half:
                low = (int)(mid + 1);
            } else {
                //eliminate the right half:
                high = (int)(mid - 1);
            }
        }
        return high;
    }
    public static int floorSqrt2(BigInteger n) {
        BigInteger low = BigInteger.ONE, high = n;
        //Binary search on the answers:
        while (low.compareTo(high) <= 0) {
            BigInteger mid = low.add(high).divide(BigInteger.valueOf(2));
            BigInteger val = mid.multiply(mid);
            if (val.compareTo(n) <= 0) {
                //eliminate the left half:
                low = mid.add(BigInteger.ONE);
            } else {
                //eliminate the right half:
                high = mid.subtract(BigInteger.ONE);
            }
        }
        return high.intValue();
    }

    public static void main(String[] args) {
        int n = 28;
        int ans = floorSqrt(n);
        System.out.println("The floor of square root of " + n + " is: " + ans);
        BigInteger n2 = new BigInteger("280909798098649746987698764780856029376593");
        int ans2 = floorSqrt2(n2);
        System.out.println("The floor of square root of " + n2 + " is: " + ans2);
    }
}
