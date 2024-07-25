package Questions.Graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/*
https://leetcode.com/problems/parallel-courses/description/
 You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

 

Example 1:


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.
Example 2:


Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.
 

Constraints:

1 <= n <= 5000
1 <= relations.length <= 5000
relations[i].length == 2
1 <= prevCoursei, nextCoursei <= n
prevCoursei != nextCoursei
All the pairs [prevCoursei, nextCoursei] are unique.
 */

//  Time complexity: O(V+E)
//  Space complexity: O(V+E)
public class ParallelCourses {
    public int minimumSemesters(int n, int[][] relations) {
        ArrayList<Integer>[] adj = new ArrayList[n + 1];
        int[] indegree = new int[n + 1];

        for (int[] rel : relations) {
            indegree[rel[1]]++;
            if (adj[rel[0]] == null) {
                adj[rel[0]] = new ArrayList();
            }
            adj[rel[0]].add(rel[1]);
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= n; i++)
            if (indegree[i] == 0)
                queue.offer(i);

        if (queue.isEmpty())
            return -1;

        int step = 0, visitedCount = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            step++;
            while (size-- > 0) {
                visitedCount++;
                Integer cur = queue.poll();
                if (adj[cur] != null) {
                    for (int k : adj[cur]) {
                        indegree[k]--;
                        if (indegree[k] == 0)
                            queue.offer(k);
                    }
                }

            }
        }

        return visitedCount == n ? step : -1;
    }

    public static void main(String[] args) {
        int n = 3;
        int[][] relations = { { 1, 3 }, { 2, 3 } };
        ParallelCourses parallelCourses = new ParallelCourses();
        int result = parallelCourses.minimumSemesters(n, relations);
        System.out.println("Minimum Semesters: " + result);
    }

}
