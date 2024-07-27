package Questions.BackTracking;

import java.util.Arrays;
/*
https://leetcode.com/problems/maximum-number-of-accepted-invitations/description/
 There are m boys and n girls in a class attending an upcoming party.

You are given an m x n integer matrix grid, where grid[i][j] equals 0 or 1. If grid[i][j] == 1, then that means the ith boy can invite the jth girl to the party. A boy can invite at most one girl, and a girl can accept at most one invitation from a boy.

Return the maximum possible number of accepted invitations.

 

Example 1:

Input: grid = [[1,1,1],
               [1,0,1],
               [0,0,1]]
Output: 3
Explanation: The invitations are sent as follows:
- The 1st boy invites the 2nd girl.
- The 2nd boy invites the 1st girl.
- The 3rd boy invites the 3rd girl.
Example 2:

Input: grid = [[1,0,1,0],
               [1,0,0,0],
               [0,0,1,0],
               [1,1,1,0]]
Output: 3
Explanation: The invitations are sent as follows:
-The 1st boy invites the 3rd girl.
-The 2nd boy invites the 1st girl.
-The 3rd boy invites no one.
-The 4th boy invites the 2nd girl.
Time Complexity: O(n*m)
Space Complexity: O(n)
 */
public class MaximumNumberOfInvitation {
    public int maximumInvitations(int[][] grid) {
        int boys = grid.length;
        int girls = grid[0].length;
        int acceptedInvitations = 0;
        int[] match = new int[girls];
        Arrays.fill(match, -1);
        for (int boy = 0; boy < boys; boy++) {
            boolean[] vis = new boolean[girls];
            if (dfs(grid, vis, match, boy)) {
                acceptedInvitations++;
            }
        }
        return acceptedInvitations;
    }

    public boolean dfs(int[][] grid, boolean[] vis, int[] match, int boy) {
        for (int girl = 0; girl < grid[boy].length; girl++) {
            if (!vis[girl] && grid[boy][girl] == 1) {
                vis[girl] = true;
                // dfs call is to adjust the prev boy matching, if prev boy can be matched to a
                // new girl
                if (match[girl] == -1 || dfs(grid, vis, match, match[girl])) {
                    match[girl] = boy;
                    return true;
                }
            }
        }
        return false;
    }
    public static void main(String[] args) {
        MaximumNumberOfInvitation maximumNumberOfInvitation = new MaximumNumberOfInvitation();
        int[][] grid = { { 1, 1, 1 }, { 1, 0, 1 }, { 0, 0, 1 } };
        System.out.println(maximumNumberOfInvitation.maximumInvitations(grid));
    }
}