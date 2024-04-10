package Questions.Graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] adj = new List[numCourses];
        int[] degree = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int[] pair : prerequisites) {
            int course = pair[0];
            int preReq = pair[1];
            adj[preReq].add(course);
            degree[course]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; ++i) {
            if (degree[i] == 0) {
                q.add(i);
            }
        }
        int count = 0;

        while (!q.isEmpty()) {
            int node = q.poll();
            count++;
            for (int x : adj[node]) {
                if (--degree[x] == 0) {
                    q.add(x);
                }
            }

        }

        return count == numCourses;

    }

    public static void main(String[] args) {
        int numCourses = 2;
        int[][] prerequisites = { { 1, 0 } };
        CourseSchedule courseSchedule = new CourseSchedule();
        boolean result = courseSchedule.canFinish(numCourses, prerequisites);
        System.out.println("Can Finish: " + result);
    }
}
