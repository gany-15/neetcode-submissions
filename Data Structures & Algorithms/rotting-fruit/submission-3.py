class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        q = collections.deque()
        self.res = 0

        def bfs():
            while q:
                i, j, k = q.popleft()
                if i < 0 or i == M or j < 0 or j == N or grid[i][j] != 1:
                    continue
                
                grid[i][j] = 2
                k += 1
                self.res = max(self.res, k)
                q.append((i+1,j,k))
                q.append((i-1,j,k))
                q.append((i,j+1,k))
                q.append((i,j-1,k))

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append((i+1,j,0))
                    q.append((i-1,j,0))
                    q.append((i,j+1,0))
                    q.append((i,j-1,0))
        bfs()

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return -1
        return self.res
