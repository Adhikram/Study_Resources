package Questions.Array;

public class TrapRainWater {
    public int trap(int[] height) {
        int lMax = Integer.MIN_VALUE;
        int rMax = Integer.MIN_VALUE;
        int left = 0;
        int right = height.length - 1;
        int result = 0;
        while (left <= right) {
            lMax = Math.max(lMax, height[left]);
            rMax = Math.max(rMax, height[right]);
            // If the current Tower is the max we will not get water from here
            // we need the water margin from the smaller tower to the present tower
            result += (lMax < rMax) ? lMax - height[left++] : rMax - height[right--];
        }
        return result;
    }

    public static void main(String[] args) {
        TrapRainWater trapRainWater = new TrapRainWater();
        int[] height = { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
        System.out.println(trapRainWater.trap(height));
    }
}
