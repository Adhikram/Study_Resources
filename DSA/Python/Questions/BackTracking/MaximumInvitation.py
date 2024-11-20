"""
# Question: Maximum Number of Accepted Invitations
# Link: https://leetcode.com/problems/maximum-number-of-accepted-invitations/

# Find maximum possible number of accepted invitations in a class

# Time Complexity: O(n*m)
# Space Complexity: O(n)

# Algorithm:
# 1. Use DFS to find augmenting paths
# 2. Track matches between boys and girls
# 3. Handle invitation constraints
# 4. Maximize accepted invitations
"""

class MaximumInvitation:
    def maximum_invitations(self, grid: list[list[int]]) -> int:
        boys = len(grid)
        girls = len(grid[0])
        accepted_invitations = 0
        match = [-1] * girls
        
        def dfs(grid: list[list[int]], vis: list[bool], match: list[int], boy: int) -> bool:
            for girl in range(len(grid[boy])):
                if not vis[girl] and grid[boy][girl] == 1:
                    vis[girl] = True
                    if match[girl] == -1 or dfs(grid, vis, match, match[girl]):
                        match[girl] = boy
                        return True
            return False
            
        # Try matching each boy
        for boy in range(boys):
            vis = [False] * girls
            if dfs(grid, vis, match, boy):
                accepted_invitations += 1
                
        return accepted_invitations

def main():
    solution = MaximumInvitation()
    grid = [[1, 1, 1], [1, 0, 1], [0, 0, 1]]
    print(solution.maximum_invitations(grid))  # Expected output: 3

if __name__ == "__main__":
    main()
