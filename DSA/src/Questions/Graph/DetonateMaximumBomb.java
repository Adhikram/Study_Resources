package Questions.Graph;

import java.util.LinkedList;
import java.util.Queue;

/*
https://leetcode.com/problems/detonate-the-maximum-bombs/description/
 You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

 

Example 1:


Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
Example 2:


Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
Example 3:


Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.
 

Constraints:

1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 105
 */
public class DetonateMaximumBomb {
    public int maximumDetonation(int[][] bombs) {
        int max = 0;
        // iterate through each bomb and keep track of max
        for (int i = 0; i < bombs.length; i++) {
            max = Math.max(max, getMaxBFS(bombs, i));
        }
        return max;
    }

    private int getMaxBFS(int[][] bombs, int index) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] seen = new boolean[bombs.length];

        seen[index] = true;
        queue.offer(index);

        int count = 1; // start from 1 since the first added bomb can detonate itself

        while (!queue.isEmpty()) {
            int currBomb = queue.poll();
            for (int j = 0; j < bombs.length; j++) { // search for bombs to detonate
                if (!seen[j] && isInRange(bombs[currBomb], bombs[j])) {
                    seen[j] = true;
                    count++;
                    queue.offer(j);
                }
            }
        }

        return count;
    }

    // use the distance between two points formula
    // then check if curr bomb radius is greater than the distance; meaning we can
    // detonate the second bombs
    private boolean isInRange(int[] point1, int[] point2) {
        long dx = point1[0] - point2[0], dy = point1[1] - point2[1], radius = point1[2];
        long distance = dx * dx + dy * dy;
        return distance <= radius * radius;
    }

    public static void main(String[] args) {
        DetonateMaximumBomb obj = new DetonateMaximumBomb();
        int[][] bombs = { { 0, 0, 1 }, { 1, 0, 1 }, { 2, 0, 1 }, { 3, 0, 1 }, { 4, 0, 1 }, { 5, 0, 1 }, { 6, 0, 1 },
                { 7, 0, 1 }, { 8, 0, 1 }, { 9, 0, 1 } };
        System.out.println(obj.maximumDetonation(bombs));
    }
}
