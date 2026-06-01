class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        seen = set()
        res = 0

        def dfs(i, j):
            if -1 < i < M and -1 < j < N and grid[i][j] == 1 and (i, j) not in seen:
                seen.add((i, j))
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return 0
                

        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i, j))
        
        return res
