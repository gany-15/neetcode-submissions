class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        box = int(math.sqrt(n))

        rows = [0] * n
        cols = [0] * n
        boxes = [0] * n

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                
                mask = 1 << int(board[i][j])
                idx = box * (i // box) + (j // box)
                
                if (rows[i] & mask) or (cols[j] & mask) or (boxes[idx] & mask):
                    return False
                
                rows[i] |= mask
                cols[j] |= mask
                boxes[idx] |= mask
        
        return True
