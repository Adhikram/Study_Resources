package Questions.Graph;

/*
https://leetcode.com/problems/parallel-courses-ii/description/
 You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei. Also, you are given the integer k.

In one semester, you can take at most k courses as long as you have taken all the prerequisites in the previous semesters for the courses you are taking.

Return the minimum number of semesters needed to take all courses. The testcases will be generated such that it is possible to take every course.

 

Example 1:


Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
Output: 3
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 2 and 3.
In the second semester, you can take course 1.
In the third semester, you can take course 4.
Example 2:


Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4
Explanation: The figure above represents the given graph.
In the first semester, you can only take courses 2 and 3 since you cannot take more than two per semester.
In the second semester, you can take course 4.
In the third semester, you can take course 1.
In the fourth semester, you can take course 5.
 

Constraints:

1 <= n <= 15
1 <= k <= n
0 <= relations.length <= n * (n-1) / 2
relations[i].length == 2
1 <= prevCoursei, nextCoursei <= n
prevCoursei != nextCoursei
All the pairs [prevCoursei, nextCoursei] are unique.
The given graph is a directed acyclic graph.
 */
public class ParallelCourses2 {
    public int minNumberOfSemesters(int n, int[][] relations, int k) {

        // total courses mask
        int course_mask = (1 << n) - 1;

        this.dp = new Integer[course_mask + 1];

        return helper(n, relations, course_mask, k);
    }

    Integer dp[];

    int helper(int n, int[][] relations, int course_mask, int k) {

        // if all courses are visited
        if (course_mask == 0)
            return 0;

        if (dp[course_mask] != null)
            return dp[course_mask];

        // calculating indegree
        int indeg[] = new int[n];
        for (int rel[] : relations) {
            int u = rel[0] - 1;
            int v = rel[1] - 1;
            if (isBitOn(course_mask, u))
                indeg[v]++;
        }

        // mask for total available course to take this semester
        int avail_course_mask = 0;
        for (int i = 0; i < indeg.length; i++) {
            if (indeg[i] == 0 && isBitOn(course_mask, i))
                avail_course_mask = setKthBit(avail_course_mask, i);
        }

        // total available course in this semester
        int total_available_course_this_sem = countSetBits(avail_course_mask);

        if (total_available_course_this_sem <= k) {
            int newMask = (course_mask ^ avail_course_mask);
            return dp[course_mask] = 1 + helper(n, relations, newMask, k);
        }

        // Generating all permutation of avail_course_mask in which K bit is ON.
        int min = n;
        for (int subs = avail_course_mask; subs > 0; subs = (subs - 1) & avail_course_mask) {
            if (countSetBits(subs) == k) {
                int newMask = (course_mask ^ subs);
                int temp = 1 + helper(n, relations, newMask, k);
                min = Math.min(min, temp);
            }
        }

        return dp[course_mask] = min;
    }

    boolean isBitOn(int num, int k) {
        return (num & (1 << k)) > 0;
    }

    int setKthBit(int num, int k) {
        return (num ^ (1 << k));
    }

    int countSetBits(int num) {
        int count = 0;
        while (num != 0) {
            num &= (num - 1);
            count++;
        }
        return count;
    }

   public static void main(String[] args) {
        int n = 4;
        int[][] relations = { { 2, 1 }, { 3, 1 }, { 1, 4 } };
        int k = 2;
        ParallelCourses2 parallelCourses2 = new ParallelCourses2();
        System.out.println(parallelCourses2.minNumberOfSemesters(n, relations, k));
   }
}
