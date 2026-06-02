class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M, N = len(grid), len(grid[0])
        q = collections.deque()

        def bfs():
            seen = set()
            while q:
                i, j, k = q.popleft()
                if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] < 1 or (i,j) in seen:
                    continue
                
                seen.add((i, j))
                grid[i][j] = min(k, grid[i][j])
                q.append((i+1,j,k+1))
                q.append((i-1,j,k+1))
                q.append((i,j+1,k+1))
                q.append((i,j-1,k+1))

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    q.append((i+1,j,1))
                    q.append((i-1,j,1))
                    q.append((i,j+1,1))
                    q.append((i,j-1,1))
        bfs()
