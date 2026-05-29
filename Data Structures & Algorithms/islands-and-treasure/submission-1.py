class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        visited = set()
        q = collections.deque()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append((0, i, j))
        
        while q:
            dist, i, j = q.popleft()
            visited.add((i, j))
            grid[i][j] = min(dist, grid[i][j])
            neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

            for ni, nj in neighbors:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > 0 and (ni, nj) not in visited:
                    q.append((dist+1, ni, nj))
