class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        q = collections.deque()
        res = 0
        count = 0
            
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append((i+1,j))
                    q.append((i-1,j))
                    q.append((i,j+1))
                    q.append((i,j-1))
                elif grid[i][j] == 1:
                    count += 1
        
        while q and count > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                if i < 0 or i == M or j < 0 or j == N or grid[i][j] != 1:
                    continue
                
                grid[i][j] = 2
                count -= 1
                q.append((i+1,j))
                q.append((i-1,j))
                q.append((i,j+1))
                q.append((i,j-1))
            res += 1

        if count > 0:
            return -1
        return res
