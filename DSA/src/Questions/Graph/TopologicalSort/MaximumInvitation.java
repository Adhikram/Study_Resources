package Questions.Graph.TopologicalSort;

import java.util.LinkedList;
import java.util.Queue;

/*
https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/description/
 A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

 

Example 1:


Input: favorite = [2,2,1,2]
Output: 3
Explanation:
The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
The maximum number of employees that can be invited to the meeting is 3. 
Example 2:

Input: favorite = [1,2,0]
Output: 3
Explanation: 
Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
The seating arrangement will be the same as that in the figure given in example 1:
- Employee 0 will sit between employees 2 and 1.
- Employee 1 will sit between employees 0 and 2.
- Employee 2 will sit between employees 1 and 0.
The maximum number of employees that can be invited to the meeting is 3.
Example 3:


Input: favorite = [3,0,1,4,1]
Output: 4
Explanation:
The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
So the company leaves them out of the meeting.
The maximum number of employees that can be invited to the meeting is 4.
 

Constraints:

n == favorite.length
2 <= n <= 105
0 <= favorite[i] <= n - 1
favorite[i] != i
Time complexity: O(n)
Space complexity: O(n)
 */
public class MaximumInvitation {
    public int maximumInvitations(int[] favorite) {
        int n = favorite.length;
        int[] inDegree = new int[n];
        for (int f : favorite) {
            inDegree[f]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        int[] longestChain = new int[n];
        boolean[] visited = new boolean[n];

        // Add nodes with zero in-degree to the queue
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }

        // Process nodes in topological order
        while (!queue.isEmpty()) {
            int node = queue.poll();
            visited[node] = true;
            int fav = favorite[node];
            longestChain[fav] = Math.max(longestChain[fav], longestChain[node] + 1);
            if (--inDegree[fav] == 0) {
                queue.offer(fav);
            }
        }

        // Detect cycles and compute results
        int maxCycleSize = 0;
        int sumOfChains = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int cycleLength = 0;
                int chainLength1 = 0, chainLength2 = 0;
                int node = i;

                while (!visited[node]) {
                    visited[node] = true;
                    cycleLength++;
                    node = favorite[node];
                }
                // Need to find the two length cycle and we can add longest chain with both of
                // them

                if (cycleLength == 2) {
                    chainLength1 = longestChain[i];
                    chainLength2 = longestChain[favorite[i]];
                    // sum off all 2 length cycle ends
                    sumOfChains += chainLength1 + chainLength2 + cycleLength;
                } else {
                    maxCycleSize = Math.max(maxCycleSize, cycleLength);
                }
            }
        }

        return Math.max(maxCycleSize, sumOfChains);
    }

    public static void main(String[] args) {
        MaximumInvitation maximumInvitation = new MaximumInvitation();
        int[] favorite = { 1, 2, 3, 4, 5, 0 };
        System.out.println(maximumInvitation.maximumInvitations(favorite));
    }
}
