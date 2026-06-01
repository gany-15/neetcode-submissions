class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        seen = set()

        def dfs(i, j):
            if -1 < i < len(grid) and -1 < j < len(grid[0]) and grid[i][j] == '1' and (i, j) not in seen:
                seen.add((i, j))
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                elif (i, j) not in seen:
                    dfs(i, j)
                    count += 1
        
        return count
