class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set([])
            for j in range(len(board[0])):
                if board[i][j].isalnum():
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        for j in range(len(board)):
            seen = set([])
            for i in range(len(board[0])):
                if board[i][j].isalnum():
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        for k in range(len(board) // 3):
            for l in range(len(board[0]) // 3):
                seen = set([])
                for i in range(3*k, 3*k + 3):
                    for j in range(3*l, 3*l + 3):
                        if board[i][j].isalnum():
                            if board[i][j] in seen:
                                return False
                            seen.add(board[i][j])
        
        return True
